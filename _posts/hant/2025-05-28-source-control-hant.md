---
audio: false
generated: true
lang: hant
layout: post
title: VS Code 原始碼控制指南
translated: true
type: note
---

Visual Studio Code (VS Code) 具備強大的內建原始碼控制支援，讓開發者能直接在編輯器中管理如 Git、Mercurial 等版本控制系統 (VCS)。本指南將全面介紹如何在 VS Code 中使用原始碼控制，重點聚焦於最常用的 VCS——Git，內容涵蓋設定、關鍵功能、工作流程及進階用法。

### VS Code 原始碼控制功能概覽
VS Code 的原始碼控制檢視界面提供直覺的版本控制系統操作介面。它預設整合 Git 並支援其他 VCS 的擴充功能。原始碼控制檢視會顯示變更內容，支援暫存、提交、分支、合併等操作，全程無需離開編輯器。以下將逐步說明如何有效運用原始碼控制功能。

### 1. **在 VS Code 中設定原始碼控制**
使用原始碼控制前，需先安裝 Git 並初始化儲存庫。設定步驟如下：

#### 必要條件
- **安裝 Git**：從 [git-scm.com](https://git-scm.com/) 下載並安裝 Git。在終端機中執行 `git --version` 驗證安裝。
- **設定 Git**：
  ```bash
  git config --global user.name "您的姓名"
  git config --global user.email "您的電子郵件@example.com"
  ```
- **安裝 VS Code**：請確保已從 [code.visualstudio.com](https://code.visualstudio.com/) 安裝最新版 VS Code。

#### 初始化 Git 儲存庫
1. 在 VS Code 中開啟專案資料夾。
2. 開啟終端機 (Ctrl+` 或 macOS 的 Cmd+`) 並執行：
   ```bash
   git init
   ```
   這會在專案中建立 `.git` 資料夾，將其初始化為 Git 儲存庫。
3. 或複製現有儲存庫：
   ```bash
   git clone <儲存庫網址>
   ```
   接著在 VS Code 中開啟複製的資料夾。

#### 啟用原始碼控制檢視界面
- 點擊活動列中的原始碼控制圖示（從上數來第三個分支狀圖標），或按下 `Ctrl+Shift+G` (Windows/Linux) / `Cmd+Shift+G` (macOS) 開啟原始碼控制檢視。
- 若偵測到 Git 儲存庫，VS Code 會顯示帶有變更管理選項的原始碼控制檢視。

### 2. **使用原始碼控制檢視界面**
原始碼控制檢視是執行版本控制任務的核心區域，顯示：
- **變更**：自上次提交後修改、新增或刪除的檔案。
- **已暫存變更**：準備提交的檔案。
- **提交訊息框**：輸入提交說明的區域。
- **操作按鈕**：提交、重新整理等功能按鈕。

#### 常用工作流程
1. **進行變更**：在專案中編輯檔案。VS Code 會自動偵測變更並列於原始碼控制檢視的「變更」區。
2. **暫存變更**：
   - 點擊檔案旁的 `+` 圖示進行暫存，或使用「暫存所有變更」選項（三點選單 > Stage All Changes）。
   - 暫存是為下次提交做準備。
3. **撰寫提交訊息**：
   - 在原始碼控制檢視頂端的文字框輸入描述性訊息。
   - 範例：`新增使用者驗證功能`。
4. **提交變更**：
   - 點擊勾選圖示或按 `Ctrl+Enter` (Windows/Linux) / `Cmd+Enter` (macOS) 提交已暫存變更。
   - 透過三點選單選擇「提交全部」、「提交已暫存」或「提交全部並推送」。
5. **推送至遠端**：
   - 若已連接遠端儲存庫（如 GitHub），透過三點選單的「推送」選項推送變更，或在終端機執行 `git push`。

### 3. **VS Code 原始碼控制關鍵功能**
VS Code 提供多項簡化版本控制的功能：

#### 差異比較檢視
- 點擊「變更」下的檔案，即可開啟並排顯示的差異比較檢視，呈現與上次提交的差異。
- 使用行內操作來暫存或捨棄特定程式行。

#### 分支管理
- 切換分支：點擊左下狀態列的分支名稱，或使用原始碼控制檢視的分支選單（三點 > Branch > Checkout to...）。
- 建立新分支：從分支選單選擇「建立分支」，輸入名稱並確認。
- 合併分支：使用「Branch > Merge Branch」並選擇要合併至當前分支的來源分支。

#### 拉取與擷取
- **拉取**：透過三點選單的「Pull」選項同步遠端儲存庫變更。
- **擷取**：使用「Fetch」取得遠端變更但不進行合併。

#### 解決衝突
- 合併或拉取時可能發生衝突。VS Code 會標示衝突檔案並提供行內衝突解決介面：
  - 選擇「接受目前變更」、「接受輸入變更」、「接受雙方變更」或手動編輯檔案。
  - 暫存並提交已解決的檔案。

#### Git Lens 擴充功能
欲使用進階 Git 功能，可安裝 **GitLens** 擴充功能：
- 檢視提交歷史、標註資訊與檔案變更記錄。
- 存取儲存庫洞察資料（近期提交、儲藏內容等）。
- 透過擴充功能檢視安裝 (`Ctrl+Shift+X` 或 `Cmd+Shift+X`)。

### 4. **進階應用**
#### 儲藏變更
- 暫時儲存未提交的變更：
  - 前往三點選單 > Stash > Stash。
  - 後續可透過相同選單套用或取出儲藏內容。
- 適用於切換分支時暫存未完成工作。

#### 終端機中的 Git 指令
- 對於介面未直接支援的操作，可使用內建終端機：
  ```bash
  git rebase <分支>
  git cherry-pick <提交>
  git log --oneline
  ```

#### 自訂原始碼控制
- **設定**：在 VS Code 設定中調整原始碼控制行為 (`Ctrl+,` 或 `Cmd+,`)：
  - `git.autoRepositoryDetection`：啟用/停用自動 Git 儲存庫偵測。
  - `git.enableSmartCommit`：當沒有暫存檔案時提交所有變更。
- **SCM 供應商**：安裝其他 VCS（如 Mercurial 或 SVN）的擴充功能。

#### GitHub 整合
- 使用 **GitHub Pull Requests and Issues** 擴充功能直接管理 PR 與議題。
- 透過左下角帳戶選單進行 GitHub 驗證，以便從 GitHub 儲存庫推送/拉取。

### 5. **範例工作流程：建立並推送功能分支**
以下示範 VS Code 中常見的 Git 工作流程：

# VS Code 中的 Git 工作流程範例

## 建立與推送功能分支步驟

1. **建立新分支**：
   - 在原始碼控制檢視中，點擊狀態列的分支名稱，或使用三點選單 > Branch > Create Branch。
   - 為分支命名，例如 `feature/add-login`。
   - VS Code 將切換至新分支。

2. **進行並暫存變更**：
   - 編輯檔案（例如在 `src/Login.js` 新增登入元件）。
   - 原始碼控制檢視的「變更」區將顯示檔案。
   - 點擊 `+` 圖示暫存變更，或選擇「Stage All Changes」。

3. **提交變更**：
   - 輸入提交訊息，例如 `新增登入元件`。
   - 點擊勾選圖示或按 `Ctrl+Enter` (Windows/Linux) / `Cmd+Enter` (macOS) 提交。

4. **推送分支**：
   - 若無遠端儲存庫，請先新增：
     ```bash
     git remote add origin <儲存庫網址>
     ```
   - 推送分支：三點選單 > Push，或執行：
     ```bash
     git push -u origin feature/add-login
     ```

5. **建立 Pull Request**：
   - 若使用 GitHub，請在瀏覽器中開啟儲存庫，或使用 GitHub Pull Requests 擴充功能建立 PR。
   - 將 PR 連結至 `feature/add-login` 分支。

## 實用技巧
- 定期從主分支拉取更新以避免衝突。
- 使用描述性提交訊息促進團隊協作。
- 安裝 GitLens 強化提交歷史與標註檢視功能。

### 6. **常見問題疑難排解**
- **未偵測到 Git**：請確認 Git 已安裝並加入系統 PATH。安裝後重新啟動 VS Code。
- **驗證錯誤**：設定 SSH 金鑰或使用 GitHub/GitLab 的個人存取權杖。透過帳戶選單進行驗證。
- **合併衝突**：使用行內衝突解決工具或手動編輯檔案，接著暫存並提交。
- **效能緩慢**：大型專案可停用 `git.autoRepositoryDetection`，或使用 GitLens 優化 Git 操作。

### 7. **最佳實踐**
- **頻繁提交**：進行小型邏輯性提交以追蹤進度。
- **使用描述性訊息**：遵循約定格式如 `<類型>(<範圍>): <描述>`（範例：`feat(auth): 新增登入端點`）。
- **定期拉取**：與遠端儲存庫保持同步以減少衝突。
- **備份儲藏**：套用儲藏前確認不會覆蓋重要變更。
- **善用擴充功能**：使用 GitLens、Git History 或 Git Graph 增強功能。

### 8. **補充資源**
- **VS Code 文件**：[VS Code 版本控制](https://code.visualstudio.com/docs/editor/versioncontrol)
- **Git 文件**：[git-scm.com/doc](https://git-scm.com/doc)
- **GitLens 擴充功能**：可在 VS Code 市集中取得。
- **GitHub Pull Requests 擴充功能**：用於管理 PR 與議題。

本指南涵蓋 VS Code 原始碼控制的基礎與進階功能，重點介紹 Git 的應用。透過遵循這些步驟與最佳實踐，您將能直接在編輯器中高效管理版本控制工作流程。