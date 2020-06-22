from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class PageIndex:


    def __init__(self, my_driver):
        self.driver = my_driver
        self.query_top = (By.ID, 'search_query_top' )
        self.submit_search = (By.NAME, 'submit_search')
        

    def search_items(self, item):
        search_box = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.query_top))
        self.driver.find_element(*self.query_top).send_keys(item)
        self.driver.find_element(*self.submit_search).click()
    

