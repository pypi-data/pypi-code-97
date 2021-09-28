from typing import Mapping
from typing import Optional
from typing import Sequence
from typing import Union

import numpy as np
import pandas as pd
from pyspark.sql import DataFrame as pysparkDF

from tecton._internals import errors
from tecton._internals.feature_retrieval_internal import find_dependent_feature_set_items
from tecton._internals.utils import infer_timestamp
from tecton._internals.utils import is_bfc_mode_single
from tecton.interactive.data_frame import DataFrame
from tecton.interactive.data_frame import FeatureVector
from tecton.interactive.feature_package import FeaturePackage
from tecton.interactive.feature_service import FeatureService
from tecton.interactive.feature_set_config import FeatureSetConfig
from tecton.interactive.feature_view import FeatureView
from tecton.tecton_errors import TectonValidationError
from tecton_spark.feature_package_view import FPBackedFeaturePackageOrView
from tecton_spark.feature_package_view import FVBackedFeaturePackageOrView


def get_online_features(
    features: Union[FeatureService, Sequence[FeaturePackage]],
    join_keys: Optional[Mapping[str, Union[int, np.int_, str, bytes]]] = None,
    include_join_keys_in_response: bool = False,
    request_data: Optional[Mapping[str, Union[int, np.int_, str, bytes, float]]] = None,
) -> FeatureVector:
    if isinstance(features, FeatureService):
        return features.get_feature_vector(
            join_keys=join_keys,
            include_join_keys_in_response=include_join_keys_in_response,
            request_context_map=request_data,
        )
    elif isinstance(features, list):
        features_vector = FeatureVector([], [], [])
        for fp in features:
            features_vector._update(
                fp.get_feature_vector(
                    join_keys=join_keys,
                    include_join_keys_in_response=include_join_keys_in_response,
                    request_context_map=request_data,
                )
            )
        return features_vector
    else:
        raise TectonValidationError(f"Unexpected data type for features: {type(features)}")


def get_historical_features(
    features: Union[Sequence[FeaturePackage], Sequence[FeatureView], FeatureService],
    spine: Union[pysparkDF, pd.DataFrame],
    from_source: bool = False,
    save: bool = False,
    save_as: str = None,
    timestamp_key: Optional[str] = None,
) -> DataFrame:
    if not timestamp_key:
        timestamp_key = infer_timestamp(spine)

    if isinstance(features, FeatureService):
        return features.get_historical_features(
            spine=spine, timestamp_key=timestamp_key, from_source=from_source, save_dataset=save, save_as=save_as
        )
    elif isinstance(features, list):
        for feature in features:
            if not (isinstance(feature, FeaturePackage) or isinstance(feature, FeatureView)):
                raise TectonValidationError(
                    "The `features` parameter can only be " "a FeatureService, or a List of FeatureViews"
                )

        feature_set_config = FeatureSetConfig()
        for feature in features:
            if isinstance(feature, FeaturePackage):
                fpov = FPBackedFeaturePackageOrView(feature._proto)
            else:
                fpov = FVBackedFeaturePackageOrView(feature._proto)

                if from_source and is_bfc_mode_single(fpov):
                    raise errors.FP_BFC_SINGLE_FROM_SOURCE

                if feature._proto.HasField("on_demand_feature_view"):
                    inputs = find_dependent_feature_set_items(
                        feature._proto.pipeline.root,
                        visited_inputs={},
                        fv_id=feature.id,
                        workspace_name=feature.workspace,
                    )
                    feature_set_config._definitions_and_configs = feature_set_config._definitions_and_configs + inputs
            feature_set_config._add(fpov)
        return feature_set_config.get_feature_dataframe(spine, timestamp_key, use_materialized_data=not from_source)
    else:
        raise TectonValidationError(
            "The `features` parameter can only be " "a FeatureService, or a List of FeatureViews"
        )
