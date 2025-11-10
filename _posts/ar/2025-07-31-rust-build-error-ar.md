---
audio: false
generated: true
image: false
lang: ar
layout: post
title: إصلاح خطأ الخصوصية في رست وتبسيط عملية البناء
translated: true
type: note
---

من رسائلك السابقة، أفهم أنك تواجه مشكلة في بناء وتشغيل مشروع Rust بسبب خطأ خصوصية (`E0603`) للدالة `run_simple` في الملف `simple.rs`. تسأل الآن حول "تسوية" أوامر `cargo build` و `cargo run` في `Cargo.tml` أو استكشاف طرق أخرى لتبسيط العملية. سأفسر هذا على أنه رغبة في تكوين مشروع Rust لتبسيط عملية البناء والتشغيل، وربما أتمتة العملية أو تخصيصها، وسأعالج أيضًا الخطأ السابق لضمان حل كامل.

### معالجة خطأ الخصوصية
أولاً، دعنا نحل خطأ `E0603` (`الدالة run_simple خاصة`) لضمان عمل `cargo build` و `cargo run`. بناءً على ناتج الخطأ:

- **إصلاح `simple.rs`**:
  افتح `src/simple.rs` واجعل الدالة `run_simple` عامة بإضافة `pub`:
  ```rust
  pub fn run_simple() {
      // الكود الحالي، مثال:
      println!("Hello from run_simple!");
  }
  ```

- **التحقق من `main.rs`**:
  تأكد من أن `src/main.rs` يشير إلى وحدة `simple` بشكل صحيح:
  ```rust
  mod simple;

  fn main() {
      simple::run_simple();
  }
  ```

- **تنظيف وإعادة البناء**:
  لتجنب بقايا البناء القديمة، نظف المشروع وأعد البناء:
  ```bash
  cargo clean
  cargo build
  ```

- **التشغيل**:
  إذا نجح البناء، شغّل البرنامج:
  ```bash
  cargo run
  ```

### "تسوية" `cargo build` و `cargo run` في `Cargo.toml`
عبارة "settle down it into Cargo.toml" توحي بأنك تريد تكوين مشروعك لتبسيط عملية البناء والتشغيل، ربما عن طريق تعريف سلوكيات مخصصة للبناء أو التشغيل في `Cargo.toml`. في Rust، يقوم `Cargo.toml` بشكل أساسي بتكوين بيانات وصف المشروع، التبعيات، وإعدادات البناء، لكنه لا يدمج أوامر مثل `cargo build` أو `cargo run` مباشرةً. بدلاً من ذلك، يمكنك:

1. **تحديد ثنائيات متعددة** (إذا كان `simple.rs` meant to be a منفذًا تنفيذيًا منفصلًا):
   إذا كان `simple.rs` meant to be a منفذًا تنفيذيًا قائمًا بذاته (وليس وحدة نمطية يستخدمها `main.rs`)، فيمكنك تكوينه في `Cargo.toml` تحت قسم `[[bin]]`. على سبيل المثال:
   ```toml
   [package]
   name = "example"
   version = "0.1.0"
   edition = "2024"

   [[bin]]
   name = "main"
   path = "src/main.rs"

   [[bin]]
   name = "simple"
   path = "src/simple.rs"
   ```
   - يخبر هذا Cargo أن مشروعك يحتوي على ثنائيين: واحد من `main.rs` (اسمه `main`) وواحد من `simple.rs` (اسمه `simple`).
   - ابنِ كلا الثنائيين:
     ```bash
     cargo build
     ```
   - شغّل ثنائيًا محددًا:
     ```bash
     cargo run --bin main
     cargo run --bin simple
     ```
   - تأكد من أن `simple.rs` يحتوي على دالة `main`:
     ```rust
     pub fn run_simple() {
         println!("Hello from run_simple!");
     }

     fn main() {
         run_simple();
     }
     ```

2. **إصلاح تحذير الإصدار**:
   أظهر الناتج السابق تحذيرًا حول أن ميزة `edition2024` غير ضرورية. حدّث `Cargo.toml` لاستخدام إصدار 2024 مباشرة:
   ```toml
   [package]
   name = "example"
   version = "0.1.0"
   edition = "2024"
   ```
   أزل أي سطر `cargo-features = ["edition2024"]` إذا كان موجودًا.

3. **نصوص البناء المخصصة** (متقدم):
   إذا كنت تريد أتمتة خطوات بناء محددة (مثل تشغيل أوامر مخصصة قبل أو بعد `cargo build`)، يمكنك استخدام نص بناء. أنشئ ملف `build.rs` في دليل المشروع الرئيسي:
   ```rust
   fn main() {
       println!("cargo:rerun-if-changed=src/simple.rs");
       // أضف منطق بناء مخصص هنا، مثال: إنشاء ملفات
   }
   ```
   أشر إليه في `Cargo.toml`:
   ```toml
   [package]
   name = "example"
   version = "0.1.0"
   edition = "2024"
   build = "build.rs"
   ```
   هذا لا يحل محل `cargo build` ولكنه يسمح بمهام مخصصة قبل البناء. ستظل تستخدم `cargo build` و `cargo run` كالمعتاد.

### طرق بديلة لتبسيط `cargo build` و `cargo run`
إذا كان هدفك هو تبسيط أو أتمتة تشغيل هذه الأوامر، فإليك طرقًا أخرى:

1. **الاختصارات في الطرفية**:
   أنشئ اختصارات في تكوين الطرفية الخاصة بك (مثل `~/.bashrc` أو `~/.zshrc`) لتقصير الأوامر:
   ```bash
   alias cb='cargo build'
   alias cr='cargo run'
   ```
   - احفظ وأعد تحميل الطرفية:
     ```bash
     source ~/.bashrc
     ```
   - ثم استخدم:
     ```bash
     cb
     cr
     ```

2. **Makefile**:
   أنشئ ملف `Makefile` في دليل المشروع الرئيسي لتعريف اختصارات:
   ```makefile
   build:
   	cargo build

   run:
   	cargo run

   clean:
   	cargo clean

   all: build run
   ```
   - شغّل:
     ```bash
     make build
     make run
     make all
     ```

3. **Cargo Watch** (للتطوير):
   استخدم `cargo-watch` لإعادة البناء والتشغيل تلقائيًا عند تغيير الملفات:
   - التثبيت:
     ```bash
     cargo install cargo-watch
     ```
   - التشغيل:
     ```bash
     cargo watch -x run
     ```
   - يراقب هذا التغييرات في `src/` ويعيد تشغيل `cargo run`.

4. **مهام VS Code** (إذا كنت تستخدم IDE):
   إذا كنت تستخدم Visual Studio Code، أنشئ ملف `.vscode/tasks.json`:
   ```json
   {
       "version": "2.0.0",
       "tasks": [
           {
               "label": "Build",
               "type": "shell",
               "command": "cargo build",
               "group": "build"
           },
           {
               "label": "Run",
               "type": "shell",
               "command": "cargo run",
               "group": "build"
           }
       ]
   }
   ```
   - شغّل المهام عبر Command Palette (`Ctrl+Shift+P` > "Tasks: Run Task").

5. **نصوص في `Cargo.toml`** (دعم محدود):
   Cargo لا يدعم بشكل أصلي اختصارات النصوص في `Cargo.toml`، ولكن يمكنك استخدام أداة مثل `cargo-xtask` أو تعريف النصوص في دليل `scripts` منفصل وتشغيلها يدويًا. للتبسيط، التزم باستخدام `Makefile` أو اختصارات الطرفية.

### الحل الموصى به
- **إصلاح الخطأ**: أضف `pub` إلى `run_simple` في `simple.rs` وتحقق من `main.rs`.
- **تكوين `Cargo.toml`**: استخدم أقسام `[[bin]]` إذا كنت تحتاج إلى ثنائيات متعددة، أو حافظ على البساطة بثنائي واحد في `main.rs`.
- **تبسيط الأوامر**: استخدم اختصارات الطرفية أو `Makefile` للراحة أثناء التطوير.

### مثال على الإعداد
**`Cargo.toml`**:
```toml
[package]
name = "example"
version = "0.1.0"
edition = "2024"
```

**`src/simple.rs`**:
```rust
pub fn run_simple() {
    println!("Hello from run_simple!");
}
```

**`src/main.rs`**:
```rust
mod simple;

fn main() {
    simple::run_simple();
}
```

**`Makefile`** (اختياري):
```makefile
build:
	cargo build

run:
	cargo run
```

- البناء والتشغيل:
  ```bash
  make build
  make run
  ```
  أو:
  ```bash
  cargo build
  cargo run
  ```

### استكشاف الأخطاء وإصلاحها
- إذا استمر خطأ الخصوصية، شارك محتويات `src/simple.rs` و `src/main.rs`.
- إذا كنت تقصد شيئًا محددًا بعبارة "settle down into Cargo.toml" (مثل نصوص تشغيل مخصصة أو ملفات تعريف)، فوضح ذلك، وسأخصص الحل accordingly.
- تحقق من إصدار Rust:
  ```bash
  rustc --version
  ```
  تأكد من أنه 1.85 أو أحدث لـ `edition = "2024"`.

أعلمني إذا كنت تحتاج إلى مزيد من التوضيح أو واجهت أخطاء جديدة!