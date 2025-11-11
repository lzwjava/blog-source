---
audio: false
generated: true
lang: hant
layout: post
title: 配置 TortoiseGit 為 Git 合併工具
translated: true
type: note
---

要配置 TortoiseGit 作為 Git 的合併工具，您需要在 Git 配置中設定 TortoiseGitMerge（TortoiseGit 內含的合併工具）。以下是實現此目標的步驟：

### 先決條件
- 確保系統已安裝 TortoiseGit。您可以從 [tortoisegit.org](https://tortoisegit.org) 下載。
- 確認 TortoiseGitMerge 執行檔可用（通常位於 `C:\Program Files\TortoiseGit\bin\TortoiseGitMerge.exe`）。

### 設定 TortoiseGitMerge 為 Git 合併工具的步驟

1. **開啟命令提示字元或 Git Bash**
   - 您可以使用 Windows 命令提示字元、PowerShell 或 Git Bash 來執行必要的 Git 配置指令。

2. **設定 TortoiseGitMerge 為合併工具**
   執行以下指令來配置 Git 使用 TortoiseGitMerge：

   ```bash
   git config --global merge.tool tortoisegitmerge
   git config --global mergetool.tortoisemerge.cmd "\"C:/Program Files/TortoiseGit/bin/TortoiseGitMerge.exe\" -base:\"$BASE\" -theirs:\"$REMOTE\" -mine:\"$LOCAL\" -merged:\"$MERGED\""
   ```

   **說明**：
   - `merge.tool tortoisegitmerge`：將合併工具名稱設定為 `tortoisegitmerge`（您可以選擇任何名稱，但這是慣例）。
   - `mergetool.tortoisemerge.cmd`：指定執行 TortoiseGitMerge 的指令及其參數：
     - `-base:"$BASE"`：共同祖先檔案。
     - `-theirs:"$REMOTE"`：來自要合併分支的檔案。
     - `-mine:"$LOCAL"`：來自您目前分支的檔案。
     - `-merged:"$MERGED"`：儲存已解決合併結果的輸出檔案。
   - 在路徑中使用正斜線 (`/`) 並根據需要轉義引號，特別是當路徑包含空格時。

   **注意**：如果 TortoiseGit 安裝在不同位置（例如 `E:/Program Files/TortoiseGit/bin/TortoiseGitMerge.exe`），請調整路徑。

3. **可選：停用合併工具提示**
   為避免每次執行 `git mergetool` 時出現提示，您可以停用提示：

   ```bash
   git config --global mergetool.prompt false
   ```

4. **可選：確保 TortoiseGitMerge 在系統 PATH 中**
   如果 Git 找不到 TortoiseGitMerge，請確保其目錄位於系統的 PATH 環境變數中：
   - 在「本機」或「我的電腦」上按右鍵 → 內容 → 進階系統設定 → 環境變數。
   - 在「系統變數」下，找到並編輯 `Path` 變數，加入 `C:\Program Files\TortoiseGit\bin`。
   - 或者，在 Git 配置中明確設定路徑：

     ```bash
     git config --global mergetool.tortoisemerge.path "C:/Program Files/TortoiseGit/bin/TortoiseGitMerge.exe"
     ```

5. **測試配置**
   - 在 Git 儲存庫中建立合併衝突（例如，合併兩個有衝突變更的分支）。
   - 執行以下指令來啟動合併工具：

     ```bash
     git mergetool
     ```

   - TortoiseGitMerge 應該會開啟，顯示衝突檔案的三窗格視圖，包含 base、theirs 和 mine 版本。底部窗格是合併結果。

6. **在 TortoiseGitMerge 中解決衝突**
   - 在三窗格視圖中，TortoiseGitMerge 顯示：
     - **左窗格**："theirs" 版本（來自要合併的分支）。
     - **右窗格**："mine" 版本（來自您目前的分支）。
     - **中間窗格**：base（共同祖先）版本。
     - **底部窗格**：用於解決衝突的合併結果。
   - 在衝突區段上按右鍵，選擇選項如「使用 'theirs' 的文字區塊」、「使用 'mine' 的文字區塊」，或手動編輯合併檔案。
   - 解決後，儲存檔案（檔案 → 儲存）並關閉 TortoiseGitMerge。
   - 如果 TortoiseGitMerge 成功退出（退出代碼 0），Git 會將檔案標記為已解決。如果出現提示，請確認將衝突標記為已解決。

7. **提交已解決的合併**
   解決衝突後，提交變更：

   ```bash
   git commit
   ```

   **注意**：如果衝突發生在 rebase 或 cherry-pick 過程中，請使用相應的 TortoiseGit 對話框（Rebase 或 Cherry-pick）來繼續過程，而不是使用標準的提交對話框。[](https://tortoisegit.org/docs/tortoisegit/tgit-dug-conflicts.html)

### 透過 TortoiseGit GUI 使用 TortoiseGitMerge
如果您偏好使用 TortoiseGit GUI 來解決衝突：
1. 在 Windows 檔案總管中，在衝突檔案上按右鍵。
2. 選擇 **TortoiseGit → Edit Conflicts**。
3. TortoiseGitMerge 將會開啟，讓您如上所述解決衝突。
4. 儲存後，再次按右鍵並選擇 **TortoiseGit → Resolved** 來將檔案標記為已解決。
5. 使用 TortoiseGit 的 Commit 對話框提交變更。

### 疑難排解
- **錯誤："Unsupported merge tool 'tortoisemerge'"**
  - 確保 `TortoiseGitMerge.exe` 的路徑正確且可存取。
  - 確認工具名稱在 `merge.tool` 和 `mergetool.<tool>.cmd` 配置中完全匹配。
  - 檢查 TortoiseGitMerge 是否在 PATH 中，或使用 `mergetool.tortoisemerge.path` 明確設定。[](https://stackoverflow.com/questions/5190188/why-cant-i-use-tortoisemerge-as-my-git-merge-tool-on-windows)
- **檔案路徑中的空格**
  - 如果檔案路徑包含空格，使用轉義引號的指令語法（如上所示）應該能正確處理。[](https://stackoverflow.com/questions/5190188/why-cant-i-use-tortoisemerge-as-my-git-merge-tool-on-windows)
- **Cygwin 使用者**
  - 如果使用 Cygwin，調整路徑以使用 Cygwin 的掛載點，例如：

    ```bash
    git config --global mergetool.tortoisemerge.cmd '"/cygdrive/c/Program Files/TortoiseGit/bin/TortoiseGitMerge.exe" -base:"$BASE" -theirs:"$REMOTE" -mine:"$LOCAL" -merged:"$MERGED"'
    ```

    這考慮了 Cygwin 的 `/cygdrive/c/` 路徑結構。[](https://devstuffs.wordpress.com/2013/03/08/setting-tortoisegitmerge-in-msysgit-as-the-git-mergetool/)
- **找不到 TortoiseGitMerge**
  - 如果您之前使用過 TortoiseSVN 的 TortoiseMerge，請確保指向 `TortoiseGitMerge.exe`，因為在 TortoiseGit 1.8 版本中執行檔名稱已變更。[](https://devstuffs.wordpress.com/2013/03/08/setting-tortoisegitmerge-in-msysgit-as-the-git-mergetool/)[](https://stackoverflow.com/questions/15881449/why-doesnt-tortoisemerge-work-as-my-mergetool)

### 補充說明
- TortoiseGitMerge 支援三窗格視圖進行衝突解決，非常適合合併。它會自動合併非衝突變更並突出顯示衝突以供手動解決。[](https://tortoisegit.org/docs/tortoisegitmerge/tmerge-dug.html)[](https://manios.org/2018/05/30/git-merge-conflicts-using-tortoise-git-merge-windows)
- 如果您也想將 TortoiseGitMerge 用作 diff 工具，請類似地配置：

  ```bash
  git config --global diff.tool tortoisediff
  git config --global difftool.tortoisediff.cmd "\"C:/Program Files/TortoiseGit/bin/TortoiseGitMerge.exe\" -mine:\"$REMOTE\" -base:\"$LOCAL\""
  ```

  然後使用 `git difftool` 來比較檔案。[](https://stackoverflow.com/questions/16493368/can-tortoisemerge-be-used-as-a-difftool-with-windows-git-bash)
- 對於進階設定，您可以配置 TortoiseGit 等待合併工具關閉，並根據退出代碼自動將檔案標記為已解決。在 TortoiseGit Settings → External Programs → Merge Tool 中，選擇 "Block TortoiseGit while executing the external merge tool" 並啟用 "Trust exit code."[](https://tortoisegit.org/docs/tortoisegit/tgit-dug-settings.html)

### 來源
- TortoiseGit 文件：[](https://tortoisegit.org/docs/tortoisegitmerge/tmerge-dug.html)[](https://tortoisegit.org/docs/tortoisegit/tgit-dug-merge.html)[](https://tortoisegit.org/docs/tortoisegit/tgit-dug-conflicts.html)
- Stack Overflow 及其他網路資源：[](https://devstuffs.wordpress.com/2013/03/08/setting-tortoisegitmerge-in-msysgit-as-the-git-mergetool/)[](https://stackoverflow.com/questions/5190188/why-cant-i-use-tortoisemerge-as-my-git-merge-tool-on-windows)[](https://stackoverflow.com/questions/16493368/can-tortoisemerge-be-used-as-a-difftool-with-windows-git-bash)

遵循這些步驟，您應該能夠有效地使用 TortoiseGitMerge 作為您的 Git 合併工具，無論是透過命令列還是 TortoiseGit GUI。