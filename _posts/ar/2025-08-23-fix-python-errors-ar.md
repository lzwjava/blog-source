---
audio: false
generated: true
image: false
lang: ar
layout: post
title: إصلاح أخطاء عدم العثور على بايثون بسهولة
translated: true
type: note
---

نعم — يحدث خطأ `"python not found"` لأن shell تسجيل الدخول الخاص بك قد لا يحتوي على نفس متغير البيئة `PATH` مثل shell التفاعلي الذي تكتب فيه `python` عادةً. عند استدعاء `subprocess.run(..., shell=True)`، قد لا يرى الـ subshell أمر `python` إذا لم يكن موجودًا في `$PATH` أو إذا كان نظامك يحتوي فقط على `python3`.

إليك الطرق الموثوقة لإصلاح ذلك:

---

### 1. استخدم `sys.executable`

بدلاً من الاعتماد على العثور على `python`، استدعِ مترجم Python قيد التشغيل حاليًا دائمًا:

```python
import os
import subprocess
import platform
import sys

def gpa():
    python_exec = sys.executable  # المسار الكامل لمترجم Python الحالي

    system = platform.system()
    if system == "Linux":
        shell_command = f"bash -l -c '{python_exec} ~/bin/gitmessageai.py --api deepseek --allow-pull-push'"
    elif system == "Darwin":
        shell_command = f"zsh -l -c '{python_exec} ~/bin/gitmessageai.py --api deepseek --allow-pull-push'"
    else:  # Windows
        shell_command = f'cmd.exe /c "{python_exec} %USERPROFILE%\\bin\\gitmessageai.py --api deepseek --allow-pull-push"'

    subprocess.run(shell_command, shell=True)
```

هذا يضمن أن نفس إصدار Python الذي استخدمته لتشغيل سكريبتك سيشغل أيضًا `gitmessageai.py`.

---

### 2. جرّب كلًا من `python` و `python3`

بعض الأنظمة تحتوي فقط على `python3`. يمكنك الكشف عن التوفر:

```python
import shutil

python_exec = shutil.which("python") or shutil.which("python3")
```

ثم استبدل ذلك في سلسلة الأمر الخاصة بك.

---

### 3. حدد مسارًا مطلقًا معروفًا

إذا كنت تعرف المسار المطلق (مثل `/usr/bin/python3` أو `/opt/homebrew/bin/python3`)، فيمكنك استخدامه مباشرة في أمرك.

---

👉 الحل الأكثر متانة هو **الخيار 1 (`sys.executable`)**، لأنه يستخدم المترجم الذي يشغل سكريبتك بالفعل. بهذه الطريقة، لا تعتمد أبدًا على `$PATH`.

هل تريد مني إعادة هيكلة الدالة الخاصة بك مع دمج `sys.executable` بالكامل حتى لا ترى خطأ `"python not found"` مرة أخرى؟