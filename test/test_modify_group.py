from model.group import Group

def test_modify_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name = "firstname"))
    app.group.modify_first_group(Group("changed value", "changed value", "changed value"))