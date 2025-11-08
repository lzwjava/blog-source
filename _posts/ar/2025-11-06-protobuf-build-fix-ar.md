---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: إصلاح خطأ بناء مترجم البروتوبوف
translated: true
type: note
---

### فهم الخطأ

يحدث فشل البناء هذا أثناء تجميع Protocol Buffers (ملفات `.proto`) في crate `greptime-proto`. تتطلب سكريبت البناء (باستخدام `prost-build`) الثنائي `protoc` لتوليد كود Rust من تعريفات الـ proto هذه، لكنها لا تستطيع العثور عليه في نظامك. هذا إغفال شائع للمتطلبات الأساسية عند بناء مشاريع مثل GreptimeDB التي تعتمد على gRPC و protobuf للاتصال الداخلي.

ملفات `.proto` المذكورة (مثل `database.proto`، `health.proto`) هي تعريفات GreptimeDB الأساسية للبيانات الوصفية، المناطق، WAL، إلخ، لذا فإن تخطي هذه الخطوة يمنع البناء بالكامل.

### الإصلاح السريع

1.  **قم بتثبيت مترجم Protobuf** (الإصدار 3.15 أو أعلى مطلوب):
    *   على Debian/Ubuntu (يطابق تلميح الخطأ لديك):
        ```
        sudo apt update
        sudo apt install protobuf-compiler
        ```
    *   على Fedora/RHEL:
        ```
        sudo dnf install protobuf-compiler
        ```
    *   على macOS (إذا كان مطبقًا):
        ```
        brew install protobuf
        ```
    *   تنزيل يدوي (عبر المنصات): احصل على أحدث إصدار من [إصدارات Protocol Buffers](https://github.com/protocolbuffers/protobuf/releases)، وقم باستخراجه، وأضف `bin/protoc` إلى متغير البيئة PATH الخاص بك.

2.  **التحقق من التثبيت**:
    ```
    protoc --version
    ```
    يجب أن يظهر إخراجًا مشابهًا لـ `libprotoc 3.21.12` (أو أعلى؛ أي إصدار ≥ 3.15 يعمل).

3.  **أعد محاولة البناء**:
    ```
    make clean  # اختياري، لمسح أي آثار جزئية
    make
    ```
    إذا كان `protoc` مثبتًا ولكن لم يتم العثور عليه (مثلًا، مشكلة في PATH)، قم بتعيين متغير البيئة:
    ```
    export PROTOC=/usr/bin/protoc  # اضبط المسار حسب الحاجة
    make
    ```

### نصائح إضافية
*   تأكد من أن لديك المتطلبات الأساسية الأخرى: إصدار Rust الليلي (والذي يبدو أنك تملكه من الخطأ السابق)، GCC/G++ (قم بتثبيته عبر `sudo apt install build-essential`)، ورؤوس تطوير glibc (`sudo apt install libc6-dev`).
*   إذا كنت تعمل داخل حاوية أو بيئة مخصصة، أضف خطوة التثبيت هناك.
*   للاختبار بعد البناء: `cargo run --bin greptime -- standalone start`.

هذا يجب أن ينقلك من مرحلة تجميع الـ proto. إذا فشل في شيء آخر (مثل تبعات C++)، تحقق من جميع المتطلبات الأساسية.

### المراجع
*   [GreptimeDB GitHub: البناء من المصدر](https://github.com/GreptimeTeam/greptimedb#build-from-source)
*   [prost-build Docs: توفير Protoc](https://docs.rs/prost-build/#sourcing-protoc)