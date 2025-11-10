---
audio: false
generated: true
lang: ar
layout: post
title: VSCode لـ Raspberry Pi Pico وMicroPython
translated: true
type: note
---

نعم، يمكنك استخدام Visual Studio Code (VSCode) لكتابة وتحميل وتشغيل برامج MicroPython على لوحة Raspberry Pi Pico الخاصة بك، بشكل مشابه لكيفية استخدامك لـ Thonny. يعد VSCode محررًا قويًا، ومع الإضافات والأدوات المناسبة، يمكنه التعامل مع تطوير MicroPython بفعالية. فيما يلي دليل خطوة بخطوة لإعداد VSCode لتحميل برنامج MicroPython بسيط إلى لوحة Pico الخاصة بك، بافتراض أن MicroPython مثبت مسبقًا (كما فعلت مع ملف `.uf2`).

---

### المتطلبات الأساسية
1.  **تثبيت MicroPython**: تم تثبيت MicroPython على لوحة Pico الخاصة بك (مثال: من ملف `RPI_PICO-20250415-v1.25.0.uf2`).
2.  **تثبيت VSCode**: قم بتنزيل وتثبيت VSCode من [code.visualstudio.com](https://code.visualstudio.com) إذا لم تكن قد قمت بذلك بالفعل.
3.  **تثبيت Python**: قم بتثبيت Python (مطلوب لأدوات MicroPython) عبر:
    ```bash
    sudo apt update
    sudo apt install python3 python3-pip
    ```
4.  **اتصال USB**: يتم توصيل لوحة Pico بجهاز الكمبيوتر الخاص بك عبر كابل USB قادر على نقل البيانات.

---

### دليل خطوة بخطوة لاستخدام VSCode لـ MicroPython على Raspberry Pi Pico

1.  **تثبيت إضافات VSCode المطلوبة**:
    *   افتح VSCode.
    *   انتقل إلى عرض الإضافات (`Ctrl+Shift+X` أو `Cmd+Shift+X` على نظام macOS).
    *   قم بتثبيت الإضافات التالية:
        *   **Python** (من Microsoft): لتلوين بناء الجملة و IntelliSense لـ Python و MicroPython.
        *   **Pico-W-Go** (اختياري ولكنه موصى به): إضافة مخصصة لتطوير Raspberry Pi Pico باستخدام MicroPython. ابحث عن "Pico-W-Go" وقم بتثبيتها.
            *   ملاحظة: يبسط Pico-W-Go نقل الملفات والوصول إلى REPL ولكنه يتطلب إعدادًا إضافيًا (موضح أدناه).
        *   بدلاً من ذلك، يمكنك استخدام إضافات عامة مثل **Remote-SSH** أو **Serial Monitor** إذا كنت تفضل التحكم اليدوي.

2.  **إعداد Pico-W-Go (موصى به)**:
    *   **تثبيت التبعيات**: يتطلب Pico-W-Go `pyserial` و `esptool`. قم بتثبيتهما عبر pip:
        ```bash
        pip3 install pyserial esptool
        ```
    *   **تكوين Pico-W-Go**:
        *   افتح Palette الأوامر في VSCode (`Ctrl+Shift+P` أو `Cmd+Shift+P`).
        *   اكتب واختر **Pico-W-Go > Configure Project**.
        *   اتبع المطالبات لإعداد مشروعك:
            *   اختر منفذ التسلسل للوحة Pico (مثال: `/dev/ttyACM0`). قم بتشغيل `ls /dev/tty*` في الطرفية للعثور عليه.
            *   اختر MicroPython كمفسر الشفرة.
            *   أنشئ مجلد مشروع جديد أو استخدم مجلدًا موجودًا.
        *   ينشئ Pico-W-Go مساحة عمل مع ملف تكوين `.picowgo`.

3.  **كتابة برنامج MicroPython بسيط**:
    *   في VSCode، أنشئ ملفًا جديدًا (مثال: `main.py`) في مجلد مشروعك.
    *   اكتب برنامجًا بسيطًا، مثل جعل LED المضمنة يومض:
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
    *   احفظ الملف (`Ctrl+S` أو `Cmd+S`).

4.  **تحميل البرنامج إلى لوحة Pico**:
    *   **باستخدام Pico-W-Go**:
        *   تأكد من أن لوحة Pico متصلة وأن المنفذ الصحيح محدد (تحقق في `Pico-W-Go > Configure Project` إذا لزم الأمر).
        *   افتح Palette الأوامر (`Ctrl+Shift+P`).
        *   اختر **Pico-W-Go > Upload Project to Pico**.
        *   سيؤدي هذا إلى تحميل جميع الملفات في مجلد مشروعك (مثال: `main.py`) إلى نظام ملفات لوحة Pico.
        *   إذا قمت بتسمية الملف `main.py`، فسيتم تشغيله تلقائيًا عند بدء التشغيل.
    *   **التحميل اليدوي باستخدام `rshell`** (إذا لم تستخدم Pico-W-Go):
        *   قم بتثبيت `rshell`:
            ```bash
            pip3 install rshell
            ```
        *   اتصل بلوحة Pico:
            ```bash
            rshell --port /dev/ttyACM0
            ```
        *   انسخ الملف إلى لوحة Pico:
            ```bash
            cp main.py /pyboard/main.py
            ```
        *   اختر `exit` للخروج من `rshell`.

5.  **تشغيل واختبار البرنامج**:
    *   **باستخدام Pico-W-Go**:
        *   افتح Palette الأوامر واختر **Pico-W-Go > Run**.
        *   يؤدي هذا إلى تنفيذ الملف الحالي أو فتح REPL للأوامر اليدوية.
        *   يجب أن ترى LED يومض إذا كنت تستخدم المثال أعلاه.
    *   **باستخدام Terminal أو REPL في VSCode**:
        *   افتح REPL مع Pico-W-Go (`Pico-W-Go > Open REPL`) أو استخدم `rshell`:
            ```bash
            rshell --port /dev/ttyACM0 repl
            ```
        *   اختبر الأوامر مباشرة، مثال:
            ```python
            from machine import Pin
            led = Pin(25, Pin.OUT)
            led.on()
            ```
        *   اضغط على `Ctrl+C` لإيقاف البرنامج قيد التشغيل في REPL.
    *   إذا كان الملف هو `main.py`، فقم بإعادة تعيين لوحة Pico (افصلها وأعد توصيلها، أو اضغط على زر RESET) لتشغيله تلقائيًا.

6.  **تصحيح الأخطاء وإدارة الملفات**:
    *   **Pico-W-Go**: استخدم **Pico-W-Go > Download Project from Pico** لاسترداد الملفات من لوحة Pico أو **Pico-W-Go > Delete All Files** لمسح نظام الملفات.
    *   **rshell**: اعرض قائمة الملفات باستخدام:
        ```bash
        rshell ls /pyboard
        ```
        احذف الملفات باستخدام:
        ```bash
        rshell rm /pyboard/main.py
        ```
    *   تحقق من ناتج البرنامج في Terminal أو REPL في VSCode.

---

### بديل: سير العمل اليدوي بدون Pico-W-Go
إذا كنت تفضل عدم استخدام Pico-W-Go، يمكنك إدارة تطوير MicroPython يدويًا:
1.  اكتب الكود الخاص بك في VSCode واحفظه كـ `main.py`.
2.  استخدم `ampy` (أداة أخرى لـ MicroPython) للتحميل:
    ```bash
    pip3 install adafruit-ampy
    ampy --port /dev/ttyACM0 put main.py
    ```
3.  الوصول إلى REPL باستخدام أداة طرفية مثل `minicom` أو `screen`:
    ```bash
    screen /dev/ttyACM0 115200
    ```
    اضغط `Ctrl+C` لإيقاف البرنامج قيد التشغيل وأدخل إلى REPL.

---

### استكشاف الأخطاء وإصلاحها
*   **المنفذ غير موجود**: قم بتشغيل `ls /dev/tty*` للتحقق من منفذ لوحة Pico (مثال: `/dev/ttyACM0`). تأكد من أن لوحة Pico متصلة وأن MicroPython مثبت.
*   **أخطاء Pico-W-Go**: تحقق من تثبيت `pyserial` و `esptool` وأن المنفذ الصحيح محدد. أعد تشغيل VSCode إذا لزم الأمر.
*   **البرنامج لا يعمل**: تأكد من حفظ الملف كـ `main.py` للتنفيذ التلقائي، أو قم بتشغيله يدويًا عبر REPL أو `ampy run main.py`.
*   **LED لا يومض**: تحقق من رقم منفذ GPIO (`25` لـ Pico، `"LED"` لـ Pico W). اختبر في REPL:
    ```python
    from machine import Pin
    led = Pin(25, Pin.OUT)
    led.on()
    ```

---

### مزايا VSCode مقارنة بـ Thonny
*   ميزات تحرير كود أفضل (مثال: IntelliSense، تكامل Git، سير عمل قابل للتخصيص).
*   يدعم المشاريع الأكبر ذات الملفات المتعددة.
*   يوفر Pico-W-Go تجربة شبيهة بـ Thonny ولكن مع قوة VSCode.

### القيود
*   الإعداد أكثر تعقيدًا قليلاً من Thonny.
*   قد يبدو تكامل REPL أقل سلاسة مقارنة بواجهة Thonny الشاملة.

إذا كنت بحاجة إلى مساعدة في إعدادات VSCode المحددة، أو تثبيت الأدوات، أو كتابة برامج MicroPython أكثر تعقيدًا، فأخطرني!