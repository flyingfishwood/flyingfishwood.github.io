# from appium import webdriver
from src.UIelement.loginpage import APP


class Assistant(APP):
    def __int__(self):
        pass

    def get_tap_assistant_content(self):
        tap_assistant_content = self.driver.find_element_by_id("com.zhl.qk.aphone:id/view_content").is_displayed()
        return tap_assistant_content

    def get_tap_assistant_my_book(self):
        tap_assistant = self.driver.find_element_by_id("com.zhl.qk.aphone:id/tab_assistant")
        return tap_assistant

    def get_tap_assistant_book_center(self):
        book_center = self.driver.find_element_by_xpath \
            (
                "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.TextView")
        return book_center


class HandleAssistant(Assistant,):

    def handle_click_tap_assistant(self):
        self.get_tap_assistant_my_book().click()

    def handle_click_book_center(self):
        self.get_tap_assistant_book_center().click()
