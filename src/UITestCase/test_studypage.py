import time
from src.UIelement.studypage import handle_study_page, get_studypage
import unittest
from src.UIelement.loginpage import APP
import warnings


class test_studypage(unittest.TestCase, get_studypage):

    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        APP.start(self)

    @unittest.skip('skip')
    def test_swipe(self):
        # 学习页面搜索，字典输入，学科切换，页面切换至我的
        handle_study_page.handle_formula_theorem(self)
        handle_study_page.handle_close_btn(self)
        handle_study_page.swipe_left(self)
        # handle_study_page.handle_english_dict(self)
        time.sleep(5)
        # tap(665,346)
        get_studypage.click_english_dict(self)
        time.sleep(1)
        handle_study_page.handle_search_view(self)
        handle_study_page.handle_search_input(self)
        self.assertEqual(handle_study_page.handle_get_list_property(self), 'food', 'false')
        handle_study_page.handle_quit_search(self)
        handle_study_page.handle_close_btn(self)
        handle_study_page.handle_switch_me(self)
        self.assertEqual(handle_study_page.handle_editor_me(self), '编辑', 'false')

    def test_change_book(self):
        # 教材更换
        handle_study_page.swipe_left(self)
        text = get_studypage.get_change_book(self).text
        handle_study_page.handle_change_book(self)
        text2 = get_studypage.get_select_grade_book(self)[0].text
        if text2 in text:
            get_studypage.get_select_grade_book(self)[0].click()
            if APP.get_current_activity(self) == 'com.zhl.qiaokao.aphone.activity.MainActivity':
                print('切换成功')
            else:
                get_studypage.get_select_grade_book(self)[1].click()
        elif text2 not in text:
            get_studypage.get_select_grade_book(self)[0].click()
            self.assertEqual(get_studypage.get_tap_me(self).text, '我的', 'False')
        else:
            raise IndexError
        time.sleep(2)

    # 闯关学习
    def test_dicts_practices(self):
        get_studypage.get_test_model(self)
        time.sleep(2)
        get_studypage.get_study_dicts(self).click()
        time.sleep(2)
        self.driver.implicitly_wait(3)
        if get_studypage.get_study_dicts(self).is_displayed():
            print('没有题目信息')
            time.sleep(2)

        else:
            get_studypage.get_select_all_dicts(self).click()
            get_studypage.get_begin_btn(self).click()
            text = get_studypage.get_title_dict(self).text
            self.assertEqual(text, '题目测试', 'False')

    def tearDown(self):
        APP.quit(self)


if __name__ == '__main__':
    unittest.main(verbosity=2)
