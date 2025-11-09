---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: Apache Bench 網頁伺服器測試指南
translated: true
type: note
---

### 什麼是 Apache Bench (ab)？

Apache Bench (ab) 是一個簡單的命令列工具，隨附於 Apache HTTP Server，用於對網頁伺服器進行效能基準測試。它會向指定 URL 發送一定數量的 HTTP 請求，並測量每秒請求數、每個請求的時間、傳輸速率和錯誤率等指標。它非常適合快速進行負載測試，但在複雜場景下功能有限（例如，預設不支援 HTTPS 或進階腳本功能——在這些情況下可考慮使用 JMeter 等工具）。

### 安裝方法

ab 隨附於 Apache HTTP Server。以下是安裝方法：

- **在 Ubuntu/Debian (Linux) 上**：
  ```
  sudo apt update
  sudo apt install apache2-utils
  ```

- **在 macOS (透過 Homebrew) 上**：
  ```
  brew install httpd
  ```

- **在 Windows 上**：
  從官方網站下載 Apache HTTP Server，並將其 `bin` 目錄加入 PATH 環境變數。

- **驗證安裝**：
  執行 `ab -V` 檢查版本。

### 基本用法

核心命令語法為：
```
ab [options] URL
```

- **URL 格式**：必須是完整的 HTTP URL，例如 `http://example.com/`。（對於 HTTPS，需使用如 `openssl s_client` 的封裝工具或改用 `wrk` 等工具。）

關鍵選項：
- `-n <requests>`：要執行的請求數量（預設值：1）。測試時可從 100–1000 開始。
- `-c <concurrency>`：同時發送的請求數量（預設值：1）。請保持較低數值（例如 10–50），以免壓垮伺服器。
- `-t <seconds>`：以指定時間執行，而非固定請求數。
- `-k`：啟用 HTTP Keep-Alive（重用連線）。
- `-H "Header: Value"`：新增自訂標頭（例如用於身份驗證）。
- `-p <file>`：從檔案讀取 POST 資料。
- `-T <content-type>`：POST 請求的內容類型。
- `-l`：接受可變文件長度（適用於動態內容）。

### 逐步操作範例

1. **測試簡單 GET 請求**：
   對本地伺服器模擬 100 個請求，並發 10 個並行用戶：
   ```
   ab -n 100 -c 10 http://localhost:8080/
   ```
   輸出範例：
   ```
   Server Software:        Apache/2.4.41
   Server Hostname:        localhost
   Server Port:            8080

   Document Path:          /
   Document Length:        1234 bytes

   Concurrency Level:      10
   Time taken for tests:   1.234 seconds
   Complete requests:      100
   Failed requests:        0
   Requests per second:    81.03 [#/sec] (mean)
   Time per request:       123.456 [ms] (mean)
   ```

2. **測試 POST 資料**（例如表單提交）：
   建立包含負載資料的 `postdata.txt` 檔案（例如 `key=value`）。
   ```
   ab -n 50 -c 5 -p postdata.txt -T application/x-www-form-urlencoded http://example.com/api/endpoint
   ```

3. **按時間執行**：
   ```
   ab -n 10000 -c 20 -t 30 http://example.com/  # 最多 10k 個請求或 30 秒
   ```

### 解讀結果

- **每秒請求數**：數值越高越好（吞吐量）。
- **每個請求時間**：數值越低越好（延遲）。
- **傳輸速率**：頻寬效率。
- 注意「Failed requests」或「Non-2xx responses」以發現問題。
- 由於快取/網路可能影響單次結果，建議多次執行並取平均值。

### 技巧與限制

- **從獨立機器執行**：盡量避免對 localhost 進行測試，以模擬真實流量。
- **預熱**：先發送少量請求以預熱快取。
- **擴展性**：對於更高負載，可使用 `wrk`、`siege` 或 Locust 等工具。
- **HTTPS**：ab 不原生支援；需使用代理或替代方案執行 `ab -n 100 -c 10 http://example.com/`。
- **錯誤處理**：若出現「socket: Too many open files」錯誤，請提高作業系統的文件描述符限制（例如 `ulimit -n 4096`）。

詳情請查閱手冊頁（`man ab`）或官方文件。

[Apache Bench 文件](https://httpd.apache.org/docs/2.4/programs/ab.html)