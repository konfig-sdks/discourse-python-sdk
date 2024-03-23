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


class UsersDeleteUserByIdJsonRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            delete_posts = schemas.BoolSchema
            block_email = schemas.BoolSchema
            block_urls = schemas.BoolSchema
            block_ip = schemas.BoolSchema
            __annotations__ = {
                "delete_posts": delete_posts,
                "block_email": block_email,
                "block_urls": block_urls,
                "block_ip": block_ip,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["delete_posts"]) -> MetaOapg.properties.delete_posts: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["block_email"]) -> MetaOapg.properties.block_email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["block_urls"]) -> MetaOapg.properties.block_urls: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["block_ip"]) -> MetaOapg.properties.block_ip: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["delete_posts"], typing_extensions.Literal["block_email"], typing_extensions.Literal["block_urls"], typing_extensions.Literal["block_ip"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["delete_posts"]) -> typing.Union[MetaOapg.properties.delete_posts, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["block_email"]) -> typing.Union[MetaOapg.properties.block_email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["block_urls"]) -> typing.Union[MetaOapg.properties.block_urls, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["block_ip"]) -> typing.Union[MetaOapg.properties.block_ip, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["delete_posts"], typing_extensions.Literal["block_email"], typing_extensions.Literal["block_urls"], typing_extensions.Literal["block_ip"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        delete_posts: typing.Union[MetaOapg.properties.delete_posts, bool, schemas.Unset] = schemas.unset,
        block_email: typing.Union[MetaOapg.properties.block_email, bool, schemas.Unset] = schemas.unset,
        block_urls: typing.Union[MetaOapg.properties.block_urls, bool, schemas.Unset] = schemas.unset,
        block_ip: typing.Union[MetaOapg.properties.block_ip, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs,
    ) -> 'UsersDeleteUserByIdJsonRequest':
        return super().__new__(
            cls,
            *args,
            delete_posts=delete_posts,
            block_email=block_email,
            block_urls=block_urls,
            block_ip=block_ip,
            _configuration=_configuration,
        )
