# coding: utf-8

"""
    DRES API

    API for DRES (Distributed Retrieval Evaluation Server), Version 1.0

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr

class ResultElement(BaseModel):
    """
    ResultElement
    """
    item: Optional[StrictStr] = None
    text: Optional[StrictStr] = None
    start_time_code: Optional[StrictStr] = Field(None, alias="startTimeCode")
    end_time_code: Optional[StrictStr] = Field(None, alias="endTimeCode")
    index: Optional[StrictInt] = None
    rank: Optional[StrictInt] = None
    weight: Optional[Union[StrictFloat, StrictInt]] = None
    __properties = ["item", "text", "startTimeCode", "endTimeCode", "index", "rank", "weight"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ResultElement:
        """Create an instance of ResultElement from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ResultElement:
        """Create an instance of ResultElement from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ResultElement.parse_obj(obj)

        _obj = ResultElement.parse_obj({
            "item": obj.get("item"),
            "text": obj.get("text"),
            "start_time_code": obj.get("startTimeCode"),
            "end_time_code": obj.get("endTimeCode"),
            "index": obj.get("index"),
            "rank": obj.get("rank"),
            "weight": obj.get("weight")
        })
        return _obj


