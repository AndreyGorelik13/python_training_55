from model.address import Address

def test_add_new_address(app, db, json_contacts):
    address = json_contacts
    old_addresses = db.get_contact_list()
    app.address.create(address)
    new_addresses = db.get_contact_list()
    old_addresses.append(address)
    assert sorted(old_addresses, key=Address.id_or_max) == sorted(new_addresses, key=Address.id_or_max)