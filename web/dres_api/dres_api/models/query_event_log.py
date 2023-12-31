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


from typing import List
from pydantic import BaseModel, Field, StrictInt, conlist
from dres_api.models.query_event import QueryEvent

class QueryEventLog(BaseModel):
    """
    QueryEventLog
    """
    timestamp: StrictInt = Field(...)
    events: conlist(QueryEvent) = Field(...)
    __properties = ["timestamp", "events"]

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
    def from_json(cls, json_str: str) -> QueryEventLog:
        """Create an instance of QueryEventLog from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in events (list)
        _items = []
        if self.events:
            for _item in self.events:
                if _item:
                    _items.append(_item.to_dict())
            _dict['events'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> QueryEventLog:
        """Create an instance of QueryEventLog from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return QueryEventLog.parse_obj(obj)

        _obj = QueryEventLog.parse_obj({
            "timestamp": obj.get("timestamp"),
            "events": [QueryEvent.from_dict(_item) for _item in obj.get("events")] if obj.get("events") is not None else None
        })
        return _obj


