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


class UploadsCompleteMultipartUploadResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "extension",
            "filesize",
            "retain_hours",
            "url",
            "short_url",
            "thumbnail_height",
            "original_filename",
            "thumbnail_width",
            "width",
            "id",
            "short_path",
            "human_filesize",
            "height",
        }
        
        class properties:
            id = schemas.IntSchema
            url = schemas.StrSchema
            original_filename = schemas.StrSchema
            filesize = schemas.IntSchema
            width = schemas.IntSchema
            height = schemas.IntSchema
            thumbnail_width = schemas.IntSchema
            thumbnail_height = schemas.IntSchema
            extension = schemas.StrSchema
            short_url = schemas.StrSchema
            short_path = schemas.StrSchema
            retain_hours = schemas.AnyTypeSchema
            human_filesize = schemas.StrSchema
            dominant_color = schemas.AnyTypeSchema
            __annotations__ = {
                "id": id,
                "url": url,
                "original_filename": original_filename,
                "filesize": filesize,
                "width": width,
                "height": height,
                "thumbnail_width": thumbnail_width,
                "thumbnail_height": thumbnail_height,
                "extension": extension,
                "short_url": short_url,
                "short_path": short_path,
                "retain_hours": retain_hours,
                "human_filesize": human_filesize,
                "dominant_color": dominant_color,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    extension: MetaOapg.properties.extension
    filesize: MetaOapg.properties.filesize
    retain_hours: MetaOapg.properties.retain_hours
    url: MetaOapg.properties.url
    short_url: MetaOapg.properties.short_url
    thumbnail_height: MetaOapg.properties.thumbnail_height
    original_filename: MetaOapg.properties.original_filename
    thumbnail_width: MetaOapg.properties.thumbnail_width
    width: MetaOapg.properties.width
    id: MetaOapg.properties.id
    short_path: MetaOapg.properties.short_path
    human_filesize: MetaOapg.properties.human_filesize
    height: MetaOapg.properties.height
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["extension"]) -> MetaOapg.properties.extension: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["filesize"]) -> MetaOapg.properties.filesize: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["retain_hours"]) -> MetaOapg.properties.retain_hours: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["short_url"]) -> MetaOapg.properties.short_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["thumbnail_height"]) -> MetaOapg.properties.thumbnail_height: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["original_filename"]) -> MetaOapg.properties.original_filename: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["thumbnail_width"]) -> MetaOapg.properties.thumbnail_width: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["width"]) -> MetaOapg.properties.width: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["short_path"]) -> MetaOapg.properties.short_path: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["human_filesize"]) -> MetaOapg.properties.human_filesize: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["height"]) -> MetaOapg.properties.height: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dominant_color"]) -> MetaOapg.properties.dominant_color: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["extension"], typing_extensions.Literal["filesize"], typing_extensions.Literal["retain_hours"], typing_extensions.Literal["url"], typing_extensions.Literal["short_url"], typing_extensions.Literal["thumbnail_height"], typing_extensions.Literal["original_filename"], typing_extensions.Literal["thumbnail_width"], typing_extensions.Literal["width"], typing_extensions.Literal["id"], typing_extensions.Literal["short_path"], typing_extensions.Literal["human_filesize"], typing_extensions.Literal["height"], typing_extensions.Literal["dominant_color"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["extension"]) -> MetaOapg.properties.extension: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["filesize"]) -> MetaOapg.properties.filesize: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["retain_hours"]) -> MetaOapg.properties.retain_hours: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["short_url"]) -> MetaOapg.properties.short_url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["thumbnail_height"]) -> MetaOapg.properties.thumbnail_height: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["original_filename"]) -> MetaOapg.properties.original_filename: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["thumbnail_width"]) -> MetaOapg.properties.thumbnail_width: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["width"]) -> MetaOapg.properties.width: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["short_path"]) -> MetaOapg.properties.short_path: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["human_filesize"]) -> MetaOapg.properties.human_filesize: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["height"]) -> MetaOapg.properties.height: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dominant_color"]) -> typing.Union[MetaOapg.properties.dominant_color, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["extension"], typing_extensions.Literal["filesize"], typing_extensions.Literal["retain_hours"], typing_extensions.Literal["url"], typing_extensions.Literal["short_url"], typing_extensions.Literal["thumbnail_height"], typing_extensions.Literal["original_filename"], typing_extensions.Literal["thumbnail_width"], typing_extensions.Literal["width"], typing_extensions.Literal["id"], typing_extensions.Literal["short_path"], typing_extensions.Literal["human_filesize"], typing_extensions.Literal["height"], typing_extensions.Literal["dominant_color"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        extension: typing.Union[MetaOapg.properties.extension, str, ],
        filesize: typing.Union[MetaOapg.properties.filesize, decimal.Decimal, int, ],
        retain_hours: typing.Union[MetaOapg.properties.retain_hours, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        url: typing.Union[MetaOapg.properties.url, str, ],
        short_url: typing.Union[MetaOapg.properties.short_url, str, ],
        thumbnail_height: typing.Union[MetaOapg.properties.thumbnail_height, decimal.Decimal, int, ],
        original_filename: typing.Union[MetaOapg.properties.original_filename, str, ],
        thumbnail_width: typing.Union[MetaOapg.properties.thumbnail_width, decimal.Decimal, int, ],
        width: typing.Union[MetaOapg.properties.width, decimal.Decimal, int, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, ],
        short_path: typing.Union[MetaOapg.properties.short_path, str, ],
        human_filesize: typing.Union[MetaOapg.properties.human_filesize, str, ],
        height: typing.Union[MetaOapg.properties.height, decimal.Decimal, int, ],
        dominant_color: typing.Union[MetaOapg.properties.dominant_color, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs,
    ) -> 'UploadsCompleteMultipartUploadResponse':
        return super().__new__(
            cls,
            *args,
            extension=extension,
            filesize=filesize,
            retain_hours=retain_hours,
            url=url,
            short_url=short_url,
            thumbnail_height=thumbnail_height,
            original_filename=original_filename,
            thumbnail_width=thumbnail_width,
            width=width,
            id=id,
            short_path=short_path,
            human_filesize=human_filesize,
            height=height,
            dominant_color=dominant_color,
            _configuration=_configuration,
        )
