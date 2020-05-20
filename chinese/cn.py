from selenium import webdriver
import random
import time

spcing = random.uniform(3, 18)
# webdriver对象,使用Chrome浏览器
wd = webdriver.Chrome('chromedriver.exe')
wd.get('https://www.ulearning.cn')

wd.implicitly_wait(10)
# 返回WebElement对象
element = wd.find_element_by_class_name('login-btn-text')
element.click()
wd.implicitly_wait(10)
element = wd.find_element_by_id('userLoginName')
element.send_keys('wit1915040123')
wd.implicitly_wait(10)
element = wd.find_element_by_id('userPassword')
element.send_keys('wit1915040123\n')
wd.implicitly_wait(10)
element = wd.find_element_by_css_selector(
    '.ko-view .course-list-body .course-list-area #courseCard47149')
element.click()
# 以上步骤进入优学院并选择语文
time.sleep(10)
# 选择课件栏目
wd.implicitly_wait(10)
element = wd.find_element_by_css_selector(
    '.ko-view .course-nav .tab-textbook')
element.click()
wd.implicitly_wait(10)
# 选择第一章学习（按需求更改章节）
elements = wd.find_elements_by_css_selector(
    '.table-body .chapter-item .button')
elements[1].click()  # 更改序号来选择不同章节（0-3）
wd.implicitly_wait(10)
for handle in wd.window_handles:
    # 先切换到该窗口
    wd.switch_to.window(handle)
    # 得到该窗口的标题栏字符串，判断是不是我们要操作的那个窗口
    if '大学语文' in wd.title:
        # 如果是，那么这时候WebDriver对象就是对应的该该窗口，正好，跳出循环，
        break
# 跳过所以提示
time.sleep(3)
element = wd.find_element_by_css_selector('.btn-submit')
element.click()
time.sleep(1)
element = wd.find_element_by_css_selector('.btn-hollow')
element.click()
time.sleep(1)
element = wd.find_element_by_css_selector('.btn-hollow')
element.click()
time.sleep(1)
element = wd.find_element_by_css_selector('.btn-hollow')
element.click()
time.sleep(3)
element = wd.find_element_by_css_selector('.page-control-area .next-page-btn')
# print(elements[2].get_attribute('innerHTML'))
# 点两次去到ppt（可能要根据具体情况定）
element.click()
element.click()
time.sleep(1)
# 点开ppt
element = wd.find_element_by_css_selector('.view-btn')
element.click()
time.sleep(2)
# 进入iframe框架
wd.switch_to.frame(wd.find_element_by_tag_name('iframe'))
# 选择翻页按钮
element1 = wd.find_element_by_id('pagePrev')
element2 = wd.find_element_by_id('pageNext')
while True:
    element2.click()
    time.sleep(random.randint(5, 10))
    element2.click()
    time.sleep(random.randint(5, 10))
    element1.click()
    time.sleep(random.randint(5, 10))
