import random

from model.address import Address

def test_modify_some_address(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.address.create(Address(firstname = "firstname"))
    old_addresses = db.get_contact_list()
    contact = random.choice(old_addresses)
    contact.firstname = Address(firstname="changed value").firstname
    app.address.modify_address_by_id(contact)
    new_addresses = db.get_contact_list()
    assert len(old_addresses) == len(new_addresses)
    if check_ui:
        assert sorted(old_addresses, key=Address.id_or_max) == sorted(app.address.get_address_list(), key=Address.id_or_max)