---
audio: false
date: 2025-09-10
generated: true
image: false
lang: hant
layout: post
model: openai/gpt-5
title: 應用程式介面測試獨特性與冪等性策略
translated: true
type: note
---

很好的問題。讓我們先從宏觀角度來看，然後再實際探討 API/整合測試中的「唯一性」問題。

# 基本概念速覽

* **URL（路徑 + 查詢參數）**

  * 路徑通常是**資源識別**：`/orders/123`
  * 查詢參數是**篩選器/修改器**：`/orders?status=PAID&page=2`

* **方法**

  * `GET/HEAD` 是安全操作
  * `PUT` 是**冪等**操作（相同呼叫，相同結果）
  * `POST` **不是**冪等操作，除非你加入**冪等金鑰**機制
  * `PATCH` 不保證冪等性

* **標頭**

  * `Content-Type`：**主體**的編碼方式

    * `application/json` → JSON 主體
    * `application/x-www-form-urlencoded` → `a=1&b=2` 主體
    * `multipart/form-data; boundary=----abcd` → 檔案上傳與混合部分
  * `Content-Disposition` 出現在**multipart部分內部**，而非頂層請求。典型部分：

    ```
    --Boundary123
    Content-Disposition: form-data; name="file"; filename="x.png"
    Content-Type: image/png

    <binary bytes>
    --Boundary123--
    ```
  * 實用的自訂標頭：

    * **Idempotency-Key**：消除重複 POST 操作的副作用
    * **X-Request-ID / Correlation-ID**：在跨服務間追蹤/記錄單一請求

* **主體**

  * JSON：序列化文件
  * `form-urlencoded`：鍵值對，類似查詢字串但位於主體中
  * `multipart/form-data`：多個「部分」，由 `boundary` 分隔符分隔（`----WebKitFormBoundary...` 是常見的瀏覽器字串）

# 識別資訊應置於何處？

* **資源識別** → 置於 **URL 路徑**（`/users/{id}`），因為它穩定且可加入書籤
* **操作修改器** → 查詢參數或標頭
* **要寫入的表示/狀態** → 主體

僅在 URL 中編碼請求唯一性通常對寫入操作無效（例如帶有大型 JSON 的 POST）。相反地，應從**兩個層面**思考：

1. **請求識別（指紋）**：
   以下項目的確定性雜湊值：

   * HTTP **方法**
   * **標準化路徑**（模板 + 具體值）
   * **標準化查詢**（排序後）
   * **選定標頭**（僅影響語義的標頭，例如 `Accept`、`Content-Language`，*而非* `Date`）
   * **主體**（標準化 JSON 或針對 multipart 每個部分的摘要）

2. **操作識別（業務冪等性）**：
   對於有副作用的操作（建立/收費/轉帳），使用 **Idempotency-Key**（每個*業務意圖*一個 UUID）。伺服器將第一個結果儲存在該金鑰下，並在重試時返回。

這些解決了不同問題：指紋有助於你的**測試**和**可觀測性**；冪等金鑰保護**生產環境**免受重複影響。

# 「唯一性」的測試策略

1. **定義請求指紋函數**（客戶端/測試端）。範例邏輯：

   * 標頭名稱轉小寫；僅包含安全的允許清單
   * 排序查詢參數；穩定地 JSON 字串化主體（移除空白字元，排序鍵）
   * 對 `METHOD\nPATH\nQUERY\nHEADERS\nBODY` 進行 SHA-256 雜湊

2. **為每個測試提供關聯 ID**

   * 為每個測試案例產生 UUID：`X-Request-ID: test-<suite>-<uuid>`
   * 在伺服器端記錄，以便將日誌與測試關聯

3. **在需要時使用冪等金鑰**

   * 對於建立資源或收費的 POST：

     * `Idempotency-Key: <uuid>`
     * 伺服器應在保留時間內對具有相同金鑰的重試返回相同的 200/201 和主體

4. **保持測試資料唯一但最小化**

   * 使用種子化、確定性的 ID（例如電子郵件 `user+T001@example.com`）或在後綴中加入測試 UUID
   * 進行清理，或者更好的是，盡可能透過對種子化 ID 使用 PUT/DELETE 來設計**冪等**測試

5. **在適當層級進行斷言**

   * 對於**冪等**操作：斷言**狀態**、**表示**和**副作用**（例如重複時記錄計數不變）
   * 對於帶有冪等金鑰的**非冪等** POST：斷言第一次呼叫為 201，後續重試為 200 且主體相同（或重複 201 且資源相同）

# 實用程式碼片段

**cURL 範例**

* JSON POST：

  ```bash
  curl -X POST https://api.example.com/orders \
    -H 'Content-Type: application/json' \
    -H 'Idempotency-Key: 4b6f2d1a-...' \
    -H 'X-Request-ID: test-orders-create-...' \
    -d '{"customerId":"C123","items":[{"sku":"ABC","qty":1}]}'
  ```
* Multipart 上傳：

  ```bash
  curl -X POST https://api.example.com/uploads \
    -H 'X-Request-ID: test-upload-...' \
    -F 'file=@/path/pic.png' \
    -F 'meta={"purpose":"avatar"};type=application/json'
  ```

  （curl 設定 `Content-Type: multipart/form-data; boundary=----...` 且每個部分都有自己的 `Content-Disposition`。）

**Python 測試端請求指紋（示意性）：**

```python
import hashlib, json, urllib.parse

def canonical_json(obj):
    return json.dumps(obj, separators=(',', ':'), sort_keys=True)

def normalize_query(url):
    parsed = urllib.parse.urlsplit(url)
    q = urllib.parse.parse_qsl(parsed.query, keep_blank_values=True)
    q.sort()
    return urllib.parse.urlunsplit((parsed.scheme, parsed.netloc, parsed.path, urllib.parse.urlencode(q), '')), q

def request_fingerprint(method, url, headers=None, body_bytes=b''):
    headers = headers or {}
    # 允許影響語義的標頭清單
    allow = {'accept', 'content-type', 'content-language'}
    norm_headers = {k.lower(): v.strip() for k, v in headers.items() if k.lower() in allow}
    header_line = '\n'.join(f'{k}:{norm_headers[k]}' for k in sorted(norm_headers))
    url_no_query, q_pairs = normalize_query(url)
    query_line = '&'.join(f'{k}={v}' for k, v in q_pairs)
    h = hashlib.sha256()
    h.update((method.upper() + '\n').encode())
    h.update((url_no_query + '\n').encode())
    h.update((query_line + '\n').encode())
    h.update((header_line + '\n').encode())
    h.update(body_bytes or b'')
    return h.hexdigest()
```

* 對於 JSON 主體，傳遞 `body_bytes=canonical_json(payload).encode()`
* 對於 multipart，對每個部分進行雜湊，然後對串聯結果進行雜湊以避免邊界雜訊

# 回答你的核心想法

> 「如果 URL 是唯一的，那麼請求就是唯一的；參數/主體仍然貢獻很大——如何思考 API/整合測試中的唯一性？」

* 將**僅 URL**視為測試中唯一性的**不足**依據，因為標頭和主體實質上改變了語義
* 如上所述建立**請求指紋**，用於測試中的去重/追蹤
* 對於 **POST** 的業務層級去重，依賴**冪等金鑰**，而非 URL
* 將**資源識別**保持在路徑中，以實現清晰度和更好的測試確定性

# 可立即採用的小清單

* [ ] 為每個測試請求加入 `X-Request-ID`（UUID）
* [ ] 為建立/收費的 POST 加入 `Idempotency-Key`
* [ ] 實作一個測試輔助工具，計算請求指紋並在每個斷言中記錄它
* [ ] 在雜湊前標準化 JSON；排序查詢參數；允許語義標頭清單
* [ ] 偏好使用 PUT 進行更新插入以使測試冪等；保留 POST 用於真正的建立操作
* [ ] 對於 multipart，斷言**伺服器解析的部分**（名稱、檔案名、內容類型）而非原始邊界位元組

如果你分享當前的測試技術堆疊（pytest/unittest + requests/httpx，或 Java/Kotlin），我可以提供針對該堆疊量身定制的即用型輔助工具。