---
audio: false
generated: true
image: false
lang: ar
layout: post
title: VPN على الآيفون وليس على نقطة الاتصال
translated: true
type: note
---

نعم، من المقبول عمومًا استخدام هاتف iPhone 14 Pro Max على بيانات الجيل الخامس الخلوية مع تطبيق VPN مثل Shadowrocket مفعل أثناء مشاركة نقطة اتصال شخصية مع جهاز Mac المحمول الخاص بك. لا يوجد عادةً تعارض inherent في هذا الإعداد، حيث أن iOS مصمم للتعامل مع كلا الميزتين في وقت واحد دون تعطيل أحدهما أو الآخر.

بخصوص سؤالك المحدد: حركة المرور من الأجهزة المتصلة بنقطة الاتصال الشخصية لهاتف iPhone (مثل جهاز Mac المحمول الخاص بك) لا يتم توجيهها عبر VPN المُكون على الـ iPhone نفسه. بدلاً من ذلك، تشارك نقطة الاتصال اتصال البيانات الخلوي raw مباشرة، متجاوزة نفق VPN. هذا يعني:
- تطبيقات الـ iPhone الخاصة بك وحركة مروره ستستخدم VPN (على سبيل المثال، وكيل أو نفق Shadowrocket).
- لكن حركة مرور الإنترنت لجهاز Mac المحمول ستذهب مباشرة عبر شبكة الجيل الخامس الخلوية دون تطبيق التشفير أو التوجيه الخاص بـ VPN.

إذا كنت تريد أن تستخدم حركة مرور الـ Mac أيضًا VPN، فستحتاج إلى إعداد واحد مباشرةً على الـ Mac نفسه.

[Does the VPN monitor my Hotspot traffic? - Accountable2You Support](https://support.accountable2you.com/article/791-faq-does-the-vpn-monitor-my-hotspot-traffic)  
[If I am connected to my phone's hotspot on my laptop and VPN is activated on the phone, does the laptop also get VPN security protection? - Quora](https://www.quora.com/If-I-am-connected-to-my-phones-hotspot-on-my-laptop-and-VPN-is-activated-on-the-phone-does-the-laptop-also-get-VPN-security-protection)  
[Why does shared WiFi connection from iPhone to laptop (personal hotspot) not go through VPN? - Apple Stack Exchange](https://apple.stackexchange.com/questions/400853/why-does-shared-wifi-connection-from-iphone-to-laptop-personal-hotspot-not-go)