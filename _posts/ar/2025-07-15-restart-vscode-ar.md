---
audio: false
generated: false
image: false
lang: ar
layout: post
title: إدارة المدونات الآلية مع إعادة تشغيل VSCode
translated: true
type: post
---

النسخة التي قدمتها مصممة لتسهيل عملية نشر مقالات المدونات المسودة بطريقة منظمة. وهي مفيدة بشكل خاص للمدونين أو مصنعي المحتوى الذين يديرون مقالاتهم كمسودات قبل أن تكون جاهزة للنشر. إليك مقدمة موسعة لتوفير المزيد من السياق حول النص:

## المقدمة

إدارة مدونة أو أي موقع محتوى يعتمد على المحتوى غالبًا ما يتضمن إنشاء وتخزين المسودات قبل أن تكون جاهزة للنشر. هذا النص مصمم لتسهيل عملية نقل مقالات المسودات إلى دليل النشر المخصص، بشكل خاص لنظام توليد المواقع الثابتة، مثل تلك التي تستخدم Jekyll أو الإطارات المماثلة.

يؤدي النص المهام الرئيسية التالية:

```python
import os
import datetime
import glob
import shutil
import sys
import subprocess
import time

def publish_drafts_to_posts():
    """تحقق من ملفات المسودات التي تم إنشاؤها اليوم وتنقلها إلى دليل _posts/en."""
    today = datetime.date.today()
    date_str = today.strftime('%Y-%m-%d')

    drafts_dir = '_drafts'
    posts_en_dir = "original"

    if not os.path.exists(drafts_dir):
        print(f"دليل المسودات '{drafts_dir}' غير موجود. لا توجد ملفات للنشر.")
        return

    if not os.path.exists(posts_en_dir):
        os.makedirs(posts_en_dir)

    # نمط للعثور على الملفات في دليل المسودات التي تبدأ بتاريخ اليوم وتنتهي بـ -en.md
    pattern = os.path.join(drafts_dir, f"{date_str}-*-en.md")

    found_files = glob.glob(pattern)

    if not found_files:
        print(f"لم يتم العثور على أي ملفات مسودة في '{drafts_dir}' تبدأ بـ '{date_str}' للنشر.")
        return

    for file_path in found_files:
        file_name = os.path.basename(file_path)
        destination_path = os.path.join(posts_en_dir, file_name)

        try:
            shutil.move(file_path, destination_path)
            print(f"تم نقل '{file_name}' من '{drafts_dir}' إلى '{posts_en_dir}'.")
        except Exception as e:
            print(f"خطأ في نقل '{file_name}': {e}")

    restart_vscode()

def restart_vscode():
    print("إعادة تشغيل VSCode بطريقة لائقة لمنع إعادة إنشاء ملفات المسودات بشكل عرضي...")
    try:
        if sys.platform == 'win32':
            # إغلاق لائق دون /f
            os.system('taskkill /im Code.exe /t')
            time.sleep(3)  # تأخير للتطهير
            subprocess.Popen(['code', '.'])  # إعادة فتح
        elif sys.platform == 'darwin':
            # استخدام AppleScript للإغلاق اللائق
            os.system('osascript -e \'quit app "Visual Studio Code"\'')
            time.sleep(3)
            subprocess.call(['open', '-a', 'Visual Studio Code', '.'])
        elif sys.platform.startswith('linux'):
            # SIGTERM للإغلاق اللائق
            os.system('killall code')
            time.sleep(3)
            subprocess.Popen(['code', '.'])
        else:
            print("منصة غير مدعومة لإعادة تشغيل VSCode.")
    except Exception as e:
        print(f"خطأ أثناء إعادة التشغيل: {e}. يرجى إعادة تشغيل VSCode يدويًا.")

if __name__ == "__main__":
    publish_drafts_to_posts()
```