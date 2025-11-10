---
audio: false
generated: true
image: false
lang: ar
layout: post
title: تكرار تشغيل الشحنات
translated: true
type: note
---

أنت محق تمامًا! في مثال `Makefile` الخاص بك:

```makefile
run:
	cargo build
	cargo run
```

تضمين `cargo build` قبل `cargo run` هو أمر زائد عن الحاجة لأن `cargo run` يتضمن بالفعل خطوة البناء. عند تنفيذ `cargo run`، يقوم Cargo تلقائيًا بالتحقق مما إذا كان المشروع يحتاج إلى إعادة بناء (على سبيل المثال، إذا كانت الملفات المصدرية قد تغيرت)، وإذا لزم الأمر، يقوم بتجميع المشروع قبل تشغيل الملف الثنائي الناتج. هذا يجعل خطوة `cargo build` الصريحة غير ضرورية في هذا السياق.

### توضيح
- **`cargo run`**:
  - يجمع بين `cargo build` (يجمّع المشروع إلى `target/debug/<project_name>`) ثم يشغل الملف الثنائي.
  - يعيد البناء فقط إذا كانت هناك تغييرات في الكود المصدري أو التبعيات.
- **`cargo build`**:
  - يجمّع المشروع فقط دون تشغيل الملف الثنائي.
  - مفيد إذا كنت تريد التحقق من التجميع دون تنفيذ البرنامج.

### إصلاح `Makefile`
لتبسيط `Makefile` الخاص بك، يمكنك إزالة `cargo build` الزائد:

```makefile
run:
	cargo run
```

يحقق هذا نفس النتيجة: يتم بناء المشروع (إذا لزم الأمر) ثم تنفيذه.

### متى تستخدم `cargo build` بشكل منفصل
قد ترغب في الاحتفاظ بـ `cargo build` كهدف منفصل في `Makefile` للحالات التي تريد فيها التجميع فقط دون التشغيل، مثل:
- التحقق من أخطاء التجميع.
- تحضير الملفات الثنائية للنشر أو الاختبار دون التنفيذ.

على سبيل المثال:

```makefile
build:
	cargo build

run:
	cargo run

clean:
	cargo clean
```

- شغّل `make build` للتجميع فقط.
- شغّل `make run` للبناء (إذا لزم الأمر) والتشغيل.
- شغّل `make clean` لمسح نواتج البناء.

### معالجة السياق السابق الخاص بك
بما أنك تعمل على مشروع Rust حيث `main.rs` يستدعي `run_simple` من `simple.rs`، تأكد من حل خطأ الخصوصية (`E0603`) عن طريق جعل `run_simple` عامًا في `src/simple.rs`:

```rust
pub fn run_simple() {
    println!("Hello from run_simple!");
}
```

وفي `src/main.rs`:

```rust
mod simple;

fn main() {
    simple::run_simple();
}
```

أيضًا، قم بتحديث `Cargo.toml` لإزالة تحذير `edition2024` كما نوقش سابقًا:

```toml
[package]
name = "example"
version = "0.1.0"
edition = "2024"
```

### اختبار الإعداد
1. قم بتحديث `Makefile` كما هو موضح أعلاه.
2. شغّل:
   ```bash
   make run
   ```
   سينفذ هذا `cargo run`، والذي سيبني (إذا لزم الأمر) ويشغل البرنامج، مطبعًا `Hello from run_simple!` (أو أي ناتج ينتجه `run_simple`).
3. إذا كنت تريد التحقق من التجميع بشكل منفصل:
   ```bash
   make build
   ```

### ملاحظات إضافية
- إذا كنت تستخدم `cargo run --bin simple` (لملف ثنائي منفصل في `simple.rs`)، تأكد من أن `Cargo.toml` يتضمن:

  ```toml
  [[bin]]
  name = "simple"
  path = "src/simple.rs"
  ```

  وأن `simple.rs` يحتوي على دالة `main`:

  ```rust
  pub fn run_simple() {
      println!("Hello from run_simple!");
  }

  fn main() {
      run_simple();
  }
  ```

- إذا واجهت مشاكل، شارك ناتج `make run` أو `cargo run` لمزيد من تصحيح الأخطاء.

### التوصية النهائية لـ `Makefile`

```makefile
build:
	cargo build

run:
	cargo run

clean:
	cargo clean
```

هذا الإعداد يتجنب التكرار، ويدعم كلًا من البناء والتشغيل، ويحافظ على سير عملك نظيفًا. دعني أعلم إذا كان لديك المزيد من الأسئلة أو تحتاج إلى مساعدة في أخطاء محددة!