import random
import string

import pytest

from model.address import Address

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Address("", "", "", "", "", "", "",
                        "", "", "", "", "", "", "", "")] + [
    Address(firstname= random_string("firstname", 10), middlename= random_string("middlename", 10), lastname= random_string("lastname", 10),
            nickname= random_string("nickname", 10), title= random_string("title", 10), company= random_string("company", 10),
            address= random_string("address", 10), home= random_string("home", 10), mobile= random_string("mobile", 10),
            work= random_string("work", 10), fax= random_string("fax", 10), email= random_string("email", 10),
            email2= random_string("email2", 10), email3= random_string("email3", 10), homepage= random_string("homepage", 10))
    for i in range(5)
]

@pytest.mark.parametrize("address", testdata, ids=[repr(x) for x in testdata])
def test_add_new_address(app, address):
    old_addresses = app.address.get_address_list()
    app.address.create(address)
    assert len(old_addresses) + 1 == app.address.count()
    new_addresses = app.address.get_address_list()
    old_addresses.append(address)
    assert sorted(old_addresses, key=Address.id_or_max) == sorted(new_addresses, key=Address.id_or_max)


#def test_add_empty_address(app):
#    old_addresses = app.address.get_address_list()
#    address = Address("", "", "", "", "", "", "",
#                            "", "", "", "", "", "", "", "")
#    app.address.create(address)
#    new_addresses = app.address.get_address_list()
#    assert len(old_addresses) + 1 == len(new_addresses)
#    old_addresses.append(address)
#    assert sorted(old_addresses, key=Address.id_or_max) == sorted(new_addresses, key=Address.id_or_max)