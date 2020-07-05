from selenium.webdriver.common.by import By


class PageShop:


    def __init__(self, my_driver):
        self.driver = my_driver
        self.quantity_wanted = (By.ID, 'quantity_wanted')
        self.sum_button = (By.XPATH, '//*[@id="quantity_wanted_p"]/a[2]/span/i')
        

    def quantity(self, cantidad):
        self.driver.find_element(*self.quantity_wanted).clear()
        self.driver.find_element(*self.quantity_wanted).send_keys(cantidad)

    def sum_quantity(self, quantity):
        for i in range(quantity):
            self.driver.find_element(*self.sum_button).click()

    def return_quantity(self):
        return self.driver.find_element(*self.quantity_wanted).get_attribute('value')

    