---
audio: false
generated: true
lang: ar
layout: post
title: مراقبة تغييرات الدليل باستخدام واجهة برمجة تطبيقات FSEvents
translated: true
type: note
---

كنت أستخدم مدونة Jekyll، وعندما قمت بتشغيل `bundle exec jekyll serve --incremental`، عرض الطرفية `fsevent_watch`. نتيجة لذلك، استفسرت عنها من ذكاء اصطناعي.

---

يبدو أنك قد تشير إلى `fsevent_watch`، والذي ليس أداة أو وظيفة قياسية مستقلة في معظم السياقات البرمجية. بناءً على سؤالك والأعراف الشائعة، سأفترض أنك تسأل عن العمل مع **FSEvents API** على نظام macOS لمراقبة أحداث نظام الملفات—ربما قصدت شيئًا مثل `fsevents` أو أداة مرتبطة. إذا أسأت الفهم، يرجى التوضيح!

FSEvents API هو إطار عمل خاص بنظام macOS يسمح للتطبيقات باستقبال إشعارات حول التغييرات في شجرة الدليل. يشيع استخدامه في برمجة C أو Objective-C أو Swift لمراقبة أحداث نظام الملفات مثل إنشاء الملفات أو حذفها أو تعديلها. نظرًا لأن `fsevent_watch` ليس أمرًا أو وظيفة معترفًا بها (قد يكون خطأ مطبعيًا أو أداة من طرف ثالث)، سأشرح كيفية استخدام FSEvents API مباشرة، وهو على الأرجح ما تبحث عنه.

إليك دليلًا عمليًا لاستخدام FSEvents لمراقبة دليل:

### استخدام FSEvents في C/Objective-C
FSEvents API هو جزء من إطار CoreServices على نظام macOS. فيما يلي مثال أساسي بلغة C لمراقبة دليل للتغييرات:

1. **تضمين الرؤوس الضرورية**:
   ستحتاج إلى تضمين رأس FSEvents من إطار CoreServices.

2. **إعداد دفق الأحداث**:
   أنشئ دفق أحداث لمراقبة دليل معين، وعرّف دالة رد لمعالجة الأحداث، وقم بجدولتها مع حلقة تشغيل (run loop).

3. **معالجة الأحداث**:
   تقوم دالة الرد بمعالجة الأحداث (مثل تغيير الملف، حذفه) وتوفر المسارات والأعلام.

إليك مثالًا بسيطًا:

```c
#include <CoreServices/CoreServices.h>
#include <stdio.h>

// دالة رد لمعالجة أحداث نظام الملفات
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
        printf("تم اكتشاف تغيير في: %s (الأعلام: 0x%x)\n", paths[i], eventFlags[i]);
    }
}

int main() {
    // المسار للمراقبة (مثل، دليل المستخدم الرئيسي)
    CFStringRef myPath = CFStringCreateWithCString(NULL, "/Users/yourusername", kCFStringEncodingUTF8);
    CFArrayRef pathsToWatch = CFArrayCreate(NULL, (const void **)&myPath, 1, NULL);

    // إنشاء دفق الأحداث
    FSEventStreamRef stream = FSEventStreamCreate(
        NULL,           // المُعيِّر (Allocator)
        &callback,      // دالة الرد
        NULL,           // معلومات الرد (السياق)
        pathsToWatch,   // المسارات للمراقبة
        kFSEventStreamEventIdSinceNow, // ابدأ بالأحداث من الآن
        1.0,            // زمن الاستجابة بالثواني (تأخير الدُفعات)
        kFSEventStreamCreateFlagNone // الأعلام (يمكن استخدام kFSEventStreamCreateFlagFileEvents لأحداث مستوى الملف)
    );

    // جدولة الدفق على حلقة التشغيل الحالية
    FSEventStreamScheduleWithRunLoop(stream, CFRunLoopGetCurrent(), kCFRunLoopDefaultMode);

    // بدء الدفق
    FSEventStreamStart(stream);

    // تشغيل الحلقة للاستماع للأحداث
    printf("جاري مراقبة /Users/yourusername... اضغط Ctrl+C للإيقاف.\n");
    CFRunLoopRun();

    // التنظيف (غير قابل للوصول في هذا المثال ما لم يتم إيقافه)
    FSEventStreamStop(stream);
    FSEventStreamInvalidate(stream);
    FSEventStreamRelease(stream);
    CFRelease(pathsToWatch);
    CFRelease(myPath);

    return 0;
}
```

#### الخطوات الموضحة:
- **المسارات للمراقبة**: تحدد واحدًا أو أكثر من الأدلة (مثل `/Users/yourusername`) في `CFArray`.
- **دالة الرد**: يتم استدعاء الدالة `callback` عند حدوث تغييرات. تستقبل مصفوفة من المسارات المتأثرة والأعلام (مثل `kFSEventStreamEventFlagItemCreated`).
- **إنشاء الدفق**: `FSEventStreamCreate` يُنشئ المراقب. يتحكم زمن الاستجابة (مثل `1.0` ثانية) في تجميع الأحداث لتجنب إرباك دالة الرد.
- **حلقة التشغيل**: يندمج الدفق مع حلقة تشغيل (مثل `CFRunLoopRun`) لإبقاء البرنامج نشطًا ومستجيبًا.
- **التنظيف**: أوقف الدفق وقم بإطلاقه عند الانتهاء (غير موضح في مثال الحلقة اللانهائية هذا).

#### الترجمة:
ترجم مع إطار CoreServices:
```bash
gcc -o fsevents_example fsevents_example.c -framework CoreServices
```

شغله:
```bash
./fsevents_example
```

### النقاط الرئيسية:
- **الدقة**: بشكل افتراضي، يراقب FSEvents التغييرات على مستوى الدليل. لأحداث مستوى الملف (مثل تعديلات ملف معين)، أضف العلم `kFSEventStreamCreateFlagFileEvents`.
- **زمن الاستجابة**: تحدد معلمة زمن الاستجابة (مثل `1.0`) عدد مرات تنفيذ دالة الرد. القيم الأقل تعطي تحديثات أسرع ولكن بمزيد من الاستدعاءات.
- **النطاق**: يراقب FSEvents شجرة الدليل بأكملها بشكل متكرر—لا حاجة لتحديد الأدلة الفرعية.

### بديل: استخدام أداة
إذا كنت تبحث عن أداة سطر أوامر بدلاً من برمجتها بنفسك، لا توجد أداة `fsevent_watch` في مجموعة أدوات macOS القياسية. ومع ذلك، فإن أدوات الطرف الثالث مثل `fswatch` تستفيد من FSEvents. لاستخدام `fswatch`:

1. **تثبيت fswatch** (عبر Homebrew مثلاً):
   ```bash
   brew install fswatch
   ```

2. **تشغيله**:
   ```bash
   fswatch /path/to/watch
   ```
   هذا يخرج المسارات عند حدوث التغييرات. على سبيل المثال:
   ```bash
   fswatch ~/Documents
   ```
   سترى أسطر مثل `/Users/yourusername/Documents/file.txt` عندما تتغير الملفات.

3. **باستخدام سكريبت**:
   يمكنك تحويل مخرجاته إلى سكريبت لإجراء أفعال مخصصة:
   ```bash
   fswatch ~/Documents | while read -r file; do echo "تغير: $file"; done
   ```

### إذا كنت تقصد شيئًا آخر
إذا كان `fsevent_watch` يشير إلى مكتبة أو أداة أو خطأ مطبعي محدد (مثل `fsevents-watch`)، يرجى تقديم المزيد من السياق—مثل لغة البرمجة أو البيئة التي تعمل فيها—وسأخصص الرد accordingly.

دعني أعرف كيف يمكنني تحسين هذا لك!