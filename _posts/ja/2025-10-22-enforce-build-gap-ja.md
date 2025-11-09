---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: 30分間のビルド間隔の強制
translated: true
type: note
---

### ビルド間に30分の間隔を強制するワークフローの変更

Jekyllデプロイメントワークフローが頻繁に実行されないようにする（つまり、連続する実行間に少なくとも30分の間隔を設ける）ためには、`build`ジョブの早い段階に条件付きステップを追加できます。このステップは、GitHub APIに対してこのワークフローの直近の成功した実行のタイムスタンプを問い合わせます。現在のトリガーがその実行の完了時刻から30分以内の場合、ジョブはメッセージを表示して早期終了し（ビルドをスキップします）。

このアプローチは：
- GitHub REST APIを使用します（外部ツールは不要です）。
- **成功した**前回の実行のみをチェックします（status: "completed", conclusion: "success"）。
- 時間差を秒単位で計算し、1800（30分）と比較します。
- 既存のpushトリガーと`workflow_dispatch`トリガーで動作します。
- 同時実行設定（重複する実行を処理する）を妨げません。

#### 更新されたYAMLスニペット
この新しいステップを`build`ジョブの「Checkout Repository」ステップの直後に挿入してください。ワークフローの残りの部分は変更されません。

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    environment: github-pages
    env:
      GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      TELEGRAM_BOT_API_KEY: ${{ secrets.TELEGRAM_BOT_API_KEY }}
      OPENROUTER_API_KEY: ${{ secrets.OPENROUTER_API_KEY }}

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 5

      - name: Enforce 30-Minute Build Gap
        id: cooldown
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          # このワークフローの直近の成功した実行を取得
          RUNS_RESPONSE=$(curl -s -H "Authorization: token $GITHUB_TOKEN" \
            -H "Accept: application/vnd.github.v3+json" \
            "https://api.github.com/repos/${{ github.repository }}/actions/workflows/${{ github.workflow_ref }}/runs?status=completed&conclusion=success&per_page=1&sort=timestamp&direction=desc")

          # 直近の成功した実行のcompleted_atタイムスタンプを抽出 (ISO 8601形式)
          LAST_COMPLETED_AT=$(echo "$RUNS_RESPONSE" | jq -r '.[0].completed_at // empty')
          
          if [ -z "$LAST_COMPLETED_AT" ] || [ "$LAST_COMPLETED_AT" = "null" ]; then
            echo "No previous successful run found. Proceeding with build."
            echo "skip_build=false" >> $GITHUB_OUTPUT
            exit 0
          fi

          # タイムスタンプをUnix秒に変換して比較
          CURRENT_TIME=$(date -u +%s)
          LAST_TIME=$(date -d "$LAST_COMPLETED_AT" +%s)
          TIME_DIFF=$((CURRENT_TIME - LAST_TIME))

          echo "Last successful run completed at: $LAST_COMPLETED_AT (diff: ${TIME_DIFF}s)"

          if [ $TIME_DIFF -lt 1800 ]; then  # 1800 seconds = 30 minutes
            echo "Build skipped: Less than 30 minutes since last successful run."
            echo "skip_build=true" >> $GITHUB_OUTPUT
            exit 0
          else
            echo "Sufficient time gap. Proceeding with build."
            echo "skip_build=false" >> $GITHUB_OUTPUT
            exit 0
          fi

      # クールダウンチェックが失敗した場合、ビルド全体をスキップ (後続のステップにこの条件を追加するか、ビルドをifでラップ)
      - name: Set up Python 3.13.2
        if: steps.cooldown.outputs.skip_build != 'true'
        uses: actions/setup-python@v4
        with:
          python-version: "3.13.2"

      # ... (この後の残りのすべてのステップに 'if: steps.cooldown.outputs.skip_build != 'true'' 条件を繰り返し追加)
```

#### 主な変更点の説明
1. **APIクエリ**:
   - `curl`を使用してGitHub Actions APIエンドポイント（ワークフロー実行用）にリクエストを送信します。
   - 完了した成功した実行のみを取得するために、`status=completed`と`conclusion=success`でフィルタリングします。
   - 最新のものを取得するために、`per_page=1`に制限し、`timestamp desc`でソートします。
   - `completed_at`（前回の実行の正確な終了時刻）を抽出します。

2. **時間計算**:
   - `date`を使用して、現在時刻と前回の完了時刻の両方をUnixタイムスタンプに変換します。
   - 差を秒単位で計算します。
   - もし`< 1800`秒の場合、`skip_build=true`を設定し、ステップを早期終了します。

3. **条件付き実行**:
   - **後続のすべてのステップ**（例: Pythonセットアップ、依存関係のインストール、Sync built siteまで）に`if: steps.cooldown.outputs.skip_build != 'true'`を追加します。
   - これにより、クールダウンがトリガーされた場合、ジョブはGitHub UIで「skipped」と報告されますが、理由はログに記録されます。

4. **考慮されたエッジケース**:
   - 前回の実行がない場合: 処理を続行します（初回ビルド）。
   - 失敗した/実行中の前回の実行: それらを無視して処理を続行します。
   - APIエラー: 処理を続行するようにフォールバックします（安全なデフォルト）。
   - `jq`は`ubuntu-latest`にプリインストールされているため、追加のセットアップは不要です。

#### 変更のテスト
- これを`main`ブランチにコミットします（ワークフローがトリガーされます）。
- 複数の迅速なプッシュ/ディスパッチをトリガーします: 30分以内の2回目はスキップされるはずです。
   - 「Build skipped」メッセージについては、ジョブログを監視してください。
- 間隔を調整したい場合（例: 1時間）、`1800`を`3600`に変更してください。

#### 代替案
- **スケジュールトリガー**: プッシュに関係なく30分ごとに*定期的な*ビルドが必要な場合は、`on:`セクションに以下を追加します:
  ```yaml
  schedule:
    - cron: '*/30 * * * *'  # 30分ごと
  ```
  ただし、これはプッシュトリガーに対して間隔を強制しません—必要に応じてクールダウンステップと併用してください。
- **カスタムアクション**: 再利用性のために、クールダウンロジックを再利用可能なワークフローまたはコンポジットアクションにラップします。
- **制限事項**: これは実行の完了時刻をチェックし、開始時刻ではありません。前回の実行がまだ実行中で>30分経過している場合、同時実行がそれをキャンセルします。

これがあなたの正確な意図に合わない場合（例えば、*少なくとも*30分ごとのスケジューリングを意味していた場合）、詳細を提供してください！