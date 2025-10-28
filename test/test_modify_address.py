from model.address import Address

def test_modify_first_address(app):
    app.address.modify_first_address(Address("changed value", "changed value", "changed value", "changed value", "changed value", "changed value", "changed value",
                            "changed value", "changed value", "changed value", "changed value", "changed value", "changed value", "changed value", "changed value"))