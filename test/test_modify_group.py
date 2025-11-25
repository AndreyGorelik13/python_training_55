import random

from model.group import Group

def test_modify_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name = "firstname"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    group.name = Group(name="changed value").name
    app.group.modify_group_by_id(group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)