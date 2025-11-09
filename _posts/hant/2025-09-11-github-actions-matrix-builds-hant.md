---
audio: false
generated: true
image: false
lang: hant
layout: post
model: openai/gpt-5
title: GitHub Actions 矩陣建置指南
translated: true
type: note
---

聽起來您想了解如何使用 **GitHub Actions** 的矩陣建置功能來平行執行測試，以及如何在矩陣策略中使用 `fail-fast` 選項。讓我為您詳細說明。

---

### GitHub Actions 中的矩陣建置
**矩陣策略** 允許您使用不同參數平行執行相同的工作——例如，在多個 Python 或 Node 版本上測試，或是在不同的作業系統上進行測試。

最小範例：

```yaml
name: CI

on:
  push:
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.8, 3.9, 3.10]
        os: [ubuntu-latest, windows-latest]
      fail-fast: false
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python-version }}
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run tests
        run: pytest
```

---

### 重點說明

- **`matrix`:** 定義用於建立工作組合的變數。  
  上述範例會執行所有 (`python-version`, `os`) 組合的測試。

- **平行執行:** 矩陣產生的每個工作預設會**平行**執行。

- **`fail-fast`:**
  - 預設值為 `true`。這表示如果一個工作失敗，其餘的矩陣工作會被取消。
  - 設定 `fail-fast: false` 如果您希望所有矩陣工作繼續執行，即使其中一個失敗。

  範例：
  ```yaml
  strategy:
    matrix:
      node: [14, 16, 18]
    fail-fast: false
  ```

- **限制總工作數:** 您可以排除某些組合：
  ```yaml
  strategy:
    matrix:
      python-version: [3.8, 3.9, 3.10]
      os: [ubuntu-latest, windows-latest]
    exclude:
      - python-version: 3.8
        os: windows-latest
  ```

---

### 平行執行測試
- 每個**矩陣工作會在自己的執行器上平行執行**，因此您無需特別設定。
- 在每個工作內部，如果您想要**平行執行測試**（例如 pytest 的 `-n auto`），您可以在測試指令層級添加。

範例：
```yaml
- name: Run pytest in parallel
  run: pytest -n auto
```

---

✅ **總結:**
- 使用 `strategy.matrix` 定義不同的參數組合。
- 設定 `fail-fast: false` 如果您希望所有矩陣工作即使有失敗也繼續執行。
- 矩陣工作會自動平行執行。
- 為了加速每個工作內部的執行時間，可使用測試框架的平行化功能（例如 pytest-xdist）。

---

需要我為您展示一個**執行 Node/JavaScript 測試**的實際範例嗎？（包含多個 Node 版本、`fail-fast: false`，以及使用 `npm test` 平行化測試）