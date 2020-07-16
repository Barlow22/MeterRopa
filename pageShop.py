from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PageShop:


    def __init__(self, my_driver):
        self.driver = my_driver
        self.quantity_wanted = (By.ID, 'quantity_wanted')
        self.sum_button = (By.XPATH, '//*[@id="quantity_wanted_p"]/a[2]/span/i')
        self.order = (By.ID, 'group_1')
        self.cart_button = (By.ID, 'add_to_cart')
        self.cart_quantity = (By.ID, 'layer_cart_product_quantity')
        self.cart_price = (By.ID, 'layer_cart_product_price')
        self.cart_product_name = (By.ID, 'layer_cart_product_title' )
        self.cart_ship_price = (By.XPATH, '/html/body/div/div[1]/header/div[3]/div/div/div[4]/div[1]/div[2]/div[2]/span')
        self.cart_total_price = (By.XPATH, '//*[@id="layer_cart"]/div[1]/div[2]/div[3]/span')

    def quantity(self, cantidad):
        self.driver.find_element(*self.quantity_wanted).clear()
        self.driver.find_element(*self.quantity_wanted).send_keys(cantidad)

    def sum_quantity(self, quantity):
        for i in range(quantity):
            self.driver.find_element(*self.sum_button).click()

    def return_quantity(self):
        return self.driver.find_element(*self.quantity_wanted).get_attribute('value')

    def order_by_text(self, text):
        order = Select(self.driver.find_element(*self.order))
        order.select_by_visible_text(text)

    def add_to_cart(self):
        self.driver.find_element(*self.cart_button).click()

    def return_cart_quantity(self):
        try:
            element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.cart_quantity))
            return element.text
        except:
            print('Elemento no encontrado')
        #return self.driver.find_element(*self.cart_quantity).text

    
    def return_cart_price(self):
        return self.driver.find_element(*self.cart_price).text

    def return_cart_ship_price(self):
        return self.driver.find_element(*self.cart_ship_price).text

    def return_cart_total_price(self):
        return self.driver.find_element(*self.cart_total_price).text

    def return_cart_product_name(self):
        return self.driver.find_element(*self.cart_product_name).text
    
        


    