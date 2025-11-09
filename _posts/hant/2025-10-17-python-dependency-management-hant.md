---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 使用 Poetry 進行 Python 依賴管理
translated: true
type: note
---

### 什麼是 Poetry？

Poetry 是 Python 中用於依賴管理與套件封裝的工具。它能讓你宣告專案所依賴的函式庫，並自動處理安裝、更新及解析這些依賴，同時確保環境的可重現性。

### 主要用途
Poetry 透過單一設定檔（`pyproject.toml`）管理依賴關係，建立 lockfile 以確保在不同機器上安裝的一致性，並支援專案建置以利分發（例如發佈至 PyPI），從而簡化 Python 專案的工作流程。其設計旨在以統一且易用的方式，取代零散的工具如 `pip`、`pipenv` 和 `setuptools`。

### 主要功能
- **依賴解析**：自動安裝及更新依賴，智能解決衝突。
- **Lockfile**：生成 `poetry.lock` 以固定確切版本，實現可重複建置。
- **虛擬環境**：為每個專案建立隔離環境，避免污染全域環境。
- **封裝功能**：建置 wheel 或 sdist 以方便分發。
- **多平台支援**：適用於 Linux、macOS 及 Windows。
- **Shell 整合**：支援 Bash、Fish 和 Zsh 的 Tab 自動完成。
- **Python 3.9+ 相容**：需使用現代 Python 版本。

### 安裝方法
建議使用 `pipx` 在隔離環境中安裝 Poetry（以實現全域存取且無衝突）：

1. 如有需要，先安裝 `pipx`（可透過作業系統套件管理員或 `python -m pip install --user pipx`）。
2. 執行：`pipx install poetry`。

更新方法：`pipx upgrade poetry`。  
解除安裝：`pipx uninstall poetry`。

啟用 shell 自動完成（例如 Bash：`poetry completions bash >> ~/.bash_completion`）。

### 基本用法
初始化新專案：`poetry init`。  
新增依賴：`poetry add requests`。  
根據 lockfile 安裝：`poetry install`。  
執行腳本：`poetry run python script.py`。  
建置套件：`poetry build`。

完整指令請查閱文件。

[Poetry 文件](https://python-poetry.org/docs/)