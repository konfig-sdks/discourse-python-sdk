# coding: utf-8

"""
    Discourse API Documentation

    This page contains the documentation on how to use Discourse through API calls.  > Note: For any endpoints not listed you can follow the [reverse engineer the Discourse API](https://meta.discourse.org/t/-/20576) guide to figure out how to use an API endpoint.  ### Request Content-Type  The Content-Type for POST and PUT requests can be set to `application/x-www-form-urlencoded`, `multipart/form-data`, or `application/json`.  ### Endpoint Names and Response Content-Type  Most API endpoints provide the same content as their HTML counterparts. For example the URL `/categories` serves a list of categories, the `/categories.json` API provides the same information in JSON format.  Instead of sending API requests to `/categories.json` you may also send them to `/categories` and add an `Accept: application/json` header to the request to get the JSON response. Sending requests with the `Accept` header is necessary if you want to use URLs for related endpoints returned by the API, such as pagination URLs. These URLs are returned without the `.json` prefix so you need to add the header in order to get the correct response format.  ### Authentication  Some endpoints do not require any authentication, pretty much anything else will require you to be authenticated.  To become authenticated you will need to create an API Key from the admin panel.  Once you have your API Key you can pass it in along with your API Username as an HTTP header like this:  ``` curl -X GET \"http://127.0.0.1:3000/admin/users/list/active.json\" \\ -H \"Api-Key: 714552c6148e1617aeab526d0606184b94a80ec048fc09894ff1a72b740c5f19\" \\ -H \"Api-Username: system\" ```  and this is how POST requests will look:  ``` curl -X POST \"http://127.0.0.1:3000/categories\" \\ -H \"Content-Type: multipart/form-data;\" \\ -H \"Api-Key: 714552c6148e1617aeab526d0606184b94a80ec048fc09894ff1a72b740c5f19\" \\ -H \"Api-Username: system\" \\ -F \"name=89853c20-4409-e91a-a8ea-f6cdff96aaaa\" \\ -F \"color=49d9e9\" \\ -F \"text_color=f0fcfd\" ```  ### Boolean values  If an endpoint accepts a boolean be sure to specify it as a lowercase `true` or `false` value unless noted otherwise. 

    The version of the OpenAPI document: latest
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from discourse_python_sdk import schemas  # noqa: F401


class TagsGetSpecificTagResponseTopicList(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def tags() -> typing.Type['TagsGetSpecificTagResponseTopicListTags']:
                return TagsGetSpecificTagResponseTopicListTags
            can_create_topic = schemas.BoolSchema
            draft = schemas.AnyTypeSchema
            draft_key = schemas.StrSchema
            draft_sequence = schemas.IntSchema
            per_page = schemas.IntSchema
        
            @staticmethod
            def topics() -> typing.Type['TagsGetSpecificTagResponseTopicListTopics']:
                return TagsGetSpecificTagResponseTopicListTopics
            __annotations__ = {
                "tags": tags,
                "can_create_topic": can_create_topic,
                "draft": draft,
                "draft_key": draft_key,
                "draft_sequence": draft_sequence,
                "per_page": per_page,
                "topics": topics,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tags"]) -> 'TagsGetSpecificTagResponseTopicListTags': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["can_create_topic"]) -> MetaOapg.properties.can_create_topic: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["draft"]) -> MetaOapg.properties.draft: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["draft_key"]) -> MetaOapg.properties.draft_key: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["draft_sequence"]) -> MetaOapg.properties.draft_sequence: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["per_page"]) -> MetaOapg.properties.per_page: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["topics"]) -> 'TagsGetSpecificTagResponseTopicListTopics': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["tags", "can_create_topic", "draft", "draft_key", "draft_sequence", "per_page", "topics", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tags"]) -> typing.Union['TagsGetSpecificTagResponseTopicListTags', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["can_create_topic"]) -> typing.Union[MetaOapg.properties.can_create_topic, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["draft"]) -> typing.Union[MetaOapg.properties.draft, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["draft_key"]) -> typing.Union[MetaOapg.properties.draft_key, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["draft_sequence"]) -> typing.Union[MetaOapg.properties.draft_sequence, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["per_page"]) -> typing.Union[MetaOapg.properties.per_page, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["topics"]) -> typing.Union['TagsGetSpecificTagResponseTopicListTopics', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["tags", "can_create_topic", "draft", "draft_key", "draft_sequence", "per_page", "topics", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        tags: typing.Union['TagsGetSpecificTagResponseTopicListTags', schemas.Unset] = schemas.unset,
        can_create_topic: typing.Union[MetaOapg.properties.can_create_topic, bool, schemas.Unset] = schemas.unset,
        draft: typing.Union[MetaOapg.properties.draft, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        draft_key: typing.Union[MetaOapg.properties.draft_key, str, schemas.Unset] = schemas.unset,
        draft_sequence: typing.Union[MetaOapg.properties.draft_sequence, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        per_page: typing.Union[MetaOapg.properties.per_page, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        topics: typing.Union['TagsGetSpecificTagResponseTopicListTopics', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TagsGetSpecificTagResponseTopicList':
        return super().__new__(
            cls,
            *args,
            tags=tags,
            can_create_topic=can_create_topic,
            draft=draft,
            draft_key=draft_key,
            draft_sequence=draft_sequence,
            per_page=per_page,
            topics=topics,
            _configuration=_configuration,
            **kwargs,
        )

from discourse_python_sdk.model.tags_get_specific_tag_response_topic_list_tags import TagsGetSpecificTagResponseTopicListTags
from discourse_python_sdk.model.tags_get_specific_tag_response_topic_list_topics import TagsGetSpecificTagResponseTopicListTopics
