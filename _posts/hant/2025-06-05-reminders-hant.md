---
audio: true
generated: false
image: false
lang: hant
layout: post
title: 透過Telegram簡化提醒事項
translated: true
---

在這個項目中，我建立了一個自動提醒系統，利用GitHub Actions和Telegram機器人來追蹤我的每日及每月任務。通過設定cron排程，我配置了工作相關任務的提醒，例如在企業微信打卡、提交工時表、查核薪資，以及個人任務如探訪家人、在京東購物，甚至與伴侶一起看電視。該系統使用Python腳本通過Telegram的Bot API發送訊息，並將環境變數安全地儲存在GitHub Secrets中。這樣的設置確保我不會錯過任何重要期限或個人承諾，將科技與日常生活完美結合，以達到最高效率。

```yaml
name: 提醒系統

on:
  schedule:
    # 每週三至週五，北京時間中午12點至晚上8點，每兩小時執行一次。
    - cron: '0 4,6,8,10,12 * * 3-5'
    # 每月27日中午12點（北京時間）執行。
    - cron: '0 4 27 * *'
    # 每月30日下午2點（北京時間）執行。
    - cron: '0 6 30 * *'
    # 每日凌晨1點（北京時間）執行。
    - cron: '0 17 * * *'
    # 每日上午11點（北京時間）執行。
    - cron: '0 3 * * *'
    # 提醒隔日前往父母家：每週二、三、四晚上9點（北京時間）。
    - cron: '0 13 * * 2-4'
    # 提醒隔日回自己家：每週日、一、五、六晚上9點（北京時間）。
    - cron: '0 13 * * 0,1,5,6'
    # 提醒在京東購買生鮮直送：每週三晚上9點（北京時間）。
    - cron: '0 13 * * 3'
    # 提醒在京東購買速食：每週五晚上9點（北京時間）。
    - cron: '0 13 * * 5'
    # 提醒副學士學位考試報名：每年3、4、9、10月的每週一中午1點（北京時間）。
    - cron: '0 5 * 3,4,9,10 1'
    # 提醒提交每週工時表：每週五台北時間下午5點。
    - cron: '0 9 * * 5'
    # 提醒提交供應商工時表：每月25日午夜12點（台北時間）。
    - cron: '0 16 25 * *'
    # 提醒家人支援房貸還款：每月16日晚上9點（台北時間）。
    - cron: '0 13 16 * *'
    # 提醒與伴侶看電視：每週五、六、日晚上10點（台北時間）。
    - cron: '0 14 * * 5,6,0'
    # 提醒移除停車許可貼紙：每週三、四、五凌晨2點（北京時間）。
    - cron: '0 18 * * 3,4,5'
  workflow_dispatch:  # 允許手動觸發

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
      - name: 檢出存儲庫
        uses: actions/checkout@v4
        with:
          fetch-depth: 5

      - name: 設置Python 3.10.x
        uses: actions/setup-python@v4
        with:
          python-version: "3.10.x"

      - name: 安裝依賴
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.simple.txt

      - name: 執行Telegram腳本發送每日打卡提醒
        run: python scripts/release/reminders_bot.py --job send_message --message "請在企業微信打卡"
        if: github.event.schedule == '0 4,6,8,10,12 * * 3-5'

      - name: 執行Telegram腳本發送每月房貸提醒
        run: python scripts/release/reminders_bot.py --job send_message --message "準備房貸扣款"
        if: github.event.schedule == '0 4 27 * *'

      - name: 執行Telegram腳本發送每月薪資查核提醒
        run: python scripts/release/reminders_bot.py --job send_message --message "查核薪資"
        if: github.event.schedule == '0 6 30 * *'

      - name: 執行Telegram腳本發送睡眠提醒
        run: python scripts/release/reminders_bot.py --job send_message --message "該睡覺了！"
        if: github.event.schedule == '0 17 * * *'

      - name: 執行Telegram腳本發送起床提醒
        run: python scripts/release/reminders_bot.py --job send_message --message "該起床了！"
        if: github.event.schedule == '0 3 * * *'

      - name: 執行Telegram腳本發送前往父母家提醒
        run: python scripts/release/reminders_bot.py --job send_message --message "明天要去父母家！"
        if: github.event.schedule == '0 13 * * 2-4'

      - name: 執行Telegram腳本發送回自己家提醒
        run: python scripts/release/reminders_bot.py --job send_message --message "明天回自己家！"
        if: github.event.schedule == '0 13 * * 0,1,5,6'

      - name: 執行Telegram腳本發送京東生鮮購買提醒
        run: python scripts/release/reminders_bot.py --job send_message --message "記得在京東購買生鮮直送！"
        if: github.event.schedule == '0 13 * * 3'

      - name: 執行Telegram腳本發送京東速食購買提醒
        run: python scripts/release/reminders_bot.py --job send_message --message "記得在京東購買速食！"
        if: github.event.schedule == '0 13 * * 5'

      - name: 執行Telegram腳本發送副學士學位考試提醒
        run: python scripts/release/reminders_bot.py --job send_message --message "記得報名副學士學位考試"
        if: github.event.schedule == '0 5 * 3,4,9,10 1'

      - name: 執行Telegram腳本發送每週工時表提交提醒
        run: python scripts/release/reminders_bot.py --job send_message --message "提交每週工時表"
        if: github.event.schedule == '0 9 * * 5'

      - name: 執行Telegram腳本發送供應商工時表提交提醒
        run: python scripts/release/reminders_bot.py --job send_message --message "提交供應商工時表"
        if: github.event.schedule == '0 16 25 * *'

      - name: 執行Telegram腳本發送家人支援房貸提醒
        run: python scripts/release/reminders_bot.py --job send_message --message "請家人支援房貸還款"
        if: github.event.schedule == '0 13 16 * *'

      - name: 執行Telegram腳本發送與伴侶看電視提醒
        run: python scripts/release/reminders_bot.py --job send_message --message "該和伴侶一起看電視了！"
        if: github.event.schedule == '0 14 * * 5,6,0'

      - name: 執行Telegram腳本發送移除停車許可貼紙提醒
        run: python scripts/release/reminders_bot.py --job send_message --message "記得移除車窗上的停車許可貼紙"
        if: github.event.schedule == '0 18 * * 3,4,5'

      - name: 執行Telegram腳本發送測試訊息
        run: python scripts/release/reminders_bot.py --job send_message --message "這是來自GitHub Actions的測試訊息。"
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
    """使用Telegram Bot API發送訊息至指定聊天室。"""
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(url, params=params)
    if response.status_code != 200:
        print(f"發送Telegram訊息時出錯：{response.status_code} - {response.text}")

def get_chat_id(bot_token):
    """獲取最後發送給機器人的訊息的聊天室ID。"""
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
    """發送提醒訊息至Telegram。"""
    if TELEGRAM_BOT2_API_KEY and TELEGRAM_CHAT_ID:
        send_telegram_message(TELEGRAM_BOT2_API_KEY, TELEGRAM_CHAT_ID, f"提醒：{message}")
    else:
        print("未設定TELEGRAM_BOT2_API_KEY和TELEGRAM_CHAT_ID。")

def main():
    parser = argparse.ArgumentParser(description="Telegram機器人腳本")
    parser.add_argument('--job', choices=['get_chat_id', 'send_message'], required=True, help="執行任務")
    parser.add_argument('--message', help="自訂發送訊息", default=None)
    args = parser.parse_args()

    if args.job == 'get_chat_id':
        bot_token = TELEGRAM_BOT2_API_KEY
        chat_id = get_chat_id(bot_token)
        if chat_id:
            print(f"聊天室ID：{chat_id}")
        else:
            print("無法獲取聊天室ID。")

    elif args.job == 'send_message':
        if args.message:
            send_reminder(args.message)
        else:
            print("未提供發送訊息的內容。")
            
if __name__ == '__main__':
    main()
```