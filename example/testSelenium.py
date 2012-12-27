#! /usr/bin/python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
import keyring

USERNAME = 'mistewart@expedia.com.dharma'
PASSWORD = keyring.get_password('GSO_Dharma', USERNAME)

class TestSelenium(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.remote.webdriver.WebDriver('http://127.0.0.1:4444/wd/hub',{"browserName": 'firefox'})
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.yahoo.com"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_selenium(self):
        driver = self.driver
        driver.get("http://test.salesforce.com")
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(USERNAME)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(PASSWORD)
        driver.find_element_by_id("Login").click()
        driver.find_element_by_link_text("Cases").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert.text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
