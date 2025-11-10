---
audio: false
generated: true
lang: hant
layout: post
title: 修復 Pillow HEIC 支援錯誤
translated: true
type: note
---

錯誤 `cannot identify image file` 表示 Pillow 無法讀取 HEIC 檔案，可能原因如下：
1. **缺少 `libheif` 函式庫**：Pillow 需要 `libheif` 才能處理 HEIC 檔案，您的系統可能未安裝或未正確配置。
2. **HEIC 檔案損毀或格式不相容**：HEIC 檔案可能已損毀，或是 Pillow 無法處理的格式。
3. **Pillow 版本問題**：雖然 Pillow 9.0.0+ 支援 HEIC，但可能存在配置問題或版本過舊。

根據您之前的輸出判斷您使用 macOS，我將提供修正版的 Python 腳本，包含額外的錯誤處理和日誌記錄功能來診斷問題。同時指導您安裝 `libheif` 並驗證 Pillow 的 HEIC 支援。若 Pillow 持續失敗，腳本還包含使用 `ImageMagick`（若已安裝）作為 HEIC 轉換的備援方案。

### 問題修正步驟

#### 1. 安裝 `libheif`
Pillow 依賴 `libheif` 來提供 HEIC 支援。使用 Homebrew 安裝：
```bash
brew install libheif
```
安裝完成後，重新安裝 Pillow 以確保其與 `libheif` 連結：
```bash
pip uninstall pillow
pip install pillow
```

#### 2. 驗證 Pillow 的 HEIC 支援
檢查 Pillow 是否能處理 HEIC 檔案：
```bash
python -c "from PIL import features; print(features.check_feature('heic'))"
```
- 若輸出 `True`，表示 Pillow 具備 HEIC 支援
- 若輸出 `False` 或錯誤，表示 `libheif` 未正確配置，或 Pillow 編譯時未包含 HEIC 支援

#### 3. 檢查檔案完整性
確認 HEIC 檔案未損毀。嘗試在 macOS 的 Preview 等檢視器中開啟其中一個檔案（例如 `IMG_5988.HEIC`）。若無法開啟，檔案可能已損毀，需要重新匯出或取得新副本。

#### 4. 更新版 Python 腳本
更新版腳本功能：
- 使用 Pillow 進行 HEIC 轉換並強化錯誤處理
- 當 Pillow 讀取 HEIC 失敗時，改用 `ImageMagick`（若已安裝）作為備援
- 將詳細錯誤記錄至檔案（`conversion_errors.log`）以供除錯
- 支援 `.heic` 和 `.heif` 副檔名
- 將輸出 JPG 壓縮至約 500KB

```python
import os
import argparse
import subprocess
import logging
from PIL import Image
from datetime import datetime

# 設定日誌記錄
logging.basicConfig(
    filename="conversion_errors.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# 解析命令列參數
parser = argparse.ArgumentParser(description="Convert HEIC images to JPG and compress to ~500KB.")
parser.add_argument("input_dir", help="Directory containing HEIC files")
args = parser.parse_args()

# 定義