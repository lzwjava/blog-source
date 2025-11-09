---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 配置 Azure DevOps 分支觸發器
translated: true
type: note
---

Azure DevOps Pipelines 允許您設定哪些分支會觸發建置和部署。這主要透過 **CI 觸發器**（用於程式碼推送時的建置）和 **PR 觸發器**（用於拉取請求）來實現。YAML 管道（建議用於版本控制）和傳統管道的配置略有不同。以下我將首先專注於 YAML，因為這是現代方法，然後簡要介紹傳統管道。所有範例均假設使用 Git 儲存庫。

## YAML 管道：設定分支觸發器

YAML 管道直接在您的 `azure-pipelines.yml` 檔案中定義觸發器。預設情況下，管道會在推送到**所有分支**時觸發（等同於 `trigger: branches: include: - '*'`）。您可以自定義此設定以實現更精細的控制。

### 步驟 1：基本設定
1. 在您的 Azure DevOps 專案中，前往 **Pipelines > Builds**（或用於 CD 的 **Releases**）。
2. 建立或編輯管道，並選擇 **YAML** 作為範本。
3. 在 YAML 編輯器中，於頂層新增 `trigger` 區段。

### 步驟 2：簡單分支包含
使用簡單清單來觸發特定分支或模式：
```yaml
trigger:
- main          # 在推送到 'main' 時觸發
- develop       # 同時也在 'develop' 時觸發
- releases/*    # 任何以 'releases/' 開頭的分支（例如 releases/v1.0）
```
- 儲存並提交 YAML 檔案到您的儲存庫。管道現在將僅為這些分支執行。
- 支援萬用字元，如 `*`（零個或多個字元）和 `?`（單一字元）。請為以 `*` 開頭的模式加上引號（例如 `*-hotfix`）。

### 步驟 3：進階包含/排除
用於排除或更高精確度：
```yaml
trigger:
  branches:
    include:
    - main
    - releases/*
    - feature/*
    exclude:
    - releases/old-*     # 排除 'releases/old-v1' 等
    - feature/*-draft    # 排除草稿功能分支
```
- **包含**：*可以*觸發的分支（如果省略則預設為所有分支）。
- **排除**：從包含清單中過濾掉（在包含之後應用）。
- 如果您指定任何 `branches` 子句，它將覆蓋預設值（所有分支）——只有明確包含的分支才會觸發。
- 對於標籤：在包含中使用 `refs/tags/v1.*`。

### 步驟 4：路徑篩選器（可選）
結合檔案路徑以實現細粒度控制：
```yaml
trigger:
  branches:
    include:
    - main
  paths:
    include:
    - src/*.cs          # 僅當 'src' 資料夾中有變更時
    exclude:
    - docs/*.md         # 忽略文件變更
```
- 路徑相對於儲存庫根目錄，且區分大小寫。

### 步驟 5：批次處理和選擇退出
- **批次執行**：將多次推送排入單一建置（減少干擾）：
  ```yaml
  trigger:
    batch: true
    branches:
      include:
      - main
  ```
- **停用觸發器**：設定 `trigger: none` 以停用 CI。
- **每次提交跳過**：在提交訊息中加入 `[skip ci]` 或 `***NO_CI***`。

### PR 觸發器
對於拉取請求，新增 `pr` 區段：
```yaml
pr:
  branches:
    include:
    - main
    - develop
  paths:
    include:
    - src/*
```
- 這會驗證針對這些分支的 PR。

### 測試
- 推送到符合條件的分支：管道會自動執行。
- 在 **Pipelines > Runs** 中檢視執行情況，並檢查觸發詳細資訊。

## 傳統管道：設定分支觸發器
對於舊版/傳統管道（基於 UI）：
1. 在 **Pipelines > Builds** 中編輯您的管道。
2. 前往 **Triggers > Continuous integration**。
3. 勾選 **Enable continuous integration**。
4. 在 **Branch filters** 下，新增包含（例如 `main`）或排除（例如 `develop`）。
5. 對於路徑：在同一標籤頁中使用 **Path filters**。
6. 對於 PR：前往 **Triggers > Pull request validation** 並設定分支篩選器。

建議切換到 YAML 以獲得更好的可維護性。

## 最佳實踐
- 從簡單開始：僅在 `main` 和 `develop` 上觸發。
- 對嘈雜分支（如 `*-hotfix`）使用排除。
- 使用分支策略（Repos > Branches > Policies）來設定必要的審核者以確保安全。
- 監控：使用管道分析來檢視觸發頻率。

有關最新詳細資訊，請參閱官方文件。

[建置 Azure Repos Git 儲存庫](https://learn.microsoft.com/en-us/azure/devops/pipelines/repos/azure-repos-git?view=azure-devops&tabs=yaml)  
[Azure Pipelines 中的觸發器](https://learn.microsoft.com/en-us/azure/devops/pipelines/build/triggers?view=azure-devops&tabs=yaml)