---
audio: false
generated: true
lang: hant
layout: post
title: 使用 Supabase 的打卡提醒
translated: true
type: note
---

我將協助您修改現有的 GitHub Actions 工作流程和 Python 腳本，實現從星期三到星期五的打卡提醒功能，在 SGT 時間中午 12 點至下午 3 點（上班打卡）和晚上 6 點至 9 點（下班打卡）期間每 5 分鐘發送提醒，並在收到 Telegram 的 "punch" 訊息時停止提醒。我們將使用 Supabase 來追蹤打卡狀態，以避免重複提醒。

以下是完整的說明和程式碼：

---

### GitHub Actions 工作流程
工作流程需要在 SGT（UTC+8）的指定時間窗口內每 5 分鐘運行一次：
- 上班打卡：中午 12 點至下午 3 點 SGT = 4 AM 至 7 AM UTC
- 下班打卡：晚上 6 點至 9 點 SGT = 10 AM 至 1 PM UTC
- 日期：星期三至星期五（cron 語法中的 3-5）

我們將使用單一的 cron 排程來合併這些時段，並讓腳本決定要執行的動作。

```yaml
name: 打卡提醒

on:
  schedule:
    # 在 UTC 時間 4-7 AM 和 10 AM-1 PM 期間每 5 分鐘運行，星期三至星期五
    # 4-7 AM UTC = 中午 12 點-下午 3 點 SGT, 10 AM-1 PM UTC = 晚上 6 點-9 點 SGT
    - cron: '*/5 4-7,10-13 * * 3-5'

  workflow_dispatch:
    inputs:
      job_name:
        description: '要執行的作業 (punch_reminder, send_message)'
        required: true
        default: 'punch_reminder'
      message:
        description: 'send_message 作業的自訂訊息（可選）'
        required: false
        default: '這是來自 GitHub Actions 的手動觸發測試訊息。'

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
    - name: 檢出儲存庫
      uses: actions/checkout@v4
      with:
        fetch-depth: 5

    - name: 設定 Python 3.13.2
      uses: actions/setup-python@v4
      with:
        python-version: "3.13.2"

    - name: 安裝依賴套件
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.simple.txt

    - name: 執行打卡提醒腳本（排程觸發）
      run: python scripts/release/location_bot.py --job punch_reminder
      if: github.event_name == 'schedule'

    - name: 執行打卡提醒腳本（手動觸發）
      run: python scripts/release/location_bot.py --job punch_reminder
      if: github.event_name == 'workflow_dispatch' && github.event.inputs.job_name == 'punch_reminder'

    - name: 執行 Telegram 腳本發送自訂訊息（手動觸發）
      run: python scripts/release/location_bot.py --job send_message --message "${{ github.event.inputs.message }}"
      if: github.event_name == 'workflow_dispatch' && github.event.inputs.job_name == 'send_message'

    - name: 在推送到 main 分支時通知
      run: python scripts/release/location_bot.py --job send_message --message "打卡提醒機器人的程式碼變更已推送至 main 分支。"
      if: github.event_name == 'push'
```

---

### Python 腳本
該腳本將：
- 檢查當前 SGT 時間以確定是否處於上班或下班打卡時段
- 使用 Supabase 追蹤打卡狀態
- 獲取 Telegram 更新以檢查 "punch" 訊息
- 如果尚未記錄打卡，則發送提醒

更新您的 `requirements.simple.txt` 以包含：
```
requests
supabase
pytz
```

以下是修改後的腳本：

```python
import os
import requests
import datetime
import pytz
from supabase import create_client
import argparse

# 載入環境變數
TELEGRAM_LOCATION_BOT_API_KEY = os.environ.get("TELEGRAM_LOCATION_BOT_API_KEY")
TELEGRAM_CHAT_ID = "610574272"  # 您的聊天 ID

def send_telegram_message(bot_token, chat_id, message):
    """使用 Telegram Bot API 發送訊息到 Telegram 聊天。"""
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown"
    }
    response = requests.post(url, params=params)
    if response.status_code != 200:
        print(f"發送 Telegram 訊息時出錯：{response.status_code} - {response.text}")

def send_reminder(action):
    """發送打卡提醒訊息。"""
    message = f"⏰ *提醒：* 請透過向此機器人發送 'punch' 來進行{action.replace('_', ' ')}打卡。"
    send_telegram_message(TELEGRAM_LOCATION_BOT_API_KEY, TELEGRAM_CHAT_ID, message)

def main():
    parser = argparse.ArgumentParser(description="Telegram 打卡提醒機器人")
    parser.add_argument('--job', choices=['punch_reminder', 'send_message'], required=True, help="要執行的作業")
    parser.add_argument('--message', type=str, help="用於 'send_message' 作業的訊息")
    args = parser.parse_args()

    if args.job == 'send_message':
        if TELEGRAM_LOCATION_BOT_API_KEY and TELEGRAM_CHAT_ID:
            message = args.message if args.message else "來自您機器人的預設測試訊息！"
            send_telegram_message(TELEGRAM_LOCATION_BOT_API_KEY, TELEGRAM_CHAT_ID, message)
            print(f"已發送訊息：{message}")
        else:
            print("未設定 TELEGRAM_LOCATION_BOT_API_KEY 和 TELEGRAM_CHAT_ID。")
        return

    elif args.job == 'punch_reminder':
        # 初始化 Supabase
        supabase = create_client(os.environ['SUPABASE_URL'], os.environ['SUPABASE_KEY'])

        # 獲取當前 SGT 時間（UTC+8）
        sgt = pytz.timezone('Asia/Singapore')
        now_utc = datetime.datetime.utcnow()
        now_sgt = now_utc.replace(tzinfo=pytz.utc).astimezone(sgt)
        today_sgt = now_sgt.date()

        # 定義時間窗口
        punch_in_start = datetime.time(12, 0)  # 中午 12 點 SGT
        punch_in_end = datetime.time(15, 0)    # 下午 3 點 SGT
        punch_out_start = datetime.time(18, 0) # 晚上 6 點 SGT
        punch_out_end = datetime.time(21, 0)   # 晚上 9 點 SGT

        current_time = now_sgt.time()

        # 確定當前時間窗口
        if punch_in_start <= current_time <= punch_in_end:
            window = 'punch_in'
        elif punch_out_start <= current_time <= punch_out_end:
            window = 'punch_out'
        else:
            window = None

        if not window:
            print("不在打卡提醒時間窗口內。")
            return

        # 獲取今天的打卡記錄
        response = supabase.table('punch_records').select('*').eq('date', str(today_sgt)).execute()
        punch_record = response.data[0] if response.data else None

        # 檢查是否已打卡
        if window == 'punch_in' and punch_record and punch_record['punch_in_time']:
            print("今天已打上班卡。")
            return
        if window == 'punch_out' and punch_record and punch_record['punch_out_time']:
            print("今天已打下班卡。")
            return

        # 獲取最後處理的 Telegram 更新 ID
        state_response = supabase.table('telegram_state').select('last_update_id').eq('id', 1).execute()
        last_update_id = state_response.data[0]['last_update_id'] if state_response.data else 0

        # 獲取新的 Telegram 更新
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
                # 處理 "punch" 訊息
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

        # 更新 last_update_id
        if max_update_id > last_update_id:
            supabase.table('telegram_state').update({
                'last_update_id': max_update_id
            }).eq('id', 1).execute()

        # 重新獲取打卡記錄以檢查最新狀態
        response = supabase.table('punch_records').select('*').eq('date', str(today_sgt)).execute()
        punch_record = response.data[0] if response.data else None

        # 如果未記錄打卡，則發送提醒
        if window == 'punch_in' and (not punch_record or not punch_record['punch_in_time']):
            send_reminder('punch_in')
        elif window == 'punch_out' and (not punch_record or not punch_record['punch_out_time']):
            send_reminder('punch_out')

if __name__ == '__main__':
    main()
```

---

### Supabase 設定
我們將在 Supabase 中建立兩個表格來管理打卡狀態和 Telegram 更新。

#### SQL 指令
在 Supabase SQL 編輯器中執行以下 SQL 指令：

```sql
-- 用於儲存每日打卡記錄的表格
CREATE TABLE punch_records (
    date DATE PRIMARY KEY,
    punch_in_time TIMESTAMP,
    punch_out_time TIMESTAMP
);

-- 用於儲存 Telegram 狀態的表格
CREATE TABLE telegram_state (
    id INTEGER PRIMARY KEY,
    last_update_id BIGINT NOT NULL DEFAULT 0
);

-- 使用單一行初始化 telegram_state
INSERT INTO telegram_state (id, last_update_id) VALUES (1, 0);
```

#### 執行步驟
1. 登入您的 Supabase 儀表板。
2. 導航至 **SQL Editor**。
3. 貼上並執行上面的 SQL 程式碼以建立和初始化表格。

---

### 環境變數
確保在您的 GitHub 儲存庫的 **Settings > Secrets and variables > Actions > Secrets** 下設定了這些秘密：
- `TELEGRAM_LOCATION_BOT_API_KEY`：您的 Telegram 機器人令牌。
- `SUPABASE_URL`：您的 Supabase 專案 URL（例如 `https://xyz.supabase.co`）。
- `SUPABASE_KEY`：您的 Supabase anon 金鑰（在 **Settings > API** 中找到）。

---

### 運作原理
1. **排程**：工作流程在星期三至星期五的 SGT 時間中午 12 點至下午 3 點和晚上 6 點至 9 點（已調整為 UTC）期間每 5 分鐘運行一次。
2. **時間檢查**：腳本檢查當前 SGT 時間以確定是否處於上班或下班打卡窗口。
3. **狀態管理**：
   - 檢查 `punch_records` 中今天的打卡記錄。
   - 如果已打卡（例如，在中午 12 點至下午 3 點期間已設定 `punch_in_time`），則不發送提醒。
4. **Telegram 更新**：
   - 獲取自上次處理的 `update_id` 以來的更新。
   - 如果找到 "punch" 訊息，則使用當前時間更新 `punch_records` 中的上班或下班打卡時間。
   - 使用最新的 `update_id` 更新 `telegram_state`。
5. **提醒**：如果當前窗口的打卡尚未記錄，則每 5 分鐘發送一次提醒。

---

### 測試
- **手動觸發**：使用 `workflow_dispatch` 並設定 `job_name: punch_reminder` 來手動測試。
- **Telegram**：在打卡窗口期間向您的機器人發送 "punch" 以停止該時間段的提醒。
- **Supabase**：檢查 `punch_records` 表格以驗證打卡時間是否已記錄。

此設定使用基於時間的打卡提醒取代了基於位置的邏輯，並在 GitHub Actions 的限制內利用 Supabase 進行持久狀態管理。