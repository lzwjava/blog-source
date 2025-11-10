---
audio: false
generated: true
lang: hant
layout: post
title: 繞過 Cloudflare 的 Selenium 腳本
translated: true
type: note
---

您的 Selenium 腳本設計用於透過 Firefox 和特定設定檔與 "https://grok.com" 互動，但遇到了 Cloudflare 的機器人檢測挑戰，特別是「驗證您是人類」的核取方塊。即使點擊了核取方塊，腳本似乎仍難以通過驗證，無法存取主要內容（例如文字區域）。Cloudflare 採用複雜的方法來檢測自動化瀏覽器，例如 HTTP 標頭分析、TLS 指紋辨識和行為檢查，這使得僅使用 Selenium 繞過此挑戰變得棘手。然而，您可以在當前的 Firefox 設定下嘗試一些策略來通過 Cloudflare 測試。以下是兩種針對您腳本的實用方法，如果這些方法無效，後面還提供了其他考量。

---

### **方法 1：重複使用設定檔手動完成挑戰**
由於您的腳本使用特定的 Firefox 設定檔 (`/home/lzw/.mozilla/firefox/wzfodx6v.default`)，您可以利用此設定檔在手動通過 Cloudflare 挑戰後儲存工作階段資料。操作步驟如下：

1. **手動開啟 Firefox 並使用該設定檔**：
   - 使用腳本中指定的相同設定檔啟動 Firefox。您可以透過指令行操作：
     ```bash
     firefox --profile "/home/lzw/.mozilla/firefox/wzfodx6v.default"
     ```
   - 或者，使用 Firefox 的設定檔管理員 (`firefox --ProfileManager`) 選擇 `wzfodx6v.default`。

2. **導航並通過挑戰**：
   - 在瀏覽器中前往 "https://grok.com"。
   - 當出現 Cloudflare 的「驗證您是人類」核取方塊提示時，點擊它並完成任何出現的額外驗證步驟。
   - 等待直到進入主頁面（例如，看到帶有 `aria-label="Ask Grok anything"` 的文字區域）。

3. **關閉瀏覽器**：
   - 退出 Firefox 以確保設定檔儲存工作階段 Cookie，包括任何 Cloudflare 的驗證通關令牌（例如 `cf_clearance`）。

4. **執行您的 Selenium 腳本**：
   - 照常執行您的腳本。由於它使用相同的設定檔，它應該會繼承儲存的 Cookie 和工作階段資料，從而有可能繞過挑戰。

**為何此方法可能有效**：Cloudflare 通常依賴 Cookie 來記住瀏覽器已通過測試。透過手動預先驗證設定檔，您的自動化工作階段可能會被視為已驗證訪問的延續。

**限制**：如果 Cloudflare 在每次頁面載入時執行額外檢查（例如，檢測 Selenium 的自動化指紋），此方法可能會失敗。在這種情況下，請嘗試下一種方法。

---

### **方法 2：在腳本中提取並設定 Cookie**
如果重複使用設定檔無效，您可以在通過挑戰後手動提取 Cookie 並將其注入到 Selenium 驅動程式中。逐步流程如下：

1. **手動通過挑戰**：
   - 遵循方法 1 的步驟 1 和 2，以到達 "https://grok.com" 的主頁面。

2. **提取 Cookie**：
   - 開啟 Firefox 的開發者工具（F12 或右鍵點擊 > 檢查）。
   - 前往 **Storage** 標籤（或 **Network** 標籤，然後重新載入頁面以檢查 Cookie）。
   - 尋找與 `.grok.com` 相關的 Cookie，特別是 `cf_clearance`（Cloudflare 的驗證 Cookie）。
   - 記下每個相關 Cookie 的 `name`、`value` 和 `domain`。例如：
     - 名稱：`cf_clearance`，值：`abc123...`，網域：`.grok.com`
     - 可能還存在其他 Cookie，例如 `__cfduid` 或工作階段特定的 Cookie。

3. **修改您的腳本**：
   - 在導航到 URL 之前，將 Cookie 添加到您的 Selenium 驅動程式中。更新您的程式碼如下：
     ```python
     # ... (現有的導入和設定保持不變)

     # 設定 geckodriver 服務
     service = Service(executable_path="/home/lzw/bin/geckodriver")
     driver = webdriver.Firefox(service=service, options=firefox_options)

     # 先開啟一個空白頁面來設定 Cookie（Cookie 只能在頁面載入後設定）
     driver.get("about:blank")

     # 添加您提取的 Cookie
     cookies = [
         {"name": "cf_clearance", "value": "abc123...", "domain": ".grok.com"},
         # 根據需要添加其他 Cookie，例如：
         # {"name": "__cfduid", "value": "xyz789...", "domain": ".grok.com"},
     ]
     for cookie in cookies:
         driver.add_cookie(cookie)

     # 現在導航到目標 URL
     driver.get("https://grok.com")

     # 列印頁面標題
     print("Title of the page:", driver.title)

     # ... (腳本其餘部分保持不變)
     ```

4. **測試腳本**：
   - 執行修改後的腳本。預先設定的 Cookie 應該向 Cloudflare 發出信號，表明瀏覽器已經通過了挑戰。

**為何此方法可能有效**：明確設定 `cf_clearance` Cookie 可以模擬已驗證的工作階段，從而可能繞過與核取方塊互動的需要。

**限制**：Cookie 可能與瀏覽器指紋（例如，使用者代理、IP 或 TLS 設定）綁定。如果 Selenium 的指紋與手動工作階段不同，Cloudflare 可能會拒絕 Cookie 或重新發起挑戰。

---

### **其他除錯和增強功能**
如果兩種方法都無法完全解決問題，請考慮對腳本進行以下調整，以確保其正確與 Cloudflare 挑戰互動：

- **檢查是否有 Iframe**：「驗證您是人類」核取方塊可能位於 iframe 內。修改您的核取方塊點擊程式碼，先切換到 iframe：
  ```python
  try:
      wait = WebDriverWait(driver, 20)
      iframe = wait.until(EC.presence_of_element_located((By.XPATH, "//iframe[contains(@src, 'cloudflare')]")))
      driver.switch_to.frame(iframe)
      label = wait.until(EC.presence_of_element_located((By.XPATH, "//label[@class='cb-lb']")))
      checkbox = label.find_element(By.TAG_NAME, "input")
      print("Checkbox found:", checkbox.is_displayed())
      checkbox.click()
      driver.switch_to.default_content()  # 切換回主要內容
      print("Checkbox clicked.")
  except Exception as e:
      print("Checkbox not found or not clickable:", e)
  ```

- **改進等待邏輯**：點擊核取方塊後，等待挑戰通過的明確信號（例如，驗證頁面消失）：
  ```python
  try:
      wait.until(EC.invisibility_of_element_located((By.XPATH, "//*[contains(text(), 'Verify you are human')]")))
      print("Challenge passed.")
  except Exception as e:
      print("Challenge not passed:", e)
  ```

- **掩蓋自動化痕跡**：添加 JavaScript 以隱藏 Selenium 的自動化痕跡：
  ```python
  driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
  ```

---

### **如果所有方法都失敗：替代方案**
如果 Cloudflare 的檢測持續存在，可能是由於進階指紋辨識技術，您當前的設定無法避開。以下是升級選項，儘管它們偏離了您對 Firefox 的偏好：

- **切換到使用 Undetected ChromeDriver 的 Chrome**：
  - 安裝：`pip install undetected-chromedriver`
  - 修改設定：
    ```python
    import undetected_chromedriver as uc
    driver = uc.Chrome()
    driver.get("https://grok.com")
    ```
  - 此程式庫會修補 Chrome 以避免常見的檢測方法。

- **使用代理或 CAPTCHA 解碼器**：像 2Captcha 或住宅代理這樣的服務可以處理挑戰，但它們會增加複雜性和成本。

---

### **建議的後續步驟**
從**方法 1**（重複使用設定檔）開始，因為它最簡單且符合您的腳本設定。如果失敗，請嘗試**方法 2**（Cookie 注入）並添加 iframe 檢查。這些方法能在不需要新工具的情況下，最大化您現有的 Firefox 配置。測試每種方法並監控輸出（例如 `driver.title` 和例外訊息）以確認挑戰是否被繞過。如果您仍然遇到問題，請根據專案的靈活性考慮替代方案。

如果您需要協助實施或疑難排解這些解決方案，請告訴我！