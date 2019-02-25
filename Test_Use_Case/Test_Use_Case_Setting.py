from Base.Get_Driver import Get_Driver
from Return_Page.Return_Page import Return_Page
from Yaml.Read_Yaml import Read_Yaml
import Page,time,pytest,allure

def gain_yaml():
    gain_yaml_data_list = []
    yaml_data = Read_Yaml('Input_Yaml.yaml').read_yaml()
    for i in yaml_data.keys():
        gain_yaml_data_list.append((i,yaml_data.get(i).get('input_text'),yaml_data.get(i).get('assert_text_01'),
                                    yaml_data.get(i).get('assert_text_02')))
    return gain_yaml_data_list
class TestSettingLogin:
    def setup_class(self):
        self.Dv = Return_Page(Get_Driver().get_driver('com.android.settings','.HWSettings'))
    def teardown_class(self):
        self.Dv.driver.quit()
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('test_number,input_text,assert_text_01,assert_text_02',gain_yaml())
    @allure.step(title='验证设置的正确性')
    def test_setting(self,test_number,input_text,assert_text_01,assert_text_02):
        @allure.step(title='输入搜索项并断言')
        def test_input():
            self.Dv.return_page().send_keys_text(Page.search_setting,input_text)
            @allure.step(title='断言')
            def assert_try_except():
                time.sleep(1)
                self.Dv.return_page().gain_screenshot()
                try:
                    if assert_text_02:
                        allure.attach('断言的用例编号：','{}'.format(test_number))
                        assert assert_text_01 | assert_text_02 in self.Dv.return_page().gain_text_list(Page.setting_title)
                    else:
                        allure.attach('断言的用例编号：','{}'.format(test_number))
                        assert assert_text_01 in self.Dv.return_page().gain_text_list(Page.setting_title)
                except Exception as e:
                    allure.attach('断言失败，错误信息：','{}'.format(e))
                finally:
                    self.Dv.return_page().click_back_button()
            assert_try_except()
        test_input()
