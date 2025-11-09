---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: Azure DevOps 入門指南
translated: true
type: note
---

Azure DevOps 是由 Microsoft 提供的一套全面雲端開發工具，協助團隊有效率地規劃、開發、測試和交付軟體。它能與其他 Microsoft 服務（如 Azure 和 GitHub）無縫整合，並支援多種方法論，包括 Agile、Scrum 和 DevOps 實踐。本指南涵蓋核心內容：什麼是 Azure DevOps、關鍵組件、入門指南、最佳實踐及深入學習資源。

## 什麼是 Azure DevOps？
Azure DevOps 提供端到端的 DevOps 功能，促進開發、運營和相關方之間的協作。它具平台無關性，支援多種語言、框架和工具。主要優勢包括：
- **擴展性**：可處理任何規模的項目，從小型團隊到企業級。
- **整合性**：可與 Visual Studio、GitHub、Slack 和 Jira 等 IDE 連接。
- **安全性**：內建合規功能，如基於角色的存取控制（RBAC）和審計日誌。
- **定價**：最多 5 名用戶免費；付費計劃起價為每位用戶每月 6 美元，提供額外功能。

截至 2025 年，Azure DevOps 已進一步發展，增強了 AI 整合（例如 GitHub Copilot for Azure）並改進了管道分析功能。

## 關鍵組件
Azure DevOps 包含五項核心服務，每項均可透過網路入口網站或 API 存取：

### 1. **Boards**
   - **用途**：視覺化規劃與工作項目追蹤工具。
   - **功能**：
     - 用於視覺化工作流程的 Kanban 看板。
     - 用於任務優先級排序的待辦事項清單。
     - 用於 Agile 迭代的衝刺計劃。
     - 用於自定義報告的查詢功能。
   - **使用場景**：即時追蹤錯誤、功能與任務。

### 2. **Repos**
   - **用途**：集中式代碼版本控制。
   - **功能**：
     - Git 或 TFVC 儲存庫。
     - 分支策略與拉取請求。
     - Wiki 整合用於文件管理。
   - **使用場景**：協作進行代碼審查並維護歷史記錄。

### 3. **Pipelines**
   - **用途**：CI/CD（持續整合/持續部署）自動化。
   - **功能**：
     - 基於 YAML 或傳統管道。
     - 多階段建置、測試與部署。
     - 與 Azure Artifacts 整合以管理套件。
     - 用於審批與閘道的環境設定。
   - **使用場景**：為每次提交自動化建置，並部署至雲端或本地環境。

### 4. **Test Plans**
   - **用途**：手動與探索性測試。
   - **功能**：
     - 測試案例管理。
     - 即時日誌與附件。
     - 與 Pipelines 中的自動化測試整合。
   - **使用場景**：在發布前確保品質。

### 5. **Artifacts**
   - **用途**：套件管理與依賴項處理。
   - **功能**：
     - 通用套件、NuGet、npm 和 Maven 儲存庫。
     - 二進位檔的保留政策。
   - **使用場景**：在團隊間共享與版本化函式庫。

## 入門指南
按照以下步驟設定 Azure DevOps：

1. **建立帳戶**：
   - 前往 [dev.azure.com](https://dev.azure.com) 並使用 Microsoft 帳戶註冊（提供免費層級）。
   - 建立新組織（例如 "MyProjectOrg"）。

2. **設定專案**：
   - 在組織中點擊「新增專案」。
   - 選擇可見性（私有/公開）與版本控制（Git/TFVC）。
   - 透過電子郵件邀請新增團隊成員。

3. **設定 Repos**：
   - 複製預設儲存庫：`git clone https://dev.azure.com/{org}/{project}/_git/{repo}`。
   - 推送初始代碼：`git add . && git commit -m "Initial commit" && git push`。

4. **建置簡單管道**：
   - 在 Pipelines > New Pipeline > 選擇儲存庫 > ASP.NET（或您的框架）。
   - 使用 YAML 以簡化設定：
     ```yaml
     trigger:
     - main
     pool:
       vmImage: 'ubuntu-latest'
     steps:
     - task: DotNetCoreCLI@2
       inputs:
         command: 'build'
         projects: '**/*.csproj'
     ```
   - 儲存並執行管道。

5. **建立看板**：
   - 前往 Boards > Sprints > New Query。
   - 定義工作項目類型（例如 Epic > Feature > Task）。

6. **測試與部署**：
   - 在管道中添加測試任務。
   - 設定發布管道以部署至 Azure App Service。

如需實作教程，請從官方快速入門開始。

## 最佳實踐
- **採用 YAML 管道**：它們是版本控制且可重複使用。
- **使用分支策略**：要求拉取請求審批並連結工作項目。
- **實施安全掃描**：整合 SonarQube 或 Microsoft Defender 等工具。
- **使用分析監控**：利用儀表板追蹤速度與建置成功率。
- **透過擴展擴展功能**：市集提供 2,000 多個擴展（例如 Slack 通知）。
- **混合支援**：對於本地環境，可使用 Azure DevOps Server（自託管）。

常見陷阱：過早過度自定義——應從簡單開始並逐步迭代。

## 進階主題
- **擴展與市集**：使用 Jenkins 或 Terraform 等工具的插件進行自定義。
- **AI/ML 整合**：在管道中使用 Azure ML 部署模型。
- **多團隊協作**：利用區域與迭代支援大型組織。
- **遷移**：提供從 GitHub 或 Jira 導入的工具。

## 參考資源
- [Azure DevOps 文件](https://learn.microsoft.com/en-us/azure/devops/)
- [Azure DevOps 入門](https://learn.microsoft.com/en-us/azure/devops/get-started/what-is-azure-devops)
- [Azure DevOps 定價](https://azure.microsoft.com/en-us/pricing/details/devops/azure-devops-services/)
- [Azure Pipelines 最佳實踐](https://learn.microsoft.com/en-us/azure/devops/pipelines/)