---
audio: false
generated: true
lang: hant
layout: post
title: 個人使用的Python機械人
translated: true
type: note
---

建立機器人可以是自動化任務、整合資訊或與用戶互動的有趣實用方式。根據您分享的兩個 Telegram 機器人（一個用於抓取和發送新聞摘要，另一個用於發送提醒或獲取聊天 ID），以下是一些針對不同使用場景和興趣的機器人開發點子。每個點子都包含簡要說明、潛在功能以及入門的簡單程式碼結構。我假設您熟悉 Python、`requests` 和 Telegram Bot API，如您的範例所示。

### 1. 天氣預報機器人
**描述**：一個從 OpenWeatherMap 等天氣 API 獲取資料，用於發送指定地點的每日或即時天氣更新的機器人。

**功能**：
- 在預定時間發送每日天氣預報。
- 回應用戶指令，如 `/weather <城市>` 以獲取即時更新。
- 包含溫度、濕度和天氣狀況等詳細資訊。
- 支援多個城市或基於地理位置的天氣預報。

**使用場景**：適用於個人提醒或群組聊天中需要天氣更新的用戶。

**基本程式碼結構**：
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

**後續步驟**：
- 從 [OpenWeatherMap](https://openweathermap.org/api) 獲取 API 金鑰。
- 為用戶請求（例如 `/weather London`）添加指令處理。
- 在小型資料庫（如 SQLite）中儲存用戶偏好設定（例如默認城市）。

---

### 2. 任務管理機器人
**描述**：一個用於管理個人或群組任務的機器人，允許用戶通過 Telegram 指令添加、列出、完成或刪除任務。

**功能**：
- 指令如 `/add <任務>`、`/list`、`/complete <任務ID>`、`/delete <任務ID>`。
- 將任務儲存在本地檔案或資料庫中。
- 為到期任務發送提醒。
- 支援群組聊天以進行協作任務管理。

**使用場景**：非常適合個人生產力或團隊協調。

**基本程式碼結構**：
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

**後續步驟**：
- 添加 `/complete` 和 `/delete` 指令。
- 使用 `schedule` 實現到期日期和提醒功能。
- 使用 SQLite 等資料庫以更好地管理任務。

---

### 3. 股票市場機器人
**描述**：一個追蹤股價或市場新聞的機器人，用於發送特定股票或指數的更新。

**功能**：
- 指令如 `/stock <股票代碼>` 以獲取實時股價。
- 每日關注股票的摘要。
- 重大價格變動的警報。
- 從 Alpha Vantage 或 Yahoo Finance 等 API 獲取資料。

**使用場景**：對投資者或任何對金融市場感興趣的人很有用。

**基本程式碼結構**：
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

**後續步驟**：
- 從 [Alpha Vantage](https://www.alphavantage.co/) 獲取 API 金鑰。
- 添加對多個股票代碼或關注列表的支援。
- 使用 `schedule` 發送每日市場摘要。

---

### 4. RSS 訂閱機器人
**描述**：一個監控 RSS 訂閱源（例如部落格、新聞網站或播客）並在檢測到新文章時發送到 Telegram 的機器人。

**功能**：
- 監控多個 RSS 訂閱源。
- 檢測到新文章或集數時發送。
- 指令如 `/addfeed <網址>` 或 `/listfeeds`。
- 按關鍵字或類別篩選。

**使用場景**：無需檢查多個網站即可隨時了解小眾部落格或播客的最新動態。

**基本程式碼結構**：
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

**後續步驟**：
- 添加 `/addfeed` 和 `/removefeed` 指令。
- 使用 `feedparser` 進行 RSS 解析（通過 `pip install feedparser` 安裝）。
- 將訂閱源和最後條目儲存在 JSON 檔案或資料庫中。

---

### 5. 迷因生成器機器人
**描述**：一個生成或獲取迷因的機器人，可以隨機或根據用戶輸入，使用 Imgflip 等 API 或自訂迷因生成器。

**功能**：
- 指令如 `/meme` 獲取隨機迷因或 `/meme <模板> <文字>`。
- 從 API 或 Reddit（例如 r/memes）獲取迷因。
- 允許用戶上傳圖片以生成自訂迷因。

**使用場景**：適合群組聊天或個人娛樂。

**基本程式碼結構**：
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

**後續步驟**：
- 註冊 [Imgflip API](https://imgflip.com/api)。
- 添加對多個迷因模板的支援。
- 使用 `praw`（Python Reddit API Wrapper）從 Reddit 獲取隨機迷因。

---

### 建立機器人的一般提示
- **錯誤處理**：始終包含健全的錯誤處理（如您的範例所示）以管理 API 故障或缺失的環境變數。
- **輪詢與 Webhooks**：您的機器人使用輪詢（`getUpdates`）。對於生產環境，請考慮使用 webhooks 以減少伺服器負載。
- **安全性**：將 API 金鑰等敏感資料儲存在 `.env` 檔案中，切勿將其提交到版本控制。
- **速率限制**：注意 API 速率限制（例如 Telegram、OpenWeatherMap、Alpha Vantage）並實施快取或退避策略。
- **可擴展性**：對於複雜的機器人，使用資料庫（例如 SQLite、MongoDB）而不是 JSON 檔案來儲存用戶資料或偏好設定。
- **用戶互動**：使用 `python-telegram-bot` 等函式庫來簡化指令處理和更新處理。

### 選擇機器人
- **個人興趣**：選擇與您的愛好相符的機器人（例如，股票適合金融愛好者，迷因適合娛樂）。
- **實用性**：考慮您想要自動化的任務（例如，任務管理、新聞聚合）。

基於提供的程式碼和點子，以下是一些可以補充現有新聞聚合器和提醒機器人的其他機器人點子，針對不同的興趣或需求：

### 6. 個人財務追蹤機器人
**描述**：一個用於追蹤支出、收入或預算目標的機器人，允許用戶記錄交易並接收摘要或警報。

**功能**：
- 指令如 `/addexpense <金額> <類別>`、`/addincome <金額>`、`/summary`。
- 每月預算目標追蹤，在接近限額時發送警報。
- 為支出趨勢生成簡單圖表（使用本地檔案或資料庫）。
- 定期的每週/每月財務報告。

**使用場景**：有助於管理個人或家庭財務。

**基本程式碼結構**：
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

**後續步驟**：
- 添加 `/setbudget <金額>` 以設定每月預算目標。
- 為支出類別建立圖表：
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
- 添加定期的預算警報。

---

### 7. 健身追蹤機器人
**描述**：一個用於記錄鍛鍊、追蹤健身目標或發送激勵提醒的機器人。

**功能**：
- 指令如 `/logworkout <類型> <持續時間>`、`/setgoal <步數>`、`/progress`。
- 追蹤步數、卡路里或鍛鍊頻率。
- 發送每日鍛鍊或喝水的提醒。
- 生成進度圖表。

**使用場景**：非常適合健身愛好者或開始健康之旅的人。

**基本程式碼結構**：
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

**後續步驟**：
- 添加 `/setgoal` 以設定每週/每月目標（例如步數、鍛鍊次數）。
- 為鍛鍊趨勢建立圖表：
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
- 與 Fitbit 或 Strava 等 API 整合。

---

### 8. 學習提醒機器人
**描述**：一個通過發送學習提醒、抽認卡或追蹤進度來支持學習目標的機器人。

**功能**：
- 指令如 `/addflashcard <問題> <答案>`、`/quiz`、`/progress`。
- 安排每日學習提醒。
- 追蹤學習時間或完成的抽認卡。
- 從儲存的抽認卡組中隨機測驗用戶。

**使用場景**：非常適合學生或終身學習者。

**基本程式碼結構**：
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

**後續步驟**：
- 為測驗添加答案驗證。
- 追蹤正確/錯誤答案並顯示進度：
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
- 允許對抽認卡進行分類（例如按主題）。

---

### 選擇合適的機器人
- **如果您對金融感興趣**：個人財務追蹤機器人非常適合預算和可視化支出。
- **如果您關注健康**：健身追蹤機器人可以通過提醒和進度追蹤來保持動力。
- **如果您正在學習**：學習提醒機器人通過抽認卡和學習計劃來支持學習。
- **考慮您的需求**：選擇能解決特定問題或與愛好相符的機器人。例如，如果您已經在聚合新聞，健身或學習機器人可能會增加多樣性。
- **複雜性**：從簡單開始（如提醒機器人），然後逐步添加圖表或 API 等功能。

### 技術建議
- **使用 `python-telegram-bot`**：簡化指令處理和更新輪詢（通過 `pip install python-telegram-bot` 安裝）。
- **資料庫**：對於具有持久性資料的機器人（例如財務、健身、抽認卡），考慮使用 SQLite 以簡化操作或 MongoDB 以實現可擴展性。
- **API**：探索免費 API，如 OpenWeatherMap、Alpha Vantage 或 Reddit 以獲取資料來源。
- **排程**：使用 `schedule` 函式庫進行定時任務，如您的新聞機器人所示。
- **錯誤處理**：繼續保持健全的錯誤處理（例如 try-except 區塊）以確保可靠性。

如果您需要對任何這些機器人進行更詳細的實現或幫助整合特定 API，請告訴我！您也可以指定是否需要針對特定興趣或任務的機器人。