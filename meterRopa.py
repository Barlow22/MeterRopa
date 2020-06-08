import unittest
from selenium import webdriver
import time
from pageIndex import PageIndex
from pageItems import PageItems
from pageShop import PageShop

class SearchCases(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.get('http://automationpractice.com/index.php')
        self.index_page = PageIndex(self.driver)
        self.items_page = PageItems(self.driver)
        self.shop_page = PageShop(self.driver)

    def test_search_tshirts(self):
        
        self.index_page.search_items('t-shirts')
        time.sleep(2)
        self.items_page.pick_color()
        time.sleep(2)
        self.shop_page.quantity('25')
        self.shop_page.sum_quantity()
        self.shop_page.sum_quantity()
        self.shop_page.sum_quantity()
        time.sleep(2)
        self.assertEqual(self.shop_page.return_quantity() , '28')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        
if __name__ == "__main__":
    unittest.main()