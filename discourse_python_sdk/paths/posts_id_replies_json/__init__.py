# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from discourse_python_sdk.paths.posts_id_replies_json import Api

from discourse_python_sdk.paths import PathValues

path = PathValues.POSTS_ID_REPLIES_JSON