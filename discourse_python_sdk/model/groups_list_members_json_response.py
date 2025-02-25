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


class GroupsListMembersJsonResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "meta",
            "members",
            "owners",
        }
        
        class properties:
            
            
            class members(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            required = {
                                "added_at",
                                "timezone",
                                "name",
                                "id",
                                "last_seen_at",
                                "title",
                                "avatar_template",
                                "last_posted_at",
                                "username",
                            }
                            
                            class properties:
                                title = schemas.AnyTypeSchema
                                id = schemas.IntSchema
                                username = schemas.StrSchema
                                name = schemas.AnyTypeSchema
                                avatar_template = schemas.StrSchema
                                last_posted_at = schemas.StrSchema
                                last_seen_at = schemas.StrSchema
                                added_at = schemas.StrSchema
                                timezone = schemas.StrSchema
                                __annotations__ = {
                                    "title": title,
                                    "id": id,
                                    "username": username,
                                    "name": name,
                                    "avatar_template": avatar_template,
                                    "last_posted_at": last_posted_at,
                                    "last_seen_at": last_seen_at,
                                    "added_at": added_at,
                                    "timezone": timezone,
                                }
                        
                        added_at: MetaOapg.properties.added_at
                        timezone: MetaOapg.properties.timezone
                        name: MetaOapg.properties.name
                        id: MetaOapg.properties.id
                        last_seen_at: MetaOapg.properties.last_seen_at
                        title: MetaOapg.properties.title
                        avatar_template: MetaOapg.properties.avatar_template
                        last_posted_at: MetaOapg.properties.last_posted_at
                        username: MetaOapg.properties.username
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["username"]) -> MetaOapg.properties.username: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["avatar_template"]) -> MetaOapg.properties.avatar_template: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["last_posted_at"]) -> MetaOapg.properties.last_posted_at: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["last_seen_at"]) -> MetaOapg.properties.last_seen_at: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["added_at"]) -> MetaOapg.properties.added_at: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["timezone"]) -> MetaOapg.properties.timezone: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["title", "id", "username", "name", "avatar_template", "last_posted_at", "last_seen_at", "added_at", "timezone", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["username"]) -> MetaOapg.properties.username: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["avatar_template"]) -> MetaOapg.properties.avatar_template: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["last_posted_at"]) -> MetaOapg.properties.last_posted_at: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["last_seen_at"]) -> MetaOapg.properties.last_seen_at: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["added_at"]) -> MetaOapg.properties.added_at: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["timezone"]) -> MetaOapg.properties.timezone: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["title", "id", "username", "name", "avatar_template", "last_posted_at", "last_seen_at", "added_at", "timezone", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, ],
                            added_at: typing.Union[MetaOapg.properties.added_at, str, ],
                            timezone: typing.Union[MetaOapg.properties.timezone, str, ],
                            name: typing.Union[MetaOapg.properties.name, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                            id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, ],
                            last_seen_at: typing.Union[MetaOapg.properties.last_seen_at, str, ],
                            title: typing.Union[MetaOapg.properties.title, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                            avatar_template: typing.Union[MetaOapg.properties.avatar_template, str, ],
                            last_posted_at: typing.Union[MetaOapg.properties.last_posted_at, str, ],
                            username: typing.Union[MetaOapg.properties.username, str, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                *args,
                                added_at=added_at,
                                timezone=timezone,
                                name=name,
                                id=id,
                                last_seen_at=last_seen_at,
                                title=title,
                                avatar_template=avatar_template,
                                last_posted_at=last_posted_at,
                                username=username,
                                _configuration=_configuration,
                                **kwargs,
                            )
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'members':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class owners(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            required = {
                                "added_at",
                                "timezone",
                                "name",
                                "id",
                                "last_seen_at",
                                "title",
                                "avatar_template",
                                "last_posted_at",
                                "username",
                            }
                            
                            class properties:
                                title = schemas.AnyTypeSchema
                                id = schemas.IntSchema
                                username = schemas.StrSchema
                                name = schemas.AnyTypeSchema
                                avatar_template = schemas.StrSchema
                                last_posted_at = schemas.StrSchema
                                last_seen_at = schemas.StrSchema
                                added_at = schemas.StrSchema
                                timezone = schemas.StrSchema
                                __annotations__ = {
                                    "title": title,
                                    "id": id,
                                    "username": username,
                                    "name": name,
                                    "avatar_template": avatar_template,
                                    "last_posted_at": last_posted_at,
                                    "last_seen_at": last_seen_at,
                                    "added_at": added_at,
                                    "timezone": timezone,
                                }
                        
                        added_at: MetaOapg.properties.added_at
                        timezone: MetaOapg.properties.timezone
                        name: MetaOapg.properties.name
                        id: MetaOapg.properties.id
                        last_seen_at: MetaOapg.properties.last_seen_at
                        title: MetaOapg.properties.title
                        avatar_template: MetaOapg.properties.avatar_template
                        last_posted_at: MetaOapg.properties.last_posted_at
                        username: MetaOapg.properties.username
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["username"]) -> MetaOapg.properties.username: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["avatar_template"]) -> MetaOapg.properties.avatar_template: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["last_posted_at"]) -> MetaOapg.properties.last_posted_at: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["last_seen_at"]) -> MetaOapg.properties.last_seen_at: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["added_at"]) -> MetaOapg.properties.added_at: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["timezone"]) -> MetaOapg.properties.timezone: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["title", "id", "username", "name", "avatar_template", "last_posted_at", "last_seen_at", "added_at", "timezone", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["username"]) -> MetaOapg.properties.username: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["avatar_template"]) -> MetaOapg.properties.avatar_template: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["last_posted_at"]) -> MetaOapg.properties.last_posted_at: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["last_seen_at"]) -> MetaOapg.properties.last_seen_at: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["added_at"]) -> MetaOapg.properties.added_at: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["timezone"]) -> MetaOapg.properties.timezone: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["title", "id", "username", "name", "avatar_template", "last_posted_at", "last_seen_at", "added_at", "timezone", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, ],
                            added_at: typing.Union[MetaOapg.properties.added_at, str, ],
                            timezone: typing.Union[MetaOapg.properties.timezone, str, ],
                            name: typing.Union[MetaOapg.properties.name, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                            id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, ],
                            last_seen_at: typing.Union[MetaOapg.properties.last_seen_at, str, ],
                            title: typing.Union[MetaOapg.properties.title, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                            avatar_template: typing.Union[MetaOapg.properties.avatar_template, str, ],
                            last_posted_at: typing.Union[MetaOapg.properties.last_posted_at, str, ],
                            username: typing.Union[MetaOapg.properties.username, str, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                *args,
                                added_at=added_at,
                                timezone=timezone,
                                name=name,
                                id=id,
                                last_seen_at=last_seen_at,
                                title=title,
                                avatar_template=avatar_template,
                                last_posted_at=last_posted_at,
                                username=username,
                                _configuration=_configuration,
                                **kwargs,
                            )
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'owners':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class meta(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    required = {
                        "total",
                        "offset",
                        "limit",
                    }
                    
                    class properties:
                        total = schemas.IntSchema
                        limit = schemas.IntSchema
                        offset = schemas.IntSchema
                        __annotations__ = {
                            "total": total,
                            "limit": limit,
                            "offset": offset,
                        }
                
                total: MetaOapg.properties.total
                offset: MetaOapg.properties.offset
                limit: MetaOapg.properties.limit
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["total"]) -> MetaOapg.properties.total: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["limit"]) -> MetaOapg.properties.limit: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["offset"]) -> MetaOapg.properties.offset: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["total", "limit", "offset", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["total"]) -> MetaOapg.properties.total: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["limit"]) -> MetaOapg.properties.limit: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["offset"]) -> MetaOapg.properties.offset: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["total", "limit", "offset", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    total: typing.Union[MetaOapg.properties.total, decimal.Decimal, int, ],
                    offset: typing.Union[MetaOapg.properties.offset, decimal.Decimal, int, ],
                    limit: typing.Union[MetaOapg.properties.limit, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'meta':
                    return super().__new__(
                        cls,
                        *args,
                        total=total,
                        offset=offset,
                        limit=limit,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "members": members,
                "owners": owners,
                "meta": meta,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    meta: MetaOapg.properties.meta
    members: MetaOapg.properties.members
    owners: MetaOapg.properties.owners
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["meta"]) -> MetaOapg.properties.meta: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["members"]) -> MetaOapg.properties.members: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["owners"]) -> MetaOapg.properties.owners: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["meta"], typing_extensions.Literal["members"], typing_extensions.Literal["owners"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["meta"]) -> MetaOapg.properties.meta: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["members"]) -> MetaOapg.properties.members: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["owners"]) -> MetaOapg.properties.owners: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["meta"], typing_extensions.Literal["members"], typing_extensions.Literal["owners"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        meta: typing.Union[MetaOapg.properties.meta, dict, frozendict.frozendict, ],
        members: typing.Union[MetaOapg.properties.members, list, tuple, ],
        owners: typing.Union[MetaOapg.properties.owners, list, tuple, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs,
    ) -> 'GroupsListMembersJsonResponse':
        return super().__new__(
            cls,
            *args,
            meta=meta,
            members=members,
            owners=owners,
            _configuration=_configuration,
        )
