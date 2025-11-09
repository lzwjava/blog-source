---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: نظرة عامة على مواصفات RFC 4122 للمعرفات الفريدة
translated: true
type: note
---

RFC 4122 هو مواصفة فنية نشرتها فرقة مهندسي الإنترنت (IETF) في يوليو 2005. وهو يُعرّف مساحة اسم Uniform Resource Name (URN) للمعرفات الفريدة عالمياً (UUIDs)، والتي تُعرف أيضاً باسم المعرفات الفريدة globally (GUIDs).

معرف UUID هو رقم 128-بت يُستخدم لتحديد المعلومات بشكل فريد في أنظمة الكمبيوتر دون الحاجة إلى سلطة مركزية لإدارة هذه المعرفات. توضح المواصفة خمس إصدارات من UUIDs (مثل الإصدار 1 المبني على الطابع الزمني وعنوان MAC، والإصدار 4 المبني على البتات العشوائية)، وطرق توليدها، وصيغ الترميز (مثل سلسلة الأرقام الست عشرية الشائعة ذات الشرطات: `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`)، والمبادئ التوجيهية لاستخدامها في البروتوكولات والتطبيقات. وهذا يضمن إمكانية التشغيل البيني عبر الأنظمة والشبكات المختلفة.

لقد تم اعتماد هذه المواصفة على نطاق واسع في تطوير البرمجيات لمهام مثل مفاتيح قواعد البيانات، ومعرفات الجلسات، والأنظمة الموزعة.

[ RFC 4122 - A Universally Unique IDentifier (UUID) URN Namespace](https://datatracker.ietf.org/doc/html/rfc4122)  
[ Universally unique identifier - Wikipedia](https://en.wikipedia.org/wiki/Universally_unique_identifier)