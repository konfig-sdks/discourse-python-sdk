# coding: utf-8

"""
    Discourse API Documentation

    This page contains the documentation on how to use Discourse through API calls.  > Note: For any endpoints not listed you can follow the [reverse engineer the Discourse API](https://meta.discourse.org/t/-/20576) guide to figure out how to use an API endpoint.  ### Request Content-Type  The Content-Type for POST and PUT requests can be set to `application/x-www-form-urlencoded`, `multipart/form-data`, or `application/json`.  ### Endpoint Names and Response Content-Type  Most API endpoints provide the same content as their HTML counterparts. For example the URL `/categories` serves a list of categories, the `/categories.json` API provides the same information in JSON format.  Instead of sending API requests to `/categories.json` you may also send them to `/categories` and add an `Accept: application/json` header to the request to get the JSON response. Sending requests with the `Accept` header is necessary if you want to use URLs for related endpoints returned by the API, such as pagination URLs. These URLs are returned without the `.json` prefix so you need to add the header in order to get the correct response format.  ### Authentication  Some endpoints do not require any authentication, pretty much anything else will require you to be authenticated.  To become authenticated you will need to create an API Key from the admin panel.  Once you have your API Key you can pass it in along with your API Username as an HTTP header like this:  ``` curl -X GET \"http://127.0.0.1:3000/admin/users/list/active.json\" \\ -H \"Api-Key: 714552c6148e1617aeab526d0606184b94a80ec048fc09894ff1a72b740c5f19\" \\ -H \"Api-Username: system\" ```  and this is how POST requests will look:  ``` curl -X POST \"http://127.0.0.1:3000/categories\" \\ -H \"Content-Type: multipart/form-data;\" \\ -H \"Api-Key: 714552c6148e1617aeab526d0606184b94a80ec048fc09894ff1a72b740c5f19\" \\ -H \"Api-Username: system\" \\ -F \"name=89853c20-4409-e91a-a8ea-f6cdff96aaaa\" \\ -F \"color=49d9e9\" \\ -F \"text_color=f0fcfd\" ```  ### Boolean values  If an endpoint accepts a boolean be sure to specify it as a lowercase `true` or `false` value unless noted otherwise. 

    The version of the OpenAPI document: latest
    Generated by: https://konfigthis.com
"""

from discourse_python_sdk.paths.posts_json.post import CreateTopicPostMessage
from discourse_python_sdk.paths.t_id_timer_json.post import CreateTopicTimer
from discourse_python_sdk.paths.t_external_id_external_id_json.get import GetByExternalId
from discourse_python_sdk.paths.latest_json.get import GetLatestTopics
from discourse_python_sdk.paths.t_id_json.get import GetSingleTopic
from discourse_python_sdk.paths.t_id_posts_json.get import GetSpecificPosts
from discourse_python_sdk.paths.top_json.get import GetTopTopicsByPeriod
from discourse_python_sdk.paths.t_id_json.delete import RemoveTopicById
from discourse_python_sdk.paths.t_id_invite_json.post import SendInviteToTopic
from discourse_python_sdk.paths.t_id_notifications_json.post import SetNotificationLevel
from discourse_python_sdk.paths.t_id_bookmark_json.put import UpdateBookmark
from discourse_python_sdk.paths.t_id_status_json.put import UpdateStatusOfTopic
from discourse_python_sdk.paths.t_id_change_timestamp_json.put import UpdateTimestampJson
from discourse_python_sdk.paths.t___id_json.put import UpdateTopicByIdJson
from discourse_python_sdk.apis.tags.topics_api_raw import TopicsApiRaw


class TopicsApi(
    CreateTopicPostMessage,
    CreateTopicTimer,
    GetByExternalId,
    GetLatestTopics,
    GetSingleTopic,
    GetSpecificPosts,
    GetTopTopicsByPeriod,
    RemoveTopicById,
    SendInviteToTopic,
    SetNotificationLevel,
    UpdateBookmark,
    UpdateStatusOfTopic,
    UpdateTimestampJson,
    UpdateTopicByIdJson,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: TopicsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = TopicsApiRaw(api_client)