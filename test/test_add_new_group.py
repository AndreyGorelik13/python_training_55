from model.group import Group

def test_add_new_group(app):
    app.group.create(Group("new_test", "new_test", "new_test"))

def test_add_empty_group(app):
    app.group.create(Group("", "", ""))