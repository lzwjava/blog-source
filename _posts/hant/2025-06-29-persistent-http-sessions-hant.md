---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: 使用請求工作階段實現持久HTTP連線
translated: true
type: note
---

### requests.Session 的工作原理

在 Python 的 `requests` 庫中，`requests.Session` 是一個類別，允許你在多個 HTTP 請求之間維持持久性工作階段。與進行單獨的 `requests.get()` 或類似呼叫相比，它提供了幾個優點：

- **Cookie 持久性**：預設情況下，它會自動儲存並在後續請求中傳送從伺服器接收的 Cookie。這實現了基於工作階段的互動，例如登入一次後保持驗證狀態。
- **連線池**：它會重複使用相同主機的底層 TCP 連線，透過避免建立新連線的開銷來提升效能。
- **共享配置**：你可以設定預設標頭、驗證、代理或其他參數，這些設定會套用至工作階段內的所有請求。
- **底層機制**：它使用 `urllib3` 庫進行 HTTP 處理。當你建立 `Session` 時，它會初始化屬性如 `cookies`（一個 `RequestsCookieJar` 實例）、`headers` 等。例如，來自一個回應的 Cookie 會自動包含在下一個對相同網域的請求中。

以下是建立和使用工作階段的基本範例：

```python
import requests

# 建立工作階段
session = requests.Session()

# 為此工作階段中的所有請求設定預設標頭
session.headers.update({'User-Agent': 'MyApp/1.0'})

# 進行多個請求，共享工作階段
response1 = session.get('https://example.com/login')
response2 = session.post('https://example.com/data', data={'key': 'value'})

# 存取工作階段中儲存的 Cookie
print(session.cookies)
```

這確保了 Cookie（如工作階段 ID）的處理是透明的，無需手動介入。

### 使用 Python 呼叫 Java/Spring 專案的 API

要與使用 Java/Spring 建構的 API（通常是透過 Spring MVC 或 Spring Boot 的 RESTful 端點）互動，你可以像使用任何 HTTP API 一樣使用 `requests.Session`。Spring 專案通常透過 HTTP/HTTPS 公開 API，而 `requests` 可以處理驗證、CSRF 令牌或速率限制（如果已實作）。

- **驗證**：Spring 可能使用帶有表單、JWT 或 OAuth 的 Spring Security。對於基於工作階段的驗證（例如透過登入表單），`requests.Session` 在登入請求後自動處理 Cookie。
- **進行呼叫**：使用標準的 HTTP 方法如 `GET`、`POST` 等。如果 Spring API 需要 JSON 負載，請傳遞 `json=your_data`。

登入 Spring 驗證的 API 並呼叫另一個端點的範例：

```python
import requests

session = requests.Session()

# 登入（假設向 /login 發送 POST 請求，包含使用者名稱和密碼）
login_payload = {'username': 'user', 'password': 'pass'}
response = session.post('https://spring-api.example.com/login', data=login_payload)

if response.ok:
    # 現在呼叫另一個 API 端點，工作階段 Cookie 會持續存在
    data_response = session.get('https://spring-api.example.com/api/data')
    print(data_response.json())
else:
    print("登入失敗")
```

Spring API 預設是無狀態的，但可以透過伺服器端儲存（例如在 Tomcat 或嵌入式伺服器中）管理工作階段。確保你的 Python 客戶端處理 Spring 所需的任何 CORS、CSRF 或自訂標頭。

### 與 Java/Spring 端的 JSESSIONID 的關係

- **什麼是 JSESSIONID？**：在 Java Web 應用程式（包括 Spring，通常運行在如 Tomcat 的 Servlet 容器中）中，JSESSIONID 是一個標準的 HTTP Cookie，由容器用於追蹤使用者工作階段。它在工作階段建立時（例如登入後）設定，並在回應中傳回。在客戶端，瀏覽器（或如 `requests` 的 HTTP 客戶端）會在後續請求中包含它以維持狀態，例如使用者驗證或購物車資料。
- **與 requests.Session 的關係**：`requests.Session` 將 JSESSIONID 視為任何其他 Cookie——它會自動從伺服器的 "Set-Cookie" 標頭儲存它，並在未來請求的 "Cookie" 標頭中包含它。這使得與有狀態的 Spring API 的互動無縫進行，無需手動解析/提取 Cookie。
- **伺服器端處理**：在 Java/Spring 端，ServletContext 管理工作階段。當你的 Python 客戶端發送帶有 JSESSIONID 的請求時，Spring 的 HttpSession 會檢索相關的伺服器端資料。如果過期或無效，Spring 可能需要重新驗證。對於安全的工作階段，請確保你的設定使用 HTTPS，因為 JSESSIONID 在 HTTP 上可能容易遭到竊取。
- **潛在問題**：如果 Spring 強制執行 CSRF 令牌或其他保護措施，你可能需要提取並包含它們（例如從隱藏表單欄位）。對於無狀態的基於 JWT 的 Spring API，`requests.Session` 仍然有助於在標頭中持久保存驗證令牌，但 JSESSIONID 變得不那麼相關。

如果在呼叫 Spring API 時遇到特定錯誤（例如 401 Unauthorized），請檢查網路日誌以查找 Cookie 問題，或透過 `import logging; logging.basicConfig(level=logging.DEBUG)` 啟用 `requests` 的除錯功能。有關 Spring Security 的更多資訊，請參閱其官方文件。