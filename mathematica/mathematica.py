from selenium import webdriver
import  random
import  time

spcing = random.uniform(3,18)
#webdriver对象,使用Chrome浏览器
wd = webdriver.Chrome(r'chromedriver')
wd.get('https://www.ulearning.cn')

wd.implicitly_wait(10)
#返回WebElement对象
element = wd.find_element_by_class_name('login-btn-text')
element.click()
wd.implicitly_wait(10)
element = wd.find_element_by_id('userLoginName')
element.send_keys('wit1915040123')

wd.implicitly_wait(10)
element = wd.find_element_by_id('userPassword')
element.send_keys('wit1915040123')

wd.implicitly_wait(10)
element = wd.find_element_by_css_selector('.button.button-red-solid.btn-confirm')
element.click()

wd.implicitly_wait(10)
element = wd.find_elements_by_class_name('cover-wrapper')
element[8].click()

time.sleep(3)

wd.implicitly_wait(10)
elements = wd.find_elements_by_class_name('tab-link')
elements[1].click()#选中课件


#课件被覆盖，改用以下方法
#wd.execute_script("arguments[3].click();", element)

wd.implicitly_wait(10)
# #button前需要等待几秒
time.sleep(3)
elements = wd.find_elements_by_class_name("button-red-hollow")
elements[2].click()#调整这里来选择不同的章节

#打开的新窗口，但仍然聚焦在旧窗口，如下代码跳转窗口
for handle in wd.window_handles:
    #切换窗口
    wd.switch_to.window(handle)
    #用标题字符判断是否是我们要的新窗口
    if '数学分析' in wd.title:
        break

time.sleep(3)
#点三次去掉提示
for i in range(0,3):
    element = wd.find_element_by_css_selector('.btn-hollow')
    element.click()

element = wd.find_element_by_css_selector('.view-btn')
element.click()
time.sleep(2)
# 进入iframe框架
wd.switch_to.frame(wd.find_element_by_tag_name('iframe'))
# 选择翻页按钮
element1 = wd.find_element_by_id('preBtn')
element2 = wd.find_element_by_id('nextBtn')
while True:
    element2.click()
    time.sleep(random.randint(1, 3))
    element2.click()
    time.sleep(random.randint(1, 3))
    element1.click()
    time.sleep(random.randint(1, 3))
