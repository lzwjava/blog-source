---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: Selenium 網頁爬取代碼解析
translated: true
type: note
---

### 程式碼中 Selenium API 使用說明

此 Python 腳本使用 **Selenium WebDriver** 函式庫來自動化網頁瀏覽器（特別是 Chrome），以便與網站（可能是位於 `https://xxdata.com/index.aspx` 的數據/貿易入口網站）進行互動。目標似乎是進行網頁爬取：登入、搜尋貿易/訂單數據（使用像 '8449' 這樣的 HS 編碼）、在分頁結果中導航、點擊詳細資料、從 HTML 表格中提取結構化數據，並將其儲存到 SQLite 資料庫 (`data.db`) 中。

此處使用 Selenium 是為了**瀏覽器自動化**，允許腳本模擬人類的互動行為，如輸入、點擊、滾動和等待頁面載入——這些行為僅使用簡單的 HTTP 請求（例如，由於 JavaScript 繁重的頁面、iframe 或動態內容）很難或不可能實現。它能處理動態網頁元素、會話以及多視窗/iframe 切換，這些在現代網路應用程式中很常見。

我將**逐節**分解，重點介紹關鍵的 Selenium API、它們的用途以及如何使用它們。請注意：程式碼中的某些方法（例如 `find_element_by_css_selector`）來自舊版 Selenium（4.0 之前），現已棄用。在現代 Selenium (4+) 中，您應改用 `find_element(By.CSS_SELECTOR, ...)`，但功能是相同的。該腳本還導入了等待、異常和元素處理所需的必要模組。

#### 1. **導入與設定 (Selenium 初始化)**
   ```python
   from selenium import webdriver
   from selenium.webdriver.chrome.webdriver import WebDriver
   from selenium.webdriver.common.keys import Keys
   from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, StaleElementReferenceException
   from selenium.webdriver.support.ui import WebDriverWait
   from selenium.webdriver.support import expected_conditions as EC
   from selenium.webdriver.common.by import By
   from selenium.webdriver.remote.webelement import WebElement
   ```
   - **目的**：這些導入核心的 Selenium 組件：
     - `webdriver`：控制瀏覽器的主要模組。
     - `WebDriver`：瀏覽器實例的類型提示（確保類型安全）。
     - `Keys`：用於模擬鍵盤輸入（例如 Page Up）。
     - 異常：處理常見錯誤，如超時或過時元素（頁面刷新後發生變化的元素）。
     - `WebDriverWait` 和 `EC` (Expected Conditions)：用於顯式等待——輪詢直到元素滿足條件（例如，在頁面上存在）。
     - `By`：定位策略（例如 CSS 選擇器、ID、標籤名稱）以查找元素。
     - `WebElement`：表示用於互動的 HTML 元素。

   在 `run()` 函式中：
   ```python
   options = webdriver.ChromeOptions()
   options.add_argument("--start-maximized")  # 以全螢幕模式開啟瀏覽器。
   options.add_argument('--log-level=3')      # 抑制控制台日誌輸出，使輸出更簡潔。
   browser: WebDriver = webdriver.Chrome(executable_path="./chromedriver", options=options)
   ```
   - **使用的 Selenium API**：`webdriver.Chrome(options=...)`
     - 使用本地的 `chromedriver` 可執行文件（必須位於腳本目錄中）初始化 Chrome 瀏覽器實例。
     - `ChromeOptions`：自定義瀏覽器會話（例如，可以添加 `options.add_argument("--headless")` 以在後台運行無頭模式）。
     - 這會創建一個實時的、可控制的瀏覽器視窗。Selenium 充當 Python 和瀏覽器 DevTools 協議之間的橋樑。

   ```python
   browser.get('https://xxdata.com/index.aspx')
   ```
   - **使用的 Selenium API**：`WebDriver.get(url)`
     - 導航到起始 URL，像使用者在地址欄中輸入一樣載入頁面。

#### 2. **登入流程**
   ```python
   input_username = browser.find_element_by_css_selector('input[name=username]')
   input_username.send_keys('name')
   input_password = browser.find_element_by_css_selector('input[name=password]')
   input_password.send_keys('password')
   btn_login = browser.find_element_by_css_selector('div.login-check')
   btn_login.click()
   ```
   - **使用的 Selenium APIs**：
     - `WebDriver.find_element_by_css_selector(css)` (已棄用；現代寫法：`find_element(By.CSS_SELECTOR, css)`)：使用 CSS 選擇器（例如，通過屬性如 `name="username"`）定位單個 HTML 元素。返回一個 `WebElement`。
     - `WebElement.send_keys(text)`：模擬在輸入欄位中輸入文字（例如，使用者名稱/密碼）。
     - `WebElement.click()`：模擬在按鈕或連結上的滑鼠點擊。
   - **Selenium 的使用方式**：自動化表單提交。沒有 Selenium，您需要反向工程 POST 請求，但這可以無縫處理 JavaScript 驗證或動態表單。憑證是硬編碼的（在生產環境中不安全——請使用環境變數）。

   登入後：
   ```python
   wait_element(browser, 'div.dsh_01')
   ```
   - 呼叫自定義的 `wait_element` 函式（如下所述）暫停，直到儀表板載入完畢。

#### 3. **導航與搜尋**
   ```python
   trade_div = browser.find_element_by_css_selector('div.dsh_01')
   trade_div.click()
   wait_element(browser, 'a.teq_icon')
   teq = browser.find_element_by_css_selector('a.teq_icon')
   teq.click()
   wait_element(browser, 'div.panel-body')
   iframe = browser.find_element_by_css_selector('div.panel-body > iframe')
   iframe_id = iframe.get_attribute('id')
   browser.switch_to.frame(iframe_id)
   ```
   - **使用的 Selenium APIs**：
     - `find_element_by_css_selector`：定位導航元素（例如，儀表板 div、圖示連結）。
     - `WebElement.click()`：點擊以進行導航（例如，到「貿易」部分）。
     - `WebElement.get_attribute('id')`：檢索 HTML 屬性（此處是 iframe 的 ID）。
     - `WebDriver.switch_to.frame(frame_id)`：將驅動程式上下文切換到 `<iframe>`（在應用程式中嵌入內容時很常見）。沒有這個，iframe 內部的元素將無法訪問。
   - **Selenium 的使用方式**：處理多步驟導航和嵌入式內容。Iframe 隔離了 DOM，因此切換對於爬取內部頁面至關重要。

   搜尋過程：
   ```python
   input_search = browser.find_element_by_id('_easyui_textbox_input7')  # 使用 ID 定位器。
   input_search.send_keys('8449')
   time.sleep(10)
   enter = browser.find_element_by_css_selector('a#btnOk > div.enter-bt')
   enter.click()
   ```
   - **使用的 Selenium APIs**：
     - `find_element_by_id(id)` (已棄用；現代寫法：`find_element(By.ID, id)`)：通過 HTML `id` 屬性定位。
     - `send_keys`：輸入搜尋查詢（產品的 HS 編碼）。
     - `time.sleep(10)`：隱式等待（較粗糙；最好使用顯式等待）。
     - `click()`：提交搜尋。
   - **Selenium 的使用方式**：模擬使用者搜尋。`time.sleep` 暫停以等待 AJAX/JavaScript 載入結果。

#### 4. **分頁與結果處理**
   ```python
   result_count_span = browser.find_element_by_css_selector('span#ResultCount')
   page = math.ceil(int(result_count_span.text) / 20)  # 計算總頁數（每頁 20 個結果）。
   skip = 0
   page = page - skip

   for p in range(page):
       input_page = browser.find_element_by_css_selector('input.laypage_skip')
       input_page.send_keys(str(p + skip + 1))
       btn_confirm = browser.find_element_by_css_selector('button.laypage_btn')
       btn_confirm.click()
       time.sleep(2)

       locates = browser.find_elements_by_css_selector('div.rownumber-bt')  # 多個元素。
       print('page ' + str(p) + ' size: ' + str(len(locates)))
       for locate in locates:
           browser.execute_script("arguments[0].scrollIntoView();", locate)  # JavaScript 滾動。
           time.sleep(1)
           browser.find_element_by_tag_name('html').send_keys(Keys.PAGE_UP)  # 鍵盤滾動。
           time.sleep(1)
           try:
               locate.click()
           except ElementClickInterceptedException:
               print('ElementClickInterceptedException')
               continue
           except StaleElementReferenceException:
               print('StaleElementReferenceException')
               continue
           # ... (更多內容如下)
   ```
   - **使用的 Selenium APIs**：
     - `find_element_by_css_selector`：從 span 獲取結果計數。
     - `WebElement.text`：從元素中提取可見文字（例如，像 "100" 這樣的計數）。
     - `find_elements_by_css_selector` (複數；已棄用：`find_elements(By.CSS_SELECTOR, ...)`)：查找多個元素（例如，頁面上的行連結）。返回一個 `WebElement` 列表。
     - `WebDriver.execute_script(js_code, *args)`：在瀏覽器中運行自定義 JavaScript（此處，將元素滾動到視圖中以避免點擊問題）。
     - `WebDriver.find_element_by_tag_name('html').send_keys(Keys.PAGE_UP)`：模擬鍵盤滾動（使用 `Keys` 枚舉）。
     - 異常：捕獲點擊失敗（例如，疊加層阻擋點擊）或過時元素（DOM 已刷新，使引用無效——在動態 UI 中很常見）。
   - **Selenium 的使用方式**：通過輸入頁碼並點擊「前往」來自動化分頁。對於每個結果行 (`div.rownumber-bt`)，它會滾動以確保可見性，然後點擊以在新視窗中打開詳細資料。這處理了懶加載或類似無限滾動的行為。

#### 5. **視窗/Iframe 切換與數據提取**
   從循環繼續：
   ```python
   time.sleep(1)
   browser.switch_to.window(browser.window_handles[1])  # 切換到新分頁/視窗。
   wait_element(browser, 'div#content')
   try:
       save_page(browser)
   except IndexError:
       print('IndexError')
       continue
   browser.close()  # 關閉詳細資料視窗。
   browser.switch_to.window(browser.window_handles[0])  # 返回主視窗。
   browser.switch_to.frame(iframe_id)  # 返回 iframe 上下文。
   ```
   - **使用的 Selenium APIs**：
     - `WebDriver.window_handles`：已開啟視窗/分頁 ID 的列表。
     - `WebDriver.switch_to.window(handle)`：將焦點切換到特定視窗（索引 0 = 主視窗，1 = 點擊開啟的新分頁）。
     - `WebDriver.close()`：關閉目前視窗。
   - **Selenium 的使用方式**：點擊在新分頁中打開詳細資料，因此它切換上下文以進行爬取，然後返回。這對於多分頁應用程式至關重要。

#### 6. **在 `save_page(browser: WebDriver)` 函式中的數據提取**
   這是核心的爬取邏輯：
   ```python
   ts = browser.find_elements_by_css_selector('table')  # 頁面上的所有表格。
   t0 = ts[0]
   tds0 = t0.find_elements_by_tag_name('td')  # 第一個表格中的 TD 儲存格。
   order_number = tds0[2].text  # 從特定儲存格提取文字。
   # ... (對其他表格 t1, t2 等類似操作)
   ```
   - **使用的 Selenium APIs**：
     - `find_elements_by_css_selector('table')` / `find_elements_by_tag_name('td')` (已棄用：使用 `By.TAG_NAME`)：查找所有 `<table>` 及其 `<td>` 儲存格。
     - `WebElement.text`：從儲存格中提取文字內容（例如，訂單編號、進口商名稱）。
     - 自定義 `tds_to_text(tds: list[WebElement])`：串接配對 `<td>` 的文字（例如，標籤 + 值）。
   - **Selenium 的使用方式**：解析頁面的 DOM 結構（包含訂單/進口商/出口商詳細資料的表格）。它處理可變的表格數量（例如，如果 `len(ts) == 8`，則存在額外表格）。然後將數據插入 SQLite（非 Selenium 部分）。

   條件邏輯根據表格索引提取字段，如 `order_number`、`importer`、`exporter` 等——假設佈局是固定的。

#### 7. **等待與錯誤處理 (`wait_element` 函式)**
   ```python
   def wait_element(browser, css):
       timeout = 30
       try:
           element_present = EC.presence_of_element_located((By.CSS_SELECTOR, css))
           WebDriverWait(browser, timeout).until(element_present)
       except TimeoutException:
           print('Timed out waiting for page to load')
   ```
   - **使用的 Selenium APIs**：
     - `expected_conditions.presence_of_element_located(locator)`：等待元素存在於 DOM 中（不一定可見）。
     - `WebDriverWait(driver, timeout).until(condition)`：在 30 秒內每隔 0.5 秒輪詢一次條件。
     - `TimeoutException`：如果等待失敗則引發。
   - **Selenium 的使用方式**：防止競爭條件（例如，在頁面載入前點擊）。比 `time.sleep` 更好，因為它是針對特定元素的並且效率更高。

#### 8. **清理**
   ```python
   time.sleep(1000)  # 長時間暫停（用於除錯？）。
   browser.quit()    # 關閉瀏覽器並結束會話。
   ```
   - **使用的 Selenium API**：`WebDriver.quit()`：終止驅動程式，關閉所有視窗並釋放資源。

#### Selenium 的整體作用
- **自動化流程**：Selenium 啟動一個真實的瀏覽器，載入頁面，通過 DOM 查詢（如 CSS/ID 定位器）進行互動，並處理動態行為（JS 執行、等待、切換）。它非常適合 SPA 或具有會話/Cookie 的受保護網站。
- **此處的優勢**：處理登入狀態、iframe、新分頁和滾動——僅使用 BeautifulSoup/Requests 等爬取工具無法單獨完成此操作。
- **程式碼中的限制/問題**：
  - 已棄用的定位器：更新為使用 `By` 以面向未來。
  - 硬編碼的睡眠：更多地替換為等待以加速/減少不穩定性。
  - 異常：處理得很好，但可以在 StaleElement 上重試。
  - 道德/合法性：爬取可能違反條款；添加 user-agent 標頭或代理以模擬人類。
  - 效能：以有頭模式運行（可見瀏覽器）；在生產環境中改為無頭模式。
- **運行它**：需要 ChromeDriver（從 Selenium 網站下載，匹配 Chrome 版本）。通過 `pip install selenium` 安裝 Selenium。

如果您對特定部分、現代化程式碼或除錯有疑問，請告訴我！