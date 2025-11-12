---
audio: false
generated: true
lang: hant
layout: post
title: 在 Windows 上處理 MINGW64 中的路徑
translated: true
type: note
---

MINGW64 作為 MSYS2 專案的一部分，在 Windows 系統上提供了類 Unix 環境，讓您能使用 bash shell 指令與 Unix 風格工具。在此環境中作業的關鍵環節是處理檔案路徑，特別是 Windows 與 Unix 系統使用不同慣例。以下將說明如何在 MINGW64 中管理路徑，提供範例（包含含空格的案例），並釐清何時需使用指令的絕對路徑。

#### 1. **MINGW64 中的路徑慣例**
- **Windows 路徑**：通常使用反斜線（例如 `C:\Users`）。
- **Unix 路徑**：使用正斜線（例如 `/usr/bin`）。在 MINGW64 中，Windows 磁碟機被掛載於 `/` 下，因此 `C:\` 變成 `/c/`，`D:\` 變成 `/d/`，依此類推。
- **通用規則**：MINGW64 偏好使用帶正斜線的 Unix 風格路徑。例如，`C:\Program Files` 應寫為 `/c/Program Files`。

#### 2. **處理含空格的路徑**
在類 Unix shell（如 MINGW64 中的 bash shell）中，空格是分隔參數的特殊字元。若路徑包含空格（例如 `Program Files`），必須防止 shell 誤解。有兩種處理方式：

- **使用反斜線跳脫空格（`\`）**：
  - 範例：要切換到 `C:\Program Files`，請使用：
    ```bash
    cd /c/Program\ Files
    ```
  - 反斜線會告知 shell 將空格視為路徑的一部分，而非分隔符號。

- **用引號包覆路徑（`"` 或 `'`）**：
  - 範例：使用雙引號：
    ```bash
    cd "/c/Program Files"
    ```
  - 範例：使用單引號：
    ```bash
    cd '/c/Program Files'
    ```
  - 引號能確保整個路徑被視為單一實體。雙引號更常見且易讀，雖然單引號也適用（在特殊字元處理上略有差異）。

這兩種方法在 MINGW64 中效果相同。引號通常因清晰度而更受青睞，特別是在處理多個空格或複雜路徑時。

#### 3. **對指令使用絕對路徑**
在 MINGW64 中，當您輸入指令（例如 `python`）時，shell 會在 `PATH` 環境變數列出的目錄中搜尋該指令。但在以下情況中，您可能需要使用指令的**絕對路徑**：

- **存在多個版本**：需指定特定版本的工具（例如某個特定的 `python.exe`）。
- **指令不在 `PATH` 中**：若可執行檔不在 `PATH` 列出的目錄內。
- **避免歧義**：為確保執行的是預期的確切指令。

當對指令使用絕對路徑時，特別是路徑包含空格時，必須按照上述方式處理空格。

#### 4. **範例**
以下實用範例涵蓋一般路徑處理、路徑中的空格，以及絕對指令路徑：

##### **範例 1：切換目錄**
- **目標**：導航至 `C:\Program Files`。
- **指令**：
  ```bash
  cd "/c/Program Files"    # 使用引號
  cd /c/Program\ Files     # 使用跳脫字元
  ```
- **說明**：因正確處理了 "Program Files" 中的空格，兩個指令皆可運作。

##### **範例 2：使用絕對路徑執行指令**
- **目標**：執行位於 `C:\Python39\python.exe` 的 `python.exe` 並帶入 `script.py` 腳本。
- **指令**：
  ```bash
  "/c/Python39/python.exe" script.py
  ```
- **說明**：絕對路徑 `/c/Python39/python.exe` 被引號包覆（雖然此處因無空格而非常必要），並執行特定的 Python 可執行檔。

##### **範例 3：含空格的指令路徑**
- **目標**：執行位於 `C:\Program Files\Python39\python.exe` 的 `python.exe`。
- **指令**：
  ```bash
  "/c/Program Files/Python39/python.exe" script.py
  ```
- **替代方式**：
  ```bash
  /c/Program\ Files/Python39/python.exe script.py
  ```
- **說明**：因 "Program Files" 中有空格，必須使用引號或跳脫字元。這能確保 shell 執行該位置的確切 Python 版本。

##### **範例 4：帶有 Windows 路徑參數的指令**
- **目標**：使用 `notepad.exe`（位於 `C:\Windows\notepad.exe`）開啟 `C:\My Documents\note.txt`。
- **指令**：
  ```bash
  "/c/Windows/notepad.exe" 'C:\My Documents\note.txt'
  ```
- **說明**：
  - 指令路徑 `/c/Windows/notepad.exe` 使用 Unix 風格斜線並以引號包覆。
  - 參數 `'C:\My Documents\note.txt'` 使用 Windows 風格反斜線，因為 `notepad.exe` 是原生 Windows 程式，預期接收 Windows 路徑。單引號可避免 shell 解譯反斜線（若用雙引號則需寫為 `C:\\My Documents\\note.txt`）。

#### 5. **補充說明**
- **參數的 Unix 與 Windows 路徑區別**：
  - 為 MINGW64 編譯的指令（例如 Unix 工具）通常預期 Unix 路徑（例如 `/c/users/file.txt`）。
  - 原生 Windows 程式（例如 `notepad.exe`）則預期 Windows 路徑（例如 `C:\Users\file.txt`）。請查閱指令文件或測試兩種格式。
- **使用 `PATH` 簡化操作**：若指令位於 `PATH` 中，可省略絕對路徑（例如用 `notepad` 取代 `/c/Windows/notepad.exe`），但絕對路徑能確保精確性。
- **如 `cygpath` 等工具**：MINGW64 繼承了 MSYS2 的 `cygpath`，可轉換路徑（例如 `cygpath -u "C:\Users"` 會輸出 `/c/Users`）。但基本使用中很少需要此功能。

#### 總結
- **MINGW64 中的路徑**：使用 Unix 風格路徑（例如用 `/c/Users` 表示 `C:\Users`）。
- **空格處理**：使用引號（`"/c/Program Files"`）或跳脫空格（`/c/Program\ Files`）。
- **絕對指令路徑**：在指定特定可執行檔時使用；若路徑含空格則需引號包覆（例如 `"/c/Program Files/app.exe"`）。
- **參數傳遞**：根據指令預期匹配路徑風格（Unix 或 Windows）。

這些技巧將協助您在 MINGW64 中有效導航與執行指令，即使面對複雜路徑也能游刃有餘。