---
audio: false
generated: false
image: true
lang: ar
layout: post
title: عموم السحابة في هتزنر
translated: true
type: post
---

أنا محتاج جداً للتجربة هذه المنصة السحابية الحديثة.

{: .centered }
![](assets/images/hertzner/h.jpg)
*مصدر: هتزنر*{: .caption }

خادم في هلسنكي مع تكوين من 2 VCPUs AMD، 2GB RAM، 40GB SSD، و20TB من الترافيك يكلف 4.49 USD شهريا.

عنوان IPv4 يكلف 0.60 USD إضافي شهريا، مما يرفع الإجمالي إلى 5.09 USD شهريا.

يوفرون الخدمات في ست أماكن:

- نورنبرغ، ألمانيا
- فالكنستاين، ألمانيا
- هلسنكي، فنلندا
- سنغافورة، سنغافورة
- هلسبورو، أوريغون، الولايات المتحدة
- أشبرن، فيرجينيا، الولايات المتحدة

هو مثير للاهتمام أنهم لا يتبعون الأتراك لاختيار الأماكن الشهيرة. مواقعهم مختلفة عن مواقع Vultr أو Digital Ocean.

إعدادات حائط النار سهلة الاستخدام. رغم أنه كان ذلك أول مرة لي استخدامه، قمت بضبط التكوين الصحيح بسرعة لخادمي الوكيل.

> sudo bash -c "$(wget -qO- https://raw.githubusercontent.com/Jigsaw-Code/outline-server/master/src/server_manager/install_scripts/install_server.sh)"

سرعة خادم هتزنر في هلسنكي سريعة جداً. باستخدام التطبيق Speedtest على iOS، سرعة التحميل هي 423 Mbps، وسرعة التحميل هي 56.1 Mbps.

وقت الترابط في Shadowrocket هو 1175 ms، ولكن هذا ليس مشكلة كبيرة.

برنامج بايثون بسيط لاسترجاع تفاصيل فريق الخادم.

```python
from hcloud import Client
import os

# احصل على مفتاح API من المتغير البيئي
api_token = os.environ.get('HERTZNER_API_KEY')

إذا لم يكن هناك API_KEY:
    print("خطأ: لم يتم تحديد متغير البيئة HERTZNER_API_KEY.")
    exit(1)

# إنشاء مثيل عميل
client = Client(token=api_token)

# احصل على قائمة بجميع الخوادم
servers = client.servers.get_all()

# طباعة تفاصيل الخادم
لكل خادم في servers:
    print(f"معرف الخادم: {server.id}")
    print(f"اسم الخادم: {server.name}")
    print(f"حالة الخادم: {server.status}")
    print(f"IPv4 العام: {server.public_net.ipv4.ip}")
    print(f"IPv6 العام: {server.public_net.ipv6.ip}")
    print(f"نوع الخادم: {server.server_type.name}")
    print(f"موقع الخادم: {server.datacenter.location.name}")
    print("----------------------------------")

# إذا كنت تفضل استرجاع خادم بيئي بواسطة معرفه
server_id = '59402674'
server = client.servers.get_by_id(server_id)

print(f"معرف الخادم المحدد: {server.id}")
print(f"اسم الخادم المحدد: {server.name}")
print(f"حالة الخادم المحدد: {server.status}")
print(f"IPv4 العام للخادم المحدد: {server.public_net.ipv4.ip}")
print(f"IPv6 العام للخادم المحدد: {server.public_net.ipv6.ip}")
print(f"نوع الخادم المحدد: {server.server_type.name}")
print(f"موقع الخادم المحدد: {server.datacenter.location.name}")
```