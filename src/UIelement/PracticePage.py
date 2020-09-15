from src.usualy.commonfuntion import APP


class PracticePage(APP):

    def get_note_book(self):
        note_book = self.driver.find_element_by_id("com.zhl.qk.aphone:id/me_view_notebook")
        return note_book

    def get_note_book_detail_grade_7(self):
        grade_7 = self.driver.find_element_by_xpath \
            (
                "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ImageView")
        return grade_7

    def get_practice_btn(self):
        practice_btn = self.driver.find_element_by_xpath \
            (
                "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[4]/android.view.View/android.view.View/android.view.View[2]/android.view.View[4]")
        return practice_btn

    def get_i_know_btn(self):
        x1 = 449 / 900
        y1 = 1010 / 1600
        screen = self.driver.get_window_size()
        width = screen['width']
        height = screen['height']
        xdict = x1 * width
        # print(xdict)
        ydict = y1 * height
        # print(ydict)
        self.driver.implicitly_wait(10)
        self.driver.tap([(xdict, ydict)])

    def get_choose_answer(self):
        x1 = 443 / 900
        y1 = 773 / 1600
        screen = self.driver.get_window_size()
        width = screen['width']
        height = screen['height']
        xdict = x1 * width
        # print(xdict)
        ydict = y1 * height
        # print(ydict)
        self.driver.implicitly_wait(10)
        self.driver.tap([(xdict, ydict)])

    def get_check_answer(self):
        x1 = 444 / 900
        y1 = 1492 / 1600
        screen = self.driver.get_window_size()
        width = screen['width']
        height = screen['height']
        xdict = x1 * width
        # print(xdict)
        ydict = y1 * height
        # print(ydict)
        self.driver.implicitly_wait(10)
        self.driver.tap([(xdict, ydict)])

    def get_finish_practice_text(self):
        finish_practice_text = self.driver.find_element_by_xpath \
            (
                "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]")
        return finish_practice_text


class HandlePracticePage(PracticePage):

    def handle_note_book(self):
        self.get_note_book().click()

    def handle_note_book_grade7(self):
        self.get_note_book_detail_grade_7().click()

    def handle_practice_btn(self):
        self.get_practice_btn().click()

    def handle_get_i_know_btn(self):
        self.get_i_know_btn()

    def handle_finish_practice_text(self):
        return self.get_finish_practice_text().text

        # print(self.get_finish_practice_text().text)
