from model.address import Address

def test_modify_first_address(app):
    if app.address.count() == 0:
        app.address.create(Address(firstname = "firstname"))
    app.address.modify_first_address(Address("changed value", "changed value", "changed value", "changed value", "changed value", "changed value", "changed value",
                            "changed value", "changed value", "changed value", "changed value", "changed value", "changed value", "changed value", "changed value"))