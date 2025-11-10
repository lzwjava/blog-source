---
audio: false
generated: true
lang: ar
layout: post
title: مراقب الغسالة الذكية باستخدام الأردوينو وتنبيهات تلغرام
translated: true
type: note
---

لإنشاء نظام يكتشف عندما يتوقف غسالة Maytag MHW8630HW (باستخدام ضوء اللوحة كمؤشر) ويخطرك عبر بوت Telegram لتعليق ملابسك، يمكنك استخدام Arduino مع وحدة كاميرا لمراقبة حالة الغسالة. فيما يلي دليل مفصل حول مجموعة التقنيات، وإعداد الأجهزة، والخوارزمية، وخطوات التنفيذ.

---

### مجموعة التقنيات
#### الأجهزة
1. **لوحة Arduino**:
   - **ESP32-CAM** (موصى به) – يجمع بين متحكم دقيق مع كاميرا OV2640 مدمجة وإمكانية Wi-Fi، مثالي لمعالجة الصور والتكامل مع Telegram.
   - بديل: Arduino Uno + وحدة كاميرا منفصلة (مثل OV7670) و ESP8266 لـ Wi-Fi، لكن هذا أكثر تعقيدًا في الإعداد.
2. **وحدة الكاميرا**:
   - OV2640 (مضمنة مع ESP32-CAM) – كاميرا 2 ميجابكسل كافية لاكتشاف ضوء اللوحة.
3. **مستشعر الضوء (اختياري)**:
   - مقاومة ضوئية (LDR) أو TSL2561 – لتكملة اكتشاف الضوء المعتمد على الكاميرا للتكرار أو الإعدادات الأبسط.
4. **مزود الطاقة**:
   - محول طاقة USB 5V أو حزمة بطارية لـ ESP32-CAM.
5. **التثبيت**:
   - علبة صغيرة أو حاوية مطبوعة ثلاثية الأبعاد لحمل ESP32-CAM، مع توفير رؤية واضحة للوحة تحكم الغسالة.
6. **موجه Wi-Fi**:
   - ليتصل ESP32-CAM بالإنترنت ويتواصل مع بوت Telegram.

#### البرمجيات
1. **Arduino IDE**:
   - لبرمجة ESP32-CAM.
2. **المكتبات**:
   - **Universal Arduino Telegram Bot Library** بواسطة Brian Lough – للتكامل مع بوت Telegram.
   - **ArduinoJson** – للتعامل مع بيانات JSON لاتصال Telegram API.
   - **مكتبات كاميرا ESP32-CAM** – المكتبات المدمجة لالتقاط ومعالجة الصور.
3. **بوت Telegram**:
   - استخدم BotFather على Telegram لإنشاء بوت والحصول على رمز البوت ومعرف الدردشة.
4. **لغة البرمجة**:
   - C++ (sketch Arduino).
5. **أدوات اختيارية**:
   - OpenCV (Python) لوضع نماذج أولية لخوارزميات معالجة الصور على الكمبيوتر قبل نقلها إلى Arduino (مبسط لـ ESP32-CAM).

---

### خوارزمية لاكتشاف حالة الغسالة
نظرًا لأن غسالة Maytag MHW8630HW تحتوي على ضوء لوحة يشير إلى تشغيل الجهاز، يمكنك استخدام الكاميرا لاكتشاف هذا الضوء. ستقوم الخوارزمية بمعالجة الصور لتحديد ما إذا كان الضوء مضاءً أم مطفأ، مما يشير إلى حالة الغسالة.

#### خوارزمية الكشف
1. **التقاط الصورة**:
   - قم بالتقاط صور دورية للوحة تحكم الغسالة باستخدام ESP32-CAM.
2. **تحديد منطقة الاهتمام (ROI)**:
   - حدد منطقة معينة في الصورة حيث يقع ضوء اللوحة (مثل منطقة مستطيلة حول مؤشر الطاقة).
3. **معالجة الصورة**:
   - **التحويل إلى التدرج الرمادي**: قم بتحويل الصورة الملتقطة إلى تدرج رمادي لتبسيط المعالجة.
   - **العتبة**: طبق عتبة سطوع لاكتشاف وجود الضوء. سيُنتج ضوء اللوحة بقعة مضيئة عند التشغيل، مقارنة بمنطقة أغمق عند الإيقاف.
   - **تحليل شدة البكسل**: احسب متوسط شدة البكسل في منطقة الاهتمام. تشير الشدة العالية إلى أن الضوء مضاء، بينما تشير الشدة المنخفضة إلى أنه مطفأ.
4. **آلة الحالة**:
   - تتبع حالة الغسالة (تشغيل أو إيقاف) بناءً على القراءات المتتالية.
   - إذا تم اكتشاف الضوء كـ "مضاء" لعدة دورات، افترض أن الغسالة تعمل.
   - إذا تحول الضوء إلى "مطفأ" وبقي مطفأًا لفترة محددة (مثل 5 دقائق)، افترض أن دورة الغسيل اكتملت.
5. **إزالة الارتداد**:
   - نفذ تأخيرًا (مثل 5 دقائق) لتأكيد توقف الغسالة، وتجنب الإشعارات الخاطئة أثناء التوقفات في دورة الغسيل (مثل النقع أو الملء).
6. **الإشعار**:
   - عندما يتم تأكيد توقف الغسالة، أرسل رسالة عبر Telegram (مثل "توقفت الغسالة! حان الوقت لتعليق الملابس.").

#### لماذا لا تستخدم خوارزميات أكثر تعقيدًا؟
- الخوارزميات المتقدمة مثل التعلم الآلي (مثل الشبكات العصبية الالتفافية لاكتشاف الكائنات) مبالغ فيها لهذه المهمة وتستهلك الكثير من الموارد بالنسبة لقوة المعالجة المحدودة لـ ESP32-CAM.
- العتبة البسيطة كافية لأن ضوء اللوحة هو مؤشر ثنائي واضح (تشغيل/إيقاف).

---

### دليل التنفيذ
#### الخطوة 1: إعداد بوت Telegram
1. **إنشاء بوت Telegram**:
   - افتح Telegram، وابحث عن **@BotFather**، وابدأ محادثة.
   - أرسل `/newbot`، سمّ بوتك (مثل "WasherBot")، واحصل على **رمز البوت**.
   - أرسل `/start` إلى بوتك واحصل على **معرف الدردشة** الخاص بك باستخدام خدمة مثل `@GetIDsBot` أو عن طريق التحقق من الرسائل الواردة في الكود الخاص بك.
2. **ثبّت Telegram على هاتفك**:
   - تأكد من أنه يمكنك استقبال الرسائل من بوتك.

#### الخطوة 2: إعداد الأجهزة
1. **ضع ESP32-CAM في مكانه**:
   - ثبّت ESP32-CAM في علبة صغيرة أو بشريط لاصق، مواجهًا لوحة تحكم الغسالة.
   - تأكد من أن الكاميرا لها رؤية واضحة لضوء اللوحة (اختبر بصورة نموذجية).
   - ثبت الإعداد لتجنب الحركة، لأن هذا قد يؤثر على اتساق منطقة الاهتمام.
2. **شغّل ESP32-CAM**:
   - وصّل محول طاقة USB 5V أو حزمة بطارية بطرف 5V في ESP32-CAM.
   - تأكد من وجود مصدر طاقة مستقر، لأن الكاميرا و Wi-Fi تستهلكان طاقة كبيرة.
3. **مستشعر الضوء (اختياري)**:
   - إذا كنت تستخدم مقاومة ضوئية، فوصّلها بطرف تماثلي على ESP32-CAM (مثل GPIO 4) مع دائرة مقسم الجهد (مثل مقاوم 10 كيلو أوم إلى الأرض).

#### الخطوة 3: إعداد البرمجيات
1. **ثبّت Arduino IDE**:
   - نزّل وثبّت Arduino IDE من [arduino.cc](https://www.arduino.cc/en/software).
2. **أضف دعم لوحة ESP32**:
   - في Arduino IDE، انتقل إلى **File > Preferences**، أضف عنوان URL التالي إلى "Additional Boards Manager URLs":
     ```
     https://raw.githubusercontent.com/espressif/arduino-esp32/master/package_esp32_index.json
     ```
   - انتقل إلى **Tools > Board > Boards Manager**، ابحث عن "ESP32"، وثبّت حزمة ESP32.
3. **ثبّت المكتبات**:
   - ثبّت **Universal Arduino Telegram Bot Library**:
     - نزّلها من [GitHub](https://github.com/witnessmenow/Universal-Arduino-Telegram-Bot) وأضفها عبر **Sketch > Include Library > Add .ZIP Library**.
   - ثبّت **ArduinoJson**:
     - انتقل إلى **Sketch > Include Library > Manage Libraries**، ابحث عن "ArduinoJson"، وثبّت الإصدار 6.x.x.
4. **اضبط Wi-Fi**:
   - تأكد من أن ESP32-CAM يمكنه الاتصال بشبكة Wi-Fi المنزلية (2.4 جيجا هرتز، حيث أن 5 جيجا هرتز غير مدعوم).

#### الخطوة 4: اكتب كود Arduino
فيما يلي نموذج لـ sketch Arduino لـ ESP32-CAM لاكتشاف ضوء اللوحة وإرسال إشعارات Telegram. يفترض هذا الكود أنك حددت إحداثيات منطقة الاهتمام لضوء اللوحة.

```cpp
#include <WiFi.h>
#include <UniversalTelegramBot.h>
#include <ArduinoJson.h>
#include "esp_camera.h"

// بيانات اعتماد Wi-Fi
#define WIFI_SSID "your_wifi_ssid"
#define WIFI_PASSWORD "your_wifi_password"

// بيانات اعتماد بوت Telegram
#define BOT_TOKEN "your_bot_token"
#define CHAT_ID "your_chat_id"

// تكوين الكاميرا (لـ ESP32-CAM)
#define PWDN_GPIO_NUM 32
#define RESET_GPIO_NUM -1
#define XCLK_GPIO_NUM 0
#define SIOD_GPIO_NUM 26
#define SIOC_GPIO_NUM 27
#define Y9_GPIO_NUM 35
#define Y8_GPIO_NUM 34
#define Y7_GPIO_NUM 39
#define Y6_GPIO_NUM 36
#define Y5_GPIO_NUM 21
#define Y4_GPIO_NUM 19
#define Y3_GPIO_NUM 18
#define Y2_GPIO_NUM 5
#define VSYNC_GPIO_NUM 25
#define HREF_GPIO_NUM 23
#define PCLK_GPIO_NUM 22

WiFiClientSecure client;
UniversalTelegramBot bot(BOT_TOKEN, client);

#define ROI_X 100 // اضغط بناءً على رؤية الكاميرا (الإحداثي X لمنطقة الاهتمام)
#define ROI_Y 100 // الإحداثي Y لمنطقة الاهتمام
#define ROI_WIDTH 50 // عرض منطقة الاهتمام
#define ROI_HEIGHT 50 // ارتفاع منطقة الاهتمام
#define THRESHOLD 150 // عتبة السطوع (0-255)
#define STOP_DELAY 300000 // 5 دقائق بالمللي ثانية

bool machineRunning = false;
unsigned long lastOnTime = 0;

void setup() {
  Serial.begin(115200);

  // تهيئة الكاميرا
  camera_config_t config;
  config.ledc_channel = LEDC_CHANNEL_0;
  config.ledc_timer = LEDC_TIMER_0;
  config.pin_d0 = Y2_GPIO_NUM;
  config.pin_d1 = Y3_GPIO_NUM;
  config.pin_d2 = Y4_GPIO_NUM;
  config.pin_d3 = Y5_GPIO_NUM;
  config.pin_d4 = Y6_GPIO_NUM;
  config.pin_d5 = Y7_GPIO_NUM;
  config.pin_d6 = Y8_GPIO_NUM;
  config.pin_d7 = Y9_GPIO_NUM;
  config.pin_xclk = XCLK_GPIO_NUM;
  config.pin_pclk = PCLK_GPIO_NUM;
  config.pin_vsync = VSYNC_GPIO_NUM;
  config.pin_href = HREF_GPIO_NUM;
  config.pin_sscb_sda = SIOD_GPIO_NUM;
  config.pin_sscb_scl = SIOC_GPIO_NUM;
  config.pin_pwdn = PWDN_GPIO_NUM;
  config.pin_reset = RESET_GPIO_NUM;
  config.xclk_freq_hz = 20000000;
  config.pixel_format = PIXFORMAT_GRAYSCALE; // التدرج الرمادي للتبسيط
  config.frame_size = FRAMESIZE_QVGA; // 320x240
  config.jpeg_quality = 12;
  config.fb_count = 1;

  esp_err_t err = esp_camera_init(&config);
  if (err != ESP_OK) {
    Serial.printf("Camera init failed with error 0x%x", err);
    return;
  }

  // الاتصال بـ Wi-Fi
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("WiFi connected");

  // تكوين عميل Telegram
  client.setInsecure(); // للتبسيط؛ فكر في استخدام شهادات SSL مناسبة في الإنتاج
}

void loop() {
  // التقاط صورة
  camera_fb_t *fb = esp_camera_framebuffer_get();
  if (!fb) {
    Serial.println("Camera capture failed");
    return;
  }

  // حساب متوسط السطوع في منطقة الاهتمام
  uint32_t totalBrightness = 0;
  uint16_t pixelCount = 0;
  for (int y = ROI_Y; y < ROI_Y + ROI_HEIGHT; y++) {
    for (int x = ROI_X; x < ROI_X + ROI_WIDTH; x++) {
      if (x < fb->width && y < fb->height) {
        totalBrightness += fb->buf[y * fb->width + x];
        pixelCount++;
      }
    }
  }
  esp_camera_framebuffer_return(fb);

  float avgBrightness = pixelCount > 0 ? (float)totalBrightness / pixelCount : 0;

  // آلة الحالة
  if (avgBrightness > THRESHOLD) {
    if (!machineRunning) {
      machineRunning = true;
      Serial.println("Machine is ON");
    }
    lastOnTime = millis();
  } else {
    if (machineRunning && (millis() - lastOnTime > STOP_DELAY)) {
      machineRunning = false;
      Serial.println("Machine stopped");
      bot.sendMessage(CHAT_ID, "Washing machine stopped! Time to hang up clothes.", "");
    }
  }

  delay(10000); // التحقق كل 10 ثوانٍ
}
```

#### الخطوة 5: تخصيص الكود
1. **حدّث بيانات الاعتماد**:
   - استبدل `your_wifi_ssid`، `your_wifi_password`، `your_bot_token`، و `your_chat_id` بقيمك الفعلية.
2. **اضبط منطقة الاهتمام والعتبة**:
   - التقط صورة اختبارية باستخدام ESP32-CAM (عدّل الكود لحفظ صورة على بطاقة SD أو بثها).
   - حدد إحداثيات منطقة الاهتمام (`ROI_X`, `ROI_Y`, `ROI_WIDTH`, `ROI_HEIGHT`) عن طريق تحليل الصورة للتركيز على ضوء اللوحة.
   - اضبط `THRESHOLD` بناءً على الصور الاختبارية (مثل، أكثر سطوعًا عند التشغيل، أغمق عند الإيقاف).
3. **اضبط `STOP_DELAY`**:
   - عيّنه على 300000 (5 دقائق) لتجنب الإشعارات الخاطئة أثناء توقفات الدورة.

#### الخطوة 6: اختبر ونفّذ
1. **حمّل الكود**:
   - وصّل ESP32-CAM بجهاز الكمبيوتر عبر محول USB-to-serial (مثل وحدة FTDI).
   - اختر **ESP32 Wrover Module** في Arduino IDE وحمّل الـ sketch.
2. **اختبر النظام**:
   - ابدأ تشغيل الغسالة وراقب Serial Monitor لتغييرات الحالة.
   - تحقق من إشعارات Telegram عندما تتوقف الغسالة.
3. **اضبط بدقة**:
   - اضبط منطقة الاهتمام، أو العتبة، أو التأخير إذا حدثت إيجابيات/سلبيات خاطئة.
4. **التثبيت الدائم**:
   - ثبت ESP32-CAM في علبته وتأكد من وجود مصدر طاقة مستقر.

---

### نهج بديل: مستشعر الضوء
إذا كان الكشف المعتمد على الكاميرا معقدًا جدًا أو غير موثوق (بسبب ضوء الغرفة، على سبيل المثال)، استخدم مقاومة ضوئية:
- **الإعداد**: اربط مقاومة ضوئية بضوء اللوحة (باستخدام شريط، مثلاً) ووصّلها بطرف تماثلي.
- **تعديل الكود**: استبدل معالجة الصور بقراءات تماثلية:
  ```cpp
  int lightValue = analogRead(A0); // المقاومة الضوئية على GPIO 4
  if (lightValue > 500) { // اضبط العتبة
    machineRunning = true;
    lastOnTime = millis();
  } else if (machineRunning && (millis() - lastOnTime > STOP_DELAY)) {
    machineRunning = false;
    bot.sendMessage(CHAT_ID, "Washing machine stopped! Time to hang up clothes.", "");
  }
  ```
- **الإيجابيات**: أبسط، أقل استهلاكًا للموارد.
- **السلبيات**: يتطلب تثبيتًا فيزيائيًا على الضوء، أقل مرونة.

---

### ملاحظات
- **استهلاك الطاقة**: يستهلك ESP32-CAM طاقة كبيرة عند استخدام الكاميرا و Wi-Fi. تأكد من وجود مصدر طاقة موثوق.
- **ضوء الغرفة**: قد يتأثر الكشف المعتمد على الكاميرا بإضاءة الغرفة. اختبر في ظروف مختلفة أو استخدم مستشعر ضوء للمتانة.
- **الأمان**: يستخدم الكود النموذجي `setInsecure()` للتبسيط. للإنتاج، اضبط شهادات SSL مناسبة لاتصال Telegram.
- **المراجع**: يستلهم هذا النهج من مشاريع مثل نظام أمان ESP32-CAM لـ Telegram وأجهزة مراقبة الغسيل باستخدام مستشعرات الاهتزاز، مُعدّلة للكشف المعتمد على الضوء.[](https://www.instructables.com/Home-Security-System-Using-ESP32-CAM-and-Telegram-/)[](https://www.instructables.com/Arduino-Washer-Dryer-Alert-Push-Notification-to-Ph/)

---

### استكشاف الأخطاء وإصلاحها
- **فشل تهيئة الكاميرا**: تحقق من الأسلاك، تأكد من كفاية الطاقة، وتحقق من تكوين الكاميرا.
- **مشاكل اتصال Wi-Fi**: أكد على استخدام Wi-Fi بتردد 2.4 جيجا هرتز وبيانات الاعتماد الصحيحة.
- **لا توجد رسائل على Telegram**: تحقق من رمز البوت ومعرف الدردشة، وتحقق من Serial Monitor للبحث عن أخطاء.
- **إشعارات خاطئة**: اضبط `THRESHOLD` أو `STOP_DELAY` لمراعاة توقفات الدورة.

يستفيد هذا الحل من إمكانيات ESP32-CAM لطريقة فعالة من حيث التكلفة وغير تدخلية لمراقبة غسالتك وإشعارك عبر Telegram. أعلمني إذا كنت بحاجة إلى مساعدة في خطوات محددة أو تصحيح الأخطاء!