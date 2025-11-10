---
audio: false
generated: true
lang: ar
layout: post
title: VSCode Pico-W-Go لـ MicroPython
translated: true
type: note
---

يُعد استخدام إضافة **Raspberry Pi Pico** في Visual Studio Code (VSCode) خيارًا ممتازًا لتطوير MicroPython على لوحة Raspberry Pi Pico الخاصة بك، حيث إنها توفر سير عمل مبسطًا يشبه Thonny ولكن داخل بيئة التحرير القوية لـ VSCode. الإضافة التي تشير إليها على الأرجح هي **Pico-W-Go** (أو إضافة مشابهة مثل **Pico-Go**)، والتي تم تصميمها خصيصًا لتطوير Raspberry Pi Pico و Pico W باستخدام MicroPython. أدناه، سأرشدك خلال إعداد واستخدام إضافة **Pico-W-Go** (الخيار الأكثر شيوعًا والصيانة) لتحميل برنامج MicroPython بسيط إلى Pico الخاص بك، بافتراض أن MicroPython مثبت مسبقًا (من ملف `RPI_PICO-20250415-v1.25.0.uf2` الذي استخدمته).

---

### المتطلبات الأساسية
1.  **MicroPython مثبت**: أن يكون لدى Pico الخاص بك MicroPython مثبتًا، كما قمت بتثبيته مسبقًا.
2.  **VSCode مثبت**: تأكد من تثبيت VSCode ([code.visualstudio.com](https://code.visualstudio.com)).
3.  **Python مثبت**: مطلوب لاعتماديات Pico-W-Go:
    ```bash
    sudo apt update
    sudo apt install python3 python3-pip
    ```
4.  **اتصال USB**: يتم توصيل Pico عبر كابل USB يدعم نقل البيانات.

---

### دليل خطوة بخطوة لاستخدام إضافة Raspberry Pi Pico (Pico-W-Go) في VSCode

1.  **تثبيت إضافة Pico-W-Go**:
    *   افتح VSCode.
    *   انتقل إلى عرض الإضافات (`Ctrl+Shift+X` أو `Cmd+Shift+X` على نظام macOS).
    *   ابحث عن **Pico-W-Go** وقم بتثبيتها (مطورة بواسطة Paul Obermeier وآخرين).
    *   ملاحظة: إذا كنت تقصد إضافة مختلفة (مثل Pico-Go)، فأخبرني، ولكن Pico-W-Go هي الأكثر استخدامًا لتطوير MicroPython على Pico.

2.  **تثبيت اعتماديات Pico-W-Go**:
    *   تتطلب Pico-W-Go `pyserial` و `esptool` للاتصال التسلسلي والتثبيت:
      ```bash
      pip3 install pyserial esptool
      ```
    *   تأكد من تثبيتها في بيئة Python الخاصة بك (استخدم `pip3 list` للتحقق).

3.  **تكوين Pico-W-Go**:
    *   افتح Command Palette في VSCode (`Ctrl+Shift+P` أو `Cmd+Shift+P`).
    *   اكتب واختر **Pico-W-Go > Configure Project**.
    *   اتبع المطالبات:
        *   **منفذ التسلسل (Serial Port)**: حدد المنفذ الخاص بـ Pico (مثل `/dev/ttyACM0`). يمكنك العثور عليه عن طريق تشغيل:
          ```bash
          ls /dev/tty*
          ```
          ابحث عن `/dev/ttyACM0` أو ما شابه، والذي يظهر عند توصيل Pico.
        *   **المُفسر (Interpreter)**: اختر MicroPython (Raspberry Pi Pico).
        *   **مجلد المشروع (Project Folder)**: حدد أو أنشئ مجلدًا لمشروعك (مثل `~/PicoProjects/MyProject`).
    *   تقوم Pico-W-Go بإنشاء ملف تكوين `.picowgo` في مجلد مشروعك لتخزين الإعدادات.

4.  **كتابة برنامج MicroPython بسيط**:
    *   في VSCode، افتح مجلد مشروعك (File > Open Folder).
    *   أنشئ ملفًا جديدًا باسم `main.py` (يقوم MicroPython بتشغيل `main.py` تلقائيًا عند بدء التشغيل).
    *   أضف برنامجًا بسيطًا، على سبيل المثال، لجعل LED المضمنة يومض:
      ```python
      from machine import Pin
      import time

      led = Pin(25, Pin.OUT)  # استخدم "LED" لـ Pico W
      while True:
          led.on()
          time.sleep(0.5)
          led.off()
          time.sleep(0.5)
      ```
    *   احفظ الملف (`Ctrl+S`).

5.  **تحميل البرنامج إلى Pico**:
    *   تأكد من توصيل Pico وأن المنفذ الصحيح محدد (أعد تشغيل **Pico-W-Go > Configure Project** إذا لزم الأمر).
    *   افتح Command Palette (`Ctrl+Shift+P`).
    *   اختر **Pico-W-Go > Upload Project to Pico**.
        *   يقوم هذا بتحميل جميع الملفات في مجلد مشروعك (مثل `main.py`) إلى نظام ملفات Pico.
    *   بدلاً من ذلك، لتحميل ملف واحد:
        *   انقر بزر الماوس الأيمن على `main.py` في مستكشف ملفات VSCode.
        *   اختر **Pico-W-Go > Upload File to Pico**.
    *   ينتقل الملف إلى Pico، وإذا كان الملف هو `main.py`، فسيتم تشغيله تلقائيًا عند بدء التشغيل.

6.  **تشغيل واختبار البرنامج**:
    *   **التنفيذ التلقائي**: إذا قمت بتحميل `main.py`، أعد ضبط Pico (افصله وأعد توصيله، أو اضغط على زر RESET إذا كان متاحًا). يجب أن تبدأ الـ LED في الوميض.
    *   **التنفيذ اليدوي**:
        *   افتح Command Palette واختر **Pico-W-Go > Run**.
        *   هذا ينفذ الملف الحالي على Pico.
    *   **استخدم REPL**:
        *   افتح Command Palette واختر **Pico-W-Go > Open REPL**.
        *   تظهر REPL في طرفية VSCode، حيث يمكنك اختبار الأوامر:
          ```python
          from machine import Pin
          led = Pin(25, Pin.OUT)
          led.on()
          ```
        *   اضغط على `Ctrl+C` لإيقاف البرنامج قيد التشغيل في REPL.

7.  **إدارة الملفات على Pico**:
    *   **سرد الملفات**: استخدم **Pico-W-Go > Download Project from Pico** لعرض أو استرجاع الملفات من نظام ملفات Pico.
    *   **حذف الملفات**: افتح Command Palette واختر **Pico-W-Go > Delete All Files** لمسح نظام ملفات Pico، أو استخدم REPL:
      ```python
      import os
      os.remove('main.py')
      ```
    *   **التحقق من الإخراج**: يظهر إخراج البرنامج (مثل جمل `print`) في REPL أو في طرفية VSCode إذا تم تكوينها.

---

### استكشاف الأخطاء وإصلاحها
*   **لم يتم اكتشاف المنفذ**:
    *   قم بتشغيل `ls /dev/tty*` للتأكد من منفذ Pico (مثل `/dev/ttyACM0`).
    *   تأكد من أن كابل USB يدعم نقل البيانات وجرب منفذًا مختلفًا.
    *   أعد تكوين المنفذ في **Pico-W-Go > Configure Project**.
*   **فشل التحميل**:
    *   تحقق من تثبيت `pyserial` و `esptool` (`pip3 list`).
    *   تأكد من أن MicroPython يعمل (يجب أن يكون الوصول إلى REPL متاحًا).
    *   أعد تثبيت MicroPython إذا لزم الأمر عن طريق إعادة الدخول إلى وضع BOOTSEL ونسخ ملف `.uf2`.
*   **LED لا يومض**:
    *   تأكد من رقم منفذ GPIO الصحيح (`25` لـ Pico، `"LED"` لـ Pico W).
    *   اختبر في REPL:
      ```python
      from machine import Pin
      led = Pin(25, Pin.OUT)
      led.on()
      ```
*   **أوامر Pico-W-Go مفقودة**: تأكد من تثبيت الإضافة وتفعيلها. أعد تشغيل VSCode إذا لزم الأمر.

---

### مزايا استخدام Pico-W-Go في VSCode
*   **سير عمل متكامل**: يجمع بين تحرير الكود، وإدارة الملفات، والوصول إلى REPL في VSCode.
*   **ميزات متقدمة**: يستفيد من تكامل Git والإضافات والتخصيص في VSCode.
*   **متعدد المنصات**: يعمل على Linux وWindows وmacOS.

### القيود مقارنة بـ Thonny
*   الإعداد أكثر تعقيدًا قليلاً (مثل تثبيت `pyserial`، وتكوين المنفذ).
*   قد يبدو تكامل REPL أقل سلاسة من واجهة Thonny الشاملة.
*   أقل ملاءمة للمبتدئين لمستخدمي MicroPython لأول مرة.

---

### إضافات بديلة
إذا كنت تقصد إضافة مختلفة (مثل **Pico-Go**)، لاحظ أن Pico-Go هي بديل أقدم لـ Pico-W-Go وقد تحتوي على ميزات أقل أو تحديثات أقل. الإعداد مشابه، ولكن يوصى باستخدام Pico-W-Go لتطويرها النشط ودعمها لكل من Pico و Pico W. إذا كنت تستخدم إضافة محددة أخرى، فيرجى التوضيح، وسأقوم بتخصيص التعليمات.

---

### مثال على سير العمل
1.  قم بتثبيت Pico-W-Go والاعتماديات.
2.  قم بتكوين المشروع باستخدام منفذ التسلسل الصحيح (`/dev/ttyACM0`).
3.  اكتب واحفظ `main.py` بكود إضاءة LED.
4.  استخدم **Pico-W-Go > Upload Project to Pico** للتحميل.
5.  أعد ضبط Pico أو استخدم **Pico-W-Go > Run** لرؤية LED يومض.
6.  استخدم REPL للاختبار أو التصحيح التفاعلي.

إذا كنت بحاجة إلى مساعدة في أوامر Pico-W-Go محددة، أو مثال برنامج آخر، أو استكشاف الأخطاء وإصلاحها (مثل مشاكل المنفذ، أخطاء الإضافة)، فأخبرني!