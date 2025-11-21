---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4.1-fast
title: FineWeb 2013 數據集概要
translated: true
type: note
---

**CC-MAIN-2013-20**（2013年夏季資料庫）在 FineWeb 資料集中的資訊：

- **.parquet 檔案數量**：約 **460–500** 個  
  （檔案採用分片儲存且大小不一：多數約 ~1 GB，部分較大檔案可達 ~2 GB。目錄總容量為 **422 GB**，因此 422 ÷ ~0.9 GB 平均値 ≈ 460–480 個分片。命名方式為依序從 `000_00000.parquet` 至約 `000_004xx.parquet`。）

- **所有 parquet 檔案的總大小**：**422 GB**

- **使用 GPT 風格分詞器編碼後的詞元數量**（GPT-4 使用的 cl100k_base 或 FineWeb 報告中使用的舊版 GPT-2 分詞器）：  
  **1445 億詞元**（經過 FineWeb 的清理、過濾與去重處理流程後）

注意：原始未處理的 Common Crawl 資料庫規模遠較龐大（過濾前約有 3930 億詞元），但 FineWeb 僅保留高品質的英文文本，因此這個 2013 年的舊資料庫經處理後會大幅縮減。

若您下載整個目錄（例如透過 `huggingface-cli download` 或循環讀取所有分片的腳本），最終將獲得約 422 GB 的 parquet 檔案，其中包含 1445 億個可供訓練使用的詞元。

[FineWeb 資料集卡片（含各資料庫詞元數量表格）](https://huggingface.co/datasets/HuggingFaceFW/fineweb)  
[HF 上的 CC-MAIN-2013-20 目錄（顯示總容量）](https://huggingface.co/datasets/HuggingFaceFW/fineweb/tree/main/data/CC-MAIN-2013-20)