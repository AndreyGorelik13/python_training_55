from random import randrange

from model.address import Address

def test_delete_some_address(app):
    if app.address.count() == 0:
        app.address.create(Address(firstname = "firstname"))
    old_addresses = app.address.get_address_list()
    index = randrange(len(old_addresses))
    app.address.delete_address_by_index(index)
    new_addresses = app.address.get_address_list()
    assert len(old_addresses) - 1 == len(new_addresses)
    old_addresses[index:index + 1] = []
    assert old_addresses == new_addresses