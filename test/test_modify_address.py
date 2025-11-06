from random import randrange

from model.address import Address

def test_modify_some_address(app):
    if app.address.count() == 0:
        app.address.create(Address(firstname = "firstname"))
    old_addresses = app.address.get_address_list()
    index = randrange(len(old_addresses))
    address = Address("changed value", "changed value", "changed value", "changed value", "changed value", "changed value", "changed value",
                            "changed value", "changed value", "changed value", "changed value", "changed value", "changed value", "changed value", "changed value")
    address.id = old_addresses[index].id
    app.address.modify_address_by_index(index, address)
    new_addresses = app.address.get_address_list()
    assert len(old_addresses) == len(new_addresses)
    old_addresses[index] = address
    assert sorted(old_addresses, key=Address.id_or_max) == sorted(new_addresses, key=Address.id_or_max)