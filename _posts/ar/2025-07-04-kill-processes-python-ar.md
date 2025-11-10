---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-code-fast-1
title: قتل العمليات باستخدام بايثون
translated: true
type: note
---

### استخدام Python لإنهاء العمليات على نظام Windows

لإنهاء العمليات برمجياً على نظام Windows، ستستخدم بشكل أساسي وحدة `subprocess` لاستدعاء أوامر النظام مثل `taskkill`. تركز وحدة `signal` على أنظمة Unix ولا تتعامل مع إنهاء العمليات بشكل موثوق على Windows (الإشارات مثل SIGKILL غير مدعومة أصلاً؛ يمكن للدالة `os.kill()` إرسال إشارات محدودة، لكنها ليست الخيار الأمثل لإنهاء العمليات بشكل كامل). يمكن لوحدة `platform` المساعدة في التأكد من أنك تعمل على نظام Windows للتعامل مع السلوك المحدد لهذا النظام.

#### الخطوة 1: تثبيت واستيراد الوحدات
- `subprocess`، `signal`، و `platform` هي جزء من المكتبة القياسية لـ Python، لذا لا حاجة للتثبيت.
- مثال على الاستيراد:

```python
import subprocess
import platform
import os  # للوصول إلى معرف العملية، إذا لزم الأمر
```

#### الخطوة 2: الكشف عن نظام التشغيل Windows (باستخدام `platform`)
- تأكد من البيئة لتجنب مشاكل التوافق بين الأنظمة:

```python
if platform.system() == 'Windows':
    print("Running on Windows - using compatible killing methods.")
```

#### الخطوة 3: إنهاء عملية
- لإنهاء عملية موجودة باستخدام معرف العملية (PID) أو اسمها، استخدم `taskkill` عبر `subprocess`. هذه هي الطريقة الموثوقة والأصلية لنظام Windows، حيث أن `subprocess.terminate()` أو `.kill()` تعمل فقط على العمليات التي قمت بتشغيلها باستخدام `subprocess.Popen`.
- مثال: إنهاء عملية باستخدام PID (بشكل قسري باستخدام الوسم `/F`). استبدل `1234` بـ PID الفعلي.

```python
def kill_process_by_pid(pid):
    try:
        subprocess.call(['taskkill', '/PID', str(pid), '/F'])
        print(f"Process {pid} terminated.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to kill process {pid}: {e}")

# الاستخدام
kill_process_by_pid(1234)
```

- إنهاء عملية باستخدام اسمها (مثال: 'notepad.exe')، مما ينهي جميع العمليات المطابقة:

```python
def kill_process_by_name(name):
    try:
        subprocess.call(['taskkill', '/IM', name, '/F'])
        print(f"Processes matching '{name}' terminated.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to kill processes '{name}': {e}")

# الاستخدام
kill_process_by_name('notepad.exe')
```

#### القيود والملاحظات
- تستدعي `subprocess` أوامر خارجية، لذا تأكد من أن البرنامج النصي لديه الأذونات المناسبة (مثال: التشغيل كمسؤول لعمليات النظام).
- بالنسبة للعملية التي تم تشغيلها عبر `subprocess.Popen`، استخدم `.terminate()` (إغلاق مهذب) أو `.kill()` (قسري) مباشرة:

```python
proc = subprocess.Popen(['notepad.exe'])  # التشغيل
proc.kill()  # إنهاؤها
```

- وحدة `signal`: استخدام `os.kill(pid, signal.SIGTERM)` قد يعمل لبعض الإشارات على Windows (Python 3.2+)، لكنه أقل موثوقية وقد لا ينهي جميع العمليات. مثال:

```python
import signal
os.kill(pid, signal.SIGTERM)  # قد يُغلق برفق؛ لكنه غير مضمون
```

تجنب الاعتماد على `signal` لإنهاء العمليات على Windows — التزم باستخدام `subprocess` مع `taskkill` للحصول على أفضل النتائج.

إذا كنت بحاجة إلى سرد PIDs (مثال: عبر أمر `tasklist`)، يمكنك الاستعلام عنها أولاً للإنهاء الديناميكي. للإدارة المتقدمة للعمليات، فكر في استخدام مكتبات خارجية مثل `psutil`، لكن الأمثلة أعلاه تستخدم الوحدات القياسية فقط.