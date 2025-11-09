---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: مراقبة نشاط الشبكة بصلاحيات المسؤول
translated: true
type: note
---

### مراقبة طلبات HTTP واتصالات TCP بصلاحيات المسؤول

بافتراض أنك تعمل على نظام شبيه بـ Linux/Unix (مثل Ubuntu أو CentOS) مع صلاحيات الجذر/المسؤول، يمكنك مراقبة نشاط الشبكة بشكل أخلاقي لاستكشاف الأخطاء وإصلاحها، أو التدقيق الأمني، أو اختبار الاختراق. **مهم: افعل هذا فقط على الأنظمة التي تملكها أو لديك إذن صريح للعمل عليها — فالمراقبة غير المصرح بها غير قانونية.** سأركز على أدوات سطر الأوامر، فهي خفيفة الوزن ولا تتطلب واجهة رسومية.

#### 1. **مراقبة جميع اتصالات TCP**
   استخدم الأدوات المدمجة مثل `ss` (البديل الحديث لـ `netstat`) أو `tcpdump` للالتقاط الفوري. هذه تُظهر الاتصالات النشطة والمنافذ والعمليات.

   - **سرد جميع اتصالات TCP الحالية (عرض ثابت):**
     ```
     sudo ss -tunap
     ```
     - `-t`: TCP فقط.
     - `-u`: UDP إذا لزم الأمر (لكنك طلبت TCP).
     - `-n`: منافذ رقمية (بدون حل DNS).
     - `-a`: جميع الحالات (مثبتة، مستمعة، إلخ).
     - `-p`: عرض العمليات المالكة.
     مثال على الناتج:
     ```
     tcp   ESTAB  0      0      192.168.1.10:80     10.0.0.5:54321    users:(("nginx",pid=1234,fd=5))
     ```
     للمقابس المستمعة فقط: `sudo ss -tlnp`.

   - **المراقبة الفورية مع watch:**
     ```
     watch -n 1 'sudo ss -tunap'
     ```
     يتم التحديث كل ثانية.

   - **التقاط حركة TCP مباشرة (ع مستوى الحزمة):**
     قم بتثبيت `tcpdump` إذا لم يكن موجودًا: `sudo apt update && sudo apt install tcpdump` (Debian/Ubuntu) أو `sudo yum install tcpdump` (RHEL/CentOS).
     ```
     sudo tcpdump -i any tcp -n -v
     ```
     - `-i any`: جميع الواجهات.
     - `-n`: بدون حل الأسماء.
     - `-v`: مفصل.
     أضف `port 80 or port 443` لتصفية HTTP/HTTPS: `sudo tcpdump -i any tcp port 80 or tcp port 443 -n -v -A` (`-A` للحصول على الحمولة ASCII، لرؤية عناوين HTTP).

     احفظ في ملف للتحليل لاحقًا: `sudo tcpdump -i any tcp -w capture.pcap`.

#### 2. **مراقبة سجلات طلبات HTTP**
   تعتمد سجلات HTTP على خادم الويب الخاص بك (Apache، Nginx، إلخ). إذا لم يكن هناك خادم ويب قيد التشغيل، استخدم الالتقاط الشبكي (أعلاه) لفحص حركة HTTP. للسجلات الخاصة بالخادم:

   - **Apache (httpd):**
     توجد السجلات عادة في `/var/log/apache2/access.log` (Ubuntu) أو `/var/log/httpd/access_log` (CentOS).
     ```
     sudo tail -f /var/log/apache2/access.log
     ```
     - يُظهر الطلبات في الوقت الفعلي: IP، الطابع الزمني، الطريقة (GET/POST)، URL، رمز الحالة.
     مثال على السطر: `192.168.1.100 - - [08/Oct/2025:10:00:00 +0000] "GET /index.html HTTP/1.1" 200 1234`.

     لجميع السجلات: `sudo grep "GET\|POST" /var/log/apache2/access.log | less`.

   - **Nginx:**
     السجلات في `/var/log/nginx/access.log`.
     ```
     sudo tail -f /var/log/nginx/access.log
     ```
     تنسيق مشابه لـ Apache.

   - **إذا لم يكن هناك خادم ويب (التقاط HTTP عام):**
     استخدم `tcpdump` كما هو مذكور أعلاه مع `-A` لتفريغ حمولات HTTP، أو قم بتثبيت `ngrep للمطابقة باستخدام التعبيرات النمطية:
     ```
     sudo apt install ngrep  # قم بالتثبيت إذا لزم الأمر
     sudo ngrep -d any 'GET|POST|HTTP' -O http_capture.pcap
     ```
     هذا يقوم بتصفية وتسجيل طرق HTTP.

   - **متقدم: إعداد وكيل شفاف للتسجيل الكامل.**
     قم بتثبيت وكيل Squid: `sudo apt install squid`.
     قم بتكوين `/etc/squid/squid.conf` لتسجيل جميع HTTP (أضف `access_log /var/log/squid/access.log squid`).
     إعادة توجيه حركة المرور عبر iptables: `sudo iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j REDIRECT --to-port 3128`.
     ثم تابع سجل Squid: `sudo tail -f /var/log/squid/access.log`.

#### نصائح لـ "الاختراق" (اختبار الاختراق الأخلاقي)
- **اجمع بين الأدوات:** استخدم pipe مع `grep` للبحث عن أنماط محددة، مثال: `sudo tcpdump -i any tcp port 80 -A | grep "User-Agent"`.
- **تصور باستخدام Wireshark:** للتحليل بواجهة رسومية، قم بتثبيت Wireshark (`sudo apt install wireshark`)، وقم بتشغيله كمسؤول، وافتح ملف `.pcap` الخاص بك.
- **تعزيز الأمان:** بعد المراقبة، امسح السجلات إذا كانت تحتوي على بيانات حساسة: `sudo truncate -s 0 /var/log/access.log`.
- **ملاحظة حول المنصات المختلفة:** على Windows (مع صلاحيات المسؤول)، استخدم `netstat -anob` لـ TCP و Event Viewer للسجلات. على macOS، استخدم `netstat -an` و `tcpdump`.

هذا الإعداد يمنحك رؤية شاملة بدون أدوات خارجية. اختبر في جهاز ظاهري أولاً.

[Linux ss Command Man Page](https://man7.org/linux/man-pages/man8/ss.8.html)  
[Tcpdump Tutorial](https://www.tcpdump.org/manpages/tcpdump.1.html)  
[Apache Access Log Format](https://httpd.apache.org/docs/2.4/logs.html)