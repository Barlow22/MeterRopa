from selenium.webdriver.common.by import By

class PageCategory:


    def __init__(self, driver):
        self.driver = driver
        self.view_list = (By.CLASS_NAME, 'icon-th-list')
                

    def select_category(self, category):
        category_selection = (By.LINK_TEXT, category)
        self.driver.find_element(*category_selection).click()

    def list_view(self):
        self.driver.find_element(*self.view_list).click()

