---
audio: false
generated: true
lang: hant
layout: post
title: Python Requests 函式庫
translated: true
type: note
---

要完全以 Python 的 `requests` 庫取代 Postman，您可以執行所有常見的 HTTP 操作，例如發送不同類型的請求、處理標頭、處理 JSON 資料、上傳檔案、使用代理伺服器以及斷言回應。以下我將逐步為您介紹每項功能的範例，確保您擁有完整且實用的指南。

### 步驟 1：安裝 Requests 庫
開始之前，請確保已安裝 `requests` 庫。在終端機中執行以下指令：

```bash
pip install requests
```

現在，讓我們深入探討範例。

---

### 發送 HTTP 請求
`requests` 庫支援所有 HTTP 方法，如 GET、POST、PUT、DELETE 等。以下是發送簡單 GET 和 POST 請求的方法：

#### GET 請求
```python
import requests

# 發送 GET 請求
response = requests.get('https://api.example.com/data')

# 輸出狀態碼和回應主體
print("狀態碼:", response.status_code)
print("回應主體:", response.text)
```

#### POST 請求
```python
# 發送不帶資料的 POST 請求
response = requests.post('https://api.example.com/submit')

print("狀態碼:", response.status_code)
print("回應主體:", response.text)
```

---

### 添加標頭
標頭通常用於身份驗證、內容類型或自訂元資料。將它們作為字典傳遞給 `headers` 參數。

```python
# 定義自訂標頭
headers = {
    'Authorization': 'Bearer my_token',
    'Content-Type': 'application/json',
    'User-Agent': 'MyApp/1.0'
}

# 發送帶有標頭的 GET 請求
response = requests.get('https://api.example.com/data', headers=headers)

print("狀態碼:", response.status_code)
print("回應標頭:", response.headers)
print("回應主體:", response.text)
```

---

### 發送 JSON 資料
要在 POST 請求中發送 JSON 資料（類似於在 Postman 的 body 標籤中選擇 JSON），請使用 `json` 參數。這會自動將 `Content-Type` 設為 `application/json`。

```python
# 定義 JSON 資料
data = {
    'key1': 'value1',
    'key2': 'value2'
}

# 發送帶有 JSON 資料的 POST 請求
response = requests.post('https://api.example.com/submit', json=data, headers=headers)

print("狀態碼:", response.status_code)
print("回應 JSON:", response.json())
```

---

### 上傳檔案
要上傳檔案（類似於 Postman 的 form-data 選項），請使用 `files` 參數。以二進位模式（`'rb'`）開啟檔案，並可選擇性地包含其他表單資料。

#### 簡單檔案上傳
```python
# 準備要上傳的檔案
files = {
    'file': open('myfile.txt', 'rb')
}

# 發送帶有檔案的 POST 請求
response = requests.post('https://api.example.com/upload', files=files)

print("狀態碼:", response.status_code)
print("回應主體:", response.text)

# 手動關閉檔案
files['file'].close()
```

#### 帶有表單資料的檔案上傳（推薦方法）
使用 `with` 語句可確保檔案自動關閉：
```python
# 額外的表單資料
form_data = {
    'description': '我的檔案上傳'
}

# 開啟並上傳檔案
with open('myfile.txt', 'rb') as f:
    files = {
        'file': f
    }
    response = requests.post('https://api.example.com/upload', data=form_data, files=files)

print("狀態碼:", response.status_code)
print("回應主體:", response.text)
```

---

### 使用代理伺服器
要透過代理伺服器路由請求（類似於 Postman 的代理設定），請使用帶有字典的 `proxies` 參數。

```python
# 定義代理伺服器設定
proxies = {
    'http': 'http://myproxy:8080',
    'https': 'https://myproxy:8080'
}

# 透過代理伺服器發送請求
response = requests.get('https://api.example.com/data', proxies=proxies)

print("狀態碼:", response.status_code)
print("回應主體:", response.text)
```

---

### 處理與斷言回應
`requests` 庫提供了對回應詳情的簡易存取，例如狀態碼、JSON 資料、標頭和 cookies。您可以使用 Python 的 `assert` 語句來驗證回應，類似於 Postman 的測試腳本。

#### 解析 JSON 回應
```python
response = requests.get('https://api.example.com/data')

# 檢查狀態碼並解析 JSON
if response.status_code == 200:
    data = response.json()  # 將回應轉換為 Python 字典/列表
    print("JSON 資料:", data)
else:
    print("錯誤:", response.status_code)
```

#### 斷言回應詳情
```python
response = requests.get('https://api.example.com/data')

# 斷言狀態碼
assert response.status_code == 200, f"預期 200，但得到 {response.status_code}"

# 解析 JSON 並斷言內容
data = response.json()
assert 'key' in data, "回應中找不到 key"
assert data['key'] == 'expected_value', "數值不匹配"

# 檢查回應標頭
assert 'Content-Type' in response.headers, "缺少 Content-Type 標頭"
assert response.headers['Content-Type'] == 'application/json', "非預期的 Content-Type"

# 檢查 cookies
cookies = response.cookies
assert 'session_id' in cookies, "缺少 Session ID cookie"

print("所有斷言通過！")
```

#### 處理錯誤
將請求包裝在 `try-except` 區塊中，以捕獲網路或 HTTP 錯誤：
```python
try:
    response = requests.get('https://api.example.com/data')
    response.raise_for_status()  # 對於 4xx/5xx 錯誤拋出異常
    data = response.json()
    print("資料:", data)
except requests.exceptions.RequestException as e:
    print("請求失敗:", e)
```

---

### 綜合範例
以下是一個結合標頭、檔案上傳、代理伺服器和回應斷言的完整範例：

```python
import requests

# 定義標頭
headers = {
    'Authorization': 'Bearer my_token'
}

# 表單資料和檔案
form_data = {
    'description': '我的檔案上傳'
}

# 代理伺服器設定
proxies = {
    'http': 'http://myproxy:8080',
    'https': 'https://myproxy:8080'
}

# 發送帶有檔案上傳的請求
try:
    with open('myfile.txt', 'rb') as f:
        files = {'file': f}
        response = requests.post(
            'https://api.example.com/upload',
            headers=headers,
            data=form_data,
            files=files,
            proxies=proxies
        )
        response.raise_for_status()  # 檢查 HTTP 錯誤

        # 解析並斷言回應
        data = response.json()
        assert 'upload_id' in data, "回應中找不到 upload_id"
        print("上傳成功，ID:", data['upload_id'])

except requests.exceptions.RequestException as e:
    print("請求失敗:", e)
```

---

### 可重用函數（取代 Postman 集合）
要模擬 Postman 的已儲存請求或集合，請將邏輯封裝在函數中：

```python
def upload_file(file_path, description, token, proxy=None):
    headers = {'Authorization': f'Bearer {token}'}
    data = {'description': description}
    proxies = {'http': proxy, 'https': proxy} if proxy else None

    try:
        with open(file_path, 'rb') as f:
            files = {'file': f}
            response = requests.post(
                'https://api.example.com/upload',
                headers=headers,
                data=data,
                files=files,
                proxies=proxies
            )
            response.raise_for_status()
            data = response.json()
            assert 'upload_id' in data, "找不到 upload_id"
            return data['upload_id']
    except requests.exceptions.RequestException as e:
        print("請求失敗:", e)
        return None

# 使用方式
upload_id = upload_file('myfile.txt', '我的檔案上傳', 'my_token', 'http://myproxy:8080')
if upload_id:
    print("上傳成功，ID:", upload_id)
```

---

### 額外功能
- **會話**：使用 `requests.Session()` 跨請求持久化 cookies 或標頭。
- **超時**：在請求中添加 `timeout=5`（秒）以避免懸掛。
- **重定向**：透過 `allow_redirects=True/False` 控制。

---

### 總結
使用 `requests` 庫，您可以：
- 發送 HTTP 請求（`get`、`post` 等）
- 包含標頭、JSON 資料和檔案上傳
- 使用代理伺服器
- 解析和斷言回應（狀態、JSON、標頭、cookies）
- 將程式碼組織成可重用的函數

這為您提供了一個程式化、靈活的 Postman 替代方案，適用於腳本編寫和自動化！