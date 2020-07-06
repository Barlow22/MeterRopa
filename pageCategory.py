from selenium.webdriver.common.by import By

class PageCategory:


    def __init__(self, driver):
        self.driver = driver
                

    def select_category(self, category):
        category_selection = (By.LINK_TEXT, category)
        self.driver.find_element(*category_selection).click()
