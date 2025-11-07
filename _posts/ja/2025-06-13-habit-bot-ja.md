---
audio: false
generated: false
image: false
lang: ja
layout: post
title: 習慣ボットをMistralで構築する
translated: true
type: post
---

このブログ記事では、PythonとGitHub Actionsを使用して自動リマインダーを送信するHabit Botの作成について探求します。このボットはTelegram APIをメッセージングに活用し、Mistral AIと統合して文脈に即したプロンプトを生成します。GitHub Actionsでタスクをスケジュールすることで、タイムリーな通知を通じて一貫した習慣を促進します。環境設定からスクリプト作成、デプロイまで、習慣トラッキングシステムを自動化するための実践的なガイドを提供します。

## コード

```python
import os
import requests
import argparse
import re
import datetime
from dotenv import load_dotenv
import random

# .envファイルから環境変数を読み込む
load_dotenv()

# 環境変数
TELEGRAM_HABIT_BOT_API_KEY = os.environ.get("TELEGRAM_HABIT_BOT_API_KEY")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")
MISTRAL_API_KEY = os.environ.get("MISTRAL_API_KEY")

# Telegramメッセージ長制限
TELEGRAM_MAX_LENGTH = 4096

def send_telegram_message(bot_token, chat_id, message):
    """Telegram Bot APIを使用してチャットにメッセージを送信する"""
    if not bot_token or not chat_id:
        print("エラー: TELEGRAM_HABIT_BOT_API_KEYまたはTELEGRAM_CHAT_IDが設定されていません。")
        return False
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    # Telegram互換性を確保するためMarkdownのアスタリスクとURLを削除
    message_no_stars = message.replace('*', '')
    url_pattern = re.compile(r'(https?://[^\s]+)')
    message_no_links = url_pattern.sub('', message_no_stars)
    # Telegramの長さ制限を超える場合メッセージを分割
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
            print(f"Telegramメッセージ部分の送信に成功しました（{len(part)}文字）。")
        except requests.exceptions.RequestException as e:
            print(f"Telegramメッセージ送信エラー: {e}")
            success = False
    return success


def call_mistral_api(prompt, model="mistral-large-latest"):
    """Mistral APIを呼び出してレスポンスを生成する"""
    if not MISTRAL_API_KEY:
        print("エラー: MISTRAL_API_KEY環境変数が設定されていません。")
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
        "temperature": 0.7,  # 創造性を調整する温度
        "max_tokens": 300  # レスポンス長を制限
    }
    try:
        print(f"Mistral APIを呼び出します（モデル: {model}）")
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        response_json = response.json()
        if response_json.get('choices'):
            content = response_json['choices'][0]['message']['content']
            print(f"Mistral APIコンテンツ: {content}")
            return content
        print(f"Mistral APIエラー: {e}")
        return None

def generate_copilot_message():
    """Mistral APIを使用してCopilot利用を促す技術プロンプト文を生成する"""
    prompt = (
        f"バックエンドエンジニア向けに、ユニークで具体的な技術プロンプト文を生成してください"
        "Java、Spring Boot、Control-M、IBM WebSphere、Maven、マルチスレッド、Nexus、Windows、JVM、Service-NOW、Python、AIまたはDevOps、Linux、アルゴリズム、銀行業務の中からランダムに1つの技術を選択してください"
        "'[具体的な課題]で行き詰まっていますか？Copilotに聞いてみましょう！' または '[タスク]に苦戦していますか？Copilotが助けになります！' の形式でフォーマットしてください"
        "設定、デバッグ、最適化など課題のバリエーションを確保してください"
        "300文字以内に収め、MarkdownやURLは避け、文のみを出力してください"
    )
    message = call_mistral_api(prompt)
    if message:
        return message.strip()[:300]
    return "Control-Mの注文日設定で行き詰まっていますか？Copilotに聞いてみましょう！"

def main():
    parser = argparse.ArgumentParser(description="Telegram習慣リマインダーボット")
    parser.add_argument("--job", choices=["send_reminder", "send_message"], required=True, help="実行するジョブ")
    parser.add_argument("--message", type=str, help="'send_message'ジョブ用の送信メッセージ")
    args = parser.parse_args()

    if args.job == "send_reminder":
        if TELEGRAM_HABIT_BOT_API_KEY and TELEGRAM_CHAT_ID:
            message = generate_copilot_message()
            send_telegram_message(TELEGRAM_HABIT_BOT_API_KEY, TELEGRAM_CHAT_ID, message)
        else:
            print("エラー: TELEGRAM_HABIT_BOT_API_KEYまたはTELEGRAM_CHAT_IDが設定されていません。")
    elif args.job == "send_message":
        if TELEGRAM_HABIT_BOT_API_KEY and TELEGRAM_CHAT_ID:
            message = args.message if args.message else "ボットからのデフォルトテストメッセージ！"
            send_telegram_message(TELEGRAM_HABIT_BOT_API_KEY, TELEGRAM_CHAT_ID, message)
        else:
            print("エラー: TELEGRAM_HABIT_BOT_API_KEYまたはTELEGRAM_CHAT_IDが設定されていません。")

if __name__ == "__main__":
    main()
```

## GitHub Action

```yaml
name: 習慣

on:
  schedule:
    # UTC時間05:00–13:00（月〜金）の毎時0,10,20,30,40,50分に実行
    # UTC+8（北京時間）では13:00–21:00に相当
    - cron: '0,10,20,30,40,50 5-13 * * 1-5'

  workflow_dispatch:
    # テスト用に手動トリガーを許可
    inputs:
      message:
        description: 'テスト用カスタムメッセージ（任意）'
        required: false
        default: 'GitHub Actionsからのテストメッセージ。'
      job:
        description: '実行するジョブ（任意）'
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
      - name: リポジトリをチェックアウト
        uses: actions/checkout@v4
        with:
          fetch-depth: 5

      - name: Python 3.13をセットアップ
        uses: actions/setup-python@v4
        with:
          python-version: "3.13"

      - name: 依存関係をインストール
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: 習慣リマインダースクリプトを実行（スケジュール）
        run: python scripts/bot/habit_bot.py --job send_reminder
        if: github.event_name == 'schedule'

      - name: 習慣リマインダースクリプトを実行（手動トリガー）
        run: python scripts/bot/habit_bot.py --job ${{ github.event.inputs.job }} --message "${{ github.event.inputs.message }}"
        if: github.event_name == 'workflow_dispatch'

      - name: mainブランチへのプッシュを通知
        run: python scripts/bot/habit_bot.py --job send_message --message "習慣ボットのコード変更がmainブランチにプッシュされました。"
        if: github.event_name == 'push'
```