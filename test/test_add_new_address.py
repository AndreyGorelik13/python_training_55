import pytest
from fixture.application import Application
from model.address import Address

@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_new_address(app):
    app.session.login("admin", "secret")
    app.address.create(Address("firstname", "middlename", "lastname", "nickname", "title", "company", "address",
                            "home", "mobile", "work", "fax", "email", "email2", "email3", "homepage"))
    app.session.logout()

def test_add_empty_address(app):
    app.session.login("admin", "secret")
    app.address.create(Address("", "", "", "", "", "", "",
                            "", "", "", "", "", "", "", ""))
    app.session.logout()