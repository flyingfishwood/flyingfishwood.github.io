from src.UIelement.SignPage import GetSignPage, HandleSignPage
import unittest
from src.UIelement.loginpage import APP


class test_studypage(unittest.TestCase, GetSignPage):

    def setUp(self):
        APP.start(self)

    def test_sign(self):
        HandleSignPage.handle_sign_btn(self)
        if GetSignPage.get_sign(self).text == '明日再来':
            print('已签到过，测试结束')
        else:
            HandleSignPage.handle_sign(self)
            HandleSignPage.handle_close_alert(self)
            self.assertEqual(GetSignPage.get_sign(self).text, '明日再来', 'false')

    def tearDown(self):
        APP.quit(self)


if __name__ == '__main__':
    unittest.main(verbosity=2)
