# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from discourse_python_sdk.paths.user_actions_json import Api

from discourse_python_sdk.paths import PathValues

path = PathValues.USER_ACTIONS_JSON