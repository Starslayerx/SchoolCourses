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

### 1. frame切换

###### iframe元素非常的特殊,在html语法中，frame元素或者iframe元素的内部会包含一个被嵌入的另一份html文档。在我们使用selenium打开一个网页是， 我们的操作范围缺省是当前的 html,并不包含被嵌入的html文档里面的内容。如果我们要操作被嵌入的html文档中的元素,就必须 切换操作范围到被嵌入的文档中。

* 使用frame的ID切换

> `wd.switch_to.frame('frameID')`

* 使用frame的name切换

> `wd.switch_to.frame('framename')`

* 先找到frame再切换(用find方法找)

> `wd.switch_to.frame(wd.find_element_by_tag_name("iframe"))`

* 切回主HTML

> `wd.switch_to.default_content()`

### 2. 窗口切换
###### 即使新窗口打开了,这时候,我们的 WebDriver对象对应的还是老窗口,自动化操作也还是在老窗口进行。

> `wd.switch_to.window(handle)`

如：

```
for handle in wd.window_handles:
    # 先切换到该窗口
    wd.switch_to.window(handle)
    # 得到该窗口的标题栏字符串，判断是不是我们要操作的那个窗口
    if 'Bing' in wd.title:
        # 如果是，那么这时候WebDriver对象就是对应的该该窗口，正好，跳出循环，
        breaks
```

* 切回原来的窗口

1. mainWindow变量保存原来窗口的句柄

> `mainWindow = wd.current_window_handle`

1. 通过前面保存的老窗口的句柄，自己切换到老窗口
 
> `wd.switch_to.window(mainWindow)`


