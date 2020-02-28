# from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from unittest import skip
import time

USER = 'instructor'
PWORD = 'maverick1a'


class AdminTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()

    @skip
    def test_admin_login(self):
        driver = self.driver

        driver.maximize_window()
        driver.get('http://127.0.0.1:8000/admin')

        elem = driver.find_element_by_id('id_username')
        elem.send_keys(USER)
        elem = driver.find_element_by_id('id_password')
        elem.send_keys(PWORD)
        elem.send_keys(Keys.RETURN)
        assert 'Logged In'

    @skip
    def test_add_customer(self):
        driver = self.driver

        driver.maximize_window()
        driver.get('http://127.0.0.1:8000/admin')

        elem = driver.find_element_by_id('id_username')
        elem.send_keys(USER)
        elem = driver.find_element_by_id('id_password')
        elem.send_keys(PWORD)
        elem.send_keys(Keys.RETURN)
        time.sleep(5)
        driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[1]/a').click()
        time.sleep(5)

        elem = driver.find_element_by_id('id_cust_name')
        elem.send_keys('Test User')
        elem = driver.find_element_by_id('id_organization')
        elem.send_keys('ISQA')
        elem = driver.find_element_by_id('id_role')
        elem.send_keys('Staff Assistant')
        elem = driver.find_element_by_id('id_email')
        elem.send_keys('test@example.com')
        elem = driver.find_element_by_id('id_bldgroom')
        elem.send_keys('PKI 150')
        elem = driver.find_element_by_id('id_address')
        elem.send_keys('1110 S. 67th St.')
        elem = driver.find_element_by_id('id_account_number')
        elem.send_keys('101')
        elem = driver.find_element_by_id('id_city')
        elem.send_keys('Omaha')
        elem = driver.find_element_by_id('id_state')
        elem.send_keys('NE')
        elem = driver.find_element_by_id('id_zipcode')
        elem.send_keys('68132')
        elem = driver.find_element_by_id('id_phone_number')
        elem.send_keys('402-555-4567')

        time.sleep(5)
        driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/form/div/div/input[1]').click()

        assert 'Saved'


class UserLoginLogoutTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()

    def test_user_login(self):
        driver = self.driver

        driver.maximize_window()
        driver.get('http://127.0.0.1:8000')
        driver.find_element_by_xpath('/html/body/nav/div/div[2]/ul[2]/li/a').click()
        time.sleep(5)

        elem = driver.find_element_by_id('id_username')
        elem.send_keys(USER)
        elem = driver.find_element_by_id('id_password')
        elem.send_keys(PWORD)
        elem.send_keys(Keys.RETURN)

        assert 'Logged In'
        
    def test_user_logout(self):
        driver = self.driver

        driver.maximize_window()
        driver.get('http://127.0.0.1:8000')
        driver.find_element_by_xpath('/html/body/nav/div/div[2]/ul[2]/li/a').click()
        time.sleep(5)

        elem = driver.find_element_by_id('id_username')
        elem.send_keys(USER)
        elem = driver.find_element_by_id('id_password')
        elem.send_keys(PWORD)
        elem.send_keys(Keys.RETURN)
        time.sleep(5)

        driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[2]/li/a").click()

        assert 'Logged Out'


if __name__ == '__main__':
    unittest.main()
