from Base.Base_Method import Base_Method
import Page,allure
class Operating_Method(Base_Method):
    def __init__(self,driver):
        Base_Method.__init__(self,driver)
    @allure.step(title='点击回退按钮')
    def click_back_button(self):
        self.click_elment(Page.back_button)
    @allure.step(title='获取元素列表中的text值')
    def gain_text_list(self,elements):
        self.list = []
        for i in self.find_elements(elements):
            self.list.append(i.text)
        return self.list
