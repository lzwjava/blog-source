---
audio: false
generated: true
lang: ar
layout: post
title: راسبيري باي مقابل أردوينو لمراقبة الغسالة مع تنبيهات تلغرام
translated: true
type: note
---

استخدام Raspberry Pi بدلاً من Arduino (مثل ESP32-CAM) للكشف عن توقف غسالتك Maytag MHW8630HW وإرسال إشعار عبر Telegram هو بديل قابل للتطبيق، حيث يقدم قوة معالجة أكبر ومرونة على حساب زيادة التعقيد واستهلاك الطاقة. أدناه، سأقارن بين نهج Raspberry Pi وحل Arduino، وأحدد خيارات المتحكمات الدقيقة الأخرى، وأقدم دليلاً مفصلاً لتنفيذ النظام باستخدام Raspberry Pi. سأناقش أيضاً النهج البديلة (مثل الأجهزة أو أجهزة الاستشعار الأخرى) لضمان رد شامل.

---

### المقارنة: Raspberry Pi مقابل Arduino مقابل الخيارات الأخرى

| **الميزة**                | **Raspberry Pi**                                                                 | **Arduino (ESP32-CAM)**                                                  | **الخيارات الأخرى (مثل NodeMCU, ESP8266)**                              |
|----------------------------|----------------------------------------------------------------------------------|-------------------------------------------------------------------------|-------------------------------------------------------------------------|
| **قوة المعالجة**       | عالية (وحدة معالجة مركزية رباعية النوى، 1-8 جيجابايت ذاكرة عشوائية) – تدعم معالجة الصور المتقدمة، OpenCV.    | محدودة (نواة مزدوجة، 520 كيلوبايت SRAM) – معالجة أساسية للصور فقط.           | محدودة جداً – غير مناسبة لمعالجة تعتمد على الكاميرا.                 |
| **دعم الكاميرا**         | سهل مع كاميرات الويب USB أو Pi Camera Module (مثلاً، 8MP Pi Camera v2).             | كاميرا مدمجة OV2640 (2MP)، لكن بدقة وجودة أقل.          | يتطلب وحدة كاميرا خارجية، معقدة للتكامل.                  |
| **Wi-Fi**                 | مدمج (في معظم الموديلات، مثلاً، Pi 4, Zero 2 W).                                   | مدمج (ESP32-CAM).                                                  | مدمج (مثلاً، ESP8266)، لكن لا يوجد دعم أصلي للكاميرا.                 |
| **البرمجة**            | Python، OpenCV، متعدد الاستخدامات لكنه يتطلب إعداد نظام التشغيل (Raspberry Pi OS).              | C++ في Arduino IDE، أبسط للمبتدئين.                              | C++ أو Lua (مثلاً، NodeMCU)، مكتبات محدودة لمعالجة الصور.     |
| **استهلاك الطاقة**      | أعلى (~2.5 واط لـ Pi Zero، ~5-10 واط لـ Pi 4).                                    | أقل (~1-2 واط لـ ESP32-CAM).                                           | الأقل (~0.5-1 واط لـ ESP8266).                                          |
| **التكلفة**                   | 10 دولارات (Pi Zero W) إلى 35+ دولار (Pi 4) + 15 دولار لـ Pi Camera.                            | ~10 دولارات (ESP32-CAM مع الكاميرا).                                          | ~5-10 دولارات (ESP8266/NodeMCU) + تكلفة أجهزة الاستشعار.                               |
| **سهولة الإعداد**          | متوسطة (إعداد نظام التشغيل، برمجة Python).                                             | سهل (Arduino IDE، sketch واحد).                                      | سهل لأجهزة الاستشعار البسيطة، معقد للكاميرات.                           |
| **أفضل حالة استخدام**          | معالجة الصور المتقدمة، مرن للتوسعات المستقبلية (مثلاً، نماذج ML).    | حل بسيط ومنخفض التكلفة للكشف عن الضوء مع تكامل Telegram.             | حلول لا تعتمد على الكاميرا (مثلاً، أجهزة استشعار الاهتزاز أو التيار).              |

**مزايا Raspberry Pi**:
- معالجة صور فائقة باستخدام OpenCV للكشف القوي عن الضوء.
- أسهل في تصحيح الأخطاء والتوسع (مثلاً، إضافة واجهة ويب أو أجهزة استشعار متعددة).
- يدعم كاميرات ذات جودة أعلى لدقة أفضل في ظروف الإضاءة المختلفة.

**عيوب Raspberry Pi**:
- يتطلب إعداداً أكثر (تثبيت نظام التشغيل، بيئة Python).
- استهلاك طاقة أعلى، أقل مثالية للإعدادات التي تعمل بالبطارية.
- أغلى ثمناً من ESP32-CAM.

**خيارات أخرى**:
- **NodeMCU/ESP8266**: مناسبة للحلول التي لا تعتمد على الكاميرا (مثلاً، استخدام مستشعر الاهتزاز أو مستشعر التيار). قوة المعالجة المحدودة تجعل دمج الكاميرا غير عملي.
- **مستشعر الاهتزاز**: يكتشف اهتزازات الآلة بدلاً من ضوء اللوحة. بسيط لكنه قد يفوت التغيرات الدقيقة في الدورة.
- **مستشعر التيار**: يقيس استهلاك الطاقة (مثلاً، وحدة ACS712) للكشف عن توقف الآلة. غير تدخلي لكنه يتطلب إعداداً كهربائياً.

---

### دليل تنفيذ Raspberry Pi

#### Tech Stack
**الأجهزة**:
1. **Raspberry Pi**:
   - **Raspberry Pi Zero 2 W** (15 دولاراً، مضغوط، مزود بـ Wi-Fi) أو **Raspberry Pi 4** (35+ دولاراً، أكثر قوة).
2. **الكاميرا**:
   - **Raspberry Pi Camera Module v2** (15 دولاراً، 8MP) أو كاميرا ويب USB.
3. **مزود الطاقة**:
   - 5V USB-C (لـ Pi 4) أو micro-USB (لـ Pi Zero) بمخرج 2-3A.
4. **التثبيت**:
   - علبة أو حامل لاصق لوضع الكاميرا مقابل ضوء لوحة الغسالة.

**البرمجيات**:
1. **نظام التشغيل**: Raspberry Pi OS (Lite للكفاءة، Full للإعداد الأسهل).
2. **لغة البرمجة**: Python.
3. **المكتبات**:
   - **OpenCV**: لمعالجة الصور للكشف عن ضوء اللوحة.
   - **python-telegram-bot**: لإشعارات Telegram.
   - **picamera2** (لـ Pi Camera) أو **fswebcam** (لكاميرا الويب USB).
4. **بوت Telegram**: نفس إعداد Arduino (استخدم BotFather للحصول على رمز البوت ومعرف الدردشة).

#### الخوارزمية
الخوارزمية مشابهة لنهج Arduino لكنها تستفيد من OpenCV لمعالجة صور أكثر قوة:
1. **التقاط الصورة**: استخدم Pi Camera أو كاميرا ويب لالتقاط الصور بشكل دوري (مثلاً، كل 10 ثوانٍ).
2. **منطقة الاهتمام (ROI)**: حدد مستطيلاً حول ضوء اللوحة في الصورة.
3. **معالجة الصورة**:
   - التحويل إلى التدرج الرمادي.
   - تطبيق Gaussian blur لتقليل الضوضاء.
   - استخدام adaptive thresholding للكشف عن ضوء اللوحة الساطع مقابل الخلفية.
   - حساب متوسط شدة البكسل في ROI أو عد البكسلات الساطعة.
4. **آلة الحالة**:
   - إذا كانت ROI مضيئة (الضوء ON)، ضع علامة على أن الآلة تعمل.
   - إذا كانت ROI مظلمة (الضوء OFF) لمدة 5 دقائق، ضع علامة على أن الآلة متوقفة وأرسل إشعار Telegram.
5. **إزالة الارتداد Debouncing**: نفذ تأخيراً لمدة 5 دقائق لتأكيد توقف الآلة.

#### خطوات التنفيذ
1. **إعداد Raspberry Pi**:
   - حمّل وانسخ **Raspberry Pi OS** (Lite أو Full) على بطاقة SD باستخدام Raspberry Pi Imager.
   - صل الـ Pi بـ Wi-Fi عن طريق تحرير `/etc/wpa_supplicant/wpa_supplicant.conf` أو باستخدام الواجهة الرسومية.
   - فعّل واجهة الكاميرا عبر `raspi-config` (Interfacing Options > Camera).

2. **تثبيت التبعيات**:
   ```bash
   sudo apt update
   sudo apt install python3-opencv python3-picamera2 python3-pip
   pip3 install python-telegram-bot
   ```

3. **وضع الكاميرا**:
   - ثبت Pi Camera أو كاميرا الويب USB لمواجهة ضوء لوحة الغسالة.
   - اختبر الكاميرا باستخدام:
     ```bash
     libcamera-still -o test.jpg
     ```
     أو لكاميرا الويب USB:
     ```bash
     fswebcam test.jpg
     ```

4. **سكريبت Python**:
أدناه نموذج لسكريبت Python لـ Raspberry Pi للكشف عن ضوء اللوحة وإرسال إشعارات Telegram.

```python
import cv2
import numpy as np
from picamera2 import Picamera2
import telegram
import asyncio
import time

# إعدادات بوت Telegram
BOT_TOKEN = "your_bot_token"
CHAT_ID = "your_chat_id"
bot = telegram.Bot(token=BOT_TOKEN)

# إعدادات الكاميرا
picam2 = Picamera2()
picam2.configure(picam2.create_still_configuration(main={"size": (640, 480)}))
picam2.start()

# إعدادات ROI (اضبط بناءً على منظر الكاميرا)
ROI_X, ROI_Y, ROI_WIDTH, ROI_HEIGHT = 200, 150, 50, 50
THRESHOLD = 150  # حد السطوع (0-255)
STOP_DELAY = 300  # 5 دقائق بالثواني

machine_running = False
last_on_time = 0

async def send_telegram_message(message):
    await bot.send_message(chat_id=CHAT_ID, text=message)

def is_light_on(frame):
    # التحويل إلى التدرج الرمادي
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # تطبيق Gaussian blur
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    # استخراج ROI
    roi = gray[ROI_Y:ROI_Y+ROI_HEIGHT, ROI_X:ROI_X+ROI_WIDTH]
    # حساب متوسط السطوع
    avg_brightness = np.mean(roi)
    return avg_brightness > THRESHOLD

async def main():
    global machine_running, last_on_time
    while True:
        # التقاط صورة
        frame = picam2.capture_array()
        # التحقق مما إذا كان الضوء مضاءً
        if is_light_on(frame):
            if not machine_running:
                machine_running = True
                print("Machine is ON")
            last_on_time = time.time()
        else:
            if machine_running and (time.time() - last_on_time > STOP_DELAY):
                machine_running = False
                print("Machine stopped")
                await send_telegram_message("Washing machine stopped! Time to hang up clothes.")
        time.sleep(10)  # التحقق كل 10 ثوانٍ

if __name__ == "__main__":
    asyncio.run(main())
```

5. **تخصيص السكريبت**:
   - استبدل `BOT_TOKEN` و `CHAT_ID` ببيانات اعتماد Telegram الخاصة بك.
   - اضبط `ROI_X`, `ROI_Y`, `ROI_WIDTH`, `ROI_HEIGHT` عن طريق التقاط صورة اختبارية وتحليلها بأداة مثل GIMP أو Python لتحديد موقع ضوء اللوحة.
   - اضبط `THRESHOLD` بناءً على الصور الاختبارية (قيمة أعلى للضوء الأسطع).
   - عدل `STOP_DELAY` إذا لزم الأمر.

6. **تشغيل السكريبت**:
   ```bash
   python3 washer_monitor.py
   ```
   - شغله في الخلفية باستخدام `nohup python3 washer_monitor.py &` أو استخدم خدمة systemd للموثوقية.

7. **الاختبار والنشر**:
   - ابدأ تشغيل الغسالة وراقب ناتج السكريبت.
   - تحقق من إشعارات Telegram.
   - ثبت الـ Pi والكاميرا في الإعداد الدائم.

---

### بدائل أخرى
1. **مستشعر الاهتزاز**:
   - **الأجهزة**: استخدم مستشعر اهتزاز (مثلاً، SW-420) مع ESP8266 أو Raspberry Pi.
   - **الإعداد**: ثبت المستشعر على الغسالة لاكتشاف الاهتزازات.
   - **الخوارزمية**: راقب الغياب المستمر للاهتزازات (مثلاً، 5 دقائق) للكشف عن توقف الآلة.
   - **الإيجابيات**: بسيط، منخفض التكلفة، غير متأثر بالضوء المحيط.
   - **السلبيات**: قد يفوت الدورات ذات التوقفات الطويلة (مثلاً، النقع).
   - **مثال على الكود (ESP8266)**:
     ```cpp
     #include <ESP8266WiFi.h>
     #include <UniversalTelegramBot.h>
     #define VIBRATION_PIN D5
     #define BOT_TOKEN "your_bot_token"
     #define CHAT_ID "your_chat_id"
     WiFiClientSecure client;
     UniversalTelegramBot bot(BOT_TOKEN, client);
     bool machineRunning = false;
     unsigned long lastVibrationTime = 0;
     void setup() {
       pinMode(VIBRATION_PIN, INPUT);
       WiFi.begin("ssid", "password");
       while (WiFi.status() != WL_CONNECTED) delay(500);
       client.setInsecure();
     }
     void loop() {
       if (digitalRead(VIBRATION_PIN)) {
         machineRunning = true;
         lastVibrationTime = millis();
       } else if (machineRunning && (millis() - lastVibrationTime > 300000)) {
         machineRunning = false;
         bot.sendMessage(CHAT_ID, "Washing machine stopped!", "");
       }
       delay(1000);
     }
     ```

2. **مستشعر التيار**:
   - **الأجهزة**: استخدم مستشعر تيار ACS712 مع ESP8266 أو Raspberry Pi.
   - **الإعداد**: ثبت المستشعر بشكل غير تدخلي حول سلك الطاقة الخاص بالغسالة.
   - **الخوارزمية**: اكتشف عندما ينخفض التيار تحت عتبة معينة (مثلاً، <0.5A) لمدة 5 دقائق.
   - **الإيجابيات**: دقيق، غير تدخلي.
   - **السلبيات**: يتطلب معرفة كهربائية، معايرة لاستهلاك طاقة الآلة.

3. **الميكروفونات**:
   - **الأجهزة**: استخدم وحدة ميكروفون (مثلاً، KY-038) مع Raspberry Pi.
   - **الخوارزمية**: حلل مستويات الصوت لاكتشاف توقف ضوضاء الآلة.
   - **الإيجابيات**: غير بصري، يعمل في ظروف الإضاءة المنخفضة.
   - **السلبيات**: حساس للضوضاء المحيطة، يتطلب معالجة إشارة.

---

### التوصية
- **Raspberry Pi**: الأفضل لمعالجة الصور القوية والقابلية للتوسع في المستقبل. استخدمه إذا كنت مرتاحاً مع Python وتريد موثوقية عالية في ظروف الإضاءة المختلفة.
- **Arduino (ESP32-CAM)**: الأفضل لإعداد بسيط ومنخفض التكلفة. مثالي إذا كنت تريد الحد الأدنى من التكوين وكنت موافقاً على معالجة الصور الأساسية.
- **مستشعر الاهتزاز أو التيار**: الأفضل لحلول لا تعتمد على الكاميرا، خاصة إذا كان ضوء اللوحة غير موثوق (مثلاً، خافت أو محجوب). استخدم مع ESP8266 للبساطة.
- **الميكروفون**: أقل موثوقية بسبب الضوضاء المحيطة، لكنه قابل للتطبيق كمستشعر ثانوي.

لبيتك المكون من طابقين، يعد Raspberry Pi أو ESP32-CAM مع كاميرا مثالياً لأنك في الطابق الثاني وتحتاج إلى إشعارات موثوقة عن بُعد عبر Telegram. يقدم Raspberry Pi دقة أفضل للكشف عن الضوء، بينما ESP32-CAM أرخص وأبسط في النشر. إذا كنت تفضل نهجاً لا يعتمد على الكاميرا، فإن مستشعر الاهتزاز مع ESP8266 هو البديل الأسهل.

دعني أعلم إذا كنت تريد تعمقاً أكبر في أي نهج محدد، أو تحتاج مساعدة في الإعداد، أو تريد كوداً لمستشعر بديل!