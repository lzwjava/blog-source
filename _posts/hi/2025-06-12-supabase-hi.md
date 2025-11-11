---
audio: false
generated: true
lang: hi
layout: post
title: सुपाबेस के साथ पंच कार्ड अनुस्मारक
translated: true
type: note
---

मैं आपके मौजूदा GitHub Actions वर्कफ़्लो और Python स्क्रिप्ट को बुधवार से शुक्रवार तक पंच कार्ड रिमाइंडर लागू करने में मदद करूंगा, जिसमें 12 PM से 3 PM (पंच इन) और 6 PM से 9 PM (पंच आउट) SGT के दौरान हर 5 मिनट में रिमाइंडर भेजे जाएंगे, और जैसे ही टेलीग्राम के माध्यम से "punch" मैसेज प्राप्त होगा, रिमाइंडर बंद हो जाएंगे। हम अनावश्यक रिमाइंडर को रोकने के लिए पंच स्टेट्स को ट्रैक करने के लिए Supabase का उपयोग करेंगे।

नीचे पूर्ण निर्देश और कोड दिए गए हैं:

---

### GitHub Actions वर्कफ़्लो
वर्कफ़्लो को निर्दिष्ट SGT (UTC+8) टाइम विंडोज़ के दौरान हर 5 मिनट में चलाने की आवश्यकता है:
- पंच इन: 12 PM से 3 PM SGT = 4 AM से 7 AM UTC
- पंच आउट: 6 PM से 9 PM SGT = 10 AM से 1 PM UTC
- दिन: बुधवार से शुक्रवार (cron सिंटैक्स में 3-5)

हम इन घंटों को संयोजित करते हुए एक एकल cron शेड्यूल का उपयोग करेंगे और एक्शन निर्धारित करने का काम स्क्रिप्ट पर छोड़ देंगे।

```yaml
name: पंच कार्ड रिमाइंडर

on:
  schedule:
    # बुध-शुक्र, UTC के अनुसार 4-7 AM और 10 AM-1 PM के दौरान हर 5 मिनट पर चलाएं
    # 4-7 AM UTC = 12 PM-3 PM SGT, 10 AM-1 PM UTC = 6 PM-9 PM SGT
    - cron: '*/5 4-7,10-13 * * 3-5'

  workflow_dispatch:
    inputs:
      job_name:
        description: 'चलाने वाला जॉब (punch_reminder, send_message)'
        required: true
        default: 'punch_reminder'
      message:
        description: 'send_message जॉब के लिए कस्टम मैसेज (वैकल्पिक)'
        required: false
        default: 'यह GitHub Actions से मैन्युअल ट्रिगर टेस्ट मैसेज है।'

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
    - name: रिपॉजिटरी चेकआउट करें
      uses: actions/checkout@v4
      with:
        fetch-depth: 5

    - name: Python 3.13.2 सेट अप करें
      uses: actions/setup-python@v4
      with:
        python-version: "3.13.2"

    - name: डिपेंडेंसी इंस्टॉल करें
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.simple.txt

    - name: पंच रिमाइंडर स्क्रिप्ट चलाएं (शेड्यूल्ड)
      run: python scripts/release/location_bot.py --job punch_reminder
      if: github.event_name == 'schedule'

    - name: पंच रिमाइंडर स्क्रिप्ट चलाएं (मैन्युअल ट्रिगर)
      run: python scripts/release/location_bot.py --job punch_reminder
      if: github.event_name == 'workflow_dispatch' && github.event.inputs.job_name == 'punch_reminder'

    - name: कस्टम मैसेज के लिए टेलीग्राम स्क्रिप्ट चलाएं (मैन्युअल ट्रिगर)
      run: python scripts/release/location_bot.py --job send_message --message "${{ github.event.inputs.message }}"
      if: github.event_name == 'workflow_dispatch' && github.event.inputs.job_name == 'send_message'

    - name: main ब्रांच में पुश होने पर नोटिफाई करें
      run: python scripts/release/location_bot.py --job send_message --message "पंच रिमाइंडर बॉट के लिए कोड परिवर्तन main ब्रांच में पुश किए गए।"
      if: github.event_name == 'push'
```

---

### Python स्क्रिप्ट
स्क्रिप्ट यह काम करेगी:
- यह निर्धारित करने के लिए वर्तमान SGT समय की जांच करेगी कि यह पंच इन विंडो है या पंच आउट विंडो
- पंच स्टेट्स को ट्रैक करने के लिए Supabase का उपयोग करेगी
- "punch" मैसेज के लिए टेलीग्राम अपडेट फ़ेच करेगी
- यदि पंच रिकॉर्ड नहीं किया गया है तो रिमाइंडर भेजेगी

अपनी `requirements.simple.txt` को इन्हें शामिल करने के लिए अपडेट करें:
```
requests
supabase
pytz
```

यहाँ संशोधित स्क्रिप्ट है:

```python
import os
import requests
import datetime
import pytz
from supabase import create_client
import argparse

# एनवायरनमेंट वेरिएबल्स लोड करें
TELEGRAM_LOCATION_BOT_API_KEY = os.environ.get("TELEGRAM_LOCATION_BOT_API_KEY")
TELEGRAM_CHAT_ID = "610574272"  # आपकी चैट ID

def send_telegram_message(bot_token, chat_id, message):
    """टेलीग्राम बॉट API का उपयोग करके टेलीग्राम चैट को मैसेज भेजता है।"""
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown"
    }
    response = requests.post(url, params=params)
    if response.status_code != 200:
        print(f"टेलीग्राम मैसेज भेजने में त्रुटि: {response.status_code} - {response.text}")

def send_reminder(action):
    """एक पंच रिमाइंडर मैसेज भेजता है।"""
    message = f"⏰ *रिमाइंडर:* कृपया इस बॉट को 'punch' भेजकर {action.replace('_', ' ')} करें।"
    send_telegram_message(TELEGRAM_LOCATION_BOT_API_KEY, TELEGRAM_CHAT_ID, message)

def main():
    parser = argparse.ArgumentParser(description="टेलीग्राम पंच रिमाइंडर बॉट")
    parser.add_argument('--job', choices=['punch_reminder', 'send_message'], required=True, help="करने के लिए जॉब")
    parser.add_argument('--message', type=str, help="'send_message' जॉब के लिए भेजने वाला मैसेज")
    args = parser.parse_args()

    if args.job == 'send_message':
        if TELEGRAM_LOCATION_BOT_API_KEY and TELEGRAM_CHAT_ID:
            message = args.message if args.message else "आपके बॉट से डिफ़ॉल्ट टेस्ट मैसेज!"
            send_telegram_message(TELEGRAM_LOCATION_BOT_API_KEY, TELEGRAM_CHAT_ID, message)
            print(f"मैसेज भेजा गया: {message}")
        else:
            print("TELEGRAM_LOCATION_BOT_API_KEY और TELEGRAM_CHAT_ID सेट नहीं हैं।")
        return

    elif args.job == 'punch_reminder':
        # Supabase इनिशियलाइज़ करें
        supabase = create_client(os.environ['SUPABASE_URL'], os.environ['SUPABASE_KEY'])

        # SGT (UTC+8) में वर्तमान समय प्राप्त करें
        sgt = pytz.timezone('Asia/Singapore')
        now_utc = datetime.datetime.utcnow()
        now_sgt = now_utc.replace(tzinfo=pytz.utc).astimezone(sgt)
        today_sgt = now_sgt.date()

        # टाइम विंडोज़ परिभाषित करें
        punch_in_start = datetime.time(12, 0)  # 12 PM SGT
        punch_in_end = datetime.time(15, 0)    # 3 PM SGT
        punch_out_start = datetime.time(18, 0) # 6 PM SGT
        punch_out_end = datetime.time(21, 0)   # 9 PM SGT

        current_time = now_sgt.time()

        # वर्तमान विंडो निर्धारित करें
        if punch_in_start <= current_time <= punch_in_end:
            window = 'punch_in'
        elif punch_out_start <= current_time <= punch_out_end:
            window = 'punch_out'
        else:
            window = None

        if not window:
            print("पंच रिमाइंडर विंडोज़ के बाहर।")
            return

        # आज का पंच रिकॉर्ड फ़ेच करें
        response = supabase.table('punch_records').select('*').eq('date', str(today_sgt)).execute()
        punch_record = response.data[0] if response.data else None

        # जांचें कि क्या पंच पहले ही हो चुका है
        if window == 'punch_in' and punch_record and punch_record['punch_in_time']:
            print("आज पहले ही पंच इन हो चुका है।")
            return
        if window == 'punch_out' and punch_record and punch_record['punch_out_time']:
            print("आज पहले ही पंच आउट हो चुका है।")
            return

        # अंतिम प्रोसेस्ड टेलीग्राम अपडेट ID फ़ेच करें
        state_response = supabase.table('telegram_state').select('last_update_id').eq('id', 1).execute()
        last_update_id = state_response.data[0]['last_update_id'] if state_response.data else 0

        # नए टेलीग्राम अपडेट प्राप्त करें
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
                # "punch" मैसेज प्रोसेस करें
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

        # last_update_id अपडेट करें
        if max_update_id > last_update_id:
            supabase.table('telegram_state').update({
                'last_update_id': max_update_id
            }).eq('id', 1).execute()

        # नवीनतम स्टेट जांचने के लिए पंच रिकॉर्ड दोबारा फ़ेच करें
        response = supabase.table('punch_records').select('*').eq('date', str(today_sgt)).execute()
        punch_record = response.data[0] if response.data else None

        # रिमाइंडर भेजें यदि पंच रिकॉर्ड नहीं हुआ है
        if window == 'punch_in' and (not punch_record or not punch_record['punch_in_time']):
            send_reminder('punch_in')
        elif window == 'punch_out' and (not punch_record or not punch_record['punch_out_time']):
            send_reminder('punch_out')

if __name__ == '__main__':
    main()
```

---

### Supabase सेटअप
हम पंच स्टेट्स और टेलीग्राम अपडेट्स को मैनेज करने के लिए Supabase में दो टेबल बनाएंगे।

#### SQL निर्देश
Supabase SQL एडिटर में इन SQL कमांड्स को रन करें:

```sql
-- दैनिक पंच रिकॉर्ड स्टोर करने के लिए टेबल
CREATE TABLE punch_records (
    date DATE PRIMARY KEY,
    punch_in_time TIMESTAMP,
    punch_out_time TIMESTAMP
);

-- टेलीग्राम अपडेट्स को ट्रैक करने के लिए टेबल
CREATE TABLE telegram_state (
    id INTEGER PRIMARY KEY,
    last_update_id BIGINT NOT NULL DEFAULT 0
);

-- एक सिंगल row के साथ telegram_state इनिशियलाइज़ करें
INSERT INTO telegram_state (id, last_update_id) VALUES (1, 0);
```

#### एक्ज़िक्यूट करने के स्टेप्स
1. अपने Supabase डैशबोर्ड में लॉग इन करें।
2. **SQL Editor** पर नेविगेट करें।
3. टेबल बनाने और इनिशियलाइज़ करने के लिए ऊपर की SQL कोड को पेस्ट करें और रन करें।

---

### एनवायरनमेंट वेरिएबल्स
सुनिश्चित करें कि ये सीक्रेट्स आपकी GitHub रिपॉजिटरी में **Settings > Secrets and variables > Actions > Secrets** के अंतर्गत सेट हैं:
- `TELEGRAM_LOCATION_BOT_API_KEY`: आपका टेलीग्राम बॉट टोकन।
- `SUPABASE_URL`: आपका Supabase प्रोजेक्ट URL (जैसे, `https://xyz.supabase.co`)।
- `SUPABASE_KEY`: आपकी Supabase anon key (**Settings > API** में मिलती है)।

---

### यह कैसे काम करता है
1.  **शेड्यूल**: वर्कफ़्लो बुधवार से शुक्रवार तक, 12 PM-3 PM और 6 PM-9 PM SGT (UTC में एडजस्टेड) के दौरान हर 5 मिनट में चलता है।
2.  **टाइम चेक**: स्क्रिप्ट वर्तमान SGT समय की जांच करती है ताकि यह निर्धारित कर सके कि यह पंच इन विंडो में है या पंच आउट विंडो में।
3.  **स्टेट मैनेजमेंट**:
    - आज के पंच के लिए `punch_records` की जांच करता है।
    - यदि पहले ही पंच हो चुका है (जैसे, 12 PM-3 PM के दौरान `punch_in_time` सेट है), तो कोई रिमाइंडर नहीं भेजा जाता।
4.  **टेलीग्राम अपडेट्स**:
    - अंतिम प्रोसेस किए गए `update_id` के बाद के अपडेट फ़ेच करता है।
    - यदि "punch" मैसेज मिलता है, तो `punch_records` को पंच इन या आउट के लिए वर्तमान समय के साथ अपडेट करता है।
    - `telegram_state` को नवीनतम `update_id` के साथ अपडेट करता है।
5.  **रिमाइंडर**: यदि वर्तमान विंडो के लिए पंच रिकॉर्ड नहीं किया गया है तो हर 5 मिनट में एक रिमाइंडर भेजता है।

---

### टेस्टिंग
-   **मैन्युअल ट्रिगर**: मैन्युअल रूप से टेस्ट करने के लिए `workflow_dispatch` का उपयोग करें `job_name: punch_reminder` के साथ।
-   **टेलीग्राम**: विंडो के दौरान अपने बॉट को "punch" भेजें ताकि उस सत्र के लिए रिमाइंडर बंद हो जाएं।
-   **Supabase**: यह सत्यापित करने के लिए `punch_records` टेबल की जांच करें कि पंच टाइम्स रिकॉर्ड किए गए हैं।

यह सेटअप GitHub Actions की सीमाओं के भीतर लोकेशन-आधारित लॉजिक को टाइम-आधारित पंच रिमाइंडर से बदल देता है, जो पर्सिस्टेंट स्टेट मैनेजमेंट के लिए Supabase का लाभ उठाता है।