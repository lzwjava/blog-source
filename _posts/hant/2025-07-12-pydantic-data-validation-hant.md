---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: Pydantic 數據驗證概覽
translated: true
type: note
---

### Pydantic 函式庫
Pydantic 是一個熱門的開源 Python 函式庫，主要用於資料驗證與解析。它利用 Python 的型別提示功能，自動根據定義的結構描述驗證輸入資料（如 JSON 或字典），在可能的情況下進行型別轉換，並在資料不匹配時提供清晰的錯誤訊息。舉例來說，它能確保整數字段不會被傳遞為字串（除非特別指定）。該函式庫被廣泛應用於 FastAPI 等網路框架中，用於處理 API 請求與回應。

- **主要功能**：支援複雜型別（例如列舉、聯合型別）、自訂驗證器，以及序列化/反序列化。
- **安裝與使用**：透過 `pip install pydantic` 安裝。基礎範例：
  ```python
  from pydantic import BaseModel

  class User(BaseModel):
      id: int
      name: str

  user = User(id='123', name='Alice')  # 將 '123' 轉換為整數
  print(user.dict())  # 輸出：{'id': 123, 'name': 'Alice'}
  ```

### Pydantic-Core
Pydantic-core 是 Pydantic 底層的高效能引擎。它採用 Rust 語言編寫（透過 PyO3 綁定），能提供比純 Python 實現更快速的資料驗證。它並非設計給使用者直接呼叫，而是由 Pydantic 自動調用。這樣的區分使得維護與優化更加容易，例如在處理型別轉換的邊界案例時，不會拖慢主函式庫的速度。

- **與 Pydantic 的關係**：可將 Pydantic 視為 Pydantic-core 的使用者友善 API 封裝層。Pydantic-core 的升級能提升效能，且無需更改公開 API。
- **重要性**：效能測試顯示，Pydantic-core 的驗證速度比 Marshmallow 或 Django Forms 等替代方案快 10 到 100 倍。

### Python 中的型別提示
`typing` 模組是 Python 標準函式庫的一部分（透過 PEP 484 於 Python 3.5+ 引入），提供為程式碼添加型別提示的工具。這些提示不會在執行時強制執行規則，但能提升程式碼可讀性、啟用 IDE 支援（例如自動完成、錯誤檢測），並讓 mypy 等靜態型別檢查工具能及早捕捉錯誤。

- **常見組件**：包含 `List[str]`（字串列表）、`Union[int, str]`（多重型別）、`Optional[int]`（`int | None`），以及泛型如 `Dict[str, Any]`。
- **與 Pydantic 的關聯**：Pydantic 直接建構在 `typing` 註解之上。例如 `class Model(BaseModel): x: int` 這樣的模型會使用 `typing` 來定義預期型別，而 Pydantic 則據此進行驗證。若沒有 `typing`，Pydantic 將無法運作，因為其型別驅動的驗證機制依賴這些提示。

### 三者間的關聯
Pydantic 結合了 `typing` 的型別提示與 Pydantic-core 的高速效能，以宣告式方法驗證資料。例如，一個 API 端點可能會使用帶有 `typing` 型別註解的 Pydantic 模型，並依賴 Pydantic-core 進行高效驗證。這個生態系統支援現代 Python 模式（如資料類別與非同步框架），使其成為型別安全資料處理的重要工具。如需進階細節，請查閱官方 Pydantic 文件或 GitHub 專案。