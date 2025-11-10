---
audio: false
generated: true
image: false
lang: hant
layout: post
title: OpenAI 的 Python 函式庫設計啟示
translated: true
type: note
---

以下是對 `openai/openai-python` 的快速解析，以及你能借鏡來打造優秀 Python 函式庫的經驗。

# 專案結構概覽

* **清晰的「src 佈局」**：程式碼位於 `src/openai`；頂層目錄包含 `tests/`、`examples/`、`scripts/`、`.github/`、`pyproject.toml`、`mypy.ini`、`noxfile.py` 等。這種分離能保持導入路徑整潔，並使測試發現更可預測。（[GitHub][1]）
* **強型別公開介面**：請求使用 `TypedDict`，回應採用 **Pydantic** 模型；提供優質開發體驗且重構更安全。（[GitHub][1]）
* **同步與非同步對等**：`OpenAI` 與 `AsyncOpenAI` 共享相同 API；預設傳輸層為 `httpx`，並可選用 `aiohttp`。（[GitHub][1]）
* **一流的串流處理**：伺服器發送事件在同步與非同步模式下皆支援簡單迭代。（[GitHub][1]）
* **自動分頁**：可迭代的清單端點，使用者無需手動編寫分頁迴圈。（[GitHub][1]）
* **即時/WebSocket 客戶端**：附帶範例與錯誤處理指引的選用子客戶端。（[GitHub][1]）
* **程式碼生成管道**：SDK 透過 OpenAPI 規範生成（經由 Stainless），確保一致性與型別覆蓋率。（[GitHub][1]）

# 可複用的設計要點

* **遵循「單一明確方式」**：提供單一 `Client`（及 `AsyncClient`）並保持方法名稱對稱。使用者不應困惑「該使用哪個類別？」OpenAI SDK 透過 `OpenAI` 與 `AsyncOpenAI` 展現此原則。（[GitHub][1]）
* **可移植的傳輸層**：預設採用 `httpx`，但允許替換 HTTP 後端（例如 `aiohttp`），讓高併發使用者不受限制。（[GitHub][1]）
* **強型別請求與模型**：提供帶型別的請求承載與豐富的回應模型。這能帶來編輯器自動完成、可檢查的範例程式碼，以及更安全的破壞性變更處理。（[GitHub][1]）
* **無摩擦串流處理**：將串流設計為簡單的迭代器/非同步迭代器。無需自訂事件泵。（[GitHub][1]）
* **基於迭代器的分頁**：提供 `for item in client.resource.list(limit=...)` 並惰性載入分頁。這既能保持使用者程式碼簡潔，又能維持效率。（[GitHub][1]）
* **子系統即子客戶端**：將特殊功能（例如即時通訊）置於明確命名的命名空間後（`client.beta.realtime`），以保持主要介面整潔。（[GitHub][1]）
* **善用程式碼生成**：若你的 API 由規範驅動，可透過程式碼生成建立繁瑣的強型別層，並手動打磨易用部分。（[GitHub][1]）

# 可複製的骨架結構

```bash
yourlib/
  pyproject.toml
  noxfile.py
  mypy.ini
  README.md
  CHANGELOG.md
  SECURITY.md
  src/yourlib/
    __init__.py
    _version.py
    _types.py            # TypedDicts, 枚舉
    _errors.py           # 異常層級結構
    _http.py             # httpx 客戶端封裝、重試、超時設定
    _pagination.py       # 通用 Pager[T]
    client.py            # Client + AsyncClient、認證、基礎 URL
    resources/
      __init__.py
      widgets.py         # 資源組（含同步與非同步方法）
    streaming.py         # SSE 輔助工具（同步/非同步）
  tests/
    test_client.py
    test_widgets.py
  examples/
    quickstart.py
    async_quickstart.py
```

## 公開 API (`src/yourlib/__init__.py`)

* 僅重新匯出使用者所需內容：

```python
from .client import Client, AsyncClient
from ._errors import YourLibError, APIError, RateLimitError
__all__ = ["Client", "AsyncClient", "YourLibError", "APIError", "RateLimitError"]
```

## 客戶端結構（同步與非同步）

* 保持相同方法名稱；僅在 `await`/`async` 使用上區別：

```python
# src/yourlib/client.py
import httpx
from .resources.widgets import Widgets
from ._http import HttpTransport

class Client:
    def __init__(self, api_key=None, base_url="https://api.example.com", http_client=None):
        self._transport = HttpTransport(api_key, base_url, http_client or httpx.Client(timeout=30))
        self.widgets = Widgets(self._transport)

class AsyncClient:
    def __init__(self, api_key=None, base_url="https://api.example.com", http_client=None):
        self._transport = HttpTransport(api_key, base_url, http_client or httpx.AsyncClient(timeout=30))
        self.widgets = Widgets(self._transport)
```

## 分頁模式

```python
# src/yourlib/_pagination.py
from typing import AsyncIterator, Iterator, Generic, TypeVar, Callable, Optional
T = TypeVar("T")
class Pager(Generic[T]):
    def __init__(self, fetch: Callable[..., dict], limit: int = 100):
        self._fetch = fetch
        self._limit = limit
        self._cursor = None
    def __iter__(self) -> Iterator[T]:
        while True:
            page = self._fetch(limit=self._limit, cursor=self._cursor)
            for item in page["data"]:
                yield item
            self._cursor = page.get("next_cursor")
            if not self._cursor:
                break
```

公開此功能，讓使用者能透過 `for item in client.widgets.list(limit=50): ...` 操作。（OpenAI 的 SDK 採用相同方法。（[GitHub][1]））

## 串流模式（SSE）

* 以輕量迭代器封裝 `httpx` 的串流功能來產生事件；並提供非同步版本。這能實現如 OpenAI SDK 中所見的直觀 `for event in client.responses.create(..., stream=True)` 使用者體驗。（[GitHub][1]）

# 可擴展的工具鏈與發布流程

* **`pyproject.toml` (PEP 621)** 用於元資料；獨立鎖定開發依賴項。
* **型別檢查**：提供型別標註，在 CI 中執行 `mypy`（其專案庫包含 `mypy.ini`）。（[GitHub][1]）
* **任務執行器**：使用 `nox` 會話執行測試、程式碼檢查、型別檢查與建置（他們使用 `noxfile.py`）。（[GitHub][1]）
* **CI**：在 `.github/` 中使用 GitHub Actions 跨 Python 版本與平台執行測試。（[GitHub][2]）
* **更新日誌與版本管理**：維護人工可讀的日誌；自動化發布流程（他們使用 release-please）。（[GitHub][1]）
* **安全與貢獻文件**：為問題回報者與貢獻者設定明確期望。（[GitHub][1]）

# 文件與範例

* **README 範例**應可執行且方便複製貼上——涵蓋同步、非同步、串流、分頁及任何「特殊傳輸層」（如 `aiohttp`）。OpenAI 的 README 簡潔展示了各項功能。（[GitHub][1]）
* **API 參考**：若為程式碼生成，請發布 `api.md`/參考網站並與版本同步更新。（[GitHub][1]）
* **範例資料夾**：包含最小且聚焦的腳本，以及一個「完整」範例。

# 錯誤、重試與超時（實作要點）

* **錯誤層級結構**：`YourLibError` → `APIError`、`AuthError`、`RateLimitError`、`TimeoutError`。將 HTTP 狀態碼對應至異常；包含請求 ID。
* **重試機制**：冪等操作應在遇到 429/5xx 錯誤時自動採用指數退避與抖動進行重試。
* **超時設定**：設定合理的預設值，並允許在客戶端與單次呼叫層級進行配置。
* **日誌掛鉤**：提供結構化除錯日誌記錄，且不洩漏敏感資訊。

# 封裝與相容性

* **支援 3–4 個活躍的 Python 次要版本**（例如 3.9–3.13），並在 CI 中進行測試。
* **導入時無副作用**；延遲網路/客戶端建立至首次使用時。
* **環境配置**：接受 `API_KEY` 環境變數，但也允許使用者明確傳遞憑證（OpenAI 展示了 `OPENAI_API_KEY` 與 `.env` 使用提示）。（[GitHub][1]）
* **穩定的公開 API**：保持內部實現私有（`_module.py`），在 `__init__.py` 中整潔地重新匯出公開介面。

# 應避免的陷阱

* 將所有內容塞入單一模組；應按資源拆分並保持公開導入穩定。
* 洩漏傳輸層型別；你的資源應依賴於簡化的「傳輸」協議，而非直接依賴 `httpx`。
* 讓非同步功能顯得次要；確保測試與範例同等涵蓋兩者（OpenAI 的對等性是良好範例）。（[GitHub][1]）
* 對於串流處理，勿強迫使用者處理執行緒或回呼——迭代器更簡單。（[GitHub][1]）

若你需要，我可以為具體領域搭建此結構（例如為你的內部 REST 服務提供強型別客戶端，包含同步/非同步、分頁與串流功能），並放入可直接執行的 `nox`、CI 及範例腳本。

[1]: https://github.com/openai/openai-python "GitHub - openai/openai-python: The official Python library for the OpenAI API"
[2]: https://github.com/openai/openai-python/tree/main/.github "openai-python/.github at main · openai/openai-python · GitHub"