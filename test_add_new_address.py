import pytest
from application import Application
from address import Address

@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_new_address(app):
    app.login("admin", "secret")
    app.create_address(Address("firstname", "middlename", "lastname", "nickname", "title", "company", "address",
                            "home", "mobile", "work", "fax", "email", "email2", "email3", "homepage"))
    app.logout()

def test_add_empty_address(app):
    app.login("admin", "secret")
    app.create_address(Address("", "", "", "", "", "", "",
                            "", "", "", "", "", "", "", ""))
    app.logout()