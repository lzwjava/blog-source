---
audio: false
generated: true
image: true
lang: ar
layout: post
title: كيف تشاهد يوتيوب على التلفزيون
translated: true
type: post
---

هذا الدليل يفترض أنك تمتلك بالفعل طريقة لتجاوز القيود الجغرافية. إليك كيفية مشاهدة YouTube على شاشتك التلفزيونية دون الحاجة إلى تثبيت firmware مخصص على الراوتر—فقط استخدم تطبيقًا.

---

## **SmartYouTubeTV**

![SmartYouTubeTV](assets/images/youtube-tv/smart.jpg)

1. **التنزيل والتثبيت**:
   قم بتنزيل التطبيق ثم تثبيته على التلفزيون باستخدام فلاشة USB.

2. **تكوين البروكسي**:
   - على عميل البروكسي الخاص بك (مثل Clash)، قم بتفعيل **"السماح بالاتصالات من الشبكة المحلية"** للسماح للأجهزة في الشبكة المحلية بتوجيه حركة المرور عبر جهازك.
   - في **SmartYouTubeTV**، انتقل إلى الإعدادات وأدخل تفاصيل البروكسي (مثل `192.168.1.3:7890`).
     *ملاحظة*: استخدم **SOCKS5** (فشلت بروكسيات HTTP في الاختبارات). استبدل `192.168.1.3` بعنوان IP المحلي لجهازك.

3. **الاختبار والتأكيد**:
   انقر على **"اختبار"** في التطبيق للتحقق من الاتصال. إذا نجحت العملية، احفظ الإعدادات وابدأ البث.

![إعداد البروكسي](assets/images/youtube-tv/proxy1.jpeg)
![نجاح](assets/images/youtube-tv/tan.jpeg)

---

## **gfreezy/seeker (بروكسي شفاف)**
مشروع على GitHub يحول جهاز الكمبيوتر الخاص بك إلى بوابة بروكسي باستخدام **TUN** (مشابه لوضعي Enhanced/Gateway في Surge). فيما يلي ملاحظات رئيسية وإعدادات تعمل:

### **التكوين (`config.yml`)**
```yml
verbose: true
dns_start_ip: 10.0.0.10
dns_servers:
  - 223.5.5.5:53
  - 114.114.114.114:53
dns_timeout: 1s
tun_name: utun4
tun_ip: 10.0.0.1
tun_cidr: 10.0.0.0/16
dns_listen: 0.0.0.0:53
gateway_mode: true
ping_timeout: 2s
probe_timeout: 30ms
connect_timeout: 1s
read_timeout: 30s
write_timeout: 5s
max_connect_errors: 2

servers:
  - name: http proxy server
   addr: 0.0.0.0:7890
   protocol: Http
  - name: https proxy server
   addr: 0.0.0.0:7890
   protocol: Https

rules:
  - 'MATCH,PROXY'
```

### **لماذا لا نستخدم SOCKS5؟**
في البداية، حاولت استخدام SOCKS5:
```yml
servers:
  - name: socks5 proxy server
   addr: 0.0.0.0:7891
   protocol: Socks5
```
لكنه تسبب في **حلقات اتصال** (وفقًا لـ [الوثائق](https://github.com/gfreezy/seeker))، مما يتطلب قواعد اتصال مباشرة صريحة للنطاقات. كانت بروكسيات **HTTP/HTTPS** أكثر استقرارًا.

### **المقايضات**
- **Seeker**: يتطلب جهازًا مخصصًا يعمل كراوتر.
- **وضع البروكسي (SmartYouTubeTV)**: مرن—يعمل مع الهواتف والأجهزة اللوحية التي تشارك منافذ البروكسي.

![Seeker](assets/images/youtube-tv/seeker.jpg)

---

## **لقطات شاشة التلفزيون (Xiaomi TV)**
لالتقاط لقطات الشاشة:
1. **اضغط مرتين على زر `Home`** في جهاز التحكم عن بعد لفتح مدير التطبيقات.
2. اختر **زر لقطات الشاشة** وشاركها عبر WeChat (أو تطبيقات أخرى).
3. استخدم هذه القائمة **لإغلاق التطبيقات المتجمدة قسريًا**.

![لقطات شاشة التلفزيون](assets/images/youtube-tv/tv_screen.jpeg)

---

استمتع بتجربة المشاهدة على الشاشة الكبيرة!

---

## **تحديث (سبتمبر 2025)**

دعمت Apple TV الآن برامج VPN بشكل أصلي. يمكنك تثبيت **Shadowrocket** للاتصال بخادم البروكسي الخاص بك وبث YouTube TV مباشرة.