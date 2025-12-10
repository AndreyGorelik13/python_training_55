import mysql.connector

from model.address import Address
from model.group import Group


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host=host
        self.name=name
        self.user=user
        self.password=password
        self.connection= mysql.connector.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list
    def destroy(self):
        self.connection.close()


    def get_contacts_in_group(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "select id, group_id from address_in_groups")
            for row in cursor:
                (id, group_id) = row
                list.append(Address(id=str(id), group_id=str(group_id)))
        finally:
            cursor.close()
        return list
    def destroy(self):
        self.connection.close()

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, home, mobile, work, email, email2, email3 from addressbook")
            for row in cursor:
                (id, firstname, lastname, address, home, mobile, work, email, email2, email3) = row
                list.append(Address(id=str(id), firstname=firstname, lastname=lastname, address=address, home=home, mobile=mobile, work=work, email=email, email2=email2, email3=email3))
        finally:
            cursor.close()
        return list
    def destroy(self):
        self.connection.close()

    def get_contact_not_in_group(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT ab.id, firstname, lastname, address, home, mobile, work, email, email2, email3 FROM addressbook ab LEFT JOIN address_in_groups ag ON ab.id = ag.id WHERE ag.id IS NULL")
            for row in cursor:
                (id, firstname, lastname, address, home, mobile, work, email, email2, email3) = row
                list.append(Address(id=str(id), firstname=firstname, lastname=lastname, address=address, home=home, mobile=mobile, work=work, email=email, email2=email2, email3=email3))
        finally:
            cursor.close()
        return list
    def destroy(self):
        self.connection.close()