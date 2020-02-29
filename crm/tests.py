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
        driver.get('http://127.0.0.1:8000/admin')  # Admin page
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
        driver.get('http://127.0.0.1:8000/admin')  # Admin page
        elem = driver.find_element_by_id('id_username')
        elem.send_keys(USER)
        elem = driver.find_element_by_id('id_password')
        elem.send_keys(PWORD)
        elem.send_keys(Keys.RETURN)
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[1]/a').click()  # Add button
        time.sleep(2)
        #  Add Customer form \/
        elem = driver.find_element_by_id('id_cust_name')
        elem.send_keys('Ringo Barrett')
        elem = driver.find_element_by_id('id_organization')
        elem.send_keys('ISQA')
        elem = driver.find_element_by_id('id_role')
        elem.send_keys('Student')
        elem = driver.find_element_by_id('id_email')
        elem.send_keys('student\u0040example\u002Ecom')
        elem = driver.find_element_by_id('id_bldgroom')
        elem.send_keys('PKI 150')
        elem = driver.find_element_by_id('id_address')
        elem.send_keys('1110 S. 67th St.')
        elem = driver.find_element_by_id('id_account_number')
        elem.send_keys('103')
        elem = driver.find_element_by_id('id_city')
        elem.send_keys('Omaha')
        elem = driver.find_element_by_id('id_state')
        elem.send_keys('NE')
        elem = driver.find_element_by_id('id_zipcode')
        elem.send_keys('68132')
        elem = driver.find_element_by_id('id_phone_number')
        elem.send_keys('402-555-4567')
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/form/div/div/input[1]').click()  # Save button

        assert 'Saved'


class UserLoginLogoutTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()

    @skip
    def test_user_login(self):
        driver = self.driver

        driver.maximize_window()
        driver.get('http://127.0.0.1:8000')  # Home page
        driver.find_element_by_xpath('/html/body/nav/div/div[2]/ul[2]/li/a').click()  # Login button
        time.sleep(2)
        elem = driver.find_element_by_id('id_username')
        elem.send_keys(USER)
        elem = driver.find_element_by_id('id_password')
        elem.send_keys(PWORD)
        elem.send_keys(Keys.RETURN)

        assert 'Logged In'

    @skip
    def test_user_logout(self):
        driver = self.driver

        driver.maximize_window()
        driver.get('http://127.0.0.1:8000')  # Home page
        driver.find_element_by_xpath('/html/body/nav/div/div[2]/ul[2]/li/a').click()  # Login button
        time.sleep(2)
        elem = driver.find_element_by_id('id_username')
        elem.send_keys(USER)
        elem = driver.find_element_by_id('id_password')
        elem.send_keys(PWORD)
        elem.send_keys(Keys.RETURN)
        time.sleep(2)

        driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[2]/li/a").click()  # Logout button

        assert 'Logged Out'


class CustomersTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()

    @skip
    def test_customer_list(self):
        driver = self.driver

        driver.maximize_window()
        driver.get('http://127.0.0.1:8000')  # Home page
        driver.find_element_by_xpath('/html/body/nav/div/div[2]/ul[2]/li/a').click()  # Login button
        time.sleep(2)
        elem = driver.find_element_by_id('id_username')
        elem.send_keys(USER)
        elem = driver.find_element_by_id('id_password')
        elem.send_keys(PWORD)
        time.sleep(2)
        elem.send_keys(Keys.RETURN)
        time.sleep(2)

        driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/div/div/div[1]/div/div/p[2]/a').click()
        # ^ View details about Customers button
        time.sleep(2)

        assert 'View List'

    @skip
    def test_customer_edit(self):
        driver = self.driver

        driver.maximize_window()
        driver.get('http://127.0.0.1:8000')  # Home page
        driver.find_element_by_xpath('/html/body/nav/div/div[2]/ul[2]/li/a').click()  # Login button
        time.sleep(2)
        elem = driver.find_element_by_id('id_username')
        elem.send_keys(USER)
        elem = driver.find_element_by_id('id_password')
        elem.send_keys(PWORD)
        elem.send_keys(Keys.RETURN)
        time.sleep(2)

        driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/div/div/div[1]/div/div/p[2]/a').click()
        # ^ View details about Customers button
        time.sleep(2)

        driver.find_element_by_xpath('/html/body/div/div/div/div[3]/table/tbody/tr[1]/td[12]/a').click()  # Edit button
        elem = driver.find_element_by_id('id_cust_name')
        elem.send_keys(100 * Keys.BACKSPACE)
        elem.send_keys('George Selenium')
        elem = driver.find_element_by_id('id_email')
        elem.send_keys(100 * Keys.DELETE)
        elem.send_keys('selenium\u0040example\u002Ecom')
        elem.send_keys(Keys.RETURN)

        assert 'Update Successful'

    @skip
    def test_customer_delete(self):
        driver = self.driver

        driver.maximize_window()
        driver.get('http://127.0.0.1:8000')  # Home page
        driver.find_element_by_xpath('/html/body/nav/div/div[2]/ul[2]/li/a').click()  # Login button
        time.sleep(2)
        elem = driver.find_element_by_id('id_username')
        elem.send_keys(USER)
        elem = driver.find_element_by_id('id_password')
        elem.send_keys(PWORD)
        elem.send_keys(Keys.RETURN)
        time.sleep(2)

        driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/div/div/div[1]/div/div/p[2]/a').click()
        # ^ View details about Customers button
        time.sleep(2)

        driver.find_element_by_xpath('/html/body/div/div/div/div[3]/table/tbody/tr[2]/td[13]/a').click()  # Delete button
        time.sleep(2)
        obj = driver.switch_to.alert
        obj.accept()
        time.sleep(2)

        assert 'Customer Deleted'

    @skip
    def test_customer_summary(self):
        driver = self.driver

        driver.maximize_window()
        driver.get('http://127.0.0.1:8000')  # Home page
        driver.find_element_by_xpath('/html/body/nav/div/div[2]/ul[2]/li/a').click()  # Login button
        time.sleep(2)
        elem = driver.find_element_by_id('id_username')
        elem.send_keys(USER)
        elem = driver.find_element_by_id('id_password')
        elem.send_keys(PWORD)
        elem.send_keys(Keys.RETURN)
        time.sleep(2)

        driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/div/div/div[1]/div/div/p[2]/a').click()
        # ^ View details about Customers button
        time.sleep(2)

        driver.find_element_by_xpath('/html/body/div/div/div/div[3]/table/tbody/tr[1]/td[14]/a').click()  # Summary button
        time.sleep(5)

        assert 'Customer Summary'


class ServicesTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()

    @skip
    def test_service_list(self):
        driver = self.driver

        driver.maximize_window()
        driver.get('http://127.0.0.1:8000')  # Home page
        driver.find_element_by_xpath('/html/body/nav/div/div[2]/ul[2]/li/a').click()  # Login button
        time.sleep(2)
        elem = driver.find_element_by_id('id_username')
        elem.send_keys(USER)
        elem = driver.find_element_by_id('id_password')
        elem.send_keys(PWORD)
        time.sleep(2)
        elem.send_keys(Keys.RETURN)
        time.sleep(2)

        driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/div/div/div[2]/div/div/p[2]/a').click()
        # ^ View details about Services button
        time.sleep(2)

        assert 'View List'

    @skip
    def test_service_edit(self):
        driver = self.driver

        driver.maximize_window()
        driver.get('http://127.0.0.1:8000')  # Home page
        driver.find_element_by_xpath('/html/body/nav/div/div[2]/ul[2]/li/a').click()  # Login button
        time.sleep(2)
        elem = driver.find_element_by_id('id_username')
        elem.send_keys(USER)
        elem = driver.find_element_by_id('id_password')
        elem.send_keys(PWORD)
        elem.send_keys(Keys.RETURN)
        time.sleep(2)

        driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/div/div/div[2]/div/div/p[2]/a').click()
        # ^ View details about Services button
        time.sleep(2)

        driver.find_element_by_xpath('/html/body/div/div/div/div[3]/table/tbody/tr[2]/td[8]/a').click()  # Edit button
        elem = driver.find_element_by_id('id_serice_category')
        elem.send_keys(100 * Keys.BACKSPACE)
        elem.send_keys('Catering Service')
        elem = driver.find_element_by_id('id_location')
        elem.send_keys(100 * Keys.DELETE)
        elem.send_keys('Peter Kiewit Institute')
        elem.send_keys(Keys.RETURN)

        assert 'Update Successful'

    @skip
    def test_service_delete(self):
        driver = self.driver

        driver.maximize_window()
        driver.get('http://127.0.0.1:8000')  # Home page
        driver.find_element_by_xpath('/html/body/nav/div/div[2]/ul[2]/li/a').click()  # Login button
        time.sleep(2)
        elem = driver.find_element_by_id('id_username')
        elem.send_keys(USER)
        elem = driver.find_element_by_id('id_password')
        elem.send_keys(PWORD)
        elem.send_keys(Keys.RETURN)
        time.sleep(2)

        driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/div/div/div[2]/div/div/p[2]/a').click()
        # ^ View details about Services button
        time.sleep(2)

        driver.find_element_by_xpath('/html/body/div/div/div/div[3]/table/tbody/tr[2]/td[9]/a').click()  # Delete button
        time.sleep(2)
        obj = driver.switch_to.alert
        obj.accept()
        time.sleep(2)

        assert 'Service Deleted'

    @skip
    def test_service_add(self):
        driver = self.driver

        driver.maximize_window()
        driver.get('http://127.0.0.1:8000')  # Home page
        driver.find_element_by_xpath('/html/body/nav/div/div[2]/ul[2]/li/a').click()  # Login button
        time.sleep(2)
        elem = driver.find_element_by_id('id_username')
        elem.send_keys(USER)
        elem = driver.find_element_by_id('id_password')
        elem.send_keys(PWORD)
        elem.send_keys(Keys.RETURN)
        time.sleep(2)

        driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/div/div/div[2]/div/div/p[2]/a').click()
        # ^ View details about Services button
        time.sleep(2)

        driver.find_element_by_xpath('/html/body/div/div/div/div[3]/div/a/span').click()  # Add Service button
        time.sleep(2)
        #  Add Customer form \/
        self.driver.find_element_by_css_selector('#id_cust_name > option:nth-child(2)').click()
        elem = driver.find_element_by_id('id_service_category')
        elem.send_keys('Catering')
        elem = driver.find_element_by_id('id_description')
        elem.send_keys('Catering service for UNO')
        elem = driver.find_element_by_id('id_location')
        elem.send_keys('Mammel Hall')
        elem = driver.find_element_by_id('id_service_charge')
        elem.send_keys('250\u002E00')
        elem.send_keys(Keys.RETURN)
        time.sleep(2)

        assert 'Service Added'


if __name__ == '__main__':
    unittest.main()
