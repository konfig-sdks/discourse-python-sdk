# coding: utf-8

"""
    Discourse API Documentation

    This page contains the documentation on how to use Discourse through API calls.  > Note: For any endpoints not listed you can follow the [reverse engineer the Discourse API](https://meta.discourse.org/t/-/20576) guide to figure out how to use an API endpoint.  ### Request Content-Type  The Content-Type for POST and PUT requests can be set to `application/x-www-form-urlencoded`, `multipart/form-data`, or `application/json`.  ### Endpoint Names and Response Content-Type  Most API endpoints provide the same content as their HTML counterparts. For example the URL `/categories` serves a list of categories, the `/categories.json` API provides the same information in JSON format.  Instead of sending API requests to `/categories.json` you may also send them to `/categories` and add an `Accept: application/json` header to the request to get the JSON response. Sending requests with the `Accept` header is necessary if you want to use URLs for related endpoints returned by the API, such as pagination URLs. These URLs are returned without the `.json` prefix so you need to add the header in order to get the correct response format.  ### Authentication  Some endpoints do not require any authentication, pretty much anything else will require you to be authenticated.  To become authenticated you will need to create an API Key from the admin panel.  Once you have your API Key you can pass it in along with your API Username as an HTTP header like this:  ``` curl -X GET \"http://127.0.0.1:3000/admin/users/list/active.json\" \\ -H \"Api-Key: 714552c6148e1617aeab526d0606184b94a80ec048fc09894ff1a72b740c5f19\" \\ -H \"Api-Username: system\" ```  and this is how POST requests will look:  ``` curl -X POST \"http://127.0.0.1:3000/categories\" \\ -H \"Content-Type: multipart/form-data;\" \\ -H \"Api-Key: 714552c6148e1617aeab526d0606184b94a80ec048fc09894ff1a72b740c5f19\" \\ -H \"Api-Username: system\" \\ -F \"name=89853c20-4409-e91a-a8ea-f6cdff96aaaa\" \\ -F \"color=49d9e9\" \\ -F \"text_color=f0fcfd\" ```  ### Boolean values  If an endpoint accepts a boolean be sure to specify it as a lowercase `true` or `false` value unless noted otherwise. 

    The version of the OpenAPI document: latest
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel, ConfigDict


class TopicsGetSingleTopicResponse(BaseModel):
    tags: typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(alias='tags')

    title: str = Field(alias='title')

    post_stream: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(alias='post_stream')

    timeline_lookup: typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(alias='timeline_lookup')

    suggested_topics: typing.List[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(alias='suggested_topics')

    tags_descriptions: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(alias='tags_descriptions')

    id: int = Field(alias='id')

    fancy_title: str = Field(alias='fancy_title')

    posts_count: int = Field(alias='posts_count')

    created_at: str = Field(alias='created_at')

    views: int = Field(alias='views')

    reply_count: int = Field(alias='reply_count')

    like_count: int = Field(alias='like_count')

    last_posted_at: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='last_posted_at')

    visible: bool = Field(alias='visible')

    closed: bool = Field(alias='closed')

    archived: bool = Field(alias='archived')

    has_summary: bool = Field(alias='has_summary')

    archetype: str = Field(alias='archetype')

    slug: str = Field(alias='slug')

    category_id: int = Field(alias='category_id')

    word_count: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='word_count')

    deleted_at: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='deleted_at')

    user_id: int = Field(alias='user_id')

    featured_link: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='featured_link')

    pinned_globally: bool = Field(alias='pinned_globally')

    pinned_at: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='pinned_at')

    pinned_until: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='pinned_until')

    image_url: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='image_url')

    slow_mode_seconds: int = Field(alias='slow_mode_seconds')

    draft: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='draft')

    draft_key: str = Field(alias='draft_key')

    draft_sequence: int = Field(alias='draft_sequence')

    unpinned: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='unpinned')

    pinned: bool = Field(alias='pinned')

    highest_post_number: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='highest_post_number')

    deleted_by: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='deleted_by')

    has_deleted: bool = Field(alias='has_deleted')

    actions_summary: typing.List[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(alias='actions_summary')

    chunk_size: int = Field(alias='chunk_size')

    bookmarked: bool = Field(alias='bookmarked')

    bookmarks: typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(alias='bookmarks')

    topic_timer: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='topic_timer')

    message_bus_last_id: int = Field(alias='message_bus_last_id')

    participant_count: int = Field(alias='participant_count')

    show_read_indicator: bool = Field(alias='show_read_indicator')

    thumbnails: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='thumbnails')

    slow_mode_enabled_until: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='slow_mode_enabled_until')

    summarizable: bool = Field(alias='summarizable')

    details: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(alias='details')

    current_post_number: typing.Optional[int] = Field(None, alias='current_post_number')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )