---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 單元測試與Pytest主要差異
translated: true
type: note
---

這是一份簡潔無表格的對照，專注於日常測試中實際會用到的變化。

# 核心理念與風格

* **unittest**: xUnit 風格（帶有 Java/JUnit 的感覺）。基於類別的測試，具有生命週期鉤子如 `setUp/tearDown`，方法名稱必須以 `test_` 開頭。
* **pytest**: Python 風格且極簡。測試**函數**或類別，豐富的 fixtures，使用簡單的 `assert` 並具備斷言重寫功能。

# 測試探索

* **unittest**: `python -m unittest discover`（或載入測試套件）。尋找 `test*.py` 檔案和 `TestCase` 的子類別。
* **pytest**: `pytest` 自動探索 `test_*.py` 和 `*_test.py` 檔案；尋找 `test_*` 函數和 `Test*` 類別上的方法。

# 斷言

* **unittest**: 許多特定的方法（`assertEqual`, `assertTrue`, `assertRaises`, …）。
* **pytest**: 使用簡單的 `assert`，它會印出清晰的差異對比（「左側 vs 右側」），支援 `pytest.raises`。

# Fixtures 與設定

* **unittest**: `setUp()/tearDown()`, `setUpClass/tearDownClass`, `setUpModule/tearDownModule`。
* **pytest**: 具有作用域（function/class/module/session）的 **Fixtures**、依賴注入、自動使用、終結器。鼓勵小型、可重複使用的設定。

# 參數化

* **unittest**: 無內建功能；需使用迴圈/subTests 或第三方函式庫。
* **pytest**: `@pytest.mark.parametrize` 是一等公民（輸入矩陣、清晰的報告）。

# 跳過、預期失敗、標記

* **unittest**: `@skip`, `@skipIf`, `@expectedFailure`。
* **pytest**: 相同概念加上強大的**標記**（`@pytest.mark.slow`, `xfail`, `filterwarnings`, 自訂標記）和命令列選擇（`-m slow`）。

# 外掛與生態系統

* **unittest**: 內建功能完整但精簡；依賴外部執行器/工具來實現進階功能。
* **pytest**: 龐大的外掛生態系統（`pytest-xdist` 用於並行測試、`pytest-randomly`, `pytest-cov`, `pytest-mock`, `pytest-asyncio`, `pytest-django` 等）。

# Mock

* **unittest**: `unittest.mock` 是標準；隨處可用。
* **pytest**: 使用 `unittest.mock` 或 `pytest-mock` 的 `mocker` fixture（更乾淨的修補與自動清理）。

# 非同步測試

* **unittest**: 自 3.8 版起，具備 `IsolatedAsyncioTestCase`（可用但較冗長）。
* **pytest**: 透過 `pytest-asyncio`（或 trio 的外掛），你可以使用 `@pytest.mark.asyncio` 並獲得對事件迴圈的 fixture 支援。

# 效能與並行

* **unittest**: 無內建並行功能；需使用 `unittest-parallel`/CI 技巧。
* **pytest**: `pytest-xdist -n auto` 是首選方案。

# IDE/CI/覆蓋率

* 兩者都能與 IDE 和 CI 整合。覆蓋率透過 `coverage.py` 實現：

  * **unittest**: `coverage run -m unittest` → `coverage report`。
  * **pytest**: `pytest --cov=your_pkg`（需安裝 `pytest-cov`）。

# 何時選擇哪一個

* **選擇 unittest** 如果：

  * 你只需要標準函式庫（無外部依賴）。
  * 你需要整合到舊版/xUnit 程式碼庫或嚴格的組織政策中。
* **選擇 pytest** 如果：

  * 你想要更快的撰寫速度、更清晰的失敗訊息以及強大的 fixtures/參數化功能。
  * 你能受益於其外掛生態系統和並行化功能。

# 互通性與遷移

你可以在 **pytest** 下執行 **unittest** 測試套件（pytest 能找到 `unittest.TestCase`）。這讓你可以逐步遷移：

1. 開始使用 `pytest` 作為測試執行器。
2. 在現有測試旁新增 pytest 測試。
3. 在需要的地方引入 fixtures/參數化。
4. 之後可選擇性地將舊的 `TestCase` 重構為函數。

# 簡短的並排範例

## 相同的測試

**unittest**

```python
import unittest

class TestMath(unittest.TestCase):
    def setUp(self):
        self.data = [1, 2, 3]

    def test_sum(self):
        self.assertEqual(sum(self.data), 6)

    def test_raises(self):
        with self.assertRaises(ZeroDivisionError):
            1 / 0

if __name__ == "__main__":
    unittest.main()
```

**pytest**

```python
import pytest

@pytest.fixture
def data():
    return [1, 2, 3]

def test_sum(data):
    assert sum(data) == 6

def test_raises():
    with pytest.raises(ZeroDivisionError):
        1 / 0
```

## 參數化

**unittest (subTest)**

```python
import unittest

class TestParity(unittest.TestCase):
    def test_even(self):
        for n in [0, 2, 4]:
            with self.subTest(n=n):
                self.assertEqual(n % 2, 0)
```

**pytest**

```python
import pytest

@pytest.mark.parametrize("n", [0, 2, 4])
def test_even(n):
    assert n % 2 == 0
```

## Mocking

**unittest.mock**

```python
from unittest.mock import patch

@patch("pkg.api.fetch_user", return_value={"id": 1})
def test_uses_api(mock_fetch):
    from pkg.service import get_user
    assert get_user(1)["id"] == 1
    mock_fetch.assert_called_once_with(1)
```

**pytest-mock**

```python
def test_uses_api(mocker):
    mock_fetch = mocker.patch("pkg.api.fetch_user", return_value={"id": 1})
    from pkg.service import get_user
    assert get_user(1)["id"] == 1
    mock_fetch.assert_called_once_with(1)
```

# 實用建議

* 新專案：預設使用 **pytest**，以獲得速度、可讀性和生態系統優勢。
* 舊版/僅限標準函式庫的環境：堅持使用 **unittest**，但考慮透過 **pytest** 執行它，以在不重寫測試的情況下獲得更好的輸出和外掛功能。
* 早期加入 `pytest-xdist` 以加速 CI，並加入 `pytest-cov` 以獲得覆蓋率報告。
* 使用 fixtures 而非大型類別設定；保持它們小巧且可組合。
* 使用標記來組織測試套件（`slow`, `integration`, `db`）並在 CI 階段執行子集。

如果你願意，告訴我你的專案結構和限制（僅限標準函式庫？需要並行？非同步？Django/Flask/FastAPI？），我可以為你勾勒一個極簡且具觀點的測試設定。