class PageIndex:


    def __init__(self, my_driver):
        self.driver = my_driver
        self.search_query_top  = 'search_query_top'
        self.submit_search = 'submit_search'
        self.color = 'color_1'

    def search_items(self, item):
        self.driver.find_element_by_id(self.search_query_top).send_keys(item)
        self.driver.find_element_by_name(self.submit_search).click()
    

