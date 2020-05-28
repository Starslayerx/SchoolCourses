# Selenium 的自动化 #
***
## Selenium的安装
* pip安装python库：
>`pip install Selenium`
* 安装浏览器驱动：
[Chrome驱动下载](https://chromedriver.storage.googleapis.com/index.html)
[Edge驱动下载](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
***
## 如何使用Selenium
* 1.使用浏览器驱动打开网页
* 2.找到所需要操控的HTML元素
*  3.操控所找到的HTML元素
#### 1、使用驱动打开网页
* 导入Selenium包
>`from selenium import webdriver`

* 创建 WebDriver 对象，指明使用chrome浏览器驱动

>`wd = webdriver.Chrome(r'd:\webdrivers\chromedriver.exe')`

>`wd = webdriver.Chrome()`

* 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
>`wd.get('https://www.baidu.com')`

#### 2、找到元素(element返回一个对象，elements返回一个对象列表)
###### 使用find_elements选择的是符合条件的所有元素，如果没有符合条件的元素，返回空列表

###### 使用find_element选择的是符合条件的第一个元素， 如果没有符合条件的元素，抛出NoSuchElementException异常

* 根据元素的ID找
>`wd.find_element_by_id('ID名')`
* 根据元素的类查找
>`wd.find_elements_by_class_name('类名')`
* 根据tag名查找
>`wd.find_elements_by_tag_name('tag名')`
* 使用CSS选择器查找（和CSS知识相似）常用
>`wd.find_element_by_css_selector('CSS Selector参数')`

如：
>`wd.find_element_by_css_selector('. + 类名')`
>`wd.find_element_by_css_selector('# + ID名')`
>`wd.find_element_by_css_selector('tag名')`
* 组选择，子节点和兄弟节点的选择暂时略，还么想好怎么写，后面应该会补上
#### 3、操控所选择的元素
* 点击元素（调用 WebElement 对象的 click 方法去点击）
>`WebElement.click()` #点击元素
* 输入框（调用元素WebElement对象的send_keys方法）
>`WebElement.clear()` #清除输入框已有的字符串

>`WebElement.send_keys('ScmTble')` #输入新字符串
* 获取元素的文本内容
>`WebElement.text`
* 获取元素属性（元素的类、ID、href等）
>`WebElement.get_attribute('class\id\href')`
* 获取元素对应的HTML
>`WebElement.get_attribute('outerHTML')` 获取整个元素对应的HTML文本内容

>`WebElement.get_attribute('innerHTML')` 获取某个元素内部的HTML文本内容
* 获取输入框内的内容（区别与Text）
>`WebElement.get_attribute('value')`

###### 但是，有时候，元素的文本内容没有展示在界面上，或者没有完全完全展示在界面上。 这时，用WebElement对象的text属性，获取文本内容，就会有问题。出现这种情况，可以尝试使用
>`WebElement.get_attribute('innerText')`   或者
`WebElement.get_attribute('textContent')`
***
## frame切换/窗口切换

