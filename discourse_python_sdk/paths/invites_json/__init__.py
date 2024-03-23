# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from discourse_python_sdk.paths.invites_json import Api

from discourse_python_sdk.paths import PathValues

path = PathValues.INVITES_JSON