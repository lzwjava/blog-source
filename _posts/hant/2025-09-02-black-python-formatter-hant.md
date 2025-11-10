---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 黑色Python代碼格式化工具指南
translated: true
type: note
---

PyPI 上的 `black` 套件是一個 **Python 程式碼格式化工具**。它能自動將你的 Python 程式碼重新格式化，使其遵循一致的風格規範（兼容 PEP 8，但具有更嚴格的規範）。以下是如何使用它：

---

### 1. 安裝 Black

```bash
pip install black
```

如果你想確保始終使用最新的穩定版本：

```bash
pip install -U black
```

---

### 2. 格式化檔案或目錄

對單一檔案執行 Black：

```bash
black my_script.py
```

對整個目錄（遞迴處理）執行 Black：

```bash
black src/
```

預設情況下，它會直接覆蓋原始檔案並輸出格式化後的程式碼。

---

### 3. 檢查格式化而不實際修改

使用 `--check` 參數來檢查檔案是否需要重新格式化：

```bash
black --check my_script.py
```

這在 CI 流程中特別有用，可確保程式碼風格的一致性。

---

### 4. 常用選項

* `--line-length 88` → 變更行長度（預設值：88）。
* `--diff` → 顯示將會變更的內容，但不修改檔案。
* `--skip-string-normalization` → 不改變字串引號的格式。
* `--exclude` → 跳過特定檔案或資料夾。

範例：

```bash
black --line-length 100 --diff src/
```

---

### 5. 整合應用

* **IDE 支援**：Black 可作為外掛在 PyCharm、VS Code、Vim、Emacs 等編輯器中使用。
* **Pre-commit 掛鉤**：將 Black 加入 `.pre-commit-config.yaml`，讓程式碼在提交前自動格式化：

  ```yaml
  repos:
    - repo: https://github.com/psf/black
      rev: stable
      hooks:
        - id: black
  ```
* **CI/CD**：在 CI 流程中加入 `black --check .` 指令。

---

👉 需要我進一步示範如何在 **VSCode 或 PyCharm 中設定自動格式化**，讓您無需手動執行 `black` 嗎？