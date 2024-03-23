import typing_extensions

from discourse_python_sdk.paths import PathValues
from discourse_python_sdk.apis.paths.admin_backups_json import AdminBackupsJson
from discourse_python_sdk.apis.paths.admin_backups_filename import AdminBackupsFilename
from discourse_python_sdk.apis.paths.admin_badges_json import AdminBadgesJson
from discourse_python_sdk.apis.paths.admin_badges_id_json import AdminBadgesIdJson
from discourse_python_sdk.apis.paths.categories_json import CategoriesJson
from discourse_python_sdk.apis.paths.categories_id_json import CategoriesIdJson
from discourse_python_sdk.apis.paths.c_slug_id_json import CSlugIdJson
from discourse_python_sdk.apis.paths.c_id_show_json import CIdShowJson
from discourse_python_sdk.apis.paths.admin_groups_json import AdminGroupsJson
from discourse_python_sdk.apis.paths.admin_groups_id_json import AdminGroupsIdJson
from discourse_python_sdk.apis.paths.groups_id_json import GroupsIdJson
from discourse_python_sdk.apis.paths.groups_id_members_json import GroupsIdMembersJson
from discourse_python_sdk.apis.paths.groups_json import GroupsJson
from discourse_python_sdk.apis.paths.invites_json import InvitesJson
from discourse_python_sdk.apis.paths.invites_create_multiple_json import InvitesCreateMultipleJson
from discourse_python_sdk.apis.paths.notifications_json import NotificationsJson
from discourse_python_sdk.apis.paths.notifications_mark_read_json import NotificationsMarkReadJson
from discourse_python_sdk.apis.paths.posts_json import PostsJson
from discourse_python_sdk.apis.paths.posts_id_json import PostsIdJson
from discourse_python_sdk.apis.paths.posts_id_replies_json import PostsIdRepliesJson
from discourse_python_sdk.apis.paths.posts_id_locked_json import PostsIdLockedJson
from discourse_python_sdk.apis.paths.post_actions_json import PostActionsJson
from discourse_python_sdk.apis.paths.topics_private_messages_username_json import TopicsPrivateMessagesUsernameJson
from discourse_python_sdk.apis.paths.topics_private_messages_sent_username_json import TopicsPrivateMessagesSentUsernameJson
from discourse_python_sdk.apis.paths.search_json import SearchJson
from discourse_python_sdk.apis.paths.site_json import SiteJson
from discourse_python_sdk.apis.paths.tag_groups_json import TagGroupsJson
from discourse_python_sdk.apis.paths.tag_groups_id_json import TagGroupsIdJson
from discourse_python_sdk.apis.paths.tags_json import TagsJson
from discourse_python_sdk.apis.paths.tag_name_json import TagNameJson
from discourse_python_sdk.apis.paths.t_id_posts_json import TIdPostsJson
from discourse_python_sdk.apis.paths.t_id_json import TIdJson
from discourse_python_sdk.apis.paths.t___id_json import TIdJson
from discourse_python_sdk.apis.paths.t_id_invite_json import TIdInviteJson
from discourse_python_sdk.apis.paths.t_id_bookmark_json import TIdBookmarkJson
from discourse_python_sdk.apis.paths.t_id_status_json import TIdStatusJson
from discourse_python_sdk.apis.paths.latest_json import LatestJson
from discourse_python_sdk.apis.paths.top_json import TopJson
from discourse_python_sdk.apis.paths.t_id_notifications_json import TIdNotificationsJson
from discourse_python_sdk.apis.paths.t_id_change_timestamp_json import TIdChangeTimestampJson
from discourse_python_sdk.apis.paths.t_id_timer_json import TIdTimerJson
from discourse_python_sdk.apis.paths.t_external_id_external_id_json import TExternalIdExternalIdJson
from discourse_python_sdk.apis.paths.uploads_json import UploadsJson
from discourse_python_sdk.apis.paths.uploads_generate_presigned_put_json import UploadsGeneratePresignedPutJson
from discourse_python_sdk.apis.paths.uploads_complete_external_upload_json import UploadsCompleteExternalUploadJson
from discourse_python_sdk.apis.paths.uploads_create_multipart_json import UploadsCreateMultipartJson
from discourse_python_sdk.apis.paths.uploads_batch_presign_multipart_parts_json import UploadsBatchPresignMultipartPartsJson
from discourse_python_sdk.apis.paths.uploads_abort_multipart_json import UploadsAbortMultipartJson
from discourse_python_sdk.apis.paths.uploads_complete_multipart_json import UploadsCompleteMultipartJson
from discourse_python_sdk.apis.paths.user_badges_username_json import UserBadgesUsernameJson
from discourse_python_sdk.apis.paths.users_json import UsersJson
from discourse_python_sdk.apis.paths.u_username_json import UUsernameJson
from discourse_python_sdk.apis.paths.u_by_external_external_id_json import UByExternalExternalIdJson
from discourse_python_sdk.apis.paths.u_by_external_provider_external_id_json import UByExternalProviderExternalIdJson
from discourse_python_sdk.apis.paths.u_username_preferences_avatar_pick_json import UUsernamePreferencesAvatarPickJson
from discourse_python_sdk.apis.paths.u_username_preferences_email_json import UUsernamePreferencesEmailJson
from discourse_python_sdk.apis.paths.u_username_preferences_username_json import UUsernamePreferencesUsernameJson
from discourse_python_sdk.apis.paths.directory_items_json import DirectoryItemsJson
from discourse_python_sdk.apis.paths.admin_users_id_json import AdminUsersIdJson
from discourse_python_sdk.apis.paths.admin_users_id_activate_json import AdminUsersIdActivateJson
from discourse_python_sdk.apis.paths.admin_users_id_deactivate_json import AdminUsersIdDeactivateJson
from discourse_python_sdk.apis.paths.admin_users_id_suspend_json import AdminUsersIdSuspendJson
from discourse_python_sdk.apis.paths.admin_users_id_silence_json import AdminUsersIdSilenceJson
from discourse_python_sdk.apis.paths.admin_users_id_anonymize_json import AdminUsersIdAnonymizeJson
from discourse_python_sdk.apis.paths.admin_users_id_log_out_json import AdminUsersIdLogOutJson
from discourse_python_sdk.apis.paths.user_avatar_username_refresh_gravatar_json import UserAvatarUsernameRefreshGravatarJson
from discourse_python_sdk.apis.paths.admin_users_list_flag_json import AdminUsersListFlagJson
from discourse_python_sdk.apis.paths.user_actions_json import UserActionsJson
from discourse_python_sdk.apis.paths.session_forgot_password_json import SessionForgotPasswordJson
from discourse_python_sdk.apis.paths.users_password_reset_token_json import UsersPasswordResetTokenJson
from discourse_python_sdk.apis.paths.u_username_emails_json import UUsernameEmailsJson

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.ADMIN_BACKUPS_JSON: AdminBackupsJson,
        PathValues.ADMIN_BACKUPS_FILENAME: AdminBackupsFilename,
        PathValues.ADMIN_BADGES_JSON: AdminBadgesJson,
        PathValues.ADMIN_BADGES_ID_JSON: AdminBadgesIdJson,
        PathValues.CATEGORIES_JSON: CategoriesJson,
        PathValues.CATEGORIES_ID_JSON: CategoriesIdJson,
        PathValues.C_SLUG_ID_JSON: CSlugIdJson,
        PathValues.C_ID_SHOW_JSON: CIdShowJson,
        PathValues.ADMIN_GROUPS_JSON: AdminGroupsJson,
        PathValues.ADMIN_GROUPS_ID_JSON: AdminGroupsIdJson,
        PathValues.GROUPS_ID_JSON: GroupsIdJson,
        PathValues.GROUPS_ID_MEMBERS_JSON: GroupsIdMembersJson,
        PathValues.GROUPS_JSON: GroupsJson,
        PathValues.INVITES_JSON: InvitesJson,
        PathValues.INVITES_CREATEMULTIPLE_JSON: InvitesCreateMultipleJson,
        PathValues.NOTIFICATIONS_JSON: NotificationsJson,
        PathValues.NOTIFICATIONS_MARKREAD_JSON: NotificationsMarkReadJson,
        PathValues.POSTS_JSON: PostsJson,
        PathValues.POSTS_ID_JSON: PostsIdJson,
        PathValues.POSTS_ID_REPLIES_JSON: PostsIdRepliesJson,
        PathValues.POSTS_ID_LOCKED_JSON: PostsIdLockedJson,
        PathValues.POST_ACTIONS_JSON: PostActionsJson,
        PathValues.TOPICS_PRIVATEMESSAGES_USERNAME_JSON: TopicsPrivateMessagesUsernameJson,
        PathValues.TOPICS_PRIVATEMESSAGESSENT_USERNAME_JSON: TopicsPrivateMessagesSentUsernameJson,
        PathValues.SEARCH_JSON: SearchJson,
        PathValues.SITE_JSON: SiteJson,
        PathValues.TAG_GROUPS_JSON: TagGroupsJson,
        PathValues.TAG_GROUPS_ID_JSON: TagGroupsIdJson,
        PathValues.TAGS_JSON: TagsJson,
        PathValues.TAG_NAME_JSON: TagNameJson,
        PathValues.T_ID_POSTS_JSON: TIdPostsJson,
        PathValues.T_ID_JSON: TIdJson,
        PathValues.T__ID_JSON: TIdJson,
        PathValues.T_ID_INVITE_JSON: TIdInviteJson,
        PathValues.T_ID_BOOKMARK_JSON: TIdBookmarkJson,
        PathValues.T_ID_STATUS_JSON: TIdStatusJson,
        PathValues.LATEST_JSON: LatestJson,
        PathValues.TOP_JSON: TopJson,
        PathValues.T_ID_NOTIFICATIONS_JSON: TIdNotificationsJson,
        PathValues.T_ID_CHANGETIMESTAMP_JSON: TIdChangeTimestampJson,
        PathValues.T_ID_TIMER_JSON: TIdTimerJson,
        PathValues.T_EXTERNAL_ID_EXTERNAL_ID_JSON: TExternalIdExternalIdJson,
        PathValues.UPLOADS_JSON: UploadsJson,
        PathValues.UPLOADS_GENERATEPRESIGNEDPUT_JSON: UploadsGeneratePresignedPutJson,
        PathValues.UPLOADS_COMPLETEEXTERNALUPLOAD_JSON: UploadsCompleteExternalUploadJson,
        PathValues.UPLOADS_CREATEMULTIPART_JSON: UploadsCreateMultipartJson,
        PathValues.UPLOADS_BATCHPRESIGNMULTIPARTPARTS_JSON: UploadsBatchPresignMultipartPartsJson,
        PathValues.UPLOADS_ABORTMULTIPART_JSON: UploadsAbortMultipartJson,
        PathValues.UPLOADS_COMPLETEMULTIPART_JSON: UploadsCompleteMultipartJson,
        PathValues.USERBADGES_USERNAME_JSON: UserBadgesUsernameJson,
        PathValues.USERS_JSON: UsersJson,
        PathValues.U_USERNAME_JSON: UUsernameJson,
        PathValues.U_BYEXTERNAL_EXTERNAL_ID_JSON: UByExternalExternalIdJson,
        PathValues.U_BYEXTERNAL_PROVIDER_EXTERNAL_ID_JSON: UByExternalProviderExternalIdJson,
        PathValues.U_USERNAME_PREFERENCES_AVATAR_PICK_JSON: UUsernamePreferencesAvatarPickJson,
        PathValues.U_USERNAME_PREFERENCES_EMAIL_JSON: UUsernamePreferencesEmailJson,
        PathValues.U_USERNAME_PREFERENCES_USERNAME_JSON: UUsernamePreferencesUsernameJson,
        PathValues.DIRECTORY_ITEMS_JSON: DirectoryItemsJson,
        PathValues.ADMIN_USERS_ID_JSON: AdminUsersIdJson,
        PathValues.ADMIN_USERS_ID_ACTIVATE_JSON: AdminUsersIdActivateJson,
        PathValues.ADMIN_USERS_ID_DEACTIVATE_JSON: AdminUsersIdDeactivateJson,
        PathValues.ADMIN_USERS_ID_SUSPEND_JSON: AdminUsersIdSuspendJson,
        PathValues.ADMIN_USERS_ID_SILENCE_JSON: AdminUsersIdSilenceJson,
        PathValues.ADMIN_USERS_ID_ANONYMIZE_JSON: AdminUsersIdAnonymizeJson,
        PathValues.ADMIN_USERS_ID_LOG_OUT_JSON: AdminUsersIdLogOutJson,
        PathValues.USER_AVATAR_USERNAME_REFRESH_GRAVATAR_JSON: UserAvatarUsernameRefreshGravatarJson,
        PathValues.ADMIN_USERS_LIST_FLAG_JSON: AdminUsersListFlagJson,
        PathValues.USER_ACTIONS_JSON: UserActionsJson,
        PathValues.SESSION_FORGOT_PASSWORD_JSON: SessionForgotPasswordJson,
        PathValues.USERS_PASSWORDRESET_TOKEN_JSON: UsersPasswordResetTokenJson,
        PathValues.U_USERNAME_EMAILS_JSON: UUsernameEmailsJson,
    }
)

path_to_api = PathToApi(
    {
        PathValues.ADMIN_BACKUPS_JSON: AdminBackupsJson,
        PathValues.ADMIN_BACKUPS_FILENAME: AdminBackupsFilename,
        PathValues.ADMIN_BADGES_JSON: AdminBadgesJson,
        PathValues.ADMIN_BADGES_ID_JSON: AdminBadgesIdJson,
        PathValues.CATEGORIES_JSON: CategoriesJson,
        PathValues.CATEGORIES_ID_JSON: CategoriesIdJson,
        PathValues.C_SLUG_ID_JSON: CSlugIdJson,
        PathValues.C_ID_SHOW_JSON: CIdShowJson,
        PathValues.ADMIN_GROUPS_JSON: AdminGroupsJson,
        PathValues.ADMIN_GROUPS_ID_JSON: AdminGroupsIdJson,
        PathValues.GROUPS_ID_JSON: GroupsIdJson,
        PathValues.GROUPS_ID_MEMBERS_JSON: GroupsIdMembersJson,
        PathValues.GROUPS_JSON: GroupsJson,
        PathValues.INVITES_JSON: InvitesJson,
        PathValues.INVITES_CREATEMULTIPLE_JSON: InvitesCreateMultipleJson,
        PathValues.NOTIFICATIONS_JSON: NotificationsJson,
        PathValues.NOTIFICATIONS_MARKREAD_JSON: NotificationsMarkReadJson,
        PathValues.POSTS_JSON: PostsJson,
        PathValues.POSTS_ID_JSON: PostsIdJson,
        PathValues.POSTS_ID_REPLIES_JSON: PostsIdRepliesJson,
        PathValues.POSTS_ID_LOCKED_JSON: PostsIdLockedJson,
        PathValues.POST_ACTIONS_JSON: PostActionsJson,
        PathValues.TOPICS_PRIVATEMESSAGES_USERNAME_JSON: TopicsPrivateMessagesUsernameJson,
        PathValues.TOPICS_PRIVATEMESSAGESSENT_USERNAME_JSON: TopicsPrivateMessagesSentUsernameJson,
        PathValues.SEARCH_JSON: SearchJson,
        PathValues.SITE_JSON: SiteJson,
        PathValues.TAG_GROUPS_JSON: TagGroupsJson,
        PathValues.TAG_GROUPS_ID_JSON: TagGroupsIdJson,
        PathValues.TAGS_JSON: TagsJson,
        PathValues.TAG_NAME_JSON: TagNameJson,
        PathValues.T_ID_POSTS_JSON: TIdPostsJson,
        PathValues.T_ID_JSON: TIdJson,
        PathValues.T__ID_JSON: TIdJson,
        PathValues.T_ID_INVITE_JSON: TIdInviteJson,
        PathValues.T_ID_BOOKMARK_JSON: TIdBookmarkJson,
        PathValues.T_ID_STATUS_JSON: TIdStatusJson,
        PathValues.LATEST_JSON: LatestJson,
        PathValues.TOP_JSON: TopJson,
        PathValues.T_ID_NOTIFICATIONS_JSON: TIdNotificationsJson,
        PathValues.T_ID_CHANGETIMESTAMP_JSON: TIdChangeTimestampJson,
        PathValues.T_ID_TIMER_JSON: TIdTimerJson,
        PathValues.T_EXTERNAL_ID_EXTERNAL_ID_JSON: TExternalIdExternalIdJson,
        PathValues.UPLOADS_JSON: UploadsJson,
        PathValues.UPLOADS_GENERATEPRESIGNEDPUT_JSON: UploadsGeneratePresignedPutJson,
        PathValues.UPLOADS_COMPLETEEXTERNALUPLOAD_JSON: UploadsCompleteExternalUploadJson,
        PathValues.UPLOADS_CREATEMULTIPART_JSON: UploadsCreateMultipartJson,
        PathValues.UPLOADS_BATCHPRESIGNMULTIPARTPARTS_JSON: UploadsBatchPresignMultipartPartsJson,
        PathValues.UPLOADS_ABORTMULTIPART_JSON: UploadsAbortMultipartJson,
        PathValues.UPLOADS_COMPLETEMULTIPART_JSON: UploadsCompleteMultipartJson,
        PathValues.USERBADGES_USERNAME_JSON: UserBadgesUsernameJson,
        PathValues.USERS_JSON: UsersJson,
        PathValues.U_USERNAME_JSON: UUsernameJson,
        PathValues.U_BYEXTERNAL_EXTERNAL_ID_JSON: UByExternalExternalIdJson,
        PathValues.U_BYEXTERNAL_PROVIDER_EXTERNAL_ID_JSON: UByExternalProviderExternalIdJson,
        PathValues.U_USERNAME_PREFERENCES_AVATAR_PICK_JSON: UUsernamePreferencesAvatarPickJson,
        PathValues.U_USERNAME_PREFERENCES_EMAIL_JSON: UUsernamePreferencesEmailJson,
        PathValues.U_USERNAME_PREFERENCES_USERNAME_JSON: UUsernamePreferencesUsernameJson,
        PathValues.DIRECTORY_ITEMS_JSON: DirectoryItemsJson,
        PathValues.ADMIN_USERS_ID_JSON: AdminUsersIdJson,
        PathValues.ADMIN_USERS_ID_ACTIVATE_JSON: AdminUsersIdActivateJson,
        PathValues.ADMIN_USERS_ID_DEACTIVATE_JSON: AdminUsersIdDeactivateJson,
        PathValues.ADMIN_USERS_ID_SUSPEND_JSON: AdminUsersIdSuspendJson,
        PathValues.ADMIN_USERS_ID_SILENCE_JSON: AdminUsersIdSilenceJson,
        PathValues.ADMIN_USERS_ID_ANONYMIZE_JSON: AdminUsersIdAnonymizeJson,
        PathValues.ADMIN_USERS_ID_LOG_OUT_JSON: AdminUsersIdLogOutJson,
        PathValues.USER_AVATAR_USERNAME_REFRESH_GRAVATAR_JSON: UserAvatarUsernameRefreshGravatarJson,
        PathValues.ADMIN_USERS_LIST_FLAG_JSON: AdminUsersListFlagJson,
        PathValues.USER_ACTIONS_JSON: UserActionsJson,
        PathValues.SESSION_FORGOT_PASSWORD_JSON: SessionForgotPasswordJson,
        PathValues.USERS_PASSWORDRESET_TOKEN_JSON: UsersPasswordResetTokenJson,
        PathValues.U_USERNAME_EMAILS_JSON: UUsernameEmailsJson,
    }
)
