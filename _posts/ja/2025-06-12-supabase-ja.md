---
audio: false
generated: true
lang: ja
layout: post
title: Supabaseを使用したパンチカードリマインダー
translated: true
type: note
---

GitHub Actionsの既存のワークフローとPythonスクリプトを修正し、水曜日から金曜日までのパンチカードリマインダーを実装します。リマインダーは12時から15時（出勤打刻）と18時から21時（退勤打刻）のSGT時間帯に5分ごとに送信され、Telegram経由で「punch」メッセージを受信すると停止します。冗長なリマインダーを防ぐため、Supabaseを使用して打刻状態を追跡します。

以下に完全な手順とコードを示します：

---

### GitHub Actionsワークフロー
ワークフローは、SGT（UTC+8）の指定時間帯に5分ごとに実行する必要があります：
- 出勤打刻：12時〜15時 SGT = 4時〜7時 UTC
- 退勤打刻：18時〜21時 SGT = 10時〜13時 UTC
- 対象日：水曜日〜金曜日（cron構文では3-5）

これらの時間を組み合わせた単一のcronスケジュールを使用し、アクションの判断はスクリプトに任せます。

```yaml
name: Punch Card Reminders

on:
  schedule:
    # 毎週水曜日から金曜日、4時〜7時および10時〜13時UTCに5分ごとに実行
    # 4時〜7時UTC = 12時〜15時SGT、10時〜13時UTC = 18時〜21時SGT
    - cron: '*/5 4-7,10-13 * * 3-5'

  workflow_dispatch:
    inputs:
      job_name:
        description: '実行するジョブ（punch_reminder, send_message）'
        required: true
        default: 'punch_reminder'
      message:
        description: 'send_messageジョブ用のカスタムメッセージ（オプション）'
        required: false
        default: 'これはGitHub Actionsからの手動トリガーテストメッセージです。'

  push:
    branches: ["main"]
    paths:
      - 'scripts/release/location_bot.py'
      - '.github/workflows/location.yml'

concurrency:
  group: 'punch_reminder'
  cancel-in-progress: false

jobs:
  punch_reminder_job:
    runs-on: ubuntu-latest
    environment: github-pages
    env:
      TELEGRAM_LOCATION_BOT_API_KEY: ${{ secrets.TELEGRAM_LOCATION_BOT_API_KEY }}
      SUPABASE_URL: ${{ secrets.SUPABASE_URL }}
      SUPABASE_KEY: ${{ secrets.SUPABASE_KEY }}

    steps:
    - name: リポジトリをチェックアウト
      uses: actions/checkout@v4
      with:
        fetch-depth: 5

    - name: Python 3.13.2をセットアップ
      uses: actions/setup-python@v4
      with:
        python-version: "3.13.2"

    - name: 依存関係をインストール
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.simple.txt

    - name: パンチリマインダースクリプトを実行（スケジュール）
      run: python scripts/release/location_bot.py --job punch_reminder
      if: github.event_name == 'schedule'

    - name: パンチリマインダースクリプトを実行（手動トリガー）
      run: python scripts/release/location_bot.py --job punch_reminder
      if: github.event_name == 'workflow_dispatch' && github.event.inputs.job_name == 'punch_reminder'

    - name: カスタムメッセージ用Telegramスクリプトを実行（手動トリガー）
      run: python scripts/release/location_bot.py --job send_message --message "${{ github.event.inputs.message }}"
      if: github.event_name == 'workflow_dispatch' && github.event.inputs.job_name == 'send_message'

    - name: mainブランチへのプッシュ時に通知
      run: python scripts/release/location_bot.py --job send_message --message "パンチリマインダーボットのコード変更がmainブランチにプッシュされました。"
      if: github.event_name == 'push'
```

---

### Pythonスクリプト
スクリプトは以下を行います：
- 現在のSGT時間をチェックし、出勤打刻または退勤打刻の時間帯かを判断
- Supabaseを使用して打刻状態を追跡
- 「punch」メッセージのTelegram更新を取得
- 打刻が記録されていない場合にリマインダーを送信

`requirements.simple.txt`を以下の内容に更新してください：
```
requests
supabase
pytz
```

修正したスクリプトは以下の通りです：

```python
import os
import requests
import datetime
import pytz
from supabase import create_client
import argparse

# 環境変数を読み込み
TELEGRAM_LOCATION_BOT_API_KEY = os.environ.get("TELEGRAM_LOCATION_BOT_API_KEY")
TELEGRAM_CHAT_ID = "610574272"  # あなたのチャットID

def send_telegram_message(bot_token, chat_id, message):
    """Telegram Bot APIを使用してTelegramチャットにメッセージを送信します。"""
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown"
    }
    response = requests.post(url, params=params)
    if response.status_code != 200:
        print(f"Telegramメッセージ送信エラー: {response.status_code} - {response.text}")

def send_reminder(action):
    """打刻リマインダーメッセージを送信します。"""
    message = f"⏰ *リマインダー:* このボットに「punch」と送信して{action.replace('_', ' ')}を打刻してください。"
    send_telegram_message(TELEGRAM_LOCATION_BOT_API_KEY, TELEGRAM_CHAT_ID, message)

def main():
    parser = argparse.ArgumentParser(description="Telegramパンチリマインダーボット")
    parser.add_argument('--job', choices=['punch_reminder', 'send_message'], required=True, help="実行するジョブ")
    parser.add_argument('--message', type=str, help="'send_message'ジョブ用の送信メッセージ")
    args = parser.parse_args()

    if args.job == 'send_message':
        if TELEGRAM_LOCATION_BOT_API_KEY and TELEGRAM_CHAT_ID:
            message = args.message if args.message else "ボットからのデフォルトテストメッセージ！"
            send_telegram_message(TELEGRAM_LOCATION_BOT_API_KEY, TELEGRAM_CHAT_ID, message)
            print(f"メッセージを送信: {message}")
        else:
            print("TELEGRAM_LOCATION_BOT_API_KEYとTELEGRAM_CHAT_IDが設定されていません。")
        return

    elif args.job == 'punch_reminder':
        # Supabaseを初期化
        supabase = create_client(os.environ['SUPABASE_URL'], os.environ['SUPABASE_KEY'])

        # SGT（UTC+8）の現在時刻を取得
        sgt = pytz.timezone('Asia/Singapore')
        now_utc = datetime.datetime.utcnow()
        now_sgt = now_utc.replace(tzinfo=pytz.utc).astimezone(sgt)
        today_sgt = now_sgt.date()

        # 時間帯を定義
        punch_in_start = datetime.time(12, 0)  # 12時 SGT
        punch_in_end = datetime.time(15, 0)    # 15時 SGT
        punch_out_start = datetime.time(18, 0) # 18時 SGT
        punch_out_end = datetime.time(21, 0)   # 21時 SGT

        current_time = now_sgt.time()

        # 現在の時間帯を判断
        if punch_in_start <= current_time <= punch_in_end:
            window = 'punch_in'
        elif punch_out_start <= current_time <= punch_out_end:
            window = 'punch_out'
        else:
            window = None

        if not window:
            print("打刻リマインダー時間帯外です。")
            return

        # 今日の打刻記録を取得
        response = supabase.table('punch_records').select('*').eq('date', str(today_sgt)).execute()
        punch_record = response.data[0] if response.data else None

        # 打刻が既に行われているか確認
        if window == 'punch_in' and punch_record and punch_record['punch_in_time']:
            print("本日は既に出勤打刻済みです。")
            return
        if window == 'punch_out' and punch_record and punch_record['punch_out_time']:
            print("本日は既に退勤打刻済みです。")
            return

        # 最後に処理したTelegram更新IDを取得
        state_response = supabase.table('telegram_state').select('last_update_id').eq('id', 1).execute()
        last_update_id = state_response.data[0]['last_update_id'] if state_response.data else 0

        # 新しいTelegram更新を取得
        url = f"https://api.telegram.org/bot{TELEGRAM_LOCATION_BOT_API_KEY}/getUpdates"
        params = {"offset": last_update_id + 1, "timeout": 0}
        response = requests.get(url, params=params)
        updates = response.json().get('result', [])

        max_update_id = last_update_id
        for update in updates:
            if update['update_id'] > max_update_id:
                max_update_id = update['update_id']
            if ('message' in update and 
                update['message'].get('text', '').lower() == 'punch' and 
                str(update['message']['chat']['id']) == TELEGRAM_CHAT_ID):
                # 「punch」メッセージを処理
                if window == 'punch_in':
                    if not punch_record:
                        supabase.table('punch_records').insert({
                            'date': str(today_sgt),
                            'punch_in_time': now_utc.isoformat()
                        }).execute()
                    else:
                        supabase.table('punch_records').update({
                            'punch_in_time': now_utc.isoformat()
                        }).eq('date', str(today_sgt)).execute()
                elif window == 'punch_out':
                    if not punch_record:
                        supabase.table('punch_records').insert({
                            'date': str(today_sgt),
                            'punch_out_time': now_utc.isoformat()
                        }).execute()
                    else:
                        supabase.table('punch_records').update({
                            'punch_out_time': now_utc.isoformat()
                        }).eq('date', str(today_sgt)).execute()

        # last_update_idを更新
        if max_update_id > last_update_id:
            supabase.table('telegram_state').update({
                'last_update_id': max_update_id
            }).eq('id', 1).execute()

        # 最新の状態を確認するため打刻記録を再取得
        response = supabase.table('punch_records').select('*').eq('date', str(today_sgt)).execute()
        punch_record = response.data[0] if response.data else None

        # 打刻が記録されていない場合にリマインダーを送信
        if window == 'punch_in' and (not punch_record or not punch_record['punch_in_time']):
            send_reminder('punch_in')
        elif window == 'punch_out' and (not punch_record or not punch_record['punch_out_time']):
            send_reminder('punch_out')

if __name__ == '__main__':
    main()
```

---

### Supabaseセットアップ
打刻状態とTelegram更新を管理するため、Supabaseに2つのテーブルを作成します。

#### SQL手順
Supabase SQLエディタで以下のSQLコマンドを実行してください：

```sql
-- 日次打刻記録を保存するテーブル
CREATE TABLE punch_records (
    date DATE PRIMARY KEY,
    punch_in_time TIMESTAMP,
    punch_out_time TIMESTAMP
);

-- Telegram状態を管理するテーブル
CREATE TABLE telegram_state (
    id INTEGER PRIMARY KEY,
    last_update_id BIGINT NOT NULL DEFAULT 0
);

-- 単一行でtelegram_stateを初期化
INSERT INTO telegram_state (id, last_update_id) VALUES (1, 0);
```

#### 実行手順
1. Supabaseダッシュボードにログインします。
2. **SQL Editor**に移動します。
3. 上記のSQLコードを貼り付けて実行し、テーブルを作成および初期化します。

---

### 環境変数
GitHubリポジトリの**Settings > Secrets and variables > Actions > Secrets**で以下のシークレットが設定されていることを確認してください：
- `TELEGRAM_LOCATION_BOT_API_KEY`: あなたのTelegramボットトークン。
- `SUPABASE_URL`: あなたのSupabaseプロジェクトURL（例：`https://xyz.supabase.co`）。
- `SUPABASE_KEY`: あなたのSupabase anonキー（**Settings > API**にあります）。

---

### 動作の仕組み
1. **スケジュール**: ワークフローは、水曜日から金曜日の12時〜15時および18時〜21時SGT（UTCに調整）に5分ごとに実行されます。
2. **時間チェック**: スクリプトは現在のSGT時間をチェックし、出勤打刻または退勤打刻の時間帯かを判断します。
3. **状態管理**:
   - 今日の打刻について`punch_records`をチェックします。
   - 既に打刻済みの場合（例：12時〜15時に`punch_in_time`が設定されている）、リマインダーは送信されません。
4. **Telegram更新**:
   - 最後に処理した`update_id`以降の更新を取得します。
   - 「punch」メッセージが見つかった場合、出勤打刻または退勤打刻の現在時刻で`punch_records`を更新します。
   - 最新の`update_id`で`telegram_state`を更新します。
5. **リマインダー**: 現在の時間帯で打刻が記録されていない場合、5分ごとにリマインダーを送信します。

---

### テスト
- **手動トリガー**: `workflow_dispatch`を`job_name: punch_reminder`で使用して手動テストします。
- **Telegram**: 時間帯中にボットに「punch」を送信して、そのセッションのリマインダーを停止します。
- **Supabase**: `punch_records`テーブルをチェックして、打刻時刻が正しく記録されていることを確認します。

このセットアップは、位置情報ベースのロジックを時間ベースの打刻リマインダーに置き換え、GitHub Actionsの制約内で永続的な状態管理をSupabaseに委ねます。