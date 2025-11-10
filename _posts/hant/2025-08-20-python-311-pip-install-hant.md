---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 安裝 Python 3.11 及 pip3.11
translated: true
type: note
---

看起來你在 Ubuntu 系統上安裝了多個 Python 和 pip 版本，而你想安裝 **Python 3.11** 及其對應的 **pip (pip3.11)**。以下是具體步驟：

---

### **1. 安裝 Python 3.11**
首先更新套件清單並安裝 Python 3.11：

```bash
sudo apt update
sudo apt install python3.11
```

驗證安裝：

```bash
python3.11 --version
```

---

### **2. 安裝 Python 3.11 的 pip**
Ubuntu 的預設軟體庫可能不包含 Python 3.11 的 `pip`。你可以透過以下步驟安裝：

#### **選項 A：透過 apt 安裝 pip（如果可用）**
```bash
sudo apt install python3.11-venv python3.11-dev python3-pip
```
如果 `python3-pip` 安裝了其他版本的 pip，請改用**選項 B**。

#### **選項 B：使用 ensurepip 安裝 pip**
```bash
python3.11 -m ensurepip --upgrade
```
這會專門為 Python 3.11 安裝 pip。

#### **選項 C：使用 get-pip.py 安裝 pip**
如果以上方法無效，請使用官方的 `get-pip.py` 腳本：

```bash
curl -sS https://bootstrap.pypa.io/get-pip.py | python3.11
```

---

### **3. 驗證 pip3.11 安裝**
檢查 `pip3.11` 是否可用：

```bash
pip3.11 --version
```
你應該會看到類似輸出：
```
pip 23.x.x from /usr/local/lib/python3.11/site-packages/pip (python 3.11)
```

---

### **4. （可選）建立虛擬環境**
為避免 Python 版本間的衝突，你可以建立虛擬環境：

```bash
python3.11 -m venv myenv
source myenv/bin/activate
```
現在虛擬環境內的 `pip` 將會使用 Python 3.11。

---

### **指令總表**

| 指令 | 用途 |
|---------|---------|
| `sudo apt update` | 更新套件清單 |
| `sudo apt install python3.11` | 安裝 Python 3.11 |
| `python3.11 -m ensurepip --upgrade` | 安裝 Python 3.11 的 pip |
| `pip3.11 --version` | 驗證 pip 安裝 |
| `python3.11 -m venv myenv` | 建立虛擬環境 |

---