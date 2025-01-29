---
audio: true
lang: ar
layout: post
title: حمولة هتزنر
translated: true
---

أنا محتمل جداً لمحاولة هذه المنصة السحابية الحديثة.

{: .centered }
![](assets/images/hertzner/h.jpg)
*مصدر: هتزنر*{: .caption }

خادم في هلسينكي مع تكوين 2 CPU AMD متعددة الوحدات المعالجة، 2 جيجابايت ذاكرة عشوائية، 40 جيجابايت SSD، و20 تيرابايت من الeiic يكلف 4.49 دولار أمريكي شهرياً.

عنوان IPv4 يكلف 50 سنت أمريكي إضافي شهرياً، مما يرفع الإجمالي إلى 5.09 دولار أمريكي شهرياً.

يوفرون الخدمات في ستة مواقع:

- نيورنبرغ، ألمانيا
- فالكنستاين، ألمانيا
- هلسينكي، فنلندا
- سنغافورة، سنغافورة
- هيلزبورو، أوريغون، ولايات المتحدة الأمريكية
- أشبورن، فيرجينيا، ولايات المتحدة الأمريكية

هو مثير للاهتمام أنهم لا يلتزمون بالاتجاهات لاختيار المواقع الشهيرة. مواقعهم مختلفة من مواقع Vultr أو Digital Ocean.

إعدادات حائط النار سهلة في الاستخدام. على الرغم من أن هذا كان أول مرة استخدامه، سهلت لي جعل تكوين الخادم المستعار بسرعة.

> sudo bash -c "$(wget -qO- https://raw.githubusercontent.com/Jigsaw-Code/outline-server/master/src/server_manager/install_scripts/install_server.sh)"

سرعة خادم هتزنر في هلسينكي سريعة جداً. باستخدام تطبيق iOS لSpeedtest، سرعة التحميل 423 ميجابايت بالثانية، وسرعة التحميل 56.1 ميجابايت بالثانية.

الرد في Shadowrocket 1175 ملي ثانية، ولكن هذا ليس مشكلة كبيرة.

برنامج أوليف بايثون بسيط لاسترجاع تفاصيل فرع الخادم.

```python
from hcloud import Client
import os

# احصل على مفتاح API من متغير البيئة
api_token = os.environ.get('HERTZNER_API_KEY')

إذا لم يكن:
    print("خطأ: لم يتم تعيين مفتاح API هتزنر لمتغير البيئة.")
    exit(1)

# إنشاء حالة عميل
client = Client(token=api_token)

# احصل على قائمة بجميع الخوادم
servers = client.servers.get_all()

# طباعة تفاصيل الخادم
لخادم في servers:
    print(f"معرف الخادم: {خادم.id}")
    print(f"اسم الخادم: {خادم.name}")
    print(f"حالة الخادم: {خادم.status}")
    print(f"IPv4 العامة: {خادم.public_net.ipv4.ip}")
    print(f"IPv6 العامة: {خادم.public_net.ipv6.ip}")
    print(f"نوع الخادم: {خادم.server_type.name}")
    print(f"موقع الخادم: {خادم.datacenter.location.name}")
    print("----------------------------------")

# إذا كنت تريد استرجاع خادم محدد بواسطة معرفه
خادم.id = '59402674'
خادم = client.servers.get_by_id(خادم.id)

print(f"معرف الخادم المحدد: {خادم.id}")
print(f"اسم الخادم المحدد: {خادم.name}")
print(f"حالة الخادم المحدد: {خادم.status}")
print(f"IPv4 العامة للخادم المحدد: {خادم.public_net.ipv4.ip}")
print(f"IPv6 العامة للخادم المحدد: {خادم.public_net.ipv6.ip}")
print(f"نوع الخادم المحدد: {خادم.server_type.name}")
print(f"موقع الخادم المحدد: {خادم.datacenter.location.name}")

```