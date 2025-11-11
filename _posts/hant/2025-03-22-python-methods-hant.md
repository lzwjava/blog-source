---
audio: false
generated: true
lang: hant
layout: post
title: Python 方法
translated: true
type: note
---

讓我逐步拆解這個 Python 單行指令：

### 指令：
```bash
python -c "from hcloud import Client; c = Client(token='fake'); print(dir(c.servers)); print('\nActions:'); print(dir(c.actions))"
```

### 說明：

1. **`python -c`**：
   - 這告訴 Python 直譯器直接執行後面字串中的程式碼，而不是運行 `.py` 檔案。

2. **`from hcloud import Client`**：
   - 從 `hcloud` 模組匯入 `Client` 類別。`hcloud` 函式庫是官方用於與 Hetzner Cloud API（一家雲端託管供應商）互動的 Python SDK。它允許您以程式方式管理伺服器、操作、映像等。

3. **`c = Client(token='fake')`**：
   - 建立 `Client` 類別的實例，並使用 API token 進行初始化。此處的 `'fake'` 是佔位符 token（非真實 token）。在實際應用中，您需要將 `'fake'` 替換為有效的 Hetzner Cloud API token 以驗證對其 API 的請求。

4. **`print(dir(c.servers))`**：
   - `c.servers` 是 `Client` 物件的一個屬性，提供對伺服器相關功能（例如建立、刪除或列出伺服器）的存取。
   - `dir()` 是一個內建的 Python 函式，它將物件所有屬性和方法的名稱以字串列表形式返回。因此，`dir(c.servers)` 列出了您可以對 `servers` 物件執行的所有操作（例如 `create`、`get_by_id` 等方法）。
   - 這會將列表列印到控制台，顯示可用於管理伺服器的操作。

5. **`print('\nActions:')`**：
   - 這會列印一個換行符（`\n`），後跟字串 `'Actions:'`，以便將 `dir(c.servers)` 的輸出與下一部分分開，提高可讀性。

6. **`print(dir(c.actions))`**：
   - `c.actions` 是 `Client` 物件的另一個屬性，提供對操作相關功能（例如追蹤重啟伺服器等操作的狀態）的存取。
   - 與之前類似，`dir(c.actions)` 列出了 `actions` 物件的所有可用屬性和方法。
   - 這會將列表列印到控制台，顯示您可以對操作執行的動作。

### 它的作用是什麼？
- 這個指令本質上是一種快速檢查 `hcloud` 函式庫的 `servers` 和 `actions` 模組的方法。它輸出：
  1. 用於管理伺服器（`c.servers`）的所有可用方法和屬性列表。
  2. 用於管理操作（`c.actions`）的所有可用方法和屬性列表。

### 範例輸出：
如果您使用有效的 token（並且已安裝 `hcloud` 函式庫）運行此指令，輸出可能類似這樣（簡化版）：
```
['create', 'delete', 'get_all', 'get_by_id', 'power_off', 'power_on', ...]
Actions:
['get_all', 'get_by_id', 'sort', ...]
```
- 第一行顯示了用於伺服器管理的方法，例如 `create` 或 `delete`。
- 在 "Actions:" 之後，它顯示了用於檢索操作詳情的方法，例如 `get_all`。

### 必要條件：
- 您需要安裝 `hcloud` Python 套件（`pip install hcloud`）。
- 實際功能需要來自 Hetzner Cloud 的真實 API token，但此特定指令僅檢查函式庫，不會進行 API 呼叫。

### 目的：
這可能用於除錯或探索，以便在不閱讀完整文件的情況下查看 `hcloud` 函式庫中有哪些方法可用。

如果您想深入了解任何部分，請告訴我！