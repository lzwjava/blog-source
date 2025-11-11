---
audio: false
generated: true
lang: ja
layout: post
title: GitHub ActionsのCronスケジューリング
translated: true
type: note
---

はい、GitHub Actionsのcronスケジュールを使用することで、GitHubワークフローを毎日1回実行するように設定できます。

### 解説
GitHub Actionsでは、`.github/workflows`ディレクトリ内のYAMLファイルで定義されるワークフローを通じて、リポジトリ内のタスクを自動化できます。ワークフローをトリガーする方法の一つに、`schedule`イベントを使用する方法があり、cron形式の構文を使ってワークフローを実行するタイミングを指定します。GitHub Actionsにおけるcron構文は標準的なPOSIX形式に従い、5つのフィールド（分、時、日、月、曜日）で構成されます。

ワークフローを毎日1回実行するには、`0 0 * * *`のようなcron式を使用します。これは「毎日UTCの00:00に実行」という意味です。各フィールドの内訳は以下の通りです：
- **分 (0)**: 毎時の0分
- **時 (0)**: 00:00（深夜）UTC
- **日 (*)**: 毎日
- **月 (*)**: 毎月
- **曜日 (*)**: 毎日

### 設定例
以下は、毎日1回実行されるGitHub Actionsワークフローの設定例です：

```yaml
name: Daily Workflow
on:
  schedule:
    - cron: '0 0 * * *'
jobs:
  example-job:
    runs-on: ubuntu-latest
    steps:
      - name: Print message
        run: echo "This runs once a day!"
```

このワークフローは、毎日UTCの深夜0時に実行されます。

### 主な注意点
- **タイムゾーン**: スケジュールはUTCで動作するため、特定の現地時間で実行する必要がある場合はcron式を調整してください。
- **デフォルトブランチ**: 特に指定がない場合、スケジュールされたワークフローはリポジトリのデフォルトブランチ（例：`main`や`master`）で実行されます。
- **信頼性**: GitHub Actionsは指定された時間にワークフローを実行することを目指していますが、インフラの負荷によりわずかな遅延が発生する可能性があります（稀なケースです）。
- **使用制限**: 無料のGitHubアカウントではActionsの使用量に制限（例：月間分数）がありますが、1日1回の実行は通常これらの制限内に収まります。

### 結論
ワークフローファイルに適切に設定されたcron式を使用することで、GitHub Actionsは確かにワークフローを毎日1回実行できます。したがって、ご質問に対する答えは**はい**となります。