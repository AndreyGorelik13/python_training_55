from selenium.webdriver.common.by import By

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
        wd.find_element(By.NAME, field_name).click()
        wd.find_element(By.NAME, field_name).clear()
        wd.find_element(By.NAME, field_name).send_keys(text)

    def delete_first_address(self):
        wd = self.app.wd
        self.open_address_page()
        # select first address
        wd.find_element(By.NAME, "selected[]").click()
        # submit deletion
        wd.find_element(By.NAME, "delete").click()
        self.return_to_home_page()

    def modify_first_address(self, address):
        wd = self.app.wd
        self.open_address_page()
        # select first address
        wd.find_element(By.NAME, "selected[]").click()
        # init address edition
        wd.find_element(By.XPATH, "(//img[@title='Edit'])[1]").click()
        # fill address firm
        self.fill_address_firm(address)
        # submit address edition
        wd.find_element(By.NAME, "update").click()
        self.return_to_home_page()

    def open_address_page(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//a[normalize-space()='home']").click()

    def click_add_address_button(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "add new").click()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "home page").click()