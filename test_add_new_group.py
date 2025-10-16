import unittest

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class TestAddNewGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
    
    def test_add_new_group(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/index.php")
        wd.find_element(By.NAME,"user").clear()
        wd.find_element(By.NAME,"user").send_keys("admin")
        wd.find_element(By.NAME,"pass").clear()
        wd.find_element(By.NAME,"pass").send_keys("secret")
        wd.find_element(By.ID,"LoginForm").submit()
        wd.find_element(By.LINK_TEXT,"groups").click()
        wd.find_element(By.NAME,"new").click()
        wd.find_element(By.NAME,"group_name").click()
        wd.find_element(By.NAME,"group_name").clear()
        wd.find_element(By.NAME,"group_name").send_keys("new_test")
        wd.find_element(By.NAME,"group_header").clear()
        wd.find_element(By.NAME,"group_header").send_keys("new_test")
        wd.find_element(By.NAME,"group_footer").click()
        wd.find_element(By.NAME,"group_footer").clear()
        wd.find_element(By.NAME,"group_footer").send_keys("new_test")
        wd.find_element(By.NAME,"submit").click()
        wd.find_element(By.LINK_TEXT,"group page").click()
        wd.find_element(By.LINK_TEXT,"Logout").click()
    
    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
