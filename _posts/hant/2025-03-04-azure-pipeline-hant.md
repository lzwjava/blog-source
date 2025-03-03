---
audio: false
generated: true
lang: hant
layout: post
title: 使用 Azure DevOps Pipelines
translated: true
---

讓我們將這個內容分成兩個部分：**使用 Azure DevOps Pipelines** 和 **撰寫 YAML 管道**。我將為兩者提供清晰、實用的解釋。

---

### **如何使用 Azure DevOps Pipelines**
Azure DevOps Pipelines 是一個 CI/CD（持續整合/持續部署）工具，自動化建置、測試和部署程式碼。以下是如何開始：

#### **1. 設定項目**
- 登入 Azure DevOps（dev.azure.com）並使用您的組織。
- 通過點擊「新增項目」，給它一個名稱並設置可見性（公開/私人）來創建一個新項目（或使用現有項目）。

#### **2. 連接您的程式碼**
- 前往項目中的 **Repos** 並將程式碼推送到一個存儲庫（GitHub、Azure Repos、Bitbucket 等）。
- 或者，在 **Pipelines > 新增管道 > 連接** 下連接外部存儲庫並選擇您的來源。

#### **3. 創建管道**
- 導航到 **Pipelines > 建置 > 新增管道**。
- 選擇您的存儲庫和分支。
- Azure 提供兩個選項：
  - **經典編輯器**：基於 GUI 的方法（不需要 YAML）。
  - **YAML**：基於程式碼的管道（建議使用以獲得靈活性和版本控制）。
- 如果使用 YAML，選擇「入門管道」或從存儲庫中的現有文件進行配置。

#### **4. 定義管道**
- 如果使用 YAML，您將在存儲庫的根目錄中撰寫一個 `.yml` 文件（例如 `azure-pipelines.yml`）（更多資訊請參見下文）。
- 添加觸發器（例如在每次推送到 `main` 時運行）、步驟（例如建置、測試）和部署目標。

#### **5. 運行和監控**
- 保存並提交 YAML 文件（或在經典編輯器中保存）。
- 點擊 **運行** 以手動觸發管道，或者根據觸發器自動運行。
- 在 **Pipelines > 建置** 下檢查日誌以監控進度或排除故障。

#### **6. 部署（可選）**
- 添加一個 **發布管道**（在 **發布** 下）或擴展您的 YAML 以部署到 Azure App Service、Kubernetes 或 VM。

---

### **如何撰寫 Azure Pipelines 的 YAML**
YAML（另一種標記語言）是一種人類可讀的格式，用於定義管道配置。以下是快速入門：

#### **基本結構**
```yaml
trigger:
  - main  # 當 'main' 分支更新時運行管道

pool:
  vmImage: 'ubuntu-latest'  # 指定建置代理（例如 Ubuntu、Windows、macOS）

steps:
  - script: echo Hello, world!  # 要運行的簡單命令
    displayName: '運行一行腳本'
```

- **`trigger`**：定義管道運行的時機（例如在推送到 `main` 時）。
- **`pool`**：指定建置代理的虛擬機映像。
- **`steps`**：列出要執行的任務（腳本、內建任務等）。

#### **常見元素**
1. **變數**：
   ```yaml
   variables:
     buildConfiguration: 'Release'
   steps:
     - script: echo $(buildConfiguration)  # 輸出 'Release'
   ```

2. **作業**（分組步驟）：
   ```yaml
   jobs:
   - job: Build
     steps:
       - script: echo Building...
   - job: Test
     steps:
       - script: echo Testing...
   ```

3. **任務**（預建動作）：
   ```yaml
   steps:
     - task: DotNetCoreCLI@2  # 例如：建置 .NET 專案
       inputs:
         command: 'build'
         projects: '**/*.csproj'
   ```

4. **條件**：
   ```yaml
   steps:
     - script: echo 這僅在 main 上運行
       condition: eq(variables['Build.SourceBranch'], 'refs/heads/main')
   ```

5. **階段**（用於多階段管道）：
   ```yaml
   stages:
   - stage: Build
     jobs:
       - job: BuildJob
         steps:
           - script: echo Building...
   - stage: Deploy
     dependsOn: Build
     jobs:
       - job: DeployJob
         steps:
           - script: echo Deploying...
   ```

#### **實際範例**
這是一個 Node.js 應用程式的管道：
```yaml
trigger:
  - main

pool:
  vmImage: 'ubuntu-latest'

steps:
  - task: NodeTool@0  # 安裝 Node.js
    inputs:
      versionSpec: '16.x'
    displayName: '安裝 Node.js'

  - script: |
      npm install
      npm run build
    displayName: '安裝和建置'

  - task: CopyFiles@2  # 複製建置產物
    inputs:
      contents: 'dist/**'
      targetFolder: '$(Build.ArtifactStagingDirectory)'

  - task: PublishBuildArtifacts@1  # 發布產物
    inputs:
      pathToPublish: '$(Build.ArtifactStagingDirectory)'
      artifactName: 'dist'
```

#### **撰寫 YAML 的技巧**
- 使用一致的縮進（2 個空格，不使用制表符）。
- 使用編輯器驗證語法（例如 VS Code 使用「YAML」擴展）。
- 參考 [Azure Pipelines YAML 結構描述](https://learn.microsoft.com/en-us/azure/devops/pipelines/yaml-schema) 以獲取選項。
- 從簡單開始，然後根據需要添加複雜性（例如階段、變數）。

---

### **下一步**
- **嘗試**：創建一個存儲庫，添加一個基本的 `azure-pipelines.yml` 文件（如上所示），並在 Azure DevOps 中運行它。
- **學習更多**：查看 Microsoft 的 [官方文檔](https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started) 或在 GitHub 上搜索範例管道。
- **問我**：如果您遇到困難或想要特定範例（例如 Python、Java），請告訴我！

您想深入了解哪個部分？設置管道、YAML 語法還是其他？