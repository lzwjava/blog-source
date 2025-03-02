---
audio: false
generated: true
lang: hant
layout: post
title: HTTP 文件上傳
translated: true
---

### 關鍵要點
- 研究表明，HTTP 文件上傳通常使用 POST 方法和 multipart/form-data 來處理網頁表單，允許上傳多個文件和額外數據。
- 似乎 PUT 方法也可以上傳文件，直接發送原始內容，通常在 RESTful API 中用於簡化。
- 證據傾向於兩種方法都有效，伺服器配置和使用情況決定選擇。

### 概述
通過 HTTP 上傳文件是分享在線數據的常見任務，例如將照片或文件發送到網站。這可以通過兩種主要方式完成：使用 POST 方法和一種稱為 multipart/form-data 的特殊格式，這對於網頁表單非常有用，或者使用 PUT 方法，這更簡單且通常在現代 API 中使用。每種方法都有其自己的設置，選擇權取決於伺服器的設置和您要做的事情。

### 運作方式
- **POST 方法與 Multipart/Form-Data**：這就像將您的文件和任何額外信息（如描述）打包成單獨的部分，用唯一的邊界字符串標記。這對於選擇要上傳的文件的網頁表單很常見。
- **PUT 方法**：這將文件內容直接發送到特定的 URL，就像在伺服器上更新文件。它更簡單，但需要伺服器支持。

### 意外細節
您可能不會想到 PUT 方法，通常用於更新數據，也可以處理文件上傳，特別是在 API 中，使其成為超越傳統表單的多功能選項。

---

### 調查筆記：HTTP 文件上傳的詳細說明

通過 HTTP 上傳文件是網頁開發中的基本操作，使用戶能夠將數據（如圖像、文件或媒體）與伺服器共享。這個過程可以通過兩種主要方法完成：使用 POST 方法和 multipart/form-data 編碼，通常用於 HTML 表單，以及 PUT 方法，通常在 RESTful API 中用於直接傳輸文件內容。下面，我們深入探討這些方法，包括其結構、實現和考慮因素，為技術和非技術受眾提供全面的理解。

#### Multipart/Form-Data：網頁表單的標準

multipart/form-data 內容類型是 HTTP 文件上傳的默認選擇，特別是處理 HTML 表單時。這種方法允許在單個請求中同時傳輸多個文件和額外的表單數據，如文本字段。該過程涉及構建一個請求體，分為多個部分，每個部分由唯一的邊界字符串分隔，這樣伺服器就能區分不同的數據片段。

##### 結構和示例
請求開始於設置 `Content-Type` 標頭為 `multipart/form-data; boundary=boundary_string`，其中 `boundary_string` 是隨機選擇的字符串，以避免與文件內容衝突。請求體的每個部分都包括標頭，如 `Content-Disposition`，指定表單字段名稱和文件名，以及 `Content-Type`，指示數據類型（例如，`text/plain` 用於文本文件，`image/jpeg` 用於 JPEG 圖像）。部分以邊界字符串結束，最後一部分以邊界字符串後跟兩個連字符標記。

考慮將名為 `example.txt` 的文件及其內容 "Hello, world!" 上傳到 [此端點](https://example.com/upload)，表單字段名為 "file"。HTTP 請求將如下所示：

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

這裡，`Content-Length` 計算為 101 字節，包括邊界、標頭和文件內容，行結束通常使用 CRLF (`\r\n`) 以正確格式化 HTTP。

##### 處理多個文件和表單字段
這種方法在需要額外元數據的情況下表現出色。例如，如果上傳一個帶有描述的文件，請求體可以包括多個部分：

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

每個部分的內容都被保留，包括任何換行符，邊界確保分隔。這種靈活性使其非常適合具有 `<input type="file">` 元素的網頁表單。

#### PUT 方法：RESTful API 的直接文件上傳

PUT 方法提供了一種更簡單的替代方案，特別是在 RESTful API 環境中，目的是更新或創建具有文件內容的資源。與 multipart/form-data 不同，PUT 直接在請求體中發送原始文件數據，減少了開銷並簡化了伺服器端處理。

##### 結構和示例
將 `example.txt` 上傳到 [此 URL](https://example.com/files/123)，請求將如下所示：

```
PUT /files/123 HTTP/1.1
Host: example.com
Content-Type: text/plain
Content-Length: 13

Hello, world!
```

這裡，`Content-Type` 指定文件的 MIME 類型（例如，`text/plain`），`Content-Length` 是文件大小（以字節為單位）。這種方法對於大文件非常高效，因為它避免了 multipart/form-data 的編碼開銷，但它需要伺服器配置以處理文件上傳的 PUT 請求。

##### 使用情況和考慮因素
PUT 通常用於更新用戶頭像或將文件上傳到 API 中的特定資源。然而，並非所有伺服器都默認支持文件上傳的 PUT，特別是在共享托管環境中，POST 使用 multipart/form-data 更普遍接受。伺服器配置，例如在 Apache 中啟用 PUT 動詞，可能是必要的，如 [PHP 手冊中 PUT 方法支持](https://www.php.net/manual/en/features.file-upload.put-method.php) 中所指出的。

#### 比較分析

為了說明兩種方法的不同，考慮以下表格比較這兩種方法：

| 方面                  | POST 方法與 Multipart/Form-Data          | PUT 方法與原始內容                  |
|-------------------------|----------------------------------------|---------------------------------------|
| **使用情況**            | 網頁表單、多個文件、元數據            | RESTful API、單個文件更新             |
| **複雜度**          | 较高（邊界處理、多個部分） | 较低（直接內容）               |
| **效率**          | 中等（編碼開銷）           | 较高（無編碼）                 |
| **伺服器支持**      | 普遍支持                      | 可能需要配置            |
| **示例標頭**     | `Content-Type: multipart/form-data; boundary=abc123` | `Content-Type: text/plain`           |
| **請求體**        | 由邊界分隔的部分          | 原始文件內容                     |

這張表格突出了 multipart/form-data 在網頁交互中的多功能性，而 PUT 方法在 API 驅動的上傳中更高效，具體取決於伺服器功能。

#### 實現細節和陷阱

##### 邊界選擇和文件內容
在 multipart/form-data 中，選擇邊界字符串至關重要，以避免與文件內容衝突。如果邊界出現在文件中，可能會導致解析錯誤。現代庫通過生成隨機邊界來處理這一點，但手動實現需要小心。對於二進制文件，內容以原樣傳輸，保留所有字節，這對於保持文件完整性至關重要。

##### 文件大小和性能
兩種方法都必須考慮伺服器施加的文件大小限制。multipart/form-data 請求可能會變得很大，包含多個文件，可能超過伺服器限制或導致內存問題。PUT，雖然更簡單，也需要流處理大文件，以避免將整個內容加載到內存中，如 [HTTPie 文件上傳文檔](https://httpie.io/docs/cli/file-upload-forms) 中所討論的。

##### 錯誤處理和安全性
發送請求後，客戶端應檢查 HTTP 狀態碼。成功通常由 200（OK）或 201（已創建）表示，而錯誤如 400（錯誤請求）或 403（禁止）表示問題。安全性至關重要，因為文件上傳可能被利用進行攻擊，如上傳惡意可執行文件。伺服器應驗證文件類型，掃描惡意軟件並限制上傳目錄，如 [Stack Overflow 關於 HTTP 文件上傳安全性的討論](https://stackoverflow.com/questions/8659808/how-does-http-file-upload-work) 中所概述的。

#### 各語言的實際示例

各種編程語言提供庫來簡化 HTTP 文件上傳。例如，Python 的 `requests` 庫處理 multipart/form-data 如下：

```python
import requests
files = {'file': open('example.txt', 'rb')}
response = requests.post('https://example.com/upload', files=files)
```

對於 PUT，curl 可以用作 [Stack Overflow 中測試 PUT 上傳](https://stackoverflow.com/questions/5143915/test-file-upload-using-http-put-method) 中所示：

```bash
curl -X PUT "https://example.com/files/123" --upload-file example.txt
```

這些示例展示了抽象，但理解底層 HTTP 結構對於故障排除和自定義實現至關重要。

#### 結論

總結來說，HTTP 文件上傳可以通過 POST 方法和 multipart/form-data 來實現，用於多功能的網頁表單交互，或者使用 PUT 方法來實現高效的 API 更新，每種方法都有其獨特的優勢和要求。伺服器配置、文件大小和安全性考慮是關鍵，確保穩健的實現。有關更多閱讀，請參閱 [Medium 上的 POST 文件上傳指南](https://medium.com/@API4AI/post-a-file-via-http-request-the-ultimate-guide-b23fb70a3f73) 以獲取各語言的實際示例。

### 關鍵引用
- [如何將文件上傳到網絡伺服器 Learn web development MDN](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Tools_and_setup/Upload_files_to_a_web_server)
- [如何進行 HTTP 文件上傳 Stack Overflow](https://stackoverflow.com/questions/8659808/how-does-http-file-upload-work)
- [通過 HTTP 請求上傳文件：終極指南 by API4AI Medium](https://medium.com/@API4AI/post-a-file-via-http-request-the-ultimate-guide-b23fb70a3f73)
- [HTTP REST API 文件上傳 Phil Sturgeon](https://philsturgeon.com/http-rest-api-file-uploads/)
- [PHP PUT 方法支持手冊](https://www.php.net/manual/en/features.file-upload.put-method.php)
- [curl 測試使用 HTTP PUT 方法上傳文件 Stack Overflow](https://stackoverflow.com/questions/5143915/test-file-upload-using-http-put-method)
- [文件上傳表單 HTTPie 3.2.4 最新文檔](https://httpie.io/docs/cli/file-upload-forms)