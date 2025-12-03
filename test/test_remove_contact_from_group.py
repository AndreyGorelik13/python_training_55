import random

from model.address import Address
from model.group import Group

def test_remove_contact_from_group(app, db):
    if len(db.get_contacts_in_group()) ==0:
        if len(db.get_group_list()) == 0:
            app.group.create(Group(name="firstname"))
        if len(db.get_contact_list()) == 0:
            app.address.create(Address(firstname = "firstname"))
        app.address.add_contact_to_group(random.choice(db.get_contact_list()).id, random.choice(db.get_group_list()).id)

    contact = random.choice(db.get_contacts_in_group())
    app.address.remove_contact_from_group(contact.id, contact.group_id)
    contacts_in_groups = db.get_contacts_in_group()

    assert not any(
        row.id == contact.id and row.group_id == contact.group_id
        for row in contacts_in_groups
    )