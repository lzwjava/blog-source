---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: Azure DevOps エッセンシャルガイド
translated: true
type: note
---

Azure DevOpsは、Microsoftが提供するクラウドベースの包括的な開発ツールセットであり、チームが効率的にソフトウェアの計画、開発、テスト、提供を行うことを支援します。AzureやGitHubなどの他のMicrosoftサービスとシームレスに統合され、Agile、Scrum、DevOpsプラクティスなどの様々な手法をサポートします。このガイドでは、基本事項（概要、主要コンポーネント、はじめ方、ベストプラクティス、詳細な学習リソース）をカバーします。

## Azure DevOpsとは？
Azure DevOpsは、開発、運用、ステークホルダーにわたるコラボレーションを可能にするエンドツーエンドのDevOps機能を提供します。これはプラットフォーム非依存であり、複数の言語、フレームワーク、ツールをサポートします。主な利点は以下の通りです：
- **スケーラビリティ**: 小規模チームからエンタープライズまで、あらゆる規模のプロジェクトを扱います。
- **統合**: Visual Studio、GitHub、Slack、JiraなどのIDEと接続します。
- **セキュリティ**: ロールベースのアクセス制御（RBAC）や監査ログなどの組み込みコンプライアンス機能。
- **価格**: 最大5ユーザーまで無料。追加機能については有料プランが$6/ユーザー/月から。

2025年現在、Azure DevOpsは、強化されたAI統合（例：GitHub Copilot for Azure）および改善されたパイプライン分析機能を備えて進化しています。

## 主要コンポーネント
Azure DevOpsは、5つのコアサービスで構成され、それぞれWebポータルまたはAPI経由でアクセス可能です：

### 1. **Boards**
   - **目的**: 作業項目のための視覚的な計画および追跡ツール。
   - **機能**:
     - ワークフローを視覚化するためのかんばんボード。
     - タスクの優先順位付けのためのバックログ。
     - アジャイル反復のためのスプリント。
     - カスタムレポートのためのクエリ。
   - **ユースケース**: バグ、機能、タスクをリアルタイムで追跡。

### 2. **Repos**
   - **目的**: コードのための集中型バージョン管理。
   - **機能**:
     - GitまたはTFVCリポジトリ。
     - ブランチ戦略とプルリクエスト。
     - ドキュメントのためのWiki統合。
   - **ユースケース**: コードレビューでの協業と履歴の維持。

### 3. **Pipelines**
   - **目的**: CI/CD（継続的インテグレーション/継続的デリバリー）自動化。
   - **機能**:
     - YAMLベースまたはクラシックパイプライン。
     - マルチステージビルド、テスト、デプロイメント。
     - パッケージ管理のためのAzure Artifactsとの統合。
     - 承認とゲートのための環境。
   - **ユースケース**: すべてのコミットに対してビルドを自動化し、クラウドまたはオンプレミスにデプロイ。

### 4. **Test Plans**
   - **目的**: 手動テストおよび探索的テスト。
   - **機能**:
     - テストケース管理。
     - ライブログと添付ファイル。
     - Pipelinesからの自動テストとの統合。
   - **ユースケース**: リリース前の品質を確保。

### 5. **Artifacts**
   - **目的**: パッケージ管理と依存関係の処理。
   - **機能**:
     - ユニバーサルパッケージ、NuGet、npm、およびMavenフィード。
     - バイナリのためのリテンションポリシー。
   - **ユースケース**: チーム間でライブラリを共有およびバージョン管理。

## はじめに
Azure DevOpsをセットアップするには、以下の手順に従ってください：

1. **アカウントを作成**:
   - [dev.azure.com](https://dev.azure.com)にアクセスし、Microsoftアカウントでサインアップ（無料ティア利用可能）。
   - 新しい組織を作成（例: "MyProjectOrg"）。

2. **プロジェクトをセットアップ**:
   - 組織内で「新しいプロジェクト」をクリック。
   - 可視性（プライベート/パブリック）とバージョン管理（Git/TFVC）を選択。
   - メール招待でチームメンバーを追加。

3. **Reposを設定**:
   - デフォルトのリポジトリをクローン: `git clone https://dev.azure.com/{org}/{project}/_git/{repo}`。
   - 初期コードをプッシュ: `git add . && git commit -m "Initial commit" && git push`。

4. **シンプルなパイプラインを構築**:
   - Pipelines > 新しいパイプライン > リポジトリを選択 > ASP.NET（または使用するフレームワーク）。
   - シンプルさのためにYAMLを使用：
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
   - パイプラインを保存して実行。

5. **ボードを作成**:
   - Boards > Sprints > 新しいクエリへ移動。
   - 作業項目タイプを定義（例: Epic > Feature > Task）。

6. **テストとデプロイ**:
   - パイプラインにテストタスクを追加。
   - Azure App Serviceへのデプロイのためにリリースパイプラインを設定。

ハンズオンチュートリアルについては、公式のクイックスタートから始めてください。

## ベストプラクティス
- **YAMLパイプラインを採用**: バージョン管理され、再利用可能です。
- **ブランチポリシーを使用**: プルリクエストの承認とリンクされた作業項目を必須にします。
- **セキュリティスキャンを実装**: SonarQubeやMicrosoft Defenderなどのツールを統合。
- **分析で監視**: ベロシティとビルド成功率のためにダッシュボードを使用。
- **拡張機能でスケール**: マーケットプレイスには2,000以上の拡張機能があります（例: Slack通知）。
- **ハイブリッドサポート**: オンプレミスの場合は、Azure DevOps Server（セルフホステッド）を使用。

一般的な落とし穴: 早期の過度なカスタマイズ—シンプルに始めて反復的に改善。

## 高度なトピック
- **拡張機能とマーケットプレイス**: JenkinsやTerraformなどのツール用のプラグインでカスタマイズ。
- **AI/ML統合**: パイプライン内でのモデルデプロイメントにAzure MLを使用。
- **マルチチームコラボレーション**: 大規模組織向けにエリアと反復を活用。
- **移行**: GitHubやJiraからのインポートツール。

## 参考資料
- [Azure DevOps ドキュメント](https://learn.microsoft.com/ja-jp/azure/devops/)
- [Azure DevOps を使ってみる](https://learn.microsoft.com/ja-jp/azure/devops/get-started/what-is-azure-devops)
- [Azure DevOps の価格](https://azure.microsoft.com/ja-jp/pricing/details/devops/azure-devops-services/)
- [Azure Pipelines のベスト プラクティス](https://learn.microsoft.com/ja-jp/azure/devops/pipelines/)