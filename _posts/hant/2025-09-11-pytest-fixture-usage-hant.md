---
audio: false
date: 2025-09-11
generated: true
image: false
lang: hant
layout: post
model: mistralai/mistral-medium-3.1
title: 理解 Pytest 夾具用法
translated: true
type: note
---

## 什麼是 `@pytest.fixture`？

`@pytest.fixture` 是一個裝飾器，用於將函數標記為 **fixture** —— 一種特殊的函數，為測試提供測試數據、設置或拆卸功能。Fixture 是 pytest 最強大的功能之一，也是許多開發者偏好 pytest 而非 Python 內建的 `unittest` 模組的關鍵原因。

## Fixture 的工作原理

Fixture 遵循一個簡單但強大的模式：

1. **設置**：`yield` 語句之前的代碼在測試前運行
2. **測試執行**：測試在到達 `yield` 語句時運行
3. **拆卸**：`yield` 語句之後的代碼在測試完成後運行

### 基礎 Fixture 範例

```python
import pytest

@pytest.fixture
def sample_data():
    # 設置代碼
    data = {"name": "John", "age": 30}
    yield data  # 測試在此處運行
    # 拆卸代碼（測試後運行）
    print("Cleaning up sample data")
```

## 為什麼需要 Fixture

Fixture 解決了幾個常見的測試問題：

1. **測試隔離**：確保每個測試使用全新、可預測的數據運行
2. **代碼重用**：避免在多個測試中重複設置/拆卸代碼
3. **資源管理**：正確處理數據庫連接、文件或網絡連接等資源
4. **測試清晰度**：讓測試函數專注於測試內容，而非設置工作
5. **依賴注入**：為每個測試提供其確切需要的內容

## Fixture 的主要功能

### 1. 依賴注入

Fixture 可以依賴於其他 fixture，形成依賴關係圖：

```python
@pytest.fixture
def database_connection():
    # 設置數據庫連接
    conn = create_connection()
    yield conn
    conn.close()

@pytest.fixture
def user_table(database_connection):
    # 使用 database_connection fixture
    create_table(database_connection, "users")
    yield
    drop_table(database_connection, "users")
```

### 2. 作用域控制

Fixture 可以有不同的生命週期：

```python
@pytest.fixture(scope="function")  # 默認 - 每個測試運行一次
def per_test_fixture():
    pass

@pytest.fixture(scope="module")  # 每個模組運行一次
def per_module_fixture():
    pass

@pytest.fixture(scope="session")  # 每個測試會話運行一次
def per_session_fixture():
    pass
```

### 3. 自動使用 Fixture

Fixture 可以自動運行而無需請求：

```python
@pytest.fixture(autouse=True)
def always_run_this():
    # 這會在模組中的每個測試前運行
    yield
    # 這會在每個測試後運行
```

### 4. 參數化 Fixture

Fixture 可以生成多組數據：

```python
@pytest.fixture(params=[1, 2, 3])
def number(request):
    return request.param  # 將使用 1、2 和 3 運行測試
```

## API 測試的實際範例

以下展示 fixture 如何協助您的金融標頭測試場景：

```python
import pytest
import requests

@pytest.fixture
def financial_header():
    # 設置 - 創建標頭
    headers = create_financial_header()  # 您的創建邏輯
    yield headers  # 測試使用這些標頭在此處運行

    # 拆卸 - 刪除標頭
    delete_financial_header(headers)  # 您的清理邏輯

def test_submit_transaction(financial_header):
    # fixture 自動提供標頭
    response = requests.post(
        "https://api.example.com/transactions",
        headers=financial_header,
        json={"amount": 100}
    )
    assert response.status_code == 201

def test_validate_header(financial_header):
    # 相同的 fixture 用於另一個測試
    response = requests.get(
        "https://api.example.com/validate",
        headers=financial_header
    )
    assert response.json()["valid"] is True
```

## 與 unittest 的比較

| 功能                  | pytest Fixtures                  | unittest setUp/tearDown         |
|-----------------------|----------------------------------|---------------------------------|
| 依賴注入              | ✅ 支持                          | ❌ 不支持                       |
| 作用域控制            | ✅ 函數、類別、模組、會話級別    | ❌ 僅方法/類別級別              |
| 簡潔語法              | ✅ 簡單的裝飾器                  | ❌ 需要繼承                     |
| 測試隔離              | ✅ 每個測試獲得全新的 fixture    | ❌ 共享狀態可能導致問題         |
| 參數化                | ✅ 內建支持                      | ❌ 需要手動實現                 |

## 何時使用 Fixture

在以下情況使用 fixture：
- 設置測試數據或對象
- 管理外部資源（數據庫連接、文件等）
- 測試後執行清理工作
- 共享常見的測試依賴項
- 創建不同的測試環境
- 實現複雜的設置/拆卸邏輯

Fixture 在 API 測試（如您的金融標頭案例）中特別有價值，因為它們有助於以清晰且可預測的方式管理測試資源的生命週期。