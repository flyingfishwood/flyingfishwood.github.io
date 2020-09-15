import unittest
from src.UIelement.studypage import get_studypage
from src.UIelement.PracticePage import HandlePracticePage, PracticePage
from src.UIelement.loginpage import APP
import time


class test_practice(unittest.TestCase, PracticePage):

    def setUp(self):
        APP.start(self)

    def test_practice(self):
        time.sleep(1)
        get_studypage.get_tap_me(self).click()
        time.sleep(1.5)
        HandlePracticePage.handle_note_book(self)
        time.sleep(2)
        HandlePracticePage.handle_note_book_grade7(self)
        time.sleep(2)
        HandlePracticePage.handle_practice_btn(self)
        time.sleep(2)
        HandlePracticePage.handle_get_i_know_btn(self)
        time.sleep(2)
        for i in range(3):
            PracticePage.get_choose_answer(self)
            time.sleep(1)
            for j in range(2):
                PracticePage.get_check_answer(self)
                time.sleep(1)
        time.sleep(2)
        text = HandlePracticePage.handle_finish_practice_text(self)
        print(text)
        self.assertEqual(HandlePracticePage.handle_finish_practice_text(self), '恭喜完成练习', 'false')

    def tearDown(self):
        APP.quit(self)


if __name__ == '__main__':
    unittest.main(verbosity=2)
