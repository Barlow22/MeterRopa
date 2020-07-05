import unittest
from selenium import webdriver
import time
from pageIndex import PageIndex
from pageItems import PageItems
from pageShop import PageShop
from selenium.webdriver.chrome.options import Options


class SearchCases(unittest.TestCase):


    def setUp(self):
        option = Options()
        option.add_argument('start-maximized')
        option.add_argument('incognito')
        option.add_argument('--headless')
        self.driver = webdriver.Chrome('chromedriver.exe', options=option)
        #self.driver.maximize_window()
        #self.driver.set_window_size(800, 600)
        #self.driver.set_window_position(150, 150)
        self.driver.get('http://automationpractice.com/index.php')
        self.driver.implicitly_wait(5)
        self.index_page = PageIndex(self.driver)
        self.items_page = PageItems(self.driver)
        self.shop_page = PageShop(self.driver)

    #@unittest.skip('not needed now')
    def test_search_tshirts(self):
        try:
            self.index_page.search_items('t-shirts')
            self.items_page.pick_color()
            self.shop_page.quantity('25')
            self.shop_page.sum_quantity(5)
            self.assertEqual(self.shop_page.return_quantity() , '28')
        except:
            self.driver.save_screenshot('error.jpg')
   
    def test_selections(self):
        self.index_page.search_items('t-shirts')
        self.items_page.select_by_text('Product Name: A to Z')
        self.items_page.select_by_value('reference:asc')
        self.items_page.select_by_index(4)
        

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        
if __name__ == "__main__":
    unittest.main()