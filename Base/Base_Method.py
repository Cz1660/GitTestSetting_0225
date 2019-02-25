from selenium.webdriver.support.wait import WebDriverWait
import time,allure

class Base_Method:
    def __init__(self,driver):
        self.driver = driver
    def find_element(self,loc,timeout=15,poll=1):
        return WebDriverWait(self.driver,timeout,poll).until(lambda x:x.find_element(*loc))
    def find_elements(self,loc,timeout=15,poll=1):
        return WebDriverWait(self.driver,timeout,poll).until(lambda x:x.find_elements(*loc))
    @allure.step(title='点击操作')
    def click_elment(self,loc):
        self.find_element(loc).click()
    @allure.step(title='输入操作')
    def send_keys_text(self,loc,text):
        allure.attach('输入：','{}'.format(text))
        self.element = self.find_element(loc)
        self.element.clear()
        self.element.send_keys(text)
    @allure.step(title='获取截图')
    def gain_screenshot(self):
        self.time = time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime(time.time()))
        self.path = 'C:/Users/Administrator/PycharmProjects/Test_Setting_0225/Gain_Screenshot/Setting_%s.png'
        return self.driver.get_screenshot_as_file(self.path % self.time)
