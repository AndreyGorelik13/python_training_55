from model.address import Address

def test_add_new_address(app):
    old_addresses = app.address.get_address_list()
    address = Address("firstname", "middlename", "lastname", "nickname", "title", "company", "address",
                        "home", "mobile", "work", "fax", "email", "email2", "email3", "homepage")
    app.address.create(address)
    new_addresses = app.address.get_address_list()
    assert len(old_addresses) + 1 == len(new_addresses)
    old_addresses.append(address)
    assert sorted(old_addresses, key=Address.id_or_max) == sorted(new_addresses, key=Address.id_or_max)


def test_add_empty_address(app):
    old_addresses = app.address.get_address_list()
    address = Address("", "", "", "", "", "", "",
                            "", "", "", "", "", "", "", "")
    app.address.create(address)
    new_addresses = app.address.get_address_list()
    assert len(old_addresses) + 1 == len(new_addresses)
    old_addresses.append(address)
    assert sorted(old_addresses, key=Address.id_or_max) == sorted(new_addresses, key=Address.id_or_max)