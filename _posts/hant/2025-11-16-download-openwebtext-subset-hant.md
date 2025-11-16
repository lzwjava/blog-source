---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 透過Hugging Face下載OpenWebText子集
translated: true
type: note
---

您所提及的資料集存放於 Hugging Face 平台，倉庫 ID 為 `Skylion007/openwebtext`。特定檔案 `subsets/urlsf_subset00.tar` 可公開存取（無需驗證），因此您可使用 Hugging Face CLI 工具（`huggingface-cli`）下載。方法如下：

### 前置準備
- 若尚未安裝 Hugging Face Hub CLI，請先執行：
  ```
  pip install huggingface_hub
  ```
- （可選）若您的系統已將 `huggingface-cli` 指令別名為 `hf`（部分系統常見設定），可直接使用此簡稱。否則請使用完整的 `huggingface-cli` 前綴。

### 下載指令
在終端機中執行：
```
huggingface-cli download Skylion007/openwebtext subsets/urlsf_subset00.tar --local-dir ./openwebtext
```
- 此指令會將檔案下載至 `./openwebtext/subsets/urlsf_subset00.tar`（並自動建立 `subsets` 子目錄）
- 檔案體積龐大（未壓縮約 1.5 GB，且為 tar 封裝檔），請確保磁碟空間充足與網路連線穩定
- 若希望直接下載至當前目錄（不保留倉庫結構），可添加 `--repo-type dataset` 參數（此處雖已隱含識別）或調整 `--local-dir` 設定

### 使用 Python（替代方案）
若傾向透過 Python 腳本操作（使用 `huggingface_hub` 程式庫）：
```python
from huggingface_hub import hf_hub_download

# 下載至當前目錄
hf_hub_download(
    repo_id="Skylion007/openwebtext",
    filename="subsets/urlsf_subset00.tar",
    local_dir="./openwebtext",  # 可選參數：指定基礎目錄
    repo_type="dataset"
)
```
請先安裝程式庫：`pip install huggingface_hub`。

### 注意事項
- 此為 OpenWebText（大型網路語料庫）的子集。下載完成後需解壓縮 `.tar` 檔案（例如執行 `tar -xvf subsets/urlsf_subset00.tar`）
- 若下載失敗（如因網路問題），請重試或使用 `--cache-dir` 指定自訂快取位置
- 如需完整資料集或其他子集，請查閱倉庫頁面：https://huggingface.co/datasets/Skylion007/openwebtext

若遇到錯誤，請提供終端機輸出訊息以便除錯！