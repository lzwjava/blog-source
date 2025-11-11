---
audio: false
generated: true
lang: ja
layout: post
title: GitHub Actionsのトリガー
translated: true
type: note
---

はい、GitHub Action は別の GitHub Action をトリガーできますが、直接的にではありません。GitHub Actions ワークフローは通常、プッシュ、プルリクエスト、スケジュールなどの特定のイベントによってトリガーされますが、あるワークフローが別のワークフローをトリガーするようにするには、いくつかの間接的な方法があります。以下に主な方法を示します：

---

### 1. `workflow_dispatch` イベントの使用
GitHub API を使用して `workflow_dispatch` イベントを介して、プログラムでワークフローをトリガーできます。これにより、あるワークフローがこのイベントをリッスンするように設定された別のワークフローを開始できます。

- **仕組み**: 最初のワークフローが API コールを行い、2 番目のワークフローをトリガーします。
- **例**:
  ```yaml
  name: 別のワークフローをトリガー
  on: [push]
  jobs:
    trigger:
      runs-on: ubuntu-latest
      steps:
        - name: ワークフローをトリガー
          run: |
            curl -X POST \
              -H "Authorization: token ${{ secrets.GITHUB_TOKEN }}" \
              -H "Accept: application/vnd.github.v3+json" \
              https://api.github.com/repos/<owner>/<repo>/actions/workflows/<workflow_id>/dispatches \
              -d '{"ref": "main"}'
  ```
  `<owner>`, `<repo>`, `<workflow_id>` をあなたのリポジトリの詳細とターゲットワークフローの ID に置き換えてください。2 番目のワークフローはその設定に `on: [workflow_dispatch]` を含んでいる必要があります。

---

### 2. リポジトリディスパッチイベントの使用
ワークフローは、リポジトリディスパッチを介してカスタムイベントを送信できます。別のワークフローがそのイベントをリッスンしてトリガーすることができます。

- **仕組み**: 最初のワークフローが GitHub API を介してリポジトリディスパッチイベントを送信し、2 番目のワークフローがそのイベントに応答します。
- **例**:
  - 最初のワークフロー (イベントを送信):
    ```yaml
    name: ディスパッチイベントを送信
    on: [push]
    jobs:
      send-dispatch:
        runs-on: ubuntu-latest
        steps:
          - name: ディスパッチを送信
            run: |
              curl -X POST \
                -H "Authorization: token ${{ secrets.GITHUB_TOKEN }}" \
                -H "Accept: application/vnd.github.v3+json" \
                https://api.github.com/repos/<owner>/<repo>/dispatches \
                -d '{"event_type": "custom_event"}'
    ```
  - 2 番目のワークフロー (イベントによってトリガー):
    ```yaml
    name: ディスパッチによってトリガー
    on:
      repository_dispatch:
        types: [custom_event]
    jobs:
      respond:
        runs-on: ubuntu-latest
        steps:
          - name: イベントに応答
            run: echo "custom_event によってトリガーされました"
    ```

---

### 3. Git イベントを介したトリガー
あるワークフローは、コミットの作成やプルリクエストのオープンなど、Git イベントを生成することで、2 番目のワークフローをトリガーできます。2 番目のワークフローはそのイベント（例: `on: [push]`）に応答するように設定されています。

- **仕組み**: 最初のワークフローがリポジトリを変更し（例: コミットをプッシュ）、そのイベントに対して設定された 2 番目のワークフロー（例: `on: [push]`）をトリガーします。
- **例**:
  ```yaml
  name: コミットを作成
  on: [push]
  jobs:
    create-commit:
      runs-on: ubuntu-latest
      steps:
        - name: Checkout
          uses: actions/checkout@v2
        - name: ファイルを作成
          run: echo "New file" > newfile.txt
        - name: コミットとプッシュ
          run: |
            git config user.name "GitHub Action"
            git config user.email "action@github.com"
            git add newfile.txt
            git commit -m "新しいファイルを追加"
            git push
  ```
  これは、`push` イベントで実行するように設定された別のワークフローをトリガーする可能性があります。

---

### 主な考慮事項
- **権限**: API コールで使用される GitHub トークンは、ワークフローをトリガーしたりディスパッチイベントを送信したりするための十分な権限を持っている必要があります。
- **レート制限**: 特に頻繁に実行されるワークフローでは、GitHub の API レート制限に注意してください。
- **ループの回避**: ワークフローが互いに無限にトリガーし合うのを防ぐために、条件を追加してください。
- **設定**: ターゲットワークフローが意図したイベントをリッスンするように正しく設定されていることを確認してください。

---

### 結論
GitHub Actions はあるワークフローが別のワークフローを直接呼び出す仕組みを提供していませんが、`workflow_dispatch`、リポジトリディスパッチイベント、またはコミットやプルリクエストなどの Git イベントを間接的に使用してこれを実現できます。これらの方法により、必要に応じてワークフローを効果的に連鎖させたりトリガーしたりすることができます。