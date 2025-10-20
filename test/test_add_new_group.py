from model.group import Group

def test_add_new_group(app):
    app.session.login( "admin", "secret")
    app.group.create(Group("new_test", "new_test", "new_test"))
    app.session.logout()

def test_add_empty_group(app):
    app.session.login("admin", "secret")
    app.group.create(Group("", "", ""))
    app.session.logout()