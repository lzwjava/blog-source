---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: सेलेनियम वेब स्क्रैपिंग कोड व्याख्या
translated: true
type: note
---

### प्रदान किए गए कोड में Selenium API के उपयोग की व्याख्या

यह Python स्क्रिप्ट **Selenium WebDriver** लाइब्रेरी का उपयोग एक वेब ब्राउज़र (विशेष रूप से Chrome) को स्वचालित करने के लिए करती है ताकि एक वेबसाइट (संभवतः `https://xxdata.com/index.aspx` पर एक डेटा/ट्रेड पोर्टल) के साथ इंटरैक्ट किया जा सके। लक्ष्य वेब स्क्रैपिंग प्रतीत होता है: लॉगिन करना, ट्रेड/ऑर्डर डेटा (जैसे '8449' HS कोड का उपयोग करके) खोजना, पेजिनेटेड परिणामों के माध्यम से नेविगेट करना, विवरण पर क्लिक करना, HTML टेबल से संरचित डेटा निकालना और इसे SQLite डेटाबेस (`data.db`) में संग्रहीत करना।

यहाँ Selenium का उपयोग **ब्राउज़र ऑटोमेशन** के लिए किया गया है, जो स्क्रिप्ट को टाइपिंग, क्लिकिंग, स्क्रॉलिंग और पेज लोड होने की प्रतीक्षा जैसे मानवीय इंटरैक्शन की नकल करने की अनुमति देता है—ऐसा कुछ जो साधारण HTTP अनुरोधों (जैसे, JavaScript-हेवी पेज, iframes, या डायनामिक कंटेंट के कारण) के साथ करना कठिन या असंभव है। यह डायनामिक वेब एलिमेंट्स, सत्रों और मल्टी-विंडो/iframe स्विचिंग को हैंडल करता है, जो आधुनिक वेब ऐप्स में आम हैं।

मैं इसे **सेक्शन दर सेक्शन** तोड़कर समझाऊंगा, जिसमें मुख्य Selenium API, उनका उद्देश्य और उनके उपयोग पर प्रकाश डाला जाएगा। ध्यान दें: कोड में कुछ विधियाँ (जैसे, `find_element_by_css_selector`) Selenium के पुराने वर्जन (4.0 से पहले) की हैं और अब डिप्रिकेटेड हैं। आधुनिक Selenium (4+) में, आप `find_element(By.CSS_SELECTOR, ...)` का उपयोग करेंगे, लेकिन फंक्शनैलिटी वही है। स्क्रिप्ट वेट्स, एक्सेप्शन और एलिमेंट हैंडलिंग के लिए आवश्यक मॉड्यूल भी इम्पोर्ट करती है।

#### 1. **इम्पोर्ट्स और सेटअप (Selenium इनिशियलाइज़ेशन)**
   ```python
   from selenium import webdriver
   from selenium.webdriver.chrome.webdriver import WebDriver
   from selenium.webdriver.common.keys import Keys
   from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, StaleElementReferenceException
   from selenium.webdriver.support.ui import WebDriverWait
   from selenium.webdriver.support import expected_conditions as EC
   from selenium.webdriver.common.by import By
   from selenium.webdriver.remote.webelement import WebElement
   ```
   - **उद्देश्य**: ये इम्पोर्ट कोर Selenium कंपोनेंट्स हैं:
     - `webdriver`: ब्राउज़र को कंट्रोल करने के लिए मुख्य मॉड्यूल।
     - `WebDriver`: ब्राउज़र इंस्टेंस के लिए टाइप हिंट (टाइप सेफ्टी सुनिश्चित करता है)।
     - `Keys`: कीबोर्ड इनपुट सिम्युलेट करने के लिए (जैसे, Page Up)।
     - एक्सेप्शन्स: टाइमआउट या स्टेल एलिमेंट्स (पेज रिफ्रेश के बाद बदलने वाले एलिमेंट) जैसी कॉमन एरर को हैंडल करते हैं।
     - `WebDriverWait` और `EC` (Expected Conditions): एक्सप्लिसिट वेट्स के लिए—पोलिंग तब तक करते हैं जब तक कोई एलिमेंट किसी कंडीशन को पूरा नहीं करता (जैसे, पेज पर मौजूद हो)।
     - `By`: एलिमेंट्स ढूंढने के लिए लोकेटर स्ट्रैटेजीज (जैसे, CSS selector, ID, tag name)।
     - `WebElement`: HTML एलिमेंट्स को इंटरैक्शन के लिए रिप्रेजेंट करता है।

   `run()` फंक्शन में:
   ```python
   options = webdriver.ChromeOptions()
   options.add_argument("--start-maximized")  # ब्राउज़र को फुल स्क्रीन में खोलता है।
   options.add_argument('--log-level=3')      # क्लीनर आउटपुट के लिए कंसोल लॉग को सप्रेस करता है।
   browser: WebDriver = webdriver.Chrome(executable_path="./chromedriver", options=options)
   ```
   - **प्रयुक्त Selenium API**: `webdriver.Chrome(options=...)`
     - एक लोकल `chromedriver` एक्जीक्यूटेबल का उपयोग करके Chrome ब्राउज़र इंस्टेंस को इनिशियलाइज़ करता है (यह स्क्रिप्ट के डायरेक्टरी में होना चाहिए)।
     - `ChromeOptions`: ब्राउज़र सत्र को कस्टमाइज़ करता है (जैसे, बैकग्राउंड रनिंग के लिए `options.add_argument("--headless")` जोड़कर हेडलेस मोड एक्टिवेट किया जा सकता है)।
     - यह एक लाइव, कंट्रोलेबल ब्राउज़र विंडो बनाता है। Selenium, Python और ब्राउज़र के DevTools प्रोटोकॉल के बीच एक ब्रिज के रूप में कार्य करता है।

   ```python
   browser.get('https://xxdata.com/index.aspx')
   ```
   - **प्रयुक्त Selenium API**: `WebDriver.get(url)`
     - स्टार्टिंग URL पर नेविगेट करता है, पेज को उसी तरह लोड करता है जैसे कोई उपयोगकर्ता इसे एड्रेस बार में टाइप करता है।

#### 2. **लॉगिन प्रक्रिया**
   ```python
   input_username = browser.find_element_by_css_selector('input[name=username]')
   input_username.send_keys('name')
   input_password = browser.find_element_by_css_selector('input[name=password]')
   input_password.send_keys('password')
   btn_login = browser.find_element_by_css_selector('div.login-check')
   btn_login.click()
   ```
   - **प्रयुक्त Selenium API**:
     - `WebDriver.find_element_by_css_selector(css)` (डिप्रिकेटेड; आधुनिक: `find_element(By.CSS_SELECTOR, css)`): CSS selector का उपयोग करके एक HTML एलिमेंट को लोकेट करता है (जैसे, `name="username"` एट्रिब्यूट द्वारा)। एक `WebElement` रिटर्न करता है।
     - `WebElement.send_keys(text)`: इनपुट फील्ड में टाइपिंग सिम्युलेट करता है (जैसे, यूजरनेम/पासवर्ड)।
     - `WebElement.click()`: बटन या लिंक पर माउस क्लिक सिम्युलेट करता है।
   - **Selenium का उपयोग कैसे किया गया है**: फॉर्म सबमिशन को ऑटोमेट करता है। Selenium के बिना, आपको POST रिक्वेस्ट्स को रिवर्स-इंजीनियर करने की आवश्यकता होगी, लेकिन यह JavaScript वैलिडेशन या डायनामिक फॉर्म्स को सीमलेसली हैंडल करता है। क्रेडेंशियल्स हार्डकोडेड हैं (प्रोडक्शन में असुरक्षित—env vars का उपयोग करें)।

   लॉगिन के बाद:
   ```python
   wait_element(browser, 'div.dsh_01')
   ```
   - डैशबोर्ड लोड होने तक रुकने के लिए एक कस्टम `wait_element` फंक्शन को कॉल करता है (नीचे समझाया गया है)।

#### 3. **नेविगेशन और खोज**
   ```python
   trade_div = browser.find_element_by_css_selector('div.dsh_01')
   trade_div.click()
   wait_element(browser, 'a.teq_icon')
   teq = browser.find_element_by_css_selector('a.teq_icon')
   teq.click()
   wait_element(browser, 'div.panel-body')
   iframe = browser.find_element_by_css_selector('div.panel-body > iframe')
   iframe_id = iframe.get_attribute('id')
   browser.switch_to.frame(iframe_id)
   ```
   - **प्रयुक्त Selenium API**:
     - `find_element_by_css_selector`: नेविगेशन एलिमेंट्स को लोकेट करता है (जैसे, डैशबोर्ड div, आइकन लिंक)।
     - `WebElement.click()`: नेविगेट करने के लिए क्लिक करता है (जैसे, "trade" सेक्शन पर)।
     - `WebElement.get_attribute('id')`: एक HTML एट्रिब्यूट रिट्रीव करता है (यहाँ, iframe का ID)।
     - `WebDriver.switch_to.frame(frame_id)`: ड्राइवर कॉन्टेक्स्ट को एक `<iframe>` पर स्विच करता है (कंटेंट एम्बेड करने के लिए ऐप्स में आम)। इसके बिना, iframe के अंदर के एलिमेंट्स अनुपलब्ध होते हैं।
   - **Selenium का उपयोग कैसे किया गया है**: मल्टी-स्टेप नेविगेशन और एम्बेडेड कंटेंट को हैंडल करता है। Iframe DOMs को आइसोलेट करते हैं, इसलिए इनर पेज स्क्रैप करने के लिए स्विच करना आवश्यक है।

   खोज प्रक्रिया:
   ```python
   input_search = browser.find_element_by_id('_easyui_textbox_input7')  # ID लोकेटर का उपयोग करता है।
   input_search.send_keys('8449')
   time.sleep(10)
   enter = browser.find_element_by_css_selector('a#btnOk > div.enter-bt')
   enter.click()
   ```
   - **प्रयुक्त Selenium API**:
     - `find_element_by_id(id)` (डिप्रिकेटेड; आधुनिक: `find_element(By.ID, id)`): HTML `id` एट्रिब्यूट द्वारा लोकेट करता है।
     - `send_keys`: सर्च क्वेरी टाइप करता है (उत्पादों के लिए HS कोड)।
     - `time.sleep(10)`: इम्प्लिसिट वेट (अपरिष्कृत; एक्सप्लिसिट वेट का उपयोग करना बेहतर है)।
     - `click()`: सर्च सबमिट करता है।
   - **Selenium का उपयोग कैसे किया गया है**: उपयोगकर्ता खोज को सिम्युलेट करता है। `time.sleep` AJAX/JavaScript के परिणाम लोड करने के लिए रुकता है।

#### 4. **पेजिनेशन और परिणाम प्रसंस्करण**
   ```python
   result_count_span = browser.find_element_by_css_selector('span#ResultCount')
   page = math.ceil(int(result_count_span.text) / 20)  # कुल पेज की गणना करता है (20 परिणाम/पेज)।
   skip = 0
   page = page - skip

   for p in range(page):
       input_page = browser.find_element_by_css_selector('input.laypage_skip')
       input_page.send_keys(str(p + skip + 1))
       btn_confirm = browser.find_element_by_css_selector('button.laypage_btn')
       btn_confirm.click()
       time.sleep(2)

       locates = browser.find_elements_by_css_selector('div.rownumber-bt')  # एकाधिक एलिमेंट्स।
       print('page ' + str(p) + ' size: ' + str(len(locates)))
       for locate in locates:
           browser.execute_script("arguments[0].scrollIntoView();", locate)  # JavaScript स्क्रॉल।
           time.sleep(1)
           browser.find_element_by_tag_name('html').send_keys(Keys.PAGE_UP)  # कीबोर्ड स्क्रॉल।
           time.sleep(1)
           try:
               locate.click()
           except ElementClickInterceptedException:
               print('ElementClickInterceptedException')
               continue
           except StaleElementReferenceException:
               print('StaleElementReferenceException')
               continue
           # ... (नीचे और अधिक)
   ```
   - **प्रयुक्त Selenium API**:
     - `find_element_by_css_selector`: एक span से परिणाम संख्या प्राप्त करता है।
     - `WebElement.text`: किसी एलिमेंट से विजिबल टेक्स्ट निकालता है (जैसे, "100" जैसी संख्या)।
     - `find_elements_by_css_selector` (बहुवचन; डिप्रिकेटेड: `find_elements(By.CSS_SELECTOR, ...)`): एकाधिक एलिमेंट्स ढूंढता है (जैसे, एक पेज पर रो लिंक)। `WebElement` की एक सूची रिटर्न करता है।
     - `WebDriver.execute_script(js_code, *args)`: ब्राउज़र में कस्टम JavaScript चलाता है (यहाँ, क्लिक इश्यू से बचने के लिए किसी एलिमेंट को व्यू में स्क्रॉल करता है)।
     - `WebDriver.find_element_by_tag_name('html').send_keys(Keys.PAGE_UP)`: कीबोर्ड स्क्रॉलिंग सिम्युलेट करता है (`Keys` enum का उपयोग करके)।
     - एक्सेप्शन्स: क्लिक फेलियर (जैसे, ओवरले क्लिक को ब्लॉक करता है) या स्टेल एलिमेंट्स (DOM रिफ्रेश हो गया, रेफरेंस अमान्य हो गए—डायनामिक UI में आम) को कैच करता है।
   - **Selenium का उपयोग कैसे किया गया है**: पेज नंबर टाइप करके और "go" पर क्लिक करके पेजिनेशन को ऑटोमेट करता है। प्रत्येक रिजल्ट रो (`div.rownumber-bt`) के लिए, यह विजिबिलिटी सुनिश्चित करने के लिए स्क्रॉल करता है, फिर विवरण को नई विंडो में खोलने के लिए क्लिक करता है। यह लेज़ी-लोडेड या इनफिनिट-स्क्रॉल जैसे व्यवहार को हैंडल करता है।

#### 5. **विंडो/Iframe स्विचिंग और डेटा निष्कर्षण**
   लूप से जारी:
   ```python
   time.sleep(1)
   browser.switch_to.window(browser.window_handles[1])  # नए टैब/विंडो पर स्विच करें।
   wait_element(browser, 'div#content')
   try:
       save_page(browser)
   except IndexError:
       print('IndexError')
       continue
   browser.close()  # विवरण विंडो बंद करता है।
   browser.switch_to.window(browser.window_handles[0])  # मुख्य विंडो पर वापस।
   browser.switch_to.frame(iframe_id)  # iframe कॉन्टेक्स्ट पर वापस।
   ```
   - **प्रयुक्त Selenium API**:
     - `WebDriver.window_handles`: खुली विंडो/टैब ID की सूची।
     - `WebDriver.switch_to.window(handle)`: फोकस को एक विशिष्ट विंडो पर स्विच करता है (इंडेक्स 0 = मुख्य, 1 = क्लिक द्वारा खोला गया नया टैब)।
     - `WebDriver.close()`: वर्तमान विंडो बंद करता है।
   - **Selenium का उपयोग कैसे किया गया है**: क्लिक विवरण को नए टैब में खोलते हैं, इसलिए यह उन्हें स्क्रैप करने के लिए कॉन्टेक्स्ट स्विच करता है, फिर वापस लौटता है। यह मल्टी-टैब ऐप्स के लिए महत्वपूर्ण है।

#### 6. **`save_page(browser: WebDriver)` फंक्शन में डेटा निष्कर्षण**
   यह कोर स्क्रैपिंग लॉजिक है:
   ```python
   ts = browser.find_elements_by_css_selector('table')  # पेज पर सभी टेबल।
   t0 = ts[0]
   tds0 = t0.find_elements_by_tag_name('td')  # पहले टेबल में TD सेल।
   order_number = tds0[2].text  # विशिष्ट सेल से टेक्स्ट निकालता है।
   # ... (अन्य टेबल के लिए समान: t1, t2, आदि)
   ```
   - **प्रयुक्त Selenium API**:
     - `find_elements_by_css_selector('table')` / `find_elements_by_tag_name('td')` (डिप्रिकेटेड: `By.TAG_NAME` का उपयोग करें): सभी `<table>` और उनके `<td>` सेल ढूंढता है।
     - `WebElement.text`: सेल से टेक्स्ट कंटेंट निकालता है (जैसे, ऑर्डर नंबर, इम्पोर्टर नाम)।
     - कस्टम `tds_to_text(tds: list[WebElement])`: जोड़े गए `<td>` से टेक्स्ट को जोड़ता है (जैसे, लेबल + वैल्यू)।
   - **Selenium का उपयोग कैसे किया गया है**: पेज की DOM संरचना को पार्स करता है (ऑर्डर/इम्पोर्टर/एक्सपोर्टर विवरण वाली टेबल)। यह वेरिएबल टेबल काउंट को हैंडल करता है (जैसे, यदि `len(ts) == 8`, तो अतिरिक्त टेबल मौजूद हैं)। डेटा फिर SQLite में इन्सर्ट किया जाता है (गैर-Selenium भाग)।

   कंडीशनल लॉजिक `order_number`, `importer`, `exporter`, आदि जैसे फील्ड्स को टेबल इंडिसेस के आधार पर निकालती है—एक फिक्स्ड लेआउट मानते हुए।

#### 7. **वेट्स और एरर हैंडलिंग (`wait_element` फंक्शन)**
   ```python
   def wait_element(browser, css):
       timeout = 30
       try:
           element_present = EC.presence_of_element_located((By.CSS_SELECTOR, css))
           WebDriverWait(browser, timeout).until(element_present)
       except TimeoutException:
           print('Timed out waiting for page to load')
   ```
   - **प्रयुक्त Selenium API**:
     - `expected_conditions.presence_of_element_located(locator)`: DOM में किसी एलिमेंट के मौजूद होने की प्रतीक्षा करता है (जरूरी नहीं कि विजिबल हो)।
     - `WebDriverWait(driver, timeout).until(condition)`: कंडीशन के लिए 30s तक हर 0.5s में पोलिंग करता है।
     - `TimeoutException`: यदि वेट फेल हो जाता है तो उठाया जाता है।
   - **Selenium का उपयोग कैसे किया गया है**: रेस कंडीशन को रोकता है (जैसे, पेज लोड होने से पहले क्लिक करना)। `time.sleep` से बेहतर है क्योंकि यह एलिमेंट-स्पेसिफिक और एफिशिएंट है।

#### 8. **क्लीनअप**
   ```python
   time.sleep(1000)  # लंबा विराम (डीबगिंग?)।
   browser.quit()    # ब्राउज़र बंद करता है और सत्र समाप्त करता है।
   ```
   - **प्रयुक्त Selenium API**: `WebDriver.quit()`: ड्राइवर को टर्मिनेट करता है, सभी विंडो बंद करता है और रिसोर्सेज रिलीज करता है।

#### समग्र रूप से Selenium कैसे फिट बैठता है
- **ऑटोमेशन फ्लो**: Selenium एक रियल ब्राउज़र लॉन्च करता है, पेज लोड करता है, DOM क्वेरी (CSS/ID जैसे लोकेटर) के माध्यम से इंटरैक्ट करता है, और डायनामिक व्यवहार (JS एक्सेक्यूशन, वेट्स, स्विच) को हैंडल करता है। यह SPAs या सत्र/कुकीज़ वाली सुरक्षित साइटों के लिए आदर्श है।
- **यहाँ मजबूत पक्ष**: लॉगिन स्टेट, iframes, नए टैब और स्क्रॉलिंग को हैंडल करता है—BeautifulSoup/Requests जैसे स्क्रैपिंग टूल अकेले ऐसा नहीं कर सकते।
- **कोड में सीमाएँ/मुद्दे**:
  - डिप्रिकेटेड लोकेटर: भविष्य के लिए `By` में अपडेट करें।
  - हार्डकोडेड स्लीप: स्पीड बढ़ाने/फ्लैकीनेस कम करने के लिए और वेट्स से बदलें।
  - एक्सेप्शन: अच्छा हैंडलिंग, लेकिन StaleElement पर रिट्राई कर सकता है।
  - नैतिकता/वैधता: स्क्रैपिंग नियमों का उल्लंघन कर सकता है; मानव की नकल करने के लिए user-agent हेडर या प्रॉक्सी जोड़ें।
  - प्रदर्शन: हेडफुल चलता है (दृश्यमान ब्राउज़र); प्रोडक्शन के लिए हेडलेस बनाएं।
- **इसे चलाना**: ChromeDriver की आवश्यकता होती है (Selenium साइट से डाउनलोड करें, Chrome वर्जन से मिलान करें)। `pip install selenium` के माध्यम से Selenium इंस्टॉल करें।

यदि आपके पास विशिष्ट भागों, कोड को आधुनिक बनाने, या डीबगिंग के बारे में प्रश्न हैं, तो मुझे बताएं!