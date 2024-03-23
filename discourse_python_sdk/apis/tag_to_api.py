import typing_extensions

from discourse_python_sdk.apis.tags import TagValues
from discourse_python_sdk.apis.tags.users_api import UsersApi
from discourse_python_sdk.apis.tags.topics_api import TopicsApi
from discourse_python_sdk.apis.tags.admin_api import AdminApi
from discourse_python_sdk.apis.tags.groups_api import GroupsApi
from discourse_python_sdk.apis.tags.posts_api import PostsApi
from discourse_python_sdk.apis.tags.uploads_api import UploadsApi
from discourse_python_sdk.apis.tags.categories_api import CategoriesApi
from discourse_python_sdk.apis.tags.tags_api import TagsApi
from discourse_python_sdk.apis.tags.badges_api import BadgesApi
from discourse_python_sdk.apis.tags.backups_api import BackupsApi
from discourse_python_sdk.apis.tags.invites_api import InvitesApi
from discourse_python_sdk.apis.tags.private_messages_api import PrivateMessagesApi
from discourse_python_sdk.apis.tags.notifications_api import NotificationsApi
from discourse_python_sdk.apis.tags.search_api import SearchApi
from discourse_python_sdk.apis.tags.site_api import SiteApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.USERS: UsersApi,
        TagValues.TOPICS: TopicsApi,
        TagValues.ADMIN: AdminApi,
        TagValues.GROUPS: GroupsApi,
        TagValues.POSTS: PostsApi,
        TagValues.UPLOADS: UploadsApi,
        TagValues.CATEGORIES: CategoriesApi,
        TagValues.TAGS: TagsApi,
        TagValues.BADGES: BadgesApi,
        TagValues.BACKUPS: BackupsApi,
        TagValues.INVITES: InvitesApi,
        TagValues.PRIVATE_MESSAGES: PrivateMessagesApi,
        TagValues.NOTIFICATIONS: NotificationsApi,
        TagValues.SEARCH: SearchApi,
        TagValues.SITE: SiteApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.USERS: UsersApi,
        TagValues.TOPICS: TopicsApi,
        TagValues.ADMIN: AdminApi,
        TagValues.GROUPS: GroupsApi,
        TagValues.POSTS: PostsApi,
        TagValues.UPLOADS: UploadsApi,
        TagValues.CATEGORIES: CategoriesApi,
        TagValues.TAGS: TagsApi,
        TagValues.BADGES: BadgesApi,
        TagValues.BACKUPS: BackupsApi,
        TagValues.INVITES: InvitesApi,
        TagValues.PRIVATE_MESSAGES: PrivateMessagesApi,
        TagValues.NOTIFICATIONS: NotificationsApi,
        TagValues.SEARCH: SearchApi,
        TagValues.SITE: SiteApi,
    }
)
