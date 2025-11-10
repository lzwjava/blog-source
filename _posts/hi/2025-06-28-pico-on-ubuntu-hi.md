---
audio: false
generated: true
lang: hi
layout: post
title: उबुन्टू पर रास्पबेरी पाई पाइको सेट अप करना
translated: true
type: note
---

**Raspberry Pi Pico** को **Ubuntu** पर उपयोग करने के लिए, आपको डेवलपमेंट एनवायरनमेंट सेट अप करना होगा, आवश्यक सॉफ़्टवेयर इंस्टॉल करना होगा और Pico को प्रोग्राम करने के लिए टूल्स को कॉन्फ़िगर करना होगा। Pico **MicroPython**, **C/C++**, या **CircuitPython** में प्रोग्रामिंग का समर्थन करता है। नीचे, मैं प्रत्येक दृष्टिकोण के लिए आवश्यक चरणों और सॉफ़्टवेयर का रूपरेखा प्रस्तुत करता हूं, जो सबसे आम सेटअप पर केंद्रित है।

### सामान्य आवश्यकताएँ
- **Raspberry Pi Pico** (या Pico W) एक USB केबल के साथ (Pico के लिए Micro-USB, Pico 2 के लिए USB-C)।
- **Ubuntu** सिस्टम (उदाहरण के लिए, Ubuntu 20.04, 22.04, या बाद का; ये निर्देश एक हाल के संस्करण जैसे 24.04 मानते हैं)।
- टर्मिनल से बुनियादी परिचितता।

### विकल्प 1: MicroPython के साथ प्रोग्रामिंग
MicroPython, Pico को प्रोग्राम करने का सबसे शुरुआत-अनुकूल तरीका है। यह माइक्रोकंट्रोलर के लिए डिज़ाइन किया गया एक हल्का Python इम्प्लीमेंटेशन है।

#### इंस्टॉल करने के लिए सॉफ़्टवेयर
1. **MicroPython फ़र्मवेयर**
   - [आधिकारिक MicroPython वेबसाइट](https://micropython.org/download/rp2-pico/) या [Raspberry Pi Pico पेज](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html) से Raspberry Pi Pico के लिए नवीनतम MicroPython UF2 फ़र्मवेयर फ़ाइल डाउनलोड करें।
   - Pico W या Pico 2 के लिए, सुनिश्चित करें कि आप उपयुक्त फ़र्मवेयर चुनते हैं (उदाहरण के लिए, Pico W के लिए `rp2-pico-w`)।

2. **Python 3**
   - Ubuntu में आमतौर पर Python 3 डिफ़ॉल्ट रूप से शामिल होता है। इसके साथ सत्यापित करें:
     ```bash
     python3 --version
     ```
   - यदि इंस्टॉल नहीं है, तो इसे इंस्टॉल करें:
     ```bash
     sudo apt update
     sudo apt install python3 python3-pip
     ```

3. **Thonny IDE** (शुरुआती लोगों के लिए अनुशंसित)
   - Thonny, MicroPython के साथ Pico को प्रोग्राम करने के लिए एक सरल IDE है।
   - Thonny इंस्टॉल करें:
     ```bash
     sudo apt install thonny
     ```
   - वैकल्पिक रूप से, नवीनतम संस्करण के लिए `pip` का उपयोग करें:
     ```bash
     pip3 install thonny
     ```

4. **वैकल्पिक: `picotool` (उन्नत प्रबंधन के लिए)**
   - MicroPython फ़र्मवेयर को प्रबंधित करने या Pico का निरीक्षण करने के लिए उपयोगी।
   - `picotool` इंस्टॉल करें:
     ```bash
     sudo apt install picotool
     ```

#### सेटअप चरण
1. **MicroPython फ़र्मवेयर इंस्टॉल करें**
   - **BOOTSEL** बटन दबाए रखते हुए Pico को अपने Ubuntu मशीन से USB के माध्यम से कनेक्ट करें (यह Pico को बूटलोडर मोड में डालता है)।
   - Pico एक USB स्टोरेज डिवाइस के रूप में दिखाई देता है (उदाहरण के लिए, `RPI-RP2`)।
   - डाउनलोड की गई MicroPython `.uf2` फ़ाइल को Pico की स्टोरेज पर ड्रैग और ड्रॉप करें। Pico स्वचालित रूप से MicroPython इंस्टॉल होने के साथ रीबूट हो जाएगा।

2. **Thonny कॉन्फ़िगर करें**
   - Thonny खोलें: टर्मिनल में `thonny` या एप्लिकेशन मेनू के माध्यम से।
   - **Tools > Options > Interpreter** पर जाएं।
   - इंटरप्रेटर के रूप में **MicroPython (Raspberry Pi Pico)** चुनें।
   - सही पोर्ट चुनें (उदाहरण के लिए, `/dev/ttyACM0`)। यदि आवश्यक हो तो पोर्ट की पहचान करने के लिए टर्मिनल में `ls /dev/tty*` चलाएं।
   - Thonny अब Pico से कनेक्ट होना चाहिए, जिससे आप Python स्क्रिप्ट लिख और चला सकते हैं।

3. **एक प्रोग्राम टेस्ट करें**
   - Thonny में, एक सरल स्क्रिप्ट लिखें, उदाहरण के लिए:
     ```python
     from machine import Pin
     led = Pin(25, Pin.OUT)  # ऑनबोर्ड LED (Pico के लिए GP25)
     led.toggle()  # LED ऑन/ऑफ टॉगल करें
     ```
   - Pico पर कोड निष्पादित करने के लिए **Run** बटन पर क्लिक करें।

4. **वैकल्पिक: `picotool` का उपयोग करें**
   - Pico की स्थिति सत्यापित करें:
     ```bash
     picotool info
     ```
   - यदि आवश्यक हो तो सुनिश्चित करें कि Pico कनेक्टेड है और बूटलोडर मोड में है।

### विकल्प 2: C/C++ के साथ प्रोग्रामिंग
अधिक उन्नत उपयोगकर्ताओं के लिए, Pico को आधिकारिक **Pico SDK** का उपयोग करके C/C++ में प्रोग्राम किया जा सकता है।

#### इंस्टॉल करने के लिए सॉफ़्टवेयर
1. **Pico SDK और टूलचेन**
   - C/C++ प्रोग्राम बनाने के लिए आवश्यक टूल्स इंस्टॉल करें:
     ```bash
     sudo apt update
     sudo apt install cmake gcc-arm-none-eabi libnewlib-arm-none-eabi build-essential git
     ```

2. **Pico SDK**
   - Pico SDK रिपॉजिटरी क्लोन करें:
     ```bash
     git clone -b master https://github.com/raspberrypi/pico-sdk.git
     cd pico-sdk
     git submodule update --init
     ```
   - `PICO_SDK_PATH` एनवायरनमेंट वेरिएबल सेट करें:
     ```bash
     export PICO_SDK_PATH=~/pico-sdk
     echo 'export PICO_SDK_PATH=~/pico-sdk' >> ~/.bashrc
     ```

3. **वैकल्पिक: Pico उदाहरण**
   - संदर्भ के लिए Pico उदाहरण क्लोन करें:
     ```bash
     git clone -b master https://github.com/raspberrypi/pico-examples.git
     ```

4. **Visual Studio Code (वैकल्पिक)**
   - बेहतर डेवलपमेंट अनुभव के लिए, VS Code इंस्टॉल करें:
     ```bash
     sudo snap install code --classic
     ```
   - VS Code में **CMake Tools** और **C/C++** एक्सटेंशन इंस्टॉल करें।

#### सेटअप चरण
1. **एक प्रोजेक्ट सेट अप करें**
   - अपने प्रोजेक्ट के लिए एक नया डायरेक्टरी बनाएं, उदाहरण के लिए, `my-pico-project`।
   - `pico-examples` से एक नमूना `CMakeLists.txt` कॉपी करें या बनाएं:
     ```cmake
     cmake_minimum_required(VERSION 3.13)
     include($ENV{PICO_SDK_PATH}/pico_sdk_init.cmake)
     project(my_project C CXX ASM)
     pico_sdk_init()
     add_executable(my_project main.c)
     pico_add_extra_outputs(my_project)
     target_link_libraries(my_project pico_stdlib)
     ```
   - एक सरल C प्रोग्राम लिखें (उदाहरण के लिए, `main.c`):
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

2. **बिल्ड और फ़्लैश करें**
   - अपने प्रोजेक्ट डायरेक्टरी में नेविगेट करें:
     ```bash
     cd my-pico-project
     mkdir build && cd build
     cmake ..
     make
     ```
   - यह एक `.uf2` फ़ाइल उत्पन्न करता है (उदाहरण के लिए, `my_project.uf2`)।
   - Pico पर **BOOTSEL** बटन दबाए रखें, इसे USB के माध्यम से कनेक्ट करें, और `.uf2` फ़ाइल को Pico की स्टोरेज पर कॉपी करें:
     ```bash
     cp my_project.uf2 /media/$USER/RPI-RP2/
     ```

3. **डीबगिंग (वैकल्पिक)**
   - डीबगिंग के लिए `openocd` इंस्टॉल करें:
     ```bash
     sudo apt install openocd
     ```
   - एक डीबगर का उपयोग करें (उदाहरण के लिए, डीबग प्रोब के रूप में एक और Pico) और चलाएं:
     ```bash
     openocd -f interface/raspberrypi-swd.cfg -f target/rp2040.cfg
     ```

### विकल्प 3: CircuitPython के साथ प्रोग्रामिंग
CircuitPython एक और Python-आधारित विकल्प है, जो MicroPython के समान है लेकिन Adafruit के इकोसिस्टम पर केंद्रित है।

#### इंस्टॉल करने के लिए सॉफ़्टवेयर
1. **CircuitPython फ़र्मवेयर**
   - [Adafruit CircuitPython वेबसाइट](https://circuitpython.org/board/raspberry_pi_pico/) से Pico के लिए CircuitPython UF2 फ़ाइल डाउनलोड करें।
   - Pico W या Pico 2 के लिए, उपयुक्त फ़र्मवेयर चुनें।

2. **Python 3 और टूल्स**
   - MicroPython के समान (Python 3, Thonny, आदि)।

#### सेटअप चरण
1. **CircuitPython फ़र्मवेयर इंस्टॉल करें**
   - MicroPython के समान: **BOOTSEL** दबाए रखें, Pico को कनेक्ट करें, और CircuitPython `.uf2` फ़ाइल को Pico की स्टोरेज पर कॉपी करें।
   - Pico `CIRCUITPY` नामक एक USB ड्राइव के रूप में रीबूट होता है।

2. **Thonny या टेक्स्ट एडिटर के साथ प्रोग्राम करें**
   - MicroPython सेक्शन में वर्णित अनुसार Thonny का उपयोग करें, इंटरप्रेटर के रूप में **CircuitPython** चुनें।
   - वैकल्पिक रूप से, किसी भी टेक्स्ट एडिटर का उपयोग करके `CIRCUITPY` ड्राइव पर सीधे `code.py` संपादित करें।
   - उदाहरण `code.py`:
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

### अतिरिक्त नोट्स
- **अनुमतियाँ**: यदि Pico का पोर्ट (उदाहरण के लिए, `/dev/ttyACM0`) एक्सेसिबल नहीं है, तो अपने उपयोगकर्ता को `dialout` समूह में जोड़ें:
  ```bash
  sudo usermod -a -G dialout $USER
  ```
  लागू करने के लिए लॉग आउट करें और वापस लॉग इन करें।

- **Pico W विचार**: Pico W के लिए, सुनिश्चित करें कि आप इसके लिए विशिष्ट फ़र्मवेयर का उपयोग करते हैं (उदाहरण के लिए, Wi-Fi सपोर्ट के साथ MicroPython)। Wi-Fi प्रोग्रामिंग के लिए अतिरिक्त लाइब्रेरीज़ की आवश्यकता होती है, जैसे MicroPython के लिए `network`।

- **Pico 2**: नया Raspberry Pi Pico 2 (RP2350 के साथ) के लिए अद्यतन फ़र्मवेयर या SDK संस्करणों की आवश्यकता हो सकती है। संगतता के लिए आधिकारिक Raspberry Pi दस्तावेज़ीकरण जांचें।

- **समस्या निवारण**:
  - यदि Pico बूटलोडर मोड में दिखाई नहीं देता है, तो USB केबल दोबारा जांचें (इसे केवल पावर ही नहीं, डेटा का भी समर्थन करना चाहिए)।
  - यह पुष्टि करने के लिए कि Ubuntu द्वारा Pico का पता लगाया गया है, `lsusb` या `dmesg` चलाएं।
  - C/C++ बिल्ड के लिए, सुनिश्चित करें कि Pico SDK पथ सही ढंग से सेट है।

### अनुशंसित दृष्टिकोण
- **शुरुआती लोगों के लिए**: सरलता और त्वरित सेटअप के लिए **MicroPython with Thonny** का उपयोग करें।
- **उन्नत उपयोगकर्ताओं के लिए**: प्रदर्शन और निम्न-स्तरीय नियंत्रण के लिए **C/C++ with Pico SDK** का उपयोग करें।
- **Adafruit इकोसिस्टम उपयोगकर्ताओं के लिए**: यदि आप Adafruit लाइब्रेरी या हार्डवेयर का उपयोग करने की योजना बना रहे हैं तो **CircuitPython** का उपयोग करें।

यदि आपके पास कोई विशिष्ट प्रोजेक्ट या प्रोग्रामिंग प्राथमिकता है, तो मुझे बताएं, और मैं निर्देशों को और अधिक अनुकूलित कर सकता हूं!