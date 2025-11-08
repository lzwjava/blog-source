---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: إصلاح خطأ إصدار Protoc في بناء Substrait
translated: true
type: note
---

### فهم الخطأ

فشل البناء هذا يحدث في صندوق `substrait` (الإصدار 0.58.0)، الذي تعتمد عليه GreptimeDB لتخطيط الاستعلامات عبر اللغات. ينشأ الخطأ من رفض مترجم البروتوكول (`protoc`) لملف `substrait/algebra.proto` لأنه يستخدم حقول "اختيارية" في بناء جملة proto3 — وهي ميزة تتطلب إما:

- إصدار Protoc ≥3.21 (حيث يكون الدعم مستقرًا ولا حاجة إلى علم خاص)، أو
- إصدار protoc أقدم (مثل 3.15–3.20) مع تمرير علم `--experimental_allow_proto3_optional` أثناء الترجمة.

أداة `prost-build` في نص بناء `substrait` لا تمرر هذا العلم، لذا فهي تفترض إصدار protoc متوافق. إن `protobuf-compiler` الموجود على نظامك (المرجح من `apt` على Ubuntu 22.04 أو إصدار أقدم، والذي يعطي ~3.12.4) قديم جدًا ويخلو من هذا العلم، مما يتسبب في الذعر.

توثيق GreptimeDB يحدد protoc ≥3.15، ولكن لهذا التبعية، فإن ≥3.21 مطلوب بشكل فعال.

### الإصلاح السريع: ترقية Protoc إلى ≥3.21

أسهل طريقة، بدون صلاحيات الجذر، هي تنزيل وتثبيت إصدار الثنائي الرسمي (لا حاجة للترجمة). إليك الطريقة:

1. **تنزيل أحدث إصدار Protoc**:
   - اذهب إلى [إصدارات Protocol Buffers](https://github.com/protocolbuffers/protobuf/releases).
   - احصل على أحدث `protoc-<version>-linux-x86_64.zip` (مثل `protoc-28.1-linux-x86_64.zip` أو أي إصدار حالي — أي إصدار ≥3.21 سيعمل).
   - رابط مباشر كمثال (اضبط الإصدار):  
     `wget https://github.com/protocolbuffers/protobuf/releases/download/v27.3/protoc-27.3-linux-x86_64.zip`

2. **قم بتثبيته**:
   ```
   unzip protoc-*.zip -d protoc-install
   sudo mv protoc-install/bin/protoc /usr/local/bin/
   sudo chmod +x /usr/local/bin/protoc
   rm -rf protoc-install protoc-*.zip  # التنظيف
   ```

3. **التحقق**:
   ```
   protoc --version
   ```
   يجب أن يظهر الناتج `libprotoc 27.3` (أو أعلى). إذا كان لا يزال قديمًا، تحقق من المسار الخاص بك (`echo $PATH`) — يجب أن يأتي `/usr/local/bin` قبل `/usr/bin`.

4. **أعد محاولة البناء**:
   ```
   make clean  # يمسح الأهداف القديمة
   make
   ```

هذا يتجاوز `protoc` الخاص بالنظام دون التعارض مع حزم `apt`. إذا كنت تستخدم توزيعة جديدة مثل Ubuntu 24.04+، فإن `apt install protobuf-compiler` قد يعطي بالفعل ≥3.21 — تحقق مرة أخرى من إصدارك أولاً.

### إذا لم تتمكن من الترقية (حالات نادرة)
- إذا كنت عالقًا على نظام قديم، فستحتاج إلى تعديل `build.rs` الخاص بـ `substrait` لإضافة العلم (عبر `Command::new(protoc).arg("--experimental_allow_proto3_optional")`)، ولكن هذا يتطلب تفرعة للصندوق وتحديث `Cargo.toml` الخاص بـ GreptimeDB — أمر فوضوي وغير موصى به.
- بدلاً من ذلك، تقدم بعض الصناديق ميزة `protobuf-src` لتضمين إصدار protoc حديث، لكن `substrait` لا يفعلها افتراضيًا.

### نصائح إضافية
- تأكد من المتطلبات الأساسية الأخرى: `build-essential` (لـ GCC)، `libc6-dev` (رؤوس glibc).
- إذا نجح البناء لكنه فشل لاحقًا في تبعيات ++C (مثل Arrow)، قم بتثبيت `libarrow-dev` عبر conda أو apt.
- لـ CI/CD أو Docker: أضف خطوة التنزيل إلى بيئتك.

هذا يجب أن يحل المشكلة — `substrait` يترجم بنظافة في الإعدادات الحديثة. إذا واجهت مشكلة أخرى، شارك `protoc --version` والتوزيعة الخاصة بك.

[توثيق بناء GreptimeDB](https://github.com/GreptimeTeam/greptimedb#build-from-source)  
[إصدارات Protobuf](https://github.com/protocolbuffers/protobuf/releases)  
[الحقول الاختيارية في Proto3](https://protobuf.dev/programming-guides/proto3/#optional)