---
audio: false
generated: true
lang: ar
layout: post
title: تثبيت Rust على نظام macOS باستخدام rustup
translated: true
type: note
---

## تثبيت Rust باستخدام rustup

1. **افتح Terminal**  
   يمكنك العثور على Terminal في **Applications > Utilities** أو البحث عنه باستخدام Spotlight.

2. **ثبّت rustup و Rust**  
   نفّذ الأمر التالي لتنزيل وتشغيل سكريبت التثبيت الخاص بـ rustup:

    ```sh
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
    ```

    سيسألك السكريبت إذا كنت تريد المتابعة. اضغط `1` للتثبيت الافتراضي.

3. **اضبط Shell الخاص بك**  
   بعد التثبيت، قد تحتاج إلى إضافة Rust إلى `PATH` الخاص بالنظام. سيعطيك المثبّت أمراً مشابهاً لـ:

    ```sh
    source $HOME/.cargo/env
    ```

    أضف هذا السطر إلى ملف الضبط الخاص بـ shell الخاص بك (مثل `.zshrc` أو `.bashrc` أو `.bash_profile`) لجعل Rust متاحاً في جلسات العمل المستقبلية.

4. **تحقق من التثبيت**  
   تحقق من تثبيت Rust بشكل صحيح:

    ```sh
    rustc --version
    ```

    يجب أن ترى إصدار مترجم Rust إذا كان التثبيت ناجحاً.

---

## استخدام Homebrew لتثبيت Rust

بدلاً من ذلك، يمكنك استخدام [Homebrew](https://brew.sh/) لتثبيت Rust، على الرغم من أن `rustup` يُوصى به عادةً لتحديثات أسهل وإدارة للإصدارات.

1. **ثبّت Homebrew** (إذا لم يكن مثبتاً مسبقاً):

    ```sh
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```

2. **ثبّت Rust باستخدام Homebrew**:

    ```sh
    brew install rust
    ```

3. **تحقق من التثبيت**:

    ```sh
    rustc --version
    ```

---

## ترجمة كود Rust

1. **اكتب برنامج Rust**  
   أنشئ ملفاً باسم `main.rs` بالمحتوى التالي:

    ```rust
    fn main() {
         println!("Hello, World!");
    }
    ```

2. **اجمع البرنامج**  
   في terminal، انتقل إلى المجلد الذي يحتوي على ملفك ونفّذ:

    ```sh
    rustc main.rs
    ```

3. **شغّل البرنامج المترجم**:

    ```sh
    ./main
    ```

---

هذا الإعداد يجب أن يبدأ معك تطوير Rust على نظام macOS. إذا واجهتك أي مشاكل، لا تتردد في السؤال!