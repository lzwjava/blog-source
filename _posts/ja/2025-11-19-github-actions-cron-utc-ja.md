---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: GitHub ActionsのCronはUTC時間を使用
translated: true
type: note
---

**GitHub Actionsのスケジュールワークフロー（`on: schedule:`トリガーとcron構文を使用）は、常にcron時間をUTC（協定世界時）で解釈します。**

ワークフローのYAML内で直接別のタイムゾーンを指定する組み込みサポートはありません。特定の現地時間（例：PSTの午前9時）にジョブを実行したい場合は、それを相当するUTC時間に変換し、それに応じてcron式を記述する必要があります。

### 公式ドキュメントからの要点：
- スケジュールワークフローはPOSIX cron構文を使用し、特定の**UTC時間**に実行されます。
- 例：`cron: '0 5 * * *'` は毎日UTCの午前5:00に実行されます（現地時間ではありません）。

これは長年にわたって一貫しており、2025年後半現在も変わりません — `schedule`イベントに対するネイティブのタイムゾーンパラメータは存在しません（Dependabotなどの他のGitHub機能とは異なります）。

[ワークフローをトリガーするイベント - GitHub Docs](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#schedule)  
[GitHub Actionsのワークフロー構文 - GitHub Docs](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#on-schedule)