---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-code-fast-1
title: مراقبة إخراج العمليات الفرعية مع مهلة زمنية
translated: true
type: note
---

```python
import subprocess
import threading
import queue
import time
import sys

def read_output(proc, output_queue):
    """دالة مؤشر لقراءة stdout و stderr، ووضعها في قائمة الانتظار."""
    try:
        for line in iter(proc.stdout.readline, b''):
            if not line:
                break
            output_queue.put(line.decode('utf-8', errors='ignore').rstrip())
        # التحقق أيضًا من stderr إذا لزم الأمر
        for line in iter(proc.stderr.readline, b''):
            if not line:
                break
            output_queue.put(line.decode('utf-8', errors='ignore').rstrip())
    except Exception as e:
        output_queue.put(f"Error reading output: {e}")

def main():
    # الأمر المراد تنفيذه (مثل 'mvn clean compile' على Windows)
    cmd = ['mvn', 'clean', 'compile']  # اضبط حسب الحاجة، مثل ['cmd', '/c', 'mvn build']
    timeout_seconds = 10

    # بدء العملية الفرعية
    proc = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        bufsize=1,  # مخزن مؤقت للسطر
        universal_newlines=False,  # معالجة البايتات
        cwd=None  # تعيين دليل العمل إذا لزم الأمر
    )

    # قائمة الانتظار للمخرجات
    output_queue = queue.Queue()

    # بدء مؤشر لقراءة المخرجات
    output_thread = threading.Thread(target=read_output, args=(proc, output_queue))
    output_thread.daemon = True
    output_thread.start()

    print("بدأ الأمر. جاري المراقبة للمخرجات كل 10 ثوان...")

    while proc.poll() is None:
        try:
            # انتظار المخرجات مع انتهاء المهلة
            output = output_queue.get(timeout=timeout_seconds)
            print(f"Output: {output}")  # اختياري: طباعة أو معالجة المخرجات
        except queue.Empty:
            print(f"لا توجد مخرجات لمدة {timeout_seconds} ثانية. إنهاء الأمر والخروج.")
            proc.terminate()  # أو proc.kill() للإنهاء القسري
            try:
                proc.wait(timeout=5)  # الانتظار قليلاً للإغلاق الأنيق
            except subprocess.TimeoutExpired:
                proc.kill()
            sys.exit(1)

    # اكتملت العملية بشكل طبيعي
    print("اكتمل الأمر.")
    output_thread.join()  # انتظار انتهاء مؤشر المخرجات

if __name__ == "__main__":
    main()
```

### الشرح
- **العملية الفرعية**: يستخدم `subprocess.Popen` لتشغيل `mvn clean compile` (اضبط الأمر حسب الحاجة؛ بالنسبة لـ `mvn build` البسيط، قد يكون `['mvn', 'build']` أو ملفوفًا في `cmd /c` إذا لزم الأمر). يتم تشغيله بشكل غير متزامن مع أنابيب لـ stdout و stderr.
- **مؤشرات قائمة الانتظار**: يقرأ مؤشر منفصل من stdout و stderr سطرًا بسطر (لتجنب قراءة المخرجات بالكامل مرة واحدة)، يفك تشفيرها، ويضع الأسطر في `queue.Queue`. هذا يسمح بقراءات غير عائقية.
- **مراقبة انتهاء المهلة**: في المؤشر الرئيسي، تحقق من قائمة الانتظار للحصول على مخرجات جديدة باستخدام `get(timeout=10)`. إذا لم تصل أي مخرجات خلال 10 ثوان، قم بإنهاء العملية الفرعية واخرج.
- **التوافق مع Windows**: يعمل `subprocess` على Windows. إذا كان الأمر يتطلب shell (مثل `mvn` إذا لم يكن في PATH)، يمكنك تعيين `shell=True` وتمرير الأمر كسلسلة: `proc = subprocess.Popen("mvn clean compile", shell=True, ...)`.
- **الحالات الخاصة**: إذا انتهت العملية بشكل طبيعي أثناء الانتظار، تتوقف الحلقة وننضم إلى المؤشر. المؤشر هو daemonic لتجنب التعلق عند الخروج.
- **التخصيص**: يمكنك التعديل لمعالجة المخرجات بشكل مختلف (مثل التسجيل في ملف بدلاً من الطباعة). بالنسبة لـ stderr، يتم دمجه في نفس قائمة الانتظار؛ يمكنك الفصل إذا لزم الأمر. إذا كانت المخرجات ثنائية، فاضبط فك التشفير.