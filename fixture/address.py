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

    def select_address_by_index(self, index):
        wd = self.app.wd
        wd.find_elements(By.NAME, "selected[]")[index].click()

    def modify_first_address(self, address):
        self.modify_address_by_index(0, address)

    def modify_address_by_index(self, index, address):
        wd = self.app.wd
        self.open_address_page()
        self.select_address_by_index(index)
        # init address edition
        wd.find_element(By.XPATH, "(//img[@title='Edit'])[1]").click()
        # fill address firm
        self.fill_address_firm(address)
        # submit address edition
        wd.find_element(By.NAME, "update").click()
        self.return_to_home_page()
        self.address_cache = None

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
                id = element.find_element(By.NAME, "selected[]").get_attribute("value")
                first_name = element.find_element(By.CSS_SELECTOR, "td:nth-child(3)").text
                last_name = element.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text
                self.address_cache.append(Address(id=id, firstname=first_name, lastname=last_name))
        return list(self.address_cache)