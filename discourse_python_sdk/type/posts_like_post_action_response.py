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

from discourse_python_sdk.type.posts_like_post_action_response_actions_summary import PostsLikePostActionResponseActionsSummary

class RequiredPostsLikePostActionResponse(TypedDict):
    pass

class OptionalPostsLikePostActionResponse(TypedDict, total=False):
    version: int

    id: int

    name: str

    username: str

    avatar_template: str

    created_at: str

    cooked: str

    post_number: int

    post_type: int

    updated_at: str

    reply_count: int

    reply_to_post_number: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    quote_count: int

    incoming_link_count: int

    reads: int

    readers_count: int

    score: typing.Union[int, float]

    yours: bool

    topic_id: int

    topic_slug: str

    display_username: str

    primary_group_name: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    flair_name: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    flair_url: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    flair_bg_color: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    flair_color: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    can_edit: bool

    can_delete: bool

    can_recover: bool

    can_wiki: bool

    user_title: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    actions_summary: PostsLikePostActionResponseActionsSummary

    moderator: bool

    admin: bool

    staff: bool

    user_id: int

    hidden: bool

    trust_level: int

    deleted_at: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    user_deleted: bool

    edit_reason: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    can_view_edit_history: bool

    wiki: bool

    notice: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    reviewable_id: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    reviewable_score_count: int

    reviewable_score_pending_count: int

class PostsLikePostActionResponse(RequiredPostsLikePostActionResponse, OptionalPostsLikePostActionResponse):
    pass