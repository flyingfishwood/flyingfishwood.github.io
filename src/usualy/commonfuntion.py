from appium import webdriver


class APP:
    def __init__(self, bool1):
        self.bool1 = bool1


    def start(self):
        caps = {"platformName": "android",
                "deviceName": "test",
                "appPackage": "com.zhl.qk.aphone",
                "appActivity": "com.zhl.qiaokao.aphone.activity.SplashActivity",
                "autoGrantPermission": "True",
                "noReset": "True",
                "ensureWebviewsHavePages": True}

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def get_current_activity(self):
        current = self.driver.current_activity
        if current == "com.zhl.qiaokao.aphone.activity.MainActivity":
            self.bool1 = True
        return self.bool1

    def quit(self):
        self.driver.quit()

    def tap(self):
        self.driver.tap([(100, 200)])



# APP.tap()
# class function(APP):
#
#     def __int__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def tap_somewhere(self):
#         self.driver.tap([(100, 200)])
# bart = function(100,200)
# print(bart.x)
# print(bart.y)
# bart.tap_somewhere()
