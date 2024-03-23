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


class BadgesUpdateBadgeByIdJsonResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "badge",
            "badge_types",
        }
        
        class properties:
            
            
            class badge_types(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            required = {
                                "name",
                                "id",
                                "sort_order",
                            }
                            
                            class properties:
                                id = schemas.IntSchema
                                name = schemas.StrSchema
                                sort_order = schemas.IntSchema
                                __annotations__ = {
                                    "id": id,
                                    "name": name,
                                    "sort_order": sort_order,
                                }
                        
                        name: MetaOapg.properties.name
                        id: MetaOapg.properties.id
                        sort_order: MetaOapg.properties.sort_order
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["sort_order"]) -> MetaOapg.properties.sort_order: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "name", "sort_order", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["sort_order"]) -> MetaOapg.properties.sort_order: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "name", "sort_order", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, ],
                            name: typing.Union[MetaOapg.properties.name, str, ],
                            id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, ],
                            sort_order: typing.Union[MetaOapg.properties.sort_order, decimal.Decimal, int, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                *args,
                                name=name,
                                id=id,
                                sort_order=sort_order,
                                _configuration=_configuration,
                                **kwargs,
                            )
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'badge_types':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class badge(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    required = {
                        "listable",
                        "image_url",
                        "query",
                        "icon",
                        "description",
                        "multiple_grant",
                        "auto_revoke",
                        "long_description",
                        "trigger",
                        "target_posts",
                        "enabled",
                        "manually_grantable",
                        "grant_count",
                        "system",
                        "badge_type_id",
                        "badge_grouping_id",
                        "allow_title",
                        "name",
                        "id",
                        "show_posts",
                        "slug",
                    }
                    
                    class properties:
                        description = schemas.StrSchema
                        id = schemas.IntSchema
                        name = schemas.StrSchema
                        grant_count = schemas.IntSchema
                        allow_title = schemas.BoolSchema
                        multiple_grant = schemas.BoolSchema
                        icon = schemas.StrSchema
                        image_url = schemas.AnyTypeSchema
                        listable = schemas.BoolSchema
                        enabled = schemas.BoolSchema
                        badge_grouping_id = schemas.IntSchema
                        system = schemas.BoolSchema
                        long_description = schemas.StrSchema
                        slug = schemas.StrSchema
                        manually_grantable = schemas.BoolSchema
                        query = schemas.AnyTypeSchema
                        trigger = schemas.AnyTypeSchema
                        target_posts = schemas.BoolSchema
                        auto_revoke = schemas.BoolSchema
                        show_posts = schemas.BoolSchema
                        badge_type_id = schemas.IntSchema
                        __annotations__ = {
                            "description": description,
                            "id": id,
                            "name": name,
                            "grant_count": grant_count,
                            "allow_title": allow_title,
                            "multiple_grant": multiple_grant,
                            "icon": icon,
                            "image_url": image_url,
                            "listable": listable,
                            "enabled": enabled,
                            "badge_grouping_id": badge_grouping_id,
                            "system": system,
                            "long_description": long_description,
                            "slug": slug,
                            "manually_grantable": manually_grantable,
                            "query": query,
                            "trigger": trigger,
                            "target_posts": target_posts,
                            "auto_revoke": auto_revoke,
                            "show_posts": show_posts,
                            "badge_type_id": badge_type_id,
                        }
                
                listable: MetaOapg.properties.listable
                image_url: MetaOapg.properties.image_url
                query: MetaOapg.properties.query
                icon: MetaOapg.properties.icon
                description: MetaOapg.properties.description
                multiple_grant: MetaOapg.properties.multiple_grant
                auto_revoke: MetaOapg.properties.auto_revoke
                long_description: MetaOapg.properties.long_description
                trigger: MetaOapg.properties.trigger
                target_posts: MetaOapg.properties.target_posts
                enabled: MetaOapg.properties.enabled
                manually_grantable: MetaOapg.properties.manually_grantable
                grant_count: MetaOapg.properties.grant_count
                system: MetaOapg.properties.system
                badge_type_id: MetaOapg.properties.badge_type_id
                badge_grouping_id: MetaOapg.properties.badge_grouping_id
                allow_title: MetaOapg.properties.allow_title
                name: MetaOapg.properties.name
                id: MetaOapg.properties.id
                show_posts: MetaOapg.properties.show_posts
                slug: MetaOapg.properties.slug
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["grant_count"]) -> MetaOapg.properties.grant_count: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["allow_title"]) -> MetaOapg.properties.allow_title: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["multiple_grant"]) -> MetaOapg.properties.multiple_grant: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["icon"]) -> MetaOapg.properties.icon: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["image_url"]) -> MetaOapg.properties.image_url: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["listable"]) -> MetaOapg.properties.listable: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["enabled"]) -> MetaOapg.properties.enabled: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["badge_grouping_id"]) -> MetaOapg.properties.badge_grouping_id: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["system"]) -> MetaOapg.properties.system: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["long_description"]) -> MetaOapg.properties.long_description: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["slug"]) -> MetaOapg.properties.slug: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["manually_grantable"]) -> MetaOapg.properties.manually_grantable: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["query"]) -> MetaOapg.properties.query: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["trigger"]) -> MetaOapg.properties.trigger: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["target_posts"]) -> MetaOapg.properties.target_posts: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["auto_revoke"]) -> MetaOapg.properties.auto_revoke: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["show_posts"]) -> MetaOapg.properties.show_posts: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["badge_type_id"]) -> MetaOapg.properties.badge_type_id: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "id", "name", "grant_count", "allow_title", "multiple_grant", "icon", "image_url", "listable", "enabled", "badge_grouping_id", "system", "long_description", "slug", "manually_grantable", "query", "trigger", "target_posts", "auto_revoke", "show_posts", "badge_type_id", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["grant_count"]) -> MetaOapg.properties.grant_count: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["allow_title"]) -> MetaOapg.properties.allow_title: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["multiple_grant"]) -> MetaOapg.properties.multiple_grant: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["icon"]) -> MetaOapg.properties.icon: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["image_url"]) -> MetaOapg.properties.image_url: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["listable"]) -> MetaOapg.properties.listable: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["enabled"]) -> MetaOapg.properties.enabled: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["badge_grouping_id"]) -> MetaOapg.properties.badge_grouping_id: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["system"]) -> MetaOapg.properties.system: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["long_description"]) -> MetaOapg.properties.long_description: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["slug"]) -> MetaOapg.properties.slug: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["manually_grantable"]) -> MetaOapg.properties.manually_grantable: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["query"]) -> MetaOapg.properties.query: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["trigger"]) -> MetaOapg.properties.trigger: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["target_posts"]) -> MetaOapg.properties.target_posts: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["auto_revoke"]) -> MetaOapg.properties.auto_revoke: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["show_posts"]) -> MetaOapg.properties.show_posts: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["badge_type_id"]) -> MetaOapg.properties.badge_type_id: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "id", "name", "grant_count", "allow_title", "multiple_grant", "icon", "image_url", "listable", "enabled", "badge_grouping_id", "system", "long_description", "slug", "manually_grantable", "query", "trigger", "target_posts", "auto_revoke", "show_posts", "badge_type_id", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    listable: typing.Union[MetaOapg.properties.listable, bool, ],
                    image_url: typing.Union[MetaOapg.properties.image_url, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    query: typing.Union[MetaOapg.properties.query, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    icon: typing.Union[MetaOapg.properties.icon, str, ],
                    description: typing.Union[MetaOapg.properties.description, str, ],
                    multiple_grant: typing.Union[MetaOapg.properties.multiple_grant, bool, ],
                    auto_revoke: typing.Union[MetaOapg.properties.auto_revoke, bool, ],
                    long_description: typing.Union[MetaOapg.properties.long_description, str, ],
                    trigger: typing.Union[MetaOapg.properties.trigger, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    target_posts: typing.Union[MetaOapg.properties.target_posts, bool, ],
                    enabled: typing.Union[MetaOapg.properties.enabled, bool, ],
                    manually_grantable: typing.Union[MetaOapg.properties.manually_grantable, bool, ],
                    grant_count: typing.Union[MetaOapg.properties.grant_count, decimal.Decimal, int, ],
                    system: typing.Union[MetaOapg.properties.system, bool, ],
                    badge_type_id: typing.Union[MetaOapg.properties.badge_type_id, decimal.Decimal, int, ],
                    badge_grouping_id: typing.Union[MetaOapg.properties.badge_grouping_id, decimal.Decimal, int, ],
                    allow_title: typing.Union[MetaOapg.properties.allow_title, bool, ],
                    name: typing.Union[MetaOapg.properties.name, str, ],
                    id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, ],
                    show_posts: typing.Union[MetaOapg.properties.show_posts, bool, ],
                    slug: typing.Union[MetaOapg.properties.slug, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'badge':
                    return super().__new__(
                        cls,
                        *args,
                        listable=listable,
                        image_url=image_url,
                        query=query,
                        icon=icon,
                        description=description,
                        multiple_grant=multiple_grant,
                        auto_revoke=auto_revoke,
                        long_description=long_description,
                        trigger=trigger,
                        target_posts=target_posts,
                        enabled=enabled,
                        manually_grantable=manually_grantable,
                        grant_count=grant_count,
                        system=system,
                        badge_type_id=badge_type_id,
                        badge_grouping_id=badge_grouping_id,
                        allow_title=allow_title,
                        name=name,
                        id=id,
                        show_posts=show_posts,
                        slug=slug,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "badge_types": badge_types,
                "badge": badge,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    badge: MetaOapg.properties.badge
    badge_types: MetaOapg.properties.badge_types
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["badge"]) -> MetaOapg.properties.badge: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["badge_types"]) -> MetaOapg.properties.badge_types: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["badge"], typing_extensions.Literal["badge_types"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["badge"]) -> MetaOapg.properties.badge: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["badge_types"]) -> MetaOapg.properties.badge_types: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["badge"], typing_extensions.Literal["badge_types"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        badge: typing.Union[MetaOapg.properties.badge, dict, frozendict.frozendict, ],
        badge_types: typing.Union[MetaOapg.properties.badge_types, list, tuple, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs,
    ) -> 'BadgesUpdateBadgeByIdJsonResponse':
        return super().__new__(
            cls,
            *args,
            badge=badge,
            badge_types=badge_types,
            _configuration=_configuration,
        )
