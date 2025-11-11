---
audio: false
generated: true
lang: hant
layout: post
title: Selenium 腳本
translated: true
type: note
---

以下是一個使用 Python 編寫的進階 Selenium 腳本範例，展示了包括頁面物件模型 (POM)、用於響應式佈局的明確 FacetGrid、明確等待、處理動態內容和錯誤處理等高級功能。該腳本自動化了一個複雜場景：從電子商務網站抓取產品數據，在多個頁面之間導航，並生成摘要報告。此範例假設了一個用於演示的虛構電子商務網站，但這些概念可以應用於實際網站。

此範例展示了：
- **頁面物件模型 (POM)**，用於組織和維護程式碼。
- **明確等待**，用於處理動態內容。
- **FacetGrid**，用於響應式表格處理。
- **無頭瀏覽器**，以提高執行效率。
- **數據處理**，以生成 JSON 報告。
- **錯誤處理**，以增強穩健性。

```python
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import Select
import time

# 產品列表頁的頁面物件
class ProductListingPage:
    def __init__(self, driver):
        self.driver = driver
        self.product_cards = (By.CLASS_NAME, "product-card")
        self.product_name = (By.CLASS_NAME, "product-name")
        self.product_price = (By.CLASS_NAME, "product-price")
        self.next_page_button = (By.ID, "next-page")
        self.sort_dropdown = (By.ID, "sort-options")

    def sort_by_price(self):
        try:
            sort_select = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.sort_dropdown)
            )
            select = Select(sort_select)
            select.select_by_value("price-asc")
            time.sleep(2)  # 等待排序應用
        except TimeoutException:
            print("未找到排序下拉選單或等待超時")

    def get_products(self):
        try:
            cards = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located(self.product_cards)
            )
            products = []
            for card in cards:
                name = card.find_element(*self.product_name).text
                price = card.find_element(*self.product_price).text
                products.append({"name": name, "price": price})
            return products
        except (TimeoutException, NoSuchElementException) as e:
            print(f"檢索產品時出錯: {e}")
            return []

    def go_to_next_page(self):
        try:
            next_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.next_page_button)
            )
            next_button.click()
            time.sleep(2)  # 等待頁面載入
            return True
        except TimeoutException:
            print("未找到下一頁按鈕或等待超時")
            return False

# 搜尋頁面的頁面物件
class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_input = (By.ID, "search-bar")
        self.search_button = (By.ID, "search-submit")

    def search(self, query):
        try:
            search_box = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.search_input)
            )
            search_box.clear()
            search_box.send_keys(query)
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.search_button)
            ).click()
            time.sleep(2)  # 等待搜尋結果
        except TimeoutException as e:
            print(f"搜尋失敗: {e}")

# 主腳本
def scrape_ecommerce_site():
    # 設定無頭 Chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=chrome_options)
    all_products = []

    try:
        # 導航到網站
        driver.get("https://example.com")
        
        # 初始化頁面物件
        search_page = SearchPage(driver)
        product_page = ProductListingPage(driver)
        
        # 執行搜尋
        search_page.search("laptop")
        
        # 按價格排序
        product_page.sort_by_price()
        
        # 抓取多個頁面
        page_count = 0
        max_pages = 3  # 演示限制
        
        while page_count < max_pages:
            products = product_page.get_products()
            all_products.extend(products)
            print(f"已抓取第 {page_count + 1} 頁: {len(products)} 個產品")
            
            if not product_page.go_to_next_page():
                break
            page_count += 1

        # 生成摘要
        summary = {
            "total_products": len(all_products),
            "average_price": calculate_average_price(all_products),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        
        # 將結果儲存為 JSON
        with open("product_data.json", "w") as f:
            json.dump({"products": all_products, "summary": summary}, f, indent=2)
        print("結果已儲存至 product_data.json")

    except Exception as e:
        print(f"發生錯誤: {e}")
    
    finally:
        driver.quit()

def calculate_average_price(products):
    if not products:
        return 0
    prices = []
    for product in products:
        try:
            price_str = product["price"].replace("$", "").replace(",", "")
            prices.append(float(price_str))
        except (ValueError, AttributeError):
            continue
    return sum(prices) / len(prices) if prices else 0

if __name__ == "__main__":
    scrape_ecommerce_site()
```

### 範例說明
1. **頁面物件模型 (POM)**:
   - 腳本使用兩個頁面物件類別 (`SearchPage` 和 `ProductListingPage`) 來封裝特定頁面的邏輯，使程式碼模組化且易於維護。
   - 每個類別包含用於與特定頁面元素互動的定位器和方法。

2. **無頭瀏覽器**:
   - 腳本在無頭模式下運行 Chrome 以提高效率，適用於 CI/CD 流水線或伺服器。

3. **明確等待**:
   - 使用 `WebDriverWait` 和 `expected_conditions` 來處理動態內容，確保在互動前元素存在或可點擊。

4. **響應式表格處理**:
   - 腳本使用類似 FacetGrid 的邏輯來抓取產品列表表格，從每個卡片中提取產品名稱和價格。
   - 它通過在多個頁面之間導航來處理分頁（此範例最多 3 頁）。

5. **錯誤處理**:
   - 腳本捕獲 `TimeoutException` 和 `NoSuchElementException` 以優雅地處理缺失元素或超時。
   - `try-finally` 區塊確保即使發生錯誤也會關閉瀏覽器。

6. **數據處理**:
   - 抓取的數據儲存在字典列表中並進行摘要（例如，產品總數、平均價格）。
   - 結果儲存到 JSON 檔案 (`product_data.json`) 以供進一步使用。

7. **動態排序**:
   - 腳本與下拉選單互動以按價格對產品進行排序，模擬真實用戶行為。

### 輸出
腳本生成一個 JSON 檔案 (`product_data.json`)，結構如下：
```json
{
  "products": [
    {"name": "Laptop Model A", "price": "$999.99"},
    {"name": "Laptop Model B", "price": "$1299.99"},
    ...
  ],
  "summary": {
    "total_products": 30,
    "average_price": 1099.45,
    "timestamp": "2025-05-24 21:33:00"
  }
}
```

### 注意事項
- **網站適應**: 定位器 (`By.ID`, `By.CLASS_NAME`) 和 URL (`https://example.com`) 是佔位符。請將它們替換為目標網站 HTML 結構中的實際值，您可以使用瀏覽器開發者工具進行檢查。
- **依賴項**: 確保已安裝 `selenium` (`pip install selenium`) 並且適當的瀏覽器驅動程式（例如 ChromeDriver）在您的 PATH 中。
- **改進建議**:
  - 添加日誌記錄以便更好地調試。
  - 為不穩定的網絡請求實施重試邏輯。
  - 使用配置檔案來管理定位器和設定。
  - 擴展以處理更複雜的場景，如身份驗證或 CAPTCHA。

### 運行腳本
1. 安裝依賴項: `pip install selenium`。
2. 下載並配置 ChromeDriver。
3. 將 URL 和定位器替換為真實電子商務網站（例如 Amazon、eBay）的對應值。
4. 運行腳本: `python advanced_selenium_ecommerce_scraper.py`。

此範例展示了一個符合生產就緒標準的 Selenium 腳本，並遵循最佳實踐。如果您需要幫助將其適應特定網站或添加如身份驗證或使用 Selenium Grid 進行並行執行等功能，請告訴我！