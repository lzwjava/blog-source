---
audio: false
generated: true
lang: ar
layout: post
title: إصلاح خطأ TCMalloc
translated: true
type: note
---

يشير الخطأ "Cannot locate TCMalloc. Do you have tcmalloc or google-perftool installed on your system? (improves CPU memory usage)" إلى أن مكتبة TCMalloc، وهي جزء من أدوات gperftools من Google، غير مثبتة أو غير مهيئة بشكل صحيح على نظام Linux الخاص بك. TCMalloc هو مُخصص للذاكرة يمكنه تحسين الأداء وتقليل استخدام الذاكرة، خاصة في تطبيقات مثل Stable Diffusion. إليك كيفية إصلاح هذه المشكلة:

### خطوات إصلاح خطأ TCMalloc

1.  **تثبيت TCMalloc و Google Perftools**
    اعتمادًا على توزيعة Linux الخاصة بك، استخدم مدير الحزم المناسب لتثبيت المكتبات المطلوبة.

    - **لأنظمة Ubuntu/Debian**:
      ```bash
      sudo apt-get update
      sudo apt-get install libgoogle-perftools-dev libtcmalloc-minimal4 -y
      ```
      يقوم هذا بتثبيت كل من `libgoogle-perftools-dev` الكاملة (تتضمن TCMalloc) و `libtcmalloc-minimal4` (نسخة خفيفة الوزن).

    - **لأنظمة Fedora**:
      ```bash
      sudo dnf install gperftools-libs -y
      ```
      يقوم هذا بتثبيت مكتبات TCMalloc اللازمة.

    - **لأنظمة CentOS/RHEL**:
      ```bash
      sudo yum install gperftools-libs -y
      ```
      إذا لم تكن الحزمة متاحة في المستودعات الافتراضية، قد تحتاج إلى تمكين مستودع EPEL أولاً:
      ```bash
      sudo yum install epel-release
      sudo yum install gperftools-libs -y
      ```

2.  **التحقق من التثبيت**
    بعد التثبيت، تحقق مما إذا كان TCMalloc مثبتًا:
    ```bash
    dpkg -l | grep tcmalloc
    ```
    يجب أن ترى `libtcmalloc-minimal4` أو حزم مشابهة مدرجة. بدلاً من ذلك، تحقق من مسار المكتبة:
    ```bash
    dpkg -L libgoogle-perftools-dev | grep libtcmalloc.so
    ```
    سيظهر هذا المسار إلى مكتبة TCMalloc (مثال: `/usr/lib/libtcmalloc.so.4`).

3.  **تعيين متغير البيئة LD_PRELOAD**
    لضمان استخدام تطبيقك لـ TCMalloc، عيّن متغير البيئة `LD_PRELOAD` ليشير إلى مكتبة TCMalloc. يمكن القيام بذلك بشكل مؤقت أو دائم.

    - **مؤقتًا (لجلسة العمل الحالية)**:
      شغّل تطبيقك مع تعيين `LD_PRELOAD`:
      ```bash
      export LD_PRELOAD=/usr/lib/libtcmalloc.so.4
      ./launch.py
      ```
      استبدل `/usr/lib/libtcmalloc.so.4` بالمسار الفعلي الذي تم العثور عليه في الخطوة 2 إذا كان مختلفًا.

    - **بشكل دائم (لـ Stable Diffusion أو ما شابه)**:
      إذا كنت تستخدم سكريبت مثل `webui.sh` (شائع مع Stable Diffusion)، قم بتحرير السكريبت (مثال: `webui-user.sh`) لتضمين:
      ```bash
      export LD_PRELOAD=libtcmalloc.so.4
      ```
      احفظ الملف وأعد تشغيل السكريبت:
      ```bash
      ./webui.sh
      ```
      بدلاً من ذلك، أضفه إلى تكوين shell الخاص بك (مثال: `~/.bashrc` أو `~/.zshrc`):
      ```bash
      echo 'export LD_PRELOAD=/usr/lib/libtcmalloc.so.4' >> ~/.bashrc
      source ~/.bashrc
      ```

4.  **أعد تشغيل التطبيق**
    بعد تثبيت TCMalloc وتعيين `LD_PRELOAD`، أعد تشغيل تطبيقك:
    ```bash
    ./launch.py
    ```
    يجب أن يختفي الخطأ، وقد تلاحظ تحسنًا في استخدام الذاكرة أو الأداء.

5.  **استكشاف الأخطاء وإصلاحها**
    - **إذا كان مسار المكتبة غير صحيح**: إذا فشل `LD_PRELOAD` (مثال: "cannot open shared object file")، تحقق من اسم المكتبة ومسارها الدقيق:
      ```bash
      find /usr/lib -name "libtcmalloc*.so*"
      ```
      قم بتحديث `LD_PRELOAD` بالمسار الصحيح (مثال: `libtcmalloc_minimal.so.4` إذا كنت تستخدم النسخة الدنيا).
    - **إذا استمر الخطأ**: تأكد من أن إصدار TCMalloc المثبت متوافق مع نظامك (glibc 2.35 و GCC 11.4.0 في حالتك). إذا استمرت المشاكل، حاول التثبيت من المصدر:
      ```bash
      git clone https://github.com/google/tcmalloc.git
      cd tcmalloc
      bazel build //tcmalloc:hello_main
      bazel run //tcmalloc:hello_main
      ```
      اتبع دليل البدء السريع لـ TCMalloc للحصول على تعليمات مفصلة.
    - **مشاكل الذاكرة**: إذا واجهت فشل في التخصيص أو تعطل، تأكد من أن نظامك يحتوي على ذاكرة كافية وأن TCMalloc لا يتعارض مع مُخصصات ذاكرة أخرى.

6.  **اختياري: التحقق من استخدام TCMalloc**
    للتأكد من أن TCMalloc يعمل، يمكنك تشغيل برنامج اختبار بسيط أو فحص استخدام الذاكرة بأدوات مثل `top` أو `htop` أثناء تشغيل تطبيقك. عادةً ما يقلل TCMalloc من تجزئة الذاكرة وقد يوفر دفعة طفيفة في الأداء.

### ملاحظات إضافية
- **لماذا TCMalloc؟** TCMalloc هو مُخصص ذاكرة عالي الأداء يقلل من استخدام ذاكرة CPU وتجزئتها، خاصة في التطبيقات الخيطية مثل Stable Diffusion. إنه ليس مطلوبًا بشكل صارم ولكن يمكنه تحسين الأداء.
- **التوافق**: نظامك (glibc 2.35, Python 3.10.12, GCC 11.4.0) متوافق مع أحدث إصدارات TCMalloc، لذا يجب أن تعمل الخطوات المذكورة أعلاه. إذا كنت تستخدم تطبيقًا مخصص البناء، فتأكد من أنه مُجمّع مع دعم TCMalloc.
- **سياق Stable Diffusion**: يظهر هذا الخطأ غالبًا مع واجهة Stable Diffusion WebUI الخاصة بـ AUTOMATIC1111. من المعروف أن الخطوات المذكورة أعلاه، خاصة تثبيت `libgoogle-perftools-dev` وتعيين `LD_PRELOAD`، تحل المشكلة.

إذا واجهت أخطاء محددة أو تحتاج إلى مساعدة بخصوص توزيعة Linux معينة، دعني أعلم، ويمكنني تخصيص التعليمات بشكل أكبر!