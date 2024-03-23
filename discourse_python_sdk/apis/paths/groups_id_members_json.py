from discourse_python_sdk.paths.groups_id_members_json.get import ApiForget
from discourse_python_sdk.paths.groups_id_members_json.put import ApiForput
from discourse_python_sdk.paths.groups_id_members_json.delete import ApiFordelete


class GroupsIdMembersJson(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
