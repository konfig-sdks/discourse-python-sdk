# coding: utf-8

"""
    Discourse API Documentation

    This page contains the documentation on how to use Discourse through API calls.  > Note: For any endpoints not listed you can follow the [reverse engineer the Discourse API](https://meta.discourse.org/t/-/20576) guide to figure out how to use an API endpoint.  ### Request Content-Type  The Content-Type for POST and PUT requests can be set to `application/x-www-form-urlencoded`, `multipart/form-data`, or `application/json`.  ### Endpoint Names and Response Content-Type  Most API endpoints provide the same content as their HTML counterparts. For example the URL `/categories` serves a list of categories, the `/categories.json` API provides the same information in JSON format.  Instead of sending API requests to `/categories.json` you may also send them to `/categories` and add an `Accept: application/json` header to the request to get the JSON response. Sending requests with the `Accept` header is necessary if you want to use URLs for related endpoints returned by the API, such as pagination URLs. These URLs are returned without the `.json` prefix so you need to add the header in order to get the correct response format.  ### Authentication  Some endpoints do not require any authentication, pretty much anything else will require you to be authenticated.  To become authenticated you will need to create an API Key from the admin panel.  Once you have your API Key you can pass it in along with your API Username as an HTTP header like this:  ``` curl -X GET \"http://127.0.0.1:3000/admin/users/list/active.json\" \\ -H \"Api-Key: 714552c6148e1617aeab526d0606184b94a80ec048fc09894ff1a72b740c5f19\" \\ -H \"Api-Username: system\" ```  and this is how POST requests will look:  ``` curl -X POST \"http://127.0.0.1:3000/categories\" \\ -H \"Content-Type: multipart/form-data;\" \\ -H \"Api-Key: 714552c6148e1617aeab526d0606184b94a80ec048fc09894ff1a72b740c5f19\" \\ -H \"Api-Username: system\" \\ -F \"name=89853c20-4409-e91a-a8ea-f6cdff96aaaa\" \\ -F \"color=49d9e9\" \\ -F \"text_color=f0fcfd\" ```  ### Boolean values  If an endpoint accepts a boolean be sure to specify it as a lowercase `true` or `false` value unless noted otherwise. 

    The version of the OpenAPI document: latest
    Generated by: https://konfigthis.com
"""

from discourse_python_sdk.paths.admin_users_id_activate_json.put import ActivateUser
from discourse_python_sdk.paths.admin_users_id_anonymize_json.put import AnonymizeByIdJson
from discourse_python_sdk.paths.users_password_reset_token_json.put import ChangePasswordAction
from discourse_python_sdk.paths.users_json.post import CreateUser
from discourse_python_sdk.paths.admin_users_id_deactivate_json.put import DeactivateUser
from discourse_python_sdk.paths.admin_users_id_json.delete import DeleteUserByIdJson
from discourse_python_sdk.paths.u_username_emails_json.get import GetEmails
from discourse_python_sdk.paths.u_by_external_provider_external_id_json.get import GetIdentityProviderExternalId
from discourse_python_sdk.paths.admin_users_list_flag_json.get import GetListOfUsers
from discourse_python_sdk.paths.u_by_external_external_id_json.get import GetUserByExternalId
from discourse_python_sdk.paths.admin_users_id_json.get import GetUserByIdJson
from discourse_python_sdk.paths.u_username_json.get import GetUserByUsername
from discourse_python_sdk.paths.directory_items_json.get import ListPublicUser
from discourse_python_sdk.paths.user_actions_json.get import ListUserActions
from discourse_python_sdk.paths.user_badges_username_json.get import ListUserBadges
from discourse_python_sdk.paths.admin_users_id_log_out_json.post import LogOutUserAction
from discourse_python_sdk.paths.user_avatar_username_refresh_gravatar_json.post import RefreshGravatarPost
from discourse_python_sdk.paths.session_forgot_password_json.post import SendPasswordResetEmail
from discourse_python_sdk.paths.admin_users_id_silence_json.put import SilenceById
from discourse_python_sdk.paths.admin_users_id_suspend_json.put import SuspendByIdJson
from discourse_python_sdk.paths.u_username_preferences_avatar_pick_json.put import UpdateAvatar
from discourse_python_sdk.paths.u_username_preferences_email_json.put import UpdateEmailPreferences
from discourse_python_sdk.paths.u_username_preferences_username_json.put import UpdatePreferencesJson
from discourse_python_sdk.paths.u_username_json.put import UpdateUserDetails
from discourse_python_sdk.apis.tags.users_api_raw import UsersApiRaw


class UsersApi(
    ActivateUser,
    AnonymizeByIdJson,
    ChangePasswordAction,
    CreateUser,
    DeactivateUser,
    DeleteUserByIdJson,
    GetEmails,
    GetIdentityProviderExternalId,
    GetListOfUsers,
    GetUserByExternalId,
    GetUserByIdJson,
    GetUserByUsername,
    ListPublicUser,
    ListUserActions,
    ListUserBadges,
    LogOutUserAction,
    RefreshGravatarPost,
    SendPasswordResetEmail,
    SilenceById,
    SuspendByIdJson,
    UpdateAvatar,
    UpdateEmailPreferences,
    UpdatePreferencesJson,
    UpdateUserDetails,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: UsersApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = UsersApiRaw(api_client)
