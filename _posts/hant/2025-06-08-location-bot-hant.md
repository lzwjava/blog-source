---
audio: false
generated: false
image: false
lang: hant
layout: post
title: 自動化您的打卡台與Telegram位置機器人
translated: true
type: post
---

日打卡系統不需要再是個負擔，我確實這樣認為。這就是為什麼我建立了個人 Telegram bot，使用位置跟蹤自動通知辦公室到達時間，並提醒重要的檢查。本文探討了如何組合Python與GitHub Actions建立無接觸、自動化的系統，基於位置保持我們獲取最新信息。

```yml
 name: Hourly Location Check

on:
  schedule:
    # Run every hour, on the hour, between 11 AM and 11 PM, on weekdays (Monday-Friday)
    # The time is in UTC. Singapore time (SGT) is UTC+8.
    # So, 11 AM SGT is 03:00 UTC, and 11 PM SGT is 15:00 UTC.
    # Therefore, we need to schedule from 03:00 to 15:00 UTC.
    - cron: '0 3-15 * * 1-5'

    # Reminder to START sharing live location: Wednesday 11 AM SGT (3 AM UTC)
    # Current time: Sunday, June 8, 2025 at 5:10:58 PM +08 (SGT)
    # For Wednesday 11 AM SGT (UTC+8): 11 - 8 = 3 AM UTC.
    - cron: '0 3 * * 3' # 3 for Wednesday

    # Reminder to STOP sharing live location: Friday 11 PM SGT (3 PM UTC)
    # Current time: Sunday, June 8, 2025 at 5:10:58 PM +08 (SGT)
    # For Friday 11 PM SGT (UTC+8): 23 - 8 = 15 PM UTC.
    - cron: '0 15 * * 5' # 5 for Friday

  workflow_dispatch:  # Allows manual triggering of the workflow
  push:
    branches: ["main"]
    paths:
      - 'scripts/release/location_bot.py' # Corrected path to your script
      - '.github/workflows/location.yml' # Path to this workflow file

concurrency:
  group: 'location'
  cancel-in-progress: false

jobs:
  check_and_notify:
    runs-on: ubuntu-latest
    env:
      TELEGRAM_LOCATION_BOT_API_KEY: ${{ secrets.TELEGRAM_LOCATION_BOT_API_KEY }}

    steps:
    - name: Checkout repository
      uses: actions/checkout@v4
      with:
        fetch-depth: 5 # Fetch only the last 5 commits for efficiency

    - name: Set up Python 3.13.2
      uses: actions/setup-python@v4
      with:
        python-version: "3.13.2" # Specify the exact Python version

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        # Assuming you have a requirements.simple.txt in your repo root.
        # If not, use: pip install requests python-dotenv
        pip install -r requirements.simple.txt

    - name: Run location check script (Scheduled)
      run: python scripts/release/location_bot.py --job check_location
      # This step will run on scheduled triggers for the hourly check
      if: github.event.schedule == '0 3-15 * * 1-5' # Match the hourly cron schedule

    - name: Reminder to START sharing live location
      run: python scripts/release/location_bot.py --job start_sharing_message
      if: github.event.schedule == '0 3 * * 3' # Matches Wednesday 11 AM SGT cron

    - name: Reminder to STOP sharing live location
      run: python scripts/release/location_bot.py --job stop_sharing_message
      if: github.event.schedule == '0 15 * * 5' # Matches Friday 11 PM SGT cron

    - name: Run Telegram script for test message (Manual Trigger)
      run: python scripts/release/location_bot.py --job send_message --message "This is a manual trigger test message from GitHub Actions."
      if: github.event_name == 'workflow_dispatch'

    - name: Run Telegram script for push to main branch
      run: python scripts/release/location_bot.py --job send_message --message "Code changes for location bot pushed to main branch."
      if: github.event_name == 'push'
```

```python
# Rest of the Python code...
```