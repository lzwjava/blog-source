---
audio: false
generated: false
image: false
lang: hant
layout: post
title: 用Mistral打造習慣養成機器人
translated: true
type: post
---

在這篇網誌文章中，我們探討如何利用Python和GitHub Actions創建一個習慣提醒機器人。這個機器人透過Telegram API發送自動化提醒訊息，並整合Mistral AI生成情境相關的提示。透過GitHub Actions排程任務，機器人能定時發送通知，鼓勵持續養成習慣。我們將逐步介紹從環境設定、腳本編寫到部署的完整流程，為自動化習慣追蹤系統提供實用指南。

## 代碼

```python
import os
import requests
import argparse
import re
import datetime
from dotenv import load_dotenv
import random

# 從.env檔案加載環境變量
load_dotenv()

# 環境變量
TELEGRAM_HABIT_BOT_API_KEY = os.environ.get("TELEGRAM_HABIT_BOT_API_KEY")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")
MISTRAL_API_KEY = os.environ.get("MISTRAL_API_KEY")

# Telegram訊息長度限制
TELEGRAM_MAX_LENGTH = 4096

def send_telegram_message(bot_token, chat_id, message):
    """使用Telegram Bot API發送訊息到指定聊天室"""
    if not bot_token or not chat_id:
        print("錯誤：TELEGRAM_HABIT_BOT_API_KEY或TELEGRAM_CHAT_ID未設定")
        return False
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    # 移除Markdown星號和URL以確保Telegram兼容性
    message_no_stars = message.replace('*', '')
    url_pattern = re.compile(r'(https?://[^\s]+)')
    message_no_links = url_pattern.sub('', message_no_stars)
    # 若訊息超過Telegram長度限制則進行分割
    messages = []
    msg = message_no_links
    while len(msg) > TELEGRAM_MAX_LENGTH:
        split_idx = msg.rfind('\n', 0, TELEGRAM_MAX_LENGTH)
        if split_idx == -1 or split_idx < TELEGRAM_MAX_LENGTH // 2:
            split_idx = TELEGRAM_MAX_LENGTH
        messages.append(msg[:split_idx])
        msg = msg[split_idx:]
    messages.append(msg)
    success = True
    for part in messages:
        params = {
            "chat_id": chat_id,
            "text": part,
            "parse_mode": "Markdown"
        }
        try:
            response = requests.post(url, params=params)
            response.raise_for_status()
            print(f"成功發送Telegram訊息部分（{len(part)}字元）")
        except requests.exceptions.RequestException as e:
            print(f"發送Telegram訊息時出錯：{e}")
            success = False
    return success


def call_mistral_api(prompt, model="mistral-large-latest"):
    """調用Mistral API生成回應"""
    if not MISTRAL_API_KEY:
        print("錯誤：未設定MISTRAL_API_KEY環境變量")
        return None
    url = "https://api.mistral.ai/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {MISTRAL_API_KEY}"
    }
    data = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.7,  # 調整溫度參數控制創造性
        "max_tokens": 300  # 限制回應長度
    }
    try:
        print(f"使用模型調用Mistral API：{model}")
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        response_json = response.json()
        if response_json.get('choices'):
            content = response_json['choices'][0]['message']['content']
            print(f"Mistral API內容：{content}")
            return content
        print(f"Mistral API錯誤：無效的回應格式：{response_json}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Mistral API錯誤：{e}")
        return None

def generate_copilot_message():
    """透過Mistral API生成鼓勵使用Copilot的技術提示句子"""
    prompt = (
        f"為後端工程師生成一個獨特且具體的技術提示句子"
        "隨機選擇以下一項技術：Java、Spring Boot、Control-M、IBM WebSphere、Maven、多線程、Nexus、Windows、JVM、Service-NOW、Python、AI或DevOps、Linux。算法與銀行業"
        "格式為'卡在[具體挑戰]？問問Copilot！'或'遇到[任務]困難？找Copilot幫忙！'"
        "確保挑戰多樣化（例如配置、調試、優化）。"
        "保持句子在300字元以內，避免使用Markdown或URL，僅輸出句子。"
    )
    message = call_mistral_api(prompt)
    if message:
        return message.strip()[:300]
    return "卡在設定Control-M訂單日期？問問Copilot！"

def main():
    parser = argparse.ArgumentParser(description="Telegram習慣提醒機器人")
    parser.add_argument("--job", choices=["send_reminder", "send_message"], required=True, help="執行任務")
    parser.add_argument("--message", type=str, help="'send_message'任務要發送的訊息")
    args = parser.parse_args()

    if args.job == "send_reminder":
        if TELEGRAM_HABIT_BOT_API_KEY and TELEGRAM_CHAT_ID:
            message = generate_copilot_message()
            send_telegram_message(TELEGRAM_HABIT_BOT_API_KEY, TELEGRAM_CHAT_ID, message)
        else:
            print("錯誤：TELEGRAM_HABIT_BOT_API_KEY或TELEGRAM_CHAT_ID未設定")
    elif args.job == "send_message":
        if TELEGRAM_HABIT_BOT_API_KEY and TELEGRAM_CHAT_ID:
            message = args.message if args.message else "來自機器人的預設測試訊息！"
            send_telegram_message(TELEGRAM_HABIT_BOT_API_KEY, TELEGRAM_CHAT_ID, message)
        else:
            print("錯誤：TELEGRAM_HABIT_BOT_API_KEY或TELEGRAM_CHAT_ID未設定")

if __name__ == "__main__":
    main()
```

## GitHub Action

```yaml
name: 習慣提醒

on:
  schedule:
    # 每10分鐘運行一次（每小時的0、10、20、30、40、50分），UTC時間05:00–13:00，週一至週五
    # 05:00–13:00 UTC = 北京時間13:00–21:00（UTC+8）
    - cron: '0,10,20,30,40,50 5-13 * * 1-5'

  workflow_dispatch:
    # 允許手動觸發測試
    inputs:
      message:
        description: '測試用的自訂訊息（可選）'
        required: false
        default: '來自GitHub Actions的測試訊息'
      job:
        description: '要運行的任務（可選）'
        required: false
        default: 'send_message'

  push:
    branches: ["main"]
    paths:
      - 'scripts/bot/habit_bot.py'
      - '.github/workflows/habit_reminder.yml'

concurrency:
  group: 'habit_reminder'
  cancel-in-progress: false

jobs:
  habit_reminder_job:
    runs-on: ubuntu-latest
    environment: github-pages
    env:
      TELEGRAM_HABIT_BOT_API_KEY: ${{ secrets.TELEGRAM_HABIT_BOT_API_KEY }}
      TELEGRAM_CHAT_ID: ${{ secrets.TELEGRAM_CHAT_ID }}
      MISTRAL_API_KEY: ${{ secrets.MISTRAL_API_KEY }}

    steps:
      - name: 檢出存儲庫
        uses: actions/checkout@v4
        with:
          fetch-depth: 5

      - name: 設置Python 3.13
        uses: actions/setup-python@v4
        with:
          python-version: "3.13"

      - name: 安裝依賴
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: 運行習慣提醒腳本（排程任務）
        run: python scripts/bot/habit_bot.py --job send_reminder
        if: github.event_name == 'schedule'

      - name: 運行習慣提醒腳本（手動觸發）
        run: python scripts/bot/habit_bot.py --job ${{ github.event.inputs.job }} --message "${{ github.event.inputs.message }}"
        if: github.event_name == 'workflow_dispatch'

      - name: 推送至main分支時通知
        run: python scripts/bot/habit_bot.py --job send_message --message "習慣機器人的代碼變更已推送至main分支"
        if: github.event_name == 'push'

```