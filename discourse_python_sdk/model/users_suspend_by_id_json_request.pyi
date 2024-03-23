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


class UsersSuspendByIdJsonRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "suspend_until",
            "reason",
        }
        
        class properties:
            suspend_until = schemas.StrSchema
            reason = schemas.StrSchema
            message = schemas.StrSchema
            post_action = schemas.StrSchema
            __annotations__ = {
                "suspend_until": suspend_until,
                "reason": reason,
                "message": message,
                "post_action": post_action,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    suspend_until: MetaOapg.properties.suspend_until
    reason: MetaOapg.properties.reason
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["suspend_until"]) -> MetaOapg.properties.suspend_until: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reason"]) -> MetaOapg.properties.reason: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["post_action"]) -> MetaOapg.properties.post_action: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["suspend_until"], typing_extensions.Literal["reason"], typing_extensions.Literal["message"], typing_extensions.Literal["post_action"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["suspend_until"]) -> MetaOapg.properties.suspend_until: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reason"]) -> MetaOapg.properties.reason: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> typing.Union[MetaOapg.properties.message, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["post_action"]) -> typing.Union[MetaOapg.properties.post_action, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["suspend_until"], typing_extensions.Literal["reason"], typing_extensions.Literal["message"], typing_extensions.Literal["post_action"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        suspend_until: typing.Union[MetaOapg.properties.suspend_until, str, ],
        reason: typing.Union[MetaOapg.properties.reason, str, ],
        message: typing.Union[MetaOapg.properties.message, str, schemas.Unset] = schemas.unset,
        post_action: typing.Union[MetaOapg.properties.post_action, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs,
    ) -> 'UsersSuspendByIdJsonRequest':
        return super().__new__(
            cls,
            *args,
            suspend_until=suspend_until,
            reason=reason,
            message=message,
            post_action=post_action,
            _configuration=_configuration,
        )
