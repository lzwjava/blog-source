---
audio: false
generated: true
lang: hant
layout: post
title: 複製檔案與目錄結構
translated: true
type: note
---

根據你的 `find` 指令輸出，你想要將所有 `.log` 檔案複製到 `/Users/lzwjava/projects/logs`，同時保留它們的目錄結構。舉例來說，像 `./CoreSimulator/FC275C39-59CC-4483-A64E-5D459D7A1D57/system.log` 這樣的檔案，最終應該成為 `/Users/lzwjava/projects/logs/CoreSimulator/FC275C39-59CC-4483-A64E-5D459D7A1D57/system.log`。我將展示如何使用 `find` 結合 `cp` 或 `rsync` 來達成此目標，確保目錄層級結構得以保留。

---

### **解決方案 1：使用 `find` 搭配 `cp`**
你可以使用 `find` 來定位 `.log` 檔案，並使用帶有 `--parents` 選項的 `cp` 來複製它們，同時保留其目錄結構。

#### **指令**
```bash
find . -name "*.log" -exec cp --parents {} /Users/lzwjava/projects/logs \;
```

#### **說明**
- **`find . -name "*.log"`**：在目前目錄及其子目錄中定位所有 `.log` 檔案（如你的範例所示）。
- **`-exec cp --parents {} /Users/lzwjava/projects/logs \;`**：
  - `cp --parents`：複製檔案並重新建立其相對於來源目錄（`.`）的目錄路徑。
  - `{}`：`find` 找到的每個檔案的佔位符。
  - `/Users/lzwjava/projects/logs`：目標目錄。
  - `\;`：終止 `-exec` 指令。

#### **結果**
- `./CoreSimulator/FC275C39-59CC-4483-A64E-5D459D7A1D57/system.log` → `/Users/lzwjava/projects/logs/CoreSimulator/FC275C39-59CC-4483-A64E-5D459D7A1D57/system.log`
- `CoreSimulator` 下的目錄結構得以保留。

#### **執行前準備**
- 確保 `/Users/lzwjava/projects/logs` 目錄存在：
  ```bash
  mkdir -p /Users/lzwjava/projects/logs
  ```

---

### **解決方案 2：使用 `rsync`**
`rsync` 是另一個功能強大的工具，可以在複製檔案時保留目錄結構，並且在處理大量操作時通常更有效率。

#### **指令**
```bash
find . -name "*.log" -exec rsync -R -a {} /Users/lzwjava/projects/logs \;
```

#### **說明**
- **`-R`**：使用相對路徑，保留來源目錄（`.`）的目錄結構。
- **`-a`**：歸檔模式（保留時間戳、權限等）。
- `{}`：每個找到的 `.log` 檔案。
- `/Users/lzwjava/projects/logs`：目標目錄。

#### **結果**
與上述相同 — 檔案會連同其完整的相對路徑一併被複製。

#### **執行前準備**
- 如果目標目錄不存在，請建立它：
  ```bash
  mkdir -p /Users/lzwjava/projects/logs
  ```

---

### **驗證複製結果**
執行任一指令後，檢查目標目錄：
```bash
ls -R /Users/lzwjava/projects/logs
```
你應該會看到：
```
/Users/lzwjava/projects/logs:
CoreSimulator

/Users/lzwjava/projects/logs/CoreSimulator:
CoreSimulator.log  FC275C39-59CC-4483-A64E-5D459D7A1D57  Simulator.log

/Users/lzwjava/projects/logs/CoreSimulator/FC275C39-59CC-4483-A64E-5D459D7A1D57:
com.apple.itunesstored  system.log

/Users/lzwjava/projects/logs/CoreSimulator/FC275C39-59CC-4483-A64E-5D459D7A1D57/com.apple.itunesstored:
itunesstored.log
```

---

### **重要注意事項**
- **權限**：確保你對 `/Users/lzwjava/projects/logs` 有寫入權限。如果沒有，請使用 `sudo`（例如 `sudo cp ...`）或調整權限：
  ```bash
  chmod -R u+w /Users/lzwjava/projects/logs
  ```
- **覆寫**：如果目標位置已存在檔案：
  - `cp` 會在不警告的情況下覆寫。
  - `rsync -a` 也會覆寫，但你可以加入 `--ignore-existing` 來跳過已存在的檔案：
    ```bash
    find . -name "*.log" -exec rsync -R -a --ignore-existing {} /Users/lzwjava/projects/logs \;
    ```
- **試運行（先測試）**：
  - 對於 `cp`，加入 `echo` 來預覽：
    ```bash
    find . -name "*.log" -exec echo cp --parents {} /Users/lzwjava/projects/logs \;
    ```
  - 對於 `rsync`，使用 `--dry-run`：
    ```bash
    find . -name "*.log" -exec rsync -R -a --dry-run {} /Users/lzwjava/projects/logs \;
    ```

---

### **該選擇哪一種？**
- **`cp`**：較簡單，不需要額外工具（所有類 Unix 系統都可用）。
- **`rsync`**：更靈活（例如用於同步、跳過重複檔案），但需要安裝 `rsync`（大多數系統已預裝）。

兩種方法都適用於你的情況。為了簡單起見，我建議從 `cp --parents` 開始。

---

### **最終指令（推薦）**
```bash
mkdir -p /Users/lzwjava/projects/logs
find . -name "*.log" -exec cp --parents {} /Users/lzwjava/projects/logs \;
```

從你的 `Logs` 目錄（`lzwjava@anonymous Logs %`）執行此指令，即可完成！如果你遇到任何問題或想調整行為（例如改為扁平化結構），請隨時告訴我。