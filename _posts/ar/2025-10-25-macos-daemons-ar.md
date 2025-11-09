---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: عمليات الخدمة الافتراضية في نظام ماك أو إس
translated: true
type: note
---

### عمليات Daemon الافتراضية في macOS

في نظام macOS، عمليات daemon هي خدمات خلفية تعمل بدون واجهة مستخدم، تبدأ عادةً أثناء التمهيد أو عند الطلب. تتم إدارتها بواسطة **launchd**، وهو إطار عمل تهيئة النظام وإدارة الخدمات (PID 1). تختلف عمليات daemon عن وكلاء المستخدم (agents): تعمل عمليات daemon كمسؤول/على مستوى النظام (قبل تسجيل الدخول)، بينما تعمل وكلاء المستخدم لكل مستخدم (بعد تسجيل الدخول).

يتم تعريف عمليات daemon الافتراضية للنظام في ملفات قائمة الخصائص (.plist) الموجودة في `/System/Library/LaunchDaemons/`. يوجد عادةً حوالي 300–350 منها في التثبيت القياسي (على سبيل المثال، 339 في macOS 10.14 Mojave)، وتغطي كل شيء من الشبكات والأمان إلى إدارة الأجهزة. توجد عمليات daemon المثبتة من قبل المستخدم أو الطرف الثالث في `/Library/LaunchDaemons/`.

#### كيفية عرض عمليات Daemon الافتراضية
لسرد جميع عمليات daemon (ووكلاء المستخدم) المحملة في Terminal:
- `sudo launchctl list` (تعرض عمليات daemon ووكلاء المستخدم على مستوى النظام).
- `launchctl list` (تعرض وكلاء المستخدم المخصصين للمستخدم فقط).

للحصول على قائمة كاملة بمحتويات الدليل: `ls /System/Library/LaunchDaemons/` (لا تتطلب sudo، لكن الملفات للقراءة فقط).

تخرج هذه الأوامر أعمدة مثل PID، والحالة، والتسمية (على سبيل المثال، `com.apple.timed`).

#### عملية Daemon "timed"
لقد ذكرت على وجه التحديد "timed"، والتي تشير إلى **com.apple.timed** (خادم مزامنة الوقت). هذه هي عملية daemon أساسية في النظام تم تقديمها في macOS High Sierra (10.13) لتحل محل عملية `ntpd` الأقدم.

- **الغرض**: تقوم بمزامنة ساعة النظام في جهاز Mac تلقائيًا مع خوادم NTP (بروتوكول وقت الشبكة) لضمان الدقة، حيث تستعلم عنها كل 15 دقيقة. يضمن هذا ضبط الوقت بدقة للسجلات والشهادات وعمليات الشبكة.
- **كيفية عملها**: يتم تشغيلها بواسطة launchd من `/System/Library/LaunchDaemons/com.apple.timed.plist`، وتعمل كمستخدم `_timed` (في مجموعتي `_timed` و `_sntpd`). تستخدم استدعاء النظام `settimeofday` لضبط الساعة بناءً على ردود الخادم. يوجد التكوين في `/etc/ntpd.conf` (خوادم NTP) ويتم تخزين الحالة مؤقتًا في `/var/db/timed/com.apple.timed.plist`.
- **مرتبط بـ**: يرتبط بإعدادات النظام > عام > التاريخ والوقت > "ضبط الوقت والتاريخ تلقائيًا". إذا تم تعطيل هذا الخيار، فلن تقوم `timed` بالمزامنة. للإعدادات المتقدمة (على سبيل المثال، احتياجات الدقة العالية)، يمكن لأدوات مثل Chrony أن تحل محلها ولكن يجب عندها تعطيل `timed`.

إذا انحرف توقيت ساعتك، تحقق من مشاكل الشبكة أو حظر الجدار الناري لـ NTP (منفذ UDP 123).

#### عمليات Daemon الافتراضية الشائعة الأخرى ("إلخ")
فيما يلي جدول لبعض عمليات daemon الافتراضية للنظام التي تعمل بشكل متكرر، مجمعة حسب الوظيفة. هذه القائمة ليست شاملة (هناك المئات)، لكنها تغطي الأساسيات. التسميات مأخوذة من أسماء ملفات .plist.

| الفئة       | تسمية Daemon                  | الوصف |
|----------------|-------------------------------|-------------|
| **النظام الأساسي** | `com.apple.launchd`          | عملية launchd نفسها؛ تبدأ جميع العمليات الأخرى. |
| **الوقت والمزامنة** | `com.apple.timed`             | مزامنة الوقت عبر NTP (كما هو مذكور أعلاه). |
| **إدارة المستخدم** | `com.apple.opendirectoryd`   | يتعامل مع حسابات المستخدمين والمجموعات وخدمات الدليل. |
| **إدارة المستخدم** | `com.apple.accounts`         | يدير حسابات المستخدمين والمصادقة. |
| **الشبكات** | `com.apple.mDNSResponder`    | Bonjour/mDNS لاكتشاف الشبكة المحلية (مثل AirDrop). |
| **الشبكات** | `com.apple.nesessionmanager` | إدارة امتدادات الشبكة و VPN. |
| **البلوتوث/اللاسلكي** | `com.apple.bluetoothd`      | التعامل مع أجهزة البلوتوث. |
| **iCloud/المزامنة** | `com.apple.cloudd`            | مزامنة بيانات iCloud والخدمات. |
| **الأمان**   | `com.apple.securityd`        | إدارة Keychain والمعلومات الاعتمادية (غالبًا ما يعمل كعميل مستخدم أيضًا). |
| **التحديثات**    | `com.apple.softwareupdated`  | يتعامل مع تحديثات البرامج وتنزيلات الكتالوجات. |
| **الأجهزة**   | `com.apple.kextd`             | تحميل إضافات النواة (Kernel extensions) وإدارتها. |
| **السجلات**    | `com.apple.systemnotificationd` | إشعارات النظام وتسجيل الأحداث. |
| **MDM (إذا كان مفعلًا)** | `com.apple.mdmclient`     | عميل Mobile Device Management للإعدادات المؤسسية. |

تعمل هذه العمليات باستمرار أو بناءً على محفزات للحفاظ على استقرار نظام macOS. إذا تسببت إحداها في مشكلة (مثل استخدام وحدة المعالجة المركزية بنسبة عالية)، يمكنك تفريغها مؤقتًا باستخدام `sudo launchctl unload /System/Library/LaunchDaemons/com.apple.example.plist`، لكن تجنب تعديل ملفات النظام.

للحصول على قائمة كاملة وحديثة على جهاز Mac الخاص بك (اعتبارًا من أكتوبر 2025، من المحتمل macOS 15 Sequoia أو إصدار لاحق)، قم بتشغيل الأوامر المذكورة أعلاه — فالإصدارات تتطور قليلاً مع التحديثات.

#### المراجع
- [The macOS Process Journey — “timed” (Time Sync Daemon)](https://medium.com/@boutnaru/the-macos-process-journey-timed-time-sync-daemon-4898c8185b4b)
- [Daemons and Agents could be slowing down your Mac](https://appleinsider.com/inside/macos/tips/daemons-and-agents-could-be-slowing-down-your-mac)
- [What files are included in the /System/Library/LaunchAgents and /System/Library/LaunchDaemons](https://apple.stackexchange.com/questions/361029/what-files-are-included-in-the-system-library-launchagents-and-system-library)
- [Script management with launchd in Terminal on Mac](https://support.apple.com/guide/terminal/script-management-with-launchd-apdc6c1077b-5d5d-4d35-9c19-60f2397b2369/mac)
- [How to show all running launchctl daemons/agents?](https://apple.stackexchange.com/questions/134817/how-to-show-all-running-launchctl-daemons-agents)