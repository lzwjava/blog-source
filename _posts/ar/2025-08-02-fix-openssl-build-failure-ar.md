---
audio: false
generated: true
image: false
lang: ar
layout: post
title: إصلاح فشل بناء OpenSSL
translated: true
type: note
---

أنت تواجه مشكلة بناء "openssl-sys" الكلاسيكية لأنك لا تملك أداة pkg-config في نظامك أو رؤوس تطوير OpenSSL مثبتة. على أوبونتو/ديبيان، أبسط حل هو:

1. **تثبيت pkg-config ورؤوس تطوير OpenSSL**

   ```bash
   sudo apt update
   sudo apt install pkg-config libssl-dev
   ```

   * `pkg-config` تسمح لبرنامج نصي للبناء Rust باكتشاف مكان وجود OpenSSL.
   * `libssl-dev` توفر الرؤوس والمكتبات (الحزمة "--dev").

2. **أعد تشغيل عملية البناء**

   ```bash
   cargo clean
   cargo run
   ```

---

### بديل: استخدم ميزة "vendored"

إذا كنت لا تريد الاعتماد على OpenSSL الموجود في النظام (أو ليس لديك صلاحيات root)، يمكنك الطلب من الحزمة بناء نسخة مجمعة من OpenSSL من المصدر:

1. في ملف **Cargo.toml** الخاص بك، غيّر الاعتماد إلى:

   ```toml
   [dependencies]
   openssl = { version = "0.10", features = ["vendored"] }
   ```
2. ثم أعد البناء مرة أخرى:

   ```bash
   cargo clean
   cargo run
   ```

سيؤدي هذا إلى تجميع OpenSSL نفسه والربط ضده، مما يتجنب الحاجة إلى تثبيت نظامي.

---

### (اختياري) تثبيت OpenSSL مخصص

إذا كان لديك OpenSSL مثبتًا في موقع غير قياسي، يمكنك توجيه البناء إليه:

```bash
export OPENSSL_DIR=/path/to/your/openssl
export OPENSSL_LIB_DIR=$OPENSSL_DIR/lib
export OPENSSL_INCLUDE_DIR=$OPENSSL_DIR/include
```

ثم أعد تشغيل `cargo run`. هذا يخبر openssl-sys بالضبط أين يمكنه العثور على الرؤوس والمكتبات.

---

> **ملاحظة:** التحذير بشأن تثبيت `edition2024` غير ضار — يمكنك إزالة هذه الميزة من ملف `Cargo.toml` الخاص بك، لكنه لن يمنع عملية البناء لديك.