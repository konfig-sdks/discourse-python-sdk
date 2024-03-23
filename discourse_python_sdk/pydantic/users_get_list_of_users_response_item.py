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

from discourse_python_sdk.pydantic.users_get_list_of_users_response_item_secondary_emails import UsersGetListOfUsersResponseItemSecondaryEmails

class UsersGetListOfUsersResponseItem(BaseModel):
    title: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='title')

    id: int = Field(alias='id')

    username: str = Field(alias='username')

    name: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='name')

    avatar_template: str = Field(alias='avatar_template')

    active: bool = Field(alias='active')

    admin: bool = Field(alias='admin')

    moderator: bool = Field(alias='moderator')

    last_seen_at: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='last_seen_at')

    last_emailed_at: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='last_emailed_at')

    created_at: str = Field(alias='created_at')

    last_seen_age: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='last_seen_age')

    last_emailed_age: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='last_emailed_age')

    created_at_age: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='created_at_age')

    trust_level: int = Field(alias='trust_level')

    manual_locked_trust_level: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='manual_locked_trust_level')

    time_read: int = Field(alias='time_read')

    staged: bool = Field(alias='staged')

    days_visited: int = Field(alias='days_visited')

    posts_read_count: int = Field(alias='posts_read_count')

    topics_entered: int = Field(alias='topics_entered')

    post_count: int = Field(alias='post_count')

    email: typing.Optional[str] = Field(None, alias='email')

    secondary_emails: typing.Optional[UsersGetListOfUsersResponseItemSecondaryEmails] = Field(None, alias='secondary_emails')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
