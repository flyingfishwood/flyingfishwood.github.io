
from src.UIelement.loginpage import APP

import time


class get_studypage(APP):

    def get_Formula_theorem(self):

        self.driver.implicitly_wait(3)
        Formula_theorem = self.driver.find_element_by_xpath\
            ("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.ImageView")
        return Formula_theorem

    def get_close_btn(self):
        self.driver.implicitly_wait(3)
        close_btn = self.driver.find_element_by_id("com.zhl.qk.aphone:id/plat_close_btn")
        return close_btn

    def click_english_dict(self):
        # self.driver.tap([(595,276),(665,346)], 100)
        x1 = 760/1080
        y1 = 479/2400
        screen = self.driver.get_window_size()
        width = screen['width']
        height = screen['height']
        xdict = x1*width
        # print(xdict)
        ydict = y1*height
        # print(ydict)
        self.driver.implicitly_wait(10)
        self.driver.tap([(xdict, ydict)])
        # print('dianji')


    def get_view_search(self):
        self.driver.implicitly_wait(3)
        view_search = self.driver.find_element_by_id("com.zhl.qk.aphone:id/view_search")
        return view_search

    def get_et_input(self):
        self.driver.implicitly_wait(3)
        et_input = self.driver.find_element_by_id("com.zhl.qk.aphone:id/et_input")
        return et_input

    def get_first_list(self):
        self.driver.implicitly_wait(3)
        first_list = self.driver.find_element_by_xpath \
                (
                "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.TextView[1]")
        return first_list

    def get_quit_search(self):
        self.driver.implicitly_wait(3)
        quit_search = self.driver.find_element_by_id("com.zhl.qk.aphone:id/plat_tv_right")
        return quit_search

    #我的页面
    def get_tap_me(self):
        self.driver.implicitly_wait(3)
        tap_me = self.driver.find_element_by_id("com.zhl.qk.aphone:id/tab_me")
        return tap_me

    def get_editor_me(self):
        self.driver.implicitly_wait(3)
        editor_me = self.driver.find_element_by_id("com.zhl.qk.aphone:id/me_view_editor")
        return editor_me

    def get_change_book(self):
        self.driver.implicitly_wait(2)
        change_book = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView")

        return change_book

    def get_select_grade_book(self):
        self.driver.implicitly_wait(2)
        select_grade_book = self.driver.find_elements_by_id("com.zhl.qk.aphone:id/tv_book_name")
        return select_grade_book

    def get_study_state(self):
        study_state = self.driver.find_elements_by_id("com.zhl.qk.aphone:id/tv_state")
        return study_state

    # 闯关学习
    def get_study_dicts(self):
        study_dicts = self.driver.find_element_by_xpath\
            ("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.Button[1]")
        return study_dicts

    # 选择全部单词
    def get_select_all_dicts(self):
        all_dicts = self.driver.find_element_by_id("com.zhl.qk.aphone:id/tv_word_practice_all")
        return all_dicts

    # 开始闯关
    def get_begin_btn(self):
        begin_btn = self.driver.find_element_by_id("com.zhl.qk.aphone:id/btn_learn_start")
        return begin_btn

    # 练习标题
    def get_title_dict(self):
        dict_title = self.driver.find_element_by_xpath\
            ("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View[1]")
        return dict_title

    def get_test_model(self):
        books = self.driver.find_elements_by_id("com.zhl.qk.aphone:id/tv_desc")
        num = len(books)
        str1 = "单词模块"
        list1 = []
        if num == 0:
            print('页面无数据，请重新选择书本')
        elif num > 0:
            for i in range(num):
                list1.append(books[i].text)

            if str1 in list1:
                index1 = list1.index(str1)
                books[index1].click()
                time.sleep(1)
        else:
            raise IndexError


class handle_study_page(get_studypage):
    # 左滑动方法
    def swipe_left(self):
        screen = self.driver.get_window_size()
        width = screen['width']
        height = screen['height']
        x1 = int(width * 0.9)
        print(x1)
        y1 = int(height * 0.5)
        print(y1)
        x2 = int(width * 0.1)
        print(x2)
        time.sleep(5)
        self.driver.swipe(x1, y1, x2, y1, 1000)

    # 公式定理点击事件
    def handle_formula_theorem(self):
        self.get_Formula_theorem().click()

    # 关闭按钮点击事件
    def handle_close_btn(self):
        self.get_close_btn().click()

    # 英语词典点击
    def handle_english_dict(self):
        self.get_english_dict()

    # 搜索点击
    def handle_search_view(self):
        self.get_view_search().click()

    # 搜索框输入
    def handle_search_input(self):
        self.get_et_input().send_keys('food')

    # 获得列表属性
    def handle_get_list_property(self):
        text = self.get_first_list().text
        return text

    # 退出字典搜索
    def handle_quit_search(self):
        self.get_quit_search().click()

    # 切换到我的页面
    def handle_switch_me(self):
        self.get_tap_me().click()

    # 获取我的页面按钮属性
    def handle_editor_me(self):
        t = self.get_editor_me().text
        return t

    # 更换教材
    def handle_change_book(self):
        self.get_change_book().click()



