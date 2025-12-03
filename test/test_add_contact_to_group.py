import random

from model.address import Address
from model.group import Group

def test_add_contact_to_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="firstname"))
    if len(db.get_contact_list()) == 0:
        app.address.create(Address(firstname = "firstname"))

    contact = random.choice(db.get_contact_list())
    group = random.choice(db.get_group_list())
    app.address.add_contact_to_group(contact.id, group.id)
    contacts_in_groups = db.get_contacts_in_group()

    assert any(
        row.id == contact.id and row.group_id == group.id
        for row in contacts_in_groups
    )