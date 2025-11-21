---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4.1-fast
title: FineWeb 數據集 Parquet 檔案數量
translated: true
type: note
---

**FineWeb** 資料集（位於 `HuggingFaceFW/fineweb` 的 15T+ token 英文版本）總共包含**約 35,000 至 50,000** 個 `.parquet` 檔案。

### 詳細說明
- 它由 **96** 個獨立的 Common Crawl 快照（資料傾印，例如 `CC-MAIN-2013-20`、`CC-MAIN-2024-10` 等）組成。
- 每個傾印都儲存在 `/data/` 下的獨立子目錄中，並分割成許多分片的 `.parquet` 檔案，名稱類似 `000_00000.parquet`、`000_00001.parquet`……（以零填充的順序編號）。
- 每個傾印的 parquet 檔案數量因其大小而異：
  - 較小/較舊的傾印（如您腳本中的 `CC-MAIN-2013-20` 範例）通常有 **約 200–1,000** 個檔案。
  - 較大型的近期傾印可能各自包含**數千個**檔案。
- 雖然沒有單一的官方公布總數，但根據社群估算及從傾印大小/token 數量進行的計算，**所有 96 個傾印的總檔案數一致落在約 35k–50k** parquet 檔案左右（完整資料集未壓縮時約為 45–53 TB）。

您的腳本從非常小的 `CC-MAIN-2013-20` 傾印中下載了第 11 到第 20 個分片（共 10 個檔案），但該傾印的總分片數量遠多於此——僅該傾印就有數百個分片。

如果您需要確切數量，可以使用 Hugging Face Hub API（例如使用 `huggingface_hub.list_repo_files`）以程式方式計算，但上述大致數字是人們在下載或處理完整資料集時通常使用的參考值。

[FineWeb 資料集介紹頁面](https://huggingface.co/datasets/HuggingFaceFW/fineweb)  
[FineWeb 資料樹狀結構（傾印範例）](https://huggingface.co/datasets/HuggingFaceFW/fineweb/tree/main/data)