---
audio: false
generated: true
lang: ja
layout: post
title: Azure DevOps パイプラインの活用
translated: true
type: note
---

これを2つのパートに分けて説明します：**Azure DevOps Pipelinesの使用方法**と**パイプラインのYAML記述方法**です。両方について明確で実践的な説明を提供します。

---

### **Azure DevOps Pipelinesの使用方法**
Azure DevOps Pipelinesは、コードのビルド、テスト、デプロイを自動化するCI/CD（継続的インテグレーション/継続的デプロイメント）ツールです。始め方は以下の通りです：

#### **1. プロジェクトの設定**
- ご自身の組織でAzure DevOps (dev.azure.com) にログインします。
- 「New Project」をクリックし、名前を付け、公開設定（公開/非公開）を選択して新しいプロジェクトを作成（または既存のプロジェクトを使用）します。

#### **2. コードの接続**
- プロジェクト内の **Repos** に移動し、コードをリポジトリ（GitHub、Azure Repos、Bitbucketなど）にプッシュします。
- または、**Pipelines > New Pipeline > Connect** で外部リポジトリをリンクし、ソースを選択します。

#### **3. パイプラインの作成**
- **Pipelines** > **Builds** > **New Pipeline** に移動します。
- リポジトリとブランチを選択します。
- Azureは2つのオプションを提供します：
  - **クラシック エディター**: GUIベースのアプローチ（YAML不要）。
  - **YAML**: コードベースのパイプライン（柔軟性とバージョン管理のため推奨）。
- YAMLの場合、リポジトリ内の既存ファイルから「Starter pipeline」を選択するか、構成します。

#### **4. パイプラインの定義**
- YAMLを使用する場合は、リポジトリのルートに `.yml` ファイル（例: `azure-pipelines.yml`）を記述します（詳細は後述）。
- トリガー（例: `main` ブランチへのプッシュ時に実行）、ステップ（例: ビルド、テスト）、デプロイターゲットを追加します。

#### **5. 実行と監視**
- YAMLファイルを保存してコミットします（またはクラシックエディターで保存します）。
- **Run** をクリックして手動でパイプラインをトリガーするか、トリガーに基づいて自動実行させます。
- **Pipelines > Builds** でログを確認し、進捗を監視したり、失敗のトラブルシューティングを行います。

#### **6. デプロイ（オプション）**
- **リリース パイプライン**（**Releases** 内）を追加するか、YAMLを拡張してAzure App Service、Kubernetes、VMなどの環境にデプロイします。

---

### **Azure PipelinesのYAML記述方法**
YAML (Yet Another Markup Language) は、パイプライン構成を定義するために使用される人間が読みやすい形式です。ここでは短期集中講座を提供します：

#### **基本構造**
```yaml
trigger:
  - main  # 'main' ブランチが更新されたときにパイプラインを実行

pool:
  vmImage: 'ubuntu-latest'  # ビルドエージェントを指定 (例: Ubuntu, Windows, macOS)

steps:
  - script: echo Hello, world!  # 実行する単純なコマンド
    displayName: '一行スクリプトを実行'
```

- **`trigger`**: パイプラインが実行される条件を定義します（例: `main` へのプッシュ時）。
- **`pool`**: ビルドエージェントの仮想マシンイメージを指定します。
- **`steps`**: 実行するタスク（スクリプト、組み込みタスクなど）をリストします。

#### **一般的な要素**
1. **変数**:
   ```yaml
   variables:
     buildConfiguration: 'Release'
   steps:
     - script: echo $(buildConfiguration)  # 'Release' を出力
   ```

2. **ジョブ**（ステップをグループ化）:
   ```yaml
   jobs:
   - job: Build
     steps:
       - script: echo ビルド中...
   - job: Test
     steps:
       - script: echo テスト中...
   ```

3. **タスク**（事前に構築されたアクション）:
   ```yaml
   steps:
     - task: DotNetCoreCLI@2  # 例: .NETプロジェクトをビルド
       inputs:
         command: 'build'
         projects: '**/*.csproj'
   ```

4. **条件**:
   ```yaml
   steps:
     - script: echo これはmainでのみ実行される
       condition: eq(variables['Build.SourceBranch'], 'refs/heads/main')
   ```

5. **ステージ**（マルチフェーズパイプライン用）:
   ```yaml
   stages:
   - stage: Build
     jobs:
       - job: BuildJob
         steps:
           - script: echo ビルド中...
   - stage: Deploy
     dependsOn: Build
     jobs:
       - job: DeployJob
         steps:
           - script: echo デプロイ中...
   ```

#### **実世界の例**
Node.jsアプリ用のパイプライン例：
```yaml
trigger:
  - main

pool:
  vmImage: 'ubuntu-latest'

steps:
  - task: NodeTool@0  # Node.jsをインストール
    inputs:
      versionSpec: '16.x'
    displayName: 'Node.jsをインストール'

  - script: |
      npm install
      npm run build
    displayName: 'インストールとビルド'

  - task: CopyFiles@2  # ビルド成果物をコピー
    inputs:
      contents: 'dist/**'
      targetFolder: '$(Build.ArtifactStagingDirectory)'

  - task: PublishBuildArtifacts@1  # 成果物を公開
    inputs:
      pathToPublish: '$(Build.ArtifactStagingDirectory)'
      artifactName: 'dist'
```

#### **YAML記述のヒント**
- 一貫したインデント（タブではなくスペース2つ）を使用します。
- エディター（例: 「YAML」拡張機能付きVS Code）で構文を検証します。
- オプションについては [Azure Pipelines YAML スキーマ](https://learn.microsoft.com/en-us/azure/devops/pipelines/yaml-schema) を参照します。
- 必要に応じて（ステージ、変数など）複雑さを追加する前に、シンプルに始めます。

---

### **次のステップ**
- **試してみる**: リポジトリを作成し、上記のような基本的な `azure-pipelines.yml` を追加し、Azure DevOpsで実行します。
- **さらに学ぶ**: Microsoftの[公式ドキュメント](https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started)を確認するか、GitHubでサンプルパイプラインを検索します。
- **質問する**: 行き詰まった場合、または特定の例（Python、Javaなど）が必要な場合は、お知らせください！

どの部分についてより深く掘り下げたいですか？パイプラインの設定、YAML構文、それとも他の何か？