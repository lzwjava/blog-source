---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: تتبع المسار غير مثبت افتراضياً
translated: true
type: note
---

تتبع المسار (Traceroute) متوفر بالتأكيد على Linux—فهو أداة تشخيص شبكة قياسية تتبع المسار الذي تسلكه الحزم للوصول إلى الوجهة. ومع ذلك، غالبًا **لا يتم تثبيته افتراضيًا** في العديد من التوزيعات الحديثة (مثل Ubuntu، أو Fedora، أو التثبيت الأدنى لـ Debian) للحفاظ على خفة الأنظمة الأساسية. هذا هو السبب في أنه لا يظهر في إكمال التبويب (tab completion) عند كتابة "trac".

### حل سريع
قم بتثبيته عبر مدير الحزم الخاص بك:
-   **Debian/Ubuntu**: `sudo apt update && sudo apt install traceroute`
-   **Fedora/RHEL/CentOS**: `sudo dnf install traceroute` (أو `sudo yum install traceroute` على الإصدارات القديمة)
-   **Arch**: `sudo pacman -S traceroute`

بمجرد التثبيت، يجب أن تضغط `trac` + Tab الآن تتضمن `traceroute` في القائمة. يمكنك بعد ذلك تشغيله مثل `traceroute example.com` للاختبار.

إذا كنت تستخدم إعدادًا حاويًا أو شديد التبسيط (مثل Alpine Linux)، فقد يستخدم `tr` كاسم مستعار أو يتطلب حزمة مختلفة—أخبرني باسم التوزيعة التي تستخدمها لمزيد من التفاصيل!