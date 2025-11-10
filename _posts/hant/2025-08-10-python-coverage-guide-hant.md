---
audio: false
generated: true
image: false
lang: hant
layout: post
title: Python 覆蓋指南要點
translated: true
type: note
---

這是一份實用且專注於開發的 **coverage** (coverage.py) 套件介紹——它測量什麼、如何有效使用，以及您真正需要關注的設定選項。

# 什麼是 coverage.py

* 一個 Python 工具，用於**測量在測試或任何執行期間，您的程式碼中有哪些行和分支被執行**。
* 輸出**文字、HTML、XML 和 JSON** 報告，讓您能夠看到測試覆蓋的空白區域，並將其整合到 CI 品質閘道中。
* 可與 unittest、pytest、nose 或純腳本一起使用。

# 核心概念（淺顯易懂的解釋）

* **行覆蓋率**：某一行是否至少被執行過一次？
* **分支覆蓋率**：決策中的每個可能分支是否都被執行？（if/else、布林短路、異常、推導式等）
* **原始碼選擇**：僅測量您自己的程式碼，以避免來自 venv/site-packages 的干擾。
* **資料儲存**：執行會建立一個 `.coverage` (SQLite) 資料檔案；您可以合併多次執行的資料。
* **上下文**：使用標籤標記執行（例如，每個測試），以便您可以按測試名稱、命令等切片報告。

# 快速開始

```bash
# 1) 安裝
pip install coverage

# 2) 在 coverage 下執行您的測試（pytest 僅為示例）
coverage run -m pytest

# 3) 查看終端報告（包含未覆蓋的行號）
coverage report -m

# 4) 生成 HTML 報告（在瀏覽器中開啟 htmlcov/index.html）
coverage html

# 可選：機器可讀的報告
coverage xml        # 用於 CI 工具，如 Sonar、Jenkins、Azure DevOps
coverage json       # 用於腳本分析
```

# 推薦的 .coveragerc

在您的儲存庫根目錄建立配置檔案，以確保本地和 CI 環境的結果一致。

```ini
[run]
# 僅測量您的套件以減少干擾
source = src, your_package
branch = True
parallel = True                 # 允許多個進程/執行寫入各自的資料
relative_files = True           # 報告中的路徑更清晰（對 CI 友好）
concurrency = thread, multiprocessing

# 您也可以完全排除檔案或模式
omit =
    */tests/*
    */.venv/*
    */site-packages/*
    */migrations/*

[report]
show_missing = True
skip_covered = False            # 如果希望報告更簡短，可設為 True
fail_under = 90                 # 如果覆蓋率低於 90%，則使 CI 失敗
exclude_lines =
    pragma: no cover            # 忽略行的標準 pragma
    if TYPE_CHECKING:
    raise NotImplementedError

[html]
directory = htmlcov
title = Coverage Report

[xml]
output = coverage.xml

[json]
output = coverage.json

[paths]
# 在合併來自不同機器/容器的資料時很有用
source =
    src
    */workspace/src
    */checkouts/your_repo/src
```

# 測量子進程和並行執行

如果您的程式碼產生子進程（多進程、CLI 工具），請設定**子進程覆蓋率**：

1. 在 `[run]` 中，保持 `parallel = True`。
2. 匯出環境變數，以便子進程使用相同配置自動啟動 coverage：

```bash
export COVERAGE_PROCESS_START=$(pwd)/.coveragerc
```

3. 正常執行您的程式/測試（或仍然透過 `coverage run -m ...` 執行）。
4. 所有執行完成後，合併資料並生成報告：

```bash
coverage combine
coverage report -m
```

> 提示：`concurrency = multiprocessing, thread, gevent, eventlet, greenlet` 讓 coverage 能夠掛鉤到不同的非同步模型。

# 分支覆蓋率和 pragma

* 在 `[run]` 中啟用 `branch = True`。這可以捕捉遺漏的 `else` 分支、短路、異常路徑等。
* 使用尾隨註解忽略無法測試的行：

  * `# pragma: no cover` — 將該行從覆蓋率中排除。
  * 對於複雜的分支，應考慮重構程式碼，而不是過度使用 pragma。

# 上下文（按測試或任務切片覆蓋率）

上下文為執行的行附加標籤，以便您回答：「哪些測試覆蓋了這段程式碼？」

* 使用 pytest 最簡單：

  * 在 `.coveragerc` 中新增 `dynamic_context = test_function`。
  * 然後執行 `coverage html --show-contexts` 或檢查每個上下文的資料，以查看哪個測試觸及了某一行。
* 您也可以透過自訂執行器中的環境變數設定 `dynamic_context = test`（測試節點 ID）或 `dynacontext`。

# Pytest 整合

兩種常見模式：

**A. 原生 coverage CLI（簡單且快速）**

```bash
coverage run -m pytest -q
coverage report -m
```

**B. pytest-cov 外掛（增加 CLI 便利性）**

```bash
pip install pytest-cov
pytest --cov=your_package --cov-branch --cov-report=term-missing --cov-report=html
```

兩者底層都使用 coverage.py；選擇符合您團隊慣例的方式即可。

# 典型的 CI 整合（GitHub Actions 草圖）

```yaml
- name: Install
  run: pip install -U pip coverage pytest

- name: Test with coverage
  run: |
    coverage run -m pytest -q
    coverage report -m
    coverage xml
- name: Enforce threshold
  run: coverage report --fail-under=90
- name: Upload HTML
  if: always()
  uses: actions/upload-artifact@v4
  with:
    name: htmlcov
    path: htmlcov/
```

# 常見陷阱與修復方法

* **報告龐大/緩慢**：限制 `source=` 並使用 `omit=` 跳過 venv、測試、生成的程式碼。
* **CI 與本地路徑不同**：新增 `[paths]` 部分，以便 `coverage combine` 合併資料集。
* **未測量子進程**：設定 `COVERAGE_PROCESS_START` 並保持 `parallel = True`，然後執行 `coverage combine`。
* **非同步框架**：將相關條目新增到 `concurrency = ...`。
* **C 擴充**：coverage.py 測量的是 Python 程式碼，而非原生程式碼——請在 Python 邊界周圍編寫輔助測試。
* **對無法執行的程式碼出現誤報**：使用 `# pragma: no cover` 標記，但應考慮重構以使行為可測試。

# 您實際會用到的實用命令

```bash
coverage erase                       # 清除先前資料
coverage run -m pytest               # 收集資料
coverage report -m                   # 帶有未覆蓋行號的文字摘要
coverage html                        # 開啟 htmlcov/index.html
coverage xml                         # 用於 CI 解析器
coverage json                        # 用於腳本/自動化
coverage combine                     # 合併並行/子進程資料
coverage annotate                    # 每行 .py，顯示哪些行被執行
```

# 何時停止調整

以**有意義的閾值**為目標（例如 80–95%），使用 `fail_under` 強制執行，並將審查重點放在**差異覆蓋率**上（新增/變更的行是否經過測試？）。不要追求難以執行的程式碼（功能旗標、防禦性守衛）達到 100%——請謹慎使用 pragma，並優先選擇更簡單、可測試的設計。

如果您需要，我可以生成一個包含可立即運行的 `.coveragerc`、pytest 配置和失敗閾值閘道的最小示例儲存庫佈局，供您直接使用於專案中。