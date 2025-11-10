---
audio: false
generated: true
lang: hant
layout: post
title: 計算目錄中的檔案數量
translated: true
type: note
---

要計算目錄中的檔案數量，你可以根據作業系統和工具使用多種方法。以下是最常見的幾種做法：

### **在 Windows 上（命令提示字元）**
```cmd
dir /a-d | find /c /v ""
```
- 列出所有檔案（不包括目錄）並統計行數，排除空行。

### **在 Windows 上（PowerShell）**
```powershell
(Get-ChildItem -File).Count
```
- 僅擷取檔案並進行計數。

### **在 Linux/macOS 上（終端機）**
```bash
ls -l | grep ^- | wc -l
```
- 列出檔案（`ls -l`），篩選出常規檔案（`grep ^-`），然後進行計數（`wc -l`）。

或者更簡單的方式：
```bash
find . -maxdepth 1 -type f | wc -l
```
- 僅尋找當前目錄中（`-maxdepth 1`）的檔案（`-type f`）並進行計數。

### **使用 Python**
```python
import os
file_count = len([f for f in os.listdir('.') if os.path.isfile(f)])
print(file_count)
```
- 列出目錄內容，檢查是否為檔案，然後進行計數。

請根據你的環境選擇合適的方法。如果你需要針對特定作業系統或工具的詳細說明，請告訴我！