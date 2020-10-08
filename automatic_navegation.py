import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.support.ui import Select #para porder seleccionar en lo select
from time import sleep #para esperar hasta ejecutar la siguiente accion


class NavegationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = './chromedriver')
        driver = self.driver
        driver.get("https://www.google.com/")
        driver.maximize_window()
        driver.implicitly_wait(30)

    def test_browser_navegation(self):
        driver = self.driver

        #buscar el elemento para agregarle la palabra a buscar y luego presionr en submit
        search_field = driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys('platzi')
        search_field.submit()

        #retrocede
        driver.back()
        sleep(3)
        #avanza
        driver.forward()
        sleep(3)
        #refresca
        driver.refresh()
        sleep(3)
        


    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.quit()
    
if __name__ == "__main__":
    unittest.main(verbosity = 2)
