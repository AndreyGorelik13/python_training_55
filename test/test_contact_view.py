import re



def test_phones_on_home_page(app, db):
    contacts_from_home_page = sorted(app.address.get_address_list(), key=lambda x: x.id)
    contacts_from_db = sorted(db.get_contact_list(), key=lambda x: x.id)

    for i in range(len(contacts_from_home_page)):
        home_contact = contacts_from_home_page[i]
        db_contact = contacts_from_db[i]
        assert home_contact.firstname == db_contact.firstname
        assert home_contact.lastname == db_contact.lastname
        assert home_contact.address == db_contact.address
        assert home_contact.all_phones_from_home_page == merge_phones_like_home_page(db_contact)
        assert home_contact.all_emails_from_home_page == merge_emails_like_home_page(db_contact)

def clear(s):
    return re.sub("[() -]", "", s) if s else ""

def merge_phones_like_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None, [contact.home, contact.mobile, contact.work]))))

def merge_emails_like_home_page(contact):
    return "\n".join(filter(None, [contact.email, contact.email2, contact.email3]))