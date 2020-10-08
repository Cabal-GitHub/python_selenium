import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.common.by import By

class RegisterNewUser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = './chromedriver')
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()
        driver.implicitly_wait(30)

    def test_new_user(self):
        driver = self.driver
        #busque el elemento y le de click
        driver.find_element_by_xpath('//*[@id="header"]/div/div[2]/div/a/span[2]').click()
        #busque el texto de register y le de click
        driver.find_element_by_link_text('Log In').click()
        #nos llevara a una pantalla nueva de login y buscaremos el botón de crear una cuenta nueva
        
        create_account_button = driver.find_element_by_xpath('//*[@id="login-form"]/div/div[1]/div[2]/a/span/span')
        #luego validadmos que ese boton esté esté visible para el usuario y habilitado
        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
        create_account_button.click()
        #validamos que el título de mi página para registrar cliente es el mismo que el navegador muestra
        self.assertEqual('Create New Customer Account', driver.title)

        #creamos las variables con el selector correspondiente a cada campo del registro
        first_name = driver.find_element_by_id('firstname')
        middle_name = driver.find_element_by_id('middlename')
        last_name = driver.find_element_by_id('lastname')
        email_address = driver.find_element_by_id('email_address')
        news_letter_subscription = driver.find_element_by_id('is_subscribed')
        pasword = driver.find_element_by_id('password')
        confirm_password = driver.find_element_by_id('confirmation')
        submit_button = driver.find_element_by_xpath('//*[@id="form-validate"]/div[1]/ul/li[4]/label')
        
        #validamos si los textbox y  botones están activos
        self.assertTrue(first_name.is_enabled()
        and middle_name.is_enabled()
        and last_name.is_enabled()
        and email_address.is_enabled()
        and news_letter_subscription.is_enabled()
        and confirm_password.is_enabled()
        and submit_button.is_enabled()
        )

        #agregamos valores a los campos
        first_name.send_keys('ijcm')
        driver.implicitly_wait(1)
        middle_name.send_keys('ijcm')
        driver.implicitly_wait(1)
        last_name.send_keys('kbal')
        driver.implicitly_wait(1)
        email_address.send_keys('kbal@kbal.com')
        driver.implicitly_wait(1)
        pasword.send_keys('kbal123')
        driver.implicitly_wait(1)
        confirm_password.send_keys('kbal123')
        driver.implicitly_wait(1)
        submit_button.click()

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.quit()
    
if __name__ == "__main__":
    unittest.main(verbosity = 2)