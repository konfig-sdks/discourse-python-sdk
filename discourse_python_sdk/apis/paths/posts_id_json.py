from discourse_python_sdk.paths.posts_id_json.get import ApiForget
from discourse_python_sdk.paths.posts_id_json.put import ApiForput
from discourse_python_sdk.paths.posts_id_json.delete import ApiFordelete


class PostsIdJson(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
