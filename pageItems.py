from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class PageItems:
    def __init__(self, my_driver):
        self.driver = my_driver
        self.color = (By.ID, 'color_1')
        self.order = (By.ID, 'selectProductSort')

    def pick_color(self):
        self.driver.find_element(*self.color).click()
    
    def select_by_text(self, texto):
        order = Select(self.driver.find_element(*self.order))
        order.select_by_visible_text(texto)

    def select_by_value(self, value):
        order_value = Select(self.driver.find_element(*self.order))
        order_value.select_by_value(value)

    def select_item(self, item):
        item_type = (By.LINK_TEXT, item)
        self.driver.find_element(*item_type).click()
    
    def select_by_index(self, number):
        order_value = Select(self.driver.find_element(*self.order))
        order_value.select_by_index(number)