import pytest
from application import Application
from group import Group

@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_new_group(app):
    app.login( "admin", "secret")
    app.create_group(Group("new_test", "new_test", "new_test"))
    app.logout()

def test_add_empty_group(app):
    app.login("admin", "secret")
    app.create_group(Group("", "", ""))
    app.logout()