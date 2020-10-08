import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.support.ui import Select #para porder seleccionar en lo select


class LanguageOption(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = './chromedriver')
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()
        driver.implicitly_wait(30)

    def test_select_language(self):
        #creamos una lista con las opciones que tiene el selector de lenguaje
        exp_options = ['English', 'French', 'German']
        #creamos una lista vacia para guardar las opciones que elijamos
        act_options = []
        #creamo una variable que contendra lo encontrado en el elemento "language"
        select_language = Select(self.driver.find_element_by_id('select-language'))
        
        #validamos que verdadereamente tiene 3 opciones
        #se compara con la lista de opciones extraidos en el select language
        self.assertEqual(3, len(select_language.options)) #options permite entrar directamente a la lista
        #recorremos la lista y guardamos SOLO el texto en la variable vacia act_options
        for option in select_language.options:
            act_options.append(option.text)

        #comparamos si la lista obtenida es igual a la declarada en exp_options
        self.assertListEqual(exp_options, act_options)

        #validamos que el idioma Englis sea el que está por defecto
        self.assertEqual('English', select_language.first_selected_option.text)

        #vamos a indicarle a seleniums que ahora seleccione el idioma ENGLISH
        select_language.select_by_visible_text('German')

        #validamos que debe salir en la url store=german para que sea true
        self.assertTrue('store=german' in self.driver.current_url)

        #volvemos a buscar en la lista los valores y lo guardamos en select_language
        select_language = Select(self.driver.find_element_by_id('select-language'))
        #luego decimos que seleccione 0 ya que es el primero en la lista (English)
        select_language.select_by_index(0)

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.quit()
    
if __name__ == "__main__":
    unittest.main(verbosity = 2)