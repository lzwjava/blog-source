---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 透過 .env 配置 Python Requests 代理
translated: true
type: note
---

### 使用 `.env` 檔案設定 Python Requests 的 HTTP/HTTPS 代理

Python 中的 `requests` 函式庫會自動遵循標準環境變數（如 `HTTP_PROXY` 和 `HTTPS_PROXY`）進行代理配置。為了安全地管理這些變數（例如，避免在程式碼中寫死），您可以將它們儲存在 `.env` 檔案中，並使用 `python-dotenv` 函式庫來載入。這樣可以將敏感的代理詳細資訊與程式碼分離。

#### 步驟 1：安裝所需套件
您需要安裝 `requests`（如果尚未安裝）和 `python-dotenv` 來載入 `.env` 檔案。

```bash
pip install requests python-dotenv
```

#### 步驟 2：建立 `.env` 檔案
在您的專案根目錄中，建立一個名為 `.env`（無副檔名）的檔案，並加入您的代理設定。代理 URL 請使用 `http://` 或 `https://` 格式，如果需要，請包含使用者名稱和密碼。

範例 `.env` 內容：
```
HTTP_PROXY=http://username:password@proxy-host:port
HTTPS_PROXY=https://username:password@proxy-host:port
NO_PROXY=localhost,127.0.0.1,example.com  # 可選：排除不使用代理的網域
```

- `HTTP_PROXY`：用於 HTTP 流量。
- `HTTPS_PROXY`：用於 HTTPS 流量（通常與 HTTP_PROXY 相同）。
- `NO_PROXY`：以逗號分隔的主機/IP 清單，這些將繞過代理。
- 注意：環境變數不區分大小寫，但通常使用大寫。

將 `.env` 加入您的 `.gitignore` 檔案，以避免提交敏感資訊。

#### 步驟 3：在 Python 腳本中載入 `.env` 檔案
在腳本頂部載入環境變數：

```python
from dotenv import load_dotenv
import requests

# 從 .env 檔案載入變數
load_dotenv()  # 預設在當前目錄中尋找 .env 檔案

# 現在發送請求 – 代理會自動應用
response = requests.get('https://httpbin.org/ip')
print(response.json())
```

- `load_dotenv()` 會讀取 `.env` 檔案並將變數設定到 `os.environ` 中。
- `requests` 會自動偵測 `HTTP_PROXY`/`HTTPS_PROXY` – 除非需要覆寫，否則無需傳遞 `proxies` 字典。

#### 步驟 4：驗證代理使用（可選）
要確認代理是否正常工作，可以使用 httpbin.org 等服務進行測試：

```python
import requests
from dotenv import load_dotenv

load_dotenv()

proxies = requests.utils.get_environ_proxies('https://httpbin.org/ip')  # 檢查載入的代理
print("載入的代理：", proxies)

response = requests.get('https://httpbin.org/ip')
print("透過代理的您的 IP：", response.json())
```

如果配置正確，這應該會顯示代理伺服器的 IP。

#### 常見問題與提示
- **代理驗證**：如果需要，請在 URL 中包含 `username:password@`。
- **SOCKS 代理**：使用 `socks5://` 前綴（需要安裝 `requests[socks]` 額外套件：`pip install requests[socks]`）。
- **每個請求覆寫代理**：如果特定呼叫需要不同的代理，請傳遞字典：
  ```python:disable-run
  proxies = {'http': 'http://custom-proxy:port', 'https': 'https://custom-proxy:port'}
  response = requests.get('url', proxies=proxies)
  ```
- **環境**：適用於 Windows/Linux/macOS。在 Windows 上，請在 cmd 中使用 `set` 或 PowerShell 的等效指令。
- **安全性**：切勿將 `.env` 提交到版本控制。

此設定簡單、安全，並遵循基於環境配置的最佳實踐。

[Requests 文件：代理](https://requests.readthedocs.io/en/latest/user/advanced/#proxies)  
[python-dotenv 文件](https://github.com/theskumar/python-dotenv)