---
audio: false
generated: true
lang: ja
layout: post
title: 個人用Pythonボット
translated: true
type: note
---

ボットを作成することは、タスクを自動化したり、情報を集約したり、ユーザーと対話したりするための、楽しく実用的な方法です。あなたが共有した2つのTelegramボット（ニュース要約をスクレイピングして送信するボットと、リマインダーを送信したりチャットIDを取得したりするボット）に基づいて、さまざまなユースケースや興味に合わせて開発できる他のボットのアイデアを紹介します。各アイデアには、簡単な説明、可能性のある機能、そして始めるためのシンプルなコード構造が含まれています。あなたの例から、Python、`requests`、Telegram Bot APIに慣れているものと想定します。

### 1. 天気予報ボット
**説明**: OpenWeatherMapのような天気APIからデータを取得して、指定された場所の毎日またはオンデマンドの天気更新を送信するボット。

**機能**:
- スケジュールされた時間に毎日の天気予報を送信。
- `/weather <都市名>` のようなユーザーコマンドに応答して即時更新を提供。
- 気温、湿度、天候などの詳細を含める。
- 複数の都市または地理位置情報に基づく予報をサポート。

**ユースケース**: 個人のリマインダーや、天気更新を希望するグループチャットのユーザーに便利。

**基本的なコード構造**:
```python
import requests
from dotenv import load_dotenv
import os
import schedule
import time

load_dotenv()

TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_API_KEY")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")
OPENWEATHER_API_KEY = os.environ.get("OPENWEATHER_API_KEY")

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    params = {"chat_id": TELEGRAM_CHAT_ID, "text": message, "parse_mode": "Markdown"}
    requests.post(url, params=params).raise_for_status()

def get_weather(city="New York"):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
    response = requests.get(url).json()
    if response.get("cod") != 200:
        return f"Error fetching weather for {city}."
    weather = response["weather"][0]["description"]
    temp = response["main"]["temp"]
    return f"Weather in {city}: {weather}, {temp}°C"

def daily_weather():
    weather_report = get_weather()
    send_telegram_message(weather_report)

# Schedule daily weather update
schedule.every().day.at("08:00").do(daily_weather)

def handle_updates():
    # Add logic to poll for /weather commands via getUpdates
    pass

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(60)
```

**次のステップ**:
- [OpenWeatherMap](https://openweathermap.org/api) からAPIキーを取得。
- ユーザーリクエスト（例: `/weather London`）のためのコマンド処理を追加。
- ユーザーの設定（例: デフォルトの都市）をSQLiteのような小さなデータベースに保存。

---

### 2. タスク管理ボット
**説明**: 個人またはグループのタスクを管理するボット。Telegramコマンドを通じてユーザーがタスクを追加、リスト表示、完了、削除できる。

**機能**:
- `/add <タスク>`, `/list`, `/complete <タスクID>`, `/delete <タスクID>` のようなコマンド。
- タスクをローカルファイルまたはデータベースに保存。
- 期限タスクのリマインダーを送信。
- 協調的なタスク管理のためのグループチャットをサポート。

**ユースケース**: 個人の生産性向上やチームの調整に最適。

**基本的なコード構造**:
```python
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_API_KEY")
TASKS_FILE = "tasks.json"

def send_telegram_message(chat_id, message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    params = {"chat_id": chat_id, "text": message}
    requests.post(url, params=params)

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def handle_updates():
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/getUpdates"
    response = requests.get(url).json()
    if not response["result"]:
        return
    for update in response["result"]:
        chat_id = update["message"]["chat"]["id"]
        text = update["message"]["text"]
        tasks = load_tasks()
        if text.startswith("/add"):
            task = text.replace("/add ", "")
            tasks[str(len(tasks) + 1)] = {"task": task, "status": "pending"}
            save_tasks(tasks)
            send_telegram_message(chat_id, f"Added task: {task}")
        elif text == "/list":
            task_list = "\n".join([f"{k}: {v['task']} ({v['status']})" for k, v in tasks.items()])
            send_telegram_message(chat_id, task_list or "No tasks.")

if __name__ == "__main__":
    while True:
        handle_updates()
        time.sleep(5)
```

**次のステップ**:
- `/complete` および `/delete` コマンドを追加。
- `schedule` を使用して期限日とリマインダーを実装。
- より良いタスク管理のためにSQLiteのようなデータベースを使用。

---

### 3. 株式市場ボット
**説明**: 特定の銘柄や指数の株価や市場ニュースを追跡し、更新を送信するボット。

**機能**:
- リアルタイム株価のための `/stock <ティッカー>` のようなコマンド。
- ウォッチリストの銘柄の毎日の要約。
- 大きな価格変動のアラート。
- Alpha Vantage や Yahoo Finance のようなAPIからデータを取得。

**ユースケース**: 投資家や金融市場に関心のある人に便利。

**基本的なコード構造**:
```python
import requests
from dotenv import load_dotenv
import os

load_dotenv()

TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_API_KEY")
ALPHA_VANTAGE_API_KEY = os.environ.get("ALPHA_VANTAGE_API_KEY")

def send_telegram_message(chat_id, message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    params = {"chat_id": chat_id, "text": message}
    requests.post(url, params=params)

def get_stock_price(ticker):
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={ticker}&apikey={ALPHA_VANTAGE_API_KEY}"
    response = requests.get(url).json()
    if "Global Quote" in response:
        price = response["Global Quote"]["05. price"]
        return f"{ticker}: ${price}"
    return f"Error fetching price for {ticker}."

def handle_updates():
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/getUpdates"
    response = requests.get(url).json()
    for update in response["result"]:
        chat_id = update["message"]["chat"]["id"]
        text = update["message"]["text"]
        if text.startswith("/stock"):
            ticker = text.replace "stock ", "")
            price = get_stock_price(ticker)
            send_telegram_message(chat_id, price)

if __name__ == "__main__":
    while True:
        handle_updates()
        time.sleep(5)
```

**次のステップ**:
- [Alpha Vantage](https://www.alphavantage.co/) からAPIキーを取得。
- 複数のティッカーまたはウォッチリストのサポートを追加。
- `schedule` を使用して毎日の市場要約を送信。

---

### 4. RSSフィードボット
**説明**: RSSフィード（ブログ、ニュースサイト、ポッドキャストなど）を監視し、新しい投稿をTelegramに送信するボット。

**機能**:
- 複数のRSSフィードを監視。
- 検出された新しい記事やエピソードを送信。
- `/addfeed <URL>` や `/listfeeds` のようなコマンド。
- キーワードやカテゴリでフィルタリング。

**ユースケース**: 複数のサイトをチェックせずにニッチなブログやポッドキャストの更新を確認。

**基本的なコード構造**:
```python
import requests
import feedparser
from dotenv import load_dotenv
import os
import json

load_dotenv()

TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_API_KEY")
FEEDS_FILE = "feeds.json"

def send_telegram_message(chat_id, message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    params = {"chat_id": chat_id, "text": message, "parse_mode": "Markdown"}
    requests.post(url, params=params)

def load_feeds():
    try:
        with open(FEEDS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"feeds": [], "last_entries": {}}

def save_feeds(feeds):
    with open(FEEDS_FILE, "w") as f:
        json.dump(feeds, f, indent=4)

def check_feeds():
    feeds = load_feeds()
    for feed_url in feeds["feeds"]:
        feed = feedparser.parse(feed_url)
        latest_entry = feed.entries[0]["link"] if feed.entries else None
        if latest_entry and latest_entry != feeds["last_entries"].get(feed_url):
            feeds["last_entries"][feed_url] = latest_entry
            send_telegram_message(TELEGRAM_CHAT_ID, f"New post: {feed.entries[0]['title']} ({latest_entry})")
    save_feeds(feeds)

if __name__ == "__main__":
    while True:
        check_feeds()
        time.sleep(600)  # Check every 10 minutes
```

**次のステップ**:
- `/addfeed` および `/removefeed` コマンドを追加。
- RSSパースに `feedparser` を使用（`pip install feedparser` でインストール）。
- フィードと最終エントリをJSONファイルまたはデータベースに保存。

---

### 5. ミームジェネレーターボット
**説明**: ImgflipのようなAPIまたはカスタムミームジェネレーターを使用して、ランダムにまたはユーザー入力に基づいてミームを生成または取得するボット。

**機能**:
- ランダムなミームのための `/meme` または `/meme <テンプレート> <テキスト>` のようなコマンド。
- APIまたはReddit（r/memesなど）からミームを取得。
- カスタムミーム生成のためにユーザーが画像をアップロードできるようにする。

**ユースケース**: グループチャットや個人の娯楽に楽しい。

**基本的なコード構造**:
```python
import requests
from dotenv import load_dotenv
import os

load_dotenv()

TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_API_KEY")
IMGFLIP_USERNAME = os.environ.get("IMGFLIP_USERNAME")
IMGFLIP_PASSWORD = os.environ.get("IMGFLIP_PASSWORD")

def send_telegram_photo(chat_id, photo_url, caption=""):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendPhoto"
    params = {"chat_id": chat_id, "photo": photo_url, "caption": caption}
    requests.post(url, params=params)

def generate_meme(template_id, text0, text1):
    url = "https://api.imgflip.com/caption_image"
    params = {
        "template_id": template_id,  # e.g., 181913649 for Drake meme
        "username": IMGFLIP_USERNAME,
        "password": IMGFLIP_PASSWORD,
        "text0": text0,
        "text1": text1
    }
    response = requests.post(url, data=params).json()
    if response["success"]:
        return response["data"]["url"]
    return None

def handle_updates():
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/getUpdates"
    response = requests.get(url).json()
    for update in response["result"]:
        chat_id = update["message"]["chat"]["id"]
        text = update["message"]["text"]
        if text.startswith("/meme"):
            parts = text.split(" ", 2)
            if len(parts) == 3:
                meme_url = generate_meme("181913649", parts[1], parts[2])
                if meme_url:
                    send_telegram_photo(chat_id, meme_url, "Here's your meme!")
                else:
                    send_telegram_photo(chat_id, "", "Failed to generate meme.")

if __name__ == "__main__":
    while True:
        handle_updates()
        time.sleep(5)
```

**次のステップ**:
- [Imgflip API](https://imgflip.com/api) にサインアップ。
- 複数のミームテンプレートのサポートを追加。
- `praw` (Python Reddit API Wrapper) を使用してRedditからランダムなミームを取得。

---

### ボット構築の一般的なヒント
- **エラー処理**: API障害や環境変数の欠落を管理するために、常に堅牢なエラー処理を含める（あなたの例のように）。
- **ポーリング vs Webhooks**: あなたのボットはポーリング（`getUpdates`）を使用しています。本番環境では、サーバーの負荷を減らすためにWebhooksを検討してください。
- **セキュリティ**: APIキーなどの機密データは `.env` ファイルに保存し、バージョン管理にコミットしないでください。
- **レート制限**: APIのレート制限（Telegram、OpenWeatherMap、Alpha Vantageなど）に注意し、キャッシングまたはバックオフ戦略を実装してください。
- **スケーラビリティ**: 複雑なボットでは、ユーザーデータや設定を保存するためにJSONファイルの代わりにデータベース（SQLite、MongoDBなど）を使用してください。
- **ユーザーインタラクション**: `python-telegram-bot` のようなライブラリを使用して、コマンド処理と更新処理を簡素化してください。

### ボットの選び方
- **個人的な興味**: あなたの趣味に合ったボットを選んでください（例: 金融愛好家には株式ボット、楽しみにはミームボット）。
- **実用性**: 自動化したいタスク（タスク管理、ニュース集約など）を考慮してください。

提供されたコードとアイデアに基づいて、既存のニュース集約ボットとリマインダーボットを補完する、さまざまな興味やニーズに合わせた追加のボットアイデアをいくつか紹介します:

### 6. 個人財務トラッカーボット
**説明**: 支出、収入、または予算目標を追跡するボット。ユーザーが取引を記録し、要約やアラートを受け取れる。

**機能**:
- `/addexpense <金額> <カテゴリ>`, `/addincome <金額>`, `/summary` のようなコマンド。
- 限度額に近づいた際のアラートを含む月次予算目標の追跡。
- 支出傾向のためのシンプルなチャートを生成（ローカルファイルまたはデータベースを使用）。
- スケジュールされた週次/月次財務レポート。

**ユースケース**: 個人または家計の財務管理に役立つ。

**基本的なコード構造**:
```python
import requests
import json
import os
from dotenv import load_dotenv
import datetime

load_dotenv()

TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_API_KEY")
FINANCE_FILE = "finance.json"

def send_telegram_message(chat_id, message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    params = {"chat_id": chat_id, "text": message, "parse_mode": "Markdown"}
    requests.post(url, params=params)

def load_finance_data():
    try:
        with open(FINANCE_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"transactions": [], "budget": 0}

def save_finance_data(data):
    with open(FINANCE_FILE, "w") as f:
        json.dump(data, f, indent=4)

def generate_summary(data):
    total_expenses = sum(t["amount"] for t in data["transactions"] if t["type"] == "expense")
    total_income = sum(t["amount"] for t in data["transactions"] if t["type"] == "income")
    return f"Summary:\nTotal Income: ${total_income}\nTotal Expenses: ${total_expenses}\nBalance: ${total_income - total_expenses}"

def handle_updates():
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/getUpdates"
    response = requests.get(url).json()
    if not response["result"]:
        return
    data = load_finance_data()
    for update in response["result"]:
        chat_id = update["message"]["chat"]["id"]
        text = update["message"]["text"]
        if text.startswith("/addexpense"):
            try:
                amount, category = text.replace("/addexpense ", "").split(" ")
                data["transactions"].append({"type": "expense", "amount": float(amount), "category": category, "date": str(datetime.datetime.now())})
                save_finance_data(data)
                send_telegram_message(chat_id, f"Added expense: ${amount} ({category})")
            except ValueError:
                send_telegram_message(chat_id, "Usage: /addexpense <amount> <category>")
        elif text == "/summary":
            summary = generate_summary(data)
            send_telegram_message(chat_id, summary)

if __name__ == "__main__":
    while True:
        handle_updates()
        time.sleep(5)
```

**次のステップ**:
- 月次予算目標を設定する `/setbudget <金額>` を追加。
- 支出カテゴリのチャートを作成:
```chartjs
{
  "type": "pie",
  "data": {
    "labels": ["Food", "Rent", "Utilities", "Other"],
    "datasets": [{
      "data": [300, 1200, 150, 200],
      "backgroundColor": ["#FF6384", "#36A2EB", "#FFCE56", "#4BC0C0"]
    }]
  },
  "options": {
    "title": {
      "display": true,
      "text": "Monthly Expenses by Category"
    }
  }
}
```
- スケジュールされた予算アラートを追加。

---

### 7. フィットネストラッカーボット
**説明**: ワークアウトを記録し、フィットネス目標を追跡、またはやる気を起こさせるリマインダーを送信するボット。

**機能**:
- `/logworkout <種類> <時間>`, `/setgoal <歩数>`, `/progress` のようなコマンド。
- 歩数、カロリー、またはワークアウト頻度を追跡。
- 運動や水分補給の毎日のリマインダーを送信。
- 進捗チャートを生成。

**ユースケース**: フィットネス愛好家や健康習慣を始める人に理想的。

**基本的なコード構造**:
```python
import requests
import json
import os
from dotenv import load_dotenv
import schedule
import time

load_dotenv()

TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_API_KEY")
FITNESS_FILE = "fitness.json"

def send_telegram_message(chat_id, message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    params = {"chat_id": chat_id, "text": message}
    requests.post(url, params=params)

def load_fitness_data():
    try:
        with open(FITNESS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"workouts": [], "goals": {}}

def save_fitness_data(data):
    with open(FITNESS_FILE, "w") as f:
        json.dump(data, f, indent=4)

def daily_reminder():
    send_telegram_message(TELEGRAM_CHAT_ID, "Time for your daily workout! 💪")

def handle_updates():
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/getUpdates"
    response = requests.get(url).json()
    if not response["result"]:
        return
    data = load_fitness_data()
    for update in response["result"]:
        chat_id = update["message"]["chat"]["id"]
        text = update["message"]["text"]
        if text.startswith("/logworkout"):
            try:
                workout_type, duration = text.replace("/logworkout ", "").split(" ")
                data["workouts"].append({"type": workout_type, "duration": int(duration)})
                save_fitness_data(data)
                send_telegram_message(chat_id, f"Logged {workout_type} for {duration} minutes.")
            except ValueError:
                send_telegram_message(chat_id, "Usage: /logworkout <type> <duration>")
        elif text == "/progress":
            total_minutes = sum(w["duration"] for w in data["workouts"])
            send_telegram_message(chat_id, f"Total workout time: {total_minutes} minutes")

schedule.every().day.at("07:00").do(daily_reminder)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        handle_updates()
        time.sleep(5)
```

**次のステップ**:
- 週次/月次の目標（歩数、ワークアウトなど）のための `/setgoal` を追加。
- ワークアウト傾向のチャートを作成:
```chartjs
{
  "type": "line",
  "data": {
    "labels": ["Mon", "Tue", "Wed", "Thu", "Fri"],
    "datasets": [{
      "label": "Workout Minutes",
      "data": [30, 45, 0, 60, 20],
      "borderColor": "#36A2EB",
      "fill": false
    }]
  },
  "options": {
    "title": {
      "display": true,
      "text": "Weekly Workout Progress"
    }
  }
}
```
- FitbitやStravaのようなAPIと統合。

---

### 8. 学習リマインダーボット
**説明**: 学習目標をサポートするボット。勉強リマインダーを送信、フラッシュカードを提供、または進捗を追跡。

**機能**:
- `/addflashcard <質問> <回答>`, `/quiz`, `/progress` のようなコマンド。
- 毎日の勉強リマインダーをスケジュール。
- 学習時間または完了したフラッシュカードを追跡。
- 保存されたフラッシュカードデッキからユーザーをランダムにクイズ。

**ユースケース**: 学生や生涯学習者に最適。

**基本的なコード構造**:
```python
import requests
import json
import os
from dotenv import load_dotenv
import random
import schedule
import time

load_dotenv()

TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_API_KEY")
FLASHCARDS_FILE = "flashcards.json"

def send_telegram_message(chat_id, message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    params = {"chat_id": chat_id, "text": message}
    requests.post(url, params=params)

def load_flashcards():
    try:
        with open(FLASHCARDS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_flashcards(flashcards):
    with open(FLASHCARDS_FILE, "w") as f:
        json.dump(flashcards, f, indent=4)

def daily_study_reminder():
    send_telegram_message(TELEGRAM_CHAT_ID, "Time to study! Try /quiz for a flashcard.")

def handle_updates():
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/getUpdates"
    response = requests.get(url).json()
    if not response["result"]:
        return
    flashcards = load_flashcards()
    for update in response["result"]:
        chat_id = update["message"]["chat"]["id"]
        text = update["message"]["text"]
        if text.startswith("/addflashcard"):
            try:
                question, answer = text.replace("/addflashcard ", "").split("|")
                flashcards.append({"question": question.strip(), "answer": answer.strip()})
                save_flashcards(flashcards)
                send_telegram_message(chat_id, f"Added flashcard: {question}")
            except ValueError:
                send_telegram_message(chat_id, "Usage: /addflashcard <question>|<answer>")
        elif text == "/quiz":
            if flashcards:
                card = random.choice(flashcards)
                send_telegram_message(chat_id, f"Question: {card['question']}\nReply with the answer!")
                # Store chat_id and question for answer verification
            else:
                send_telegram_message(chat_id, "No flashcards available. Add some with /addflashcard!")

schedule.every().day.at("18:00").do(daily_study_reminder)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        handle_updates()
        time.sleep(5)
```

**次のステップ**:
- クイズの回答検証を追加。
- 正解/不正解を追跡し、進捗を表示:
```chartjs
{
  "type": "bar",
  "data": {
    "labels": ["Week 1", "Week 2", "Week 3", "Week 4"],
    "datasets": [{
      "label": "Correct Answers",
      "data": [10, 15, 12, 18],
      "backgroundColor": "#36A2EB"
    }]
  },
  "options": {
    "title": {
      "display": true,
      "text": "Quiz Performance"
    }
  }
}
```
- フラッシュカードの分類（科目別など）を許可。

---

### 適切なボットの選択
- **金融に興味がある場合**: 個人財務トラッカーボットは、予算管理と支出の可視化に優れています。
- **健康に関心がある場合**: フィットネストラッカーボットは、リマインダーと進捗追跡でやる気を維持できます。
- **勉強中の場合**: 学習リマインダーボットは、フラッシュカードと学習スケジュールで学習をサポートします。
- **自分のニーズを考慮する**: 特定の問題を解決する、または趣味に合ったボットを選んでください。例えば、すでにニュースを集約しているなら、フィットネスや学習ボットが変化を加えるかもしれません。
- **複雑さ**: シンプルに始め（リマインダーボットのように）、チャートやAPIなどの機能を追加していきましょう。

### 技術的推奨事項
- **`python-telegram-bot`を使用**: コマンド処理と更新ポーリングを簡素化（`pip install python-telegram-bot` でインストール）。
- **データベース**: 永続的なデータを持つボット（財務、フィットネス、フラッシュカードなど）には、シンプルさのためにSQLite、またはスケーラビリティのためにMongoDBを検討。
- **API**: OpenWeatherMap、Alpha Vantage、Redditなどの無料APIをデータソースとして探索。
- **スケジューリング**: あなたのニュースボットで示されているように、タイマー処理に `schedule` ライブラリを使用。
- **エラー処理**: 信頼性を確保するために、堅牢なエラー処理（try-exceptブロックなど）を継続。

これらのボットのいずれかについてより詳細な実装や特定のAPIの統合に関するヘルプが必要な場合は、お知らせください！特定の興味やタスクに合わせたボットについても指定できます。