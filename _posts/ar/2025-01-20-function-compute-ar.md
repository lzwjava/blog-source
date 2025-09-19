---
audio: false
generated: false
image: false
lang: ar
layout: post
title: Function Compute على Alibaba Cloud
translated: true
---

أستخدم Function Compute من Alibaba Cloud لتوليد حركة مرور تبدو طبيعية، مما يساعد في إخفاء نشاط خادم الوكيل الخاص بي من جدار الحماية العظيم (GFW). لقد نشرت خادمًا للنطاق الترددي بجانب خادم الوكيل الخاص بي، وتقوم وظيفة Function Compute هذه بطلب واجهة برمجة تطبيقات النطاق الترددي كل دقيقة. هذا يخلق مزيجًا من حركة المرور العادية وحركة المرور عبر الوكيل.

```python
from flask import Flask, request, jsonify
import requests
import concurrent.futures

REQUEST_ID_HEADER = 'x-fc-request-id'

app = Flask(__name__)

# وظيفة لاستدعاء واجهة برمجة التطبيقات الخارجية
def call_bandwidth_api():
    try:
        response = requests.get('https://www.lzwjava.xyz/bandwidth')
        response.raise_for_status()  # إثارة استثناء لأخطاء HTTP
        return True  # الإشارة إلى النجاح
    except Exception as e:
        print("خطأ في جلب بيانات النطاق الترددي:", e)
        return False  # الإشارة إلى الفشل

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def hello_world(path):
    # تسجيل معرف الطلب وتفاصيل أخرى
    rid = request.headers.get(REQUEST_ID_HEADER)
    print("بدء استدعاء FC RequestId: " + rid)
    data = request.stream.read()
    print("المسار: " + path)
    print("البيانات: " + str(data))

    # تهيئة العدادات
    total_calls = 10  # العدد الإجمالي لاستدعاءات واجهة برمجة التطبيقات
    successful_calls = 0  # تتبع الاستدعاءات الناجحة

    # استخدام ThreadPoolExecutor لاستدعاء واجهة برمجة التطبيقات 10 مرات بشكل متزامن
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # إرسال المهام إلى المنفذ
        futures = [executor.submit(call_bandwidth_api) for _ in range(total_calls)]

        # انتظار انتهاء جميع المهام وعد النجاحات
        for future in concurrent.futures.as_completed(futures):
            if future.result():  # إذا كانت الاستدعاء ناجحًا
                successful_calls += 1

    # تسجيل نهاية الطلب
    print("نهاية استدعاء FC RequestId: " + rid)

    # إرجاع عدد الاستدعاءات والاستدعاءات الناجحة
    return jsonify({
        "message": "مرحبًا بالعالم!",
        "total_calls": total_calls,
        "successful_calls": successful_calls
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
```