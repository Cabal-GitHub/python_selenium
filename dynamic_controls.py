import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait #para espera explicitas
from time import sleep #para esperar hasta ejecutar la siguiente accion
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class DynamicControlsTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = './chromedriver')
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com/")
        driver.find_element_by_link_text('Dynamic Controls').click()
        sleep(3)



    def test_dynamic_controls(self):
        driver = self.driver
        # check_box = driver.find_element_by_xpath('//*[@id="checkbox"]/input')
        # check_box.click()
        # remove_add_button = driver.find_element_by_xpath('//*[@id="checkbox-example"]/button')
        # remove_add_button.click()
        # #hacemo un pausa de 15 segundos
        # #cuando la pausa terminar, vemos si está el elemento clicleable, en ete caso sería
        # #que aparezca nuevamente e botón de remove/add
        # WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="checkbox-example"]/button')))
        # remove_add_button.click()

        enable_disable_button = driver.find_element_by_xpath('//*[@id="input-example"]/button')
        enable_disable_button.click()
        
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input-example"]/input')))
        #self.assertTrue(text_insert.is_enabled)
        
        text_insert = driver.find_element_by_xpath('//*[@id="input-example"]/input')

        text_insert.send_keys('Hola mundo')
        enable_disable_button.click()
        sleep(5)
        

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.quit()
    
if __name__ == "__main__":
    unittest.main(verbosity = 2)