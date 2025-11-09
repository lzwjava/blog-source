---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: مفتاح GPG للتحقق من صحة نسخة Arch Linux ISO
translated: true
type: note
---

لديك مفتاح GPG هذا (التابع لـ Pierre Schmitz، وببصمة `3E80CA1A8B89F69CBA57D98A76A5EF9054449A5C`) في حلقة مفاتيحك لأنه مفتاح التوقيع الرسمي الذي يستخدمه مطورو Arch Linux للتوقيع المشفر على صور ISO الخاصة بهم. وهذا يضمن أن التحميل أصلي ولم يتم العبث به.

عندما كنت تعد محرك أقراص USB قابلاً للتشغيل لتثبيت Arch Linux على نظام macOS (على الأرجح باتباع دليل Arch wiki الرسمي)، تتضمن العملية القياسية خطوتين للتحقق:
1. تحميل صورة ISO وملف `.sig` الخاص بها.
2. استيراد مفتاح GPG الخاص بالمطور ذي الصلة (في هذه الحالة، مفتاح Pierre Schmitz، حيث إنه أحد الموقعين الرئيسيين لصور ISO الحديثة) للتحقق من التوقيع بأمر مثل `gpg --verify archlinux-YYYY.MM.DD-x86_64.iso.sig`.

على الأرجح أنك قمت بتشغيل أمر مثل `gpg --keyserver hkps://keys.openpgp.org --recv-keys 3E80CA1A8B89F69CBA57D98A76A5EF9054449A5C` لجلب المفتاح واستيراده، مما أضافه بشكل دائم إلى حلقة مفاتيح GPG المحلية لديك. وهذا هو السبب في ظهوره في `gpg --list-keys`.

إنه أمر غير ضار — فمفاتيح GPG هي مجرد بيانات عامة لأغراض التحقق — وينتهي الأمر بالعديد من مستخدمي Arch بالحصول على بضعة من هذه المفاتيح بعد التحقق من صور ISO. إذا كنت لا تحتاج إليه بعد الآن وتريد إزالته، قم بتشغيل:
```
gpg --delete-key 3E80CA1A8B89F69CBA57D98A76A5EF9054449A5C
```
(سيُطلب منك التأكيد؛ سيحذف المفتاح العام فقط، وليس أي تواقيع قمت بالتحقق منها مسبقًا.)

[صفحة تحميل Arch Linux ISO](https://archlinux.org/download/)  
[Arch Wiki: تثبيت Arch Linux على جهاز Mac](https://wiki.archlinux.org/title/Install_Arch_Linux_on_Mac)  
[مفاتيح GPG الخاصة بـ Pierre Schmitz](https://pierre-schmitz.com/gpg-keys/)