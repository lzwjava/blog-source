---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 已安裝的 Python 套件
translated: true
type: note
---

這些都是正在安裝的 Python 套件（wheel 檔案）—以下是每個套件的簡要說明：

* **safetensors**：一種快速、安全的檔案格式，用於保存/載入張量資料，無需擔心 pickle 的安全問題。
* **typer**：一個現代化的函式庫，用於透過 Python 類型提示來建置 CLI 應用程式。
* **shellingham**：用於偵測當前運行環境中使用的 shell（如 bash、zsh 等）的實用工具。
* **uvicorn**：一個極速的 ASGI 伺服器，用於託管 Python 網路應用程式（例如 FastAPI）。
* **httptools**：低階 HTTP 解析函式庫，被 Uvicorn 等伺服器用於提升速度。
* **uvloop**：以 Cython 實現的超高速 asyncio 事件循環，可無縫替換 asyncio。
* **watchfiles**：檔案監視函式庫，可在檔案系統變更時觸發動作（例如自動重新載入）。
* **airportsdata**：提供機場代碼、名稱和位置的簡易查詢表。
* **astor**：將 Python AST 轉換回原始碼（反之亦然）的工具。
* **blake3**：BLAKE3 加密雜湊演算法的 Python 綁定。
* **cloudpickle**：增強版的 Python 物件 pickler，比標準函式庫的 pickle 能處理更多類型。
* **cupy\_cuda12x**：與 NumPy 相容的 GPU 陣列函式庫，適用於 CUDA 12.x。
* **fastrlock**：一個非常快速的 Python 可重入鎖實作。
* **diskcache**：一個基於磁碟的快取函式庫，可高效持久化 Python 物件。
* **einops**：提供表達力強、可讀性高的張量重塑與重新排序操作。
* **importlib\_metadata**：在運行時存取套件元資料（版本、進入點等）（適用於舊版 Python 的 backport）。
* **zipp**：為 ZIP 壓縮檔提供 pathlib 風格的介面，被 importlib\_metadata 使用。
* **msgspec**：高效能的訊息序列化/反序列化（支援 JSON、Msgpack 等）。
* **nest\_asyncio**：允許嵌套 asyncio 事件循環（例如用於運行 notebook）。
* **ninja**：Ninja 建置系統的 Python 綁定（快速、增量建置）。
* **partial\_json\_parser**：用於大型或格式錯誤 JSON 的串流/部分 JSON 解析器。
* **py\_cpuinfo**：收集有關 CPU 的詳細資訊（型號、核心數、頻率等）。
* **python\_json\_logger**：為 Python 的 logging 模組提供的 JSON 格式化工具。
* **pyzmq**：ZeroMQ 高效能訊息傳遞函式庫的 Python 綁定。
* **scipy**：核心科學計算函式庫（最佳化、積分、統計等）。
* **outlines\_core**：「outlines」函式庫的核心工具（處理文件大綱/結構）。
* **xformers**：來自 Meta 的高效率、模組化 transformer（注意力機制）實作。
* **sentencepiece**：無監督文字分詞器/反分詞器（常用於 NLP）。