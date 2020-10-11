import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.support.ui import Select #para porder seleccionar en lo select
from time import sleep #para esperar hasta ejecutar la siguiente accion


class AddRemoveElementTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = './chromedriver')
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com/")
        driver.find_element_by_link_text('Add/Remove Elements').click()



    def test_add_remove(self):
        driver = self.driver

        elements_added =  int(input('How many elements will you add?'))
        elements_removed = int(input('How mnay elments will you remove?'))
        total_elements = elements_added - elements_removed

        add_button = driver.find_element_by_xpath('//*[@id="content"]/div/button')

        sleep(3) #para que se detenga 3 segundos

        for i in range(elements_added):
            add_button.click()

        for i in range(elements_removed):
            try:
                delete_button = driver.find_element_by_xpath('//*[@id="elements"]/button')
                delete_button.click()
            except:
                print("You're trying to delete  more elements the existent")
                break
    
    #vamos a mostrar en consola lo que intento hacer
        if total_elements > 0:
            print(f"There are {total_elements} elements")
        else:
            print("There 0 are elements")
        
        sleep(3)


    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.quit()
    
if __name__ == "__main__":
    unittest.main(verbosity = 2)