---
audio: false
generated: true
lang: hi
layout: post
title: आर्डुइनो और टेलीग्राम अलर्ट के साथ स्मार्ट वाशिंग मशीन मॉनिटर
translated: true
type: note
---

अपने Maytag MHW8630HW वॉशिंग मशीन के रुकने का पता लगाने के लिए (इसकी पैनल लाइट को संकेतक के रूप में उपयोग करके) और आपको अपने कपड़े टांगने के लिए Telegram बॉट के माध्यम से सूचित करने वाली एक प्रणाली बनाने के लिए, आप मशीन की स्थिति की निगरानी करने के लिए एक कैमरा मॉड्यूल के साथ Arduino का उपयोग कर सकते हैं। टेक स्टैक, हार्डवेयर सेटअप, एल्गोरिदम और कार्यान्वयन चरणों पर एक विस्तृत मार्गदर्शिका नीचे दी गई है।

---

### टेक स्टैक
#### हार्डवेयर
1. **Arduino बोर्ड**:
   - **ESP32-CAM** (अनुशंसित) – एक माइक्रोकंट्रोलर को बिल्ट-इन OV2640 कैमरा और Wi-Fi क्षमता के साथ जोड़ता है, जो इमेज प्रोसेसिंग और Telegram एकीकरण के लिए एकदम सही है।
   - विकल्प: Arduino Uno + अलग कैमरा मॉड्यूल (जैसे, OV7670) और Wi-Fi के लिए ESP8266, लेकिन यह सेटअप करने में अधिक जटिल है।
2. **कैमरा मॉड्यूल**:
   - OV2640 (ESP32-CAM के साथ शामिल) – पैनल लाइट का पता लगाने के लिए पर्याप्त 2MP कैमरा।
3. **लाइट सेंसर (वैकल्पिक)**:
   - फोटोरेसिस्टर (LDR) या TSL2561 – रिडंडेंसी या सरल सेटअप के लिए कैमरा-आधारित लाइट डिटेक्शन के पूरक के रूप में।
4. **पावर सप्लाई**:
   - ESP32-CAM के लिए 5V USB पावर एडाप्टर या बैटरी पैक।
5. **माउंटिंग**:
   - वॉशिंग मशीन के कंट्रोल पैनल के स्पष्ट दृश्य के साथ, ESP32-CAM को रखने के लिए छोटा एन्क्लोजर या 3D-प्रिंटेड केस।
6. **Wi-Fi राउटर**:
   - इंटरनेट से कनेक्ट होने और Telegram बॉट के साथ संचार करने के लिए ESP32-CAM के लिए।

#### सॉफ्टवेयर
1. **Arduino IDE**:
   - ESP32-CAM को प्रोग्राम करने के लिए।
2. **लाइब्रेरीज़**:
   - **Universal Arduino Telegram Bot Library** by Brian Lough – Telegram बॉट एकीकरण के लिए।
   - **ArduinoJson** – Telegram API संचार के लिए JSON डेटा को हैंडल करने के लिए।
   - **ESP32-CAM कैमरा लाइब्रेरीज़** – छवियों को कैप्चर करने और प्रोसेस करने के लिए बिल्ट-इन लाइब्रेरीज़।
3. **Telegram बॉट**:
   - Telegram पर BotFather का उपयोग करके एक बॉट बनाएं और एक बॉट टोकन और चैट ID प्राप्त करें।
4. **प्रोग्रामिंग लैंग्वेज**:
   - C++ (Arduino स्केच)।
5. **वैकल्पिक टूल्स**:
   - Arduino पर पोर्ट करने से पहले कंप्यूटर पर इमेज प्रोसेसिंग एल्गोरिदम के प्रोटोटाइप के लिए OpenCV (Python) (ESP32-CAM के लिए सरलीकृत)।

---

### वॉशिंग मशीन स्थिति का पता लगाने के लिए एल्गोरिदम
चूंकि Maytag MHW8630HW में एक पैनल लाइट है जो इंगित करती है कि मशीन चालू है, आप इस लाइट का पता लगाने के लिए कैमरे का उपयोग कर सकते हैं। एल्गोरिदम मशीन की स्थिति का संकेत देने वाली लाइट के चालू या बंद होने का निर्धारण करने के लिए छवियों को प्रोसेस करेगा।

#### डिटेक्शन एल्गोरिदम
1. **इमेज कैप्चर**:
   - ESP32-CAM का उपयोग करके वॉशिंग मशीन के कंट्रोल पैनल की छवियों को समय-समय पर कैप्चर करें।
2. **रुचि का क्षेत्र (ROI) चयन**:
   - छवि में एक विशिष्ट क्षेत्र परिभाषित करें जहां पैनल लाइट स्थित है (जैसे, पावर इंडिकेटर के चारों ओर एक आयताकार क्षेत्र)।
3. **इमेज प्रोसेसिंग**:
   - **ग्रेस्केल रूपांतरण**: प्रोसेसिंग को सरल बनाने के लिए कैप्चर की गई छवि को ग्रेस्केल में बदलें।
   - **थ्रेशोल्डिंग**: लाइट की उपस्थिति का पता लगाने के लिए एक चमक थ्रेशोल्ड लागू करें। पैनल लाइट चालू होने पर एक चमकदार स्थान उत्पन्न करेगी, जबकि बंद होने पर एक गहरे क्षेत्र की तुलना में।
   - **पिक्सेल तीव्रता विश्लेषण**: ROI में औसत पिक्सेल तीव्रता की गणना करें। उच्च तीव्रता इंगित करती है कि लाइट चालू है, जबकि कम तीव्रता इंगित करती है कि यह बंद है।
4. **स्टेट मशीन**:
   - लगातार रीडिंग के आधार पर मशीन की स्थिति (ON या OFF) ट्रैक करें।
   - यदि लाइट को लगातार कई चक्रों के लिए ON के रूप में पाया जाता है, तो मान लें कि मशीन चल रही है।
   - यदि लाइट OFF में बदल जाती है और एक निर्धारित अवधि (जैसे, 5 मिनट) के लिए बंद रहती है, तो मान लें कि वॉश चक्र पूरा हो गया है।
5. **डिबाउंसिंग**:
   - वॉश चक्र में विराम (जैसे, सोकिंग या भरने) के दौरान गलत सूचनाओं से बचने के लिए मशीन के रुकने की पुष्टि करने के लिए एक विलंब (जैसे, 5 मिनट) लागू करें।
6. **सूचना**:
   - जब मशीन के रुकने की पुष्टि हो जाए, तो एक Telegram संदेश भेजें (जैसे, "वॉशिंग मशीन रुक गई! कपड़े टांगने का समय आ गया है।")।

#### अधिक जटिल एल्गोरिदम का उपयोग क्यों नहीं?
- उन्नत एल्गोरिदम जैसे मशीन लर्निंग (जैसे, ऑब्जेक्ट डिटेक्शन के लिए CNNs) इस कार्य के लिए अत्यधिक हैं और ESP32-CAM की सीमित प्रोसेसिंग शक्ति के लिए संसाधन-गहन हैं।
- साधारण थ्रेशोल्डिंग पर्याप्त है क्योंकि पैनल लाइट एक स्पष्ट बाइनरी संकेतक (ON/OFF) है।

---

### कार्यान्वयन मार्गदर्शिका
#### चरण 1: Telegram बॉट सेट करें
1. **एक Telegram बॉट बनाएं**:
   - Telegram खोलें, **@BotFather** खोजें, और एक चैट शुरू करें।
   - `/newbot` भेजें, अपने बॉट का नाम दें (जैसे, "WasherBot"), और **Bot Token** प्राप्त करें।
   - अपने बॉट को `/start` भेजें और `@GetIDsBot` जैसी सेवा का उपयोग करके या अपने कोड में आने वाले संदेशों को जांचकर अपनी **Chat ID** प्राप्त करें।
2. **अपने फोन पर Telegram इंस्टॉल करें**:
   - सुनिश्चित करें कि आप अपने बॉट से संदेश प्राप्त कर सकते हैं।

#### चरण 2: हार्डवेयर सेटअप
1. **ESP32-CAM की स्थिति निर्धारित करें**:
   - ESP32-CAM को एक छोटे एन्क्लोजर में या चिपकने वाले टेप के साथ माउंट करें, जो वॉशिंग मशीन के कंट्रोल पैनल की ओर हो।
   - सुनिश्चित करें कि कैमरे का पैनल लाइट का स्पष्ट दृश्य है (एक नमूना फोटो के साथ परीक्षण करें)।
   - सेटअप को हिलने-डुलने से बचाने के लिए सुरक्षित करें, क्योंकि इससे ROI की स्थिरता प्रभावित हो सकती है।
2. **ESP32-CAM को पावर दें**:
   - ESP32-CAM के 5V पिन से 5V USB पावर एडाप्टर या बैटरी पैक कनेक्ट करें।
   - स्थिर बिजली स्रोत सुनिश्चित करें, क्योंकि कैमरा और Wi-Fi महत्वपूर्ण शक्ति का उपभोग करते हैं।
3. **वैकल्पिक लाइट सेंसर**:
   - यदि फोटोरेसिस्टर का उपयोग कर रहे हैं, तो इसे ESP32-CAM के एक एनालॉग पिन (जैसे, GPIO 4) से वोल्टेज डिवाइडर सर्किट (जैसे, ग्राउंड के लिए 10kΩ रेसिस्टर) के साथ कनेक्ट करें।

#### चरण 3: सॉफ्टवेयर सेटअप
1. **Arduino IDE इंस्टॉल करें**:
   - [arduino.cc](https://www.arduino.cc/en/software) से Arduino IDE डाउनलोड करें और इंस्टॉल करें।
2. **ESP32 बोर्ड सपोर्ट जोड़ें**:
   - Arduino IDE में, **File > Preferences** पर जाएं, Additional Boards Manager URLs में निम्न URL जोड़ें:
     ```
     https://raw.githubusercontent.com/espressif/arduino-esp32/master/package_esp32_index.json
     ```
   - **Tools > Board > Boards Manager** पर जाएं, "ESP32" खोजें, और ESP32 पैकेज इंस्टॉल करें।
3. **लाइब्रेरीज़ इंस्टॉल करें**:
   - **Universal Arduino Telegram Bot Library** इंस्टॉल करें:
     - [GitHub](https://github.com/witnessmenow/Universal-Arduino-Telegram-Bot) से डाउनलोड करें और **Sketch > Include Library > Add .ZIP Library** के माध्यम से जोड़ें।
   - **ArduinoJson** इंस्टॉल करें:
     - **Sketch > Include Library > Manage Libraries** पर जाएं, "ArduinoJson" खोजें, और वर्जन 6.x.x इंस्टॉल करें।
4. **Wi-Fi कॉन्फ़िगर करें**:
   - सुनिश्चित करें कि आपका ESP32-CAM आपके घरेलू Wi-Fi नेटवर्क (2.4GHz, क्योंकि 5GHz सपोर्टेड नहीं है) से कनेक्ट हो सकता है।

#### चरण 4: Arduino कोड लिखें
नीचे पैनल लाइट का पता लगाने और Telegram सूचनाएं भेजने के लिए ESP32-CAM के लिए एक नमूना Arduino स्केच दिया गया है। यह कोड मानता है कि आपने पैनल लाइट के लिए ROI निर्देशांक की पहचान कर ली है।

```cpp
#include <WiFi.h>
#include <UniversalTelegramBot.h>
#include <ArduinoJson.h>
#include "esp_camera.h"

// Wi-Fi क्रेडेंशियल्स
#define WIFI_SSID "your_wifi_ssid"
#define WIFI_PASSWORD "your_wifi_password"

// Telegram Bot क्रेडेंशियल्स
#define BOT_TOKEN "your_bot_token"
#define CHAT_ID "your_chat_id"

// कैमरा कॉन्फ़िगरेशन (ESP32-CAM के लिए)
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

#define ROI_X 100 // कैमरा दृश्य के आधार पर समायोजित करें (ROI का x-निर्देशांक)
#define ROI_Y 100 // ROI का y-निर्देशांक
#define ROI_WIDTH 50 // ROI की चौड़ाई
#define ROI_HEIGHT 50 // ROI की ऊंचाई
#define THRESHOLD 150 // चमक थ्रेशोल्ड (0-255)
#define STOP_DELAY 300000 // मिलीसेकंड में 5 मिनट

bool machineRunning = false;
unsigned long lastOnTime = 0;

void setup() {
  Serial.begin(115200);

  // कैमरा इनिशियलाइज़ करें
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
  config.pixel_format = PIXFORMAT_GRAYSCALE; // सरलता के लिए ग्रेस्केल
  config.frame_size = FRAMESIZE_QVGA; // 320x240
  config.jpeg_quality = 12;
  config.fb_count = 1;

  esp_err_t err = esp_camera_init(&config);
  if (err != ESP_OK) {
    Serial.printf("Camera init failed with error 0x%x", err);
    return;
  }

  // Wi-Fi से कनेक्ट करें
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("WiFi connected");

  // Telegram क्लाइंट कॉन्फ़िगर करें
  client.setInsecure(); // सरलता के लिए; प्रोडक्शन में उचित SSL पर विचार करें
}

void loop() {
  // इमेज कैप्चर करें
  camera_fb_t *fb = esp_camera_framebuffer_get();
  if (!fb) {
    Serial.println("Camera capture failed");
    return;
  }

  // ROI में औसत चमक की गणना करें
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

  // स्टेट मशीन
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

  delay(10000); // हर 10 सेकंड में जांचें
}
```

#### चरण 5: कोड को कस्टमाइज़ करें
1. **क्रेडेंशियल्स अपडेट करें**:
   - `your_wifi_ssid`, `your_wifi_password`, `your_bot_token`, और `your_chat_id` को अपने वास्तविक मानों से बदलें।
2. **ROI और थ्रेशोल्ड ट्यून करें**:
   - ESP32-CAM का उपयोग करके एक टेस्ट इमेज कैप्चर करें (एसडी कार्ड पर इमेज सेव करने या इसे स्ट्रीम करने के लिए कोड संशोधित करें)।
   - पैनल लाइट पर ध्यान केंद्रित करने के लिए इमेज का विश्लेषण करके ROI निर्देशांक (`ROI_X`, `ROI_Y`, `ROI_WIDTH`, `ROI_HEIGHT`) निर्धारित करें।
   - टेस्ट इमेज के आधार पर `THRESHOLD` समायोजित करें (जैसे, ON होने पर उज्जवल, OFF होने पर गहरा)।
3. **`STOP_DELAY` समायोजित करें**:
   - चक्र विराम के दौरान गलत सूचनाओं से बचने के लिए 300000 (5 मिनट) पर सेट करें।

#### चरण 6: परीक्षण और डिप्लॉयमेंट
1. **कोड अपलोड करें**:
   - ESP32-CAM को USB-to-serial एडाप्टर (जैसे, FTDI मॉड्यूल) के माध्यम से अपने कंप्यूटर से कनेक्ट करें।
   - Arduino IDE में **ESP32 Wrover Module** चुनें और स्केच अपलोड करें।
2. **सिस्टम का परीक्षण करें**:
   - वॉशिंग मशीन शुरू करें और स्थिति परिवर्तनों के लिए Serial Monitor की निगरानी करें।
   - मशीन के रुकने पर Telegram सूचनाओं की पुष्टि करें।
3. **फाइन-ट्यून**:
   - यदि गलत सकारात्मक/नकारात्मक परिणाम होते हैं तो ROI, थ्रेशोल्ड, या विलंब समायोजित करें।
4. **स्थायी इंस्टॉलेशन**:
   - ESP32-CAM को उसके एन्क्लोजर में सुरक्षित करें और एक स्थिर बिजली आपूर्ति सुनिश्चित करें।

---

### वैकल्पिक दृष्टिकोण: लाइट सेंसर
यदि कैमरा-आधारित डिटेक्शन बहुत जटिल या अविश्वसनीय है (जैसे, परिवेश प्रकाश के कारण), तो एक फोटोरेसिस्टर का उपयोग करें:
- **सेटअप**: एक फोटोरेसिस्टर को पैनल लाइट से जोड़ें (जैसे, टेप के साथ) और इसे एक एनालॉग पिन से कनेक्ट करें।
- **कोड संशोधन**: इमेज प्रोसेसिंग को एनालॉग रीडिंग से बदलें:
  ```cpp
  int lightValue = analogRead(A0); // GPIO 4 पर फोटोरेसिस्टर
  if (lightValue > 500) { // थ्रेशोल्ड समायोजित करें
    machineRunning = true;
    lastOnTime = millis();
  } else if (machineRunning && (millis() - lastOnTime > STOP_DELAY)) {
    machineRunning = false;
    bot.sendMessage(CHAT_ID, "Washing machine stopped! Time to hang up clothes.", "");
  }
  ```
- **फायदे**: सरल, कम संसाधन-गहन।
- **नुकसान**: लाइट से भौतिक संलग्नता की आवश्यकता होती है, कम लचीला।

---

### नोट्स
- **पावर खपत**: ESP32-CAM कैमरा और Wi-Fi का उपयोग करते समय महत्वपूर्ण शक्ति का उपभोग करता है। एक विश्वसनीय बिजली स्रोत सुनिश्चित करें।
- **परिवेश प्रकाश**: कैमरा-आधारित डिटेक्शन कमरे की रोशनी से प्रभावित हो सकता है। विभिन्न परिस्थितियों में परीक्षण करें या मजबूती के लिए लाइट सेंसर का उपयोग करें।
- **सुरक्षा**: नमूना कोड सरलता के लिए `setInsecure()` का उपयोग करता है। प्रोडक्शन के लिए, Telegram संचार के लिए उचित SSL प्रमाणपत्र कॉन्फ़िगर करें।
- **संदर्भ**: यह दृष्टिकोण ESP32-CAM Telegram सुरक्षा प्रणाली और कंपन सेंसर का उपयोग करने वाले लॉन्ड्री मॉनिटर जैसी परियोजनाओं से प्रेरित है, जिसे प्रकाश-आधारित डिटेक्शन के लिए अनुकूलित किया गया है।[](https://www.instructables.com/Home-Security-System-Using-ESP32-CAM-and-Telegram-/)[](https://www.instructables.com/Arduino-Washer-Dryer-Alert-Push-Notification-to-Ph/)

---

### समस्या निवारण
- **कैमरा इनिशियलाइज़ करने में विफल**: वायरिंग जांचें, पर्याप्त बिजली सुनिश्चित करें, और कैमरा कॉन्फ़िगरेशन सत्यापित करें।
- **Wi-Fi कनेक्शन समस्याएं**: 2.4GHz Wi-Fi और सही क्रेडेंशियल्स की पुष्टि करें।
- **कोई Telegram संदेश नहीं**: बॉट टोकन और चैट ID सत्यापित करें, त्रुटियों के लिए Serial Monitor जांचें।
- **गलत सूचनाएं**: चक्र विराम के लिए `THRESHOLD` या `STOP_DELAY` समायोजित करें।

यह समाधान आपकी वॉशिंग मशीन की निगरानी करने और आपको Telegram के माध्यम से सूचित करने के लिए एक लागत-प्रभावी, गैर-आक्रामक तरीके से ESP32-CAM की क्षमताओं का लाभ उठाता है। यदि आपको विशिष्ट चरणों या डिबगिंग में सहायता की आवश्यकता है तो मुझे बताएं!