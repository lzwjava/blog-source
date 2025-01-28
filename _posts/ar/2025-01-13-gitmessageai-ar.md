---
audio: true
lang: ar
layout: post
title: رسائل الالتزام في Git التي يعمل بالذكاء الاصطناعي
translated: true
---

يجب وضع هذا البرنامج النصي البايثون في دليل مضمن في مسار النظام الخاص بك، مثل `~/bin`.

```python
import subprocess
import os
from openai import OpenAI
from dotenv import load_dotenv
import argparse
import requests

load_dotenv()

def call_mistral_api(prompt):
    api_key = os.environ.get("MISTRAL_API_KEY")
    if not api_key:
        print("خطأ: متغير البيئة MISTRAL_API_KEY غير معرف.")
        return None

    url = "https://api.mistral.ai/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "model": "mistral-large-latest",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        response_json = response.json()
        if response_json and response_json['choices']:
            return response_json['choices'][0]['message']['content']
        else:
            print(f"خطأ Mistral API: تنسيق الاستجابة غير صالح: {response_json}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"خطأ Mistral API: {e}")
        if e.response:
            print(f"رمز حالة الاستجابة: {e.response.status_code}")
            print(f"محتوى الاستجابة: {e.response.text}")
        return None

def call_gemini_api(prompt):
    gemini_api_key = os.environ.get("GEMINI_API_KEY")
    if not gemini_api_key:
        print("خطأ: متغير البيئة GEMINI_API_KEY غير معرف.")
        return None
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"
    params = {"key": gemini_api_key}
    payload = {"contents": [{"parts": [{"text": prompt}]}]}
    try:
        response = requests.post(url, json=payload, params=params)
        response.raise_for_status()  # ارفع استثناء لرموز الحالة السيئة
        response_json = response.json()
        if response_json and 'candidates' in response_json and response_json['candidates']:
            return response_json['candidates'][0]['content']['parts'][0]['text']
        else:
            print(f"خطأ Gemini API: تنسيق الاستجابة غير صالح: {response_json}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"خطأ Gemini API: {e}")
        if e.response:
            print(f"رمز حالة الاستجابة: {e.response.status_code}")
            print(f"محتوى الاستجابة: {e.response.text}")
        return None

def call_deepseek_api(prompt):
    api_key = os.environ.get("DEEPSEEK_API_KEY")
    if not api_key:
        print("خطأ: متغير البيئة DEEPSEEK_API_KEY غير معرف.")
        return None

    client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=100
        )
        if response and response.choices:
            commit_message = response.choices[0].message.content.strip()
            commit_message = commit_message.replace('`', '')
            return commit_message
        else:
            print("خطأ: عدم وجود استجابة من الواجهة البرمجية.")
            return None
    except Exception as e:
        print(f"خطأ أثناء الاتصال بالواجهة البرمجية: {e}")
        print(e)
        return None

def gitmessageai(push=True, only_message=False, api='deepseek'):
    # تجهيز جميع التغييرات
    subprocess.run(["git", "add", "-A"], check=True)

    # الحصول على ملخص موجز للتغييرات
    files_process = subprocess.run(["git", "diff", "--staged", "--name-only"], capture_output=True, text=True, check=True)
    changed_files = files_process.stdout

    if not changed_files:
        print("لا توجد تغييرات للإرسال.")
        return

    # إعداد الوصف للذكاء الاصطناعي
    prompt = f"""
أنشئ رسالة إرسال موجزة بتنسيق Conventional Commits للتغييرات البرمجية التالية.
استخدم أحد الأنواع التالية: feat, fix, docs, style, refactor, test, chore, perf, ci, build, or revert.
إذا كان مناسبًا، تضمين نطاق بين أقواس لوصف جزء القاعدة المستندة إلى التغييرات.
يجب ألا تتجاوز رسالة الإرسال 70 حرفًا.

الملفات المعدلة:
{changed_files}

رسالة الإرسال:
"""

    if api == 'deepseek':
        commit_message = call_deepseek_api(prompt)
        if not commit_message:
            return
    elif api == 'gemini':
        commit_message = call_gemini_api(prompt)
        if not commit_message:
            print("خطأ: عدم وجود استجابة من Gemini API.")
            return
    elif api == 'mistral':
        commit_message = call_mistral_api(prompt)
        if not commit_message:
            print("خطأ: عدم وجود استجابة من Mistral API.")
            return
    else:
        print(f"خطأ: واجهة برمجية غير صالحة محددة: {api}")
        return

    # التحقق مما إذا كانت رسالة الإرسال فارغة
    if not commit_message:
        print("خطأ: رسالة الإرسال المنشأة فارغة. إلغاء الإرسال.")
        return

    if only_message:
        print(f"رسالة الإرسال المقترحة: {commit_message}")
        return

    # الإرسال مع الرسالة المنشأة
    subprocess.run(["git", "commit", "-m", commit_message], check=True)

    # دفع التغييرات
    if push:
        subprocess.run(["git", "push"], check=True)
    else:
        print("تم الإرسال محليًا، ولكن لم يتم دفعه.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="إنشاء رسالة إرسال مع الذكاء الاصطناعي والإرسال مع التغييرات.")
    parser.add_argument('--no-push', dest='push', action='store_false', help='الإرسال محليًا دون دفع.')
    parser.add_argument('--only-message', dest='only_message', action='store_true', help='طباعة رسالة الإرسال المنشأة بالذكاء الاصطناعي فقط.')
    parser.add_argument('--api', type=str, default='deepseek', choices=['deepseek', 'gemini', 'mistral'], help='الواجهة البرمجية المستخدمة لإنشاء رسالة الإرسال (deepseek، gemini، أو mistral).')
    args = parser.parse_args()
    gitmessageai(push=args.push, only_message=args.only_message, api=args.api)
```

يمكن استدعاء هذا البرنامج النصي مع واجهات برمجية مختلفة. على سبيل المثال:

```bash
python ~/bin/gitmessageai.py
python ~/bin/gitmessageai.py --no-push
python ~/bin/gitmessageai.py --only-message
python ~/bin/gitmessageai.py --api gemini
python ~/bin/gitmessageai.py --api mistral --no-push
python ~/bin/gitmessageai.py --api deepseek --only-message
```

ثم، في ملف `~/.zprofile` الخاص بك، أضف التالي:

```bash
alias gpa='python ~/bin/gitmessageai.py'
alias gca='python ~/bin/gitmessageai.py --no-push'
alias gm='python ~/bin/gitmessageai.py --only-message'
```

هناك العديد من التحسينات.

* واحدة هي إرسال تغييرات أسماء الملفات فقط، وعدم قراءة التغييرات المفصلة للملف باستخدام `git diff`. لا نريد إعطاء الكثير من التفاصيل لواجهة الخدمة الذكاء الاصطناعي. في هذه الحالة، لا نحتاج إليها، حيث أن عدد قليل من الأشخاص سيقرأون رسائل الإرسال بعناية.

* أحيانًا، قد تفشل واجهة برمجية Deepseek، حيث أنها شائعة جدًا حاليًا. قد نحتاج إلى استخدام Gemini بدلاً من ذلك.