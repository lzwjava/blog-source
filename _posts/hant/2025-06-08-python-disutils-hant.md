---
audio: false
generated: true
lang: hant
layout: post
title: 修復 Python distutils 模組找不到錯誤
translated: true
type: note
---

出現此錯誤是因為您的環境中缺少 Python 標準庫中的 `distutils` 模組。這在精簡版 Python 安裝中很常見。以下是解決方法：

### 解決方案：
1. **安裝 Python 開發工具**（包含 `distutils`）：
   ```bash
   sudo apt update && sudo apt install python3-distutils python3-dev
   ```

2. **重新安裝 `setuptools`**（以確保正常功能）：
   ```bash
   pip install --upgrade --force-reinstall setuptools
   ```

3. **重新嘗試安裝您的需求檔案**：
   ```bash
   pip install -r requirements.local.txt
   ```

### 為何有效：
- `python3-distutils` 提供缺失的 `distutils` 模組
- `python3-dev` 包含必要的標頭檔/建置工具
- 重新安裝 `setuptools` 可解決任何殘留的配置問題

若您處於虛擬環境中，請在安裝系統套件後重新建立環境，以確保環境能存取所需的模組。