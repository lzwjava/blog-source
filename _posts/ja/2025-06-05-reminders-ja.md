---
audio: true
generated: false
image: false
lang: ja
layout: post
title: Telegramで効率化するリマインダー
translated: true
type: post
---

このプロジェクトでは、GitHub ActionsとTelegramボットを活用して、日々のタスクや月次の業務を管理する自動リマインダーシステムを構築しました。cronスケジュールを利用することで、WeComでの打刻、タイムシート提出、給与確認といった仕事関連のタスクから、実家訪問、JD.comでの買い物、パートナーとのテレビ鑑賞といったプライベートな予定まで、様々なリマインダーを設定しています。PythonスクリプトでTelegramのBot APIを介してメッセージを送信し、GitHub Secretsに環境変数を安全に保管しています。このシステムにより、重要な締切や個人的な約束を見逃すことなく、テクノロジーと日常生活を融合させて最大限の効率を実現しています。

```yaml
name: リマインダー

on:
  schedule:
    # 毎週水曜日から金曜日、北京時間午後12時から午後8時まで2時間ごとに実行（UTC+8）
    - cron: '0 4,6,8,10,12 * * 3-5'
    # 毎月27日午後12時北京時間（UTC+8）に実行
    - cron: '0 4 27 * *'
    # 毎月30日午後2時北京時間（UTC+8）に実行
    - cron: '0 6 30 * *'
    # 毎日午前1時北京時間（前日UTC午後5時）に実行
    - cron: '0 17 * * *'
    # 毎日午前11時北京時間（UTC午前3時）に実行
    - cron: '0 3 * * *'
    # 実家訪問リマインダー：火曜～木曜 北京時間午後9時（UTC午後1時）
    - cron: '0 13 * * 2-4'
    # 自宅訪問リマインダー：日曜、月曜、金曜、土曜 北京時間午後9時（UTC午後1時）
    - cron: '0 13 * * 0,1,5,6'
    # JD.comで新鮮食材を購入：水曜日 北京時間午後9時（UTC午後1時）
    - cron: '0 13 * * 3'
    # JD.comで速達食品を購入：金曜日 北京時間午後9時（UTC午後1時）
    - cron: '0 13 * * 5'
    # 短期大学試験リマインダー：3月、4月、9月、10月の毎週月曜日 北京時間午後1時（UTC午前5時）
    - cron: '0 5 * 3,4,9,10 1'
    # 週次タイムシート提出リマインダー：毎週金曜日 台北時間午後5時（UTC午前9時）
    - cron: '0 9 * * 5'
    # ベンダータイムシート提出リマインダー：毎月25日 台北時間午前0時（前日UTC午後4時）
    - cron: '0 16 25 * *'
    # 住宅ローン支援依頼リマインダー：毎月16日 台北時間午後9時（UTC午後1時）
    - cron: '0 13 16 * *'
    # パートナーとテレビ鑑賞リマインダー：毎週金曜、土曜、日曜 台北時間午後10時（UTC午後2時）
    - cron: '0 14 * * 5,6,0'
    # 駐車許可証剥がしリマインダー：水曜～金曜 北京時間午前2時（UTC午後6時）
    - cron: '0 18 * * 3,4,5'
  workflow_dispatch:  # 手動トリガーを許可

concurrency:
  group: 'reminders'
  cancel-in-progress: false

jobs:
  send-reminders:
    runs-on: ubuntu-latest
    environment: github-pages
    env:
      TELEGRAM_BOT2_API_KEY: ${{ secrets.TELEGRAM_BOT2_API_KEY }}

    steps:
      - name: リポジトリをチェックアウト
        uses: actions/checkout@v4
        with:
          fetch-depth: 5

      - name: Python 3.10.xをセットアップ
        uses: actions/setup-python@v4
        with:
          python-version: "3.10.x"

      - name: 依存関係をインストール
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.simple.txt

      - name: WeCom打刻リマインダー用Telegramスクリプト実行
        run: python scripts/release/reminders_bot.py --job send_message --message "WeComで打刻してください"
        if: github.event.schedule == '0 4,6,8,10,12 * * 3-5'

      - name: 住宅ローン控除リマインダー用Telegramスクリプト実行
        run: python scripts/release/reminders_bot.py --job send_message --message "住宅ローン控除の準備をしてください"
        if: github.event.schedule == '0 4 27 * *'

      - name: 給与確認リマインダー用Telegramスクリプト実行
        run: python scripts/release/reminders_bot.py --job send_message --message "給与を確認してください"
        if: github.event.schedule == '0 6 30 * *'

      - name: 就寝リマインダー用Telegramスクリプト実行
        run: python scripts/release/reminders_bot.py --job send_message --message "寝る時間です！"
        if: github.event.schedule == '0 17 * * *'

      - name: 起床リマインダー用Telegramスクリプト実行
        run: python scripts/release/reminders_bot.py --job send_message --message "起きる時間です！"
        if: github.event.schedule == '0 3 * * *'

      - name: 実家訪問リマインダー用Telegramスクリプト実行
        run: python scripts/release/reminders_bot.py --job send_message --message "明日は実家に行きましょう！"
        if: github.event.schedule == '0 13 * * 2-4'

      - name: 自宅訪問リマインダー用Telegramスクリプト実行
        run: python scripts/release/reminders_bot.py --job send_message --message "明日は自宅に行きましょう！"
        if: github.event.schedule == '0 13 * * 0,1,5,6'

      - name: JD.com新鮮食材購入リマインダー用Telegramスクリプト実行
        run: python scripts/release/reminders_bot.py --job send_message --message "JD.comで産直新鮮食材を購入しましょう！"
        if: github.event.schedule == '0 13 * * 3'

      - name: JD.com速達食品購入リマインダー用Telegramスクリプト実行
        run: python scripts/release/reminders_bot.py --job send_message --message "JD.comで速達食品を購入しましょう！"
        if: github.event.schedule == '0 13 * * 5'

      - name: 短期大学試験登録リマインダー用Telegramスクリプト実行
        run: python scripts/release/reminders_bot.py --job send_message --message "短期大学試験に登録してください"
        if: github.event.schedule == '0 5 * 3,4,9,10 1'

      - name: 週次タイムシート提出リマインダー用Telegramスクリプト実行
        run: python scripts/release/reminders_bot.py --job send_message --message "週次タイムシートを提出してください"
        if: github.event.schedule == '0 9 * * 5'

      - name: ベンダータイムシート提出リマインダー用Telegramスクリプト実行
        run: python scripts/release/reminders_bot.py --job send_message --message "ベンダータイムシートを提出してください"
        if: github.event.schedule == '0 16 25 * *'

      - name: 住宅ローン支援依頼リマインダー用Telegramスクリプト実行
        run: python scripts/release/reminders_bot.py --job send_message --message "家族に住宅ローンの支援を依頼してください"
        if: github.event.schedule == '0 13 16 * *'

      - name: パートナーとテレビ鑑賞リマインダー用Telegramスクリプト実行
        run: python scripts/release/reminders_bot.py --job send_message --message "パートナーとテレビを見る時間です！"
        if: github.event.schedule == '0 14 * * 5,6,0'

      - name: 駐車許可証剥がしリマインダー用Telegramスクリプト実行
        run: python scripts/release/reminders_bot.py --job send_message --message "車窓から駐車許可証ステッカーを剥がしてください"
        if: github.event.schedule == '0 18 * * 3,4,5'

      - name: テストメッセージ用Telegramスクリプト実行
        run: python scripts/release/reminders_bot.py --job send_message --message "これはGitHub Actionsからのテストメッセージです"
        if: github.event_name == 'workflow_dispatch'
```

```python
import os
import requests
from dotenv import load_dotenv
import json
import argparse

load_dotenv()

TELEGRAM_BOT2_API_KEY = os.environ.get("TELEGRAM_BOT2_API_KEY")
TELEGRAM_CHAT_ID = "610574272"

def send_telegram_message(bot_token, chat_id, message):
    """Telegram Bot APIを使用してチャットにメッセージを送信します"""
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(url, params=params)
    if response.status_code != 200:
        print(f"Telegramメッセージ送信エラー: {response.status_code} - {response.text}")

def get_chat_id(bot_token):
    """ボットに送信された最後のメッセージのチャットIDを取得します"""
    url = f"https://api.telegram.org/bot{bot_token}/getUpdates"
    response = requests.get(url)
    if response.status_code == 200:
        updates = response.json()
        print(json.dumps(updates, indent=4))
        if updates['result']:
            chat_id = updates['result'][-1]['message']['chat']['id']
            return chat_id
    return None

def send_reminder(message):
    """リマインダーメッセージをTelegramに送信します"""
    if TELEGRAM_BOT2_API_KEY and TELEGRAM_CHAT_ID:
        send_telegram_message(TELEGRAM_BOT2_API_KEY, TELEGRAM_CHAT_ID, f"リマインダー: {message}")
    else:
        print("TELEGRAM_BOT2_API_KEYとTELEGRAM_CHAT_IDが設定されていません")

def main():
    parser = argparse.ArgumentParser(description="Telegramボットスクリプト")
    parser.add_argument('--job', choices=['get_chat_id', 'send_message'], required=True, help="実行するジョブ")
    parser.add_argument('--message', help="送信するカスタムメッセージ", default=None)
    args = parser.parse_args()

    if args.job == 'get_chat_id':
        bot_token = TELEGRAM_BOT2_API_KEY
        chat_id = get_chat_id(bot_token)
        if chat_id:
            print(f"チャットID: {chat_id}")
        else:
            print("チャットIDを取得できませんでした")

    elif args.job == 'send_message':
        if args.message:
            send_reminder(args.message)
        else:
            print("send_messageジョブにメッセージが指定されていません")
            
if __name__ == '__main__':
    main()
```