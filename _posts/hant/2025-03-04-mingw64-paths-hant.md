---
audio: false
generated: true
lang: hant
layout: post
title: 處理MINGW64在Windows上的路徑
translated: true
---

MINGW64 是 MSYS2 計劃的一部分，提供 Windows 上的類 Unix 環境，讓你可以使用 bash shell 命令和 Unix 风格的工具。在這個環境中工作的關鍵方面之一是處理文件路徑，特別是因為 Windows 和 Unix 系統使用不同的約定。以下，我將解釋如何在 MINGW64 中管理路徑，提供示例（包括包含空格的情況），並澄清何時使用命令的絕對路徑。

#### 1. **MINGW64 中的路徑約定**
- **Windows 路徑**：通常使用反斜杠（例如，`C:\Users`）。
- **Unix 路徑**：使用正斜杠（例如，`/usr/bin`）。在 MINGW64 中，Windows 驅動器被掛載在 `/` 下，所以 `C:\` 變成 `/c/`，`D:\` 變成 `/d/`，依此類推。
- **一般規則**：MINGW64 喜歡使用正斜杠的 Unix 风格路徑。例如，`C:\Program Files` 寫作 `/c/Program Files`。

#### 2. **處理包含空格的路徑**
在類 Unix 的 shell（如 MINGW64 中的 bash shell）中，空格是特殊字符，用於分隔參數。如果路徑包含空格（例如，`Program Files`），你必須防止 shell 誤解。有兩種處理方法：

- **用反斜杠（`\`）轉義空格**：
  - 示例：要變換到 `C:\Program Files`，使用：
    ```bash
    cd /c/Program\ Files
    ```
  - 反斜杠告訴 shell 將空格視為路徑的一部分，而不是分隔符。

- **用引號（`"` 或 `'`）括住路徑**：
  - 示例：使用雙引號：
    ```bash
    cd "/c/Program Files"
    ```
  - 示例：使用單引號：
    ```bash
    cd '/c/Program Files'
    ```
  - 引號確保整個路徑被視為單一實體。雙引號更常見且易讀，雖然單引號也有效（處理特殊字符的方式稍有不同）。

在 MINGW64 中，這兩種方法同樣有效。引號通常更受歡迎，特別是在有多個空格或複雜路徑的情況下。

#### 3. **使用命令的絕對路徑**
在 MINGW64 中，當你輸入命令（例如，`python`）時，shell 會在 `PATH` 環境變量中列出的目錄中搜索它。然而，你可能需要使用命令的**絕對路徑**在這些情況下：

- **存在多個版本**：指定特定工具的版本（例如，特定的 `python.exe`）。
- **命令不在 `PATH` 中**：如果可執行文件不在 `PATH` 中列出的目錄中。
- **避免模糊**：確保執行你打算的確切命令。

使用命令的絕對路徑時，特別是如果它包含空格，你必須像上述描述的那樣處理空格。

#### 4. **示例**
以下是涵蓋一般路徑處理、路徑中的空格和命令絕對路徑的實際示例：

##### **示例 1：變換目錄**
- **目標**：導航到 `C:\Program Files`。
- **命令**：
  ```bash
  cd "/c/Program Files"    # 使用引號
  cd /c/Program\ Files     # 使用轉義
  ```
- **說明**：這兩個命令都有效，因為它們正確處理了 "Program Files" 中的空格。

##### **示例 2：使用絕對路徑運行命令**
- **目標**：運行位於 `C:\Python39\python.exe` 的 `python.exe`，並使用腳本 `script.py`。
- **命令**：
  ```bash
  "/c/Python39/python.exe" script.py
  ```
- **說明**：絕對路徑 `/c/Python39/python.exe` 被引號括住（雖然這裡不嚴格需要，因為沒有空格），並運行特定的 Python 可執行文件。

##### **示例 3：包含空格的命令路徑**
- **目標**：運行位於 `C:\Program Files\Python39\python.exe` 的 `python.exe`。
- **命令**：
  ```bash
  "/c/Program Files/Python39/python.exe" script.py
  ```
- **替代方案**：
  ```bash
  /c/Program\ Files/Python39/python.exe script.py
  ```
- **說明**：由於 "Program Files" 中的空格，需要引號或轉義。這樣可以確保 shell 運行該位置的確切 Python 版本。

##### **示例 4：包含 Windows 路徑參數的命令**
- **目標**：使用 `notepad.exe`（位於 `C:\Windows\notepad.exe`）打開 `C:\My Documents\note.txt`。
- **命令**：
  ```bash
  "/c/Windows/notepad.exe" 'C:\My Documents\note.txt'
  ```
- **說明**：
  - 命令路徑 `/c/Windows/notepad.exe` 使用 Unix 风格的斜杠並被引號括住。
  - 參數 `'C:\My Documents\note.txt'` 使用 Windows 风格的反斜杠，因為 `notepad.exe` 是原生 Windows 程序，期望 Windows 路徑。單引號避免 shell 解釋反斜杠（在雙引號中，你需要 `C:\\My Documents\\note.txt`）。

#### 5. **附加說明**
- **參數的 Unix 與 Windows 路徑**：
  - 為 MINGW64 編譯的命令（例如 Unix 工具）通常期望 Unix 路徑（例如，`/c/users/file.txt`）。
  - 原生 Windows 程序（例如 `notepad.exe`）期望 Windows 路徑（例如，`C:\Users\file.txt`）。檢查命令的文檔或測試兩種格式。
- **使用 `PATH` 簡化**：如果命令在你的 `PATH` 中，可以省略絕對路徑（例如，`notepad` 而不是 `/c/Windows/notepad.exe`），但絕對路徑確保精確。
- **工具如 `cygpath`**：MINGW64 從 MSYS2 繼承了 `cygpath`，它轉換路徑（例如，`cygpath -u "C:\Users"` 輸出 `/c/Users`）。然而，這對於基本使用來說很少需要。

#### 總結
- **MINGW64 中的路徑**：使用 Unix 风格路徑（例如，`/c/Users` 代替 `C:\Users`）。
- **空格**：使用引號（`"/c/Program Files"`）或轉義空格（`/c/Program\ Files`）。
- **命令的絕對路徑**：在指定特定可執行文件時使用；引號路徑包含空格（例如，`"/c/Program Files/app.exe"`）。
- **參數**：匹配路徑風格（Unix 或 Windows）以符合命令的期望。

這些技術將幫助你在 MINGW64 中有效地導航和執行命令，即使路徑複雜。