---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: Cronによる自動Git同期
translated: true
type: note
---

あるノートパソコンでの Git プッシュによる更新を、別のノートパソコン上の同じリポジトリのクローンに自動的に同期するには（手動での `git pull` なし）、Git だけに依存してマシン間でリアルタイムの「自動」更新を行うことはできません。Git は設計上、プルベースだからです。しかし、2台目のノートパソコンにスケジュールされたタスクを設定し、リモート（あなたの場合は GitHub）からの変更を定期的にフェッチしてマージすることができます。これは、あなたのような個人設定において最もシンプルで信頼性の高い方法です。

以下は、あなたの Mac（MacBook Air を使用しているため）で行う方法です。スケジューリングには、組み込みで軽量な `cron` を使用します。両方のノートパソコンが `github.com:lzwjava/blog-source` のクローンを持ち、あなたが `main` ブランチにいるものとします。

### ステップ 1: 2台目のノートパソコンのリポジトリが正しく設定されていることを確認する
2台目のノートパソコンで:
1.  リポジトリに移動: `cd /path/to/blog-source`
2.  リモートを追跡していることを確認: `git remote -v` (`origin` があなたの GitHub リポジトリを示すはずです)。
3.  そうでない場合は追加: `git remote add origin git@github.com:lzwjava/blog-source.git`
4.  現在の状態をフェッチ: `git fetch origin`
5.  main に切り替え: `git checkout main`
6.  上流を設定: `git branch --set-upstream-to=origin/main main`

手動でのプルをテスト: `git pull origin main`。あなたの出力のように動作するはずです。

### ステップ 2: 自動プール用のスクリプトを作成する
プルを安全に処理する（フェッチし、競合をチェックし、クリーンな場合にプルする）シンプルなシェルスクリプトを作成します。

1.  リポジトリのルートに `auto-pull.sh` を作成:
    ```bash:disable-run
    #!/bin/bash
    cd "$(dirname "$0")"  # リポジトリディレクトリに変更
    git fetch origin
    if git diff HEAD origin/main --quiet; then
        git pull origin main
        echo "Auto-pull completed: $(date)"
    else
        echo "Warning: Local changes detected. Skipping pull. Resolve manually: $(date)"
        # オプション: メールや通知を送信（下記参照）
    fi
    ```

2.  実行可能にする: `chmod +x auto-pull.sh`

このスクリプトは:
-   マージせずに更新をフェッチします。
-   ローカルブランチがクリーンか（未コミットの変更がないか）をチェックします。
-   安全な場合のみプルし、そうでない場合は警告します。

### ステップ 3: Cron でスケジュールする
Cron はジョブを定期的に実行します。これを5分ごとに実行します（必要に応じて調整、例えば毎時）。

1.  crontab エディタを開く: `crontab -e` (プロンプトが表示されたら nano を使用: `nano ~/.crontab`)。

2.  末尾にこの行を追加（5分ごと）:
    ```
    */5 * * * * /path/to/blog-source/auto-pull.sh >> /path/to/blog-source/pull-log.txt 2>&1
    ```
    -   `/path/to/blog-source` を実際のリポジトリパスに置き換えてください（例: `~/blog-source`）。
    -   `>> pull-log.txt` は出力をファイルに記録し、デバッグを容易にします。

3.  保存して終了（nano では Ctrl+O, Enter, Ctrl+X）。
4.  確認: `crontab -l`（あなたの行が表示されるはずです）。
5.  テスト: 5分待つか、一時的に `* * * * *`（毎分）を追加するために `crontab -e` を再度実行し、後で元に戻します。

Cron はあなたのユーザーとして実行するため、GitHub 認証用のあなたの SSH キーを尊重します（あなたのプル出力のように）。

### オプションの拡張
-   **競合/通知の処理**: スクリプトが問題を検出した場合、通知を追加します。`auto-pull.sh` を編集して以下を追加:
    ```bash
    # 警告の場合、macOS 通知を送信
    osascript -e 'display notification "Git pull skipped due to local changes" with title "Blog Repo Sync"'
    ```
-   **プッシュ時に実行（1台目のノートパソコンから）**: より「プッシュ的」な同期を行うには、1台目のノートパソコンで GitHub Actions を使用します。`.github/workflows/sync.yml` を作成:
    ```yaml
    name: Auto Sync
    on: [push]
    jobs:
      sync:
        runs-on: ubuntu-latest
        steps:
          - uses: actions/checkout@v4
          - name: Notify (e.g., via webhook to second laptop)
            run: curl -X POST https://your-second-laptop-webhook-endpoint  # 2台目のノートパソコンでシンプルなサーバーをセットアップ
    ```
    しかし、これには2台目のマシンにリスナーが必要です（例: ngrok + 小さな Flask アプリ）。ほとんどのケースでは過剰です。
-   **頻度のトレードオフ**: 5分ごとはブログリポジトリには問題ありません。リアルタイムを求める場合は、ターミナルで `watch` ツールを検討してください (`watch -n 300 git pull`) が、cron は手間がかかりません。
-   **プロキシに関する注意**: あなたの出力は HTTP/HTTPS プロキシを示しています。cron はそれらを継承するため、プルはそのまま動作するはずです。

これで、1台目のノートパソコンから (`git push origin main`) プッシュすると、2台目は5分ごとに自動的に同期されます。履歴は `pull-log.txt` を確認してください。

cron で認証/プロキシの問題が発生した場合は、スクリプトに `export HTTP_PROXY=http://127.0.0.1:7890` などを追加してください。もう一方のノートパソコンが Windows の場合は、代わりにタスク スケジューラを使用してください。