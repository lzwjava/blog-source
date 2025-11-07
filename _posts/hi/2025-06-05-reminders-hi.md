---
audio: true
generated: false
image: false
lang: hi
layout: post
title: टेलीग्राम के माध्यम से अनुस्मारक सुव्यवस्थित करें
translated: true
type: post
---

इस प्रोजेक्ट में, मैंने GitHub Actions और एक Telegram बॉट का उपयोग करके एक स्वचालित अनुस्मारक प्रणाली स्थापित की है ताकि मैं अपने दैनिक और मासिक कार्यों को ट्रैक पर रख सकूँ। क्रॉन शेड्यूल का उपयोग करके, मैंने कार्य-संबंधित कार्यों के लिए अनुस्मारक कॉन्फ़िगर किए हैं जैसे WeCom में पंच इन करना, टाइमशीट जमा करना, और वेतन की जाँच करना, साथ ही व्यक्तिगत कार्य जैसे परिवार से मिलना, JD.com पर खरीदारी करना, और यहाँ तक कि अपने साथी के साथ TV देखना। यह प्रणाली Telegram के Bot API के माध्यम से संदेश भेजने के लिए एक Python स्क्रिप्ट का उपयोग करती है, जिसमें पर्यावरण चर GitHub Secrets में सुरक्षित रूप से संग्रहीत हैं। यह सेटअप सुनिश्चित करता है कि मैं कभी भी महत्वपूर्ण समय सीमाओं या व्यक्तिगत प्रतिबद्धताओं को न छोड़ूँ, प्रौद्योगिकी को रोजमर्रा की जिंदगी के साथ मिलाकर अधिकतम दक्षता प्राप्त करूँ।

```yaml
name: अनुस्मारक

on:
  schedule:
    # बीजिंग समय (UTC+8) के अनुसार बुधवार से शुक्रवार तक दोपहर 12 बजे से रात 8 बजे तक हर 2 घंटे में चलता है।
    - cron: '0 4,6,8,10,12 * * 3-5'
    # हर महीने की 27 तारीख को दोपहर 12 बजे बीजिंग समय (UTC+8) पर चलता है।
    - cron: '0 4 27 * *'
    # हर महीने की 30 तारीख को दोपहर 2 बजे बीजिंग समय (UTC+8) पर चलता है।
    - cron: '0 6 30 * *'
    # हर दिन बीजिंग समयानुसार रात 1 बजे (पिछले दिन UTC अनुसार शाम 5 बजे) चलता है।
    - cron: '0 17 * * *'
    # हर दिन बीजिंग समयानुसार सुबह 11 बजे (UTC अनुसार रात 3 बजे) चलता है।
    - cron: '0 3 * * *'
    # अगले दिन माता-पिता के घर जाने की याद दिलाता है: बीजिंग समयानुसार रात 9 बजे (UTC अनुसार दोपहर 1 बजे) मंगलवार, बुधवार, गुरुवार को।
    - cron: '0 13 * * 2-4'
    # अगले दिन अपने घर जाने की याद दिलाता है: बीजिंग समयानुसार रात 9 बजे (UTC अनुसार दोपहर 1 बजे) रविवार, सोमवार, शुक्रवार, शनिवार को।
    - cron: '0 13 * * 0,1,5,6'
    # JD.com से सीधे स्रोत से ताजा उत्पाद खरीदने की याद दिलाता है: बीजिंग समयानुसार रात 9 बजे (UTC अनुसार दोपहर 1 बजे) बुधवार को।
    - cron: '0 13 * * 3'
    # JD.com से त्वरित डिलीवरी भोजन खरीदने की याद दिलाता है: बीजिंग समयानुसार रात 9 बजे (UTC अनुसार दोपहर 1 बजे) शुक्रवार को।
    - cron: '0 13 * * 5'
    # मार्च, अप्रैल, सितंबर और अक्टूबर में एसोसिएट डिग्री परीक्षा के लिए याद दिलाता है: बीजिंग समयानुसार दोपहर 1 बजे (UTC अनुसार सुबह 5 बजे) हर सोमवार को।
    - cron: '0 5 * 3,4,9,10 1'
    # हर शुक्रवार को ताइपे समयानुसार शाम 5 बजे (UTC अनुसार सुबह 9 बजे) क्लैरिटी टाइमशीट जमा करने की याद दिलाता है।
    - cron: '0 9 * * 5'
    # हर महीने की 25 तारीख को ताइपे समयानुसार रात 12 बजे (पिछले दिन UTC अनुसार शाम 4 बजे) वेंडर टाइमशीट जमा करने की याद दिलाता है।
    - cron: '0 16 25 * *'
    # हर महीने की 16 तारीख को ताइपे समयानुसार रात 9 बजे (UTC अनुसार दोपहर 1 बजे) परिवार से गृह ऋण भुगतान में सहायता मांगने की याद दिलाता है।
    - cron: '0 13 16 * *'
    # हर शुक्रवार, शनिवार और रविवार को ताइपे समयानुसार रात 10 बजे (UTC अनुसार दोपहर 2 बजे) अपने साथी के साथ TV देखने की याद दिलाता है।
    - cron: '0 14 * * 5,6,0'
    # बीजिंग समयानुसार रात 2 बजे (UTC अनुसार शाम 6 बजे) बुधवार, गुरुवार, शुक्रवार को पार्किंग परमिट स्टिकर हटाने की याद दिलाता है।
    - cron: '0 18 * * 3,4,5'
  workflow_dispatch:  # मैन्युअल ट्रिगर करने की अनुमति देता है

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
      - name: रिपॉजिटरी चेकआउट करें
        uses: actions/checkout@v4
        with:
          fetch-depth: 5

      - name: Python 3.10.x सेटअप करें
        uses: actions/setup-python@v4
        with:
          python-version: "3.10.x"

      - name: निर्भरताएँ इंस्टॉल करें
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.simple.txt

      - name: WeCom में पंच कार्ड के लिए Telegram स्क्रिप्ट चलाएँ
        run: python scripts/release/reminders_bot.py --job send_message --message "WeCom में पंच कार्ड करें"
        if: github.event.schedule == '0 4,6,8,10,12 * * 3-5'

      - name: मासिक गृह ऋण अनुस्मारक के लिए Telegram स्क्रिप्ट चलाएँ
        run: python scripts/release/reminders_bot.py --job send_message --message "गृह ऋण कटौती की तैयारी करें"
        if: github.event.schedule == '0 4 27 * *'

      - name: मासिक वेतन जाँच अनुस्मारक के लिए Telegram स्क्रिप्ट चलाएँ
        run: python scripts/release/reminders_bot.py --job send_message --message "वेतन जाँचें"
        if: github.event.schedule == '0 6 30 * *'

      - name: सोने के समय के लिए Telegram स्क्रिप्ट चलाएँ
        run: python scripts/release/reminders_bot.py --job send_message --message "सोने का समय हो गया!"
        if: github.event.schedule == '0 17 * * *'

      - name: जागने के समय के लिए Telegram स्क्रिप्ट चलाएँ
        run: python scripts/release/reminders_bot.py --job send_message --message "जागने का समय हो गया!"
        if: github.event.schedule == '0 3 * * *'

      - name: माता-पिता के घर जाने के लिए Telegram स्क्रिप्ट चलाएँ
        run: python scripts/release/reminders_bot.py --job send_message --message "कल माता-पिता के घर जाएँ!"
        if: github.event.schedule == '0 13 * * 2-4'

      - name: अपने घर जाने के लिए Telegram स्क्रिप्ट चलाएँ
        run: python scripts/release/reminders_bot.py --job send_message --message "कल अपने घर जाएँ!"
        if: github.event.schedule == '0 13 * * 0,1,5,6'

      - name: JD.com से ताजा उत्पाद खरीदने के लिए Telegram स्क्रिप्ट चलाएँ
        run: python scripts/release/reminders_bot.py --job send_message --message "JD.com से सीधे स्रोत से ताजा उत्पाद खरीदें!"
        if: github.event.schedule == '0 13 * * 3'

      - name: JD.com से त्वरित डिलीवरी भोजन खरीदने के लिए Telegram स्क्रिप्ट चलाएँ
        run: python scripts/release/reminders_bot.py --job send_message --message "JD.com से त्वरित डिलीवरी भोजन खरीदें!"
        if: github.event.schedule == '0 13 * * 5'

      - name: एसोसिएट डिग्री परीक्षा पंजीकरण के लिए Telegram स्क्रिप्ट चलाएँ
        run: python scripts/release/reminders_bot.py --job send_message --message "एसोसिएट डिग्री परीक्षा के लिए पंजीकरण करें"
        if: github.event.schedule == '0 5 * 3,4,9,10 1'

      - name: क्लैरिटी टाइमशीट जमा करने के लिए Telegram स्क्रिप्ट चलाएँ
        run: python scripts/release/reminders_bot.py --job send_message --message "क्लैरिटी टाइमशीट जमा करें"
        if: github.event.schedule == '0 9 * * 5'

      - name: वेंडर टाइमशीट जमा करने के लिए Telegram स्क्रिप्ट चलाएँ
        run: python scripts/release/reminders_bot.py --job send_message --message "वेंडर टाइमशीट जमा करें"
        if: github.event.schedule == '0 16 25 * *'

      - name: परिवार से गृह ऋण सहायता मांगने के लिए Telegram स्क्रिप्ट चलाएँ
        run: python scripts/release/reminders_bot.py --job send_message --message "परिवार से गृह ऋण भुगतान में सहायता मांगें"
        if: github.event.schedule == '0 13 16 * *'

      - name: अपने साथी के साथ TV देखने के लिए Telegram स्क्रिप्ट चलाएँ
        run: python scripts/release/reminders_bot.py --job send_message --message "अपने साथी के साथ TV देखने का समय हो गया!"
        if: github.event.schedule == '0 14 * * 5,6,0'

      - name: कार की खिड़की से पार्किंग परमिट स्टिकर हटाने के लिए Telegram स्क्रिप्ट चलाएँ
        run: python scripts/release/reminders_bot.py --job send_message --message "कार की खिड़की से पार्किंग परमिट स्टिकर हटाएँ"
        if: github.event.schedule == '0 18 * * 3,4,5'

      - name: टेस्ट संदेश के लिए Telegram स्क्रिप्ट चलाएँ
        run: python scripts/release/reminders_bot.py --job send_message --message "यह GitHub Actions से एक टेस्ट संदेश है।"
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
    """Telegram Bot API का उपयोग करके Telegram चैट में एक संदेश भेजता है।"""
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(url, params=params)
    if response.status_code != 200:
        print(f"Telegram संदेश भेजने में त्रुटि: {response.status_code} - {response.text}")

def get_chat_id(bot_token):
    """बॉट को भेजे गए अंतिम संदेश की चैट ID प्राप्त करता है।"""
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
    """Telegram पर एक अनुस्मारक संदेश भेजता है।"""
    if TELEGRAM_BOT2_API_KEY and TELEGRAM_CHAT_ID:
        send_telegram_message(TELEGRAM_BOT2_API_KEY, TELEGRAM_CHAT_ID, f"अनुस्मारक: {message}")
    else:
        print("TELEGRAM_BOT2_API_KEY और TELEGRAM_CHAT_ID सेट नहीं हैं।")

def main():
    parser = argparse.ArgumentParser(description="Telegram बॉट स्क्रिप्ट")
    parser.add_argument('--job', choices=['get_chat_id', 'send_message'], required=True, help="करने के लिए कार्य")
    parser.add_argument('--message', help="भेजने के लिए कस्टम संदेश", default=None)
    args = parser.parse_args()

    if args.job == 'get_chat_id':
        bot_token = TELEGRAM_BOT2_API_KEY
        chat_id = get_chat_id(bot_token)
        if chat_id:
            print(f"चैट ID: {chat_id}")
        else:
            print("चैट ID प्राप्त नहीं कर सका।")

    elif args.job == 'send_message':
        if args.message:
            send_reminder(args.message)
        else:
            print("send_message कार्य के लिए कोई संदेश प्रदान नहीं किया गया।")
            
if __name__ == '__main__':
    main()
```