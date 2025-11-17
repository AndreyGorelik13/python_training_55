import re
from random import randrange



def test_phones_on_home_page(app):
    index = randrange(len(app.address.get_address_list()))
    contact_from_home_page = app.address.get_address_list()[index]
    contact_from_edit_page = app.address.get_address_info_from_edit_page(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_home_page(contact_from_edit_page)

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None, [contact.home, contact.mobile, contact.work]))))

def merge_emails_like_home_page(contact):
    return "\n".join(filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3]))