---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 不支援代理方案
translated: true
type: note
---

錯誤顯示，您的 `gitmessageai.py` 腳本中 `openai` 客戶端使用的 `httpx` 庫正嘗試配置代理，其 URL 為 `socks://127.0.0.1:7891/`，但該庫不支援或無法識別 `socks` 方案，導致出現 `ValueError: Unknown scheme for proxy URL`。這表明您的環境或代碼中載入了代理配置，且該配置使用了不支援的 SOCKS 代理方案。

讓我們分析代理配置可能來自何處，以及如何修復此問題。

### 代理配置來自何處？

代理配置 (`socks://127.0.0.1:7891/`) 很可能來自以下其中一個來源：

1. **環境變數**
   - `httpx` 庫會自動檢查環境變數中的代理設置，例如 `HTTP_PROXY`、`HTTPS_PROXY`、`ALL_PROXY` 或其小寫形式 (`http_proxy`、`https_proxy`、`all_proxy`)。
   - 像 `socks://127.0.0.1:7891/` 這樣的值表明某個環境變數中設置了 SOCKS 代理（常見於 Shadowsocks 或 VPN 等工具）。
   - 要檢查這些變數是否已設置，請在終端機中執行以下指令：
     ```bash
     env | grep -i proxy
     ```
     尋找類似 `HTTP_PROXY=socks://127.0.0.1:7891` 或 `HTTPS_PROXY=socks://127.0.0.1:7891` 的變數。

2. **系統全域代理設置**
   - 如果您使用的是 Linux 系統，代理設置可能已全域配置（例如在 `/etc/environment`、`/etc/profile` 或您的 Shell 配置檔案中，如 `~/.bashrc`、`~/.zshrc` 或 `~/.profile`）。
   - 檢查這些檔案中是否有如下行：
     ```bash
     export HTTP_PROXY="socks://127.0.0.1:7891"
     export HTTPS_PROXY="socks://127.0.0.1:7891"
     ```
   - 您可以使用以下指令查看這些檔案：
     ```bash
     cat ~/.bashrc | grep -i proxy
     cat ~/.zshrc | grep -i proxy
     cat /etc/environment | grep -i proxy
     ```

3. **代理工具中的代理配置**
   - 地址 `127.0.0.1:7891` 通常被代理或 VPN 工具（如 Shadowsocks、V2Ray 或 Clash）使用，這些工具通常預設使用 7890 或 7891 等埠的 SOCKS5 代理。
   - 如果您安裝或配置了此類工具，它可能已自動設置環境變數或系統代理設置。

4. **代碼中的顯式代理配置**
   - 雖然可能性較小，但您的 `gitmessageai.py` 腳本或其使用的庫可能顯式配置了代理。由於錯誤發生在 `httpx` 中，請檢查您的腳本是否將代理傳遞給 `OpenAI` 客戶端或 `httpx` 客戶端。
   - 在您的腳本中搜尋 `proxy`、`proxies` 或 `httpx.Client` 等術語：
     ```bash
     grep -r -i proxy /home/lzwjava/bin/gitmessageai.py
     ```

5. **Python 庫配置**
   - 某些 Python 庫（例如 `requests` 或 `httpx`）可能會從配置檔案或先前的設置中繼承代理設置。然而，`httpx` 主要依賴環境變數或顯式代碼。

### 為什麼 `socks://` 會導致問題？

- `httpx` 庫（由 `openai` 使用）本身不支援 `socks` 方案（SOCKS4/SOCKS5 代理），除非安裝了額外的依賴項（如 `httpx-socks`）。
- 發生錯誤 `Unknown scheme for proxy URL` 是因為 `httpx` 預期的代理方案是 `http://` 或 `https://`，而不是 `socks://`。

### 如何修復此問題

您有兩個選擇：如果不需要代理，則**移除或繞過代理**；如果需要使用 SOCKS 代理，則**支援 SOCKS 代理**。

#### 選項 1：移除或繞過代理

如果您不需要為 DeepSeek API 使用代理，可以停用或繞過代理配置。

1. **取消設置環境變數**
   - 如果代理是在環境變數中設置的，請為您的會話取消設置它們：
     ```bash
     unset HTTP_PROXY
     unset HTTPS_PROXY
     unset ALL_PROXY
     unset http_proxy
     unset https_proxy
     unset all_proxy
     ```
   - 要永久取消設置，請從 `~/.bashrc`、`~/.zshrc`、`/etc/environment` 或其他 Shell 配置檔案中移除相應的 `export` 行。

2. **在無代理情況下執行腳本**
   - 暫時在沒有代理設置的情況下執行您的腳本：
     ```bash
     HTTP_PROXY= HTTPS_PROXY= ALL_PROXY= python3 /home/lzwjava/bin/gitmessageai.py
     ```
   - 如果這樣可以正常執行，則問題在於代理。

3. **在代碼中繞過代理**
   - 修改您的 `gitmessageai.py` 腳本，以在 `OpenAI` 客戶端中顯式停用代理：
     ```python
     from openai import OpenAI
     import httpx

     def call_deepseek_api(prompt):
         api_key = os.getenv("DEEPSEEK_API_KEY")
         if not api_key:
             raise ValueError("DEEPSEEK_API_KEY environment variable is not set")
         client = OpenAI(
             api_key=api_key,
             base_url="https://api.deepseek.com",
             http_client=httpx.Client(proxies=None)  # 停用代理
         )
         # 您的 API 呼叫邏輯在此
         response = client.chat.completions.create(
             model="deepseek",  # 替換為正確的模型
             messages=[{"role": "user", "content": prompt}]
         )
         return response.choices[0].message.content
     ```
   - 設置 `proxies=None` 可確保 `httpx` 忽略任何環境代理設置。

#### 選項 2：支援 SOCKS 代理

如果您需要使用 SOCKS 代理（例如，透過 VPN 或代理伺服器存取 DeepSeek API），則必須為 `httpx` 添加 SOCKS 支援。

1. **安裝 `httpx-socks`**
   - 安裝 `httpx-socks` 套件以啟用 SOCKS4/SOCKS5 代理支援：
     ```bash
     pip install httpx-socks
     ```
   - 這將擴展 `httpx` 以處理 `socks://` 和 `socks5://` 方案。

2. **更新您的代碼**
   - 修改您的腳本以顯式使用 SOCKS 代理：
     ```python
     from openai import OpenAI
     import httpx
     from httpx_socks import SyncProxyTransport

     def call_deepseek_api(prompt):
         api_key = os.getenv("DEEPSEEK_API_KEY")
         if not api_key:
             raise ValueError("DEEPSEEK_API_KEY environment variable is not set")
         # 配置 SOCKS5 代理
         proxy_transport = SyncProxyTransport.from_url("socks5://127.0.0.1:7891")
         client = OpenAI(
             api_key=api_key,
             base_url="https://api.deepseek.com",
             http_client=httpx.Client(transport=proxy_transport)
         )
         # 您的 API 呼叫邏輯在此
         response = client.chat.completions.create(
             model="deepseek",  # 替換為正確的模型
             messages=[{"role": "user", "content": prompt}]
         )
         return response.choices[0].message.content
     ```
   - 如果您的代理使用 SOCKS4，請將 `socks5://` 替換為 `socks4://`。

3. **驗證代理伺服器**
   - 確保 `127.0.0.1:7891` 上的代理伺服器正在執行。如果您使用的是 Clash 或 Shadowsocks 等工具，請檢查其狀態：
     ```bash
     netstat -tuln | grep 7891
     ```
   - 如果沒有進程在監聽 7891 埠，請啟動您的代理工具或更正代理 URL 中的埠。

### 其他除錯步驟

- **檢查代理工具配置**
  - 如果您使用的是 Clash 或 Shadowsocks 等代理工具，請驗證其配置檔案（例如 `~/.config/clash/config.yaml`），確認其設置為使用 `127.0.0.1:7891` 作為 SOCKS5 代理。
  - 確保該工具正在執行且可存取。

- **測試代理連線**
  - 使用 `curl` 等工具測試代理（需要 `curl` 支援 SOCKS）：
    ```bash
    curl --socks5 127.0.0.1:7891 https://api.deepseek.com
    ```
  - 如果失敗，則代理伺服器可能已關閉或配置錯誤。

- **記錄代理使用情況**
  - 在您的腳本中添加日誌記錄以確認正在使用哪個代理：
    ```python
    import logging
    logging.basicConfig(level=logging.DEBUG)
    ```

### 建議的修復方法

如果您不需要代理，最簡單的修復方法是透過取消設置環境變數來停用它，並執行：
```bash
HTTP_PROXY= HTTPS_PROXY= ALL_PROXY= python3 /home/lzwjava/bin/gitmessageai.py
```

如果您需要代理，請安裝 `httpx-socks` 並更新您的代碼以使用如上所示的 `SyncProxyTransport`。

### 參考資料
- [httpx 文件](https://www.python-httpx.org/advanced/#proxy-support)
- [httpx-socks GitHub](https://github.com/romis2012/httpx-socks)
- [DeepSeek API 文件](https://platform.deepseek.com/docs)