---
audio: false
generated: true
lang: ja
layout: post
title: GitHub Actionsの同時実行設定
translated: true
type: note
---

現在のGitHub Actionsワークフロー設定には`cancel-in-progress: false`が既に設定されており、これは`gh-pages`同時実行グループに対して*実行中のジョブをキャンセルしない*はずです。それでもジョブがキャンセルされる場合、別の問題や設定ミスが原因である可能性があります。以下に問題を確認して修正する手順を示します：

### 1. **同時実行設定の確認**
設定はジョブのキャンセルを防ぐために正しく見えます：

```yaml
concurrency:
  group: 'gh-pages'
  cancel-in-progress: false
```

- **この設定の効果**：`concurrency`キーに`cancel-in-progress: false`を設定することで、同じ`gh-pages`グループに対する複数のワークフロー実行が互いにキャンセルせずに同時に実行できるようになります。
- **配置場所**：この`concurrency`ブロックが**ワークフローレベル**（YAMLファイルの最上位レベル、ジョブやステップ内ではない）で定義されていることを確認してください。例：

```yaml
name: Deploy to GitHub Pages
on:
  push:
    branches: [ main ]
concurrency:
  group: 'gh-pages'
  cancel-in-progress: false
jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      # ステップをここに記述
```

`concurrency`ブロックが誤って配置されている場合（例：ジョブ内）、期待通りに機能しません。必要に応じて最上位レベルに移動してください。

### 2. **競合する同時実行設定の確認**
- **複数のワークフロー**：`gh-pages`ブランチと相互作用する複数のワークフロー（別々のYAMLファイルなど）がある場合、*すべての*関連ワークフローに`cancel-in-progress: false`が設定されていることを確認してください。1つのワークフローに`cancel-in-progress: true`（または`concurrency`の欠落）があると、他のワークフローのジョブがキャンセルされる可能性があります。
- **リポジトリ設定**：リポジトリレベルの設定やサードパーティのGitHub Actionsがキャンセルを強制していないか確認してください。例えば、一部のCI/CD統合やカスタムアクションが同時実行動作を上書きする可能性があります。

### 3. **ワークフロートリガーの確認**
トリガーが誤って設定されている場合や競合状態がある場合、ジョブが「キャンセル」されたように見えることがあります。ワークフローの`on`セクションを確認してください：
- ワークフローが意図したときのみトリガーされることを確認してください（例：`on: push: branches: [ main ]`または`on: pull_request`）。
- 複数のトリガー（例：`push`と`pull_request`）が定義されている場合、重複する実行が作成される可能性があります。必要に応じて、異なるトリガーに一意の`concurrency.group`名を使用してください：

```yaml
concurrency:
  group: 'gh-pages-${{ github.event_name }}'
  cancel-in-progress: false
```

これにより、`push`と`pull_request`イベントに対して別々の同時実行グループが作成され、干渉を防ぎます。

### 4. **GitHub Actionsログの確認**
- GitHubリポジトリの**Actions**タブに移動し、キャンセルされたジョブのログを確認してください。
- ジョブがキャンセルされた理由を示すメッセージ（例：「同時実行によりキャンセルされました」や、タイムアウト、手動キャンセル、失敗などの他の理由）を探してください。
- ログに同時実行が記載されている場合、`gh-pages`ブランチに影響する*すべての*ワークフローに`cancel-in-progress: false`が設定されていることを再確認してください。

### 5. **手動キャンセルの対応**
誰かがGitHub UI経由でワークフロー実行を手動でキャンセルすると、`cancel-in-progress: false`に関係なく、その実行内のすべてのジョブが停止します。必要な場合以外は実行を手動でキャンセルしないようチームに周知してください。

### 6. **ワークフローの依存関係を考慮**
以前のステップでの依存関係や失敗によりジョブがキャンセルされている場合：
- ワークフロー内の`needs`キーワードを確認してください。1つのジョブが失敗すると、依存するジョブがスキップまたはキャンセルされる可能性があります。
- 以前のジョブが失敗した場合でも後続のジョブが実行されるように`if: always()`を使用してください：

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      # ビルドステップ
  deploy:
    needs: build
    if: always()
    runs-on: ubuntu-latest
    steps:
      # デプロイステップ
```

### 7. **最小限のワークフローでテスト**
問題が解決しない場合、問題を切り分けるために最小限のテストワークフローを作成してください：

```yaml
name: Test Concurrency
on:
  push:
    branches: [ main ]
concurrency:
  group: 'gh-pages'
  cancel-in-progress: false
jobs:
  test-job:
    runs-on: ubuntu-latest
    steps:
      - name: Sleep to simulate long job
        run: sleep 60
      - name: Print message
        run: echo "Job completed!"
```

複数のコミットをプッシュして同時実行をトリガーし、ジョブがキャンセルされずに完了することを確認してください。

### 8. **GitHub Actionsのステータスを確認**
稀に、GitHub Actionsにプラットフォーム全体の問題が発生することがあります。[GitHub Statusページ](https://www.githubstatus.com/)またはXでのGitHub Actionsの障害に関する最近の投稿を確認してください。

### 9. **デバッグのヒント**
- ワークフロー実行IDと同時実行グループをログに記録するステップを追加してください：

```yaml
steps:
  - name: Log run details
    run: echo "Run ID: ${{ github.run_id }}, Concurrency Group: ${{ github.workflow }}-${{ github.event_name }}"
```

- 必要に応じて、GitHub Actions APIを使用して実行中のワークフローをプログラムで検査してください（高度な設定が必要です）。

### それでも動作しない場合
ジョブがまだキャンセルされる場合：
- 完全なワークフローYAMLファイルと、GitHub Actionsログからのキャンセルメッセージのスクリーンショットまたは説明を共有してください。
- 特定のアクション（例：`actions/checkout`、`peaceiris/actions-gh-pages`）を使用しているか、または`gh-pages`と相互作用する複数のワークフローがあるかどうか教えてください。

これにより正確な問題を特定するのに役立ちます。さらにどのようにサポートできるかお知らせください！