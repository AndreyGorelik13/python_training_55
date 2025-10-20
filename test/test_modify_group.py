from model.group import Group

def test_modify_first_group(app):
    app.session.login( "admin", "secret")
    app.group.modify_first_group(Group("changed value", "changed value", "changed value"))
    app.session.logout()