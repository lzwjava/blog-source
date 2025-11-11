---
audio: false
generated: true
lang: hant
layout: post
title: HTTP 檔案上傳
translated: true
type: note
---

### 重點摘要
- 研究顯示 HTTP 檔案上傳通常使用 POST 方法搭配 multipart/form-data 格式處理網頁表單，可同時上傳多個檔案及附加資料
- PUT 方法似乎也能用於檔案上傳，直接傳送原始內容，常見於 RESTful API 以簡化流程
- 證據顯示兩種方法皆有效，實際選擇取決於伺服器配置與使用情境

### 概覽
透過 HTTP 上傳檔案是網路資料分享的常見任務，例如將照片或文件傳送至網站。主要有兩種實現方式：使用 POST 方法搭配 multipart/form-data 特殊格式（適合網頁表單），或使用 PUT 方法（較簡潔且常用於現代 API）。每種方法各有配置要求，合適的選擇需視伺服器設定與使用目的而定。

### 運作原理
- **POST 搭配 Multipart/Form-Data**：如同將檔案與附加資訊（如描述文字）分裝成獨立區塊，以獨特邊界字串標記。常見於需選擇上傳檔案的網頁表單
- **PUT 方法**：直接將檔案內容傳送至特定 URL，類似於更新伺服器上的檔案。較簡潔但需伺服器支援

### 特殊細節
您可能沒想到通常用於更新資料的 PUT 方法，特別在 API 情境中也能處理檔案上傳，使其成為傳統表單之外的多功能選擇。

---

### 技術解析：HTTP 檔案上傳詳解

透過 HTTP 上傳檔案是網頁開發的基礎操作，讓使用者能與伺服器分享圖片、文件或多媒體等資料。此過程主要透過兩種方法實現：適用於網頁表單的 POST 方法搭配 multipart/form-data 編碼，以及常用於 RESTful API 直接傳輸檔案內容的 PUT 方法。以下我們將深入探討這些方法的結構、實作與注意事項，為技術與非技術讀者提供全面理解。

#### Multipart/Form-Data：網頁表單標準格式

multipart/form-data 內容類型是 HTTP 檔案上傳的預設選擇，特別在處理 HTML 表單時。此方法允許在單一請求中同時傳輸多個檔案與附加表單資料（如文字欄位）。流程涉及建構由多部分組成的請求主體，各部分以獨特邊界字串分隔，確保伺服器能區分不同資料區塊。

##### 結構與範例
請求起始需設定 `Content-Type` 標頭為 `multipart/form-data; boundary=邊界字串`，其中 `邊界字串` 是隨機選取以避免與檔案內容衝突。主體每個部分包含如 `Content-Disposition` 的標頭（指定表單欄位名稱與檔案名稱），以及 `Content-Type`（標明資料類型如文字檔案用 `text/plain`，JPEG 圖片用 `image/jpeg`）。部分結尾以邊界字串標記，最終部分則以邊界字串加兩個連字號結尾。

假設上傳名為 `example.txt` 的檔案（內容為 "Hello, world!"）至[此端點](https://example.com/upload)，表單欄位名稱為 "file"。HTTP 請求範例如下：

```
POST /upload HTTP/1.1
Host: example.com
Content-Type: multipart/form-data; boundary=abc123
Content-Length: 101

--abc123
Content-Disposition: form-data; name="file"; filename="example.txt"
Content-Type: text/plain

Hello, world!
--abc123--
```

此處 `Content-Length` 計算為 101 位元組，包含邊界、標頭與檔案內容，行尾通常使用 CRLF (`\r\n`) 以符合 HTTP 標準格式。

##### 處理多檔案與表單欄位
此方法特別適合需要附加元資料的情境。例如上傳檔案時若需包含描述，請求主體可包含多個部分：

```
--abc123
Content-Disposition: form-data; name="description"

This is my file
--abc123
Content-Disposition: form-data; name="file"; filename="example.txt"
Content-Type: text/plain

Hello, world!
--abc123--
```

每個部分的內容（包括換行符號）都會保留，邊界字串確保區隔。這種彈性使其成為含 `<input type="file"> 元素網頁表單的理想選擇。

#### PUT 方法：RESTful API 直接檔案上傳

PUT 方法提供更簡潔的替代方案，特別在 RESTful API 情境中，目標是以檔案內容更新或建立資源。與 multipart/form-data 不同，PUT 直接將原始檔案資料置於請求主體，減少負載並簡化伺服器端處理。

##### 結構與範例
將 `example.txt` 上傳至[此網址](https://example.com/files/123)的請求範例：

```
PUT /files/123 HTTP/1.1
Host: example.com
Content-Type: text/plain
Content-Length: 13

Hello, world!
```

此處 `Content-Type` 指定檔案的 MIME 類型（如 `text/plain`），`Content-Length` 為檔案位元組大小。此方法對大檔案較高效，因避免 multipart/form-data 的編碼負載，但需伺服器配置支援 PUT 請求處理檔案上傳。

##### 使用情境與注意事項
PUT 常用於更新使用者頭像或上傳檔案至 API 特定資源等情境。但非所有伺服器預設支援 PUT 檔案上傳，特別在共享主機環境中，POST 搭配 multipart/form-data 的接受度更普遍。可能需要伺服器配置（如 Apache 啟用 PUT 動詞），如 [PHP 手冊關於 PUT 方法支援](https://www.php.net/manual/en/features.file-upload.put-method.php) 所述。

#### 比較分析

為說明差異，請參考以下兩種方法比較表：

| 比較維度             | POST 搭配 Multipart/Form-Data        | PUT 搭配原始內容                  |
|----------------------|--------------------------------------|-----------------------------------|
| **使用情境**         | 網頁表單、多檔案、元資料             | RESTful API、單檔案更新           |
| **複雜度**           | 較高（邊界處理、多部分）             | 較低（直接內容）                  |
| **效率**             | 中等（編碼負載）                     | 較高（無編碼）                    |
| **伺服器支援**       | 廣泛支援                             | 可能需要配置                      |
| **標頭範例**         | `Content-Type: multipart/form-data; boundary=abc123` | `Content-Type: text/plain`        |
| **請求主體**         | 以邊界分隔的多部分                   | 原始檔案內容                      |

此表顯示 multipart/form-data 在網頁互動方面較多功能，而 PUT 在 API 驅動的上傳方面較高效，實際選擇取決於伺服器能力。

#### 實作細節與潛在問題

##### 邊界選擇與檔案內容
在 multipart/form-data 中，選擇邊界字串至關重要，需避免與檔案內容重複。若邊界出現於檔案內，可能導致解析錯誤。現代函式庫會透過隨機產生邊界處理此問題，但手動實作需特別注意。對於二進位檔案，內容會按原樣傳輸，保留所有位元組，對維持檔案完整性至關重要。

##### 檔案大小與效能
兩種方法皆需考慮伺服器設定的檔案大小限制。Multipart/form-data 請求可能因多檔案變大，超出伺服器限制或導致記憶體問題。PUT 方法雖較簡潔，但大檔案仍需串流處理以避免整個內容載入記憶體，如 [HTTPie 文件關於檔案上傳表單](https://httpie.io/docs/cli/file-upload-forms) 所述。

##### 錯誤處理與安全性
傳送請求後，客戶端應檢查 HTTP 狀態碼。成功通常以 200 (OK) 或 201 (Created) 表示，而 400 (Bad Request) 或 403 (Forbidden) 等錯誤碼則表示問題。安全性至關重要，因檔案上傳可能被利用進行攻擊（如上傳惡意執行檔）。伺服器應驗證檔案類型、掃描惡意軟體並限制上傳目錄，如 [Stack Overflow 關於 HTTP 檔案上傳安全性的討論](https://stackoverflow.com/questions/8659808/how-does-http-file-upload-work) 所述。

#### 跨語言實務範例

各種程式語言提供函式庫簡化 HTTP 檔案上傳。例如 Python 的 `requests` 函式庫處理 multipart/form-data：

```python
import requests
files = {'file': open('example.txt', 'rb')}
response = requests.post('https://example.com/upload', files=files)
```

對於 PUT，可使用 curl 如 [Stack Overflow 關於測試 PUT 上傳](https://stackoverflow.com/questions/5143915/test-file-upload-using-http-put-method) 所示：

```bash
curl -X PUT "https://example.com/files/123" --upload-file example.txt
```

這些範例展示抽象化工具的使用，但理解底層 HTTP 結構對除錯與自訂實作至關重要。

#### 結論

總括而言，HTTP 檔案上傳可透過 POST 搭配 multipart/form-data 實現多功能網頁表單互動，或透過 PUT 實現高效 API 更新，各自具備獨特優勢與需求。伺服器配置、檔案大小與安全性考量皆為關鍵，確保穩健實作。延伸閱讀可參考 [Medium 的 POST 檔案上傳指南](https://medium.com/@API4AI/post-a-file-via-http-request-the-ultimate-guide-b23fb70a3f73) 查看跨語言實務範例。

### 主要參考文獻
- [How do you upload your files to a web server Learn web development MDN](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Tools_and_setup/Upload_files_to_a_web_server)
- [How does HTTP file upload work Stack Overflow](https://stackoverflow.com/questions/8659808/how-does-http-file-upload-work)
- [POST a File via HTTP Request The Ultimate Guide by API4AI Medium](https://medium.com/@API4AI/post-a-file-via-http-request-the-ultimate-guide-b23fb70a3f73)
- [HTTP REST API File Uploads Phil Sturgeon](https://philsturgeon.com/http-rest-api-file-uploads/)
- [PHP PUT method support Manual](https://www.php.net/manual/en/features.file-upload.put-method.php)
- [curl Test file upload using HTTP PUT method Stack Overflow](https://stackoverflow.com/questions/5143915/test-file-upload-using-http-put-method)
- [File upload forms HTTPie 3.2.4 latest docs](https://httpie.io/docs/cli/file-upload-forms)