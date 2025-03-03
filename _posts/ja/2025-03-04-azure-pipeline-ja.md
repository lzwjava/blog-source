---
audio: false
generated: true
lang: ja
layout: post
title: Azure DevOps Pipelinesを使用する
translated: true
---

この内容を二つの部分に分けて説明します：**Azure DevOps Pipelinesの使用**と**パイプライン用のYAMLの作成**。それぞれについて明確で実践的な説明を提供します。

---

### **Azure DevOps Pipelinesの使用方法**
Azure DevOps Pipelinesは、CI/CD（継続的インテグレーション/継続的デプロイメント）ツールで、コードのビルド、テスト、デプロイを自動化します。以下に、始め方を示します。

#### **1. プロジェクトの設定**
- Azure DevOps（dev.azure.com）に組織でログインします。
- 「新しいプロジェクト」をクリックし、名前を付け、公開範囲（公開/非公開）を設定して新しいプロジェクトを作成します（または既存のプロジェクトを使用します）。

#### **2. コードの接続**
- プロジェクトの**Repos**に移動し、コードをリポジトリ（GitHub、Azure Repos、Bitbucketなど）にプッシュします。
- または、**Pipelines > 新しいパイプライン > 接続**の下で外部リポジトリをリンクし、ソースを選択します。

#### **3. パイプラインの作成**
- **Pipelines > ビルド > 新しいパイプライン**に移動します。
- リポジトリとブランチを選択します。
- Azureは2つのオプションを提供します：
  - **クラシックエディタ**：GUIベースのアプローチ（YAMLは不要）。
  - **YAML**：コードベースのパイプライン（柔軟性とバージョン管理のために推奨）。
- YAMLの場合、「スタートパイプライン」を選択するか、リポジトリ内の既存のファイルから設定します。

#### **4. パイプラインの定義**
- YAMLを使用する場合、リポジトリのルートに`.yml`ファイル（例：`azure-pipelines.yml`）を作成します。（以下で詳しく説明します。）
- トリガー（例：`main`へのプッシュごとに実行）、ステップ（例：ビルド、テスト）、デプロイ先を追加します。

#### **5. 実行とモニタリング**
- YAMLファイルを保存し、コミットします（またはクラシックエディタで保存）。
- **実行**をクリックしてパイプラインを手動でトリガーするか、トリガーに基づいて自動的に実行します。
- **Pipelines > ビルド**の下でログを確認し、進捗状況を監視したり、失敗をトラブルシューティングしたりします。

#### **6. デプロイ（オプション）**
- **リリース**パイプライン（**リリース**の下）を追加するか、YAMLを拡張してAzure App Service、Kubernetes、VMなどの環境にデプロイします。

---

### **Azure Pipelines用のYAMLの作成方法**
YAML（Yet Another Markup Language）は、パイプラインの設定を定義するために使用される人間が読める形式です。以下に、基本的な概要を示します。

#### **基本構造**
```yaml
trigger:
  - main  # 'main'ブランチが更新されたときにパイプラインを実行

pool:
  vmImage: 'ubuntu-latest'  # ビルドエージェント（例：Ubuntu、Windows、macOS）を指定

steps:
  - script: echo Hello, world!  # 実行する簡単なコマンド
    displayName: '一行のスクリプトを実行'
```

- **`trigger`**：パイプラインが実行されるタイミングを定義します（例：`main`へのプッシュ）。
- **`pool`**：ビルドエージェントの仮想マシンイメージを指定します。
- **`steps`**：実行するタスク（スクリプト、組み込みタスクなど）のリスト。

#### **一般的な要素**
1. **変数**:
   ```yaml
   variables:
     buildConfiguration: 'Release'
   steps:
     - script: echo $(buildConfiguration)  # 'Release'を出力
   ```

2. **ジョブ**（ステップをグループ化）：
   ```yaml
   jobs:
   - job: Build
     steps:
       - script: echo Building...
   - job: Test
     steps:
       - script: echo Testing...
   ```

3. **タスク**（事前構築されたアクション）：
   ```yaml
   steps:
     - task: DotNetCoreCLI@2  # 例：.NETプロジェクトをビルド
       inputs:
         command: 'build'
         projects: '**/*.csproj'
   ```

4. **条件**:
   ```yaml
   steps:
     - script: echo This runs only on main
       condition: eq(variables['Build.SourceBranch'], 'refs/heads/main')
   ```

5. **ステージ**（複数フェーズのパイプライン）：
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

#### **実用例**
以下は、Node.jsアプリ用のパイプラインです：
```yaml
trigger:
  - main

pool:
  vmImage: 'ubuntu-latest'

steps:
  - task: NodeTool@0  # Node.jsをインストール
    inputs:
      versionSpec: '16.x'
    displayName: 'Node.jsのインストール'

  - script: |
      npm install
      npm run build
    displayName: 'インストールとビルド'

  - task: CopyFiles@2  # ビルドアーティファクトをコピー
    inputs:
      contents: 'dist/**'
      targetFolder: '$(Build.ArtifactStagingDirectory)'

  - task: PublishBuildArtifacts@1  # アーティファクトを公開
    inputs:
      pathToPublish: '$(Build.ArtifactStagingDirectory)'
      artifactName: 'dist'
```

#### **YAMLの作成に関するヒント**
- 一貫したインデント（2スペース、タブなし）を使用します。
- エディタ（例：VS Codeの「YAML」拡張機能）で構文を検証します。
- [Azure Pipelines YAMLスキーマ](https://learn.microsoft.com/en-us/azure/devops/pipelines/yaml-schema)を参照してオプションを確認します。
- 簡単に始め、必要に応じて複雑さを追加します（例：ステージ、変数）。

---

### **次のステップ**
- **試してみる**：リポジトリを作成し、上記のような基本的な`azure-pipelines.yml`を追加して、Azure DevOpsで実行します。
- **さらに学ぶ**：Microsoftの[公式ドキュメント](https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started)を確認するか、GitHubでサンプルパイプラインを検索します。
- **質問**：トラブルに遭った場合や特定の例（例：Python、Java）が必要な場合は、お知らせください！

どの部分に深掘りしたいですか？パイプラインの設定、YAML構文、それとも他の何かですか？