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

from discourse_python_sdk.pydantic.posts_list_replies_to_post_response_item_actions_summary import PostsListRepliesToPostResponseItemActionsSummary
from discourse_python_sdk.pydantic.posts_list_replies_to_post_response_item_reply_to_user import PostsListRepliesToPostResponseItemReplyToUser

class PostsListRepliesToPostResponseItem(BaseModel):
    version: int = Field(alias='version')

    id: int = Field(alias='id')

    name: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='name')

    username: str = Field(alias='username')

    avatar_template: str = Field(alias='avatar_template')

    created_at: str = Field(alias='created_at')

    cooked: str = Field(alias='cooked')

    post_number: int = Field(alias='post_number')

    post_type: int = Field(alias='post_type')

    updated_at: str = Field(alias='updated_at')

    reply_count: int = Field(alias='reply_count')

    reply_to_post_number: int = Field(alias='reply_to_post_number')

    quote_count: int = Field(alias='quote_count')

    incoming_link_count: int = Field(alias='incoming_link_count')

    reads: int = Field(alias='reads')

    readers_count: int = Field(alias='readers_count')

    score: typing.Union[int, float] = Field(alias='score')

    yours: bool = Field(alias='yours')

    topic_id: int = Field(alias='topic_id')

    topic_slug: str = Field(alias='topic_slug')

    display_username: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='display_username')

    primary_group_name: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='primary_group_name')

    flair_name: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='flair_name')

    flair_url: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='flair_url')

    flair_bg_color: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='flair_bg_color')

    flair_color: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='flair_color')

    can_edit: bool = Field(alias='can_edit')

    can_delete: bool = Field(alias='can_delete')

    can_recover: bool = Field(alias='can_recover')

    can_see_hidden_post: bool = Field(alias='can_see_hidden_post')

    can_wiki: bool = Field(alias='can_wiki')

    user_title: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='user_title')

    reply_to_user: PostsListRepliesToPostResponseItemReplyToUser = Field(alias='reply_to_user')

    bookmarked: bool = Field(alias='bookmarked')

    actions_summary: PostsListRepliesToPostResponseItemActionsSummary = Field(alias='actions_summary')

    moderator: bool = Field(alias='moderator')

    admin: bool = Field(alias='admin')

    staff: bool = Field(alias='staff')

    user_id: int = Field(alias='user_id')

    hidden: bool = Field(alias='hidden')

    trust_level: int = Field(alias='trust_level')

    deleted_at: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='deleted_at')

    user_deleted: bool = Field(alias='user_deleted')

    edit_reason: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='edit_reason')

    can_view_edit_history: bool = Field(alias='can_view_edit_history')

    wiki: bool = Field(alias='wiki')

    reviewable_id: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='reviewable_id')

    reviewable_score_count: int = Field(alias='reviewable_score_count')

    reviewable_score_pending_count: int = Field(alias='reviewable_score_pending_count')

    flair_group_id: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='flair_group_id')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
