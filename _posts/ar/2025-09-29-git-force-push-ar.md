---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-code-fast-1
title: دفع جيت القسري عبر حذف الفرع
translated: true
type: note
---

```python
#!/usr/bin/env python3
"""
git_force_push.py

هذا النص ينفذ "دفع قسري" عن طريق حذف الفرع البعيد أولاً،
ثم دفع الفرع المحلي. يعمل هذا إذا كان المستودع يسمح بحذف الفروع
ولكن لا يسمح بالدفع القسري.

الاستخدام: python git_force_push.py <remote> <branch>
مثال: python git_force_push.py origin main

ملاحظة: يفترض هذا أن لديك الصلاحيات الكافية وأن الحذف مسموح به.
كن حذرًا، لأن حذف فرع يمكن أن يؤدي إلى فقدان commits.
"""

import subprocess
import sys

def run_command(command):
    """ينفذ أمر shell ويعيد مخرجاته."""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"خطأ في تنفيذ الأمر '{command}': {e}")
        print(f"Stderr: {e.stderr}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("الاستخدام: python git_force_push.py <remote> <branch>")
        sys.exit(1)

    remote = sys.argv[1]
    branch = sys.argv[2]

    # حذف الفرع البعيد
    delete_cmd = f"git push {remote} :{branch}"
    print(f"جاري حذف الفرع البعيد: {delete_cmd}")
    run_command(delete_cmd)

    # دفع الفرع المحلي
    push_cmd = f"git push {remote} {branch}"
    print(f"جاري دفع الفرع المحلي: {push_cmd}")
    run_command(push_cmd)

    print("تم الدفع القسري بنجاح.")
```

### آلية العمل
- **خطوة الحذف**: ينفذ `git push origin :main` لحذف الفرع البعيد (كما هو مسموح في مستودعك).
- **خطوة الدفع**: ينفذ `git push origin main` لدفع الفرع المحلي، مما يعيد إنشائه من جديد على البعيد.
- يحقق هذا بشكل فعال دفعًا قسريًا عن طريق تجاهل السجل البعيد واستبداله بالسجل المحلي.
- **ملاحظات الأمان/الاستخدام**: اختبر في مستودع غير حاسم أولاً. يتطلب هذا إعداد Git مناسبًا والصلاحيات الكافية. إذا كان المستودع يحتوي على حماية إضافية (عبر hooks مثلًا)، فقد يفشل. لا توجد ضمانات؛ عمليات Git يمكن أن تكون مدمرة.