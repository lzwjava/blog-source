---
audio: false
generated: true
lang: hant
layout: post
title: 使用 Azure DevOps 管線
translated: true
type: note
---

讓我們將這分為兩部分來講解：**使用 Azure DevOps Pipelines** 和**編寫管道的 YAML**。我會為兩者提供清晰實用的說明。

---

### **如何使用 Azure DevOps Pipelines**
Azure DevOps Pipelines 是一個 CI/CD（持續整合/持續部署）工具，能自動化建置、測試和部署程式碼。以下是入門步驟：

#### **1. 設定專案**
- 登入 Azure DevOps (dev.azure.com) 並選擇您的組織。
- 點擊「新增專案」建立新專案（或使用現有專案），輸入名稱並設定可見性（公開/私人）。

#### **2. 連接您的程式碼**
- 在專案中前往 **Repos**，將程式碼推送至儲存庫（GitHub、Azure Repos、Bitbucket 等）。
- 或者，在 **Pipelines > New Pipeline > Connect** 下連結外部儲存庫並選擇來源。

#### **3. 建立管道**
- 前往 **Pipelines** > **Builds** > **New Pipeline**。
- 選擇您的儲存庫和分支。
- Azure 提供兩種選項：
  - **Classic Editor**：基於圖形介面的方法（無需 YAML）。
  - **YAML**：基於程式碼的管道（推薦，因具靈活性且支援版本控制）。
- 對於 YAML，選擇「Starter pipeline」或從儲存庫中的現有檔案進行配置。

#### **4. 定義管道**
- 如果使用 YAML，您需要在儲存庫根目錄編寫一個 `.yml` 檔案（例如 `azure-pipelines.yml`）。（詳情見下文。）
- 加入觸發條件（例如每次推送到 `main` 分支時執行）、步驟（例如建置、測試）和部署目標。

#### **5. 執行與監控**
- 儲存並提交 YAML 檔案（或在 Classic Editor 中儲存）。
- 點擊 **Run** 手動觸發管道，或讓它根據觸發條件自動執行。
- 在 **Pipelines > Builds** 下檢查日誌以監控進度或排查失敗。

#### **6. 部署（可選）**
- 加入 **release Pipeline**（在 **Releases** 下）或擴展您的 YAML 以部署到環境，如 Azure App Service、Kubernetes 或虛擬機器。

---

### **如何編寫 Azure Pipelines 的 YAML**
YAML（Yet Another Markup Language）是一種人類可讀的格式，用於定義管道配置。以下是快速入門：

#### **基本結構**
```yaml
trigger:
  - main  # 當 'main' 分支更新時執行管道

pool:
  vmImage: 'ubuntu-latest'  # 指定建置代理程式（例如 Ubuntu、Windows、macOS）

steps:
  - script: echo Hello, world!  # 執行的簡單指令
    displayName: '執行單行指令'
```

- **`trigger`**：定義管道何時執行（例如推送到 `main` 分支時）。
- **`pool`**：指定建置代理程式的虛擬機器映像。
- **`steps`**：列出要執行的任務（指令碼、內建任務等）。

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
     - task: DotNetCoreCLI@2  # 範例：建置 .NET 專案
       inputs:
         command: 'build'
         projects: '**/*.csproj'
   ```

4. **條件**：
   ```yaml
   steps:
     - script: echo This runs only on main
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
以下是一個 Node.js 應用程式的管道：
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
    displayName: '安裝與建置'

  - task: CopyFiles@2  # 複製建置成品
    inputs:
      contents: 'dist/**'
      targetFolder: '$(Build.ArtifactStagingDirectory)'

  - task: PublishBuildArtifacts@1  # 發佈成品
    inputs:
      pathToPublish: '$(Build.ArtifactStagingDirectory)'
      artifactName: 'dist'
```

#### **編寫 YAML 的提示**
- 使用一致的縮排（2 個空格，無 Tab 鍵）。
- 使用編輯器（例如安裝了「YAML」擴充功能的 VS Code）驗證語法。
- 參考 [Azure Pipelines YAML 結構描述](https://learn.microsoft.com/en-us/azure/devops/pipelines/yaml-schema)以了解選項。
- 從簡單開始，然後根據需要增加複雜性（例如階段、變數）。

---

### **後續步驟**
- **嘗試**：建立一個儲存庫，加入如上所述的基本 `azure-pipelines.yml`，並在 Azure DevOps 中執行。
- **深入學習**：查閱 Microsoft 的[官方文件](https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started)或在 GitHub 上搜尋範例管道。
- **詢問我**：如果您遇到困難或需要特定範例（例如 Python、Java），請告訴我！

您想深入了解哪個部分？設定管道、YAML 語法，還是其他內容？