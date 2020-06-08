class PageItems:
    def __init__(self, my_driver):
        self.driver = my_driver
        self.color = 'color_1'

    def pick_color(self):
        self.driver.find_element_by_id(self.color).click()