---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 解決 Python 版本不符問題
translated: true
type: note
---

明白了 — 你遇到了 **Python 版本不相容** 的問題。

你的日誌顯示：

* `python3` → **3.10.12**
* `python` → **3.13.7**

所以當 Claude Code（或你的研究代理腳本）調用 `python3` 時，它使用的是 3.10 版本，而該版本並未安裝 `pyperclip`。你將 `pyperclip` 安裝到了 3.13 的環境中，因此 3.10 無法識別它。

以下是幾種解決方法：

---

### 1. 使用你想要的 Python 版本運行 Claude Code

如果你希望 Claude Code 始終使用 Python 3.13，請在 shell 中明確設定執行檔：

```bash
export PYTHON_EXECUTABLE=$(which python)
```

或者如果你特別需要 `python3`：

```bash
export PYTHON_EXECUTABLE=$(which python3)
```

然後在啟動 Claude Code 或你的代理時，它就能讀取該環境變數。

---

### 2. 將 `python3` 指向 Python 3.13

在 Ubuntu 上，你可以更新 `alternatives` 系統：

```bash
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.13 2
sudo update-alternatives --config python3
```

然後選擇 Python 3.13。

---

### 3. 將 `pyperclip` 安裝到 Python 3.10

如果你想繼續對 `python3` 使用 3.10 版本，只需在該環境中安裝：

```bash
python3 -m pip install --user pyperclip
```

這能確保 `python3` 可以導入該模組。

---

### 4. 使用虛擬環境

最佳實踐：創建一個包含你所需 Python 版本的 venv，並在其中運行 Claude Code：

```bash
python3.13 -m venv ~/.venvs/claude
source ~/.venvs/claude/bin/activate
pip install pyperclip
```

然後在此 venv 內啟動你的代理，這樣它就會始終使用 3.13。

---

👉 請問：你希望 Claude Code **始終使用 Python 3.13 運行**，還是願意繼續將 3.10 作為 `python3` 但僅修復缺失的模組？