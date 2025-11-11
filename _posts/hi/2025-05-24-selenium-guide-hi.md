---
audio: false
generated: true
lang: hi
layout: post
title: सेलेनियम गाइड
translated: true
type: note
---

मैं सेलेनियम के बारे में एक व्यापक गाइड प्रदान करूंगा, जो वेब ब्राउज़रों को ऑटोमेट करने के लिए एक लोकप्रिय टूल है। यह गाइड सेलेनियम के कॉम्पोनेंट्स, सेटअप, बेसिक यूज़ेज, एडवांस्ड फीचर्स और बेस्ट प्रैक्टिसेज़ को कवर करेगी, जिसमें पायथन में कोड उदाहरण भी शामिल होंगे। मैं कोड और महत्वपूर्ण सेक्शन्स को आवश्यक आर्टिफैक्ट टैग्स में रैप कर दूंगा।

सेलेनियम वेब ब्राउज़रों को ऑटोमेट करने के लिए एक ओपन-सोर्स फ्रेमवर्क है, जिसका उपयोग मुख्य रूप से वेब एप्लिकेशन्स को टेस्ट करने के लिए किया जाता है, लेकिन यह वेब स्क्रैपिंग और ऑटोमेशन टास्क्स के लिए भी उपयोगी है। यह कई ब्राउज़रों (Chrome, Firefox, Safari, Edge, आदि) और प्रोग्रामिंग लैंग्वेजेज (Python, Java, C#, Ruby, JavaScript, आदि) को सपोर्ट करता है।

---

### सेलेनियम की व्यापक गाइड

#### 1. **सेलेनियम क्या है?**
सेलेनियम टूल्स का एक सूट है जो वेब ब्राउज़रों को ऑटोमेट करने के लिए डिज़ाइन किया गया है। यह आपको वेब एलिमेंट्स के साथ इंटरैक्ट करने, यूज़र एक्शन्स (क्लिक, टाइपिंग, नेविगेशन) को सिम्युलेट करने और वेब एप्लिकेशन बिहेवियर को वैलिडेट करने की अनुमति देता है। सेलेनियम के मुख्य कॉम्पोनेंट्स हैं:
- **Selenium WebDriver**: ब्राउज़र ऑटोमेशन के लिए कोर कॉम्पोनेंट, जो ब्राउज़रों को प्रोग्रामेटिक रूप से कंट्रोल करने के लिए एक API प्रदान करता है।
- **Selenium IDE**: ब्राउज़र इंटरैक्शन्स को रिकॉर्ड करने और प्ले बैक करने के लिए एक ब्राउज़र एक्सटेंशन (मुख्य रूप से शुरुआती लोगों के लिए)।
- **Selenium Grid**: एक से अधिक मशीनों या ब्राउज़रों पर टेस्ट्स को समानांतर में चलाने के लिए एक टूल।

यह गाइड **Selenium WebDriver** पर पायथन के साथ केंद्रित है, क्योंकि यह सबसे व्यापक रूप से उपयोग किया जाने वाला कॉम्पोनेंट है।

---

#### 2. **सेलेनियम सेटअप करना**
सेलेनियम को पायथन के साथ उपयोग करने के लिए, आपको आवश्यक डिपेंडेंसीज़ इंस्टॉल करनी होंगी और ब्राउज़र ड्राइवर्स सेटअप करने होंगे।

##### आवश्यक शर्तें
- Python (3.6 या बाद वाला वर्जन रिकमेंडेड)
- एक वेब ब्राउज़र (जैसे, Chrome, Firefox)
- संबंधित ब्राउज़र ड्राइवर (जैसे, Chrome के लिए ChromeDriver, Firefox के लिए GeckoDriver)
- Selenium Python पैकेज

##### इंस्टॉलेशन स्टेप्स
1. **Python इंस्टॉल करें**: सुनिश्चित करें कि Python इंस्टॉल है और आपके सिस्टम के PATH में एडेड है।
2. **Selenium इंस्टॉल करें**:
   अपने टर्मिनल में निम्न कमांड रन करें:
   ```bash
   pip install selenium
   ```
3. **ब्राउज़र ड्राइवर डाउनलोड करें**:
   - Chrome के लिए: [chromedriver.chromium.org](https://chromedriver.chromium.org/downloads) से ChromeDriver डाउनलोड करें। सुनिश्चित करें कि वर्जन आपके इंस्टॉल किए गए Chrome ब्राउज़र से मेल खाता हो।
   - Firefox के लिए: [github.com/mozilla/geckodriver](https://github.com/mozilla/geckodriver/releases) से GeckoDriver डाउनलोड करें।
   - ड्राइवर एक्जीक्यूटेबल को एक डायरेक्टरी में रखें जो आपके सिस्टम के PATH में शामिल हो या अपने कोड में इसके पाथ को स्पेसिफाई करें।
4. **इंस्टॉलेशन वेरिफाई करें**:
   सेलेनियम सेटअप को टेस्ट करने के लिए एक साधारण स्क्रिप्ट बनाएं।

```python
from selenium import webdriver

# Chrome WebDriver इनिशियलाइज़ करें
driver = webdriver.Chrome()
# एक वेबसाइट ओपन करें
driver.get("https://www.example.com")
# पेज टाइटल प्रिंट करें
print(driver.title)
# ब्राउज़र बंद करें
driver.quit()
```

स्क्रिप्ट रन करें। यदि ब्राउज़र ओपन होता है, `example.com` पर नेविगेट करता है और पेज टाइटल प्रिंट करता है, तो आपका सेटअप सफल है।

---

#### 3. **Selenium WebDriver के कोर कॉन्सेप्ट्स**
Selenium WebDriver वेब एलिमेंट्स के साथ इंटरैक्ट करने के लिए एक API प्रदान करता है। प्रमुख अवधारणाओं में शामिल हैं:

- **WebDriver**: एक ब्राउज़र इंस्टेंस को कंट्रोल करने के लिए इंटरफेस (जैसे, Chrome के लिए `webdriver.Chrome()`)।
- **WebElement**: एक वेबपेज पर HTML एलिमेंट (जैसे, बटन, इनपुट फील्ड) को रिप्रेजेंट करता है।
- **Locators**: एलिमेंट्स को ढूंढने के तरीके (जैसे, ID, name, class, XPath, CSS selector द्वारा)।
- **Actions**: एलिमेंट्स के साथ इंटरैक्ट करने के तरीके (जैसे, क्लिक, कीज़ भेजना, टेक्स्ट प्राप्त करना)।

##### सामान्य Locators
सेलेनियम वेबपेज पर एलिमेंट्स को पहचानने के लिए लोकेटर्स का उपयोग करता है:
- `find_element_by_id("id")`: किसी एलिमेंट को उसके ID द्वारा ढूंढता है।
- `find_element_by_name("name")`: किसी एलिमेंट को उसके name एट्रिब्यूट द्वारा ढूंढता है।
- `find_element_by_class_name("class")`: किसी एलिमेंट को उसके class name द्वारा ढूंढता है।
- `find_element_by_tag_name("tag")`: किसी एलिमेंट को उसके HTML टैग द्वारा ढूंढता है।
- `find_element_by_css_selector("selector")`: CSS selector का उपयोग करके किसी एलिमेंट को ढूंढता है।
- `find_element_by_xpath("xpath")`: XPath एक्सप्रेशन का उपयोग करके किसी एलिमेंट को ढूंढता है।
- `find_elements_*`: मिलान करने वाले सभी एलिमेंट्स की एक सूची लौटाता है (जैसे, `find_elements_by_tag_name`)।

##### बेसिक इंटरैक्शन्स
- `click()`: किसी एलिमेंट पर क्लिक करता है।
- `send_keys("text")`: इनपुट फील्ड में टेक्स्ट टाइप करता है।
- `text`: किसी एलिमेंट की टेक्स्ट सामग्री प्राप्त करता है।
- `get_attribute("attribute")`: किसी एलिमेंट के एट्रिब्यूट का मान प्राप्त करता है (जैसे, `value`, `href`)।
- `is_displayed()`, `is_enabled()`, `is_selected()`: एलिमेंट स्टेट चेक करता है।

---

#### 4. **एक बेसिक सेलेनियम स्क्रिप्ट लिखना**
यहां एक उदाहरण स्क्रिप्ट है जो किसी वेबसाइट पर लॉग इन करने को ऑटोमेट करती है (डेमोन्स्ट्रेशन के लिए एक काल्पनिक लॉगिन पेज का उपयोग करते हुए)।

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Chrome WebDriver इनिशियलाइज़ करें
driver = webdriver.Chrome()

try:
    # लॉगिन पेज पर नेविगेट करें
    driver.get("https://example.com/login")
    
    # यूज़रनेम और पासवर्ड फील्ड ढूंढें
    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")
    
    # क्रेडेंशियल्स एंटर करें
    username.send_keys("testuser")
    password.send_keys("testpassword")
    
    # फॉर्म सबमिट करें
    password.send_keys(Keys.RETURN)
    
    # पेज लोड होने का इंतज़ार करें
    time.sleep(2)
    
    # लॉगिन सफलता वेरिफाई करें (वेलकम मैसेज के लिए चेक करें)
    welcome_message = driver.find_element(By.CLASS_NAME, "welcome").text
    print(f"लॉगिन सफल! वेलकम मैसेज: {welcome_message}")
    
except Exception as e:
    print(f"एक एरर आई: {e}")
    
finally:
    # ब्राउज़र बंद करें
    driver.quit()
```

**नोट्स**:
- `"https://example.com/login"` को टारगेट वेबसाइट के एक्चुअल URL से बदलें।
- वेबसाइट की HTML स्ट्रक्चर के आधार पर एलिमेंट लोकेटर्स (`By.ID`, `By.CLASS_NAME`) को एडजस्ट करें।
- `time.sleep(2)` एक साधारण वेट है; प्रोडक्शन के लिए, एक्सप्लिसिट वेट्स का उपयोग करें (जिसे बाद में कवर किया गया है)।

---

#### 5. **एडवांस्ड फीचर्स**
सेलेनियम रोबस्ट ऑटोमेशन के लिए एडवांस्ड फीचर्स प्रदान करता है।

##### a. **वेटिंग मैकेनिज्म्स**
सेलेनियम डायनामिक वेब पेजेज़ को हैंडल करने के लिए दो प्रकार के वेट्स प्रदान करता है:
- **Implicit Wait**: सभी एलिमेंट सर्च के लिए एक डिफॉल्ट वेट टाइम सेट करता है।
  ```python
  driver.implicitly_wait(10)  # एलिमेंट्स के दिखने तक 10 सेकंड तक इंतज़ार करें
  ```
- **Explicit Wait**: एक स्पेसिफिक कंडीशन के लिए इंतज़ार करता है (जैसे, एलिमेंट क्लिक करने योग्य है)।

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Chrome WebDriver इनिशियलाइज़ करें
driver = webdriver.Chrome()

try:
    driver.get("https://example.com")
    
    # किसी एलिमेंट के क्लिक करने योग्य होने तक इंतज़ार करें (10 सेकंड तक)
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "submit-button"))
    )
    button.click()
    
    print("बटन सफलतापूर्वक क्लिक किया गया!")
    
except Exception as e:
    print(f"एक एरर आई: {e}")
    
finally:
    driver.quit()
```

##### b. **अलर्ट्स को हैंडल करना**
सेलेनियम JavaScript अलर्ट्स, कन्फर्म्स और प्रॉम्प्ट्स के साथ इंटरैक्ट कर सकता है:
```python
alert = driver.switch_to.alert
alert.accept()  # OK क्लिक करें
alert.dismiss()  # Cancel क्लिक करें
alert.send_keys("text")  # प्रॉम्प्ट में टाइप करें
```

##### c. **फ्रेम्स और विंडोज़ को नेविगेट करना**
- **फ्रेम्स/आईफ्रेम्स**: किसी फ्रेम के एलिमेंट्स के साथ इंटरैक्ट करने के लिए उस फ्रेम पर स्विच करें।
  ```python
  driver.switch_to.frame("frame-id")
  driver.switch_to.default_content()  # मुख्य कंटेंट पर वापस आएं
  ```
- **विंडोज़/टैब्स**: एक से अधिक ब्राउज़र विंडोज़ को हैंडल करें।
  ```python
  original_window = driver.current_window_handle
  for window_handle in driver.window_handles:
      driver.switch_to.window(window_handle)
  ```

##### d. **JavaScript एक्जीक्यूट करना**
ब्राउज़र में सीधे JavaScript कोड रन करें:
```python
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # नीचे तक स्क्रॉल करें
```

##### e. **स्क्रीनशॉट्स**
डीबगिंग या डॉक्यूमेंटेशन के लिए स्क्रीनशॉट कैप्चर करें:
```python
driver.save_screenshot("screenshot.png")
```

---

#### 6. **हेडलेस ब्राउज़रों के साथ सेलेनियम**
हेडलेस ब्राउज़र बिना GUI के चलते हैं, जो CI/CD पाइपलाइन्स या सर्वर के लिए आदर्श हैं।
हेडलेस मोड में Chrome के साथ उदाहरण:

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# हेडलेस मोड के लिए Chrome ऑप्शन्स सेटअप करें
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

# हेडलेस मोड में Chrome WebDriver इनिशियलाइज़ करें
driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get("https://www.example.com")
    print(f"पेज टाइटल: {driver.title}")
    
except Exception as e:
    print(f"एक एरर आई: {e}")
    
finally:
    driver.quit()
```

---

#### 7. **बेस्ट प्रैक्टिसेज़**
- **एक्सप्लिसिट वेट्स का उपयोग करें**: डायनामिक पेजेज़ के लिए `time.sleep()` से बचें; `WebDriverWait` के साथ `expected_conditions` का उपयोग करें।
- **एक्सेप्शन्स को हैंडल करें**: एरर्स को सहजता से हैंडल करने के लिए कोड को `try-except` ब्लॉक्स में रैप करें।
- **WebDriver बंद करें**: ब्राउज़र को बंद करने और रिसोर्सेज़ को रिलीज़ करने के लिए हमेशा `driver.quit()` को कॉल करें।
- **लोकेटर्स को ऑर्गनाइज़ करें**: मेंटेनबिलिटी के लिए लोकेटर्स को एक अलग फाइल या क्लास में स्टोर करें।
- **पेज ऑब्जेक्ट मॉडल (POM) का उपयोग करें**: कोड रियूज़ेबिलिटी को बेहतर बनाने के लिए पेज इंटरैक्शन्स को क्लासेज़ में एनकैप्सुलेट करें।

पेज ऑब्जेक्ट मॉडल का उदाहरण:

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, "username")
        self.password_field = (By.ID, "password")
        self.submit_button = (By.ID, "submit-button")
    
    def login(self, username, password):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.username_field)
        ).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.submit_button).click()

# यूज़ेज
from selenium import webdriver

driver = webdriver.Chrome()
login_page = LoginPage(driver)
try:
    driver.get("https://example.com/login")
    login_page.login("testuser", "testpassword")
except Exception as e:
    print(f"एक एरर आई: {e}")
finally:
    driver.quit()
```

---

#### 8. **सेलेनियम ग्रिड**
सेलेनियम ग्रिड समानांतर में एक से अधिक ब्राउज़रों, ऑपरेटिंग सिस्टम्स, या मशीनों पर टेस्ट्स चलाने की अनुमति देता है। इसमें एक **हब** (सेंट्रल सर्वर) और **नोड्स** (ब्राउज़र चलाने वाली मशीनें) शामिल होते हैं।
- **सेटअप**: Selenium Grid की JAR फाइल या Docker का उपयोग करके एक हब और नोड्स कॉन्फ़िगर करें।
- **यूज़ केस**: क्रॉस-ब्राउज़र कम्पैटिबिलिटी टेस्ट करें (जैसे, Windows पर Chrome, Linux पर Firefox)।
- **उदाहरण**: एक रिमोट WebDriver से कनेक्ट करें:
  ```python
  from selenium.webdriver.remote.webdriver import WebDriver
  driver = WebDriver(command_executor="http://hub-ip:4444/wd/hub", desired_capabilities={"browserName": "chrome"})
  ```

---

#### 9. **सामान्य चुनौतियाँ और समाधान**
- **एलिमेंट नहीं मिल रहा**: एक्सप्लिसिट वेट्स का उपयोग करें या ब्राउज़र डेवलपर टूल्स के साथ लोकेटर्स को वेरिफाई करें।
- **स्टेल एलिमेंट रेफरेंस**: पेज रिफ्रेश या DOM बदलाव के बाद एलिमेंट्स को फिर से लोकेट करें।
- **स्लो परफॉर्मेंस**: लोकेटर्स को ऑप्टिमाइज़ करें (XPath पर ID/CSS को प्राथमिकता दें) और हेडलेस मोड का उपयोग करें।
- **डायनामिक कंटेंट**: AJAX-लोडेड कंटेंट को हैंडल करने के लिए JavaScript एक्जीक्यूशन या वेट्स का उपयोग करें।

---

#### 10. **रिसोर्सेज़**
- ऑफिशियल डॉक्यूमेंटेशन: [selenium.dev](https://www.selenium.dev/documentation/)
- Python सेलेनियम बाइंडिंग्स: [selenium-python.readthedocs.io](https://selenium-python.readthedocs.io/)
- ब्राउज़र ड्राइवर्स: ChromeDriver, GeckoDriver
- कम्युनिटी: Stack Overflow, X पोस्ट्स (#Selenium या #WebDriver के लिए सर्च करें)

---

यह गाइड सेलेनियम WebDriver के आवश्यक तत्वों को सेटअप से लेकर एडवांस्ड यूज़ेज तक कवर करती है। यदि आपको किसी स्पेसिफिक सेलेनियम टास्क या अधिक एडवांस्ड उदाहरणों के साथ मदद की आवश्यकता है, तो मुझे बताएं!