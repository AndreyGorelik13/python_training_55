import re
from operator import index

from selenium.webdriver.common.by import By

from model.address import Address


class AddressHelper:

    def __init__(self, app):
        self.app = app

    def create(self, address):
        wd = self.app.wd
        self.open_address_page()
        self.click_add_address_button()
        # fill address firm
        self.fill_address_firm(address)
        # submit address creation
        wd.find_element(By.NAME, "submit").click()
        self.return_to_home_page()
        self.address_cache = None

    def fill_address_firm(self, address):
        wd = self.app.wd
        self.filling_address_field_value("firstname", address.firstname)
        self.filling_address_field_value("middlename", address.middlename)
        self.filling_address_field_value("lastname", address.lastname)
        self.filling_address_field_value("nickname", address.nickname)
        self.filling_address_field_value("title", address.title)
        self.filling_address_field_value("company", address.company)
        self.filling_address_field_value("address", address.address)
        self.filling_address_field_value("home", address.home)
        self.filling_address_field_value("mobile", address.mobile)
        self.filling_address_field_value("work", address.work)
        self.filling_address_field_value("fax", address.fax)
        self.filling_address_field_value("email", address.email)
        self.filling_address_field_value("email2", address.email2)
        self.filling_address_field_value("email3", address.email3)
        self.filling_address_field_value("homepage", address.homepage)

    def filling_address_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    def delete_first_address(self):
        self.delete_address_by_index(0)

    def delete_address_by_index(self, index):
        wd = self.app.wd
        self.open_address_page()
        self.select_address_by_index(index)
        # submit deletion
        wd.find_element(By.NAME, "delete").click()
        self.return_to_home_page()
        self.address_cache = None

    def delete_address_by_id(self, id):
        wd = self.app.wd
        self.open_address_page()
        self.select_address_by_id(id)
        # submit deletion
        wd.find_element(By.NAME, "delete").click()
        self.return_to_home_page()
        self.address_cache = None

    def select_address_by_index(self, index):
        wd = self.app.wd
        wd.find_elements(By.NAME, "selected[]")[index].click()

    def select_address_by_id(self, id):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, "input[value='%s']" % id).click()

    def modify_first_address(self, address):
        self.modify_address_by_index(0, address)

    def modify_address_by_index(self, index, address):
        wd = self.app.wd
        self.open_address_page()
        #self.select_address_by_index(index)
        self.init_address_edition_by_index(index)
        # fill address firm
        self.fill_address_firm(address)
        # submit address edition
        wd.find_element(By.NAME, "update").click()
        self.return_to_home_page()
        self.address_cache = None

    def modify_address_by_id(self, contact):
        wd = self.app.wd
        self.open_address_page()
        self.init_address_edition_by_id(contact.id)
        self.fill_address_firm(contact)
        # submit address edition
        wd.find_element(By.NAME, "update").click()
        self.return_to_home_page()
        self.address_cache = None

    def init_address_edition_by_index(self, index):
        wd = self.app.wd
        self.open_address_page()
        wd.find_elements(By.XPATH, "(//img[@title='Edit'])")[index].click()

    def init_address_edition_by_id(self, id):
        wd = self.app.wd
        self.open_address_page()
        wd.find_element(By.CSS_SELECTOR, "a[href='edit.php?id=%s']" % id).click()

    def open_address_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php") and len(wd.find_elements(By.XPATH, "//input[@value='Send e-Mail']")) > 0):
           wd.find_element(By.XPATH, "//a[normalize-space()='home']").click()

    def click_add_address_button(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "add new").click()

    def return_to_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php") and len(wd.find_elements(By.XPATH, "//input[@value='Send e-Mail']")) > 0):
            wd.find_element(By.LINK_TEXT, "home page").click()

    def count(self):
        wd = self.app.wd
        self.open_address_page()
        return len(wd.find_elements(By.NAME, "selected[]"))

    address_cache = None

    def get_address_list(self):
        if self.address_cache is None:
            wd = self.app.wd
            self.open_address_page()
            self.address_cache = []
            for element in (wd.find_elements(By.XPATH, "(//tr[@name='entry'])")):
                cells = element.find_elements(By.TAG_NAME, "td")
                id = element.find_element(By.NAME, "selected[]").get_attribute("value")
                last_name = cells[1].text
                first_name = cells[2].text
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.address_cache.append(Address(id=id, firstname=first_name, lastname=last_name, address=address, all_phones_from_home_page = all_phones, all_emails_from_home_page = all_emails))
        return list(self.address_cache)

    def open_address_view_by_index(self, index):
        wd = self.app.wd
        self.open_address_page()
        row = wd.find_elements(By.NAME, "entry")[index]
        cell = row.find_elements(By.TAG_NAME, "td")[6]
        cell.find_element(By.TAG_NAME, "a").click()

    def get_address_info_from_edit_page(self, index):
        wd = self.app.wd
        self.init_address_edition_by_index(index)
        firstname = wd.find_element(By.NAME, "firstname").get_attribute("value")
        lastname = wd.find_element(By.NAME, "lastname").get_attribute("value")
        id = wd.find_element(By.NAME, "id").get_attribute("value")
        home = wd.find_element(By.NAME, "home").get_attribute("value")
        work = wd.find_element(By.NAME, "work").get_attribute("value")
        mobile = wd.find_element(By.NAME, "mobile").get_attribute("value")
        fax = wd.find_element(By.NAME, "fax").get_attribute("value")
        address = wd.find_element(By.NAME, "address").get_attribute("value")
        email = wd.find_element(By.NAME, "email").get_attribute("value")
        email2 = wd.find_element(By.NAME, "email2").get_attribute("value")
        email3 = wd.find_element(By.NAME, "email3").get_attribute("value")
        return Address (firstname=firstname, lastname=lastname, id=id, home=home, mobile=mobile, work=work, fax=fax, address=address, email=email, email2=email2, email3=email3)

    def get_address_from_view_page(self, index):
        wd = self.app.wd
        self.open_address_view_by_index(index)
        text = wd.find_element(By.ID, "content").text
        home = re.search("H: (.*)", text).group(1)
        work = re.search("W: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        fax = re.search("F: (.*)", text).group(1)
        return Address(home=home, work=work, mobile=mobile, fax=fax)