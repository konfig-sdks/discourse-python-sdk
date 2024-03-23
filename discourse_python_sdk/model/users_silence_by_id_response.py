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


class UsersSilenceByIdResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "silence",
        }
        
        class properties:
            
            
            class silence(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    required = {
                        "silenced",
                        "silenced_at",
                        "silenced_till",
                        "silence_reason",
                        "silenced_by",
                    }
                    
                    class properties:
                        silenced = schemas.BoolSchema
                        silence_reason = schemas.StrSchema
                        silenced_till = schemas.StrSchema
                        silenced_at = schemas.StrSchema
                        
                        
                        class silenced_by(
                            schemas.DictSchema
                        ):
                        
                        
                            class MetaOapg:
                                required = {
                                    "name",
                                    "id",
                                    "avatar_template",
                                    "username",
                                }
                                
                                class properties:
                                    id = schemas.IntSchema
                                    username = schemas.StrSchema
                                    name = schemas.StrSchema
                                    avatar_template = schemas.StrSchema
                                    __annotations__ = {
                                        "id": id,
                                        "username": username,
                                        "name": name,
                                        "avatar_template": avatar_template,
                                    }
                            
                            name: MetaOapg.properties.name
                            id: MetaOapg.properties.id
                            avatar_template: MetaOapg.properties.avatar_template
                            username: MetaOapg.properties.username
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["username"]) -> MetaOapg.properties.username: ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["avatar_template"]) -> MetaOapg.properties.avatar_template: ...
                            
                            @typing.overload
                            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                            
                            def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "username", "name", "avatar_template", ], str]):
                                # dict_instance[name] accessor
                                return super().__getitem__(name)
                            
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["username"]) -> MetaOapg.properties.username: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["avatar_template"]) -> MetaOapg.properties.avatar_template: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                            
                            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "username", "name", "avatar_template", ], str]):
                                return super().get_item_oapg(name)
                            
                        
                            def __new__(
                                cls,
                                *args: typing.Union[dict, frozendict.frozendict, ],
                                name: typing.Union[MetaOapg.properties.name, str, ],
                                id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, ],
                                avatar_template: typing.Union[MetaOapg.properties.avatar_template, str, ],
                                username: typing.Union[MetaOapg.properties.username, str, ],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                            ) -> 'silenced_by':
                                return super().__new__(
                                    cls,
                                    *args,
                                    name=name,
                                    id=id,
                                    avatar_template=avatar_template,
                                    username=username,
                                    _configuration=_configuration,
                                    **kwargs,
                                )
                        __annotations__ = {
                            "silenced": silenced,
                            "silence_reason": silence_reason,
                            "silenced_till": silenced_till,
                            "silenced_at": silenced_at,
                            "silenced_by": silenced_by,
                        }
                
                silenced: MetaOapg.properties.silenced
                silenced_at: MetaOapg.properties.silenced_at
                silenced_till: MetaOapg.properties.silenced_till
                silence_reason: MetaOapg.properties.silence_reason
                silenced_by: MetaOapg.properties.silenced_by
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["silenced"]) -> MetaOapg.properties.silenced: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["silence_reason"]) -> MetaOapg.properties.silence_reason: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["silenced_till"]) -> MetaOapg.properties.silenced_till: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["silenced_at"]) -> MetaOapg.properties.silenced_at: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["silenced_by"]) -> MetaOapg.properties.silenced_by: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["silenced", "silence_reason", "silenced_till", "silenced_at", "silenced_by", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["silenced"]) -> MetaOapg.properties.silenced: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["silence_reason"]) -> MetaOapg.properties.silence_reason: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["silenced_till"]) -> MetaOapg.properties.silenced_till: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["silenced_at"]) -> MetaOapg.properties.silenced_at: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["silenced_by"]) -> MetaOapg.properties.silenced_by: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["silenced", "silence_reason", "silenced_till", "silenced_at", "silenced_by", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    silenced: typing.Union[MetaOapg.properties.silenced, bool, ],
                    silenced_at: typing.Union[MetaOapg.properties.silenced_at, str, ],
                    silenced_till: typing.Union[MetaOapg.properties.silenced_till, str, ],
                    silence_reason: typing.Union[MetaOapg.properties.silence_reason, str, ],
                    silenced_by: typing.Union[MetaOapg.properties.silenced_by, dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'silence':
                    return super().__new__(
                        cls,
                        *args,
                        silenced=silenced,
                        silenced_at=silenced_at,
                        silenced_till=silenced_till,
                        silence_reason=silence_reason,
                        silenced_by=silenced_by,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "silence": silence,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    silence: MetaOapg.properties.silence
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["silence"]) -> MetaOapg.properties.silence: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["silence"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["silence"]) -> MetaOapg.properties.silence: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["silence"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        silence: typing.Union[MetaOapg.properties.silence, dict, frozendict.frozendict, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs,
    ) -> 'UsersSilenceByIdResponse':
        return super().__new__(
            cls,
            *args,
            silence=silence,
            _configuration=_configuration,
        )
