from appium import webdriver
import time

caps = {"platformName": "android",
        "deviceName": "test",
        "appPackage": "com.zhl.qk.aphone",
        "appActivity": "com.zhl.qiaokao.aphone.activity.TranslucentActivity",
        "autoGrantPermission": "True",
        "noReset": "True",
        "ensureWebviewsHavePages": True}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
driver.implicitly_wait(10)


def get_current_activity():
    bool1 = 0
    time.sleep(5)

    current = driver.current_activity
    if current == "com.zhl.qiaokao.aphone.activity.MainActivity":
        bool1 = True
    return bool1


def swipe_left():
    screen = driver.get_window_size()
    width = screen['width']
    height = screen['height']
    x1 = int(width * 0.9)
    print(x1)
    y1 = int(height * 0.5)
    print(y1)
    x2 = int(width * 0.1)
    print(x2)
    time.sleep(5)
    driver.swipe(x1, y1, x2, y1, 1000)


def quit():
    driver.quit()


def get_element():

    books = driver.find_elements_by_id("com.zhl.qk.aphone:id/tv_desc")
    num = len(books)
    str1 = "单词模块"
    list1 = []
    for i in range(num):

        list1.append(books[i].text)

    if str1 in list1:
        index1 = list1.index(str1)
        books[index1].click()
        time.sleep(3)
    print(list1)






def change_book():
    change_book = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView")

    return change_book


def get_text():
    text = get_element()
    text[0]
    text[0].click()
    time.sleep(3)
    print('Waiting')


swipe_left()
change_book().click()
get_element()
type(get_element())
get_text()


def tap(x, y):
    driver.tap([(x, y)])


# get_current_activity()
# tap(300, 600)
# time.sleep(3)
