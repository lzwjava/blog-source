---
audio: false
generated: true
image: false
lang: ar
layout: post
title: تمكين الإصدار 2024 في رست
translated: true
type: note
---

يحدث هذا الخطأ لأن مشروع Rust الخاص بك يحاول استخدام ميزة `edition2024`، والتي لم يتم تثبيتها في إصدار Cargo الحالي لديك (1.75.0). لحل هذه المشكلة، تحتاج إلى تفعيل ميزة `edition2024` غير المستقرة بشكل صريح.

### خطوات الإصلاح:

1. **تمكين ميزة `edition2024`**:
   افتح ملف `Cargo.toml` الخاص بك وأضف السطر التالي في أعلى الملف، قبل قسم `[package]`:

   ```toml
   cargo-features = ["edition2024"]
   ```

   على سبيل المثال، قد يبدو ملف `Cargo.toml` الخاص بك هكذا:

   ```toml
   cargo-features = ["edition2024"]

   [package]
   name = "your_project_name"
   version = "0.1.0"
   edition = "2024"
   ```

2. **استخدام أداة Rust الليلة (Nightly)**:
   نظرًا لأن `edition2024` هي ميزة غير مستقرة، فأنت بحاجة إلى استخدام أداة Rust الليلة، حيث أن الإصدارات المستقرة (مثل 1.75.0) لا تدعمها. قم بتشغيل الأوامر التالية:

   ```bash
   rustup update nightly
   rustup override set nightly
   ```

   يقوم الأمر الأول بتحديث أداة الليلة، ويقوم الثاني بتعيين دليل مشروعك لاستخدام أداة الليلة.

3. **إعادة تشغيل عملية البناء**:
   بعد إجراء هذه التغييرات، حاول بناء مشروعك مرة أخرى:

   ```bash
   cargo build
   ```

### ملاحظات إضافية:
- ميزة `edition2024` هي ميزة تجريبية وقد تتغير. تحقق من وثائق Rust للحصول على تحديثات حول حالتها: [Rust Edition 2024](https://doc.rust-lang.org/nightly/cargo/reference/unstable.html#edition-2024).
- إذا كنت لا تحتاج إلى `edition2024`، يمكنك العودة إلى إصدار مستقر (مثل `edition = "2021"`) في ملف `Cargo.toml` لتجنب استخدام أداة الليلة.
- تأكد من أن `rustup` محدث لديك عن طريق تشغيل `rustup update`.

إذا واجهت المزيد من المشاكل، شارك محتويات ملف `Cargo.toml` الخاص بك أو أي رسائل خطأ جديدة للحصول على إرشادات أكثر تحديدًا.

[Rust Edition 2024](https://doc.rust-lang.org/nightly/cargo/reference/unstable.html#edition-2024)