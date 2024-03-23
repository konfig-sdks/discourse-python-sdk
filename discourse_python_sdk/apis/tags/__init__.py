# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from discourse_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    USERS = "Users"
    TOPICS = "Topics"
    ADMIN = "Admin"
    GROUPS = "Groups"
    POSTS = "Posts"
    UPLOADS = "Uploads"
    CATEGORIES = "Categories"
    TAGS = "Tags"
    BADGES = "Badges"
    BACKUPS = "Backups"
    INVITES = "Invites"
    PRIVATE_MESSAGES = "Private Messages"
    NOTIFICATIONS = "Notifications"
    SEARCH = "Search"
    SITE = "Site"
