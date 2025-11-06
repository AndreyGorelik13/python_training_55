from model.address import Address

def test_modify_first_address(app):
    if app.address.count() == 0:
        app.address.create(Address(firstname = "firstname"))
    old_addresses = app.address.get_address_list()
    address = Address("changed value", "changed value", "changed value", "changed value", "changed value", "changed value", "changed value",
                            "changed value", "changed value", "changed value", "changed value", "changed value", "changed value", "changed value", "changed value")
    address.id = old_addresses[0].id
    app.address.modify_first_address(address)
    new_addresses = app.address.get_address_list()
    assert len(old_addresses) == len(new_addresses)
    old_addresses[0] = address
    assert sorted(old_addresses, key=Address.id_or_max) == sorted(new_addresses, key=Address.id_or_max)