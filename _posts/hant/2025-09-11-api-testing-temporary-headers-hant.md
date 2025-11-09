---
audio: false
date: 2025-09-11
generated: true
image: false
lang: hant
layout: post
model: mistralai/mistral-medium-3.1
title: 使用臨時標頭的 API 測試
translated: true
type: note
---

在為 Java 專案的 Python 測試套件中測試需要臨時標頭（例如金融標頭）的 API 端點時，`unittest` 和 `pytest` 都是可行的選擇，但 `pytest` 在此場景下具有一些優勢。

## 推薦方法：使用 pytest 夾具

`pytest` 通常更適合此使用案例，因為：
- 它具有更強大的夾具管理功能
- 設定/拆卸的語法更簡潔
- 對依賴注入的支援更好
- 測試組織更靈活

以下是實現方式：

### 1. 使用 pytest 的基本結構

```python
import pytest
import requests

@pytest.fixture
def financial_header():
    # 設定 - 建立標頭
    headers = {
        "X-Financial-Id": "test_123",
        "X-Transaction-Type": "payment",
        "Authorization": "Bearer test_token"
    }
    yield headers  # 此處執行測試

    # 拆卸 - 刪除標頭（如需要）
    # 這可能涉及呼叫清理 API 端點
    cleanup_url = "http://your-api/cleanup"
    requests.post(cleanup_url, headers=headers)

def test_api_with_header(financial_header):
    # 在測試中使用標頭
    response = requests.get(
        "http://your-api/endpoint",
        headers=financial_header
    )

    # 驗證回應
    assert response.status_code == 200
    assert "expected_field" in response.json()
```

### 2. 多測試階段的進階範例

```python
import pytest
import requests

class FinancialHeaderManager:
    def __init__(self):
        self.header = None
        self.created = False

    def create(self):
        # 呼叫 API 建立標頭
        response = requests.post("http://your-api/headers", json={
            "type": "financial",
            "metadata": {"test": True}
        })
        self.header = response.json()["header"]
        self.created = True
        return self.header

    def delete(self):
        if self.created:
            requests.delete(
                "http://your-api/headers",
                headers={"X-Header-Id": self.header["id"]}
            )
            self.created = False

@pytest.fixture
def header_manager():
    manager = FinancialHeaderManager()
    manager.create()
    yield manager
    manager.delete()

def test_header_lifecycle(header_manager):
    # 測試建立
    assert header_manager.created
    assert "X-Financial-Id" in header_manager.header

    # 測試使用
    response = requests.get(
        "http://your-api/protected",
        headers=header_manager.header
    )
    assert response.status_code == 200

    # 測試驗證（如 API 具有驗證端點）
    validation = requests.post(
        "http://your-api/validate",
        headers=header_manager.header
    )
    assert validation.json()["valid"]
```

### 3. 如偏好使用 unittest

雖然推薦 pytest，但以下是使用 unittest 的實現方式：

```python
import unittest
import requests

class TestFinancialAPI(unittest.TestCase):
    def setUp(self):
        # 建立標頭
        self.header = {
            "X-Financial-Id": "test_123",
            "X-Transaction-Type": "payment"
        }
        # 如需要呼叫 API 建立：
        # response = requests.post(...)
        # self.header = response.json()

    def tearDown(self):
        # 刪除標頭
        requests.delete(
            "http://your-api/headers",
            headers={"X-Header-Id": self.header["X-Financial-Id"]}
        )

    def test_api_with_header(self):
        response = requests.get(
            "http://your-api/endpoint",
            headers=self.header
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("expected_field", response.json())
```

## 最佳實踐

1. **對複雜設定/拆卸使用 pytest 夾具** - 比 unittest 的 setUp/tearDown 更靈活
2. **隔離測試依賴** - 每個測試應保持獨立
3. **考慮使用 requests Session** 以提升測試效能
4. **為不穩定測試添加重試邏輯**（如需要）
5. **使用環境變數** 區分不同測試環境
6. **考慮使用模擬** 如不需測試實際 Java 後端

## 額外建議

1. 對於更複雜的場景，可考慮使用：
   - `pytest-xdist` 用於並行測試執行
   - `responses` 函式庫用於模擬 HTTP 請求（如需要）
   - `pytest-html` 用於更好的測試報告

2. 如 Java API 有特定要求，您可能需要：
   - 處理 CSRF 令牌
   - 管理會話/cookies
   - 處理速率限制

您是否需要我詳細說明此測試方法的任何特定方面？