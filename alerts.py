import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.support.ui import Select #para porder seleccionar en lo select


class CompareProducts(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = './chromedriver')
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()
        driver.implicitly_wait(30)

    def test_compare_products_renoval_alert(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        search_field.clear()
        
        search_field.send_keys('tee')
        search_field.submit()

        driver.find_element_by_class_name('link-compare').click()
        driver.find_element_by_link_text('Clear All').click()

        #le vamos a pedir que desvie el foco a la alerta
        alert = driver.switch_to_alert()
        alert_text = alert.text

        #verificamos si el texto del alert es igual al que estamos buscando
        self.assertEqual('Are you sure you would like to remove all products from your comparison?', alert_text)
        #simulamos un aceptar en caso de ser el mensaje declarado anteriormete
        alert.accept()
        


    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.quit()
    
if __name__ == "__main__":
    unittest.main(verbosity = 2)
