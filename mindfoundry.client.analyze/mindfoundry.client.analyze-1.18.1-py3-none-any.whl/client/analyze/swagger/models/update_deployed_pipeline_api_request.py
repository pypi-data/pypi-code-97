from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateDeployedPipelineApiRequest")

@attr.s(auto_attribs=True)
class UpdateDeployedPipelineApiRequest:
    """  """
    new_pipeline_id: int
    notes: Union[Unset, Optional[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        new_pipeline_id =  self.new_pipeline_id
        notes =  self.notes

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "newPipelineId": new_pipeline_id,
        })
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        new_pipeline_id = d.pop("newPipelineId")

        notes = d.pop("notes", UNSET)

        update_deployed_pipeline_api_request = cls(
            new_pipeline_id=new_pipeline_id,
            notes=notes,
        )

        update_deployed_pipeline_api_request.additional_properties = d
        return update_deployed_pipeline_api_request

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
