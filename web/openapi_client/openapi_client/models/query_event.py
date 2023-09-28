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



from pydantic import BaseModel, Field, StrictInt, StrictStr, validator

class QueryEvent(BaseModel):
    """
    QueryEvent
    """
    timestamp: StrictInt = Field(...)
    category: StrictStr = Field(...)
    type: StrictStr = Field(...)
    value: StrictStr = Field(...)
    __properties = ["timestamp", "category", "type", "value"]

    @validator('category')
    def category_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('TEXT', 'IMAGE', 'SKETCH', 'FILTER', 'BROWSING', 'COOPERATION', 'OTHER'):
            raise ValueError("must be one of enum values ('TEXT', 'IMAGE', 'SKETCH', 'FILTER', 'BROWSING', 'COOPERATION', 'OTHER')")
        return value

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
    def from_json(cls, json_str: str) -> QueryEvent:
        """Create an instance of QueryEvent from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> QueryEvent:
        """Create an instance of QueryEvent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return QueryEvent.parse_obj(obj)

        _obj = QueryEvent.parse_obj({
            "timestamp": obj.get("timestamp"),
            "category": obj.get("category"),
            "type": obj.get("type"),
            "value": obj.get("value")
        })
        return _obj


