---
audio: false
generated: true
lang: ja
layout: post
title: Dependabotの削除
translated: true
type: note
---

GitHub Actions から Dependabot を削除するには、ワークフローをトリガーするプルリクエストを作成する機能を無効にし、必要に応じて Dependabot に特化したカスタムワークフローも削除する必要があります。以下にその手順を説明します。お問い合わせの「dependant bot」は、GitHub で依存関係を管理する一般的なツール「Dependabot」を指すと想定します。

---

### ステップ 1: Dependabot バージョン更新を無効にする
Dependabot のバージョン更新は、依存関係を最新に保つためにプルリクエストを自動的に作成します。これらのプルリクエストは GitHub Actions ワークフローをトリガーする可能性があります。この機能を無効にするには:

- **設定ファイルを特定**: リポジトリの `.github` ディレクトリに `dependabot.yml` ファイルがあるか確認してください。
- **ファイルを削除**: 存在する場合は、`dependabot.yml` ファイルを削除し、この変更をコミットしてください。これにより、Dependabot がバージョン更新用のプルリクエストを作成するのを停止します。
- **確認**: `dependabot.yml` ファイルが存在しない場合、バージョン更新は既に無効になっています。

---

### ステップ 2: Dependabot セキュリティ更新を無効にする
Dependabot のセキュリティ更新は、依存関係の脆弱性を修正するプルリクエストを生成し、これも GitHub Actions ワークフローをトリガーする可能性があります。これをオフにするには:

- **リポジトリ設定に移動**: GitHub リポジトリで **Settings** タブをクリックします。
- **セキュリティ設定に移動**: **Security & analysis** (または GitHub インターフェースに応じて **Code security and analysis**) までスクロールします。
- **セキュリティ更新を無効化**: **Dependabot security updates** を見つけて **Disable** をクリックします。

これにより、Dependabot がセキュリティ修正用のプルリクエストを作成するのを防ぎます。

---

### ステップ 3: (オプション) カスタムの Dependabot 関連ワークフローを削除する
Dependabot のプルリクエストを処理するために GitHub Actions ワークフローを特別に設定している場合 (例: 自動マージ、ラベル付け、Dependabot メタデータの使用)、これらをクリーンアップすることもできます:

- **ワークフローファイルを確認**: `.github/workflows` ディレクトリ内の YAML ファイルを調べてください。
- **Dependabot ロジックを特定**: `if: github.event.pull_request.user.login == 'dependabot[bot]'` のような条件や、`dependabot/fetch-metadata` のようなアクションを検索してください。
- **削除または変更**: これらのワークフローを削除するか、Dependabot 固有のロジックを削除するように修正し、変更をコミットしてください。

このステップはオプションです。ステップ 1 と 2 で Dependabot を無効にすると、新しいプルリクエストが作成されなくなるため、既存のワークフローが Dependabot によってトリガーされることはなくなります。ただし、これらのワークフローを削除することで、完全なクリーンアップが保証されます。

---

### 追加の注意点
- **既存のプルリクエスト**: Dependabot を無効にしても、既に作成されたプルリクエストは閉じられません。これらが更新されると、ワークフローをトリガーする可能性があります。必要に応じて手動で閉じてください。
- **Dependabot アラート**: 脆弱性通知も停止したい場合 (GitHub Actions に直接関連しない)、**Settings > Security & analysis** に移動し、**Dependabot alerts** を無効にしてください。これはオプションであり、ワークフローのトリガーとは無関係です。

---

### 結果
ステップ 1 と 2 を完了することで、Dependabot はリポジトリ内でプルリクエストを作成しなくなり、GitHub Actions への影響が事実上「削除」されます。Dependabot 用にワークフローをカスタマイズしていた場合、ステップ 3 により関連するすべての自動化がなくなります。これで、GitHub Actions は他のイベントに基づいてのみ実行され、Dependabot の影響を受けなくなります。