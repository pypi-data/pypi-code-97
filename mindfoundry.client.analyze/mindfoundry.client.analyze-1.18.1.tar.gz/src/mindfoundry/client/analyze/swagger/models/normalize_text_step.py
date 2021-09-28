from typing import Any, Dict, List, Type, TypeVar, cast

import attr

from ..models.normalize_text_step_rule import NormalizeTextStepRule
from ..models.normalize_text_step_step_type import NormalizeTextStepStepType

T = TypeVar("T", bound="NormalizeTextStep")

@attr.s(auto_attribs=True)
class NormalizeTextStep:
    """  """
    columns: List[str]
    rule: NormalizeTextStepRule
    step_type: NormalizeTextStepStepType
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        columns = self.columns




        rule = self.rule.value

        step_type = self.step_type.value


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "columns": columns,
            "rule": rule,
            "stepType": step_type,
        })

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        columns = cast(List[str], d.pop("columns"))


        rule = NormalizeTextStepRule(d.pop("rule"))




        step_type = NormalizeTextStepStepType(d.pop("stepType"))




        normalize_text_step = cls(
            columns=columns,
            rule=rule,
            step_type=step_type,
        )

        normalize_text_step.additional_properties = d
        return normalize_text_step

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
