---
audio: false
generated: true
lang: hant
layout: post
title: 設定 BeyondCompare 與 Git Difftool
translated: true
type: note
---

要設定 Beyond Compare 作為 `git difftool`，請按照以下步驟操作。這些說明假設您已在系統上安裝 Beyond Compare 並配置好 Git。

### 設定 Beyond Compare 為 `git difftool` 的步驟

1. **檢查 Beyond Compare 安裝**
   確保 Beyond Compare 已安裝且可從命令列存取。您可以執行以下指令驗證：
   ```
   bcomp
   ```
   如果無法識別，請確保 Beyond Compare 的可執行檔（例如 Windows 上的 `BCompare.exe` 或 macOS/Linux 上的 `bcomp`）位於系統的 PATH 環境變數中。

2. **配置 Git 使用 Beyond Compare**
   在終端機或命令提示字元中執行以下 Git 配置指令：

   ```bash
   git config --global diff.tool bc
   git config --global difftool.bc.path "path/to/bcomp"
   git config --global difftool.prompt false
   ```

   - 將 `"path/to/bcomp"` 替換為 Beyond Compare 可執行檔的實際路徑：
     - **Windows**：通常為 `"C:\Program Files\Beyond Compare 4\BCompare.exe"`。路徑中使用雙反斜線 (`\\`) 或正斜線 (`/`)。
     - **macOS**：通常為 `/Applications/Beyond Compare.app/Contents/MacOS/bcomp`。
     - **Linux**：通常為 `/usr/bin/bcomp` 或 `bcomp` 的安裝位置。
   - `difftool.prompt false` 設定可防止 Git 在每個檔案上提示您啟動 difftool。

3. **（可選）設定為合併工具**
   如果您也想將 Beyond Compare 用作 `mergetool`，請加入以下指令：

   ```bash
   git config --global merge.tool bc
   git config --global mergetool.bc.path "path/to/bcomp"
   git config --global mergetool.prompt false
   ```

4. **測試配置**
   為驗證設定，請建立或導航至具有變更的 Git 儲存庫並執行：

   ```bash
   git difftool
   ```

   這應該會啟動 Beyond Compare 來顯示您修改的檔案與最後一次提交之間的差異。如果您將其用作合併工具，請使用以下指令測試：

   ```bash
   git mergetool
   ```

   （這僅在您有合併衝突時適用。）

5. **各平台的特定注意事項**
   - **Windows**：確保使用正確的 `BCompare.exe` 路徑。如果路徑包含空格，請用引號括住。
   - **macOS/Linux**：`bcomp` 指令通常需要等待 Beyond Compare 關閉後才將控制權返回終端機。Beyond Compare 的文件表明它會自動處理此情況，但如果 Git 過早退出，您可能需要調整腳本或使用包裝程式（詳情請參閱 Beyond Compare 的支援文件）。
   - 如果遇到問題，請驗證路徑並確保 Beyond Compare 已授權且功能正常。

6. **Windows 配置範例**
   在 Windows 上設定 Beyond Compare 4 的指令可能如下：

   ```bash
   git config --global diff.tool bc
   git config --global difftool.bc.path "C:\\Program Files\\Beyond Compare 4\\BCompare.exe"
   git config --global difftool.prompt false
   git config --global merge.tool bc
   git config --global mergetool.bc.path "C:\\Program Files\\Beyond Compare 4\\BCompare.exe"
   git config --global mergetool.prompt false
   ```

7. **驗證配置**
   檢查您的 Git 配置以確保設定已應用：

   ```bash
   git config --global --list
   ```

   尋找如 `diff.tool=bc` 和 `difftool.bc.path` 等條目。

### 其他提示
- **比較特定檔案**：使用 `git difftool <file>` 來比較特定檔案。
- **比較分支**：使用 `git difftool branch1 branch2` 來比較兩個分支之間的差異。
- **Beyond Compare 設定**：在 Beyond Compare 中，您可以透過其介面自訂比較規則（例如忽略空白字元）以獲得更好的差異視覺化效果。
- **疑難排解**：如果 Beyond Compare 未啟動，請仔細檢查 `difftool.bc.path` 設定中的路徑。使用 `which bcomp`（macOS/Linux）或 `where BCompare.exe`（Windows）來定位可執行檔。

此設定應能讓您無縫地將 Beyond Compare 與 `git difftool` 及（可選的）`git mergetool` 搭配使用。如果您遇到特定問題，請告知您的作業系統和任何錯誤訊息，以獲得更有針對性的建議！