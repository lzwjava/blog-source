---
audio: false
generated: true
lang: hant
layout: post
title: PortAudio 與 PyAudio
translated: true
type: note
---

出現此錯誤是因為 **pyaudio** 需要 PortAudio 開發標頭檔才能編譯，而您的系統中缺少這些檔案。以下是解決方法：

### 逐步解決方案：

1. **安裝 PortAudio 開發標頭檔**（pyaudio 所需）：
```bash
sudo apt update && sudo apt install portaudio19-dev
```

2. **安裝 Python 開發工具**（若尚未安裝）：
```bash
sudo apt install python3-dev
```

3. **重新嘗試安裝**：
```bash
pip install -r requirements.local.txt
```

### 若仍遇到 pycrypto 問題：
pycrypto 套件已過時且可能存在相容性問題。請透過修改您的 `requirements.local.txt` 將其替換為 **pycryptodome**：

1. 開啟需求檔案：
```bash
nano requirements.local.txt
```

2. 將 `pycrypto` 替換為：
```
pycryptodome
```

3. 儲存後重新執行安裝：
```bash
pip install -r requirements.local.txt
```

### 解決原理：
- `portaudio19-dev` 提供編譯 pyaudio 所需的 PortAudio 標頭檔
- `python3-dev` 包含必要的 Python 開發標頭檔
- `pycryptodome` 是已棄用 pycrypto 的維護版替代品

### pycrypto 的替代方案（若必須保留）：
若您確實需要使用 pycrypto，請先安裝編譯依賴項：
```bash
sudo apt install build-essential libgmp-dev
pip install pycrypto
```
但請注意，pycrypto 與較新版本的 Python 存在相容性問題。

完成這些步驟後，所有套件應能正確安裝。關於舊版建構的 DEPRECATION 警告屬資訊性提示，不會阻礙安裝程序——這些警告表示這些套件未來需要遷移至 PEP 517 建構標準。