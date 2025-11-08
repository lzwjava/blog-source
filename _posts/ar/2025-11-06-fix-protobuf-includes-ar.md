---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: إصلاح ملفات تضمين بروتوبوف المفقودة
translated: true
type: note
---

### فهم الخطأ

يحدث هذا الفشل في `greptime-proto` (المثبت عند commit `14b9dc40` من مستودع GreptimeTeam) أثناء تجميع protobuf. على وجه التحديد، لا يستطيع `protoc` العثور على النوع القياسي المعروف من جوجل `google/protobuf/duration.proto` (ومن المحتمل وجود ملفات أخرى مثل `timestamp.proto`). يؤدي هذا إلى حدوث أخطاء متتالية في الاستيراد في ملفات protos الخاصة بـ GreptimeDB (على سبيل المثال، `ddl.proto` تستورد Duration، مما يتسبب في أخطاء نوع غير معرّف في `database.proto`).

السبب الجذري: تثبيت `protoc` الخاص بك (من التحديث اليدوي) يتضمن فقط الملف الثنائي (`/usr/local/bin/protoc`)، ولكن ليس ملفات التضمين التي تحتوي على ملفات proto الأساسية من جوجل. تقوم `prost-build` في `build.rs` التابع للـ crate بتشغيل `protoc` بدون تعيين `--proto_path` بشكل صريح ليوجه إلى ملفات التضمين الخاصة بجوجل، لذا يفشل في عمليات الاستيراد النسبية مثل `"google/protobuf/duration.proto"`.

هذا شائع مع التثبيتات الثنائية فقط لـ protobuf؛ حيث يوفر الـ SDK الكامل `/usr/include/google/protobuf/` (أو ما يعادلها).

### الإصلاح السريع: تثبيت ملفات التضمين Protobuf

نظرًا لأن لديك بالفعل ملف `protoc` ثنائي حديث، أضف ملفات التضمين المفقودة دون الرجوع إلى إصدار أقدم:

1.  **تنزيل إصدار Protobuf الكامل** (مطابق لإصدار protoc الخاص بك، على سبيل المثال، 27.3 أو الأحدث):
    ```
    wget https://github.com/protocolbuffers/protobuf/releases/download/v27.3/protoc-27.3-linux-x86_64.zip
    unzip protoc-27.3-linux-x86_64.zip -d protoc-full
    ```

2.  **تثبيت ملفات التضمين**:
    ```
    sudo mkdir -p /usr/local/include/google/protobuf
    sudo cp -r protoc-full/include/google /usr/local/include/
    sudo chmod -R a+r /usr/local/include/google/protobuf  # التأكد من إمكانية القراءة
    rm -rf protoc-full protoc-*.zip  # التنظيف
    ```

3.  **التحقق**:
    *   تحقق من protoc: `protoc --version` (يجب أن يكون ≥3.21).
    *   اختبر ملفات التضمين: `ls /usr/local/include/google/protobuf/duration.proto` (يجب أن يكون الملف موجودًا).
    *   اختبر سريعًا: `protoc --proto_path=/usr/local/include proto/greptime/v1/ddl.proto --decode_raw=stdin < /dev/null` (من دليل مشروعك؛ تجاهل الناتج، فقط تحقق من عدم ظهور "File not found").

4.  **أعد المحاولة في عملية البناء**:
    ```
    make clean  # يمسح عمليات البناء الجزئية
    make
    ```

إذا كنت تستخدم توزيعة تدعم `apt` (مثل Ubuntu)، فإن البديل هو `sudo apt install libprotobuf-dev` — ولكن هذا قد يثبت إصدارًا أقدم (مثل 3.12)، مما يتعارض مع إعداد `protoc` اليدوي الخاص بك. إذا حدث ذلك، التزم بنسخ ملفات التضمين يدويًا وعيّن `PROTOC=/usr/local/bin/protoc` بشكل صريح.

### نصائح إضافية
*   إذا استمرت الأخطاء (على سبيل المثال، ملفات proto أخرى مفقودة مثل `wrappers.proto`)، فإن نسخ `include/google/` الكامل يجب أن يغطيها.
*   لعمليات البناء داخل الحاويات (Docker)، أضف هذه الخطوات إلى Dockerfile الخاص بك.
*   بعد البناء، اختبر باستخدام `cargo run --bin greptime -- standalone start` للتأكد من دمج ملفات proto بشكل صحيح.
*   هذا المراجعة لـ greptime-proto حديثة (تقريبًا أكتوبر 2024)؛ إذا استمرت المشاكل، تحقق من وجود إصلاحات upstream في المستودع.

[مستندات بناء GreptimeDB](https://github.com/GreptimeTeam/greptimedb#build-from-source)  
[الأنواع المعروفة في Protobuf](https://protobuf.dev/reference/protobuf/google.protobuf/)