---
audio: true
lang: ar
layout: post
title: رسائل Git Commit المدعومة بالذكاء الاصطناعي
translated: true
---

```python
import subprocess
import os
from openai import OpenAI
from dotenv import load_dotenv
import argparse

load_dotenv()

def gitmessageai(push=True):
    """
    يولد رسالة commit باستخدام الذكاء الاصطناعي بناءً على التغييرات المعلقة ويقوم بإجراء commit لها.

    Args:
        push (bool, optional): ما إذا كان سيتم دفع التغييرات بعد الـ commit. الافتراضي هو True.
    """
    # إضافة جميع التغييرات
    subprocess.run(["git", "add", "-A"], check=True)

    # الحصول على الاختلافات المعلقة
    diff_process = subprocess.run(["git", "diff", "--staged"], capture_output=True, text=True, check=True)
    diff = diff_process.stdout

    if not diff:
        print("لا توجد تغييرات لإجراء commit لها.")
        return

    # إعداد النص الموجه للذكاء الاصطناعي
    prompt = f"""
قم بإنشاء رسالة commit موجزة بتنسيق Conventional Commits للتغييرات التالية في الكود.
استخدم أحد الأنواع التالية: feat, fix, docs, style, refactor, test, chore, perf, ci, build, أو revert.
إذا كان ذلك مناسبًا، قم بتضمين نطاق بين الأقواس لوصف الجزء المتأثر من قاعدة الكود.
يجب ألا تتجاوز رسالة commit 70 حرفًا.

التغييرات في الكود:
{diff}

رسالة commit:
"""    

    # إرسال النص الموجه إلى واجهة برمجة تطبيقات DeepSeek
    api_key = os.environ.get("DEEPSEEK_API_KEY")
    if not api_key:
        print("خطأ: لم يتم تعيين متغير البيئة DEEPSEEK_API_KEY.")
        return
    
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
        else:
            print("خطأ: لا توجد استجابة من واجهة برمجة التطبيقات.")
            return
    except Exception as e:
        print(f"خطأ أثناء استدعاء واجهة برمجة التطبيقات: {e}")
        return

    # تصحيح: طباعة استجابة واجهة برمجة التطبيقات
    print(f"استجابة واجهة برمجة التطبيقات: {response}")


    # التحقق مما إذا كانت رسالة commit فارغة
    if not commit_message:
        print("خطأ: تم إنشاء رسالة commit فارغة. إلغاء الـ commit.")
        return

    # إجراء commit بالرسالة التي تم إنشاؤها
    subprocess.run(["git", "commit", "-m", commit_message], check=True)

    # دفع التغييرات
    if push:
        subprocess.run(["git", "push"], check=True)
    else:
        print("تم إجراء commit للتغييرات محليًا، ولكن لم يتم دفعها.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="إنشاء رسالة commit باستخدام الذكاء الاصطناعي وإجراء commit للتغييرات.")
    parser.add_argument('--no-push', dest='push', action='store_false', help='إجراء commit للتغييرات محليًا دون دفعها.')
    args = parser.parse_args()
    gitmessageai(push=args.push)
```

ثم، في ملف `~/.zprofile` الخاص بك، أضف ما يلي:

```
function gitpush {
  python ~/bin/gitmessageai.py
}

function gitcommit {
  python ~/bin/gitmessageai.py --no-push
}

alias gpa=gitpush
alias gca=gitcommit
```