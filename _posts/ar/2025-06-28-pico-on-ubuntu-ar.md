---
audio: false
generated: true
lang: ar
layout: post
title: إعداد راسبيري باي بيكو على أوبونتو
translated: true
type: note
---

لاستخدام **Raspberry Pi Pico** على **Ubuntu**، تحتاج إلى إعداد بيئة التطوير، وتثبيت البرامج اللازمة، وتكوين الأدوات لبرمجة الـ Pico. يدعم الـ Pico البرمجة باستخدام **MicroPython**، أو **C/C++**، أو **CircuitPython**. أدناه، أشرح الخطوات والبرامج المطلوبة لكل نهج، مع التركيز على الإعدادات الأكثر شيوعًا.

### المتطلبات العامة
- **Raspberry Pi Pico** (أو Pico W) مع كابل USB (Micro-USB لـ Pico، USB-C لـ Pico 2).
- نظام **Ubuntu** (مثل Ubuntu 20.04 أو 22.04 أو إصدار أحدث؛ تفترض هذه التعليمات إصدارًا حديثًا مثل 24.04).
- معرفة أساسية باستخدام الطرفية (Terminal).

### الخيار 1: البرمجة باستخدام MicroPython
تعتبر MicroPython الطريقة الأكثر ملاءمة للمبتدئين لبرمجة الـ Pico. إنها تطبيق خفيف الوزن لـ Python مصمم للمتحكمات الدقيقة (microcontrollers).

#### البرامج المطلوب تثبيتها
1. **برنامج Microduino الثابت (Firmware)**
   - حمّل أحدث ملف برنامج ثابت من نوع UF2 لـ MicroPython الخاص بـ Raspberry Pi Pico من [موقع MicroPython الرسمي](https://micropython.org/download/rp2-pico/) أو [صفحة Raspberry Pi Pico](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html).
   - بالنسبة لـ Pico W أو Pico 2، تأكد من اختيار البرنامج الثابت المناسب (مثل `rp2-pico-w` لـ Pico W).

2. **Python 3**
   - عادةً ما يتضمن Ubuntu Python 3 بشكل افتراضي. تحقق من ذلك باستخدام:
     ```bash
     python3 --version
     ```
   - إذا لم يكن مثبتًا، قم بتثبيته:
     ```bash
     sudo apt update
     sudo apt install python3 python3-pip
     ```

3. **بيئة Thonny للتطوير المتكاملة (موصى بها للمبتدئين)**
   - Thonny هي بيئة تطوير بسيطة لبرمجة الـ Pico باستخدام MicroPython.
   - قم بتثبيت Thonny:
     ```bash
     sudo apt install thonny
     ```
   - بدلاً من ذلك، استخدم `pip` للحصول على أحدث إصدار:
     ```bash
     pip3 install thonny
     ```

4. **اختياري: `picotool` (لإدارة متقدمة)**
   - أداة مفيدة لإدارة برنامج MicroPython الثابت أو فحص الـ Pico.
   - قم بتثبيت `picotool`:
     ```bash
     sudo apt install picotool
     ```

#### خطوات الإعداد
1. **تثبيت برنامج MicroPython الثابت**
   - صل الـ Pico بجهاز Ubuntu الخاص بك عبر USB مع الاستمرار في الضغط على زر **BOOTSEL** (هذا يضع الـ Pico في وضع bootloader).
   - سيظهر الـ Pico كجهاز تخزين USB (مثل `RPI-RP2`).
   - اسحب ملف الـ `.uf2` الذي تم تنزيله وأفلته على مساحة التخزين الخاصة بالـ Pico. سيعيد الـ Pico التشغيل تلقائيًا مع تثبيت MicroPython.

2. **تكوين Thonny**
   - افتح Thonny: اكتب `thonny` في الطرفية أو عبر قائمة التطبيقات.
   - انتقل إلى **Tools > Options > Interpreter**.
   - اختر **MicroPython (Raspberry Pi Pico)** كمفسر (interpreter).
   - اخرب المنفذ (port) الصحيح (مثل `/dev/ttyACM0`). يمكنك تشغيل `ls /dev/tty*` في الطرفية لتحديد المنفذ إذا لزم الأمر.
   - يجب أن يتصل Thonny الآن بالـ Pico، مما يسمح لك بكتابة وتشغيل نصوص Python.

3. **اختبار برنامج**
   - في Thonny، اكتب نصًا برمجيًا بسيطًا، مثل:
     ```python
     from machine import Pin
     led = Pin(25, Pin.OUT)  # LED المدمج (GP25 لـ Pico)
     led.toggle()  # تبديل حالة LED تشغيل/إيقاف
     ```
   - انقر على زر **Run** لتنفيذ الكود على الـ Pico.

4. **اختياري: استخدام `picotool`**
   - تحقق من حالة الـ Pico:
     ```bash
     picotool info
     ```
   - تأكد من أن الـ Pico متصل وفي وضع bootloader إذا لزم الأمر.

### الخيار 2: البرمجة باستخدام C/C++
للمستخدمين المتقدمين، يمكن برمجة الـ Pico باستخدام C/C++ عبر **Pico SDK** الرسمي.

#### البرامج المطلوب تثبيتها
1. **Pico SDK وأدوات السلسلة (Toolchain)**
   - قم بتثبيت الأدوات المطلوبة لبناء برامج C/C++:
     ```bash
     sudo apt update
     sudo apt install cmake gcc-arm-none-eabi libnewlib-arm-none-eabi build-essential git
     ```

2. **Pico SDK**
   - انسخ مستودع Pico SDK:
     ```bash
     git clone -b master https://github.com/raspberrypi/pico-sdk.git
     cd pico-sdk
     git submodule update --init
     ```
   - عيّن متغير البيئة `PICO_SDK_PATH`:
     ```bash
     export PICO_SDK_PATH=~/pico-sdk
     echo 'export PICO_SDK_PATH=~/pico-sdk' >> ~/.bashrc
     ```

3. **اختياري: أمثلة Pico**
   - انسخ أمثلة Pico للاستئناس بها:
     ```bash
     git clone -b master https://github.com/raspberrypi/pico-examples.git
     ```

4. **Visual Studio Code (اختياري)**
   - لتجربة تطوير أفضل، قم بتثبيت VS Code:
     ```bash
     sudo snap install code --classic
     ```
   - قم بتثبيت إضافات **CMake Tools** و **C/C++** في VS Code.

#### خطوات الإعداد
1. **إعداد مشروع**
   - أنشئ دليلاً جديدًا لمشروعك، مثل `my-pico-project`.
   - انسخ ملف `CMakeLists.txt` نموذجي من `pico-examples` أو أنشئ واحدًا:
     ```cmake
     cmake_minimum_required(VERSION 3.13)
     include($ENV{PICO_SDK_PATH}/pico_sdk_init.cmake)
     project(my_project C CXX ASM)
     pico_sdk_init()
     add_executable(my_project main.c)
     pico_add_extra_outputs(my_project)
     target_link_libraries(my_project pico_stdlib)
     ```
   - اكتب برنامجًا بسيطًا بلغة C (مثل `main.c`):
     ```c
     #include "pico/stdlib.h"
     int main() {
         const uint LED_PIN = 25;
         gpio_init(LED_PIN);
         gpio_set_dir(LED_PIN, GPIO_OUT);
         while (true) {
             gpio_put(LED_PIN, 1);
             sleep_ms(500);
             gpio_put(LED_PIN, 0);
             sleep_ms(500);
         }
     }
     ```

2. **البناء والتنفيذ (Build and Flash)**
   - انتقل إلى دليل مشروعك:
     ```bash
     cd my-pico-project
     mkdir build && cd build
     cmake ..
     make
     ```
   - سينشئ هذا ملف `.uf2` (مثل `my_project.uf2`).
   - اضغط باستمرار على زر **BOOTSEL** في الـ Pico، وصله via USB، وانسخ ملف `.uf2` إلى مساحة تخزين الـ Pico:
     ```bash
     cp my_project.uf2 /media/$USER/RPI-RP2/
     ```

3. **التصحيح (اختياري)**
   - قم بتثبيت `openocd` للتصحيح:
     ```bash
     sudo apt install openocd
     ```
   - استخدم مصحح أخطاء (debugger) (مثل Pico آخر كـ debug probe) وشغّل:
     ```bash
     openocd -f interface/raspberrypi-swd.cfg -f target/rp2040.cfg
     ```

### الخيار 3: البرمجة باستخدام CircuitPython
CircuitPython هو خيار آخر قائم على Python، مشابه لـ MicroPython ولكنه يركز على نظام Adafruit.

#### البرامج المطلوب تثبيتها
1. **برنامج CircuitPython الثابت (Firmware)**
   - حمّل ملف CircuitPython UF2 الخاص بالـ Pico من [موقع Adafruit CircuitPython](https://circuitpython.org/board/raspberry_pi_pico/).
   - بالنسبة لـ Pico W أو Pico 2، اختر البرنامج الثابت المناسب.

2. **Python 3 والأدوات**
   - نفس المتطلبات الخاصة بـ MicroPython (Python 3، Thonny، إلخ).

#### خطوات الإعداد
1. **تثبيت برنامج CircuitPython الثابت**
   - مشابه لـ MicroPython: اضغط باستمرار على **BOOTSEL**، صل الـ Pico، وانسخ ملف CircuitPython `.uf2` إلى مساحة تخزين الـ Pico.
   - يعيد الـ Pico التشغيل كقرص USB اسمه `CIRCUITPY`.

2. **البرمجة باستخدام Thonny أو محرر نصوص**
   - استخدم Thonny كما هو موضح في قسم MicroPython، واختر **CircuitPython** كمفسر (interpreter).
   - بدلاً من ذلك، يمكنك تحرير ملف `code.py` مباشرة على قرص `CIRCUITPY` باستخدام أي محرر نصوص.
   - مثال لـ `code.py`:
     ```python
     import board
     import digitalio
     import time
     led = digitalio.DigitalInOut(board.LED)
     led.direction = digitalio.Direction.OUTPUT
     while True:
         led.value = True
         time.sleep(0.5)
         led.value = False
         time.sleep(0.5)
     ```

### ملاحظات إضافية
- **الصلاحيات**: إذا كان منفذ الـ Pico (مثل `/dev/ttyACM0`) غير قابل للوصول، أضف مستخدمك إلى مجموعة `dialout`:
  ```bash
  sudo usermod -a -G dialout $USER
  ```
  سجّل الخروج ثم أدخل مرة أخرى للتطبيق.

- **اعتبارات Pico W**: بالنسبة لـ Pico W، تأكد من استخدام برنامج ثابت مخصص له (مثل MicroPython مع دعم Wi-Fi). تتطلب برمجة Wi-Fi مكتبات إضافية، مثل `network` لـ MicroPython.

- **Pico 2**: قد يتطلب Raspberry Pi Pico 2 الأحدث (مع RP2350) إصدارات محدثة من البرنامج الثابت أو SDK. تحقق من وثائق Raspberry Pi الرسمية للتأكد من التوافق.

- **استكشاف الأخطاء وإصلاحها**:
  - إذا لم يظهر الـ Pico في وضع bootloader، تحقق مرة أخرى من كابل USB (يجب أن يدعم نقل البيانات، وليس الطاقة فقط).
  - شغّل `lsusb` أو `dmesg` لتأكيد اكتشاف Ubuntu للـ Pico.
  - لبناء برامج C/C++، تأكد من تعيين مسار Pico SDK بشكل صحيح.

### النهج الموصى به
- **للمبتدئين**: استخدم **MicroPython مع Thonny** للبساطة والإعداد السريع.
- **للمستخدمين المتقدمين**: استخدم **C/C++ مع Pico SDK** للأداء والتحكم على مستوى منخفض.
- **لمستخدمي نظام Adafruit**: استخدم **CircuitPython** إذا كنت تخطط لاستخدام مكتبات أو أجهزة Adafruit.

إذا كان لديك مشروع محدد أو تفضيل برمجة معين، فأخبرني، وسأقوم بتخصيص التعليمات بشكل أكبر!