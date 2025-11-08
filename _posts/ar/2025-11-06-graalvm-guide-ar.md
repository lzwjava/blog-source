---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: دليل تثبيت واستخدام GraalVM
translated: true
type: note
---

## ما هو GraalVM؟

GraalVM هو وقت تشغيل مفتوح المصدر عالي الأداء (توزيعة JDK) يدعم لغات برمجة متعددة مثل Java وJavaScript وPython وغيرها. يتميز بمترجم JIT متطور لتنفيذ أسرع وإمكانية تجميع تطبيقات Java إلى ملفات تنفيذية أصلية عبر Native Image، مما يقلل وقت بدء التشغيل واستهلاك الذاكرة.

## التثبيت

1. **تحميل GraalVM**:
   - انتقل إلى صفحة تحميل GraalVM الرسمية.
   - اختر الإصدار المجتمعي (مجاني) أو Oracle GraalVM (بميزات إضافية).
   - حدد الإصدار المناسب لمنصتك (مثل Linux أو macOS أو Windows) والبنية المعمارية (x64 أو ARM).
   - اعتبارًا من عام 2025، أحدث إصدار مستقر هو GraalVM لـ JDK 22 أو 23 — تحقق من الموقع للحصول على أحدث إصدار.

2. **استخراج الملفات والتثبيت**:
   - قم بفك ضغط الأرشيف الذي تم تحميله إلى دليل، مثل `/opt/graalvm` على Linux/macOS أو `C:\Program Files\GraalVM` على Windows.
   - لا حاجة لبرنامج تثبيت؛ إنه توزيع محمول.

3. **تعيين متغيرات البيئة**:
   - عيّن `JAVA_HOME` ليشير إلى دليل GraalVM (مثال: `export JAVA_HOME=/opt/graalvm` على Linux/macOS).
   - أضف دليل `bin` إلى متغير البيئة `PATH` الخاص بك (مثال: `export PATH=$JAVA_HOME/bin:$PATH`).
   - تحقق من التثبيت باستخدام الأمر `java -version`؛ يجب أن يعرض تفاصيل GraalVM.

4. **تثبيت مكونات إضافية (اختياري)**:
   - استخدم `gu` (أداة تحديث GraalVM) لتثبيت بيئات تشغيل اللغات أو Native Image: `gu install native-image` (يتطلب أدوات بناء مثل `build-essential` على Linux).

## بناء برنامج Hello World

سنستخدم Java في هذا المثال، كونها اللغة الأساسية لـ GraalVM. سنقوم بإنشاء تطبيق بسيط "Hello World"، وتجميعه، وتشغيله.

### الخطوة 1: كتابة الكود
أنشئ ملفًا باسم `HelloWorld.java`:

```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World from GraalVM!");
    }
}
```

### الخطوة 2: التجميع
افتح طرفية (Terminal) في الدليل الذي يحتوي على الملف وشغّل:
```
javac HelloWorld.java
```
هذا سينتج ملف `HelloWorld.class`.

### الخطوة 3: التشغيل
```
java HelloWorld
```
الناتج:
```
Hello, World from GraalVM!
```

### متقدم: التجميع إلى ملف تنفيذي أصلي
ميزة Native Image في GraalVM تتيح لك بناء ملف ثنائي قائم بذاته.

1. تأكد من تثبيت Native Image: `gu install native-image`.
2. قم بتوليد التهيئة (قد يتطلب هذا في التشغيل الأول):
   ```
   native-image --no-fallback -H:+ReportExceptionStackTraces HelloWorld
   ```
   - هذا ينشئ `HelloWorld` (أو `helloworld.exe` على Windows)، وهو ملف ثنائي أصلي.
   - في عملية البناء الأولى، يقوم بتحليل التطبيق وقد يستغرق بضع دقائق.

3. شغّل الملف الثنائي الأصلي:
   ```
   ./HelloWorld
   ```
   الناتج هو نفسه، لكنه يبدأ فورًا وباستهلاك منخفض للذاكرة.

## نصائح لاستخدام GraalVM
- **التبديل بين إصدارات JDK**: استخدم SDKMAN! (`sdk install java 22.0.2-graal`) للإدارة السهلة.
- **متعدد اللغات**: شغّل كود Node.js باستخدام `node` من GraalVM، أو Python باستخدام `python`.
- **الأداء**: فعّل مترجم JIT الخاص بـ GraalVM باستخدام `-XX:+UnlockExperimentalVMOptions -XX:+UseJVMCICompiler`.
- **استكشاف الأخطاء وإصلاحها**: تحقق من السجلات في `~/.gu/` للمشاكل؛ تأكد من وجود مترجم لغة C في نظامك لـ Native Image.

لمزيد من التفاصيل، راجع الوثائق الرسمية.

[تحميل GraalVM](https://www.graalvm.org/downloads/)  
[دليل مستخدم GraalVM](https://www.graalvm.org/latest/reference-manual/)  
[برنامج تعليمي لـ Native Image](https://www.graalvm.org/latest/reference-manual/native-image/)