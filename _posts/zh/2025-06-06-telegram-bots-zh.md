---
audio: false
generated: true
lang: zh
layout: post
title: 个人用Python机器人开发
translated: true
type: note
---

创建机器人可以是一种有趣且实用的方式来自动化任务、聚合信息或与用户互动。基于您分享的两个Telegram机器人（一个用于抓取和发送新闻摘要，另一个用于发送提醒或获取聊天ID），以下是一些针对不同使用场景和兴趣定制的其他机器人创意。每个创意都包含简要描述、潜在功能以及简单的代码结构供您入门。我假设您熟悉Python、`requests`和Telegram Bot API，如您的示例所示。

### 1. 天气预报机器人
**描述**：一个从OpenWeatherMap等天气API获取数据，用于发送指定位置的每日或按需天气更新的机器人。

**功能**：
- 在预定时间发送每日天气预报。
- 响应用户命令，如`/weather <城市>`获取即时更新。
- 包含温度、湿度和天气状况等详细信息。
- 支持多个城市或基于地理位置的预报。

**使用场景**：适用于个人提醒或群聊中需要天气更新的用户。

**基础代码结构**：
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
        return f"获取{city}的天气时出错。"
    weather = response["weather"][0]["description"]
    temp = response["main"]["temp"]
    return f"{city}的天气：{weather}，温度{temp}°C"

def daily_weather():
    weather_report = get_weather()
    send_telegram_message(weather_report)

# 安排每日天气更新
schedule.every().day.at("08:00").do(daily_weather)

def handle_updates():
    # 添加通过getUpdates轮询/weather命令的逻辑
    pass

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(60)
```

**后续步骤**：
- 从[OpenWeatherMap](https://openweathermap.org/api)获取API密钥。
- 添加用户请求的命令处理（例如`/weather London`）。
- 在小型数据库（如SQLite）中存储用户偏好（例如默认城市）。

---

### 2. 任务管理机器人
**描述**：一个管理个人或群组任务的机器人，允许用户通过Telegram命令添加、列出、完成或删除任务。

**功能**：
- 命令如`/add <任务>`、`/list`、`/complete <任务ID>`、`/delete <任务ID>`。
- 在本地文件或数据库中存储任务。
- 发送到期任务的提醒。
- 支持群聊协作任务管理。

**使用场景**：适用于个人生产力或团队协作。

**基础代码结构**：
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
            send_telegram_message(chat_id, f"已添加任务：{task}")
        elif text == "/list":
            task_list = "\n".join([f"{k}: {v['task']} ({v['status']})" for k, v in tasks.items()])
            send_telegram_message(chat_id, task_list or "无任务。")

if __name__ == "__main__":
    while True:
        handle_updates()
        time.sleep(5)
```

**后续步骤**：
- 添加`/complete`和`/delete`命令。
- 使用`schedule`实现截止日期和提醒功能。
- 使用SQLite等数据库进行更好的任务管理。

---

### 3. 股票市场机器人
**描述**：一个跟踪股票价格或市场新闻的机器人，发送特定股票或指数的更新。

**功能**：
- 命令如`/stock <股票代码>`获取实时股价。
- 每日关注股票的摘要。
- 价格显著变动时发送警报。
- 从Alpha Vantage或Yahoo Finance等API获取数据。

**使用场景**：适用于投资者或对金融市场感兴趣的人。

**基础代码结构**：
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
    return f"获取{ticker}的价格时出错。"

def handle_updates():
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/getUpdates"
    response = requests.get(url).json()
    for update in response["result"]:
        chat_id = update["message"]["chat"]["id"]
        text = update["message"]["text"]
        if text.startswith("/stock"):
            ticker = text.replace("/stock ", "")
            price = get_stock_price(ticker)
            send_telegram_message(chat_id, price)

if __name__ == "__main__":
    while True:
        handle_updates()
        time.sleep(5)
```

**后续步骤**：
- 从[Alpha Vantage](https://www.alphavantage.co/)获取API密钥。
- 添加对多个股票代码或观察列表的支持。
- 使用`schedule`发送每日市场摘要。

---

### 4. RSS订阅机器人
**描述**：一个监控RSS订阅（例如博客、新闻网站或播客）并在检测到新内容时发送到Telegram的机器人。

**功能**：
- 监控多个RSS订阅源。
- 检测到新文章或剧集时发送。
- 命令如`/addfeed <URL>`或`/listfeeds`。
- 按关键词或类别过滤。

**使用场景**：无需检查多个网站即可关注小众博客或播客。

**基础代码结构**：
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
            send_telegram_message(TELEGRAM_CHAT_ID, f"新文章：{feed.entries[0]['title']} ({latest_entry})")
    save_feeds(feeds)

if __name__ == "__main__":
    while True:
        check_feeds()
        time.sleep(600)  # 每10分钟检查一次
```

**后续步骤**：
- 添加`/addfeed`和`/removefeed`命令。
- 使用`feedparser`解析RSS（通过`pip install feedparser`安装）。
- 在JSON文件或数据库中存储订阅源和最后条目。

---

### 5. 表情包生成机器人
**描述**：一个生成或获取表情包的机器人，可以随机或基于用户输入，使用Imgflip等API或自定义表情包生成器。

**功能**：
- 命令如`/meme`获取随机表情包或`/meme <模板> <文本>`。
- 从API或Reddit（例如r/memes）获取表情包。
- 允许用户上传图像以生成自定义表情包。

**使用场景**：适用于群聊或个人娱乐。

**基础代码结构**：
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
        "template_id": template_id,  # 例如，181913649用于Drake表情包
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
                    send_telegram_photo(chat_id, meme_url, "这是您的表情包！")
                else:
                    send_telegram_photo(chat_id, "", "生成表情包失败。")

if __name__ == "__main__":
    while True:
        handle_updates()
        time.sleep(5)
```

**后续步骤**：
- 注册[Imgflip API](https://imgflip.com/api)。
- 添加对多个表情包模板的支持。
- 使用`praw`（Python Reddit API Wrapper）从Reddit获取随机表情包。

---

### 构建机器人的通用技巧
- **错误处理**：始终包含健壮的错误处理（如您的示例所示）以管理API故障或缺失的环境变量。
- **轮询与Webhook**：您的机器人使用轮询（`getUpdates`）。对于生产环境，考虑使用Webhook以减少服务器负载。
- **安全性**：将API密钥等敏感数据存储在`.env`文件中，切勿提交到版本控制。
- **速率限制**：注意API速率限制（例如Telegram、OpenWeatherMap、Alpha Vantage）并实施缓存或退避策略。
- **可扩展性**：对于复杂机器人，使用数据库（例如SQLite、MongoDB）代替JSON文件存储用户数据或偏好。
- **用户交互**：使用`python-telegram-bot`等库简化命令处理和更新处理。

### 选择机器人
- **个人兴趣**：选择与您的爱好相符的机器人（例如，股票适合金融爱好者，表情包适合娱乐）。
- **实用性**：考虑您想要自动化的任务（例如，任务管理、新闻聚合）。

基于提供的代码和创意，以下是一些补充的机器人创意，可以完善现有的新闻聚合和提醒机器人，针对不同的兴趣或需求定制：

### 6. 个人财务追踪机器人
**描述**：一个追踪支出、收入或预算目标的机器人，允许用户记录交易并接收摘要或警报。

**功能**：
- 命令如`/addexpense <金额> <类别>`、`/addincome <金额>`、`/summary`。
- 月度预算目标追踪，在接近限制时发送警报。
- 生成支出趋势的简单图表（使用本地文件或数据库）。
- 安排每周/月度财务报告。

**使用场景**：帮助管理个人或家庭财务。

**基础代码结构**：
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
    return f"摘要：\n总收入：${total_income}\n总支出：${total_expenses}\n余额：${total_income - total_expenses}"

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
                send_telegram_message(chat_id, f"已添加支出：${amount}（{category}）")
            except ValueError:
                send_telegram_message(chat_id, "用法：/addexpense <金额> <类别>")
        elif text == "/summary":
            summary = generate_summary(data)
            send_telegram_message(chat_id, summary)

if __name__ == "__main__":
    while True:
        handle_updates()
        time.sleep(5)
```

**后续步骤**：
- 添加`/setbudget <金额>`设置月度预算目标。
- 创建支出类别图表：
```chartjs
{
  "type": "pie",
  "data": {
    "labels": ["食品", "房租", "水电费", "其他"],
    "datasets": [{
      "data": [300, 1200, 150, 200],
      "backgroundColor": ["#FF6384", "#36A2EB", "#FFCE56", "#4BC0C0"]
    }]
  },
  "options": {
    "title": {
      "display": true,
      "text": "按类别划分的月度支出"
    }
  }
}
```
- 添加预算警报安排。

---

### 7. 健身追踪机器人
**描述**：一个记录锻炼、追踪健身目标或发送激励提醒的机器人。

**功能**：
- 命令如`/logworkout <类型> <时长>`、`/setgoal <步数>`、`/progress`。
- 追踪步数、卡路里或锻炼频率。
- 发送每日锻炼或喝水提醒。
- 生成进度图表。

**使用场景**：适合健身爱好者或开始健康之旅的人。

**基础代码结构**：
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
    send_telegram_message(TELEGRAM_CHAT_ID, "每日锻炼时间到！💪")

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
                send_telegram_message(chat_id, f"已记录{workout_type}，时长{duration}分钟。")
            except ValueError:
                send_telegram_message(chat_id, "用法：/logworkout <类型> <时长>")
        elif text == "/progress":
            total_minutes = sum(w["duration"] for w in data["workouts"])
            send_telegram_message(chat_id, f"总锻炼时间：{total_minutes}分钟")

schedule.every().day.at("07:00").do(daily_reminder)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        handle_updates()
        time.sleep(5)
```

**后续步骤**：
- 添加`/setgoal`设置每周/月度目标（例如步数、锻炼次数）。
- 创建锻炼趋势图表：
```chartjs
{
  "type": "line",
  "data": {
    "labels": ["周一", "周二", "周三", "周四", "周五"],
    "datasets": [{
      "label": "锻炼分钟数",
      "data": [30, 45, 0, 60, 20],
      "borderColor": "#36A2EB",
      "fill": false
    }]
  },
  "options": {
    "title": {
      "display": true,
      "text": "每周锻炼进度"
    }
  }
}
```
- 与Fitbit或Strava等API集成。

---

### 8. 学习提醒机器人
**描述**：一个通过发送学习提醒、抽认卡或追踪进度来支持学习目标的机器人。

**功能**：
- 命令如`/addflashcard <问题> <答案>`、`/quiz`、`/progress`。
- 安排每日学习提醒。
- 追踪学习时间或完成的抽认卡。
- 从存储的抽认卡组中随机测试用户。

**使用场景**：适合学生或终身学习者。

**基础代码结构**：
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
    send_telegram_message(TELEGRAM_CHAT_ID, "学习时间到！尝试使用/quiz进行抽认卡测试。")

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
                send_telegram_message(chat_id, f"已添加抽认卡：{question}")
            except ValueError:
                send_telegram_message(chat_id, "用法：/addflashcard <问题>|<答案>")
        elif text == "/quiz":
            if flashcards:
                card = random.choice(flashcards)
                send_telegram_message(chat_id, f"问题：{card['question']}\n请回复答案！")
                # 存储chat_id和问题以验证答案
            else:
                send_telegram_message(chat_id, "无可用抽认卡。使用/addflashcard添加一些！")

schedule.every().day.at("18:00").do(daily_study_reminder)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        handle_updates()
        time.sleep(5)
```

**后续步骤**：
- 添加答案验证功能。
- 追踪正确/错误答案并显示进度：
```chartjs
{
  "type": "bar",
  "data": {
    "labels": ["第1周", "第2周", "第3周", "第4周"],
    "datasets": [{
      "label": "正确答案数",
      "data": [10, 15, 12, 18],
      "backgroundColor": "#36A2EB"
    }]
  },
  "options": {
    "title": {
      "display": true,
      "text": "测试表现"
    }
  }
}
```
- 允许对抽认卡进行分类（例如按主题）。

---

### 选择合适的机器人
- **如果您对金融感兴趣**：个人财务追踪机器人非常适合预算规划和可视化支出。
- **如果您关注健康**：健身追踪机器人可以通过提醒和进度追踪保持动力。
- **如果您正在学习**：学习提醒机器人通过抽认卡和学习计划支持学习。
- **考虑您的需求**：选择解决特定问题或与爱好相符的机器人。例如，如果您已经在聚合新闻，健身或学习机器人可能会增加多样性。
- **复杂性**：从简单开始（如提醒机器人），然后逐步添加图表或API等功能。

### 技术建议
- **使用`python-telegram-bot`**：简化命令处理和更新轮询（通过`pip install python-telegram-bot`安装）。
- **数据库**：对于需要持久化数据的机器人（例如财务、健身、抽认卡），考虑使用SQLite简化操作或MongoDB提高可扩展性。
- **API**：探索OpenWeatherMap、Alpha Vantage或Reddit等免费API作为数据源。
- **调度**：使用`schedule`库进行定时任务，如您的新闻机器人所示。
- **错误处理**：继续使用健壮的错误处理（例如try-except块）以确保可靠性。

如果您需要任何这些机器人的更详细实现或帮助集成特定API，请告知！您也可以指定是否需要针对特定兴趣或任务定制的机器人。