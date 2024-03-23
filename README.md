<div align="left">

[![Visit Discourse](./header.png)](https://discourse.org)

# Discourse<a id="discourse"></a>

This page contains the documentation on how to use Discourse through API calls.

> Note: For any endpoints not listed you can follow the
[reverse engineer the Discourse API](https://meta.discourse.org/t/-/20576)
guide to figure out how to use an API endpoint.

### Request Content-Type<a id="request-content-type"></a>

The Content-Type for POST and PUT requests can be set to `application/x-www-form-urlencoded`,
`multipart/form-data`, or `application/json`.

### Endpoint Names and Response Content-Type<a id="endpoint-names-and-response-content-type"></a>

Most API endpoints provide the same content as their HTML counterparts. For example
the URL `/categories` serves a list of categories, the `/categories.json` API provides the
same information in JSON format.

Instead of sending API requests to `/categories.json` you may also send them to `/categories`
and add an `Accept: application/json` header to the request to get the JSON response.
Sending requests with the `Accept` header is necessary if you want to use URLs
for related endpoints returned by the API, such as pagination URLs.
These URLs are returned without the `.json` prefix so you need to add the header in
order to get the correct response format.

### Authentication<a id="authentication"></a>

Some endpoints do not require any authentication, pretty much anything else will
require you to be authenticated.

To become authenticated you will need to create an API Key from the admin panel.

Once you have your API Key you can pass it in along with your API Username
as an HTTP header like this:

```
curl -X GET \"http://127.0.0.1:3000/admin/users/list/active.json\" \\
-H \"Api-Key: 714552c6148e1617aeab526d0606184b94a80ec048fc09894ff1a72b740c5f19\" \\
-H \"Api-Username: system\"
```

and this is how POST requests will look:

```
curl -X POST \"http://127.0.0.1:3000/categories\" \\
-H \"Content-Type: multipart/form-data;\" \\
-H \"Api-Key: 714552c6148e1617aeab526d0606184b94a80ec048fc09894ff1a72b740c5f19\" \\
-H \"Api-Username: system\" \\
-F \"name=89853c20-4409-e91a-a8ea-f6cdff96aaaa\" \\
-F \"color=49d9e9\" \\
-F \"text_color=f0fcfd\"
```

### Boolean values<a id="boolean-values"></a>

If an endpoint accepts a boolean be sure to specify it as a lowercase
`true` or `false` value unless noted otherwise.



</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`discourse.admin.activate_user`](#discourseadminactivate_user)
  * [`discourse.admin.anonymize_by_id_json`](#discourseadminanonymize_by_id_json)
  * [`discourse.admin.deactivate_user`](#discourseadmindeactivate_user)
  * [`discourse.admin.delete_user_by_id_json`](#discourseadmindelete_user_by_id_json)
  * [`discourse.admin.get_list_of_users`](#discourseadminget_list_of_users)
  * [`discourse.admin.get_user_by_id_json`](#discourseadminget_user_by_id_json)
  * [`discourse.admin.log_out_user_action`](#discourseadminlog_out_user_action)
  * [`discourse.admin.refresh_gravatar_post`](#discourseadminrefresh_gravatar_post)
  * [`discourse.admin.silence_by_id`](#discourseadminsilence_by_id)
  * [`discourse.admin.suspend_by_id_json`](#discourseadminsuspend_by_id_json)
  * [`discourse.backups.create_backup_request`](#discoursebackupscreate_backup_request)
  * [`discourse.backups.download_backup`](#discoursebackupsdownload_backup)
  * [`discourse.backups.list`](#discoursebackupslist)
  * [`discourse.backups.send_download_backup_email`](#discoursebackupssend_download_backup_email)
  * [`discourse.badges.create_badge`](#discoursebadgescreate_badge)
  * [`discourse.badges.delete_by_id_json`](#discoursebadgesdelete_by_id_json)
  * [`discourse.badges.list`](#discoursebadgeslist)
  * [`discourse.badges.list_user_badges`](#discoursebadgeslist_user_badges)
  * [`discourse.badges.update_badge_by_id_json`](#discoursebadgesupdate_badge_by_id_json)
  * [`discourse.categories.create_category_request`](#discoursecategoriescreate_category_request)
  * [`discourse.categories.get_categories_and_subcategories`](#discoursecategoriesget_categories_and_subcategories)
  * [`discourse.categories.get_category_by_id_json`](#discoursecategoriesget_category_by_id_json)
  * [`discourse.categories.list`](#discoursecategorieslist)
  * [`discourse.categories.list_topics`](#discoursecategorieslist_topics)
  * [`discourse.categories.update_category_by_id_json`](#discoursecategoriesupdate_category_by_id_json)
  * [`discourse.groups.add_members_to_group`](#discoursegroupsadd_members_to_group)
  * [`discourse.groups.create_new_group`](#discoursegroupscreate_new_group)
  * [`discourse.groups.delete_group_by_id_json`](#discoursegroupsdelete_group_by_id_json)
  * [`discourse.groups.get_group_by_id`](#discoursegroupsget_group_by_id)
  * [`discourse.groups.list`](#discoursegroupslist)
  * [`discourse.groups.list_members_json`](#discoursegroupslist_members_json)
  * [`discourse.groups.remove_members`](#discoursegroupsremove_members)
  * [`discourse.groups.update_group_by_id_json`](#discoursegroupsupdate_group_by_id_json)
  * [`discourse.invites.create_invite`](#discourseinvitescreate_invite)
  * [`discourse.invites.create_multiple_invites`](#discourseinvitescreate_multiple_invites)
  * [`discourse.invites.send_invite_to_topic`](#discourseinvitessend_invite_to_topic)
  * [`discourse.notifications.get_user_notifications`](#discoursenotificationsget_user_notifications)
  * [`discourse.notifications.mark_as_read`](#discoursenotificationsmark_as_read)
  * [`discourse.posts.create_topic_post_message`](#discoursepostscreate_topic_post_message)
  * [`discourse.posts.delete_single_post`](#discoursepostsdelete_single_post)
  * [`discourse.posts.get_single_post_likes`](#discoursepostsget_single_post_likes)
  * [`discourse.posts.like_post_action`](#discoursepostslike_post_action)
  * [`discourse.posts.list_latest_posts_across_topics`](#discoursepostslist_latest_posts_across_topics)
  * [`discourse.posts.list_replies_to_post`](#discoursepostslist_replies_to_post)
  * [`discourse.posts.lock_post_action`](#discoursepostslock_post_action)
  * [`discourse.posts.update_single_post_json`](#discoursepostsupdate_single_post_json)
  * [`discourse.private_messages.create_topic_post_message`](#discourseprivate_messagescreate_topic_post_message)
  * [`discourse.private_messages.list_for_user`](#discourseprivate_messageslist_for_user)
  * [`discourse.private_messages.list_sent_for_user`](#discourseprivate_messageslist_sent_for_user)
  * [`discourse.search.term_results`](#discoursesearchterm_results)
  * [`discourse.site.get_categories_and_subcategories`](#discoursesiteget_categories_and_subcategories)
  * [`discourse.tags.create_tag_group`](#discoursetagscreate_tag_group)
  * [`discourse.tags.get_single_tag_group`](#discoursetagsget_single_tag_group)
  * [`discourse.tags.get_specific_tag`](#discoursetagsget_specific_tag)
  * [`discourse.tags.get_tag_groups`](#discoursetagsget_tag_groups)
  * [`discourse.tags.list`](#discoursetagslist)
  * [`discourse.tags.update_tag_group`](#discoursetagsupdate_tag_group)
  * [`discourse.topics.create_topic_post_message`](#discoursetopicscreate_topic_post_message)
  * [`discourse.topics.create_topic_timer`](#discoursetopicscreate_topic_timer)
  * [`discourse.topics.get_by_external_id`](#discoursetopicsget_by_external_id)
  * [`discourse.topics.get_latest_topics`](#discoursetopicsget_latest_topics)
  * [`discourse.topics.get_single_topic`](#discoursetopicsget_single_topic)
  * [`discourse.topics.get_specific_posts`](#discoursetopicsget_specific_posts)
  * [`discourse.topics.get_top_topics_by_period`](#discoursetopicsget_top_topics_by_period)
  * [`discourse.topics.remove_topic_by_id`](#discoursetopicsremove_topic_by_id)
  * [`discourse.topics.send_invite_to_topic`](#discoursetopicssend_invite_to_topic)
  * [`discourse.topics.set_notification_level`](#discoursetopicsset_notification_level)
  * [`discourse.topics.update_bookmark`](#discoursetopicsupdate_bookmark)
  * [`discourse.topics.update_status_of_topic`](#discoursetopicsupdate_status_of_topic)
  * [`discourse.topics.update_timestamp_json`](#discoursetopicsupdate_timestamp_json)
  * [`discourse.topics.update_topic_by_id_json`](#discoursetopicsupdate_topic_by_id_json)
  * [`discourse.uploads.abort_multipart_upload`](#discourseuploadsabort_multipart_upload)
  * [`discourse.uploads.complete_external_upload`](#discourseuploadscomplete_external_upload)
  * [`discourse.uploads.complete_multipart_upload`](#discourseuploadscomplete_multipart_upload)
  * [`discourse.uploads.create_multipart_external_upload`](#discourseuploadscreate_multipart_external_upload)
  * [`discourse.uploads.create_new_upload`](#discourseuploadscreate_new_upload)
  * [`discourse.uploads.generate_presigned_urls_for_multipart_parts`](#discourseuploadsgenerate_presigned_urls_for_multipart_parts)
  * [`discourse.uploads.initiate_direct_external_upload`](#discourseuploadsinitiate_direct_external_upload)
  * [`discourse.users.activate_user`](#discourseusersactivate_user)
  * [`discourse.users.anonymize_by_id_json`](#discourseusersanonymize_by_id_json)
  * [`discourse.users.change_password_action`](#discourseuserschange_password_action)
  * [`discourse.users.create_user`](#discourseuserscreate_user)
  * [`discourse.users.deactivate_user`](#discourseusersdeactivate_user)
  * [`discourse.users.delete_user_by_id_json`](#discourseusersdelete_user_by_id_json)
  * [`discourse.users.get_emails`](#discourseusersget_emails)
  * [`discourse.users.get_identity_provider_external_id`](#discourseusersget_identity_provider_external_id)
  * [`discourse.users.get_list_of_users`](#discourseusersget_list_of_users)
  * [`discourse.users.get_user_by_external_id`](#discourseusersget_user_by_external_id)
  * [`discourse.users.get_user_by_id_json`](#discourseusersget_user_by_id_json)
  * [`discourse.users.get_user_by_username`](#discourseusersget_user_by_username)
  * [`discourse.users.list_public_user`](#discourseuserslist_public_user)
  * [`discourse.users.list_user_actions`](#discourseuserslist_user_actions)
  * [`discourse.users.list_user_badges`](#discourseuserslist_user_badges)
  * [`discourse.users.log_out_user_action`](#discourseuserslog_out_user_action)
  * [`discourse.users.refresh_gravatar_post`](#discourseusersrefresh_gravatar_post)
  * [`discourse.users.send_password_reset_email`](#discourseuserssend_password_reset_email)
  * [`discourse.users.silence_by_id`](#discourseuserssilence_by_id)
  * [`discourse.users.suspend_by_id_json`](#discourseuserssuspend_by_id_json)
  * [`discourse.users.update_avatar`](#discourseusersupdate_avatar)
  * [`discourse.users.update_email_preferences`](#discourseusersupdate_email_preferences)
  * [`discourse.users.update_preferences_json`](#discourseusersupdate_preferences_json)
  * [`discourse.users.update_user_details`](#discourseusersupdate_user_details)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Discourse&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from discourse_python_sdk import Discourse, ApiException

discourse = Discourse()

try:
    # Activate a user
    activate_user_response = discourse.admin.activate_user(
        id=1,
    )
    print(activate_user_response)
except ApiException as e:
    print("Exception when calling AdminApi.activate_user: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from discourse_python_sdk import Discourse, ApiException

discourse = Discourse()


async def main():
    try:
        # Activate a user
        activate_user_response = await discourse.admin.aactivate_user(
            id=1,
        )
        print(activate_user_response)
    except ApiException as e:
        print("Exception when calling AdminApi.activate_user: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from discourse_python_sdk import Discourse, ApiException

discourse = Discourse()

try:
    # Activate a user
    activate_user_response = discourse.admin.raw.activate_user(
        id=1,
    )
    pprint(activate_user_response.body)
    pprint(activate_user_response.body["success"])
    pprint(activate_user_response.headers)
    pprint(activate_user_response.status)
    pprint(activate_user_response.round_trip_time)
except ApiException as e:
    print("Exception when calling AdminApi.activate_user: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `discourse.admin.activate_user`<a id="discourseadminactivate_user"></a>

Activate a user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
activate_user_response = discourse.admin.activate_user(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UsersActivateUserResponse`](./discourse_python_sdk/pydantic/users_activate_user_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/admin/users/{id}/activate.json` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.admin.anonymize_by_id_json`<a id="discourseadminanonymize_by_id_json"></a>

Anonymize a user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
anonymize_by_id_json_response = discourse.admin.anonymize_by_id_json(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UsersAnonymizeByIdJsonResponse`](./discourse_python_sdk/pydantic/users_anonymize_by_id_json_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/admin/users/{id}/anonymize.json` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.admin.deactivate_user`<a id="discourseadmindeactivate_user"></a>

Deactivate a user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
deactivate_user_response = discourse.admin.deactivate_user(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UsersDeactivateUserResponse`](./discourse_python_sdk/pydantic/users_deactivate_user_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/admin/users/{id}/deactivate.json` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.admin.delete_user_by_id_json`<a id="discourseadmindelete_user_by_id_json"></a>

Delete a user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_user_by_id_json_response = discourse.admin.delete_user_by_id_json(
    id=1,
    delete_posts=True,
    block_email=True,
    block_urls=True,
    block_ip=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

##### delete_posts: `bool`<a id="delete_posts-bool"></a>

##### block_email: `bool`<a id="block_email-bool"></a>

##### block_urls: `bool`<a id="block_urls-bool"></a>

##### block_ip: `bool`<a id="block_ip-bool"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersDeleteUserByIdJsonRequest`](./discourse_python_sdk/type/users_delete_user_by_id_json_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`UsersDeleteUserByIdJsonResponse`](./discourse_python_sdk/pydantic/users_delete_user_by_id_json_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/admin/users/{id}.json` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.admin.get_list_of_users`<a id="discourseadminget_list_of_users"></a>

Get a list of users

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_list_of_users_response = discourse.admin.get_list_of_users(
    flag="active",
    order="created",
    asc="true",
    page=1,
    show_emails=True,
    stats=True,
    email="string_example",
    ip="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### flag: `str`<a id="flag-str"></a>

##### order: `str`<a id="order-str"></a>

##### asc: `str`<a id="asc-str"></a>

##### page: `int`<a id="page-int"></a>

##### show_emails: `bool`<a id="show_emails-bool"></a>

Include user email addresses in response. These requests will be logged in the staff action logs.

##### stats: `bool`<a id="stats-bool"></a>

Include user stats information

##### email: `str`<a id="email-str"></a>

Filter to the user with this email address

##### ip: `str`<a id="ip-str"></a>

Filter to users with this IP address

#### 🔄 Return<a id="🔄-return"></a>

[`UsersGetListOfUsersResponse`](./discourse_python_sdk/pydantic/users_get_list_of_users_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/admin/users/list/{flag}.json` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.admin.get_user_by_id_json`<a id="discourseadminget_user_by_id_json"></a>

Get a user by id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_by_id_json_response = discourse.admin.get_user_by_id_json(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UsersGetUserByIdJsonResponse`](./discourse_python_sdk/pydantic/users_get_user_by_id_json_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/admin/users/{id}.json` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.admin.log_out_user_action`<a id="discourseadminlog_out_user_action"></a>

Log a user out

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
log_out_user_action_response = discourse.admin.log_out_user_action(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UsersLogOutUserActionResponse`](./discourse_python_sdk/pydantic/users_log_out_user_action_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/admin/users/{id}/log_out.json` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.admin.refresh_gravatar_post`<a id="discourseadminrefresh_gravatar_post"></a>

Refresh gravatar

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
refresh_gravatar_post_response = discourse.admin.refresh_gravatar_post(
    username="username_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### username: `str`<a id="username-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UsersRefreshGravatarPostResponse`](./discourse_python_sdk/pydantic/users_refresh_gravatar_post_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/user_avatar/{username}/refresh_gravatar.json` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.admin.silence_by_id`<a id="discourseadminsilence_by_id"></a>

Silence a user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
silence_by_id_response = discourse.admin.silence_by_id(
    id=1,
    silenced_till="2022-06-01T08:00:00.000Z",
    reason="string_example",
    message="string_example",
    post_action="delete",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

##### silenced_till: `str`<a id="silenced_till-str"></a>

##### reason: `str`<a id="reason-str"></a>

##### message: `str`<a id="message-str"></a>

Will send an email with this message when present

##### post_action: `str`<a id="post_action-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersSilenceByIdRequest`](./discourse_python_sdk/type/users_silence_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`UsersSilenceByIdResponse`](./discourse_python_sdk/pydantic/users_silence_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/admin/users/{id}/silence.json` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.admin.suspend_by_id_json`<a id="discourseadminsuspend_by_id_json"></a>

Suspend a user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
suspend_by_id_json_response = discourse.admin.suspend_by_id_json(
    suspend_until="2121-02-22",
    reason="string_example",
    id=1,
    message="string_example",
    post_action="delete",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### suspend_until: `str`<a id="suspend_until-str"></a>

##### reason: `str`<a id="reason-str"></a>

##### id: `int`<a id="id-int"></a>

##### message: `str`<a id="message-str"></a>

Will send an email with this message when present

##### post_action: `str`<a id="post_action-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersSuspendByIdJsonRequest`](./discourse_python_sdk/type/users_suspend_by_id_json_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`UsersSuspendByIdJsonResponse`](./discourse_python_sdk/pydantic/users_suspend_by_id_json_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/admin/users/{id}/suspend.json` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.backups.create_backup_request`<a id="discoursebackupscreate_backup_request"></a>

Create backup

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_backup_request_response = discourse.backups.create_backup_request(
    with_uploads=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### with_uploads: `bool`<a id="with_uploads-bool"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BackupsCreateBackupRequestRequest`](./discourse_python_sdk/type/backups_create_backup_request_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`BackupsCreateBackupRequestResponse`](./discourse_python_sdk/pydantic/backups_create_backup_request_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/admin/backups.json` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.backups.download_backup`<a id="discoursebackupsdownload_backup"></a>

Download backup

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
discourse.backups.download_backup(
    filename="filename_example",
    token="token_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### filename: `str`<a id="filename-str"></a>

##### token: `str`<a id="token-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/admin/backups/{filename}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.backups.list`<a id="discoursebackupslist"></a>

List backups

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = discourse.backups.list()
```

#### 🔄 Return<a id="🔄-return"></a>

[`BackupsListResponse`](./discourse_python_sdk/pydantic/backups_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/admin/backups.json` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.backups.send_download_backup_email`<a id="discoursebackupssend_download_backup_email"></a>

Send download backup email

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
discourse.backups.send_download_backup_email(
    filename="filename_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### filename: `str`<a id="filename-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/admin/backups/{filename}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.badges.create_badge`<a id="discoursebadgescreate_badge"></a>

Create badge

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_badge_response = discourse.badges.create_badge(
    name="string_example",
    badge_type_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

The name for the new badge.

##### badge_type_id: `int`<a id="badge_type_id-int"></a>

The ID for the badge type. 1 for Gold, 2 for Silver, 3 for Bronze.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BadgesCreateBadgeRequest`](./discourse_python_sdk/type/badges_create_badge_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`BadgesCreateBadgeResponse`](./discourse_python_sdk/pydantic/badges_create_badge_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/admin/badges.json` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.badges.delete_by_id_json`<a id="discoursebadgesdelete_by_id_json"></a>

Delete badge

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
discourse.badges.delete_by_id_json(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/admin/badges/{id}.json` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.badges.list`<a id="discoursebadgeslist"></a>

List badges

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = discourse.badges.list()
```

#### 🔄 Return<a id="🔄-return"></a>

[`BadgesListResponse`](./discourse_python_sdk/pydantic/badges_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/admin/badges.json` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.badges.list_user_badges`<a id="discoursebadgeslist_user_badges"></a>

List badges for a user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_user_badges_response = discourse.badges.list_user_badges(
    username="username_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### username: `str`<a id="username-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`BadgesListUserBadgesResponse`](./discourse_python_sdk/pydantic/badges_list_user_badges_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/user-badges/{username}.json` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.badges.update_badge_by_id_json`<a id="discoursebadgesupdate_badge_by_id_json"></a>

Update badge

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_badge_by_id_json_response = discourse.badges.update_badge_by_id_json(
    name="string_example",
    badge_type_id=1,
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

The name for the new badge.

##### badge_type_id: `int`<a id="badge_type_id-int"></a>

The ID for the badge type. 1 for Gold, 2 for Silver, 3 for Bronze.

##### id: `int`<a id="id-int"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BadgesUpdateBadgeByIdJsonRequest`](./discourse_python_sdk/type/badges_update_badge_by_id_json_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`BadgesUpdateBadgeByIdJsonResponse`](./discourse_python_sdk/pydantic/badges_update_badge_by_id_json_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/admin/badges/{id}.json` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.categories.create_category_request`<a id="discoursecategoriescreate_category_request"></a>

Creates a category

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_category_request_response = discourse.categories.create_category_request(
    name="string_example",
    color="49d9e9",
    text_color="f0fcfd",
    parent_category_id=1,
    allow_badges=True,
    slug="string_example",
    topic_featured_links_allowed=True,
    permissions={
        "everyone": 1,
    },
    search_priority=1,
    form_template_ids=[None],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

##### color: `str`<a id="color-str"></a>

##### text_color: `str`<a id="text_color-str"></a>

##### parent_category_id: `int`<a id="parent_category_id-int"></a>

##### allow_badges: `bool`<a id="allow_badges-bool"></a>

##### slug: `str`<a id="slug-str"></a>

##### topic_featured_links_allowed: `bool`<a id="topic_featured_links_allowed-bool"></a>

##### permissions: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./discourse_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="permissions-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonediscourse_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

##### search_priority: `int`<a id="search_priority-int"></a>

##### form_template_ids: List[[`Union[bool, date, datetime, dict, float, int, list, str, None]`](./discourse_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)]<a id="form_template_ids-listunionbool-date-datetime-dict-float-int-list-str-nonediscourse_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CategoriesCreateCategoryRequestRequest`](./discourse_python_sdk/type/categories_create_category_request_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CategoriesCreateCategoryRequestResponse`](./discourse_python_sdk/pydantic/categories_create_category_request_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/categories.json` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.categories.get_categories_and_subcategories`<a id="discoursecategoriesget_categories_and_subcategories"></a>

Can be used to fetch all categories and subcategories

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_categories_and_subcategories_response = (
    discourse.categories.get_categories_and_subcategories()
)
```

#### 🔄 Return<a id="🔄-return"></a>

[`SiteGetCategoriesAndSubcategoriesResponse`](./discourse_python_sdk/pydantic/site_get_categories_and_subcategories_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/site.json` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.categories.get_category_by_id_json`<a id="discoursecategoriesget_category_by_id_json"></a>

Show category

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_category_by_id_json_response = discourse.categories.get_category_by_id_json(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`CategoriesGetCategoryByIdJsonResponse`](./discourse_python_sdk/pydantic/categories_get_category_by_id_json_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/c/{id}/show.json` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.categories.list`<a id="discoursecategorieslist"></a>

Retrieves a list of categories

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = discourse.categories.list(
    include_subcategories=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### include_subcategories: `bool`<a id="include_subcategories-bool"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`CategoriesListResponse`](./discourse_python_sdk/pydantic/categories_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/categories.json` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.categories.list_topics`<a id="discoursecategorieslist_topics"></a>

List topics

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_topics_response = discourse.categories.list_topics(
    slug="slug_example",
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### slug: `str`<a id="slug-str"></a>

##### id: `int`<a id="id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`CategoriesListTopicsResponse`](./discourse_python_sdk/pydantic/categories_list_topics_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/c/{slug}/{id}.json` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.categories.update_category_by_id_json`<a id="discoursecategoriesupdate_category_by_id_json"></a>

Updates a category

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_category_by_id_json_response = discourse.categories.update_category_by_id_json(
    name="string_example",
    id=1,
    color="49d9e9",
    text_color="f0fcfd",
    parent_category_id=1,
    allow_badges=True,
    slug="string_example",
    topic_featured_links_allowed=True,
    permissions={
        "everyone": 1,
    },
    search_priority=1,
    form_template_ids=[None],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

##### id: `int`<a id="id-int"></a>

##### color: `str`<a id="color-str"></a>

##### text_color: `str`<a id="text_color-str"></a>

##### parent_category_id: `int`<a id="parent_category_id-int"></a>

##### allow_badges: `bool`<a id="allow_badges-bool"></a>

##### slug: `str`<a id="slug-str"></a>

##### topic_featured_links_allowed: `bool`<a id="topic_featured_links_allowed-bool"></a>

##### permissions: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./discourse_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="permissions-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonediscourse_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

##### search_priority: `int`<a id="search_priority-int"></a>

##### form_template_ids: List[[`Union[bool, date, datetime, dict, float, int, list, str, None]`](./discourse_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)]<a id="form_template_ids-listunionbool-date-datetime-dict-float-int-list-str-nonediscourse_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CategoriesUpdateCategoryByIdJsonRequest`](./discourse_python_sdk/type/categories_update_category_by_id_json_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CategoriesUpdateCategoryByIdJsonResponse`](./discourse_python_sdk/pydantic/categories_update_category_by_id_json_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/categories/{id}.json` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.groups.add_members_to_group`<a id="discoursegroupsadd_members_to_group"></a>

Add group members

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_members_to_group_response = discourse.groups.add_members_to_group(
    id=1,
    usernames="username1,username2",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

##### usernames: `str`<a id="usernames-str"></a>

comma separated list

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GroupsAddMembersToGroupRequest`](./discourse_python_sdk/type/groups_add_members_to_group_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`GroupsAddMembersToGroupResponse`](./discourse_python_sdk/pydantic/groups_add_members_to_group_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/groups/{id}/members.json` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.groups.create_new_group`<a id="discoursegroupscreate_new_group"></a>

Create a group

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_group_response = discourse.groups.create_new_group(
    group={
        "name": "name_example",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### group: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./discourse_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="group-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonediscourse_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GroupsCreateNewGroupRequest`](./discourse_python_sdk/type/groups_create_new_group_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`GroupsCreateNewGroupResponse`](./discourse_python_sdk/pydantic/groups_create_new_group_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/admin/groups.json` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.groups.delete_group_by_id_json`<a id="discoursegroupsdelete_group_by_id_json"></a>

Delete a group

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_group_by_id_json_response = discourse.groups.delete_group_by_id_json(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`GroupsDeleteGroupByIdJsonResponse`](./discourse_python_sdk/pydantic/groups_delete_group_by_id_json_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/admin/groups/{id}.json` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.groups.get_group_by_id`<a id="discoursegroupsget_group_by_id"></a>

Get a group

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_group_by_id_response = discourse.groups.get_group_by_id(
    id="name",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Use group name instead of id

#### 🔄 Return<a id="🔄-return"></a>

[`GroupsGetGroupByIdResponse`](./discourse_python_sdk/pydantic/groups_get_group_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/groups/{id}.json` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.groups.list`<a id="discoursegroupslist"></a>

List groups

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = discourse.groups.list()
```

#### 🔄 Return<a id="🔄-return"></a>

[`GroupsListResponse`](./discourse_python_sdk/pydantic/groups_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/groups.json` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.groups.list_members_json`<a id="discoursegroupslist_members_json"></a>

List group members

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_members_json_response = discourse.groups.list_members_json(
    id="name",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Use group name instead of id

#### 🔄 Return<a id="🔄-return"></a>

[`GroupsListMembersJsonResponse`](./discourse_python_sdk/pydantic/groups_list_members_json_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/groups/{id}/members.json` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.groups.remove_members`<a id="discoursegroupsremove_members"></a>

Remove group members

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_members_response = discourse.groups.remove_members(
    id=1,
    usernames="username1,username2",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

##### usernames: `str`<a id="usernames-str"></a>

comma separated list

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GroupsRemoveMembersRequest`](./discourse_python_sdk/type/groups_remove_members_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`GroupsRemoveMembersResponse`](./discourse_python_sdk/pydantic/groups_remove_members_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/groups/{id}/members.json` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.groups.update_group_by_id_json`<a id="discoursegroupsupdate_group_by_id_json"></a>

Update a group

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_group_by_id_json_response = discourse.groups.update_group_by_id_json(
    group={
        "name": "name_example",
    },
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### group: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./discourse_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="group-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonediscourse_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>


##### id: `int`<a id="id-int"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GroupsUpdateGroupByIdJsonRequest`](./discourse_python_sdk/type/groups_update_group_by_id_json_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`GroupsUpdateGroupByIdJsonResponse`](./discourse_python_sdk/pydantic/groups_update_group_by_id_json_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/groups/{id}.json` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.invites.create_invite`<a id="discourseinvitescreate_invite"></a>

Create an invite

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_invite_response = discourse.invites.create_invite(
    api_key="Api-Key_example",
    api_username="Api-Username_example",
    email="not-a-user-yet@example.com",
    skip_email=False,
    custom_message="string_example",
    max_redemptions_allowed=5,
    topic_id=1,
    group_ids="42,43",
    group_names="foo,bar",
    expires_at="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: `str`<a id="api_key-str"></a>

##### api_username: `str`<a id="api_username-str"></a>

##### email: `str`<a id="email-str"></a>

required for email invites only

##### skip_email: `bool`<a id="skip_email-bool"></a>

##### custom_message: `str`<a id="custom_message-str"></a>

optional, for email invites

##### max_redemptions_allowed: `int`<a id="max_redemptions_allowed-int"></a>

optional, for link invites

##### topic_id: `int`<a id="topic_id-int"></a>

##### group_ids: `str`<a id="group_ids-str"></a>

Optional, either this or `group_names`. Comma separated list for multiple ids.

##### group_names: `str`<a id="group_names-str"></a>

Optional, either this or `group_ids`. Comma separated list for multiple names.

##### expires_at: `str`<a id="expires_at-str"></a>

optional, if not supplied, the invite_expiry_days site setting is used

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`InvitesCreateInviteRequest`](./discourse_python_sdk/type/invites_create_invite_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`InvitesCreateInviteResponse`](./discourse_python_sdk/pydantic/invites_create_invite_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/invites.json` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.invites.create_multiple_invites`<a id="discourseinvitescreate_multiple_invites"></a>

Create multiple invites

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_multiple_invites_response = discourse.invites.create_multiple_invites(
    api_key="Api-Key_example",
    api_username="Api-Username_example",
    email="[not-a-user-yet-1@example.com, not-a-user-yet-2@example.com]",
    skip_email=False,
    custom_message="string_example",
    max_redemptions_allowed=5,
    topic_id=1,
    group_ids="42,43",
    group_names="foo,bar",
    expires_at="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: `str`<a id="api_key-str"></a>

##### api_username: `str`<a id="api_username-str"></a>

##### email: `str`<a id="email-str"></a>

pass 1 email per invite to be generated. other properties will be shared by each invite.

##### skip_email: `bool`<a id="skip_email-bool"></a>

##### custom_message: `str`<a id="custom_message-str"></a>

optional, for email invites

##### max_redemptions_allowed: `int`<a id="max_redemptions_allowed-int"></a>

optional, for link invites

##### topic_id: `int`<a id="topic_id-int"></a>

##### group_ids: `str`<a id="group_ids-str"></a>

Optional, either this or `group_names`. Comma separated list for multiple ids.

##### group_names: `str`<a id="group_names-str"></a>

Optional, either this or `group_ids`. Comma separated list for multiple names.

##### expires_at: `str`<a id="expires_at-str"></a>

optional, if not supplied, the invite_expiry_days site setting is used

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`InvitesCreateMultipleInvitesRequest`](./discourse_python_sdk/type/invites_create_multiple_invites_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`InvitesCreateMultipleInvitesResponse`](./discourse_python_sdk/pydantic/invites_create_multiple_invites_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/invites/create-multiple.json` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.invites.send_invite_to_topic`<a id="discourseinvitessend_invite_to_topic"></a>

Invite to topic

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
send_invite_to_topic_response = discourse.invites.send_invite_to_topic(
    api_key="Api-Key_example",
    api_username="Api-Username_example",
    id="id_example",
    user="string_example",
    email="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: `str`<a id="api_key-str"></a>

##### api_username: `str`<a id="api_username-str"></a>

##### id: `str`<a id="id-str"></a>

##### user: `str`<a id="user-str"></a>

##### email: `str`<a id="email-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TopicsSendInviteToTopicRequest`](./discourse_python_sdk/type/topics_send_invite_to_topic_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TopicsSendInviteToTopicResponse`](./discourse_python_sdk/pydantic/topics_send_invite_to_topic_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/t/{id}/invite.json` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.notifications.get_user_notifications`<a id="discoursenotificationsget_user_notifications"></a>

Get the notifications that belong to the current user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_notifications_response = discourse.notifications.get_user_notifications()
```

#### 🔄 Return<a id="🔄-return"></a>

[`NotificationsGetUserNotificationsResponse`](./discourse_python_sdk/pydantic/notifications_get_user_notifications_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/notifications.json` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.notifications.mark_as_read`<a id="discoursenotificationsmark_as_read"></a>

Mark notifications as read

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
mark_as_read_response = discourse.notifications.mark_as_read(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

(optional) Leave off to mark all notifications as read

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`NotificationsMarkAsReadRequest`](./discourse_python_sdk/type/notifications_mark_as_read_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`NotificationsMarkAsReadResponse`](./discourse_python_sdk/pydantic/notifications_mark_as_read_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/notifications/mark-read.json` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.posts.create_topic_post_message`<a id="discoursepostscreate_topic_post_message"></a>

Creates a new topic, a new post, or a private message

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_topic_post_message_response = discourse.posts.create_topic_post_message(
    raw="string_example",
    title="string_example",
    topic_id=1,
    category=1,
    target_recipients="blake,sam",
    target_usernames="string_example",
    archetype="private_message",
    created_at="string_example",
    reply_to_post_number=1,
    embed_url="string_example",
    external_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### raw: `str`<a id="raw-str"></a>

##### title: `str`<a id="title-str"></a>

Required if creating a new topic or new private message.

##### topic_id: `int`<a id="topic_id-int"></a>

Required if creating a new post.

##### category: `int`<a id="category-int"></a>

Optional if creating a new topic, and ignored if creating a new post.

##### target_recipients: `str`<a id="target_recipients-str"></a>

Required for private message, comma separated.

##### target_usernames: `str`<a id="target_usernames-str"></a>

Deprecated. Use target_recipients instead.

##### archetype: `str`<a id="archetype-str"></a>

Required for new private message.

##### created_at: `str`<a id="created_at-str"></a>

##### reply_to_post_number: `int`<a id="reply_to_post_number-int"></a>

Optional, the post number to reply to inside a topic.

##### embed_url: `str`<a id="embed_url-str"></a>

Provide a URL from a remote system to associate a forum topic with that URL, typically for using Discourse as a comments system for an external blog.

##### external_id: `str`<a id="external_id-str"></a>

Provide an external_id from a remote system to associate a forum topic with that id.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PostsCreateTopicPostMessageRequest`](./discourse_python_sdk/type/posts_create_topic_post_message_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PostsCreateTopicPostMessageResponse`](./discourse_python_sdk/pydantic/posts_create_topic_post_message_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/posts.json` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.posts.delete_single_post`<a id="discoursepostsdelete_single_post"></a>

delete a single post

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
discourse.posts.delete_single_post(
    id=1,
    force_destroy=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

##### force_destroy: `bool`<a id="force_destroy-bool"></a>

The `SiteSetting.can_permanently_delete` needs to be enabled first before this param can be used. Also this endpoint needs to be called first without `force_destroy` and then followed up with a second call 5 minutes later with `force_destroy` to permanently delete.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PostsDeleteSinglePostRequest`](./discourse_python_sdk/type/posts_delete_single_post_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/posts/{id}.json` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.posts.get_single_post_likes`<a id="discoursepostsget_single_post_likes"></a>

This endpoint can be used to get the number of likes on a post using the
`actions_summary` property in the response. `actions_summary` responses
with the id of `2` signify a `like`. If there are no `actions_summary`
items with the id of `2`, that means there are 0 likes. Other ids likely
refer to various different flag types.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_single_post_likes_response = discourse.posts.get_single_post_likes(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PostsGetSinglePostLikesResponse`](./discourse_python_sdk/pydantic/posts_get_single_post_likes_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/posts/{id}.json` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.posts.like_post_action`<a id="discoursepostslike_post_action"></a>

Like a post and other actions

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
like_post_action_response = discourse.posts.like_post_action(
    id=1,
    post_action_type_id=1,
    api_key="Api-Key_example",
    api_username="Api-Username_example",
    flag_topic=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

##### post_action_type_id: `int`<a id="post_action_type_id-int"></a>

##### api_key: `str`<a id="api_key-str"></a>

##### api_username: `str`<a id="api_username-str"></a>

##### flag_topic: `bool`<a id="flag_topic-bool"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PostsLikePostActionRequest`](./discourse_python_sdk/type/posts_like_post_action_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PostsLikePostActionResponse`](./discourse_python_sdk/pydantic/posts_like_post_action_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/post_actions.json` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.posts.list_latest_posts_across_topics`<a id="discoursepostslist_latest_posts_across_topics"></a>

List latest posts across topics

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_latest_posts_across_topics_response = (
    discourse.posts.list_latest_posts_across_topics(
        api_key="Api-Key_example",
        api_username="Api-Username_example",
        before="string_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: `str`<a id="api_key-str"></a>

##### api_username: `str`<a id="api_username-str"></a>

##### before: `str`<a id="before-str"></a>

Load posts with an id lower than this value. Useful for pagination.

#### 🔄 Return<a id="🔄-return"></a>

[`PostsListLatestPostsAcrossTopicsResponse`](./discourse_python_sdk/pydantic/posts_list_latest_posts_across_topics_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/posts.json` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.posts.list_replies_to_post`<a id="discoursepostslist_replies_to_post"></a>

List replies to a post

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_replies_to_post_response = discourse.posts.list_replies_to_post(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PostsListRepliesToPostResponse`](./discourse_python_sdk/pydantic/posts_list_replies_to_post_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/posts/{id}/replies.json` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.posts.lock_post_action`<a id="discoursepostslock_post_action"></a>

Lock a post from being edited

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
lock_post_action_response = discourse.posts.lock_post_action(
    locked="string_example",
    api_key="Api-Key_example",
    api_username="Api-Username_example",
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### locked: `str`<a id="locked-str"></a>

##### api_key: `str`<a id="api_key-str"></a>

##### api_username: `str`<a id="api_username-str"></a>

##### id: `str`<a id="id-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PostsLockPostActionRequest`](./discourse_python_sdk/type/posts_lock_post_action_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PostsLockPostActionResponse`](./discourse_python_sdk/pydantic/posts_lock_post_action_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/posts/{id}/locked.json` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.posts.update_single_post_json`<a id="discoursepostsupdate_single_post_json"></a>

Update a single post

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_single_post_json_response = discourse.posts.update_single_post_json(
    id="id_example",
    post={
        "raw": "raw_example",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

##### post: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./discourse_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="post-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonediscourse_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PostsUpdateSinglePostJsonRequest`](./discourse_python_sdk/type/posts_update_single_post_json_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PostsUpdateSinglePostJsonResponse`](./discourse_python_sdk/pydantic/posts_update_single_post_json_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/posts/{id}.json` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.private_messages.create_topic_post_message`<a id="discourseprivate_messagescreate_topic_post_message"></a>

Creates a new topic, a new post, or a private message

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_topic_post_message_response = (
    discourse.private_messages.create_topic_post_message(
        raw="string_example",
        title="string_example",
        topic_id=1,
        category=1,
        target_recipients="blake,sam",
        target_usernames="string_example",
        archetype="private_message",
        created_at="string_example",
        reply_to_post_number=1,
        embed_url="string_example",
        external_id="string_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### raw: `str`<a id="raw-str"></a>

##### title: `str`<a id="title-str"></a>

Required if creating a new topic or new private message.

##### topic_id: `int`<a id="topic_id-int"></a>

Required if creating a new post.

##### category: `int`<a id="category-int"></a>

Optional if creating a new topic, and ignored if creating a new post.

##### target_recipients: `str`<a id="target_recipients-str"></a>

Required for private message, comma separated.

##### target_usernames: `str`<a id="target_usernames-str"></a>

Deprecated. Use target_recipients instead.

##### archetype: `str`<a id="archetype-str"></a>

Required for new private message.

##### created_at: `str`<a id="created_at-str"></a>

##### reply_to_post_number: `int`<a id="reply_to_post_number-int"></a>

Optional, the post number to reply to inside a topic.

##### embed_url: `str`<a id="embed_url-str"></a>

Provide a URL from a remote system to associate a forum topic with that URL, typically for using Discourse as a comments system for an external blog.

##### external_id: `str`<a id="external_id-str"></a>

Provide an external_id from a remote system to associate a forum topic with that id.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PostsCreateTopicPostMessageRequest`](./discourse_python_sdk/type/posts_create_topic_post_message_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PostsCreateTopicPostMessageResponse`](./discourse_python_sdk/pydantic/posts_create_topic_post_message_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/posts.json` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.private_messages.list_for_user`<a id="discourseprivate_messageslist_for_user"></a>

Get a list of private messages for a user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_for_user_response = discourse.private_messages.list_for_user(
    username="username_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### username: `str`<a id="username-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PrivateMessagesListForUserResponse`](./discourse_python_sdk/pydantic/private_messages_list_for_user_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/topics/private-messages/{username}.json` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.private_messages.list_sent_for_user`<a id="discourseprivate_messageslist_sent_for_user"></a>

Get a list of private messages sent for a user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_sent_for_user_response = discourse.private_messages.list_sent_for_user(
    username="username_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### username: `str`<a id="username-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PrivateMessagesListSentForUserResponse`](./discourse_python_sdk/pydantic/private_messages_list_sent_for_user_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/topics/private-messages-sent/{username}.json` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.search.term_results`<a id="discoursesearchterm_results"></a>

Search for a term

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
term_results_response = discourse.search.term_results(
    q="api @blake #support tags:api after:2021-06-04 in:unseen in:open\norder:latest_topic",
    page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### q: `str`<a id="q-str"></a>

The query string needs to be url encoded and is made up of the following options: - Search term. This is just a string. Usually it would be the first item in the query. - `@<username>`: Use the `@` followed by the username to specify posts by this user. - `#<category>`: Use the `#` followed by the category slug to search within this category. - `tags:`: `api,solved` or for posts that have all the specified tags `api+solved`. - `before:`: `yyyy-mm-dd` - `after:`: `yyyy-mm-dd` - `order:`: `latest`, `likes`, `views`, `latest_topic` - `assigned:`: username (without `@`) - `in:`: `title`, `likes`, `personal`, `messages`, `seen`, `unseen`, `posted`, `created`, `watching`, `tracking`, `bookmarks`, `assigned`, `unassigned`, `first`, `pinned`, `wiki` - `with:`: `images` - `status:`: `open`, `closed`, `public`, `archived`, `noreplies`, `single_user`, `solved`, `unsolved` - `group:`: group_name or group_id - `group_messages:`: group_name or group_id - `min_posts:`: 1 - `max_posts:`: 10 - `min_views:`: 1 - `max_views:`: 10  If you are using cURL you can use the `-G` and the `--data-urlencode` flags to encode the query:  ``` curl -i -sS -X GET -G \"http://localhost:4200/search.json\" \\ --data-urlencode 'q=wordpress @scossar #fun after:2020-01-01' ``` 

##### page: `int`<a id="page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`SearchTermResultsResponse`](./discourse_python_sdk/pydantic/search_term_results_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/search.json` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.site.get_categories_and_subcategories`<a id="discoursesiteget_categories_and_subcategories"></a>

Can be used to fetch all categories and subcategories

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_categories_and_subcategories_response = (
    discourse.site.get_categories_and_subcategories()
)
```

#### 🔄 Return<a id="🔄-return"></a>

[`SiteGetCategoriesAndSubcategoriesResponse`](./discourse_python_sdk/pydantic/site_get_categories_and_subcategories_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/site.json` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.tags.create_tag_group`<a id="discoursetagscreate_tag_group"></a>

Creates a tag group

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_tag_group_response = discourse.tags.create_tag_group(
    name="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TagsCreateTagGroupRequest`](./discourse_python_sdk/type/tags_create_tag_group_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TagsCreateTagGroupResponse`](./discourse_python_sdk/pydantic/tags_create_tag_group_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tag_groups.json` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.tags.get_single_tag_group`<a id="discoursetagsget_single_tag_group"></a>

Get a single tag group

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_single_tag_group_response = discourse.tags.get_single_tag_group(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`TagsGetSingleTagGroupResponse`](./discourse_python_sdk/pydantic/tags_get_single_tag_group_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tag_groups/{id}.json` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.tags.get_specific_tag`<a id="discoursetagsget_specific_tag"></a>

Get a specific tag

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_specific_tag_response = discourse.tags.get_specific_tag(
    name="name_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`TagsGetSpecificTagResponse`](./discourse_python_sdk/pydantic/tags_get_specific_tag_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tag/{name}.json` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.tags.get_tag_groups`<a id="discoursetagsget_tag_groups"></a>

Get a list of tag groups

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_tag_groups_response = discourse.tags.get_tag_groups()
```

#### 🔄 Return<a id="🔄-return"></a>

[`TagsGetTagGroupsResponse`](./discourse_python_sdk/pydantic/tags_get_tag_groups_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tag_groups.json` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.tags.list`<a id="discoursetagslist"></a>

Get a list of tags

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = discourse.tags.list()
```

#### 🔄 Return<a id="🔄-return"></a>

[`TagsListResponse`](./discourse_python_sdk/pydantic/tags_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tags.json` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.tags.update_tag_group`<a id="discoursetagsupdate_tag_group"></a>

Update tag group

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_tag_group_response = discourse.tags.update_tag_group(
    id="id_example",
    name="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

##### name: `str`<a id="name-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TagsUpdateTagGroupRequest`](./discourse_python_sdk/type/tags_update_tag_group_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TagsUpdateTagGroupResponse`](./discourse_python_sdk/pydantic/tags_update_tag_group_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tag_groups/{id}.json` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.topics.create_topic_post_message`<a id="discoursetopicscreate_topic_post_message"></a>

Creates a new topic, a new post, or a private message

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_topic_post_message_response = discourse.topics.create_topic_post_message(
    raw="string_example",
    title="string_example",
    topic_id=1,
    category=1,
    target_recipients="blake,sam",
    target_usernames="string_example",
    archetype="private_message",
    created_at="string_example",
    reply_to_post_number=1,
    embed_url="string_example",
    external_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### raw: `str`<a id="raw-str"></a>

##### title: `str`<a id="title-str"></a>

Required if creating a new topic or new private message.

##### topic_id: `int`<a id="topic_id-int"></a>

Required if creating a new post.

##### category: `int`<a id="category-int"></a>

Optional if creating a new topic, and ignored if creating a new post.

##### target_recipients: `str`<a id="target_recipients-str"></a>

Required for private message, comma separated.

##### target_usernames: `str`<a id="target_usernames-str"></a>

Deprecated. Use target_recipients instead.

##### archetype: `str`<a id="archetype-str"></a>

Required for new private message.

##### created_at: `str`<a id="created_at-str"></a>

##### reply_to_post_number: `int`<a id="reply_to_post_number-int"></a>

Optional, the post number to reply to inside a topic.

##### embed_url: `str`<a id="embed_url-str"></a>

Provide a URL from a remote system to associate a forum topic with that URL, typically for using Discourse as a comments system for an external blog.

##### external_id: `str`<a id="external_id-str"></a>

Provide an external_id from a remote system to associate a forum topic with that id.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PostsCreateTopicPostMessageRequest`](./discourse_python_sdk/type/posts_create_topic_post_message_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PostsCreateTopicPostMessageResponse`](./discourse_python_sdk/pydantic/posts_create_topic_post_message_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/posts.json` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.topics.create_topic_timer`<a id="discoursetopicscreate_topic_timer"></a>

Create topic timer

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_topic_timer_response = discourse.topics.create_topic_timer(
    api_key="Api-Key_example",
    api_username="Api-Username_example",
    id="id_example",
    time="",
    status_type="string_example",
    based_on_last_post=True,
    category_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: `str`<a id="api_key-str"></a>

##### api_username: `str`<a id="api_username-str"></a>

##### id: `str`<a id="id-str"></a>

##### time: `str`<a id="time-str"></a>

##### status_type: `str`<a id="status_type-str"></a>

##### based_on_last_post: `bool`<a id="based_on_last_post-bool"></a>

##### category_id: `int`<a id="category_id-int"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TopicsCreateTopicTimerRequest`](./discourse_python_sdk/type/topics_create_topic_timer_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TopicsCreateTopicTimerResponse`](./discourse_python_sdk/pydantic/topics_create_topic_timer_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/t/{id}/timer.json` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.topics.get_by_external_id`<a id="discoursetopicsget_by_external_id"></a>

Get topic by external_id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
discourse.topics.get_by_external_id(
    external_id="external_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### external_id: `str`<a id="external_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/t/external_id/{external_id}.json` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.topics.get_latest_topics`<a id="discoursetopicsget_latest_topics"></a>

Get the latest topics

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_latest_topics_response = discourse.topics.get_latest_topics(
    api_key="Api-Key_example",
    api_username="Api-Username_example",
    order="string_example",
    ascending="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: `str`<a id="api_key-str"></a>

##### api_username: `str`<a id="api_username-str"></a>

##### order: `str`<a id="order-str"></a>

Enum: `default`, `created`, `activity`, `views`, `posts`, `category`, `likes`, `op_likes`, `posters`

##### ascending: `str`<a id="ascending-str"></a>

Defaults to `desc`, add `ascending=true` to sort asc

#### 🔄 Return<a id="🔄-return"></a>

[`TopicsGetLatestTopicsResponse`](./discourse_python_sdk/pydantic/topics_get_latest_topics_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/latest.json` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.topics.get_single_topic`<a id="discoursetopicsget_single_topic"></a>

Get a single topic

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_single_topic_response = discourse.topics.get_single_topic(
    api_key="Api-Key_example",
    api_username="Api-Username_example",
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: `str`<a id="api_key-str"></a>

##### api_username: `str`<a id="api_username-str"></a>

##### id: `str`<a id="id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`TopicsGetSingleTopicResponse`](./discourse_python_sdk/pydantic/topics_get_single_topic_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/t/{id}.json` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.topics.get_specific_posts`<a id="discoursetopicsget_specific_posts"></a>

Get specific posts from a topic

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_specific_posts_response = discourse.topics.get_specific_posts(
    post_ids_=1,
    api_key="Api-Key_example",
    api_username="Api-Username_example",
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### post_ids_: `int`<a id="post_ids_-int"></a>

##### api_key: `str`<a id="api_key-str"></a>

##### api_username: `str`<a id="api_username-str"></a>

##### id: `str`<a id="id-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TopicsGetSpecificPostsRequest`](./discourse_python_sdk/type/topics_get_specific_posts_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TopicsGetSpecificPostsResponse`](./discourse_python_sdk/pydantic/topics_get_specific_posts_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/t/{id}/posts.json` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.topics.get_top_topics_by_period`<a id="discoursetopicsget_top_topics_by_period"></a>

Get the top topics filtered by period

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_top_topics_by_period_response = discourse.topics.get_top_topics_by_period(
    api_key="Api-Key_example",
    api_username="Api-Username_example",
    period="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: `str`<a id="api_key-str"></a>

##### api_username: `str`<a id="api_username-str"></a>

##### period: `str`<a id="period-str"></a>

Enum: `all`, `yearly`, `quarterly`, `monthly`, `weekly`, `daily`

#### 🔄 Return<a id="🔄-return"></a>

[`TopicsGetTopTopicsByPeriodResponse`](./discourse_python_sdk/pydantic/topics_get_top_topics_by_period_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/top.json` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.topics.remove_topic_by_id`<a id="discoursetopicsremove_topic_by_id"></a>

Remove a topic

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
discourse.topics.remove_topic_by_id(
    api_key="Api-Key_example",
    api_username="Api-Username_example",
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: `str`<a id="api_key-str"></a>

##### api_username: `str`<a id="api_username-str"></a>

##### id: `str`<a id="id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/t/{id}.json` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.topics.send_invite_to_topic`<a id="discoursetopicssend_invite_to_topic"></a>

Invite to topic

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
send_invite_to_topic_response = discourse.topics.send_invite_to_topic(
    api_key="Api-Key_example",
    api_username="Api-Username_example",
    id="id_example",
    user="string_example",
    email="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: `str`<a id="api_key-str"></a>

##### api_username: `str`<a id="api_username-str"></a>

##### id: `str`<a id="id-str"></a>

##### user: `str`<a id="user-str"></a>

##### email: `str`<a id="email-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TopicsSendInviteToTopicRequest`](./discourse_python_sdk/type/topics_send_invite_to_topic_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TopicsSendInviteToTopicResponse`](./discourse_python_sdk/pydantic/topics_send_invite_to_topic_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/t/{id}/invite.json` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.topics.set_notification_level`<a id="discoursetopicsset_notification_level"></a>

Set notification level

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
set_notification_level_response = discourse.topics.set_notification_level(
    notification_level="0",
    api_key="Api-Key_example",
    api_username="Api-Username_example",
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### notification_level: `str`<a id="notification_level-str"></a>

##### api_key: `str`<a id="api_key-str"></a>

##### api_username: `str`<a id="api_username-str"></a>

##### id: `str`<a id="id-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TopicsSetNotificationLevelRequest`](./discourse_python_sdk/type/topics_set_notification_level_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TopicsSetNotificationLevelResponse`](./discourse_python_sdk/pydantic/topics_set_notification_level_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/t/{id}/notifications.json` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.topics.update_bookmark`<a id="discoursetopicsupdate_bookmark"></a>

Bookmark topic

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
discourse.topics.update_bookmark(
    api_key="Api-Key_example",
    api_username="Api-Username_example",
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: `str`<a id="api_key-str"></a>

##### api_username: `str`<a id="api_username-str"></a>

##### id: `str`<a id="id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/t/{id}/bookmark.json` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.topics.update_status_of_topic`<a id="discoursetopicsupdate_status_of_topic"></a>

Update the status of a topic

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_status_of_topic_response = discourse.topics.update_status_of_topic(
    status="closed",
    enabled="true",
    api_key="Api-Key_example",
    api_username="Api-Username_example",
    id="id_example",
    until="2030-12-31",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### status: `str`<a id="status-str"></a>

##### enabled: `str`<a id="enabled-str"></a>

##### api_key: `str`<a id="api_key-str"></a>

##### api_username: `str`<a id="api_username-str"></a>

##### id: `str`<a id="id-str"></a>

##### until: `str`<a id="until-str"></a>

Only required for `pinned` and `pinned_globally`

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TopicsUpdateStatusOfTopicRequest`](./discourse_python_sdk/type/topics_update_status_of_topic_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TopicsUpdateStatusOfTopicResponse`](./discourse_python_sdk/pydantic/topics_update_status_of_topic_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/t/{id}/status.json` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.topics.update_timestamp_json`<a id="discoursetopicsupdate_timestamp_json"></a>

Update topic timestamp

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_timestamp_json_response = discourse.topics.update_timestamp_json(
    timestamp="1594291380",
    api_key="Api-Key_example",
    api_username="Api-Username_example",
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### timestamp: `str`<a id="timestamp-str"></a>

##### api_key: `str`<a id="api_key-str"></a>

##### api_username: `str`<a id="api_username-str"></a>

##### id: `str`<a id="id-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TopicsUpdateTimestampJsonRequest`](./discourse_python_sdk/type/topics_update_timestamp_json_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TopicsUpdateTimestampJsonResponse`](./discourse_python_sdk/pydantic/topics_update_timestamp_json_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/t/{id}/change-timestamp.json` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.topics.update_topic_by_id_json`<a id="discoursetopicsupdate_topic_by_id_json"></a>

Update a topic

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_topic_by_id_json_response = discourse.topics.update_topic_by_id_json(
    api_key="Api-Key_example",
    api_username="Api-Username_example",
    id="id_example",
    topic={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: `str`<a id="api_key-str"></a>

##### api_username: `str`<a id="api_username-str"></a>

##### id: `str`<a id="id-str"></a>

##### topic: [`TopicsUpdateTopicByIdJsonRequestTopic`](./discourse_python_sdk/type/topics_update_topic_by_id_json_request_topic.py)<a id="topic-topicsupdatetopicbyidjsonrequesttopicdiscourse_python_sdktypetopics_update_topic_by_id_json_request_topicpy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TopicsUpdateTopicByIdJsonRequest`](./discourse_python_sdk/type/topics_update_topic_by_id_json_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TopicsUpdateTopicByIdJsonResponse`](./discourse_python_sdk/pydantic/topics_update_topic_by_id_json_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/t/-/{id}.json` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.uploads.abort_multipart_upload`<a id="discourseuploadsabort_multipart_upload"></a>

This endpoint aborts the multipart upload initiated with /create-multipart.
This should be used when cancelling the upload. It does not matter if parts
were already uploaded into the external storage provider.

You must have the correct permissions and CORS settings configured in your
external provider. We support AWS S3 as the default. See:

https://meta.discourse.org/t/-/210469#s3-multipart-direct-uploads-4.

An external file store must be set up and `enable_direct_s3_uploads` must
be set to true for this endpoint to function.



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
abort_multipart_upload_response = discourse.uploads.abort_multipart_upload(
    external_upload_identifier="84x83tmxy398t3y._Q_z8CoJYVr69bE6D7f8J6Oo0434QquLFoYdGVerWFx9X5HDEI_TP_95c34n853495x35345394.d.ghQ",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### external_upload_identifier: `str`<a id="external_upload_identifier-str"></a>

The identifier of the multipart upload in the external storage provider. This is the multipart upload_id in AWS S3.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UploadsAbortMultipartUploadRequest`](./discourse_python_sdk/type/uploads_abort_multipart_upload_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`UploadsAbortMultipartUploadResponse`](./discourse_python_sdk/pydantic/uploads_abort_multipart_upload_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/uploads/abort-multipart.json` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.uploads.complete_external_upload`<a id="discourseuploadscomplete_external_upload"></a>

Completes an external upload initialized with /get-presigned-put. The
file will be moved from its temporary location in external storage to
a final destination in the S3 bucket. An Upload record will also be
created in the database in most cases.

If a sha1-checksum was provided in the initial request it will also
be compared with the uploaded file in storage to make sure the same
file was uploaded. The file size will be compared for the same reason.

You must have the correct permissions and CORS settings configured in your
external provider. We support AWS S3 as the default. See:

https://meta.discourse.org/t/-/210469#s3-multipart-direct-uploads-4.

An external file store must be set up and `enable_direct_s3_uploads` must
be set to true for this endpoint to function.



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
complete_external_upload_response = discourse.uploads.complete_external_upload(
    unique_identifier="66e86218-80d9-4bda-b4d5-2b6def968705",
    for_private_message="true",
    for_site_setting="true",
    pasted="true",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### unique_identifier: `str`<a id="unique_identifier-str"></a>

The unique identifier returned in the original /generate-presigned-put request.

##### for_private_message: `str`<a id="for_private_message-str"></a>

Optionally set this to true if the upload is for a private message.

##### for_site_setting: `str`<a id="for_site_setting-str"></a>

Optionally set this to true if the upload is for a site setting.

##### pasted: `str`<a id="pasted-str"></a>

Optionally set this to true if the upload was pasted into the upload area. This will convert PNG files to JPEG.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UploadsCompleteExternalUploadRequest`](./discourse_python_sdk/type/uploads_complete_external_upload_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`UploadsCompleteExternalUploadResponse`](./discourse_python_sdk/pydantic/uploads_complete_external_upload_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/uploads/complete-external-upload.json` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.uploads.complete_multipart_upload`<a id="discourseuploadscomplete_multipart_upload"></a>

Completes the multipart upload in the external store, and copies the
file from its temporary location to its final location in the store.
All of the parts must have been uploaded to the external storage provider.
An Upload record will be completed in most cases once the file is copied
to its final location.

You must have the correct permissions and CORS settings configured in your
external provider. We support AWS S3 as the default. See:

https://meta.discourse.org/t/-/210469#s3-multipart-direct-uploads-4.

An external file store must be set up and `enable_direct_s3_uploads` must
be set to true for this endpoint to function.



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
complete_multipart_upload_response = discourse.uploads.complete_multipart_upload(
    unique_identifier="66e86218-80d9-4bda-b4d5-2b6def968705",
    parts=[None, None],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### unique_identifier: `str`<a id="unique_identifier-str"></a>

The unique identifier returned in the original /create-multipart request.

##### parts: List[[`Union[bool, date, datetime, dict, float, int, list, str, None]`](./discourse_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)]<a id="parts-listunionbool-date-datetime-dict-float-int-list-str-nonediscourse_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

All of the part numbers and their corresponding ETags that have been uploaded must be provided.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UploadsCompleteMultipartUploadRequest`](./discourse_python_sdk/type/uploads_complete_multipart_upload_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`UploadsCompleteMultipartUploadResponse`](./discourse_python_sdk/pydantic/uploads_complete_multipart_upload_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/uploads/complete-multipart.json` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.uploads.create_multipart_external_upload`<a id="discourseuploadscreate_multipart_external_upload"></a>

Creates a multipart upload in the external storage provider, storing
a temporary reference to the external upload similar to /get-presigned-put.

You must have the correct permissions and CORS settings configured in your
external provider. We support AWS S3 as the default. See:

https://meta.discourse.org/t/-/210469#s3-multipart-direct-uploads-4.

An external file store must be set up and `enable_direct_s3_uploads` must
be set to true for this endpoint to function.



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_multipart_external_upload_response = (
    discourse.uploads.create_multipart_external_upload(
        upload_type="avatar",
        file_name="IMG_2021.jpeg",
        file_size=4096,
        metadata={},
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### upload_type: `str`<a id="upload_type-str"></a>

##### file_name: `str`<a id="file_name-str"></a>

##### file_size: `int`<a id="file_size-int"></a>

File size should be represented in bytes.

##### metadata: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./discourse_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="metadata-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonediscourse_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UploadsCreateMultipartExternalUploadRequest`](./discourse_python_sdk/type/uploads_create_multipart_external_upload_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`UploadsCreateMultipartExternalUploadResponse`](./discourse_python_sdk/pydantic/uploads_create_multipart_external_upload_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/uploads/create-multipart.json` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.uploads.create_new_upload`<a id="discourseuploadscreate_new_upload"></a>

Creates an upload

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_upload_response = discourse.uploads.create_new_upload(
    type="avatar",
    user_id=1,
    synchronous=True,
    file=open("/path/to/file", "rb"),
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### type: `str`<a id="type-str"></a>

##### user_id: `int`<a id="user_id-int"></a>

required if uploading an avatar

##### synchronous: `bool`<a id="synchronous-bool"></a>

Use this flag to return an id and url

##### file: `IO`<a id="file-io"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UploadsCreateNewUploadRequest`](./discourse_python_sdk/type/uploads_create_new_upload_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`UploadsCreateNewUploadResponse`](./discourse_python_sdk/pydantic/uploads_create_new_upload_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/uploads.json` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.uploads.generate_presigned_urls_for_multipart_parts`<a id="discourseuploadsgenerate_presigned_urls_for_multipart_parts"></a>

Multipart uploads are uploaded in chunks or parts to individual presigned
URLs, similar to the one generated by /generate-presigned-put. The part
numbers provided must be between 1 and 10000. The total number of parts
will depend on the chunk size in bytes that you intend to use to upload
each chunk. For example a 12MB file may have 2 5MB chunks and a final
2MB chunk, for part numbers 1, 2, and 3.

This endpoint will return a presigned URL for each part number provided,
which you can then use to send PUT requests for the binary chunk corresponding
to that part. When the part is uploaded, the provider should return an
ETag for the part, and this should be stored along with the part number,
because this is needed to complete the multipart upload.

You must have the correct permissions and CORS settings configured in your
external provider. We support AWS S3 as the default. See:

https://meta.discourse.org/t/-/210469#s3-multipart-direct-uploads-4.

An external file store must be set up and `enable_direct_s3_uploads` must
be set to true for this endpoint to function.



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_presigned_urls_for_multipart_parts_response = (
    discourse.uploads.generate_presigned_urls_for_multipart_parts(
        part_numbers=[1, 2, 3],
        unique_identifier="66e86218-80d9-4bda-b4d5-2b6def968705",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### part_numbers: List[[`Union[bool, date, datetime, dict, float, int, list, str, None]`](./discourse_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)]<a id="part_numbers-listunionbool-date-datetime-dict-float-int-list-str-nonediscourse_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

The part numbers to generate the presigned URLs for, must be between 1 and 10000.

##### unique_identifier: `str`<a id="unique_identifier-str"></a>

The unique identifier returned in the original /create-multipart request.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UploadsGeneratePresignedUrlsForMultipartPartsRequest`](./discourse_python_sdk/type/uploads_generate_presigned_urls_for_multipart_parts_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`UploadsGeneratePresignedUrlsForMultipartPartsResponse`](./discourse_python_sdk/pydantic/uploads_generate_presigned_urls_for_multipart_parts_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/uploads/batch-presign-multipart-parts.json` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.uploads.initiate_direct_external_upload`<a id="discourseuploadsinitiate_direct_external_upload"></a>

Direct external uploads bypass the usual method of creating uploads
via the POST /uploads route, and upload directly to an external provider,
which by default is S3. This route begins the process, and will return
a unique identifier for the external upload as well as a presigned URL
which is where the file binary blob should be uploaded to.

Once the upload is complete to the external service, you must call the
POST /complete-external-upload route using the unique identifier returned
by this route, which will create any required Upload record in the Discourse
database and also move file from its temporary location to the final
destination in the external storage service.

You must have the correct permissions and CORS settings configured in your
external provider. We support AWS S3 as the default. See:

https://meta.discourse.org/t/-/210469#s3-multipart-direct-uploads-4.

An external file store must be set up and `enable_direct_s3_uploads` must
be set to true for this endpoint to function.



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
initiate_direct_external_upload_response = (
    discourse.uploads.initiate_direct_external_upload(
        type="avatar",
        file_name="IMG_2021.jpeg",
        file_size=4096,
        metadata={},
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### type: `str`<a id="type-str"></a>

##### file_name: `str`<a id="file_name-str"></a>

##### file_size: `int`<a id="file_size-int"></a>

File size should be represented in bytes.

##### metadata: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./discourse_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="metadata-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonediscourse_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UploadsInitiateDirectExternalUploadRequest`](./discourse_python_sdk/type/uploads_initiate_direct_external_upload_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`UploadsInitiateDirectExternalUploadResponse`](./discourse_python_sdk/pydantic/uploads_initiate_direct_external_upload_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/uploads/generate-presigned-put.json` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.users.activate_user`<a id="discourseusersactivate_user"></a>

Activate a user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
activate_user_response = discourse.users.activate_user(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UsersActivateUserResponse`](./discourse_python_sdk/pydantic/users_activate_user_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/admin/users/{id}/activate.json` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.users.anonymize_by_id_json`<a id="discourseusersanonymize_by_id_json"></a>

Anonymize a user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
anonymize_by_id_json_response = discourse.users.anonymize_by_id_json(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UsersAnonymizeByIdJsonResponse`](./discourse_python_sdk/pydantic/users_anonymize_by_id_json_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/admin/users/{id}/anonymize.json` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.users.change_password_action`<a id="discourseuserschange_password_action"></a>

Change password

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
discourse.users.change_password_action(
    username="string_example",
    password="string_example",
    token="token_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### username: `str`<a id="username-str"></a>

##### password: `str`<a id="password-str"></a>

##### token: `str`<a id="token-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersChangePasswordActionRequest`](./discourse_python_sdk/type/users_change_password_action_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/password-reset/{token}.json` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.users.create_user`<a id="discourseuserscreate_user"></a>

Creates a user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_user_response = discourse.users.create_user(
    name="string_example",
    email="string_example",
    password="string_example",
    username="string_example",
    api_key="Api-Key_example",
    api_username="Api-Username_example",
    active=True,
    approved=True,
    user_fields_1=True,
    external_ids={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

##### email: `str`<a id="email-str"></a>

##### password: `str`<a id="password-str"></a>

##### username: `str`<a id="username-str"></a>

##### api_key: `str`<a id="api_key-str"></a>

##### api_username: `str`<a id="api_username-str"></a>

##### active: `bool`<a id="active-bool"></a>

This param requires an api key in the request header or it will be ignored

##### approved: `bool`<a id="approved-bool"></a>

##### user_fields_1: `bool`<a id="user_fields_1-bool"></a>

##### external_ids: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="external_ids-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersCreateUserRequest`](./discourse_python_sdk/type/users_create_user_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`UsersCreateUserResponse`](./discourse_python_sdk/pydantic/users_create_user_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users.json` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.users.deactivate_user`<a id="discourseusersdeactivate_user"></a>

Deactivate a user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
deactivate_user_response = discourse.users.deactivate_user(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UsersDeactivateUserResponse`](./discourse_python_sdk/pydantic/users_deactivate_user_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/admin/users/{id}/deactivate.json` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.users.delete_user_by_id_json`<a id="discourseusersdelete_user_by_id_json"></a>

Delete a user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_user_by_id_json_response = discourse.users.delete_user_by_id_json(
    id=1,
    delete_posts=True,
    block_email=True,
    block_urls=True,
    block_ip=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

##### delete_posts: `bool`<a id="delete_posts-bool"></a>

##### block_email: `bool`<a id="block_email-bool"></a>

##### block_urls: `bool`<a id="block_urls-bool"></a>

##### block_ip: `bool`<a id="block_ip-bool"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersDeleteUserByIdJsonRequest`](./discourse_python_sdk/type/users_delete_user_by_id_json_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`UsersDeleteUserByIdJsonResponse`](./discourse_python_sdk/pydantic/users_delete_user_by_id_json_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/admin/users/{id}.json` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.users.get_emails`<a id="discourseusersget_emails"></a>

Get email addresses belonging to a user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_emails_response = discourse.users.get_emails(
    username="username_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### username: `str`<a id="username-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UsersGetEmailsResponse`](./discourse_python_sdk/pydantic/users_get_emails_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/u/{username}/emails.json` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.users.get_identity_provider_external_id`<a id="discourseusersget_identity_provider_external_id"></a>

Get a user by identity provider external ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_identity_provider_external_id_response = (
    discourse.users.get_identity_provider_external_id(
        api_key="Api-Key_example",
        api_username="Api-Username_example",
        provider="provider_example",
        external_id="external_id_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: `str`<a id="api_key-str"></a>

##### api_username: `str`<a id="api_username-str"></a>

##### provider: `str`<a id="provider-str"></a>

Authentication provider name. Can be found in the provider callback URL: `/auth/{provider}/callback`

##### external_id: `str`<a id="external_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UsersGetIdentityProviderExternalIdResponse`](./discourse_python_sdk/pydantic/users_get_identity_provider_external_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/u/by-external/{provider}/{external_id}.json` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.users.get_list_of_users`<a id="discourseusersget_list_of_users"></a>

Get a list of users

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_list_of_users_response = discourse.users.get_list_of_users(
    flag="active",
    order="created",
    asc="true",
    page=1,
    show_emails=True,
    stats=True,
    email="string_example",
    ip="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### flag: `str`<a id="flag-str"></a>

##### order: `str`<a id="order-str"></a>

##### asc: `str`<a id="asc-str"></a>

##### page: `int`<a id="page-int"></a>

##### show_emails: `bool`<a id="show_emails-bool"></a>

Include user email addresses in response. These requests will be logged in the staff action logs.

##### stats: `bool`<a id="stats-bool"></a>

Include user stats information

##### email: `str`<a id="email-str"></a>

Filter to the user with this email address

##### ip: `str`<a id="ip-str"></a>

Filter to users with this IP address

#### 🔄 Return<a id="🔄-return"></a>

[`UsersGetListOfUsersResponse`](./discourse_python_sdk/pydantic/users_get_list_of_users_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/admin/users/list/{flag}.json` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.users.get_user_by_external_id`<a id="discourseusersget_user_by_external_id"></a>

Get a user by external_id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_by_external_id_response = discourse.users.get_user_by_external_id(
    api_key="Api-Key_example",
    api_username="Api-Username_example",
    external_id="external_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: `str`<a id="api_key-str"></a>

##### api_username: `str`<a id="api_username-str"></a>

##### external_id: `str`<a id="external_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UsersGetUserByExternalIdResponse`](./discourse_python_sdk/pydantic/users_get_user_by_external_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/u/by-external/{external_id}.json` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.users.get_user_by_id_json`<a id="discourseusersget_user_by_id_json"></a>

Get a user by id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_by_id_json_response = discourse.users.get_user_by_id_json(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UsersGetUserByIdJsonResponse`](./discourse_python_sdk/pydantic/users_get_user_by_id_json_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/admin/users/{id}.json` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.users.get_user_by_username`<a id="discourseusersget_user_by_username"></a>

Get a single user by username

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_by_username_response = discourse.users.get_user_by_username(
    api_key="Api-Key_example",
    api_username="Api-Username_example",
    username="username_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: `str`<a id="api_key-str"></a>

##### api_username: `str`<a id="api_username-str"></a>

##### username: `str`<a id="username-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UsersGetUserByUsernameResponse`](./discourse_python_sdk/pydantic/users_get_user_by_username_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/u/{username}.json` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.users.list_public_user`<a id="discourseuserslist_public_user"></a>

Get a public list of users

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_public_user_response = discourse.users.list_public_user(
    period="daily",
    order="likes_received",
    asc="true",
    page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### period: `str`<a id="period-str"></a>

##### order: `str`<a id="order-str"></a>

##### asc: `str`<a id="asc-str"></a>

##### page: `int`<a id="page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UsersListPublicUserResponse`](./discourse_python_sdk/pydantic/users_list_public_user_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/directory_items.json` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.users.list_user_actions`<a id="discourseuserslist_user_actions"></a>

Get a list of user actions

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_user_actions_response = discourse.users.list_user_actions(
    offset=1,
    username="username_example",
    filter="filter_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### offset: `int`<a id="offset-int"></a>

##### username: `str`<a id="username-str"></a>

##### filter: `str`<a id="filter-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UsersListUserActionsResponse`](./discourse_python_sdk/pydantic/users_list_user_actions_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/user_actions.json` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.users.list_user_badges`<a id="discourseuserslist_user_badges"></a>

List badges for a user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_user_badges_response = discourse.users.list_user_badges(
    username="username_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### username: `str`<a id="username-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`BadgesListUserBadgesResponse`](./discourse_python_sdk/pydantic/badges_list_user_badges_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/user-badges/{username}.json` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.users.log_out_user_action`<a id="discourseuserslog_out_user_action"></a>

Log a user out

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
log_out_user_action_response = discourse.users.log_out_user_action(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UsersLogOutUserActionResponse`](./discourse_python_sdk/pydantic/users_log_out_user_action_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/admin/users/{id}/log_out.json` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.users.refresh_gravatar_post`<a id="discourseusersrefresh_gravatar_post"></a>

Refresh gravatar

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
refresh_gravatar_post_response = discourse.users.refresh_gravatar_post(
    username="username_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### username: `str`<a id="username-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UsersRefreshGravatarPostResponse`](./discourse_python_sdk/pydantic/users_refresh_gravatar_post_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/user_avatar/{username}/refresh_gravatar.json` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.users.send_password_reset_email`<a id="discourseuserssend_password_reset_email"></a>

Send password reset email

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
send_password_reset_email_response = discourse.users.send_password_reset_email(
    login="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### login: `str`<a id="login-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersSendPasswordResetEmailRequest`](./discourse_python_sdk/type/users_send_password_reset_email_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`UsersSendPasswordResetEmailResponse`](./discourse_python_sdk/pydantic/users_send_password_reset_email_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/session/forgot_password.json` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.users.silence_by_id`<a id="discourseuserssilence_by_id"></a>

Silence a user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
silence_by_id_response = discourse.users.silence_by_id(
    id=1,
    silenced_till="2022-06-01T08:00:00.000Z",
    reason="string_example",
    message="string_example",
    post_action="delete",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

##### silenced_till: `str`<a id="silenced_till-str"></a>

##### reason: `str`<a id="reason-str"></a>

##### message: `str`<a id="message-str"></a>

Will send an email with this message when present

##### post_action: `str`<a id="post_action-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersSilenceByIdRequest`](./discourse_python_sdk/type/users_silence_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`UsersSilenceByIdResponse`](./discourse_python_sdk/pydantic/users_silence_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/admin/users/{id}/silence.json` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.users.suspend_by_id_json`<a id="discourseuserssuspend_by_id_json"></a>

Suspend a user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
suspend_by_id_json_response = discourse.users.suspend_by_id_json(
    suspend_until="2121-02-22",
    reason="string_example",
    id=1,
    message="string_example",
    post_action="delete",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### suspend_until: `str`<a id="suspend_until-str"></a>

##### reason: `str`<a id="reason-str"></a>

##### id: `int`<a id="id-int"></a>

##### message: `str`<a id="message-str"></a>

Will send an email with this message when present

##### post_action: `str`<a id="post_action-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersSuspendByIdJsonRequest`](./discourse_python_sdk/type/users_suspend_by_id_json_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`UsersSuspendByIdJsonResponse`](./discourse_python_sdk/pydantic/users_suspend_by_id_json_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/admin/users/{id}/suspend.json` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.users.update_avatar`<a id="discourseusersupdate_avatar"></a>

Update avatar

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_avatar_response = discourse.users.update_avatar(
    upload_id=1,
    type="uploaded",
    username="username_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### upload_id: `int`<a id="upload_id-int"></a>

##### type: `str`<a id="type-str"></a>

##### username: `str`<a id="username-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersUpdateAvatarRequest`](./discourse_python_sdk/type/users_update_avatar_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`UsersUpdateAvatarResponse`](./discourse_python_sdk/pydantic/users_update_avatar_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/u/{username}/preferences/avatar/pick.json` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.users.update_email_preferences`<a id="discourseusersupdate_email_preferences"></a>

Update email

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
discourse.users.update_email_preferences(
    email="string_example",
    username="username_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### email: `str`<a id="email-str"></a>

##### username: `str`<a id="username-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersUpdateEmailPreferencesRequest`](./discourse_python_sdk/type/users_update_email_preferences_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/u/{username}/preferences/email.json` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.users.update_preferences_json`<a id="discourseusersupdate_preferences_json"></a>

Update username

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
discourse.users.update_preferences_json(
    new_username="string_example",
    username="username_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### new_username: `str`<a id="new_username-str"></a>

##### username: `str`<a id="username-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersUpdatePreferencesJsonRequest`](./discourse_python_sdk/type/users_update_preferences_json_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/u/{username}/preferences/username.json` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `discourse.users.update_user_details`<a id="discourseusersupdate_user_details"></a>

Update a user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_user_details_response = discourse.users.update_user_details(
    api_key="Api-Key_example",
    api_username="Api-Username_example",
    username="username_example",
    name="string_example",
    external_ids={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: `str`<a id="api_key-str"></a>

##### api_username: `str`<a id="api_username-str"></a>

##### username: `str`<a id="username-str"></a>

##### name: `str`<a id="name-str"></a>

##### external_ids: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="external_ids-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersUpdateUserDetailsRequest`](./discourse_python_sdk/type/users_update_user_details_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`UsersUpdateUserDetailsResponse`](./discourse_python_sdk/pydantic/users_update_user_details_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/u/{username}.json` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
