---
audio: false
generated: true
lang: hant
layout: post
title: 龜兔 Git
translated: true
type: note
---

TortoiseGit 是一款 Windows Shell 擴充套件，為熱門的版本控制系統 Git 提供使用者友善的操作介面。它直接整合於 Windows 檔案總管中，讓您能透過右鍵選單執行 Git 操作。本指南將介紹在 Windows 上安裝、設定及使用 TortoiseGit 的方法，並涵蓋常見任務與最佳實踐。

### TortoiseGit 概覽
TortoiseGit 建基於 msysGit（Git for Windows），為 Git 指令提供圖形化操作介面，特別適合偏好 GUI 操作的使用者。主要功能包括：
- 與 Windows 檔案總管右鍵選單整合
- 視覺化差異比較與合併工具
- 支援常見 Git 工作流程（提交、推送、拉取、分支、合併等）
- 可與常用問題追蹤系統及外部工具整合

### 環境準備
安裝 TortoiseGit 前，請確認：
- 使用 Windows 作業系統（建議 Windows 10 或更新版本）
- 已安裝 Git for Windows（TortoiseGit 需依賴此元件）
- 具備 Git 基礎概念（儲存庫、提交、分支等）

### 安裝步驟
1. **安裝 Git for Windows**：
   - 從 [Git for Windows](https://gitforwindows.org/) 或 [Git SCM](https://git-scm.com/downloads) 下載最新版本
   - 執行安裝程式並遵循指示，建議設定：
     - 使用預設編輯器（如 Notepad）或選擇 VS Code 等工具
     - 選擇「Use Git from the Windows Command Prompt」以確保可存取性
     - HTTPS 傳輸選用「OpenSSL」
     - 行尾符號選擇「Checkout as-is, commit as-is」（跨平台團隊協作除外）
   - 完成安裝程序

2. **安裝 TortoiseGit**：
   - 從 [TortoiseGit 官方網站](https://tortoisegit.org/download/) 下載最新版本
   - 執行安裝程式：
     - 選擇預設語言與元件
     - 確保系統已偵測到 Git for Windows（若未安裝會提示）
     - 如需 SSH 功能可安裝 TortoiseGitPlink
   - 若系統要求請重新啟動電腦

3. **驗證安裝**：
   - 在 Windows 檔案總管中對任意資料夾點擊右鍵，應可見 TortoiseGit 選項（如「Git Clone」、「Git Create Repository here」等）

### 初始設定
安裝完成後，請依個人需求進行設定：
1. **設定使用者資訊**：
   - 於資料夾內點擊右鍵，選擇 **TortoiseGit > Settings**
   - 在設定視窗中前往 **Git > Config** 分頁
   - 輸入姓名與電子郵件（需與 GitHub、GitLab 等服務一致）：
     ```
     Name: Your Name
     Email: your.email@example.com
     ```
   - 點擊 **Apply** 與 **OK**

2. **設定 SSH（選用）**：
   - 若使用 SSH 連接遠端儲存庫：
     - 開啟 TortoiseGit 內建的 **PuTTYgen**
     - 生成新 SSH 金鑰對，儲存私鑰並複製公鑰
     - 將公鑰新增至 Git 託管服務（如 GitHub、GitLab）
     - 在 TortoiseGit 設定中的 **Git > Remote** 分頁選擇 TortoiseGitPlink 作為 SSH 客戶端

3. **設定差異比較與合併工具**：
   - 於 **TortoiseGit > Settings > Diff Viewer** 選擇工具（預設 TortoiseGitMerge 或外部工具如 Beyond Compare）
   - 合併工具可在 **Merge Tool** 設定（初學者建議使用 TortoiseGitMerge）

### 基礎操作
以下為透過 Windows 檔案總管右鍵選單執行的常見 TortoiseGit 操作：

#### 1. **複製儲存庫**
   - 在資料夾內點擊右鍵選擇 **Git Clone**
   - 在對話視窗中：
     - 輸入儲存庫 URL（如 `https://github.com/username/repo.git`）
     - 指定本地儲存目錄
     - 可選取特定分支或載入 SSH 金鑰
   - 點擊 **OK** 開始複製

#### 2. **建立新儲存庫**
   - 進入目標資料夾，點擊右鍵選擇 **Git Create Repository here**
   - 若建立伺服器端儲存庫請勾選「Make it Bare」（本地使用通常不需勾選）
   - 點擊 **OK**，系統將建立 `.git` 資料夾完成初始化

#### 3. **提交變更**
   - 將檔案新增至儲存庫資料夾
   - 對資料夾或選取檔案點擊右鍵，選擇 **Git Commit -> "main"**（或當前分支名稱）
   - 在提交視窗中：
     - 輸入描述變更的提交訊息
     - 勾選要暫存的檔案
     - 點擊 **OK** 或 **Commit & Push** 直接推送至遠端儲存庫

#### 4. **推送變更**
   - 提交後點擊右鍵選擇 **TortoiseGit > Push**
   - 選擇遠端儲存庫與分支
   - 依提示完成驗證（HTTPS 需輸入帳密，SSH 使用金鑰）
   - 點擊 **OK** 完成推送

#### 5. **拉取變更**
   - 更新本地儲存庫時點擊右鍵選擇 **TortoiseGit > Pull**
   - 選擇遠端分支後點擊 **OK**
   - 若發生衝突請依提示解決（使用合併工具）

#### 6. **建立與切換分支**
   - 點擊右鍵選擇 **TortoiseGit > Create Branch**
   - 輸入分支名稱後點擊 **OK**
   - 切換分支時選擇 **TortoiseGit > Switch/Checkout** 並選取目標分支

#### 7. **檢視歷史記錄**
   - 點擊右鍵選擇 **TortoiseGit > Show Log**
   - 瀏覽提交歷史（含作者、日期與訊息）
   - 對特定提交點擊右鍵可檢視變更、還原或揀選提交

#### 8. **解決合併衝突**
   - 拉取或合併時若發生衝突，TortoiseGit 將發出通知
   - 對衝突檔案點擊右鍵選擇 **TortoiseGit > Resolve**
   - 使用合併工具手動編輯後標記為已解決
   - 提交解決後的變更

### 進階功能
1. **暫存變更**：
   - 儲存未提交的變更：點擊右鍵選擇 **TortoiseGit > Stash Save**
   - 取回暫存變更：選擇 **TortoiseGit > Stash Pop**

2. **變基操作**：
   - 點擊右鍵選擇 **TortoiseGit > Rebase**
   - 選擇要變基的目標分支，依提示重新排序或壓縮提交

3. **子模組管理**：
   - 點擊右鍵選擇 **TortoiseGit > Submodule Update** 或 **Add**
   - 子模組設定可在 TortoiseGit 設定中調整

4. **二分偵錯**：
   - 定位問題提交時使用 **TortoiseGit > Bisect Start**
   - 標記提交為「良好」或「故障」以縮小問題範圍

### 最佳實踐
- **頻繁提交**：以清晰訊息進行小規模多次提交
- **定期拉取**：保持本地儲存庫更新以減少衝突
- **善用分支**：建立功能分支維護主分支穩定性
- **備份金鑰**：安全儲存與備份 SSH 金鑰
- **檢視變更**：提交前使用差異比較工具確認修改內容

### 疑難排解
- **驗證問題**：確認 SSH 金鑰或憑證已在 Git 託管服務正確設定
- **合併衝突**：使用 TortoiseGitMerge 視覺化解決衝突，合併前請備份檔案
- **選單遺失**：檢查 TortoiseGit 安裝狀態與檔案總管整合功能是否啟用
- **效能遲滯**：於 **TortoiseGit > Settings > Icon Overlays** 停用非必要圖示疊加

### 範例工作流程
以下為參與專案開發的典型工作流程：

# TortoiseGit 範例工作流程

## 1. 複製儲存庫
- 在資料夾內點擊右鍵選擇 **Git Clone**
- 輸入儲存庫 URL 與本地目錄
- 點擊 **OK**

## 2. 建立功能分支
- 點擊右鍵選擇 **TortoiseGit > Create Branch**
- 命名分支（如 `feature/add-login`）
- 點擊 **OK** 並切換至新分支

## 3. 進行修改
- 在儲存庫資料夾中編輯檔案
- 點擊右鍵選擇 **Git Commit -> "feature/add-login"**
- 編寫提交訊息並勾選要暫存的檔案
- 點擊 **Commit**

## 4. 推送變更
- 點擊右鍵選擇 **TortoiseGit > Push**
- 選擇遠端分支（如 `origin/feature/add-login`）
- 點擊 **OK**

## 5. 建立拉取請求
- 在 Git 託管服務（如 GitHub）建立從功能分支到主分支的拉取請求
- 等待審核與合併

## 6. 更新本地儲存庫
- 切換至主分支（**TortoiseGit > Switch/Checkout**）
- 拉取更新（**TortoiseGit > Pull**）

### 參考資源
- **官方文件**：[TortoiseGit Documentation](https://tortoisegit.org/docs/)
- **Git for Windows**：[Git SCM](https://git-scm.com/)
- **教學資源**：於 YouTube 或技術部落格搜尋「TortoiseGit tutorial」觀看視覺化指南

TortoiseGit 透過直覺的介面簡化 Git 操作，讓 Windows 使用者能輕鬆進行版本控制。若需特定任務協助或進階設定支援，歡迎隨時提出！