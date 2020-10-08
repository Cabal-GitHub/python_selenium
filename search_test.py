import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.common.by import By

class SearchTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = './chromedriver')
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()
        driver.implicitly_wait(15)

    def test_search_tee(self):
        driver=self.driver
        search_field = driver.find_element_by_name('q')
        search_field.clear()
        
        search_field.send_keys('tee') #enviamos la palabra como si fuera el humano
        search_field.submit()

    def test_search_salt_shaker(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')

        search_field.send_keys('salt shaker') #enviamos la palabra como si fuera el teclado
        search_field.submit()
#la lista rapida para obtener los elemtentos es por su XPATH
        products = driver.find_elements_by_xpath('//*[@id="top"]/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li/div/h2/a')
        self.assertEqual(1, len(products)) #si la cantidad de productos es 1 o no
    def tearDown(self):
        self.driver.quit()
    
if __name__ == "__main__":
    unittest.main(verbosity = 2)