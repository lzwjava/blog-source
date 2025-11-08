---
audio: false
generated: false
image: false
lang: ar
layout: post
title: تطبيق فلاتر
translated: true
type: post
---

تتناول هذه التدوينة مشروعًا باستخدام Flutter، على الأرجح تطبيق مدونة شخصية. يشير هيكل الملفات المقدم إلى إعداد مشروع Flutter قياسي، بما في ذلك أدلة خاصة بالمنصة (android، ios، linux، macos، web) وملفات Flutter الأساسية (lib/main.dart، pubspec.yaml). إن عدم وجود تفاصيل محددة يستلزم تقديم لمحة عامة.

يتضمن مشروع Flutter نموذجي بناء واجهات المستخدم باستخدام الأدوات، وإدارة حالة التطبيق، ومعالجة إدخال المستخدم، والتكامل مع ميزات خاصة بالمنصة أو واجهات برمجة التطبيقات الخارجية. يعمل ملف `main.dart` كنقطة دخول، حيث يُعرّف شجرة الأدوات الأولية للتطبيق. يدير ملف `pubspec.yaml` التبعيات وبيانات تعريف المشروع.

يتوفر كود مصدر هذا المشروع على الرابط [https://github.com/lzwjava/lzwjava_blog](https://github.com/lzwjava/lzwjava_blog).

الاعتبارات الرئيسية لهذا المشروع في Flutter تتضمن:

* **بيئة التطوير:** تأكد من تثبيت كل من Android Studio و Xcode للتطوير متعدد المنصات.
* **الاختبار:** قم بتوصيل أجهزة فعلية أو افتراضية لاختبار التطبيق بدقة على منصات مختلفة.
* **الخبرة السابقة:** ستكون معرفة مبادئ تطوير iOS و Android مفيدة.


أدلة الملفات:

```bash
.
├── README.md
├── analysis_options.yaml
├── android
│   ├── app
│   ├── build.gradle
│   ├── gradle
│   ├── gradle.properties
│   ├── gradlew
│   ├── gradlew.bat
│   ├── local.properties
│   ├── lzwjava_blog_android.iml
│   └── settings.gradle
├── build
│   ├── 26c07c686c162683d91db277284f9499
│   ├── app
│   ├── cache.dill.track.dill
│   ├── flutter_assets
│   ├── macos
│   ├── native_assets
│   ├── path_provider_android
│   └── web
├── ios
│   ├── Flutter
│   ├── Podfile
│   ├── Runner
│   ├── Runner.xcodeproj
│   ├── Runner.xcworkspace
│   └── RunnerTests
├── lib
│   └── main.dart
├── linux
│   ├── CMakeLists.txt
│   ├── flutter
│   └── runner
├── lzwjava_blog.iml
├── macos
│   ├── Flutter
│   ├── Podfile
│   ├── Podfile.lock
│   ├── Pods
│   ├── Runner
│   ├── Runner.xcodeproj
│   ├── Runner.xcworkspace
│   └── RunnerTests
├── pubspec.lock
├── pubspec.yaml
├── test
│   └── widget_test.dart
├── web
│   ├── favicon.png
│   ├── icons
│   ├── index.html
│   └── manifest.json
└── windows
    ├── CMakeLists.txt
    ├── flutter
    └── runner
```

الكود:

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Hello World',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
        useMaterial3: true,
      ),
      home: const Scaffold(
        body: Center(
          child: Text('Hello World!'),
        ),
      ),
    );
  }
}
```