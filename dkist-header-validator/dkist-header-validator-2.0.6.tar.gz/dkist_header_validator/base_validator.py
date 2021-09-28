"""
Definition of the base objects for the creation of a spec validator
"""
import logging
import os
import pathlib
from io import BytesIO
from numbers import Integral
from numbers import Real
from pathlib import Path
from pathlib import PurePath
from typing import IO
from typing import List
from typing import Tuple
from typing import Type
from typing import Union

import astropy.time as t
import astropy.units as u
import numpy as np
import voluptuous as vol
from astropy.io import fits
from astropy.io.fits.hdu.hdulist import HDUList
from dkist_fits_specifications import spec214
from dkist_fits_specifications.utils import expand_naxis
from voluptuous.error import Invalid

from dkist_header_validator.exceptions import ReturnTypeException
from dkist_header_validator.exceptions import SpecSchemaDefinitionException
from dkist_header_validator.exceptions import SpecValidationException
from dkist_header_validator.exceptions import ValidationException
from dkist_header_validator.translator import translate_spec122_to_spec214_l0


logger = logging.getLogger(__name__)

__all__ = ["SpecValidator", "SpecSchema"]


class FormatInvalid(Invalid):
    """
    An value which does not match the schema format.
    """


class FormatValidator:
    """
    Validate that the format is valid.
    """

    supported_formats = ["isot", "unit"]

    def __init__(self, format_value):
        if format_value not in self.supported_formats:
            raise SpecSchemaDefinitionException(f"{format_value} is an unknown format to validate.")
        self.format_value = format_value

    def __call__(self, value):
        if self.format_value == "unit":
            try:
                return u.Unit(value, format="fits")
            except Exception:
                raise FormatInvalid(f"{value} is not a valid FITS unit")

        if self.format_value == "isot":
            try:
                return t.Time(value, format="fits")
            except Exception:
                raise FormatInvalid(f"{value} is not a valid FITS time")

    def __repr__(self):
        return f"FormatValidator(format='{self.format_value}')"


class FITSFloatInvalid(Invalid):
    """
    Validates a header value is a valid FITS float.

    This means it's not NaN or ±Inf.
    """


class FITSFloatValidator:
    """
    Validate a FITS floating point value.

    This validator assumes the type has also been validated independently.
    """

    def __call__(self, value):
        if not np.isfinite(value):
            raise FITSFloatInvalid(
                f"{value} is not finite, floats in a FITS header must be finite."
            )

        return value


class SpecSchema:
    """
    Define a schema that is used to validate FITS headers for a spec based upon structured definitions
    in YAML or dicts
    """

    # Schemas defined for a spec have the following structure per key
    definition_schema_definition = {
        vol.Required("required"): vol.Any(True, False),
        vol.Required("type"): vol.Any("int", "float", "str", "bool"),
        "values": list,
        "values_range": list,
        "expected": vol.Any(True, False),
        "expand": vol.Any(True, False),
        "format": vol.Any("unit", "isot"),
    }
    # Voluptuous schema instance used to validate the definitions
    definition_schema = vol.Schema(definition_schema_definition, extra=vol.ALLOW_EXTRA)

    def __init__(self, spec_schema_definitions: Union[Path, dict, List[dict]]):
        """
        Constructor for the SpecSchema which builds a voluptuous schema from
        specification definition files in YAML or dicts
        :param spec_schema_definitions: Definition of the spec's schema in one of the following forms
            - Dict definition of the spec schema
            - List of Dict definitions of the spec schema
            - Path to a YAML file defining the spec schema
            - Path to a directory containing YAML files defining spec schema
        """
        # convert spec schema definitions to a list of dicts
        self.spec_schema_definitions = self._parse_spec_schema_definitions(spec_schema_definitions)
        # validate the dict definition of the spec schema
        self._validate_spec_schema_definitions()

    @classmethod
    def _parse_spec_schema_definitions(cls, spec_schema: List[dict]) -> dict:
        """
        Convert from a list of dicts multiple formats to a dict
        :param spec_schema: Definition(s) of the spec's schema
        :return: Dictionary capturing the spec schema definition
        """

        # Test for proper types and non-emptiness
        if spec_schema:
            if all([isinstance(item, dict) and item for item in spec_schema]):
                schema = {key: schema for item in spec_schema for (key, schema) in item.items()}
                return schema
        # empty or not a known type
        raise SpecSchemaDefinitionException(
            "Schema definition is empty or is not a supported type",
            errors={
                "received": type(spec_schema),
                "expected": List[dict],
            },
        )

    def _validate_spec_schema_definitions(self) -> None:
        """
        Validate the spec schema definitions against the class schema for
        spec schema definitions and raise a SpecSchemaDefinitionException
        on failure
        :return: None
        """

        for key, spec_schema in self.spec_schema_definitions.items():
            schema_errors = {}
            try:
                self.definition_schema(spec_schema)
            except vol.MultipleInvalid as e:
                schema_errors = {error.path[0]: error.msg for error in e.errors}
            if schema_errors:
                logger.debug(
                    f"Errors during schema definition validation. key={key} errors={schema_errors}"
                )
                raise SpecSchemaDefinitionException(
                    f"Errors during schema definition validation. key={key}",
                    errors=schema_errors,
                )

    def expand_schema(self, headers) -> dict:
        """
        Expand schema indices using information from fits headers
        :param headers: Fits file headers whose values are to be used to know how to expand spec keys
        :return: schema dictionary
        """
        # 214 Expansion
        if {"DAAXES", "DEAXES", "DNAXIS"}.issubset(headers.keys()):
            # This function includes the expansion for NAXIS
            return spec214.expand_214_schema(self.spec_schema_definitions, **headers)

        # 122 Only expands "n" with NAXIS
        return expand_naxis(headers["NAXIS"], self.spec_schema_definitions)

    @staticmethod
    def generate_schema_for_key(key_schema):
        """
        Generate voluptuous schema for a key
        :param key_schema: Spec schema (from yml) used to generate voluptuous schema
        :return: Voluptuous schema for a key
        """
        type_map = {"int": Integral, "float": Real, "str": str, "bool": bool}

        checks = []
        # Always check type
        checks.append(type_map[key_schema.get("type")])

        def case_insenstive_values(value):
            allowed_values = key_schema.get("values")
            if key_schema.get("type") == "str":
                value = value.lower()
                allowed_values = [v.lower() for v in allowed_values]

            return vol.Any(*allowed_values)(value)

        def expand_values_range(value):
            min_value = key_schema.get("values_range")[0]
            try:
                max_value = key_schema.get("values_range")[1]
            except IndexError:
                max_value = None

            return vol.Range(min=min_value, max=max_value)(value)

        if key_schema.get("values"):
            checks.append(case_insenstive_values)

        if key_schema.get("values_range"):
            checks.append(expand_values_range)

        if "format" in key_schema:
            checks.append(FormatValidator(key_schema["format"]))

        if key_schema.get("type") == "float":
            checks.append(FITSFloatValidator())

        return vol.All(*checks)

    def _add_keys_to_schema(self, schema: dict) -> dict:
        schema_keys = {}  # keys to be added to voluptuous schema
        required_keys = {
            vol.Required(k): self.generate_schema_for_key(v)
            for k, v in schema.items()
            if v.get("required")
        }
        schema_keys.update(required_keys)
        remaining_keys = {
            k: self.generate_schema_for_key(v) for k, v in schema.items() if not v.get("required")
        }
        schema_keys.update(remaining_keys)
        return schema_keys

    def _check_for_expansion(self, headers):
        for value in self.spec_schema_definitions.values():
            # check the whole schema to see if there is an expand = True keyword
            if value["expand"]:
                # if there is an 'expand' keyword set to true in the schema, expand the whole spec schema
                expanded_schema = self.expand_schema(headers)
                return expanded_schema
        return self.spec_schema_definitions

    def _create_spec_schema(self, headers, extra) -> vol.Schema:
        """
        A voluptuous.spec_validator object to validate headers against.
        Constructed from Spec keywords.
        :param headers: Fits file headers
        :return: Voluptuous schema
        """

        spec_schema = {}

        schema = self._check_for_expansion(headers)
        spec_schema.update(self._add_keys_to_schema(schema))
        if extra:
            return vol.Schema(spec_schema, extra=vol.ALLOW_EXTRA)
        return vol.Schema(spec_schema)

    def __call__(self, headers: dict, extra) -> vol.Schema:
        """
        Validate headers against the instance spec schema
        raising voluptuous errors on failure
        :param headers: header dict to validate
        :return: vol.Schema
        """
        """for value in self.spec_schema_definitions.values():
            if value["values_range"]:
                pass"""

        spec_schema = self._create_spec_schema(headers, extra)
        return spec_schema(headers)


class SpecValidator:
    """
    Validates FITS Headers against a schema
    """

    def __init__(
        self,
        spec_schema: Union[Path, PurePath, dict, List[dict], SpecSchema],
        SchemaValidationException: Type[SpecValidationException] = SpecValidationException,
    ):
        """
        Constructor for the SpecValidator
        :param spec_schema: Definition of the spec's schema in one of the following forms
            - SpecSchema instance
            - Dict definition of the spec schema
            - List of Dict definitions of the spec schema
            - Path to a YAML file defining the spec schema
            - Path to a directory containing YAML files defining spec schema
        :param SchemaValidationException: SpecValidationException or subclass of SpecValidationException
            to raise if spec_validator validation fails
        """
        # Callable for validating a dict against the defined spec_validator
        if isinstance(spec_schema, SpecSchema):
            self.spec_schema = spec_schema
        else:
            self.spec_schema = SpecSchema(spec_schema)

        # Exception raised when spec validation fails
        self.SchemaValidationException = SchemaValidationException

    @staticmethod
    def _headers_to_dict(headers: Union[HDUList, dict, fits.header.Header, str, IO]) -> dict:
        """
        Convert headers from multiple types to a dict
        :param headers: Headers to convert to a dict
        :return: Dict of the headers
        """
        if isinstance(headers, dict):
            return headers
        if isinstance(headers, fits.header.Header):
            return dict(headers)
        if isinstance(headers, HDUList):
            if len(headers) > 1:
                return dict(headers[1].header)
            return dict(headers[0].header)

    def verify_headers(self, headers, extra) -> dict:
        """
        Validates file headers against the instance spec_validator
        :param headers: file headers
        :param extra: switch for validation to allow extra keys in schema
        :return: dict of headers
        :raises: SchemaValidationException
        """

        validation_errors = {}
        try:
            self.spec_schema(headers, extra)
        except vol.MultipleInvalid as e:
            for error in e.errors:
                value_str = "Required keyword not present"
                if error.path[0] in headers:
                    value_str = (
                        f"Actual value: {headers[error.path[0]]!r} {type(headers[error.path[0]])}"
                    )
                validation_errors[error.path[0]] = f"{error.msg}. {value_str}"
        # Raise exception if we have errors
        if validation_errors:
            missing_list = []
            badtype_list = []
            other_list = []

            for key in validation_errors.keys():
                if "required key not provided" in validation_errors[key]:
                    missing_list.append(key)
                elif "expected" in validation_errors[key]:
                    badtype_list.append(key)
                else:
                    other_list.append(key)
            # Log the bad keys
            for sublist, message in zip(
                [missing_list, badtype_list, other_list],
                [
                    "The following keys are missing:",
                    "The following keys have bad types:",
                    "The following keys have other errors:",
                ],
            ):
                if len(sublist) > 0:
                    logger.debug(f"\n{message}")
                    for k in sorted(sublist):
                        logger.debug(f"{str(k):<10}:\t{validation_errors[k]}")

            raise self.SchemaValidationException(errors=validation_errors)
        logger.debug("Schema validation succeeded")

        return headers

    def _validate_headers(
        self, input_headers: Union[HDUList, dict, fits.header.Header], extra
    ) -> Tuple[dict, dict]:
        """
        Validates open input headers against the instance spec_schema
        :param input_headers: The input headers to validate in the following formats:
            - HDUList object
            - fits.header.Header object
            - Dictionary of header keys and values
        :param extra: switch for validation to allow extra keys in schema
        :return: dictionary of verified headers to be used later
        """
        if isinstance(input_headers, HDUList):
            if len(input_headers) > 2:
                raise ValidationException(
                    "Too many HDUs in your HDUList! May only have two HDUs at most."
                )
        headers = self._headers_to_dict(input_headers)
        fits_cards = self._capture_fits_cards(headers)
        verified_headers = self.verify_headers(headers, extra)
        return verified_headers, fits_cards

    def _validate_file(self, input_headers: Union[str, IO], extra) -> Tuple[dict, dict, np.ndarray]:
        """
        Validates files against the astropy and then instance spec_schema
        :param input_headers: The input headers to validate in the following formats:
            - string file path
            - File like object
        :param extra: switch for validation to allow extra keys in schema
        :return: dictionary of verified headers to be used later
        """
        try:
            with fits.open(input_headers) as hdul:
                if len(hdul) > 2:
                    raise ValidationException(
                        "Too many HDUs in your HDUList! May only have two HDUs at most."
                    )
                # verify fits headers with astropy verify library
                hdul.verify("exception")
                # normalize headers into a dict
                try:
                    hdus = self._headers_to_dict(hdul[1].header)
                    data = hdul[1].data
                except IndexError:  # non-compressed
                    hdus = self._headers_to_dict(hdul[0].header)
                    data = hdul[0].data
                fits_cards = self._capture_fits_cards(hdus)
                verified_headers = self.verify_headers(hdus, extra)
                return verified_headers, fits_cards, data
        except (ValueError, FileNotFoundError, OSError, IndexError) as exc:
            logger.debug(f"Cannot parse headers: detail = {exc}")
            raise ValidationException(f"Cannot parse headers", errors={type(exc): str(exc)})

    @staticmethod
    def _return_hdulist(validated_headers, fits_cards) -> HDUList:
        """
        Returns validated headers as an HDUList
        :param validated_headers: Already validated/translated headers to be written out into
          an HDUList
        :param fits_cards: Any special cards to be included in the HDUList
        :return: HDUList
        """
        if isinstance(validated_headers, HDUList):
            return validated_headers
        temp_array: np.ndarray = np.ones((1, 1, 1), dtype=np.int16)
        new_hdu = fits.PrimaryHDU(temp_array, header=fits.Header())
        for (key, value) in validated_headers.items():
            new_hdu.header[key] = value
        for key in fits_cards:
            new_hdu.header[key] = str(fits_cards[key])
        new_hdu_list = fits.HDUList([new_hdu])
        return new_hdu_list

    @staticmethod
    def _return_dictionary(validated_headers, fits_cards) -> dict:
        """
        Returns validated headers as a dictionary
        :param validated_headers: Already validated/translated headers to be written out into
          a dictionary
        :param fits_cards: Any special cards to be included in the dictionary
        :return: dictionary
        """
        for key in fits_cards:
            validated_headers[key] = str(fits_cards[key])
        return validated_headers

    @staticmethod
    def _return_BytesIO(validated_headers, input_headers, data, fits_cards) -> BytesIO:
        """
        Returns validated headers as a BytesIO object
        :param validated_headers: Already validated/translated headers to be written out into
          the BytesIO object
        :param input_headers: original filepath or BytesIO object
        :param data: original data
        :param fits_cards: Any special cards to be included in the BytesIO object
        :return: BytesIO object
        """
        new_hdu = fits.PrimaryHDU(data, header=fits.Header())
        for (key, value) in validated_headers.items():
            new_hdu.header[key] = value
        for key in fits_cards:
            new_hdu.header[key] = str(fits_cards[key])
        new_hdu_list = fits.HDUList([new_hdu])
        return BytesIO(
            new_hdu_list.writeto(
                str(os.path.basename(input_headers)),
                overwrite=True,
                output_verify="exception",
                checksum=True,
            )
        )

    @staticmethod
    def _return_file(validated_headers, input_headers, data, fits_cards) -> (str, IO):
        """
        Returns validated headers as a FITS file
        :param validated_headers: Already validated/translated headers to be written out
          into a FITS file
        :param input_headers: original filepath or BytesIO object
        :param data: original data
        :param fits_cards: Any special cards to be included in the FITS file
        :return: FITS file
        """
        new_hdu = fits.PrimaryHDU(data, header=fits.Header())
        for (key, value) in validated_headers.items():
            new_hdu.header[key] = value
        for key in fits_cards:
            new_hdu.header[key] = str(fits_cards[key])
        new_hdu_list = fits.HDUList([new_hdu])
        new_hdu_list.writeto(
            str(os.path.basename(input_headers)),
            overwrite=True,
            output_verify="exception",
            checksum=True,
        )
        return Path(os.path.basename(input_headers))

    @staticmethod
    def _return_HDU(validated_headers, data, fits_cards):
        """
        Returns validated headers as an HDU
        :param validated_headers: Already validated/translated headers to be written out
          into a FITS file
        :param data: original data
        :param fits_cards: Any special cards to be included in the FITS file
        :return: HDU
        """
        new_hdu = fits.PrimaryHDU(data, header=fits.Header())
        for (key, value) in validated_headers.items():
            new_hdu.header[key] = value
        for key in fits_cards:
            new_hdu.header[key] = str(fits_cards[key])
        return new_hdu

    def _format_output(
        self, return_type, validated_headers, input_headers=None, data=None, fits_cards=None
    ):
        fits_cards = fits_cards or {}
        if return_type == Path:
            if data is None:
                raise ReturnTypeException("No data. Cannot write file.")
            return self._return_file(validated_headers, input_headers, data, fits_cards)
        if return_type == BytesIO:
            if data is None:
                raise ReturnTypeException("No data. Cannot write BytesIO object.")
            return self._return_BytesIO(validated_headers, input_headers, data, fits_cards)
        if return_type == dict:
            return self._return_dictionary(validated_headers, fits_cards)
        if return_type == HDUList:
            return self._return_hdulist(validated_headers, fits_cards)
        if return_type == fits.header.Header:
            return self._return_HDU(validated_headers, data, fits_cards).header
        if return_type == fits.PrimaryHDU:
            if data is None:
                raise ReturnTypeException("No data. Cannot write PrimaryHDU.")
            return self._return_HDU(validated_headers, data, fits_cards)

    def _capture_fits_cards(self, validated_headers) -> dict:
        """
        Pull special fits cards out of validated_headers dict.
        This is necessary for astropy header formatting.

        :param validated_headers: validated headers
        :return: fits_cards: dictionary containing special fits header keys and values
        """
        fits_cards = {}
        if "HISTORY" in validated_headers:
            fits_cards["HISTORY"] = str(validated_headers["HISTORY"])
            validated_headers.pop("HISTORY")
        if "COMMENT" in validated_headers:
            fits_cards["COMMENT"] = str(validated_headers["COMMENT"])
            validated_headers.pop("COMMENT")
        return fits_cards

    def validate(self, input_headers, return_type=HDUList, extra=True):
        """
        Validates against the instance spec_schema
        :param input_headers: The headers to validate in the following formats:
            - string file path
            - File like object
            - HDUList object
            - fits.header.Header object
            - Dictionary of header keys and values
        :param return_type: determines return type. Default is HDUList. May be one of:
            - dict
            - BytesIO
            - fits.header.Header
            - Path (file)
            - HDUList
            - fits.PrimaryHDU
        :param extra: switch for validation to allow extra keys in schema. Default is true, which will
        allow extra keys. Ingest validation should allow extra keys.
        :return: formatted headers
        :raises: SpecValidationException or subclass
        """
        if isinstance(input_headers, (dict, fits.header.Header, HDUList)):
            validated_headers, fits_cards = self._validate_headers(input_headers, extra)
            return self._format_output(
                return_type, validated_headers, input_headers, None, fits_cards
            )
        validated_headers, fits_cards, data = self._validate_file(input_headers, extra)
        return self._format_output(return_type, validated_headers, input_headers, data, fits_cards)

    def validate_and_translate_to_214_l0(self, input_headers, return_type=HDUList, extra=True):
        """
        Validates against the instance spec_schema and then translates to the spec214_l0 schema
        :param input_headers: The headers to validate in the following formats:
            - string file path
            - File like object
            - HDUList object
            - fits.header.Header object
            - Dictionary of header keys and values
        :param return_type: determines return type. Default is HDUList. May be one of:
            - dict
            - BytesIO
            - fits.header.Header
            - Path (file)
            - HDUList
            - fits.PrimaryHDU
        :param extra: switch for validation to allow extra keys in schema. Default is true, which will
        allow extra keys. Ingest validation should allow extra keys.
        :return: formatted 214 l0 headers
        :raises: SpecValidationException or subclass
        """
        if isinstance(input_headers, (dict, fits.header.Header, HDUList)):
            validated_headers, fits_cards = self._validate_headers(input_headers, extra)
            translated_headers = translate_spec122_to_spec214_l0(validated_headers)
            return self._format_output(return_type, translated_headers, None, None, fits_cards)
        else:
            validated_headers, fits_cards, data = self._validate_file(input_headers, extra)
            translated_headers = translate_spec122_to_spec214_l0(validated_headers)
            return self._format_output(
                return_type, translated_headers, input_headers, data, fits_cards
            )
