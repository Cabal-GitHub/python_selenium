import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.common.by import By

class RegisterNewUser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = './chromedriver')
        driver = self.driver
        driver.get("http://10.92.57.48:44380/wfc_ui/faces/application/workspace/Welcome.jsp")
        driver.maximize_window()
        driver.implicitly_wait(30)

    def test_new_user(self):
        driver = self.driver

        #creamos las variables con el selector correspondiente a cada campo del registro
        user_name = driver.find_element_by_id('j_username')
        password = driver.find_element_by_id('j_password')
        submit_button = driver.find_element_by_class_name('loginbutton')
        
        #validamos si los textbox y  botones están activos
        self.assertTrue(user_name.is_enabled()
        and password.is_enabled()
        and submit_button.is_enabled()
        )

        #agregamos valores a los campos
        user_name.send_keys('cti22541')
        driver.implicitly_wait(1)
        password.send_keys('Septi2021')
        driver.implicitly_wait(1)
        submit_button.click()

        driver.find_element_by_id('mainForm:header_gen_links_view:Logout').click()
        driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.quit()
    
if __name__ == "__main__":
    unittest.main(verbosity = 2)