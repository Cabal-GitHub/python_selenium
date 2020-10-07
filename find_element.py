import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HomePageTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = './chromedriver')
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()
        driver.implicitly_wait(15)

    def test_search_text_field(self):
        search_field = self.driver.find_element_by_id("search")

    def test_search_text_field_by_name(self):
        search_field = self.driver.find_element_by_name("q")

    def test_search_text_field_class_name(self):
        search_field = self.driver.find_element_by_class_name("input-text")
        
    def test_search_text_button_enable(self):
        button = self.driver.find_element_by_class_name("button")

#muestra la cantidad de imagenes que hay dentro de una clase div
    def test_count_of_promo_banner_images(self):
        banner_list = self.driver.find_element_by_class_name("promos")
        banners = banner_list.find_elements_by_tag_name('img') #al ser varios debe tener la S en elements
        self.assertEqual(3, len(banners))

    #cuando no son elementos bien definidos sin selectores, se copia el Xpath
    def test_vip_promo(self):
        vip_promo = self.driver.find_element_by_xpath('//*[@id="top"]/body/div[1]/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[3]/a/img')

    #identificar al elemento por su selector de css
    def test_seletor_css (self):
        select_css = self.driver.find_elements_by_css_selector("div.header-minicart span.icon")

    def tearDown(self):
        self.driver.quit()
    
if __name__ == "__main__":
    unittest.main(verbosity = 2)