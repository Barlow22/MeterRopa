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
        
    def test_casual_dresses(self):
        # no estoy seguro de que esto sea una buena practica, pero quiera algo un poco mas abstracto. Quizas lo
        # ideal es para cada seleccion que hagamos un metodo distinto, pero me la jugue con esto!
        self.index_page.select_banner_tittle('DRESSES')
        self.category_page.select_category('CASUAL DRESSES')
        self.items_page.select_item('Printed Dress')
        self.shop_page.quantity('5')
        self.shop_page.order_by_text('L')
        self.shop_page.add_to_cart()
        self.assertIn(self.shop_page.return_cart_quantity(), '5')
        self.assertIs(self.shop_page.return_cart_price, '$130.00')
        self.assertIs(self.shop_page.return_cart_ship_price, '$2.00')
        self.assertEqual(self.shop_page.return_cart_total_price, '$132.00')
        self.assertEqual(self.shop_page.return_cart_product_name, 'Printed Dress')
        time.sleep(2)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        
if __name__ == "__main__":
    unittest.main()