---
audio: false
generated: true
lang: hant
layout: post
title: Git 分支視覺化工具
translated: true
type: note
---

要在 Windows 上視覺化 Git 儲存庫中的多個分支，您可以使用 TortoiseGit 或其他工具來顯示所選分支的圖形。TortoiseGit 的版本圖功能強大，但在顯示所有分支時可能會顯得雜亂。以下是使用 TortoiseGit 查看多個特定分支圖形的步驟，以及提供更靈活選擇的替代工具。

### 使用 TortoiseGit 查看多個分支
TortoiseGit 的版本圖可以顯示多個分支，但無法直接在介面中選擇特定分支。不過，您可以透過篩選功能來聚焦相關分支。

1. **開啟版本圖**：
   - 在 Windows 檔案總管中導航至您的儲存庫資料夾。
   - 右鍵點擊資料夾，選擇 **TortoiseGit** > **Revision Graph**。
   - 預設情況下，這會顯示所有參考（分支、標籤等）的圖形，如果分支眾多可能會顯得雜亂。[](https://tortoisegit.org/docs/tortoisegit/tgit-dug-revgraph.html)

2. **篩選特定分支**：
   - 在版本圖視窗中，使用**篩選選項**來減少雜亂：
     - 前往 **View** 選單，選擇 **Show branchings and mergings** 以強調分支關係。[](https://stackoverflow.com/questions/67642974/tortoisegit-log-can-i-view-only-branch-and-merge-commits)
     - 要聚焦特定分支，可右鍵點擊提交並選擇 **Show Log** 以查看日誌對話框，在此您可以切換 **View > Labels > Local branches** 或 **Remote branches** 來僅顯示相關參考。[](https://tortoisegit.org/docs/tortoisegit/tgit-dug-showlog.html)
   - 或者，在日誌對話框中使用 **Walk Behavior > Compressed Graph** 選項來簡化圖形，僅顯示合併點和帶有參考（如分支尖端）的提交。[](https://tortoisegit.org/docs/tortoisegit/tgit-dug-showlog.html)[](https://stackoverflow.com/questions/67642974/tortoisegit-log-can-i-view-only-branch-and-merge-commits)

3. **導覽圖形**：
   - 使用**概覽視窗**來導覽大型圖形，可拖曳突出顯示的區域。[](https://tortoisegit.org/docs/tortoisegit/tgit-dug-revgraph.html)
   - 將滑鼠懸停在修訂節點上可查看詳細資訊，如日期、作者和註解。[](https://tortoisegit.org/docs/tortoisegit/tgit-dug-revgraph.html)
   - 按住 Ctrl 鍵並點擊兩個修訂版本，可透過右鍵選單進行比較（例如 **Compare Revisions**）。[](https://tortoisegit.org/docs/tortoisegit/tgit-dug-revgraph.html)

4. **限制**：
   - TortoiseGit 的版本圖會顯示所有分支（除非進行篩選），且圖形視圖中沒有直接選項來僅選擇特定分支。[](https://stackoverflow.com/questions/60244772/how-to-interpret-tortoise-git-revision-graph)
   - 若需要更清晰的視圖，請考慮使用以下替代工具。

### 用於查看多個分支的替代工具
如果 TortoiseGit 的介面在選擇特定分支方面過於受限，可嘗試這些提供更多分支視覺化控制權的工具：

#### 1. **Visual Studio Code 與 Git Graph 擴充功能**
   - **安裝**：下載 Visual Studio Code 並安裝 **Git Graph** 擴充功能。[](https://x.com/midudev/status/1797990974917927150)
   - **使用方法**：
     - 在 VS Code 中開啟您的儲存庫。
     - 從 Source Control 標籤頁或命令選擇區（`Ctrl+Shift+P`，輸入「Git Graph」）存取 Git Graph 視圖。
     - 點擊介面中的分支名稱以選擇要在圖形中顯示的特定分支。
     - 圖形會以顏色編碼的線條清晰顯示提交、分支和合併。[](https://ardalis.com/git-graph-visualizes-branches-in-vs-code-for-free/)
   - **優點**：輕量、免費，並允許互動式選擇多個分支。支援比較提交和基本 Git 操作。[](https://ardalis.com/git-graph-visualizes-branches-in-vs-code-for-free/)

#### 2. **SourceTree**
   - **安裝**：為 Windows 下載 SourceTree（免費）。[](https://stackoverflow.com/questions/12324050/how-can-i-visualize-github-branch-history-on-windows)[](https://stackoverflow.com/questions/12912985/git-visual-diff-between-branches)
   - **使用方法**：
     - 在 SourceTree 中開啟您的儲存庫。
     - **History** 視圖顯示分支和提交的圖形化表示。
     - 使用左側的分支列表來切換特定分支的可見性，僅聚焦於您想查看的分支。
     - 右鍵點擊分支或提交可進行合併或比較等操作。[](https://www.geeksforgeeks.org/how-to-visualizing-branch-topology-in-git/)
   - **優點**：清晰的分支視覺化，具有一致的著色和互動功能，如拖放合併。[](https://superuser.com/questions/699094/how-can-i-visualize-git-flow-branches)[](https://www.geeksforgeeks.org/how-to-visualizing-branch-topology-in-git/)

#### 3. **GitKraken**
   - **安裝**：下載 GitKraken（開源項目免費，私有儲存庫需付費）。[](https://www.geeksforgeeks.org/how-to-visualizing-branch-topology-in-git/)[](https://stackoverflow.com/questions/1838873/visualizing-branch-topology-in-git)
   - **使用方法**：
     - 在 GitKraken 中開啟您的儲存庫。
     - 中央圖形顯示所有分支，可透過分支列表來隱藏/顯示特定分支。
     - 點擊分支標籤以聚焦特定分支，或使用搜尋來篩選提交。[](https://www.geeksforgeeks.org/how-to-visualizing-branch-topology-in-git/)
   - **優點**：直觀且視覺吸引力強，具有一致的分支著色和進階功能，如衝突解決。[](https://superuser.com/questions/699094/how-can-i-visualize-git-flow-branches)[](https://www.geeksforgeeks.org/how-to-visualizing-branch-topology-in-git/)

#### 4. **使用 `git log` 命令列**
   - 如果您偏好終端機解決方案，可使用 Git 內建的圖形視圖：
     ```bash
     git log --graph --oneline --decorate --branches=<branch1> --branches=<branch2>
     ```
     將 `<branch1>` 和 `<branch2>` 替換為您要視覺化的分支名稱（例如 `feature1`、`feature2`）。使用 `--branches=*` 表示所有分支，或明確指定多個分支。[](https://how-to.dev/how-to-display-git-branches-as-a-tree-in-cli)
   - **為方便起見的別名**：
     建立 Git 別名以便更輕鬆地存取：
     ```bash
     git config --global alias.tree "log --graph --oneline --decorate --branches="
     ```
     然後執行 `git tree feature1 feature2` 即可查看僅包含這些分支的圖形。[](https://how-to.dev/how-to-display-git-branches-as-a-tree-in-cli)
   - **優點**：無需額外軟體，且可指定確切分支。輸出為文字形式，但在小型儲存庫中清晰易讀。[](https://x.com/GWierzowiecki/status/1927657575048179899)

### 建議
- **追求簡單和整合性**：使用 **VS Code 與 Git Graph**，這是一個輕量級的免費解決方案，可讓您選擇特定分支。[](https://x.com/midudev/status/1797990974917927150)
- **追求進階視覺化**：使用 **GitKraken** 或 **SourceTree**，它們提供更精緻的 GUI，具有互動式分支選擇和一致的著色。[](https://www.geeksforgeeks.org/how-to-visualizing-branch-topology-in-git/)
- **TortoiseGit 使用者**：可繼續使用版本圖，並利用 **Compressed Graph** 或 **Show branchings and mergings** 等篩選功能來聚焦關鍵分支，但需注意其在選擇特定分支方面的限制。[](https://stackoverflow.com/questions/67642974/tortoisegit-log-can-i-view-only-branch-and-merge-commits)
- **終端機使用者**：使用帶有特定分支篩選器的 `git log` 命令，無需額外工具即可快速、精確地進行視覺化。[](https://how-to.dev/how-to-display-git-branches-as-a-tree-in-cli)

如果您擁有大量分支，GitKraken 或 SourceTree 可能是選擇性視覺化您所關注分支的最佳選擇，因為它們提供直觀的分支切換功能。如果您需要協助設定任何這些工具或進一步的說明，請告訴我！