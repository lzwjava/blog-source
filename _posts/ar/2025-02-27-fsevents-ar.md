---
audio: false
generated: true
lang: ar
layout: post
title: تتبع تغييرات الدليل باستخدام API FSEvents
translated: true
---

كنت أستخدم مدونتي Jekyll، وعندما قمت بتشغيل `bundle exec jekyll serve --incremental`، ظهر في الشاشة `fsevent_watch`. لذلك، سألت عن ذلك مع الذكاء الاصطناعي.

---

يبدو أنك تتحدث عن `fsevent_watch`، والذي ليس أداة أو وظيفة مستقلة قياسية في معظم السياقات البرمجية. بناءً على سؤالك و العادات الشائعة، سأفترض أنك تتحدث عن استخدام **FSEvents API** على macOS لمراقبة أحداث نظام الملفات - ربما كنت تتحدث عن شيء مثل `fsevents` أو أداة ذات صلة. إذا كنت قد فهمت خطأ، يرجى توضيح ذلك!

FSEvents API هو إطار عمل خاص بماك أو إس يسمح للبرامج بتلقي إشعارات حول التغييرات في شجرة الدليل. يستخدم بشكل شائع في C، Objective-C أو Swift لتتبع أحداث نظام الملفات مثل إنشاء الملف، حذفه أو تعديله. نظرًا لأن `fsevent_watch` ليس أمرًا أو وظيفة معترف بها (قد يكون خطأ طباعة أو أداة ثالثة)، سأشرح كيفية استخدام FSEvents API مباشرة، وهو ما قد يكون ما تبحث عنه.

هنا دليل عملي لاستخدام FSEvents لمراقبة الدليل:

### استخدام FSEvents في C/Objective-C
FSEvents API هو جزء من إطار عمل CoreServices على macOS. أدناه مثال أساسي في C لمراقبة دليل للتغييرات:

1. **شمل الرؤوس اللازمة**:
   عليك شمل رأس FSEvents من إطار عمل CoreServices.

2. **إعداد تدفق الأحداث**:
   إنشاء تدفق الأحداث لمراقبة دليل معين، تعريف وظيفة استدعاء للتصرف على الأحداث، وتخطيطها مع حلقة تشغيل.

3. **تصرف على الأحداث**:
   تقوم وظيفة الاستدعاء بتعالجة الأحداث (مثل تغيير الملف، حذفه) وتوفر مسارات وأعلام.

هنا مثال بسيط:

```c
#include <CoreServices/CoreServices.h>
#include <stdio.h>

// وظيفة استدعاء لتعامل مع أحداث نظام الملفات
void callback(
    ConstFSEventStreamRef streamRef,
    void *clientCallBackInfo,
    size_t numEvents,
    void *eventPaths,
    const FSEventStreamEventFlags eventFlags[],
    const FSEventStreamEventId eventIds[])
{
    char **paths = (char **)eventPaths;
    for (size_t i = 0; i < numEvents; i++) {
        printf("تغير تم اكتشافه في: %s (أعلام: 0x%x)\n", paths[i], eventFlags[i]);
    }
}

int main() {
    // مسار المراقبة (مثل دليل المستخدم الخاص بك)
    CFStringRef myPath = CFStringCreateWithCString(NULL, "/Users/yourusername", kCFStringEncodingUTF8);
    CFArrayRef pathsToWatch = CFArrayCreate(NULL, (const void **)&myPath, 1, NULL);

    // إنشاء تدفق الأحداث
    FSEventStreamRef stream = FSEventStreamCreate(
        NULL,           // المخصص
        &callback,      // وظيفة الاستدعاء
        NULL,           // معلومات الاستدعاء (السياق)
        pathsToWatch,   // المسارات المراقبة
        kFSEventStreamEventIdSinceNow, // بدء مع الأحداث من الآن
        1.0,            // تأخير في الثواني (تجميع التأخير)
        kFSEventStreamCreateFlagNone // أعلام (يمكن استخدام kFSEventStreamCreateFlagFileEvents لأحداث مستوى الملف)
    );

    // جدول التدفق على الحلقة الحالية
    FSEventStreamScheduleWithRunLoop(stream, CFRunLoopGetCurrent(), kCFRunLoopDefaultMode);

    // بدء التدفق
    FSEventStreamStart(stream);

    // تشغيل الحلقة للاستماع إلى الأحداث
    printf("مراقبة /Users/yourusername... اضغط على Ctrl+C لإيقاف.\n");
    CFRunLoopRun();

    // التنظيف (غير قابل للوصول في هذا المثال إلا إذا تم إيقافه)
    FSEventStreamStop(stream);
    FSEventStreamInvalidate(stream);
    FSEventStreamRelease(stream);
    CFRelease(pathsToWatch);
    CFRelease(myPath);

    return 0;
}
```

#### خطوات شرحها:
- **مسارات المراقبة**: تحدد واحد أو أكثر من الدلائل (مثل `/Users/yourusername`) في `CFArray`.
- **استدعاء**: يتم استدعاء وظيفة `callback` عند حدوث تغييرات. تتلقى مجموعة من المسارات المتأثرة وأعلام (مثل `kFSEventStreamEventFlagItemCreated`).
- **إنشاء التدفق**: `FSEventStreamCreate` يحدد المراقب. تأخير (مثل `1.0` ثانية) يجمع الأحداث لمنع إغراق الاستدعاء.
- **حلقة التشغيل**: يتكامل التدفق مع حلقة تشغيل (مثل `CFRunLoopRun`) لحفظ البرنامج على قيد الحياة ومتفاعل.
- **التنظيف**: إيقاف وإلغاء التدفق عند الانتهاء (غير مذكور في هذا المثال الحلقة اللانهائية).

#### التجميع:
تجميع مع إطار عمل CoreServices:
```bash
gcc -o fsevents_example fsevents_example.c -framework CoreServices
```

تشغيله:
```bash
./fsevents_example
```

### النقاط الرئيسية:
- **التفصيل**: بشكل افتراضي، FSEvents يراقب التغييرات على مستوى الدليل. لأحداث مستوى الملف (مثل تعديل ملف معين)، أضف علامة `kFSEventStreamCreateFlagFileEvents`.
- **التأخير**: يسيطر المعامل التأخير (مثل `1.0`) على كيفية تكرار استدعاء الاستدعاء. القيم الأقل تتيح تحديثات أسرع ولكن أكثر استدعاءات.
- **المنطقة**: FSEvents يراقب شجرة الدليل بالكامل بشكل تكراري - لا حاجة إلى تحديد الدلائل الفرعية.

### بديل: استخدام أداة
إذا كنت تبحث عن أداة سطر الأوامر بدلاً من كتابة الكود بنفسك، فلا يوجد `fsevent_watch` في مجموعة أدوات macOS القياسية. ومع ذلك، هناك أدوات ثالثة مثل `fswatch` تستفيد من FSEvents. لاستخدام `fswatch`:

1. **تثبيت fswatch** (مثلًا عبر Homebrew):
   ```bash
   brew install fswatch
   ```

2. **تشغيله**:
   ```bash
   fswatch /path/to/watch
   ```
   يخرج المسارات عند حدوث التغييرات. على سبيل المثال:
   ```bash
   fswatch ~/Documents
   ```
   ستشاهد خطوط مثل `/Users/yourusername/Documents/file.txt` عند تغيير الملفات.

3. **مع نصيبي**:
   قم بتوجيهه إلى نصيبي للتصرفات المخصصة:
   ```bash
   fswatch ~/Documents | while read -r file; do echo "تغير: $file"; done
   ```

### إذا كنت تتحدث عن شيء آخر
إذا كان `fsevent_watch` يشير إلى مكتبة أو أداة أو خطأ طباعة معينة (مثل `fsevents-watch`), يرجى تقديم المزيد من السياق - مثل لغة البرمجة أو البيئة التي تعمل بها - وسأعدل الرد بشكل أفضل.

أعلمني كيف يمكنني تحسين هذا لك!