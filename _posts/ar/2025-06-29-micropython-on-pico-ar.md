---
audio: false
generated: true
lang: ar
layout: post
title: رفع MicroPython إلى Pico
translated: true
type: note
---

بعد تثبيت MicroPython على لوحة Raspberry Pi Pico الخاص بك (باستخدام ملف `.uf2` كما هو موضح سابقًا)، يمكنك رفع وتشغيل برنامج MicroPython بسيط باستخدام أداة مثل Thonny IDE، وهي مناسبة للمبتدئين ومستخدمة على نطاق واسع لتطوير MicroPython. فيما يلي الخطوات لإعداد MicroPython ورفع برنامج بسيط إلى لوحتك Pico.

---

### المتطلبات الأساسية
1.  **MicroPython مثبت**: لقد قمت مسبقًا بنسخ ملف `RPI_PICO-20250415-v1.25.0.uf2` إلى محرك الأقراص `RPI-RP2، وأعيد تشغيل لوحة Pico (يجب أن يختفي محرك الأقراص `RPI-RP2`).
2.  **اتصال USB**: لوحة Pico موصولة بجهاز الكمبيوتر الخاص بك عبر كابل USB يدعم نقل البيانات.
3.  **Thonny IDE**: قم بتثبيت Thonny إذا لم تكن قد قمت بذلك بالفعل:
    *   **Linux**: قم بتثبيت Thonny باستخدام مدير الحزم الخاص بك أو قم بتنزيله من [thonny.org](https://thonny.org).
        ```bash
        sudo apt update
        sudo apt install thonny
        ```
    *   بدلاً من ذلك، يمكنك استخدام `pip`:
        ```bash
        pip install thonny
        ```
    *   لأنظمة Windows/macOS، قم بالتنزيل والتثبيت من [thonny.org](https://thonny.org).

---

### دليل خطوة بخطوة لرفع برنامج MicroPython بسيط

1.  **قم بتوصيل لوحة Pico وافتح Thonny**:
    *   قم بتوصيل لوحة Pico بمنفذ USB في جهاز الكمبيوتر الخاص بك.
    *   افتح Thonny IDE.

2.  **تهيئة Thonny ليعمل مع MicroPython**:
    *   في Thonny، انتقل إلى **Tools > Options > Interpreter** (أو **Run > Select interpreter**).
    *   اختر **MicroPython (Raspberry Pi Pico)** من القائمة المنسدلة للمفسر (Interpreter).
    *   إذا لم يظهر منفذ الاتصال التسلسلي (Serial Port) للوحة Pico (مثل `/dev/ttyACM0` على Linux) تلقائيًا:
        *   تحقق من المنافذ المتاحة في القائمة المنسدلة أو قم بتنفيذ الأمر `ls /dev/tty*` في الطرفية (Terminal) لتحديد منفذ لوحة Pico (عادةً `/dev/ttyACM0` أو ما شابه).
        *   اختر المنفذ الصحيح يدويًا.
    *   انقر على **OK** للحفظ.

3.  **تأكد من أن MicroPython يعمل**:
    *   في نافذة **Shell** في Thonny (اللوحة السفلية)، يجب أن ترى موجه (REPL) خاص بـ MicroPython مثل:
        ```
        >>>
        ```
    *   اختبره بكتابة أمر بسيط، مثل:
        ```python
        print("Hello, Pico!")
        ```
        اضغط على Enter، ويجب أن ترى الناتج في نافذة Shell.

4.  **اكتب برنامج MicroPython بسيط**:
    *   في محرر Thonny الرئيسي، أنشئ ملفًا جديدًا واكتب برنامجًا بسيطًا. على سبيل المثال، برنامج لإضاءة LED المدمج في لوحة Pico وإطفائه (على منفذ GPIO 25 للوحة Pico العادية، أو استخدام "LED" للوحة Pico W):
        ```python
        from machine import Pin
        import time

        # تهيئة LED المدمج
        led = Pin(25, Pin.OUT)  # استخدم "LED" بدلاً من 25 للوحة Pico W

        # جعل LED يومض
        while True:
            led.on()           # شغّل LED
            time.sleep(0.5)    # انتظر 0.5 ثانية
            led.off()          # أوقف LED
            time.sleep(0.5)    # انتظر 0.5 ثانية
        ```
    *   ملاحظة: إذا كنت تستخدم لوحة Pico W، فاستبدل `Pin(25, Pin.OUT)` بـ `Pin("LED", Pin.OUT)`.

5.  **احفظ البرنامج على لوحة Pico**:
    *   انقر على **File > Save As**.
    *   في مربع الحوار، اختر **Raspberry Pi Pico** كوجهة الحفظ (وليس جهاز الكمبيوتر الخاص بك).
    *   سمّ الملف `main.py` (حيث يقوم MicroPython بتشغيل `main.py` تلقائيًا عند بدء التشغيل) أو اسمًا آخر مثل `blink.py`.
    *   انقر على **OK** لحفظ الملف على نظام ملفات لوحة Pico.

6.  **شغّل البرنامج**:
    *   انقر على زر **Run** الأخضر (أو اضغط على **F5**) في Thonny لتنفيذ البرنامج.
    *   بدلاً من ذلك، إذا قمت بحفظه باسم `main.py`، فأعد ضبط لوحة Pico (افصلها وأعد توصيلها، أو اضغط على زر RESET إذا كان متاحًا)، وسيعمل البرنامج تلقائيًا.
    *   يجب أن ترى LED المدمج يومض كل 0.5 ثانية.

7.  **أوقف البرنامج** (إذا لزم الأمر):
    *   لإيقاف البرنامج، اضغط على **Ctrl+C** في نافذة Shell الخاصة بـ Thonny لإيقاف النص البرمجي قيد التشغيل.
    *   لإزالة `main.py` حتى لا يعمل تلقائيًا، احذفه من لوحة Pico:
        *   في Thonny، انتقل إلى **View > Files**، اختر نظام ملفات لوحة Pico، انقر بزر الماوس الأيمن على `main.py`، واختر **Delete**.

---

### الاختبار واستكشاف الأخطاء وإصلاحها
*   **لا يظهر موجه REPL**: إذا لم تظهر نافذة Shell موجه MicroPython REPL:
    *   تأكد من اختيار المنفذ الصحيح في إعدادات المفسر (Interpreter).
    *   تحقق من تثبيت MicroPython بشكل صحيح. إذا لم يكن الأمر كذلك، أعد تثبيت ملف `.uf2` كما هو موضح سابقًا.
    *   تحقق من كابل USB (يجب أن يدعم نقل البيانات) وجرب منفذًا مختلفًا.
*   **LED لا يومض**: تأكد من استخدام منفذ GPIO الصحيح (`25` للوحة Pico العادية، `"LED"` للوحة Pico W). إذا كان لا يزال لا يعمل، اختبر LED باستخدام أمر بسيط في REPL:
    ```python
    from machine import Pin
    led = Pin(25, Pin.OUT)
    led.on()
    ```
*   **الملف لا يتم حفظه**: تأكد من أن Thonny متصل بلوحة Pico وأن المفسر مضبوط على MicroPython (Raspberry Pi Pico).

---

### نصائح إضافية
*   **استخدام أدوات أخرى**: إلى جانب Thonny، يمكنك استخدام `rshell` أو `ampy` لإدارة الملفات على لوحة Pico:
    ```bash
    pip install rshell
    rshell --port /dev/ttyACM0
    cp blink.py /pyboard/main.py
    ```
*   **المزيد من البرامج الأمثلة**:
    *   قراءة ضغطة زر (على سبيل المثال، على منفذ GPIO 14):
        ```python
        from machine import Pin
        button = Pin(14, Pin.IN, Pin.PULL_UP)
        while True:
            print(button.value())
        ```
    *   التحكم في LED خارجي أو أطراف طرفية أخرى عن طريق ضبط رقم منفذ GPIO.
*   **التشغيل التلقائي**: حفظ ملف باسم `main.py` يجعله يعمل تلقائيًا عند بدء التشغيل. استخدم `boot.py` لكتابة كود إعداد يعمل قبل `main.py`.

إذا واجهت مشاكل محددة (مثل اكتشاف المنفذ، أخطاء في Thonny، أو مشاكل في العتاد)، أو إذا أردت تجربة برنامج مختلف، فأخبرني وسأرشدك أكثر!