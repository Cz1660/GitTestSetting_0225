from Page.Operating_Method import Operating_Method

class Return_Page:
    def __init__(self,driver):
        self.driver = driver
    def return_page(self):
        return Operating_Method(self.driver)