---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 黑色：Python 代碼格式化工具指南
translated: true
type: note
---

Black 是由 Python 軟件基金會（PSF）開發的一款固執己見、不妥協的 Python 程式碼格式化工具。它能自動將 Python 程式碼重新格式化為一致的風格，主要基於 PEP 8 的嚴格子集，同時強調可讀性、一致性以及版本控制中的最小差異。通過使用 Black，開發者同意放棄對次要格式化細節的控制，以換取速度、確定性以及減少程式碼審查中關於風格的爭論。Black 確保格式化後的程式碼在各個專案中看起來一致，從而節省時間和精力，讓開發者能專注於更關鍵的開發環節。它支援 Python 3.8 及更高版本，最新穩定版本為 25.1.0（於 2025 年 1 月 29 日發布），該版本引入了 2025 穩定風格，並帶來了如標準化 Unicode 轉義字元大小寫和改進尾隨逗號處理等增強功能。

Black 的哲學優先考慮：
- **一致性**：相似的結構會被格式化為相同形式。
- **通用性**：規則廣泛適用，無特殊情況。
- **可讀性**：專注於易於閱讀的程式碼。
- **差異最小化**：減少 Git 差異中的變更，以加速審查。

因其可靠性和整合能力，Black 在開源和專業專案中被廣泛使用。

## 安裝

Black 可通過 PyPI 獲取，並可使用 pip 安裝。建議在虛擬環境中安裝以實現專案隔離。

- 基本安裝：
  ```
  pip install black
  ```

- 如需額外功能，如 Jupyter Notebook 支援或彩色差異顯示：
  ```
  pip install 'black[jupyter,colorama]'
  ```
  （`d` 額外選項用於 blackd，一個用於編輯器整合的守護行程。）

在 Arch Linux 上，您可以通過套件管理器安裝：`pacman -S python-black`。

Black 也可以通過 conda 或其他套件管理器安裝。安裝後，使用 `black --version` 驗證。

對於開發或測試，您可以克隆 GitHub 儲存庫並以可編輯模式安裝：
```
git clone https://github.com/psf/black.git
cd black
pip install -e .
```

## 使用方法

Black 主要是一個命令列工具。基本命令會就地格式化檔案或目錄：

```
black {source_file_or_directory}
```

如果將 Black 作為腳本執行無效（例如，由於環境問題），請使用：
```
python -m black {source_file_or_directory}
```

### 主要命令列選項

Black 提供各種標誌用於自定義和控制。以下是主要選項的摘要：

- `-h, --help`：顯示幫助並退出。
- `-c, --code <code>`：格式化一串程式碼（例如，`black --code "print ( 'hello, world' )"` 輸出格式化後的版本）。
- `-l, --line-length <int>`：設定行長度（預設值：88）。
- `-t, --target-version <version>`：指定 Python 版本以確保相容性（例如，`py38`，可以指定多個，如 `-t py311 -t py312`）。
- `--pyi`：將檔案視為型別存根（`.pyi` 風格）。
- `--ipynb`：將檔案視為 Jupyter Notebooks。
- `--python-cell-magics <magic>`：識別自定義 Jupyter 魔術指令。
- `-x, --skip-source-first-line`：跳過格式化第一行（適用於 shebangs）。
- `-S, --skip-string-normalization`：不將字符串標準化為雙引號或前綴。
- `-C, --skip-magic-trailing-comma`：忽略尾隨逗號以進行換行。
- `--preview`：啟用下一版本中的實驗性風格變更。
- `--unstable`：啟用所有預覽變更以及不穩定功能（需要 `--preview`）。
- `--enable-unstable-feature <feature>`：啟用特定的不穩定功能。
- `--check`：檢查檔案是否需要重新格式化而不進行變更（如果需要變更，則退出碼為 1）。
- `--diff`：顯示變更的差異而不寫入檔案。
- `--color / --no-color`：對差異輸出進行彩色顯示。
- `--line-ranges <ranges>`：格式化特定的行範圍（例如，`--line-ranges=1-10`）。
- `--fast / --safe`：跳過（`--fast`）或強制執行（`--safe`）AST 安全性檢查（預設：safe）。
- `--required-version <version>`：要求特定的 Black 版本。
- `--exclude <regex>`：通過正則表達式排除檔案/目錄。
- `--extend-exclude <regex>`：添加到預設排除項。
- `--force-exclude <regex>`：即使明確傳遞也排除。
- `--include <regex>`：通過正則表達式包含檔案/目錄。
- `-W, --workers <int>`：設定並行工作進程數（預設：CPU 數量）。
- `-q, --quiet`：抑制非錯誤訊息。
- `-v, --verbose`：顯示詳細輸出。
- `--version`：顯示 Black 版本。
- `--config <file>`：從檔案載入配置。

### 範例

- 格式化單個檔案：`black example.py`
- 檢查而不格式化：`black --check .`
- 顯示差異：`black --diff example.py`
- 格式化 stdin：`echo "print('hello')" | black -`
- 使用自定義行長度格式化：`black -l 79 example.py`
- 格式化 Jupyter Notebook：`black notebook.ipynb`

### 提示與注意事項

- Black 格式化整個檔案；使用 `# fmt: off` / `# fmt: on` 來跳過區塊，或使用 `# fmt: skip` 來跳過行。
- 對於 stdin，使用 `--stdin-filename` 以尊重排除規則。
- Black 是確定性的：相同的輸入總是產生相同的輸出。
- 使用 `--preview` 來測試即將推出的風格，但請注意它們可能會發生變化。

## 配置

Black 可以通過命令列標誌或 `pyproject.toml` 檔案（專案首選）進行配置。在 `pyproject.toml` 中的配置位於 `[tool.black]` 部分下。

### 使用 pyproject.toml

範例：
```
[tool.black]
line-length = 79
target-version = ['py311']
include = '\.pyi?$'
exclude = '''
/(
    \.git
  | \.hg
  | \.mypy_cache
  | \.tox
  | \.venv
  | _build
  | buck-out
  | build
  | dist
)/
'''
skip-string-normalization = true
```

支援的選項鏡像了 CLI 標誌（例如，`line-length`、`skip-string-normalization`）。多值選項如 `target-version` 使用陣列。

### 優先順序

- 命令列標誌覆蓋配置檔案設定。
- 如果未找到 `pyproject.toml`，Black 使用預設值並搜尋父目錄。
- 使用 `--config` 來指定自定義配置檔案。

### 檔案發現與忽略

Black 自動發現目錄中的 Python 檔案，預設情況下尊重 `.gitignore`。使用 `--include`/`--exclude` 進行自定義。它會忽略常見目錄，如 `.git`、`.venv` 等，除非被覆蓋。

對於版本控制，可以與 pre-commit 等工具整合以強制執行格式化。

## Black 程式碼風格

Black 強制執行特定的風格，配置選項有限。關鍵規則：

### 行長度
- 預設值：88 個字元。如果無法斷行（例如，長字符串），則可能超過。

### 字符串
- 偏好雙引號；將前綴標準化為小寫（例如，`r` 在 `f` 之前）。
- 將轉義序列轉為小寫（除了 `\N` 名稱）。
- 處理文檔字符串：修正縮排，移除多餘的空白/換行，保留文字中的製表符。

### 數字字面值
- 語法部分小寫（例如，`0xAB`），數字大寫。

### 換行與運算子
- 在二元運算子之前換行。
- 大多數運算子周圍使用單一空格；對於簡單運算元的單目/冪運算不使用空格。

### 尾隨逗號
- 添加到多行集合/函數參數中（如果使用 Python 3.6+）。
- 「魔術」尾隨逗號如果存在，則會展開列表。

### 註解
- 行內註解前兩個空格；文字前一個空格。
- 保留 shebangs、文檔註解等的特殊間距。

### 縮排
- 4 個空格；與取消縮排的閉合括號匹配。

### 空行
- 最小化空白：函數內單一空行，模組級別雙空行。
- 文檔字符串、類別和函數的特定規則。

### 導入
- 拆分長導入；與 isort 的 `black` 配置檔案相容。

### 其他規則
- 偏好括號而非反斜線。
- 根據檔案標準化行結束符。
- `.pyi` 檔案的簡潔風格（例如，方法之間沒有額外空行）。
- 在預覽模式下折疊導入後的空行。

Black 旨在減少差異並提高可讀性，變更主要用於錯誤修復或新語法支援。

## 整合

Black 與編輯器和版本控制無縫整合，實現自動格式化。

### 編輯器

- **VS Code**：使用 Python 擴充功能並將 Black 設為格式化工具。在 settings.json 中設定 `"python.formatting.provider": "black"`。對於 LSP，安裝 python-lsp-server 和 python-lsp-black。
- **PyCharm/IntelliJ**：
  - 內建（2023.2+）：設定 > 工具 > Black，配置路徑。
  - 外部工具：設定 > 工具 > 外部工具，添加 Black 並使用 `$FilePath$` 參數。
  - 檔案監視器：用於在儲存時自動格式化。
  - BlackConnect 插件用於基於守護行程的格式化。
- **Vim**：使用官方插件（通過 vim-plug：`Plug 'psf/black', { 'branch': 'stable' }`）。命令：`:Black` 進行格式化。自動儲存：將 autocmd 添加到 vimrc。配置變數如 `g:black_linelength`。
- **Emacs**：使用 reformatter.el 或 python-black 套件進行儲存時格式化。
- **其他**：通過插件或擴充功能支援 Sublime Text、JupyterLab、Spyder 等。

### 版本控制

- **Pre-commit Hooks**：添加到 `.pre-commit-config.yaml`：
  ```
  repos:
    - repo: https://github.com/psf/black-pre-commit-mirror
      rev: 25.1.0
      hooks:
        - id: black
          language_version: python3.11
  ```
  對於 Jupyter：使用 `id: black-jupyter`。
- **GitHub Actions**：在工作流程中使用如 `psf/black-action` 的 actions 進行 CI 檢查。
- **Git**：在 pre-commit 腳本或 husky 中執行 Black 以進行強制執行。

## 進階主題

- **預覽和不穩定風格**：使用 `--preview` 用於未來的變更（例如，更好的括號擁抱）。`--unstable` 用於實驗性功能。
- **Blackd**：用於整合的 HTTP 伺服器（`blackd --bind-host 127.0.0.1 --bind-port 45484`）。
- **Jupyter 支援**：格式化筆記本，保留魔術指令。
- **型別存根**：對 `.pyi` 檔案的特別簡潔格式化。
- **相容性**：目標為 Python 3.8+；對舊程式碼使用 `--target-version`。
- **替代方案**：與 autopep8（更靈活但較不固執）或 Ruff（更快，包含 linting）進行比較。

對於故障排除，請查閱官方文件或 GitHub issues 上的 FAQ。

## 參考資料

- [Black 25.1.0 文件](https://black.readthedocs.io/en/stable/)
- [psf/black GitHub 儲存庫](https://github.com/psf/black)
- [Black 程式碼風格](https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html)
- [使用與配置](https://black.readthedocs.io/en/stable/usage_and_configuration/the_basics.html)
- [編輯器整合](https://black.readthedocs.io/en/stable/integrations/editors.html)
- [版本控制整合](https://black.readthedocs.io/en/stable/integrations/source_version_control.html)
- [使用 Black 進行 Python 程式碼格式化 - GeeksforGeeks](https://www.geeksforgeeks.org/python/python-code-formatting-using-black/)
- [如何使用 Black 自動格式化您的 Python 程式碼 - freeCodeCamp](https://www.freecodecamp.org/news/auto-format-your-python-code-with-black/)
- [Black - PyPI](https://pypi.org/project/black/)
- [Python Black 模組簡介 - GeeksforGeeks](https://www.geeksforgeeks.org/introduction-to-python-black-module/)
- [Python 自動格式化工具：Autopep8 vs. Black - Built In](https://builtin.com/data-science/autopep8-vs-black)