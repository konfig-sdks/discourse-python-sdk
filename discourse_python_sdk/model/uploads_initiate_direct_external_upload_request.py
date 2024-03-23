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


class UploadsInitiateDirectExternalUploadRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "file_name",
            "type",
            "file_size",
        }
        
        class properties:
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "avatar": "AVATAR",
                        "profile_background": "PROFILE_BACKGROUND",
                        "card_background": "CARD_BACKGROUND",
                        "custom_emoji": "CUSTOM_EMOJI",
                        "composer": "COMPOSER",
                    }
                
                @schemas.classproperty
                def AVATAR(cls):
                    return cls("avatar")
                
                @schemas.classproperty
                def PROFILE_BACKGROUND(cls):
                    return cls("profile_background")
                
                @schemas.classproperty
                def CARD_BACKGROUND(cls):
                    return cls("card_background")
                
                @schemas.classproperty
                def CUSTOM_EMOJI(cls):
                    return cls("custom_emoji")
                
                @schemas.classproperty
                def COMPOSER(cls):
                    return cls("composer")
            file_name = schemas.StrSchema
            file_size = schemas.IntSchema
            
            
            class metadata(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        sha1_checksum = schemas.StrSchema
                        __annotations__ = {
                            "sha1-checksum": sha1_checksum,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["sha1-checksum"]) -> MetaOapg.properties.sha1_checksum: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["sha1-checksum", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["sha1-checksum"]) -> typing.Union[MetaOapg.properties.sha1_checksum, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["sha1-checksum", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'metadata':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "type": type,
                "file_name": file_name,
                "file_size": file_size,
                "metadata": metadata,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    file_name: MetaOapg.properties.file_name
    type: MetaOapg.properties.type
    file_size: MetaOapg.properties.file_size
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["file_name"]) -> MetaOapg.properties.file_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["file_size"]) -> MetaOapg.properties.file_size: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> MetaOapg.properties.metadata: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["file_name"], typing_extensions.Literal["type"], typing_extensions.Literal["file_size"], typing_extensions.Literal["metadata"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["file_name"]) -> MetaOapg.properties.file_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["file_size"]) -> MetaOapg.properties.file_size: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> typing.Union[MetaOapg.properties.metadata, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["file_name"], typing_extensions.Literal["type"], typing_extensions.Literal["file_size"], typing_extensions.Literal["metadata"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        file_name: typing.Union[MetaOapg.properties.file_name, str, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        file_size: typing.Union[MetaOapg.properties.file_size, decimal.Decimal, int, ],
        metadata: typing.Union[MetaOapg.properties.metadata, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs,
    ) -> 'UploadsInitiateDirectExternalUploadRequest':
        return super().__new__(
            cls,
            *args,
            file_name=file_name,
            type=type,
            file_size=file_size,
            metadata=metadata,
            _configuration=_configuration,
        )
