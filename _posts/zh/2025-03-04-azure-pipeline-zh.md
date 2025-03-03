---
audio: false
generated: true
lang: zh
layout: post
title: 使用 Azure DevOps 管道
translated: true
---

让我们将其分为两个部分：**使用 Azure DevOps Pipelines** 和 **编写 YAML 管道**。我将为两者提供清晰、实用的解释。

---

### **如何使用 Azure DevOps Pipelines**
Azure DevOps Pipelines 是一个 CI/CD（持续集成/持续部署）工具，用于自动化构建、测试和部署代码。以下是入门指南：

#### **1. 设置项目**
- 登录 Azure DevOps（dev.azure.com）并使用您的组织。
- 通过点击“新建项目”，给项目命名并设置可见性（公开/私有）来创建一个新项目（或使用现有项目）。

#### **2. 连接代码**
- 进入项目中的 **Repos**，将代码推送到仓库（GitHub、Azure Repos、Bitbucket 等）。
- 或者在 **Pipelines > 新建管道 > 连接** 下链接外部仓库并选择源。

#### **3. 创建管道**
- 导航到 **Pipelines > 构建 > 新建管道**。
- 选择您的仓库和分支。
- Azure 提供两个选项：
  - **经典编辑器**：基于 GUI 的方法（不需要 YAML）。
  - **YAML**：基于代码的管道（推荐用于灵活性和版本控制）。
- 对于 YAML，选择“入门管道”或从仓库中的现有文件配置。

#### **4. 定义管道**
- 如果使用 YAML，您将在仓库的根目录中编写一个 `.yml` 文件（例如 `azure-pipelines.yml`）（下面会详细介绍）。
- 添加触发器（例如在每次推送到 `main` 时运行），步骤（例如构建、测试）和部署目标。

#### **5. 运行和监控**
- 保存并提交 YAML 文件（或在经典编辑器中保存）。
- 点击 **运行** 手动触发管道，或者根据触发器自动运行。
- 在 **Pipelines > 构建** 下检查日志以监控进度或排查失败。

#### **6. 部署（可选）**
- 添加 **发布管道**（在 **发布** 下）或扩展您的 YAML 以部署到 Azure App Service、Kubernetes 或 VM 等环境。

---

### **如何为 Azure Pipelines 编写 YAML**
YAML（Yet Another Markup Language）是一种用于定义管道配置的易读格式。以下是快速入门指南：

#### **基本结构**
```yaml
trigger:
  - main  # 当 'main' 分支更新时运行管道

pool:
  vmImage: 'ubuntu-latest'  # 指定构建代理的虚拟机镜像（例如 Ubuntu、Windows、macOS）

steps:
  - script: echo Hello, world!  # 运行一个简单的命令
    displayName: '运行一行脚本'
```

- **`trigger`**：定义管道运行时机（例如在推送到 `main` 时）。
- **`pool`**：指定构建代理的虚拟机镜像。
- **`steps`**：列出要执行的任务（脚本、内置任务等）。

#### **常见元素**
1. **变量**：
   ```yaml
   variables:
     buildConfiguration: 'Release'
   steps:
     - script: echo $(buildConfiguration)  # 输出 'Release'
   ```

2. **作业**（分组步骤）：
   ```yaml
   jobs:
   - job: Build
     steps:
       - script: echo Building...
   - job: Test
     steps:
       - script: echo Testing...
   ```

3. **任务**（预构建操作）：
   ```yaml
   steps:
     - task: DotNetCoreCLI@2  # 示例：构建 .NET 项目
       inputs:
         command: 'build'
         projects: '**/*.csproj'
   ```

4. **条件**：
   ```yaml
   steps:
     - script: echo 这只在 main 上运行
       condition: eq(variables['Build.SourceBranch'], 'refs/heads/main')
   ```

5. **阶段**（用于多阶段管道）：
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

#### **实际示例**
这是一个 Node.js 应用的管道：
```yaml
trigger:
  - main

pool:
  vmImage: 'ubuntu-latest'

steps:
  - task: NodeTool@0  # 安装 Node.js
    inputs:
      versionSpec: '16.x'
    displayName: '安装 Node.js'

  - script: |
      npm install
      npm run build
    displayName: '安装和构建'

  - task: CopyFiles@2  # 复制构建工件
    inputs:
      contents: 'dist/**'
      targetFolder: '$(Build.ArtifactStagingDirectory)'

  - task: PublishBuildArtifacts@1  # 发布工件
    inputs:
      pathToPublish: '$(Build.ArtifactStagingDirectory)'
      artifactName: 'dist'
```

#### **编写 YAML 的技巧**
- 使用一致的缩进（2 个空格，不使用制表符）。
- 使用编辑器验证语法（例如 VS Code 使用“YAML”扩展）。
- 参考 [Azure Pipelines YAML 结构](https://learn.microsoft.com/en-us/azure/devops/pipelines/yaml-schema) 了解选项。
- 从简单开始，然后根据需要添加复杂性（例如阶段、变量）。

---

### **下一步**
- **尝试**：创建一个仓库，添加一个基本的 `azure-pipelines.yml` 文件（如上所示），并在 Azure DevOps 中运行它。
- **学习更多**：查看 Microsoft 的 [官方文档](https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started) 或在 GitHub 上搜索示例管道。
- **问我**：如果遇到问题或需要特定示例（例如 Python、Java），告诉我！

您想深入了解哪个部分？设置管道、YAML 语法还是其他内容？