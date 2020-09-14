# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

import unittest
from src.UIelement.loginpage import *
from src.UIelement.TapAssistantPage import *
from src.UIelement.studypage import get_studypage


class loginTest(unittest.TestCase, login_page, Assistant):

    def setUp(self):
        APP.start(self)

    def test_login(self):
        # login.get_loginpage(self)
        if APP.get_current_activity(self):
            print('已登录,退出中')
            get_studypage.get_tap_me(self).click()
            login_page.get_setting_btn(self)
            login_page.get_logout(self).click()
            login_page.get_commit_quit(self).click()
            login_handle.click_select_phone(self)
            login_page.get_phone_input(self).clear()
            login_page.get_phone_input(self).send_keys('18665116319')
            login_handle.click_box_login(self)
            login_handle.click_iv_pwd(self)
            login_handle.handle_person_login_et_pwd(self)
            login_handle.click_login_btn_register(self)
            study_tab = login_page.get_study_tab(self)
            self.assertEqual(study_tab, '学习', 'fales')
        else:
            login_handle.click_select_phone(self)
            login_page.get_phone_input(self).clear()
            login_page.get_phone_input(self).send_keys('18665116319')
            login_handle.click_box_login(self)
            login_handle.click_iv_pwd(self)
            login_handle.handle_person_login_et_pwd(self)
            login_handle.click_login_btn_register(self)
            study_tab = login_page.get_study_tab(self)
            self.assertEqual(study_tab, '学习', 'fales')

    @unittest.skip('T')
    def test_assistant(self):
        HandleAssistant.handle_click_tap_assistant(self)
        HandleAssistant.handle_click_book_center(self)
        bool1 = Assistant.get_tap_assistant_content(self)
        self.assertEqual(bool1, True, 'FALSE')

    def tearDown(self):
        APP.quit(self)


if __name__ == '__main__':
    unittest.main(verbosity=2)
