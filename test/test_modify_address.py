from model.address import Address

def test_modify_first_address(app):
    app.session.login("admin", "secret")
    app.address.modify_first_address(Address("changed value", "changed value", "changed value", "changed value", "changed value", "changed value", "changed value",
                            "changed value", "changed value", "changed value", "changed value", "changed value", "changed value", "changed value", "changed value"))
    app.session.logout()