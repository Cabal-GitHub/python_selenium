import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.support.ui import Select #para porder seleccionar en lo select
from time import sleep #para esperar hasta ejecutar la siguiente accion


class DynamicTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = './chromedriver')
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com/")
        driver.find_element_by_link_text('Disappearing Elements').click()



    def test_dynaminc(self):
        driver = self.driver
        #creamos una variable que tendra la lista del total de variables que tenemos
        options = []
        menu = 5
        tries = 1

        while len(options) < 5:
            options.clear()

            for i in range(menu):
                try:
                    options_name = driver.find_element_by_xpath(f'//*[@id="content"]/div/ul/li[{i + 1}]/a')
                    options.append(options_name.text)
                    print(options)
                except:
                    print(f'Option number {i+1} NOT found')
                    tries + 1
                    driver.refresh()
    
        print(f'Finished in {tries} tries')





    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.quit()
    
if __name__ == "__main__":
    unittest.main(verbosity = 2)