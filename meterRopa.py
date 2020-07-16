import unittest
from selenium import webdriver
import time
from pageIndex import PageIndex
from pageItems import PageItems
from pageShop import PageShop
from pageCategory import PageCategory
from selenium.webdriver.chrome.options import Options


class SearchCases(unittest.TestCase):


    def setUp(self):
        option = Options()
        option.add_argument('start-maximized')
        option.add_argument('incognito')
        #option.add_argument('--headless')
        self.driver = webdriver.Chrome('chromedriver.exe', options=option)
        #self.driver.maximize_window()
        #self.driver.set_window_size(800, 600)
        #self.driver.set_window_position(150, 150)
        self.driver.get('http://automationpractice.com/index.php')
        self.driver.implicitly_wait(5)
        self.index_page = PageIndex(self.driver)
        self.items_page = PageItems(self.driver)
        self.shop_page = PageShop(self.driver)
        self.category_page = PageCategory(self.driver)

    @unittest.skip('not needed now')
    def test_search_tshirts(self):
        try:
            self.index_page.search_items('t-shirts')
            self.items_page.pick_color()
            self.shop_page.quantity('25')
            self.shop_page.sum_quantity(3)
            self.assertEqual(self.shop_page.return_quantity() , '28')
        except:
            self.driver.save_screenshot('error.jpg')
    @unittest.skip('not needed now')
    def test_selections(self):
        self.index_page.search_items('t-shirts')
        self.items_page.select_by_text('Product Name: A to Z')
        self.items_page.select_by_value('reference:asc')
        self.items_page.select_by_index(4)

    @unittest.skip('No se necesita ahora')    
    def test_casual_dresses(self):
        # no estoy seguro de que esto sea una buena practica, pero quiera algo un poco mas abstracto. Quizas lo
        # ideal es para cada seleccion que hagamos un metodo distinto, pero me la jugue con esto!
        self.index_page.select_banner_tittle('DRESSES')
        self.category_page.select_category('CASUAL DRESSES')
        self.items_page.select_item('Printed Dress')
        self.shop_page.quantity('5')
        self.shop_page.order_by_text('L')
        self.shop_page.add_to_cart()       
        #esto seguramente este mal, pero queria probar todos los casos sin que me termine la ejecucion y ver cuales fallan
        #y cuales no. No encontre si hay una forma de poner todo en un solo bloque try.
        try:
            self.assertTrue('5' in self.shop_page.return_cart_quantity())
        except:
            print('La cantidad del carrito es distinta')
        try:
            self.assertEqual(self.shop_page.return_cart_price(), '$130.00')
        except:
            print('El precio del carrito es incorrecto')
        try:
            self.assertEqual(self.shop_page.return_cart_ship_price(), '$2.00')
        except:
            print('El precio del envio es incorrecto')
        try:
            self.assertEqual(self.shop_page.return_cart_total_price(), '$132.00')
        except:
            print('El precio total es incorrecto')
        try:
            self.assertEqual(self.shop_page.return_cart_product_name(), 'Printed Dress')
        except:
            print('El nombre de la prenda es incorrecto')
        finally:
            print()
            print(self.shop_page.return_cart_quantity())
            print(type(self.shop_page.return_cart_quantity()))
            print()
            print(self.shop_page.return_cart_price())
            print(type(self.shop_page.return_cart_price()))
            print(self.shop_page.return_cart_ship_price())
            print(type(self.shop_page.return_cart_ship_price()))
            print()
            print(self.shop_page.return_cart_total_price())
            print(type(self.shop_page.return_cart_total_price()))
            print()
            print(self.shop_page.return_cart_product_name())
            print(type(self.shop_page.return_cart_product_name()))
        
    #@unittest.skip('no se necesita')
    def test_second_dress(self):
        self.index_page.select_banner_tittle('DRESSES')
        self.category_page.list_view()
    @unittest.skip('No esta terminado')
    def test_invalid_mail(self):
        pass
    
    @unittest.skip('No esta terminado')
    def test_authentication_invalid(self):
        pass

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        
if __name__ == "__main__":
    unittest.main()