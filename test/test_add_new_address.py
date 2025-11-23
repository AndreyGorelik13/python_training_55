from model.address import Address


def test_add_new_address(app, json_contacts):
    address = json_contacts
    old_addresses = app.address.get_address_list()
    app.address.create(address)
    assert len(old_addresses) + 1 == app.address.count()
    new_addresses = app.address.get_address_list()
    old_addresses.append(address)
    assert sorted(old_addresses, key=Address.id_or_max) == sorted(new_addresses, key=Address.id_or_max)