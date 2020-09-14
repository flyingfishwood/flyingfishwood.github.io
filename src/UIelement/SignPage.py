from src.UIelement.loginpage import APP




class GetSignPage(APP):
    # 首页签到按钮
    def get_sign_btn(self):
        sign_btn = self.driver.find_element_by_id("com.zhl.qk.aphone:id/img_btn_sign")
        return sign_btn

    # 签到按钮元素
    def get_sign(self):
        self.driver.implicitly_wait(3)
        sign = self.driver.find_element_by_xpath \
                (
                "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View[15]/android.view.View")
        return sign

    # 关闭弹窗
    def get_close_alert(self):
        self.driver.implicitly_wait(5)
        close_alert = self.driver.find_element_by_xpath \
                (
                "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.app.Dialog/android.view.View[2]/android.widget.Image")
        return close_alert


class HandleSignPage(GetSignPage):
    # 首页签到点击动作
    def handle_sign_btn(self):
        self.get_sign_btn().click()

    # 关闭弹窗动作
    def handle_close_alert(self):
        self.get_close_alert().click()

    #签到点击
    def handle_sign(self):
        self.get_sign().click()