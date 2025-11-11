---
audio: false
generated: true
lang: hant
layout: post
title: 設定 VSCode 進行 Python 除錯
translated: true
type: note
---

要解決在 Visual Studio Code (VSCode) 中除錯 Python 腳本時出現「no module named `ibm_db_dbi`」錯誤的問題（即使透過命令列直接執行 `python test_db.py` 使用 Python 3.11.8 可以成功導入模組），請按照以下步驟操作。這種差異通常是由於命令列和 VSCode 除錯器之間的 Python 環境或配置不同所引起。以下是修復方法：

---

### 步驟 1：驗證 VSCode 中的 Python 解譯器
此問題最常見的原因是 VSCode 使用的 Python 解譯器與命令列中安裝了 `ibm_db_dbi` 的解譯器不同。

- **檢查 VSCode 中選擇的解譯器：**
  - 查看 VSCode 視窗的左下角。它會顯示當前選擇的 Python 解譯器（例如 "Python 3.11.8" 或路徑如 `/usr/bin/python3.11`）。
  - 點擊它以打開解譯器選擇選單。

- **與命令列進行比較：**
  - 在終端機中執行：
    ```bash
    python --version
    ```
    確保輸出為 "Python 3.11.8"。如果您使用 `python3` 而不是 `python`，請嘗試：
    ```bash
    python3 --version
    ```
    同時，找到此 Python 可執行檔的路徑：
    ```bash
    which python
    ```
    或
    ```bash
    which python3
    ```
    這可能會返回類似 `/usr/local/bin/python3.11` 的路徑。

- **在 VSCode 中選擇正確的解譯器：**
  - 如果 VSCode 中顯示的解譯器與 Python 3.11.8 或命令列的路徑不匹配，請選擇正確的解譯器：
    - 在解譯器選擇選單中，選擇 "Python 3.11.8" 或與您命令列 Python 匹配的路徑（例如 `/usr/local/bin/python3.11`）。
    - 如果未列出，請點擊「Enter interpreter path」並手動輸入 Python 3.11.8 可執行檔的路徑。

---

### 步驟 2：確認 `ibm_db_dbi` 已安裝在選定的環境中
由於模組在從命令列執行腳本時正常工作，因此它很可能已安裝在該 Python 環境中。請確認這與 VSCode 解譯器匹配。

- **檢查模組位置：**
  - 在終端機中，使用相同的 Python 可執行檔（例如 `python` 或 `/usr/local/bin/python3.11`），執行：
    ```bash
    pip show ibm_db_dbi
    ```
    查看輸出中的 "Location" 欄位。它可能是類似 `/usr/local/lib/python3.11/site-packages` 的路徑。這是 `ibm_db_dbi` 安裝的位置。

- **確保 VSCode 解譯器具有該模組：**
  - 如果您在步驟 1 中選擇了不同的解譯器，請在終端機中啟動該解譯器：
    ```bash
    /path/to/python3.11 -m pip show ibm_db_dbi
    ```
    將 `/path/to/python3.11` 替換為 VSCode 中的路徑。如果沒有返回任何內容，請安裝該模組：
    ```bash
    /path/to/python3.11 -m pip install ibm_db_dbi
    ```

---

### 步驟 3：調整 VSCode 中的除錯配置
如果解譯器正確但除錯仍然失敗，問題可能出在 VSCode 的除錯環境上。修改 `launch.json` 檔案以確保除錯器使用與命令列相同的環境。

- **打開除錯配置：**
  - 前往 VSCode 的「Run and Debug」視圖（Ctrl+Shift+D 或 macOS 上的 Cmd+Shift+D）。
  - 點擊齒輪圖標以編輯 `launch.json`。如果該檔案不存在，VSCode 會在您開始除錯時建立一個。

- **編輯 `launch.json`：**
  - 確保它包含您的腳本配置。基本範例如下：
    ```json
    {
        "version": "0.2.0",
        "configurations": [
            {
                "name": "Python: Current File",
                "type": "python",
                "request": "launch",
                "program": "${file}",
                "console": "integratedTerminal"
            }
        ]
    }
    ```

- **設定環境變數（如果需要）：**
  - 用於 IBM DB2 資料庫的 `ibm_db_dbi` 模組可能需要環境變數，例如 `LD_LIBRARY_PATH` 或 DB2 特定設定來定位共享函式庫。
  - 在 `python test_db.py` 可正常工作的終端機中，檢查相關變數：
    ```bash
    env | grep -i db2
    ```
    或列出所有變數：
    ```bash
    env
    ```
    尋找如 `DB2INSTANCE` 或 `LD_LIBRARY_PATH` 等變數。
  - 將這些變數添加到 `launch.json` 中的 `"env"` 鍵下。例如：
    ```json
    {
        "version": "0.2.0",
        "configurations": [
            {
                "name": "Python: Current File",
                "type": "python",
                "request": "launch",
                "program": "${file}",
                "console": "integratedTerminal",
                "env": {
                    "LD_LIBRARY_PATH": "/path/to/db2/libraries",
                    "DB2INSTANCE": "db2inst1"
                }
            }
        ]
    }
    ```
    將值替換為您命令列環境中的值。

- **設定 PYTHONPATH（如果需要）：**
  - 如果 `ibm_db_dbi` 位於非標準位置，請透過設定 `PYTHONPATH` 確保除錯器可以找到它。
  - 從 `pip show ibm_db_dbi` 輸出中，記下 "Location"（例如 `/usr/local/lib/python3.11/site-packages`）。
  - 將其添加到 `launch.json`：
    ```json
    "env": {
        "PYTHONPATH": "/usr/local/lib/python3.11/site-packages"
    }
    ```

---

### 步驟 4：測試與疑難排解
- **執行除錯器：**
  - 儲存 `launch.json`，然後按 F5 或點擊綠色的「Start Debugging」按鈕來除錯您的腳本。
  - 檢查 Debug Console 中的錯誤。它可能會顯示使用的 Python 可執行檔（例如 "Starting debug adapter with python executable: /path/to/python"）。

- **驗證可執行檔：**
  - 如果 Debug Console 中的路徑與您預期的 Python 3.11.8 不匹配，請重新檢視步驟 1 以確保選擇了正確的解譯器。

- **在不除錯的情況下測試：**
  - 在不除錯的情況下執行腳本（Ctrl+F5 或「Run Without Debugging」）。如果這樣可以工作但除錯失敗，則問題特定於除錯配置，確認需要調整 `launch.json`。

---

### 最終解決方案
根本原因可能是 VSCode 的除錯器未使用與您命令列執行相同的 Python 環境或設定。透過確保解譯器匹配 Python 3.11.8、驗證 `ibm_db_dbi` 已安裝，並配置 `launch.json` 以包含必要的環境變數或 `PYTHONPATH`，您可以對齊環境。以下是針對您的情況量身定制的完整 `launch.json` 範例：

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "env": {
                "PYTHONPATH": "/usr/local/lib/python3.11/site-packages",
                "LD_LIBRARY_PATH": "/path/to/db2/libraries"
            }
        }
    ]
}
```

根據您的 `pip show ibm_db_dbi` 輸出和命令列環境調整 `PYTHONPATH` 和 `LD_LIBRARY_PATH` 路徑。套用這些變更後，您應該能夠在 VSCode 中除錯腳本，而不會出現「no module named `ibm_db_dbi`」錯誤。

---

由於您使用 Windows 並在 VSCode 的 Python 除錯器中遇到「no module named `ibm_db_dbi`」錯誤，問題很可能是由於除錯器未使用安裝了 `ibm_db_dbi` 的相同 Python 環境，或者缺少必要的配置設定。以下是在 Windows 上解決此問題的步驟，確保您的腳本在 VSCode 的除錯器中正確執行。

---

### 步驟 1：驗證 VSCode 中的 Python 解譯器
如果 VSCode 使用的 Python 解譯器與安裝了 `ibm_db_dbi` 的解譯器不同，則可能發生錯誤。

- **檢查 VSCode 中的目前解譯器：**
  - 查看 VSCode 視窗的左下角。它顯示選擇的 Python 解譯器（例如 "Python 3.11.8" 或路徑如 `C:\Python311\python.exe`）。
  - 點擊它以打開解譯器選擇選單。

- **與命令列進行比較：**
  - 開啟命令提示字元 (cmd.exe) 並輸入：
    ```cmd
    python --version
    ```
    這應顯示 Python 版本（例如 "Python 3.11.8"）。如果 `python` 無效，請嘗試 `py --version` 或根據您的設定進行調整。
  - 找到 Python 可執行檔的路徑：
    ```cmd
    where python
    ```
    這可能會輸出類似 `C:\Python311\python.exe` 的路徑。

- **在 VSCode 中設定正確的解譯器：**
  - 如果 VSCode 解譯器與命令列的版本或路徑不匹配（例如 `C:\Python311\python.exe`），請選擇它：
    - 在解譯器選單中，選擇匹配的版本（例如 "Python 3.11.8"）或路徑。
    - 如果未列出，請選擇「Enter interpreter path」並輸入完整路徑（例如 `C:\Python311\python.exe`）。

---

### 步驟 2：確認 `ibm_db_dbi` 已安裝
假設您的腳本在 VSCode 外部正常工作（例如透過命令提示字元中的 `python test_db.py`），則 `ibm_db_dbi` 很可能已安裝在該 Python 環境中。讓我們驗證並使其與 VSCode 對齊。

- **檢查 `ibm_db_dbi` 的安裝位置：**
  - 在命令提示字元中執行：
    ```cmd
    pip show ibm_db_dbi
    ```
    查看 "Location" 欄位（例如 `C:\Python311\Lib\site-packages`）。這是模組所在的位置。

- **驗證 VSCode 解譯器是否具有該模組：**
  - 如果您在步驟 1 中變更了解譯器，請測試它：
    ```cmd
    C:\path\to\python.exe -m pip show ibm_db_dbi
    ```
    將 `C:\path\to\python.exe` 替換為 VSCode 解譯器路徑。如果沒有顯示輸出，請安裝該模組：
    ```cmd
    C:\path\to\python.exe -m pip install ibm_db_dbi
    ```

---

### 步驟 3：配置 VSCode 中的除錯器
即使解譯器正確，除錯器也可能因環境差異而失敗。我們將調整 `launch.json` 檔案。

- **存取 `launch.json`：**
  - 前往 VSCode 的「Run and Debug」（Ctrl+Shift+D）。
  - 點擊齒輪圖標以開啟或建立 `launch.json`。

- **更新 `launch.json`：**
  - 新增或修改配置，如下所示：
    ```json
    {
        "version": "0.2.0",
        "configurations": [
            {
                "name": "Python: Current File",
                "type": "python",
                "request": "launch",
                "program": "${file}",
                "console": "integratedTerminal"
            }
        ]
    }
    ```

- **新增環境變數（如果需要）：**
  - `ibm_db_dbi` 模組可能需要 DB2 相關設定（例如指向 DB2 DLL 的 `PATH`）。檢查您的命令列環境：
    ```cmd
    set
    ```
    尋找如 `PATH`（包含 DB2 路徑）或 `DB2INSTANCE` 等項目。
  - 將它們添加到 `launch.json`。範例：
    ```json
    {
        "version": "0.2.0",
        "configurations": [
            {
                "name": "Python: Current File",
                "type": "python",
                "request": "launch",
                "program": "${file}",
                "console": "integratedTerminal",
                "env": {
                    "PATH": "C:\\path\\to\\db2\\bin;${env:PATH}",
                    "DB2INSTANCE": "db2inst1"
                }
            }
        ]
    }
    ```
    將 `C:\\path\\to\\db2\\bin` 和 `db2inst1` 替換為您系統中的值。

- **設定 `PYTHONPATH`（如果需要）：**
  - 從 `pip show ibm_db_dbi` 輸出中，記下 "Location"（例如 `C:\Python311\Lib\site-packages`）。
  - 將其添加到 `launch.json`：
    ```json
    "env": {
        "PYTHONPATH": "C:\\Python311\\Lib\\site-packages"
    }
    ```

---

### 步驟 4：測試除錯器
- 儲存 `launch.json`。
- 按 F5 或點擊「Start Debugging」以在除錯器中執行您的腳本。
- 檢查 Debug Console 中的錯誤。它可能會顯示使用的 Python 路徑（例如 `C:\Python311\python.exe`）。如果不正確，請重新檢視步驟 1。
- 如果除錯失敗但在不除錯的情況下執行（Ctrl+F5）可以工作，則問題在於 `launch.json`，請仔細檢查 `env` 設定。

---

### 完整範例
以下是針對您的問題量身定制的 `launch.json`：
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "env": {
                "PYTHONPATH": "C:\\Python311\\Lib\\site-packages",
                "PATH": "C:\\path\\to\\db2\\bin;${env:PATH}"
            }
        }
    ]
}
```
- 將 `PYTHONPATH` 調整為符合您的 `pip show ibm_db_dbi` "Location"。
- 根據您命令列 `set` 輸出中的任何 DB2 路徑更新 `PATH`。

---

### 結論
「no module named `ibm_db_dbi`」錯誤的發生是因為 VSCode 的除錯器與安裝模組的 Python 環境未對齊。透過設定正確的解譯器、確保 `ibm_db_dbi` 可用，並在 `launch.json` 中配置正確的環境變數，您將解決此問題並在 Windows 上的 VSCode 中成功除錯。