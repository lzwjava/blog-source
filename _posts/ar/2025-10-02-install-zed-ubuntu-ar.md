---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-code-fast-1
title: تثبيت زيد على أوبونتو 24.04
translated: true
type: note
---

بالنسبة لأوبونتو 24.04 LTS، فإن طريقة التثبيت الأكثر مباشرة والرسمية لـ Zed (محرر الأكواد عالي الأداء) هي عبر البرنامج النصي (سكريبت) الذي يوفروه، والذي يعمل بشكل أصلي على معظم توزيعات لينكس بما في ذلك تلك المستندة إلى ديبيان مثل أوبونتو. فهو يتعامل مع التبعيات تلقائيًا ويضمن حصولك على أحدث إصدار مستقر.

### التثبيت الموصى به: البرنامج النصي الرسمي
شغّل هذا في طرفيتك:
```
curl -f https://zed.dev/install.sh | sh
```
- يقوم هذا بتثبيت Zed في المسار `~/.local/bin/zed` (أضفه إلى متغير البيئة PATH إذا لزم الأمر: `export PATH="$HOME/.local/bin:$PATH"` في ملف `~/.bashrc` أو ما شابه).
- المتطلبات الأساسية: يجب أن يفي نظامك (glibc 2.39 على النواة 6.14) بالمتطلبات (x86_64 glibc >= 2.31).
- بعد التثبيت، يمكنك تشغيله بـ `zed` أو من قائمة التطبيقات في GNOME.
- لقناة المعاينة (الإصدارات الليلية): `curl -f https://zed.dev/install.sh | ZED_CHANNEL=preview sh`.

إذا كنت تفضل حزمة عالمية معزولة (لا داعي للقلق بشأن التبعيات الأصلية)، استخدم خيار Flathub من قائمتك (`dev.zed.Zed`) عبر Flatpak:
1. قم بتثبيت Flatpak إذا لم يكن مثبتًا: `sudo apt update && sudo apt install flatpak`.
2. أضف مستودع Flathub: `flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo`.
3. قم بالتثبيت: `flatpak install flathub dev.zed.Zed`.
4. شغّل: `flatpak run dev.zed.Zed`.

البرنامج النصي بشكل عام أسرع وأكثر تكاملاً لسطح مكتب مثل GNOME، لكن Flatpak رائع إذا كنت تريد العزل أو إذا كنت تستخدمه بالفعل لتطبيقات أخرى. تجنب الخيارات الأخرى في قائمتك، لأنها مخصصة لتوزيعات لينكس غير المستندة إلى ديبيان ولن تعمل مباشرة على أوبونتو دون إعداد إضافي.

### المراجع
- [Zed Linux Installation Docs](https://zed.dev/docs/linux)
- [Zed on Linux Announcement](https://zed.dev/linux)
- [Repology Zed Packages](https://repology.org/project/zed-editor/versions)