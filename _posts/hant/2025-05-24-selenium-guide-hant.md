---
audio: false
generated: true
lang: hant
layout: post
title: Selenium 指南
translated: true
type: note
---

我將提供一份關於 Selenium 的完整指南，這是一個用於自動化網頁瀏覽器的熱門工具。本指南將涵蓋 Selenium 的元件、設定、基本用法、進階功能以及最佳實踐，包括 Python 程式碼範例。我將按照要求，將程式碼和關鍵部分包裹在指定的成品標籤中。

Selenium 是一個用於自動化網頁瀏覽器的開源框架，主要用於測試網頁應用程式，但也適用於網頁爬取和自動化任務。它支援多種瀏覽器（Chrome、Firefox、Safari、Edge 等）和程式語言（Python、Java、C#、Ruby、JavaScript 等）。

---

### Selenium 完整指南

#### 1. **什麼是 Selenium？**
Selenium 是一套專為自動化網頁瀏覽器設計的工具。它允許您與網頁元素互動、模擬使用者操作（點擊、輸入、導航）並驗證網頁應用程式的行為。Selenium 的主要元件包括：
- **Selenium WebDriver**：用於瀏覽器自動化的核心元件，提供以程式方式控制瀏覽器的 API。
- **Selenium IDE**：一個瀏覽器擴充功能，用於錄製和重播瀏覽器互動（主要適合初學者）。
- **Selenium Grid**：一個用於在多台機器或瀏覽器上並行執行測試的工具。

本指南重點介紹 **Selenium WebDriver** 與 Python 的結合使用，因為這是最廣泛使用的元件。

---

#### 2. **設定 Selenium**
要使用 Selenium 與 Python，您需要安裝必要的依賴項並設定瀏覽器驅動程式。

##### 先決條件
- Python（建議 3.6 或更高版本）
- 網頁瀏覽器（例如 Chrome、Firefox）
- 對應的瀏覽器驅動程式（例如 ChromeDriver 用於 Chrome，GeckoDriver 用於 Firefox）
- Selenium Python 套件

##### 安裝步驟
1. **安裝 Python**：確保 Python 已安裝並添加到系統的 PATH 中。
2. **安裝 Selenium**：
   在終端機中執行以下指令：
   ```bash
   pip install selenium
   ```
3. **下載瀏覽器驅動程式**：
   - 對於 Chrome：從 [chromedriver.chromium.org](https://chromedriver.chromium.org/downloads) 下載 ChromeDriver。確保版本與您安裝的 Chrome 瀏覽器相符。
   - 對於 Firefox：從 [github.com/mozilla/geckodriver](https://github.com/mozilla/geckodriver/releases) 下載 GeckoDriver。
   - 將驅動程式執行檔置於系統 PATH 包含的目錄中，或在程式碼中指定其路徑。
4. **驗證安裝**：
   建立一個簡單的腳本來測試 Selenium 設定。

```python
from selenium import webdriver

# 初始化 Chrome WebDriver
driver = webdriver.Chrome()
# 開啟一個網站
driver.get("https://www.example.com")
# 列印頁面標題
print(driver.title)
# 關閉瀏覽器
driver.quit()
```

執行該腳本。如果瀏覽器開啟、導航至 `example.com` 並列印頁面標題，則表示設定成功。

---

#### 3. **Selenium WebDriver 的核心概念**
Selenium WebDriver 提供了一個用於與網頁元素互動的 API。關鍵概念包括：

- **WebDriver**：控制瀏覽器實例的介面（例如，`webdriver.Chrome()` 用於 Chrome）。
- **WebElement**：表示網頁上的 HTML 元素（例如，按鈕、輸入欄位）。
- **定位器**：用於尋找元素的方法（例如，按 ID、名稱、類別、XPath、CSS 選擇器）。
- **操作**：與元素互動的方法（例如，點擊、傳送按鍵、取得文字）。

##### 常用定位器
Selenium 使用定位器來識別網頁上的元素：
- `find_element_by_id("id")`：透過 ID 尋找元素。
- `find_element_by_name("name")`：透過名稱屬性尋找元素。
- `find_element_by_class_name("class")`：透過類別名稱尋找元素。
- `find_element_by_tag_name("tag")`：透過 HTML 標籤尋找元素。
- `find_element_by_css_selector("selector")`：使用 CSS 選擇器尋找元素。
- `find_element_by_xpath("xpath")`：使用 XPath 表達式尋找元素。
- `find_elements_*`：傳回所有符合元素的列表（例如，`find_elements_by_tag_name`）。

##### 基本互動
- `click()`：點擊元素。
- `send_keys("text")`：在輸入欄位中輸入文字。
- `text`：擷取元素的文字內容。
- `get_attribute("attribute")`：取得元素屬性的值（例如，`value`、`href`）。
- `is_displayed()`、`is_enabled()`、`is_selected()`：檢查元素狀態。

---

#### 4. **編寫基本的 Selenium 腳本**
以下是一個自動化登入網站的範例腳本（使用假設的登入頁面進行示範）。

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 初始化 Chrome WebDriver
driver = webdriver.Chrome()

try:
    # 導航至登入頁面
    driver.get("https://example.com/login")
    
    # 尋找使用者名稱和密碼欄位
    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")
    
    # 輸入憑證
    username.send_keys("testuser")
    password.send_keys("testpassword")
    
    # 提交表單
    password.send_keys(Keys.RETURN)
    
    # 等待頁面載入
    time.sleep(2)
    
    # 驗證登入成功（檢查歡迎訊息）
    welcome_message = driver.find_element(By.CLASS_NAME, "welcome").text
    print(f"登入成功！歡迎訊息：{welcome_message}")
    
except Exception as e:
    print(f"發生錯誤：{e}")
    
finally:
    # 關閉瀏覽器
    driver.quit()
```

**注意事項**：
- 將 `"https://example.com/login"` 替換為目標網站的實際 URL。
- 根據網站的 HTML 結構調整元素定位器（`By.ID`、`By.CLASS_NAME`）。
- `time.sleep(2)` 是一個簡單的等待方式；在生產環境中，請使用顯式等待（稍後介紹）。

---

#### 5. **進階功能**
Selenium 提供了用於穩健自動化的進階功能。

##### a. **等待機制**
Selenium 提供兩種類型的等待來處理動態網頁：
- **隱式等待**：為所有元素搜尋設定預設等待時間。
  ```python
  driver.implicitly_wait(10)  # 最多等待 10 秒讓元素出現
  ```
- **顯式等待**：等待特定條件（例如，元素可點擊）。

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 初始化 Chrome WebDriver
driver = webdriver.Chrome()

try:
    driver.get("https://example.com")
    
    # 等待直到元素可點擊（最多 10 秒）
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "submit-button"))
    )
    button.click()
    
    print("按鈕點擊成功！")
    
except Exception as e:
    print(f"發生錯誤：{e}")
    
finally:
    driver.quit()
```

##### b. **處理警示框**
Selenium 可以與 JavaScript 警示框、確認框和提示框互動：
```python
alert = driver.switch_to.alert
alert.accept()  # 點擊確定
alert.dismiss()  # 點擊取消
alert.send_keys("text")  # 在提示框中輸入文字
```

##### c. **導航框架和視窗**
- **框架/內嵌框架**：切換到框架以與其元素互動。
  ```python
  driver.switch_to.frame("frame-id")
  driver.switch_to.default_content()  # 返回主內容
  ```
- **視窗/分頁**：處理多個瀏覽器視窗。
  ```python
  original_window = driver.current_window_handle
  for window_handle in driver.window_handles:
      driver.switch_to.window(window_handle)
  ```

##### d. **執行 JavaScript**
直接在瀏覽器中執行 JavaScript 程式碼：
```python
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # 滾動至底部
```

##### e. **截圖**
擷取截圖用於除錯或文件記錄：
```python
driver.save_screenshot("screenshot.png")
```

---

#### 6. **使用無頭瀏覽器的 Selenium**
無頭瀏覽器在沒有圖形使用者介面的情況下執行，適合 CI/CD 管道或伺服器。
在無頭模式下使用 Chrome 的範例：

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 設定無頭模式的 Chrome 選項
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

# 在無頭模式下初始化 Chrome WebDriver
driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get("https://www.example.com")
    print(f"頁面標題：{driver.title}")
    
except Exception as e:
    print(f"發生錯誤：{e}")
    
finally:
    driver.quit()
```

---

#### 7. **最佳實踐**
- **使用顯式等待**：對於動態頁面，避免使用 `time.sleep()`；使用帶有 `expected_conditions` 的 `WebDriverWait`。
- **處理異常**：將程式碼包裹在 `try-except` 區塊中，以優雅地處理錯誤。
- **關閉 WebDriver**：始終呼叫 `driver.quit()` 來關閉瀏覽器並釋放資源。
- **組織定位器**：將定位器儲存在單獨的檔案或類別中，以便維護。
- **使用頁面物件模型 (POM)**：將頁面互動封裝在類別中，以提高程式碼的可重用性。

頁面物件模型範例：

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, "username")
        self.password_field = (By.ID, "password")
        self.submit_button = (By.ID, "submit-button")
    
    def login(self, username, password):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.username_field)
        ).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.submit_button).click()

# 使用方式
from selenium import webdriver

driver = webdriver.Chrome()
login_page = LoginPage(driver)
try:
    driver.get("https://example.com/login")
    login_page.login("testuser", "testpassword")
except Exception as e:
    print(f"發生錯誤：{e}")
finally:
    driver.quit()
```

---

#### 8. **Selenium Grid**
Selenium Grid 允許在多個瀏覽器、作業系統或機器上並行執行測試。它由一個 **hub**（中央伺服器）和 **nodes**（執行瀏覽器的機器）組成。
- **設定**：使用 Selenium Grid 的 JAR 檔案或 Docker 配置 hub 和 nodes。
- **使用案例**：測試跨瀏覽器相容性（例如，Windows 上的 Chrome，Linux 上的 Firefox）。
- **範例**：連接到遠端 WebDriver：
  ```python
  from selenium.webdriver.remote.webdriver import WebDriver
  driver = WebDriver(command_executor="http://hub-ip:4444/wd/hub", desired_capabilities={"browserName": "chrome"})
  ```

---

#### 9. **常見挑戰與解決方案**
- **找不到元素**：使用顯式等待或透過瀏覽器開發者工具驗證定位器。
- **過時元素參考**：在頁面重新整理或 DOM 變更後重新定位元素。
- **效能緩慢**：優化定位器（優先使用 ID/CSS 而非 XPath）並使用無頭模式。
- **動態內容**：使用 JavaScript 執行或等待來處理 AJAX 載入的內容。

---

#### 10. **資源**
- 官方文件：[selenium.dev](https://www.selenium.dev/documentation/)
- Python Selenium 綁定：[selenium-python.readthedocs.io](https://selenium-python.readthedocs.io/)
- 瀏覽器驅動程式：ChromeDriver、GeckoDriver
- 社群：Stack Overflow、X 貼文（搜尋 #Selenium 或 #WebDriver）

---

本指南涵蓋了 Selenium WebDriver 的基礎知識，從設定到進階用法。如果您需要有關特定 Selenium 任務或更進階範例的幫助，請告訴我！