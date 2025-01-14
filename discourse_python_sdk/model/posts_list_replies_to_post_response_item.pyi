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


class PostsListRepliesToPostResponseItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "flair_color",
            "moderator",
            "wiki",
            "trust_level",
            "can_see_hidden_post",
            "score",
            "can_view_edit_history",
            "reviewable_score_count",
            "actions_summary",
            "incoming_link_count",
            "can_delete",
            "post_type",
            "id",
            "readers_count",
            "edit_reason",
            "cooked",
            "reply_count",
            "reply_to_post_number",
            "deleted_at",
            "version",
            "reply_to_user",
            "user_id",
            "can_recover",
            "name",
            "user_title",
            "post_number",
            "hidden",
            "can_wiki",
            "admin",
            "created_at",
            "updated_at",
            "topic_id",
            "quote_count",
            "avatar_template",
            "bookmarked",
            "reads",
            "can_edit",
            "staff",
            "flair_url",
            "flair_bg_color",
            "reviewable_score_pending_count",
            "reviewable_id",
            "primary_group_name",
            "user_deleted",
            "yours",
            "flair_name",
            "topic_slug",
            "display_username",
            "username",
        }
        
        class properties:
            version = schemas.IntSchema
            id = schemas.IntSchema
            name = schemas.AnyTypeSchema
            username = schemas.StrSchema
            avatar_template = schemas.StrSchema
            created_at = schemas.StrSchema
            cooked = schemas.StrSchema
            post_number = schemas.IntSchema
            post_type = schemas.IntSchema
            updated_at = schemas.StrSchema
            reply_count = schemas.IntSchema
            reply_to_post_number = schemas.IntSchema
            quote_count = schemas.IntSchema
            incoming_link_count = schemas.IntSchema
            reads = schemas.IntSchema
            readers_count = schemas.IntSchema
            score = schemas.NumberSchema
            yours = schemas.BoolSchema
            topic_id = schemas.IntSchema
            topic_slug = schemas.StrSchema
            display_username = schemas.AnyTypeSchema
            primary_group_name = schemas.AnyTypeSchema
            flair_name = schemas.AnyTypeSchema
            flair_url = schemas.AnyTypeSchema
            flair_bg_color = schemas.AnyTypeSchema
            flair_color = schemas.AnyTypeSchema
            can_edit = schemas.BoolSchema
            can_delete = schemas.BoolSchema
            can_recover = schemas.BoolSchema
            can_see_hidden_post = schemas.BoolSchema
            can_wiki = schemas.BoolSchema
            user_title = schemas.AnyTypeSchema
        
            @staticmethod
            def reply_to_user() -> typing.Type['PostsListRepliesToPostResponseItemReplyToUser']:
                return PostsListRepliesToPostResponseItemReplyToUser
            bookmarked = schemas.BoolSchema
        
            @staticmethod
            def actions_summary() -> typing.Type['PostsListRepliesToPostResponseItemActionsSummary']:
                return PostsListRepliesToPostResponseItemActionsSummary
            moderator = schemas.BoolSchema
            admin = schemas.BoolSchema
            staff = schemas.BoolSchema
            user_id = schemas.IntSchema
            hidden = schemas.BoolSchema
            trust_level = schemas.IntSchema
            deleted_at = schemas.AnyTypeSchema
            user_deleted = schemas.BoolSchema
            edit_reason = schemas.AnyTypeSchema
            can_view_edit_history = schemas.BoolSchema
            wiki = schemas.BoolSchema
            reviewable_id = schemas.AnyTypeSchema
            reviewable_score_count = schemas.IntSchema
            reviewable_score_pending_count = schemas.IntSchema
            flair_group_id = schemas.AnyTypeSchema
            __annotations__ = {
                "version": version,
                "id": id,
                "name": name,
                "username": username,
                "avatar_template": avatar_template,
                "created_at": created_at,
                "cooked": cooked,
                "post_number": post_number,
                "post_type": post_type,
                "updated_at": updated_at,
                "reply_count": reply_count,
                "reply_to_post_number": reply_to_post_number,
                "quote_count": quote_count,
                "incoming_link_count": incoming_link_count,
                "reads": reads,
                "readers_count": readers_count,
                "score": score,
                "yours": yours,
                "topic_id": topic_id,
                "topic_slug": topic_slug,
                "display_username": display_username,
                "primary_group_name": primary_group_name,
                "flair_name": flair_name,
                "flair_url": flair_url,
                "flair_bg_color": flair_bg_color,
                "flair_color": flair_color,
                "can_edit": can_edit,
                "can_delete": can_delete,
                "can_recover": can_recover,
                "can_see_hidden_post": can_see_hidden_post,
                "can_wiki": can_wiki,
                "user_title": user_title,
                "reply_to_user": reply_to_user,
                "bookmarked": bookmarked,
                "actions_summary": actions_summary,
                "moderator": moderator,
                "admin": admin,
                "staff": staff,
                "user_id": user_id,
                "hidden": hidden,
                "trust_level": trust_level,
                "deleted_at": deleted_at,
                "user_deleted": user_deleted,
                "edit_reason": edit_reason,
                "can_view_edit_history": can_view_edit_history,
                "wiki": wiki,
                "reviewable_id": reviewable_id,
                "reviewable_score_count": reviewable_score_count,
                "reviewable_score_pending_count": reviewable_score_pending_count,
                "flair_group_id": flair_group_id,
            }
    
    flair_color: MetaOapg.properties.flair_color
    moderator: MetaOapg.properties.moderator
    wiki: MetaOapg.properties.wiki
    trust_level: MetaOapg.properties.trust_level
    can_see_hidden_post: MetaOapg.properties.can_see_hidden_post
    score: MetaOapg.properties.score
    can_view_edit_history: MetaOapg.properties.can_view_edit_history
    reviewable_score_count: MetaOapg.properties.reviewable_score_count
    actions_summary: 'PostsListRepliesToPostResponseItemActionsSummary'
    incoming_link_count: MetaOapg.properties.incoming_link_count
    can_delete: MetaOapg.properties.can_delete
    post_type: MetaOapg.properties.post_type
    id: MetaOapg.properties.id
    readers_count: MetaOapg.properties.readers_count
    edit_reason: MetaOapg.properties.edit_reason
    cooked: MetaOapg.properties.cooked
    reply_count: MetaOapg.properties.reply_count
    reply_to_post_number: MetaOapg.properties.reply_to_post_number
    deleted_at: MetaOapg.properties.deleted_at
    version: MetaOapg.properties.version
    reply_to_user: 'PostsListRepliesToPostResponseItemReplyToUser'
    user_id: MetaOapg.properties.user_id
    can_recover: MetaOapg.properties.can_recover
    name: MetaOapg.properties.name
    user_title: MetaOapg.properties.user_title
    post_number: MetaOapg.properties.post_number
    hidden: MetaOapg.properties.hidden
    can_wiki: MetaOapg.properties.can_wiki
    admin: MetaOapg.properties.admin
    created_at: MetaOapg.properties.created_at
    updated_at: MetaOapg.properties.updated_at
    topic_id: MetaOapg.properties.topic_id
    quote_count: MetaOapg.properties.quote_count
    avatar_template: MetaOapg.properties.avatar_template
    bookmarked: MetaOapg.properties.bookmarked
    reads: MetaOapg.properties.reads
    can_edit: MetaOapg.properties.can_edit
    staff: MetaOapg.properties.staff
    flair_url: MetaOapg.properties.flair_url
    flair_bg_color: MetaOapg.properties.flair_bg_color
    reviewable_score_pending_count: MetaOapg.properties.reviewable_score_pending_count
    reviewable_id: MetaOapg.properties.reviewable_id
    primary_group_name: MetaOapg.properties.primary_group_name
    user_deleted: MetaOapg.properties.user_deleted
    yours: MetaOapg.properties.yours
    flair_name: MetaOapg.properties.flair_name
    topic_slug: MetaOapg.properties.topic_slug
    display_username: MetaOapg.properties.display_username
    username: MetaOapg.properties.username
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["version"]) -> MetaOapg.properties.version: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["username"]) -> MetaOapg.properties.username: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["avatar_template"]) -> MetaOapg.properties.avatar_template: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cooked"]) -> MetaOapg.properties.cooked: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["post_number"]) -> MetaOapg.properties.post_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["post_type"]) -> MetaOapg.properties.post_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reply_count"]) -> MetaOapg.properties.reply_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reply_to_post_number"]) -> MetaOapg.properties.reply_to_post_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["quote_count"]) -> MetaOapg.properties.quote_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["incoming_link_count"]) -> MetaOapg.properties.incoming_link_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reads"]) -> MetaOapg.properties.reads: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["readers_count"]) -> MetaOapg.properties.readers_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["score"]) -> MetaOapg.properties.score: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["yours"]) -> MetaOapg.properties.yours: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["topic_id"]) -> MetaOapg.properties.topic_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["topic_slug"]) -> MetaOapg.properties.topic_slug: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["display_username"]) -> MetaOapg.properties.display_username: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["primary_group_name"]) -> MetaOapg.properties.primary_group_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["flair_name"]) -> MetaOapg.properties.flair_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["flair_url"]) -> MetaOapg.properties.flair_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["flair_bg_color"]) -> MetaOapg.properties.flair_bg_color: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["flair_color"]) -> MetaOapg.properties.flair_color: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["can_edit"]) -> MetaOapg.properties.can_edit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["can_delete"]) -> MetaOapg.properties.can_delete: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["can_recover"]) -> MetaOapg.properties.can_recover: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["can_see_hidden_post"]) -> MetaOapg.properties.can_see_hidden_post: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["can_wiki"]) -> MetaOapg.properties.can_wiki: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_title"]) -> MetaOapg.properties.user_title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reply_to_user"]) -> 'PostsListRepliesToPostResponseItemReplyToUser': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bookmarked"]) -> MetaOapg.properties.bookmarked: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["actions_summary"]) -> 'PostsListRepliesToPostResponseItemActionsSummary': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["moderator"]) -> MetaOapg.properties.moderator: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["admin"]) -> MetaOapg.properties.admin: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["staff"]) -> MetaOapg.properties.staff: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_id"]) -> MetaOapg.properties.user_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hidden"]) -> MetaOapg.properties.hidden: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trust_level"]) -> MetaOapg.properties.trust_level: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deleted_at"]) -> MetaOapg.properties.deleted_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_deleted"]) -> MetaOapg.properties.user_deleted: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["edit_reason"]) -> MetaOapg.properties.edit_reason: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["can_view_edit_history"]) -> MetaOapg.properties.can_view_edit_history: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["wiki"]) -> MetaOapg.properties.wiki: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reviewable_id"]) -> MetaOapg.properties.reviewable_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reviewable_score_count"]) -> MetaOapg.properties.reviewable_score_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reviewable_score_pending_count"]) -> MetaOapg.properties.reviewable_score_pending_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["flair_group_id"]) -> MetaOapg.properties.flair_group_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["version", "id", "name", "username", "avatar_template", "created_at", "cooked", "post_number", "post_type", "updated_at", "reply_count", "reply_to_post_number", "quote_count", "incoming_link_count", "reads", "readers_count", "score", "yours", "topic_id", "topic_slug", "display_username", "primary_group_name", "flair_name", "flair_url", "flair_bg_color", "flair_color", "can_edit", "can_delete", "can_recover", "can_see_hidden_post", "can_wiki", "user_title", "reply_to_user", "bookmarked", "actions_summary", "moderator", "admin", "staff", "user_id", "hidden", "trust_level", "deleted_at", "user_deleted", "edit_reason", "can_view_edit_history", "wiki", "reviewable_id", "reviewable_score_count", "reviewable_score_pending_count", "flair_group_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["version"]) -> MetaOapg.properties.version: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["username"]) -> MetaOapg.properties.username: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["avatar_template"]) -> MetaOapg.properties.avatar_template: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cooked"]) -> MetaOapg.properties.cooked: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["post_number"]) -> MetaOapg.properties.post_number: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["post_type"]) -> MetaOapg.properties.post_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reply_count"]) -> MetaOapg.properties.reply_count: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reply_to_post_number"]) -> MetaOapg.properties.reply_to_post_number: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["quote_count"]) -> MetaOapg.properties.quote_count: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["incoming_link_count"]) -> MetaOapg.properties.incoming_link_count: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reads"]) -> MetaOapg.properties.reads: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["readers_count"]) -> MetaOapg.properties.readers_count: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["score"]) -> MetaOapg.properties.score: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["yours"]) -> MetaOapg.properties.yours: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["topic_id"]) -> MetaOapg.properties.topic_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["topic_slug"]) -> MetaOapg.properties.topic_slug: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["display_username"]) -> MetaOapg.properties.display_username: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["primary_group_name"]) -> MetaOapg.properties.primary_group_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["flair_name"]) -> MetaOapg.properties.flair_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["flair_url"]) -> MetaOapg.properties.flair_url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["flair_bg_color"]) -> MetaOapg.properties.flair_bg_color: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["flair_color"]) -> MetaOapg.properties.flair_color: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["can_edit"]) -> MetaOapg.properties.can_edit: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["can_delete"]) -> MetaOapg.properties.can_delete: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["can_recover"]) -> MetaOapg.properties.can_recover: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["can_see_hidden_post"]) -> MetaOapg.properties.can_see_hidden_post: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["can_wiki"]) -> MetaOapg.properties.can_wiki: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_title"]) -> MetaOapg.properties.user_title: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reply_to_user"]) -> 'PostsListRepliesToPostResponseItemReplyToUser': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bookmarked"]) -> MetaOapg.properties.bookmarked: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["actions_summary"]) -> 'PostsListRepliesToPostResponseItemActionsSummary': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["moderator"]) -> MetaOapg.properties.moderator: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["admin"]) -> MetaOapg.properties.admin: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["staff"]) -> MetaOapg.properties.staff: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_id"]) -> MetaOapg.properties.user_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hidden"]) -> MetaOapg.properties.hidden: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trust_level"]) -> MetaOapg.properties.trust_level: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deleted_at"]) -> MetaOapg.properties.deleted_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_deleted"]) -> MetaOapg.properties.user_deleted: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["edit_reason"]) -> MetaOapg.properties.edit_reason: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["can_view_edit_history"]) -> MetaOapg.properties.can_view_edit_history: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["wiki"]) -> MetaOapg.properties.wiki: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reviewable_id"]) -> MetaOapg.properties.reviewable_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reviewable_score_count"]) -> MetaOapg.properties.reviewable_score_count: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reviewable_score_pending_count"]) -> MetaOapg.properties.reviewable_score_pending_count: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["flair_group_id"]) -> typing.Union[MetaOapg.properties.flair_group_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["version", "id", "name", "username", "avatar_template", "created_at", "cooked", "post_number", "post_type", "updated_at", "reply_count", "reply_to_post_number", "quote_count", "incoming_link_count", "reads", "readers_count", "score", "yours", "topic_id", "topic_slug", "display_username", "primary_group_name", "flair_name", "flair_url", "flair_bg_color", "flair_color", "can_edit", "can_delete", "can_recover", "can_see_hidden_post", "can_wiki", "user_title", "reply_to_user", "bookmarked", "actions_summary", "moderator", "admin", "staff", "user_id", "hidden", "trust_level", "deleted_at", "user_deleted", "edit_reason", "can_view_edit_history", "wiki", "reviewable_id", "reviewable_score_count", "reviewable_score_pending_count", "flair_group_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        flair_color: typing.Union[MetaOapg.properties.flair_color, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        moderator: typing.Union[MetaOapg.properties.moderator, bool, ],
        wiki: typing.Union[MetaOapg.properties.wiki, bool, ],
        trust_level: typing.Union[MetaOapg.properties.trust_level, decimal.Decimal, int, ],
        can_see_hidden_post: typing.Union[MetaOapg.properties.can_see_hidden_post, bool, ],
        score: typing.Union[MetaOapg.properties.score, decimal.Decimal, int, float, ],
        can_view_edit_history: typing.Union[MetaOapg.properties.can_view_edit_history, bool, ],
        reviewable_score_count: typing.Union[MetaOapg.properties.reviewable_score_count, decimal.Decimal, int, ],
        actions_summary: 'PostsListRepliesToPostResponseItemActionsSummary',
        incoming_link_count: typing.Union[MetaOapg.properties.incoming_link_count, decimal.Decimal, int, ],
        can_delete: typing.Union[MetaOapg.properties.can_delete, bool, ],
        post_type: typing.Union[MetaOapg.properties.post_type, decimal.Decimal, int, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, ],
        readers_count: typing.Union[MetaOapg.properties.readers_count, decimal.Decimal, int, ],
        edit_reason: typing.Union[MetaOapg.properties.edit_reason, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        cooked: typing.Union[MetaOapg.properties.cooked, str, ],
        reply_count: typing.Union[MetaOapg.properties.reply_count, decimal.Decimal, int, ],
        reply_to_post_number: typing.Union[MetaOapg.properties.reply_to_post_number, decimal.Decimal, int, ],
        deleted_at: typing.Union[MetaOapg.properties.deleted_at, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        version: typing.Union[MetaOapg.properties.version, decimal.Decimal, int, ],
        reply_to_user: 'PostsListRepliesToPostResponseItemReplyToUser',
        user_id: typing.Union[MetaOapg.properties.user_id, decimal.Decimal, int, ],
        can_recover: typing.Union[MetaOapg.properties.can_recover, bool, ],
        name: typing.Union[MetaOapg.properties.name, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        user_title: typing.Union[MetaOapg.properties.user_title, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        post_number: typing.Union[MetaOapg.properties.post_number, decimal.Decimal, int, ],
        hidden: typing.Union[MetaOapg.properties.hidden, bool, ],
        can_wiki: typing.Union[MetaOapg.properties.can_wiki, bool, ],
        admin: typing.Union[MetaOapg.properties.admin, bool, ],
        created_at: typing.Union[MetaOapg.properties.created_at, str, ],
        updated_at: typing.Union[MetaOapg.properties.updated_at, str, ],
        topic_id: typing.Union[MetaOapg.properties.topic_id, decimal.Decimal, int, ],
        quote_count: typing.Union[MetaOapg.properties.quote_count, decimal.Decimal, int, ],
        avatar_template: typing.Union[MetaOapg.properties.avatar_template, str, ],
        bookmarked: typing.Union[MetaOapg.properties.bookmarked, bool, ],
        reads: typing.Union[MetaOapg.properties.reads, decimal.Decimal, int, ],
        can_edit: typing.Union[MetaOapg.properties.can_edit, bool, ],
        staff: typing.Union[MetaOapg.properties.staff, bool, ],
        flair_url: typing.Union[MetaOapg.properties.flair_url, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        flair_bg_color: typing.Union[MetaOapg.properties.flair_bg_color, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        reviewable_score_pending_count: typing.Union[MetaOapg.properties.reviewable_score_pending_count, decimal.Decimal, int, ],
        reviewable_id: typing.Union[MetaOapg.properties.reviewable_id, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        primary_group_name: typing.Union[MetaOapg.properties.primary_group_name, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        user_deleted: typing.Union[MetaOapg.properties.user_deleted, bool, ],
        yours: typing.Union[MetaOapg.properties.yours, bool, ],
        flair_name: typing.Union[MetaOapg.properties.flair_name, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        topic_slug: typing.Union[MetaOapg.properties.topic_slug, str, ],
        display_username: typing.Union[MetaOapg.properties.display_username, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        username: typing.Union[MetaOapg.properties.username, str, ],
        flair_group_id: typing.Union[MetaOapg.properties.flair_group_id, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PostsListRepliesToPostResponseItem':
        return super().__new__(
            cls,
            *args,
            flair_color=flair_color,
            moderator=moderator,
            wiki=wiki,
            trust_level=trust_level,
            can_see_hidden_post=can_see_hidden_post,
            score=score,
            can_view_edit_history=can_view_edit_history,
            reviewable_score_count=reviewable_score_count,
            actions_summary=actions_summary,
            incoming_link_count=incoming_link_count,
            can_delete=can_delete,
            post_type=post_type,
            id=id,
            readers_count=readers_count,
            edit_reason=edit_reason,
            cooked=cooked,
            reply_count=reply_count,
            reply_to_post_number=reply_to_post_number,
            deleted_at=deleted_at,
            version=version,
            reply_to_user=reply_to_user,
            user_id=user_id,
            can_recover=can_recover,
            name=name,
            user_title=user_title,
            post_number=post_number,
            hidden=hidden,
            can_wiki=can_wiki,
            admin=admin,
            created_at=created_at,
            updated_at=updated_at,
            topic_id=topic_id,
            quote_count=quote_count,
            avatar_template=avatar_template,
            bookmarked=bookmarked,
            reads=reads,
            can_edit=can_edit,
            staff=staff,
            flair_url=flair_url,
            flair_bg_color=flair_bg_color,
            reviewable_score_pending_count=reviewable_score_pending_count,
            reviewable_id=reviewable_id,
            primary_group_name=primary_group_name,
            user_deleted=user_deleted,
            yours=yours,
            flair_name=flair_name,
            topic_slug=topic_slug,
            display_username=display_username,
            username=username,
            flair_group_id=flair_group_id,
            _configuration=_configuration,
            **kwargs,
        )

from discourse_python_sdk.model.posts_list_replies_to_post_response_item_actions_summary import PostsListRepliesToPostResponseItemActionsSummary
from discourse_python_sdk.model.posts_list_replies_to_post_response_item_reply_to_user import PostsListRepliesToPostResponseItemReplyToUser
