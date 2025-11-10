---
audio: false
generated: true
image: false
lang: hant
layout: post
title: Python API 測試框架
translated: true
type: note
---

### 推薦用於 API 端點測試的 Python 測試框架

對於測試以 Java 編寫的伺服器端點（例如 Spring Boot），您可以使用 Python 框架來執行整合或端點測試，方法是發送 HTTP 請求（如 GET、POST、PUT、DELETE 等）並驗證回應碼、標頭和主體內容。由於伺服器是使用 Java，請將其視為黑盒 API，並使用 Python 的 HTTP 客戶端程式庫（如 `requests` 或 `httpx`）與其互動。最常見的設定涉及結合測試執行器框架和 HTTP 程式庫。

以下是一些強力的選擇，根據受歡迎程度和對您使用案例的適用性進行優先排序（基於 2025 年的最新推薦）。我將重點介紹那些支援簡易 HTTP 互動和回應驗證的框架：

#### 1. **pytest（搭配 requests 或 httpx 程式庫）**
   - **推薦原因**：pytest 是 Python 中最受歡迎的測試框架，適用於單元測試、整合測試和 API 測試。它靈活、語法簡單，並支援用於設定/拆卸的 fixture（例如啟動測試伺服器或模擬）。您可以編寫測試來發送 GET/POST 請求，並對狀態碼（例如 200 OK）和 JSON 回應進行斷言。它可透過外掛（如 `pytest-httpx`）擴展以支援非同步測試。
   - **在您的情境中使用方法**：
     - 安裝：`pip install pytest requests`（或對於非同步：`pip install pytest httpx`）。
     - 測試範例：
       ```python
       import requests
       import pytest

       @pytest.fixture
       def base_url():
           return "http://your-java-server:8080"

       def test_get_endpoint(base_url):
           response = requests.get(f"{base_url}/api/resource")
           assert response.status_code == 200
           assert "expected_key" in response.json()

       def test_post_endpoint(base_url):
           data = {"key": "value"}
           response = requests.post(f"{base_url}/api/resource", json=data)
           assert response.status_code == 201
           assert response.json()["status"] == "created"
       ```
     - 優點：可讀性高、有社群外掛、支援平行執行、非常適合 CI/CD。
     - 缺點：需要編寫一些程式碼；非純宣告式。
   - **最適合**：需要自訂邏輯的整合測試。

#### 2. **Tavern**
   - **推薦原因**：Tavern 是一個專門用於 RESTful API 測試的 pytest 外掛。它使用 YAML 檔案以宣告式方式定義測試，無需編寫太多 Python 程式碼即可輕鬆指定 HTTP 方法、負載和預期回應。非常適合端點驗證，包括狀態碼和 JSON 結構檢查。
   - **在您的情境中使用方法**：
     - 安裝：`pip install tavern`。
     - YAML 測試檔案範例：
       ```yaml
       test_name: Test GET endpoint
       stages:
         - name: Get resource
           request:
             url: http://your-java-server:8080/api/resource
             method: GET
           response:
             status_code: 200
             json:
               expected_key: expected_value

       test_name: Test POST endpoint
       stages:
         - name: Post resource
           request:
             url: http://your-java-server:8080/api/resource
             method: POST
             json: { "key": "value" }
           response:
             status_code: 201
             json:
               status: created
       ```
     - 執行方式：`pytest your_test.yaml`。
   - 優點：人類可讀的 YAML、與 pytest 整合、自動重試和驗證。
   - 缺點：對於複雜邏輯，靈活性不如純 Python。
   - **最適合**：專注於端點的快速、宣告式 API 測試。

#### 3. **PyRestTest**
   - **推薦原因**：一個輕量級的 Python 工具，用於使用 YAML 或 JSON 配置進行 REST API 測試。對於基本測試無需編寫程式碼，支援基準測試，非常適合驗證來自外部伺服器（如您的 Java 端點）的 HTTP 回應。
   - **在您的情境中使用方法**：
     - 安裝：`pip install pyresttest`。
     - YAML 範例：
       ```yaml
       - config:
           url: http://your-java-server:8080
       - test:
           name: GET test
           url: /api/resource
           method: GET
           expected_status: [200]
           validators:
             - {jsonpath_mini: 'expected_key', expected: 'expected_value'}
       - test:
           name: POST test
           url: /api/resource
           method: POST
           body: '{"key": "value"}'
           expected_status: [201]
           validators:
             - {jsonpath_mini: 'status', expected: 'created'}
       ```
     - 執行方式：`pyresttest http://base-url test.yaml`。
   - 優點：設定簡單、無需樣板程式碼、便攜。
   - 缺點：與 pytest 相比，社群較有限；工具較舊但仍維護中。
   - **最適合**：微基準測試和簡單的整合測試。

#### 4. **Robot Framework（搭配 RequestsLibrary）**
   - **推薦原因**：一個關鍵字驅動的框架，用於驗收測試和 API 測試。透過 `RequestsLibrary`，它可以原生處理 HTTP 請求，並可擴展用於整合測試。適合偏好可讀性高、非程式碼測試的團隊。
   - **在您的情境中使用方法**：
     - 安裝：`pip install robotframework robotframework-requests`。
     - 測試檔案範例：
       ```
       *** Settings ***
       Library    RequestsLibrary

       *** Test Cases ***
       Test GET Endpoint
           Create Session    mysession    http://your-java-server:8080
           ${response}=    GET On Session    mysession    /api/resource
           Status Should Be    200    ${response}
           ${json}=    To Json    ${response.content}
           Should Be Equal    ${json['expected_key']}    expected_value

       Test POST Endpoint
           Create Session    mysession    http://your-java-server:8080
           ${data}=    Create Dictionary    key=value
           ${response}=    POST On Session    mysession    /api/resource    json=${data}
           Status Should Be    201    ${response}
           ${json}=    To Json    ${response.content}
           Should Be Equal    ${json['status']}    created
       ```
     - 執行方式：`robot your_test.robot`。
   - 優點：基於關鍵字（對非開發人員友好）、內建報告功能。
   - 缺點：語法冗長；對於 Python 純粹主義者學習曲線較陡。
   - **最適合**：BDD 風格的整合測試。

#### 額外提示
- **常用程式庫：requests**：幾乎所有框架都能與其良好搭配進行 HTTP 呼叫。它簡單（`response = requests.get(url)`），能自動處理 JSON，且經過實戰測試。
- **requests 的替代方案：httpx**：如果您需要非同步支援（例如用於高吞吐量測試），請使用它。透過 `pip install httpx` 安裝。
- **Java 伺服器設定**：確保您的 Java 伺服器在本地或遠端運行。對於整合測試，請考慮在 CI/CD 中使用 Docker 啟動 Spring Boot 應用程式。
- **整體最佳選擇**：從 pytest + requests 開始以獲得靈活性。如果您偏好宣告式測試，請選擇 Tavern 或 PyRestTest。
- **注意事項**：由於這些工具使用標準 HTTP，因此適用於跨語言情境。對於結構驗證，請新增如 `jsonschema` 的程式庫。在 CI/CD 中使用 Jenkins 或 GitHub Actions 等工具執行。

### 參考資料
[2025 年您應該轉向的頂級 Python 測試框架](https://medium.com/@hadiyolworld007/top-python-testing-frameworks-in-2025-you-should-switch-to-6ddeb679ccd5)  
[2025 年值得關注的 10 個最佳 Python 測試框架](https://www.lambdatest.com/blog/top-python-testing-frameworks/)  
[2025 年 14 個最佳 Python 自動化測試工具](https://apidog.com/blog/best-python-testing-tools-2025/)  
[2025 年最佳開源 API 測試工具](https://testguild.com/12-open-source-api-testing-tools-rest-soap-services/)