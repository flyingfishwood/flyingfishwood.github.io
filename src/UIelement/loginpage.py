from appium import webdriver
import time


class APP:

    def __int__(self, bool1):

        self.bool1 = bool1


    def start(self):
        caps = {"platformName": "android",
                "deviceName": "CLB7N18B21007184",
                "appPackage": "com.zhl.qk.aphone",
                "appActivity": "com.zhl.qiaokao.aphone.activity.TranslucentActivity",
                "autoGrantPermission": "True",
                "noReset": "True",
                "ensureWebviewsHavePages": True}

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def quit(self):
        self.driver.quit()

    def get_current_activity(self):
        bool1 = 0
        print('启动中')
        time.sleep(5)
        current = self.driver.current_activity
        if current == "com.zhl.qiaokao.aphone.activity.MainActivity":
            bool1 = True
        return bool1








class login_page(APP):

    def __init__(self):
        self.login = APP.start()
        pass

    def get_login_select_phone(self):
        select_phone = self.driver.find_element_by_id("com.zhl.qk.aphone:id/login_btn_select_phone")
        return select_phone

    def get_login_box_login(self):
        box_login = self.driver.find_element_by_id("com.zhl.qk.aphone:id/box_login")
        return box_login

    def get_iv_pwd(self):
        iv_pwd = self.driver.find_element_by_id("com.zhl.qk.aphone:id/iv_pwd")
        return iv_pwd

    def get_person_login_et_pwd(self):
        person_login_et_pwd = self.driver.find_element_by_id("com.zhl.qk.aphone:id/person_login_et_pwd")
        return person_login_et_pwd

    def get_login_btn_register(self):
        login_btn_register = self.driver.find_element_by_id("com.zhl.qk.aphone:id/login_btn_register")
        return login_btn_register

    def get_study_tab(self):
        study = self.driver.find_element_by_id("com.zhl.qk.aphone:id/tab_learn").text
        return study

    #设置btn
    def get_setting_btn(self):
        x1 = 844 / 900
        y1 = 83.9 / 1600
        screen = self.driver.get_window_size()
        width = screen['width']
        height = screen['height']
        xdict = x1 * width
        # print(xdict)
        ydict = y1 * height
        # print(ydict)
        self.driver.implicitly_wait(10)
        self.driver.tap([(xdict, ydict)])

    #退出登录
    def get_logout(self):
        logout = self.driver.find_element_by_id("com.zhl.qk.aphone:id/btn_login_out")
        return logout

    #确定退出
    def get_commit_quit(self):
        commit_quit = self.driver.find_element_by_id("com.zhl.qk.aphone:id/tv_right")
        return commit_quit

    #登录页，手机号输出框
    def get_phone_input(self):
        phone_input = self.driver.find_element_by_id("com.zhl.qk.aphone:id/person_login_et_phone")
        return phone_input

class login_handle(login_page):
    def __init__(self):
        pass

    def click_select_phone(self):
        self.get_login_select_phone().click()

    def click_box_login(self):
        self.get_login_box_login().click()

    def click_iv_pwd(self):
        self.get_iv_pwd().click()

    def handle_person_login_et_pwd(self,pwd='123456'):
        self.get_person_login_et_pwd().click()
        self.get_person_login_et_pwd().send_keys(pwd)

    def click_login_btn_register(self):
        self.get_login_btn_register().click()


