---
audio: false
generated: false
image: false
lang: hi
layout: post
title: मिस्ट्रल के साथ एक आदत बॉट बनाना
translated: true
type: post
---

इस ब्लॉग पोस्ट में, हम पायथन और GitHub Actions का उपयोग करके स्वचालित अनुस्मारक भेजने के लिए डिज़ाइन किए गए एक हैबिट बॉट के निर्माण का पता लगाते हैं। यह बॉट मैसेजिंग के लिए टेलीग्राम API का उपयोग करता है और संदर्भ-संबंधित प्रॉम्प्ट उत्पन्न करने के लिए Mistral AI के साथ एकीकृत होता है। GitHub Actions के साथ कार्यों को शेड्यूल करके, यह बॉट समय पर नोटिफिकेशन के माध्यम से निरंतर आदतों को प्रोत्साहित करता है। हम सेटअप से लेकर स्क्रिप्टिंग और डिप्लॉयमेंट तक, आपके हैबिट ट्रैकिंग सिस्टम को स्वचालित करने के लिए एक व्यावहारिक गाइड प्रदान करते हुए चलेंगे।

## कोड

```python
import os
import requests
import argparse
import re
import datetime
from dotenv import load_dotenv
import random

# .env फ़ाइल से पर्यावरण चर लोड करें
load_dotenv()

# पर्यावरण चर
TELEGRAM_HABIT_BOT_API_KEY = os.environ.get("TELEGRAM_HABIT_BOT_API_KEY")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")
MISTRAL_API_KEY = os.environ.get("MISTRAL_API_KEY")

# टेलीग्राम संदेश की अधिकतम लंबाई
TELEGRAM_MAX_LENGTH = 4096

def send_telegram_message(bot_token, chat_id, message):
    """टेलीग्राम बॉट API का उपयोग करके टेलीग्राम चैट में एक संदेश भेजता है।"""
    if not bot_token or not chat_id:
        print("त्रुटि: TELEGRAM_HABIT_BOT_API_KEY या TELEGRAM_CHAT_ID सेट नहीं है।")
        return False
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    # टेलीग्राम संगतता सुनिश्चित करने के लिए मार्कडाउन एस्टरिस्क और URL हटाएं
    message_no_stars = message.replace('*', '')
    url_pattern = re.compile(r'(https?://[^\s]+)')
    message_no_links = url_pattern.sub('', message_no_stars)
    # यदि संदेश टेलीग्राम की लंबाई सीमा से अधिक है, तो इसे विभाजित करें
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
            print(f"टेलीग्राम संदेश भाग ({len(part)} वर्ण) सफलतापूर्वक भेजा गया।")
        except requests.exceptions.RequestException as e:
            print(f"टेलीग्राम संदेश भेजने में त्रुटि: {e}")
            success = False
    return success


def call_mistral_api(prompt, model="mistral-large-latest"):
    """Mistral API को कॉल करके एक प्रतिक्रिया उत्पन्न करता है।"""
    if not MISTRAL_API_KEY:
        print("त्रुटि: MISTRAL_API_KEY पर्यावरण चर सेट नहीं है।")
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
        "temperature": 0.7,  # रचनात्मकता के लिए तापमान समायोजित करें
        "max_tokens": 300  # प्रतिक्रिया की लंबाई सीमित करें
    }
    try:
        print(f"Mistral API को मॉडल के साथ कॉल कर रहा है: {model}")
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        response_json = response.json()
        if response_json.get('choices'):
            content = response_json['choices'][0]['message']['content']
            print(f"Mistral API सामग्री: {content}")
            return content
        print(f"Mistral API त्रुटि: {e}")
        return None

def generate_copilot_message():
    """Mistral API के माध्यम से Copilot उपयोग को प्रोत्साहित करने वाला एक तकनीकी प्रॉम्प्ट वाक्य उत्पन्न करता है।"""
    prompt = (
        f"एक यूजर बैकएंड इंजीनियर के लिए एक अद्वितीय, विशिष्ट तकनीकी प्रॉम्प्ट वाक्य उत्पन्न करें"
        "निम्नलिखित में से एक तकनीक को यादृच्छिक रूप से चुनें: Java, Spring Boot, Control-M, IBM WebSphere, Maven, मल्टीथ्रेडिंग, Nexus, Windows, JVM, Service-NOW, Python, AI या DevOps, Linux. एल्गोरिदम और बैंकिंग "
        "इसे 'क्या आप [विशिष्ट चुनौती] पर अटके हैं? Copilot से पूछें!' या '[कार्य] से जूझ रहे हैं? Copilot की मदद लें!' के रूप में फॉर्मेट करें। "
        "चुनौतियों में विविधता सुनिश्चित करें (जैसे, कॉन्फ़िगरेशन, डिबगिंग, ऑप्टिमाइज़ेशन)। "
        "इसे 300 वर्णों से कम रखें, मार्कडाउन या URL से बचें, और केवल वाक्य आउटपुट करें।"
    )
    message = call_mistral_api(prompt)
    if message:
        return message.strip()[:300]
    return "क्या आप Control-M ऑर्डर डेट कॉन्फ़िगर करने में अटके हैं? Copilot से पूछें!"

def main():
    parser = argparse.ArgumentParser(description="टेलीग्राम हैबिट अनुस्मारक बॉट")
    parser.add_argument("--job", choices=["send_reminder", "send_message"], required=True, help="करने के लिए कार्य")
    parser.add_argument("--message", type=str, help="'send_message' कार्य के लिए भेजने का संदेश")
    args = parser.parse_args()

    if args.job == "send_reminder":
        if TELEGRAM_HABIT_BOT_API_KEY and TELEGRAM_CHAT_ID:
            message = generate_copilot_message()
            send_telegram_message(TELEGRAM_HABIT_BOT_API_KEY, TELEGRAM_CHAT_ID, message)
        else:
            print("त्रुटि: TELEGRAM_HABIT_BOT_API_KEY या TELEGRAM_CHAT_ID सेट नहीं है।")
    elif args.job == "send_message":
        if TELEGRAM_HABIT_BOT_API_KEY and TELEGRAM_CHAT_ID:
            message = args.message if args.message else "बॉट से डिफ़ॉल्ट टेस्ट संदेश!"
            send_telegram_message(TELEGRAM_HABIT_BOT_API_KEY, TELEGRAM_CHAT_ID, message)
        else:
            print("त्रुटि: TELEGRAM_HABIT_BOT_API_KEY या TELEGRAM_CHAT_ID सेट नहीं है।")

if __name__ == "__main__":
    main()
```

## GitHub Action

```yaml
name: Habit

on:
  schedule:
    # हर 10 मिनट में चलाएं (0, 10, 20, 30, 40, 50 मिनट) 05:00–13:00 UTC, सोम–शुक्र
    # 05:00–13:00 UTC = 13:00–21:00 बीजिंग समय (UTC+8)
    - cron: '0,10,20,30,40,50 5-13 * * 1-5'

  workflow_dispatch:
    # परीक्षण के लिए मैनुअल ट्रिगर की अनुमति दें
    inputs:
      message:
        description: 'परीक्षण के लिए कस्टम संदेश (वैकल्पिक)'
        required: false
        default: 'GitHub Actions से टेस्ट संदेश।'
      job:
        description: 'चलाने के लिए कार्य (वैकल्पिक)'
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
      - name: रिपॉजिटरी चेकआउट करें
        uses: actions/checkout@v4
        with:
          fetch-depth: 5

      - name: Python 3.13 सेटअप करें
        uses: actions/setup-python@v4
        with:
          python-version: "3.13"

      - name: निर्भरताएँ इंस्टॉल करें
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: हैबिट अनुस्मारक स्क्रिप्ट चलाएं (शेड्यूल्ड)
        run: python scripts/bot/habit_bot.py --job send_reminder
        if: github.event_name == 'schedule'

      - name: हैबिट अनुस्मारक स्क्रिप्ट चलाएं (मैनुअल ट्रिगर)
        run: python scripts/bot/habit_bot.py --job ${{ github.event.inputs.job }} --message "${{ github.event.inputs.message }}"
        if: github.event_name == 'workflow_dispatch'

      - name: मुख्य शाखा में पुश पर नोटिफाई करें
        run: python scripts/bot/habit_bot.py --job send_message --message "हैबिट बॉट के लिए कोड परिवर्तन मुख्य शाखा में पुश किए गए।"
        if: github.event_name == 'push'
```