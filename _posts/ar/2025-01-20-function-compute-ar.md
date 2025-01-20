---
audio: true
lang: ar
layout: post
title: Function Compute على Alibaba Cloud
translated: true
---

لقد قمت بإعداد وظيفة باستخدام خدمة Function Compute من Alibaba Cloud. هدفي هو توليد حركة مرور تبدو طبيعية للمساعدة في إخفاء نشاط خادم الوكيل الخاص بي من جدار الحماية العظيم (GFW). للقيام بذلك، قمت بنشر خادم عرض النطاق الترددي بجانب خادم الوكيل الخاص بي. الآن، أنا أستخدم Function Compute من Alibaba Cloud لإجراء طلب إلى واجهة برمجة التطبيقات (API) الخاصة بعرض النطاق الترددي كل دقيقة، مما يخلق مزيجًا من حركة المرور العادية وحركة المرور الخاصة بالوكيل.

```python
from flask import Flask, request, jsonify
import requests
import time

REQUEST_ID_HEADER = 'x-fc-request-id'

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def hello_world(path):
    # تسجيل معرف الطلب وتفاصيل أخرى
    rid = request.headers.get(REQUEST_ID_HEADER)
    print("FC Invoke Start RequestId: " + rid)
    data = request.stream.read()
    print("Path: " + path)
    print("Data: " + str(data))

    # تهيئة العدادات
    start_time = time.time()  # تسجيل وقت البدء
    duration = 60  # التشغيل لمدة دقيقة واحدة (60 ثانية)
    total_calls = 0  # تتبع إجمالي عدد الطلبات
    successful_calls = 0  # تتبع عدد الطلبات الناجحة

    # حلقة لمدة دقيقة واحدة
    while time.time() - start_time < duration:
        try:
            # استدعاء واجهة برمجة التطبيقات الخارجية /bandwidth
            response = requests.get('https://www.lzwjava.xyz/bandwidth')
            response.raise_for_status()  # إثارة استثناء في حالة وجود أخطاء HTTP
            successful_calls += 1  # زيادة عداد الطلبات الناجحة
        except Exception as e:
            print("Error fetching bandwidth data:", e)
        finally:
            total_calls += 1  # زيادة عداد إجمالي الطلبات

        # الانتظار لمدة 5 ثوانٍ قبل الطلب التالي
        time.sleep(5)

    # تسجيل نهاية الطلب
    print("FC Invoke End RequestId: " + rid)

    # إرجاع عدد الطلبات والطلبات الناجحة
    return jsonify({
        "message": "Hello, World!",
        "total_calls": total_calls,
        "successful_calls": successful_calls
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
```