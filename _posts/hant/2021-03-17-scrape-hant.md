---
lang: hant
layout: post
title: 抓取網站內容
---

市面上已有众多现成的工具可用于抓取网站内容。然而，依赖这些工具，我们难以深入理解其背后的运作机制。当工作中遇到结构复杂或具有特殊性的网站时，这些现成工具可能无法满足我们的需求，难以获取预期的结果。因此，为了更深入地学习并灵活运用这些技术，我们需要亲手打造属于自己的“轮子”。

Also, take a look at some existing tools.

## 数据挖掘者

![礦工](assets/images/scrape/miner.png)

`Data Miner` 是 Chrome 上的一個非常方便的插件。它能夠輕鬆地抓取網頁上的連結和內容。

## 获取书籍

`getbook` 是一個非常方便的製作電子書工具。

```powershell
pip install getbook
```

翻譯為繁體中文：

```powershell
pip 安裝 getbook
```

`book.json`:

```json
{
  "uid": "book",
  "title": "你好，世界",
  "author": "Armin",
  "chapters": [
    "http://lucumr.pocoo.org/2018/7/13/python/",
    "http://lucumr.pocoo.org/2017/6/5/diversity-in-technology",
  ]
}
```

```shell
getbook -f ./book.json --mobi
``` 

這段指令的意思是使用 `getbook` 工具，從當前目錄下的 `book.json` 文件中獲取書籍內容，並將其轉換為 `.mobi` 格式的電子書。

如此便便捷地将一系列链接转化为电子书。借助`Data Miner`与`getbook`这两款工具，前者负责抓取链接，后者则将这些链接转化为电子书，从而轻松实现电子书的制作。

## 费曼物理学讲义

![fl](assets/images/scrape/fl.png)

在「项目实战：将费曼物理讲义网页做成电子书」章节中，我们学会了如何将一个使用`mathjax`渲染的`html`网页制作成电子书。现在，我们将继续这个项目，探讨如何获取所有相关的网页。费曼物理讲义共有三卷。上图展示了第一卷的目录。

> http.client — HTTP 协议客户端
>
> 源代码：Lib/http/client.py
>
> 本模块定义了实现 HTTP 和 HTTPS 协议客户端功能的类。通常不直接使用它 —— 模块 urllib.request 会用它来处理使用 HTTP 和 HTTPS 的 URL。
>
> 另请参阅：推荐使用 Requests 包作为更高级的 HTTP 客户端接口。

可见`requests`是更高階的接口。

```python
import requests
```

```python
def main():
    r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
    print(r.status_code)
```

主函数()
```

```shell
401
```

```python
import requests
```

def main():
    r = requests.get('https://github.com')
    print(r.status_code)
    print(r.text)

主函数()
```

```html
200
<html>
  ...
</html>
```

试了一下，说明`requests`的接口是可以使用的。

```html
     <div class="toc-chapter" id="C03">
        <span class="triangle">
         ▼
        </span>
        <a class="chapterlink" href="javascript:Goto(1,3)">
         <span class="tag">
          第三章
         </span>
         物理学与其他科学的关系
        </a>
        <div class="sections">
         <a href="javascript:Goto(1,3,1)">
          <span class="tag">
           3-1
          </span>
          引言
         </a>
         <a href="javascript:Goto(1,3,2)">
          <span class="tag">
           3-2
          </span>
          化学
         </a>
         <a href="javascript:Goto(1,3,3)">
          <span class="tag">
           3-3
          </span>
          生物学
         </a>
         <a href="javascript:Goto(1,3,4)">
          <span class="tag">
           3-4
          </span>
          天文学
         </a>
         <a href="javascript:Goto(1,3,5)">
          <span class="tag">
           3-5
          </span>
          地质学
         </a>
         <a href="javascript:Goto(1,3,6)">
          <span class="tag">
           3-6
          </span>
          心理学
         </a>
         <a href="javascript:Goto(1,3,7)">
          <span class="tag">
           3-7
          </span>
          它是如何变成这样的？
         </a>
        </div>
       </div>
```

这是在目录页面中，第三章节的`html`代码。想从这里抓取每一章节的链接。`<a href="javascript:Goto(1,3,7)">`，可见是一个`javascript`的超链接。

要抓取这些章节链接，你需要解析`javascript:Goto(1,3,7)`中的参数。通常，这种链接的格式是`javascript:Goto(bookId, chapterId, pageId)`，其中`bookId`、`chapterId`和`pageId`分别代表书籍ID、章节ID和页面ID。

你可以使用正则表达式或字符串分割来提取这些参数。例如，在Python中，你可以这样做：

```python
import re

# 假设这是你的链接
link = "javascript:Goto(1,3,7)"

# 使用正则表达式提取参数
match = re.search(r'Goto\((\d+),(\d+),(\d+)\)', link)
if match:
    book_id = match.group(1)
    chapter_id = match.group(2)
    page_id = match.group(3)
    print(f"Book ID: {book_id}, Chapter ID: {chapter_id}, Page ID: {page_id}")
```

输出将会是：

```
Book ID: 1, Chapter ID: 3, Page ID: 7
```

通过这些参数，你可以构建实际的章节链接。例如，如果网站的结构是`/book/{bookId}/chapter/{chapterId}/page/{pageId}`，那么你可以这样构建链接：

```python
url = f"/book/{book_id}/chapter/{chapter_id}/page/{page_id}"
print(url)
```

输出将会是：

```
/book/1/chapter/3/page/7
```

这样，你就可以抓取并构建每一章节的链接了。

```
https://www.feynmanlectures.caltech.edu/I_03.html
```

随后发现，每一章节的路径遵循着一定的规律。例如，`I_03.html`代表的是第一卷的第三章。

```python
import requests
from bs4 import BeautifulSoup
from multiprocessing import Process
```

def scrape(chapter):
    if chapter < 1 or chapter > 52:
        raise Exception(f'章节 {chapter} 超出范围')
    chapter_str = '{:02d}'.format(chapter)
    url = f'https://www.feynmanlectures.caltech.edu/I_{chapter_str}.html'
    print(f'正在抓取 {url}')
    r = requests.get(url)
    if r.status_code != 200:
        raise Exception(r.status_code)
    soup = BeautifulSoup(r.text, features='lxml')
    f = open(f'./chapters/I_{chapter_str}.html', 'w')
    f.write(soup.prettify())
    f.close()

```python
def main():
    for i in range(52):
        p = Process(target=scrape, args=(i+1,))
        p.start()
        p.join()
        
main()
```

接下来，我将继续编写抓取代码。这里使用了`Process`。

```python
from multiprocessing import Process
import requests

def fetch_url(url):
    response = requests.get(url)
    print(f"URL: {url}, Status Code: {response.status_code}")

if __name__ == "__main__":
    urls = [
        "https://example.com",
        "https://example.org",
        "https://example.net"
    ]

    processes = []
    for url in urls:
        p = Process(target=fetch_url, args=(url,))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()
```

### 代码说明：
1. **`Process`**：我们使用`multiprocessing`模块中的`Process`类来创建多个进程，每个进程负责抓取一个URL。
2. **`fetch_url`函数**：这个函数负责发送HTTP请求并打印URL和响应的状态码。
3. **`urls`列表**：包含要抓取的URL列表。
4. **`processes`列表**：用于存储所有创建的进程对象。
5. **`start()`方法**：启动进程。
6. **`join()`方法**：等待所有进程完成。

### 运行结果：
每个URL的抓取任务会在独立的进程中执行，并输出相应的状态码。

```plaintext
URL: https://example.com, Status Code: 200
URL: https://example.org, Status Code: 200
URL: https://example.net, Status Code: 200
```

这个代码示例展示了如何使用多进程来并行抓取多个URL，从而提高抓取效率。

```shell
    raise RuntimeError('''
RuntimeError: 
        在當前進程完成其啟動階段之前，
        嘗試啟動一個新進程。
```

這可能意味著您沒有使用 fork 來啟動子進程，
並且在主模塊中忘記使用正確的慣用語法：

            if __name__ == '__main__':
                freeze_support()
                ...

如果程序不会被冻结以生成可执行文件，
        则可以省略“freeze_support()”这一行。
```

```python
def main():
    for i in range(52):        
        p = Process(target=scrape, args=(i+1,))
        p.start()
    p.join()
```

```python
if __name__ == "__main__":
    main()
```

```python
def main():
    start = timeit.default_timer()
    ps = [Process(target=scrape, args=(i+1,)) for i in range(52)]
    for p in ps:
        p.start()
    for p in ps:
        p.join()
    stop = timeit.default_timer()
    print('時間: ', stop - start)
```

```python
if __name__ == "__main__":    
    main()
```

```shell
正在抓取 https://www.feynmanlectures.caltech.edu/I_01.html
正在抓取 https://www.feynmanlectures.caltech.edu/I_04.html
...
正在抓取 https://www.feynmanlectures.caltech.edu/I_51.html
正在抓取 https://www.feynmanlectures.caltech.edu/I_52.html
耗时：9.144841699 秒
```

![图](assets/images/scrape/fig.png)

```html
<div class="figure" id="Ch1-F1">
        <img src="img/FLP_I/f01-01/f01-01_tc_big.svgz">
        <div class="caption empty">
         <span class="tag">
          圖1–1
         </span>
        </div>
</div>
```

```python
import requests
from bs4 import BeautifulSoup
from multiprocessing import Process
import timeit
```

def scrape(chapter):
    if chapter < 1 or chapter > 52:
        raise Exception(f'章节 {chapter} 超出范围')
    chapter_str = '{:02d}'.format(chapter)
    url = f'https://www.feynmanlectures.caltech.edu/I_{chapter_str}.html'
    print(f'正在抓取 {url}')
    r = requests.get(url)
    if r.status_code != 200:
        raise Exception(f'HTTP 状态码: {r.status_code}')
    soup = BeautifulSoup(r.text, features='lxml')
    f = open(f'./chapters/I_{chapter_str}.html', 'w')
    f.write(soup.prettify())
    f.close()

def main():
    start = timeit.default_timer()
    ps = [Process(target=scrape, args=(i+1,)) for i in range(52)]
    for p in ps:
        p.start()
    for p in ps:
        p.join()
    stop = timeit.default_timer()
    print('時間: ', stop - start)

```python
if __name__ == "__main__":    
    main()
```

查看链接。

```python
    imgs = soup.find_all('img')
    for img in imgs:
        print(img)
```

翻譯成繁體中文：

```python
    imgs = soup.find_all('img')
    for img in imgs:
        print(img)
```

這段程式碼的功能是從網頁中找出所有的圖片標籤（`<img>`），並逐一印出這些標籤的內容。

```html
正在抓取 https://www.feynmanlectures.caltech.edu/I_01.html
<img id="TwitLink" src=""/>
<img id="FBLink" src=""/>
<img id="MailLink" src=""/>
<img id="MobileLink" src=""/>
<img id="DarkModeLink" src=""/>
<img id="DesktopLink" src=""/>
<img src="img/camera.svg"/>
<img src="img/FLP_I/f01-00/f01-00.jpg"/>
<img data-src="img/FLP_I/f01-01/f01-01_tc_big.svgz"/>
<img data-src="img/FLP_I/f01-02/f01-02_tc_big.svgz"/>
<img data-src="img/FLP_I/f01-03/f01-03_tc_big.svgz"/>
<img data-src="img/FLP_I/f01-04/f01-04_tc_big.svgz"/>
<img data-src="img/FLP_I/f01-05/f01-05_tc_big.svgz"/>
<img data-src="img/FLP_I/f01-06/f01-06_tc_big.svgz"/>
<img class="first" data-src="img/FLP_I/f01-07/f01-07_tc_iPad_big_a.svgz"/>
<img class="last" data-src="img/FLP_I/f01-07/f01-07_tc_iPad_big_b.svgz"/>
<img data-src="img/FLP_I/f01-08/f01-08_tc_big.svgz"/>
<img data-src="img/FLP_I/f01-09/f01-09_tc_big.svgz"/>
<img data-src="img/FLP_I/f01-10/f01-10_tc_big.svgz"/>
```

https://www.feynmanlectures.caltech.edu/img/FLP_I/f01-01/f01-01_tc_big.svgz

```shell
禁止
```

您没有权限访问此资源。

Apache/2.4.38 (Debian) 服务器位于 www.feynmanlectures.caltech.edu 端口 443
```

```shell
% pip install selenium
正在收集 selenium
  使用緩存的 selenium-3.141.0-py2.py3-none-any.whl (904 kB)
要求已滿足：urllib3 在 /usr/local/lib/python3.9/site-packages (來自 selenium) (1.24.2)
正在安裝收集的套件：selenium
成功安裝 selenium-3.141.0
```

```shell
export CHROME_DRIVER_HOME=$HOME/dev-env/chromedriver
export PATH="${PATH}:${CHROME_DRIVER_HOME}"
```

翻譯成繁體中文：

```shell
export CHROME_DRIVER_HOME=$HOME/dev-env/chromedriver
export PATH="${PATH}:${CHROME_DRIVER_HOME}"
```

這段程式碼是設定環境變數的指令，用於指定 ChromeDriver 的安裝路徑，並將其加入到系統的 PATH 環境變數中，以便在終端中可以直接執行 ChromeDriver。

```shell
% chromedriver -h
用法：chromedriver [選項]
```

選項
  --port=PORT                     指定監聽的端口
  --adb-port=PORT                 指定adb服務器的端口
  --log-path=FILE                 將服務器日誌寫入文件而非標準錯誤輸出，並將日誌級別提升至INFO
  --log-level=LEVEL               設置日誌級別：ALL, DEBUG, INFO, WARNING, SEVERE, OFF
  --verbose                       詳細記錄日誌（等同於 --log-level=ALL）
  --silent                        不記錄任何日誌（等同於 --log-level=OFF）
  --append-log                    追加日誌到文件而非覆蓋
  --replayable                    （實驗性功能）詳細記錄日誌且不截斷長字符串，以便日誌可重播
  --version                       打印版本號並退出
  --url-base                      命令的基礎URL路徑前綴，例如wd/url
  --readable-timestamp            在日誌中添加可讀的時間戳
  --enable-chrome-logs            顯示瀏覽器的日誌（覆蓋其他日誌選項）
  --allowed-ips                   允許連接到ChromeDriver的遠程IP地址的逗號分隔白名單

```python
# 这是一个Python代码块的开始标记
```

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

```python
with webdriver.Chrome() as driver:
    wait = WebDriverWait(driver, 10)
    driver.get("https://google.com/ncr")
    driver.find_element(By.NAME, "q").send_keys("cheese" + Keys.RETURN)
    first_result = wait.until(presence_of_element_located((By.CSS_SELECTOR, "h3>div")))
    print(first_result.get_attribute("textContent"))
```

```python
```

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import urllib

```python
def main():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.feynmanlectures.caltech.edu/I_01.html")
    elements = driver.find_elements(By.TAG_NAME, "img")
    # print(dir(elements[0]))
    print(driver.page_source)
    i = 0
    for element in elements:
        # src = element.get_attribute('src')
        element.screenshot(f'images/{i}.png')        
        i +=1                
    driver.close()
main()
```

```python
from bs4 import BeautifulSoup
from multiprocessing import Process
import timeit
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
```

def img_path(chapter):
    return f'./chapters/{chapter}/img'

```python
def img_name(url):
    splits = url.split('/')
    last = splits[len(splits) - 1]
    parts = last.split('.')
    name = parts[0]
    return name
```

翻譯成繁體中文：

```python
def 圖片名稱(url):
    分割 = url.split('/')
    最後一段 = 分割[len(分割) - 1]
    部分 = 最後一段.split('.')
    名稱 = 部分[0]
    return 名稱
```

def download_images(driver: webdriver.Chrome, chapter):        
    # 生成图片保存路径
    path = img_path(chapter)
    # 创建目录，如果目录已存在则忽略
    Path(path).mkdir(parents=True, exist_ok=True)    
        
    # 查找所有图片元素
    elements = driver.find_elements(By.TAG_NAME, "img")    
    for element in elements:
        # 获取图片的src属性
        src = element.get_attribute('src')
        # 生成图片文件名
        name = img_name(src)
        # 截图并保存图片
        element.screenshot(f'{path}/{name}.png')

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, 类似 Gecko) 版本/14.0.3 Safari/605.1.15'

```python
def scrape(chapter):
    if chapter < 1 or chapter > 52:
        raise Exception(f'章节 {chapter} 超出范围')
    chapter_str = '{:02d}'.format(chapter)
    url = f'https://www.feynmanlectures.caltech.edu/I_{chapter_str}.html'
    driver = webdriver.Chrome()
    driver.get(url)
    page_source = driver.page_source        
    Path(f'./chapters/{chapter_str}').mkdir(parents=True, exist_ok=True)    
    print(f'正在抓取 {url}')
        
    download_images(driver, chapter_str)
        
    soup = BeautifulSoup(page_source, features='lxml')        
    imgs = soup.find_all('img')
    for img in imgs:
        if 'src' in img.attrs or 'data-src' in img.attrs:
            src = ''
            if 'src' in img.attrs:
                src = img.attrs['src']
            elif 'data-src' in img.attrs:
                src = img.attrs['data-src']
                del img.attrs['data-src']
            name = img_name(src)
            img.attrs['src'] = f'img/{name}.png'                
    
    f = open(f'./chapters/{chapter_str}/I_{chapter_str}.html', 'w')
    f.write(soup.prettify())
    f.close()
    
    driver.close()
```

def main():
    start = timeit.default_timer()
    ps = [Process(target=scrape, args=(i+1,)) for i in range(2)]
    for p in ps:
        p.start()
    for p in ps:
        p.join()
    stop = timeit.default_timer()
    print('時間: ', stop - start)

```python
if __name__ == "__main__":    
    main()
```
這段代碼的意思是，如果這個文件是作為主程序運行，而不是被其他模塊導入時，則執行`main()`函數。這是一種常見的Python編程慣例，用於區分模塊的導入和直接執行。

```shell
正在抓取 https://www.feynmanlectures.caltech.edu/I_01.html
正在抓取 https://www.feynmanlectures.caltech.edu/I_02.html
耗时：21.478510914999998 秒
```

```shell
errpipe_read, errpipe_write = os.pipe()
OSError: [Errno 24] 打开的文件过多
```

```shell
% ulimit a
ulimit: 無效的數字: a
lzw@lzwjava feynman-lectures-mobi % ulimit -a
-t: CPU 時間（秒）              無限制
-f: 檔案大小（區塊）            無限制
-d: 資料段大小（KB）            無限制
-s: 堆疊大小（KB）               8192
-c: 核心檔案大小（區塊）         0
-v: 位址空間（KB）              無限制
-l: 鎖定記憶體大小（KB）         無限制
-u: 程序數                       2784
-n: 檔案描述符數量               256
```

```shell
12
下載圖片
12
將MathJax轉換為SVG
LaTeXs 128
生成SVG 0
插入SVG 0
生成SVG 1
插入SVG 1
生成SVG 2
插入SVG 2
生成SVG 3
插入SVG 3
轉換
```

```shell
12
下載圖片
12
數學公式轉SVG
LaTeX 0
LaTeX 0
轉換
耗時：11.369145162秒
```

```shell
% grep --include=\*.html -r '\$' *
43/I_43.html:一段長時間 $T$ 內，會有某個次數，$N$，的碰撞。如果我們
43/I_43.html:碰撞次數與時間 $T$ 成正比。我們希望
43/I_43.html:我們將比例常數寫為 $1/\tau$，其中
43/I_43.html:$\tau$ 將具有時間的維度。常數 $\tau$ 是
43/I_43.html:有 $60$ 次碰撞；那麼 $\tau$ 就是一分鐘。我們會說
43/I_43.html:$\tau$（一分鐘）是
```

```shell
錯誤	E21018: 解析文件內容時，創建改進的 Mobi 域名失敗。內容：<In earlier chapters > 文件： /private/var/folders/_3/n3b7dq8x6652drmx6_d3t3bh0000gr/T/069e0b8a-f12e-4102-aed3-977c0c3c1178/cTemp/mTemp/mobi-GxL1ye/OEBPS/c-49.xhtml 行： 969
提醒	W28001: Kindle 閱讀器不支援內容中指定的 CSS 樣式。正在刪除 CSS 屬性： 'max-width' 文件： /private/var/folders/_3/n3b7dq8x6652drmx6_d3t3bh0000gr/T/069e0b8a-f12e-4102-aed3-977c0c3c1178/cTemp/mTemp/mobi-GxL1ye/OEBPS/stylesheet.css
提醒	W29004: 強制關閉的已開啟標籤為： <span amzn-src-id="985"> 文件： /private/var/folders/_3/n3b7dq8x6652drmx6_d3t3bh0000gr/T/069e0b8a-f12e-4102-aed3-977c0c3c1178/cTemp/mTemp/mobi-GxL1ye/OEBPS/c-4.xhtml     行： 0000102
提醒	W29004: 強制關閉的已開啟標籤為： <p amzn-src-id="975"> 文件： /private/var/folders/_3/n3b7dq8x6652drmx6_d3t3bh0000gr/T/069e0b8a-f12e-4102-aed3-977c0c3c1178/cTemp/mTemp/mobi-GxL1ye/OEBPS/c-4.xhtml     行： 0000102
```

```shell
提醒	W14001: 超連結出現問題，尚未解決：  /private/var/folders/_3/n3b7dq8x6652drmx6_d3t3bh0000gr/T/97c9cb4d-35f7-4920-81eb-4705325c482f/cTemp/mTemp/mobi-pvawPN/OEBPS/c-1.xhtml#Ch1-F1			
提醒	W14001: 超連結出現問題，尚未解決：  /private/var/folders/_3/n3b7dq8x6652drmx6_d3t3bh0000gr/T/97c9cb4d-35f7-4920-81eb-4705325c482f/cTemp/mTemp/mobi-pvawPN/OEBPS/c-1.xhtml#Ch1-F2			
提醒	W14001: 超連結出現問題，尚未解決：  /private/var/folders/_3/n3b7dq8x6652drmx6_d3t3bh0000gr/T/97c9cb4d-35f7-4920-81eb-4705325c482f/cTemp/mTemp/mobi-pvawPN/OEBPS/c-1.xhtml#Ch1-F3			
```

```html
<span class="disabled" href="#Ch1-F1">
          1–1
</span>
``` 

翻譯成繁體中文為：

```html
<span class="disabled" href="#Ch1-F1">
          1–1
</span>
``` 

在這個例子中，代碼本身並不需要翻譯，因為它是HTML標籤和屬性，這些是通用的程式語言元素。如果你需要翻譯的是頁面上的文字內容，那麼這裡的「1–1」是一個數字範圍，通常不需要翻譯，除非是在特定的上下文中需要轉換成中文表達方式。如果是在中文環境中，可能會保持不變，或者根據上下文翻譯成「第一章第一節」之類的表述。但由於這裡沒有提供足夠的上下文信息，我們保持原樣。

```shell
將 'OEBPS/84b8b4179175f097be1180a10089107be75d7d85.svg' 光柵化為 1264x1011
將 'OEBPS/23a4df37f269c8ed43f54753eb838b29cff538a1.svg' 光柵化為 1264x259
回溯（最近一次調用最後）：
  文件 "runpy.py"，第 194 行，在 _run_module_as_main 中
  文件 "runpy.py"，第 87 行，在 _run_code 中
  文件 "site.py"，第 39 行，在 <module> 中
  文件 "site.py"，第 35 行，在 main 中
  文件 "calibre/utils/ipc/worker.py"，第 216 行，在 main 中
  文件 "calibre/gui2/convert/gui_conversion.py"，第 41 行，在 gui_convert_override 中
  文件 "calibre/gui2/convert/gui_conversion.py"，第 28 行，在 gui_convert 中
  文件 "calibre/ebooks/conversion/plumber.py"，第 1274 行，在 run 中
  文件 "calibre/ebooks/conversion/plugins/mobi_output.py"，第 214 行，在 convert 中
  文件 "calibre/ebooks/conversion/plugins/mobi_output.py"，第 237 行，在 write_mobi 中
  文件 "calibre/ebooks/oeb/transforms/rasterize.py"，第 55 行，在 __call__ 中
  文件 "calibre/ebooks/oeb/transforms/rasterize.py"，第 142 行，在 rasterize_spine 中
  文件 "calibre/ebooks/oeb/transforms/rasterize.py"，第 152 行，在 rasterize_item 中
  文件 "calibre/ebooks/oeb/transforms/rasterize.py"，第 185 行，在 rasterize_external 中
  文件 "calibre/ebooks/oeb/base.py"，第 1092 行，在 bytes_representation 中
  文件 "calibre/ebooks/oeb/base.py"，第 432 行，在 serialize 中
TypeError: 無法將 'NoneType' 對象轉換為字節
```

```shell
% kindlepreviewer feynman-lectures-on-physics-volumn-1.epub -convert
正在檢查指定的參數。
預處理進行中。
正在處理 1/1 本書籍。
書籍已轉換，但有警告！: /Users/lzw/projects/feynman-lectures-mobi/feynman-lectures-on-physics-volumn-1.epub
後處理進行中。
將輸出/日誌文件寫入 /Users/lzw/projects/feynman-lectures-mobi/output
```

```shell
清理清單中...
從清單中修剪未使用的文件...
創建AZW3輸出...
序列化資源...
根據頁面斷點和流限制（如有）分割標記...
創建KF8輸出
	生成KF8標記...
標籤表沒有aid且塊大小過大。仍然添加。
標籤表沒有aid且塊大小過大。仍然添加。
標籤表沒有aid且塊大小過大。仍然添加。
	壓縮標記...
	創建索引...
```