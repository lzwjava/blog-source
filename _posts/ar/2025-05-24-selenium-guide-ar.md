---
audio: false
generated: true
lang: ar
layout: post
title: دليل السيلينيوم
translated: true
type: note
---

سأقدم دليلاً شاملاً لـ Selenium، وهو أداة شائعة لأتمتة متصفحات الويب. سيغطي هذا الدليل مكونات Selenium، والإعداد، والاستخدام الأساسي، والميزات المتقدمة، وأفضل الممارسات، بما في ذلك أمثلة التعليمات البرمجية بلغة Python. سأقوم بتغليف الأقسام الرئيسية ورمز المثال بعلامات القطع الأثرية المطلوبة.

Selenium هو إطار عمل مفتوح المصدر لأتمتة متصفحات الويب، يُستخدم أساسًا لاختبار تطبيقات الويب ولكن أيضًا لمهام scraping الويب والأتمتة. وهو يدعم متصفحات متعددة (Chrome، Firefox، Safari، Edge، إلخ) ولغات البرمجة (Python، Java، C#، Ruby، JavaScript، إلخ).

---

### دليل شامل لـ Selenium

#### 1. **ما هو Selenium؟**
Selenium عبارة عن مجموعة أدوات مصممة لأتمتة متصفحات الويب. يسمح لك بالتفاعل مع عناصر الويب، ومحاكاة إجراءات المستخدم (النقر، والكتابة، والتنقل)، والتحقق من سلوك تطبيق الويب. المكونات الرئيسية لـ Selenium هي:
- **Selenium WebDriver**: المكون الأساسي لأتمتة المتصفح، ويوفر واجهة برمجة تطبيقات (API) للتحكم في المتصفحات برمجيًا.
- **Selenium IDE**: امتداد للمتصفح لتسجيل وتشغيل تفاعلات المتصفح (موجه للمبتدئين بشكل أساسي).
- **Selenium Grid**: أداة لتشغيل الاختبارات بالتوازي عبر أجهزة أو متصفحات متعددة.

يركز هذا الدليل على **Selenium WebDriver** مع Python، لأنه المكون الأكثر استخدامًا على نطاق واسع.

---

#### 2. **إعداد Selenium**
لاستخدام Selenium مع Python، تحتاج إلى تثبيت التبعيات المطلوبة وإعداد برامج تشغيل المتصفح.

##### المتطلبات الأساسية
- Python (يُوصى بـ 3.6 أو إصدار أحدث)
- متصفح ويب (مثل Chrome، Firefox)
- برنامج تشغيل المتصفح المقابل (مثل ChromeDriver لـ Chrome، وGeckoDriver لـ Firefox)
- حزمة Selenium لـ Python

##### خطوات التثبيت
1. **تثبيت Python**: تأكد من تثبيت Python وإضافته إلى مسار النظام (PATH).
2. **تثبيت Selenium**:
   قم بتشغيل الأمر التالي في الطرفية:
   ```bash
   pip install selenium
   ```
3. **تنزيل برنامج تشغيل المتصفح**:
   - لـ Chrome: قم بتنزيل ChromeDriver من [chromedriver.chromium.org](https://chromedriver.chromium.org/downloads). تأكد من أن الإصدار يتطابق مع متصفح Chrome المثبت لديك.
   - لـ Firefox: قم بتنزيل GeckoDriver من [github.com/mozilla/geckodriver](https://github.com/mozilla/geckodriver/releases).
   - ضع الملف القابل للتنفيذ لبرنامج التشغيل في دليل مدرج في مسار النظام (PATH) أو حدد مساره في الكود الخاص بك.
4. **التحقق من التثبيت**:
   أنشئ نصًا برمجيًا بسيطًا لاختبار إعداد Selenium.

```python
from selenium import webdriver

# تهيئة Chrome WebDriver
driver = webdriver.Chrome()
# افتح موقع ويب
driver.get("https://www.example.com")
# اطبع عنوان الصفحة
print(driver.title)
# أغلق المتصفح
driver.quit()
```

شغّل النص البرمجي. إذا فتح المتصفح، وانتقل إلى `example.com`، وطبع عنوان الصفحة، فإن إعدادك ناجح.

---

#### 3. **المفاهيم الأساسية لـ Selenium WebDriver**
يوفر Selenium WebDriver واجهة برمجة تطبيقات (API) للتفاعل مع عناصر الويب. تشمل المفاهيم الرئيسية:

- **WebDriver**: الواجهة للتحكم في نسخة المتصفح (مثل `webdriver.Chrome()` لـ Chrome).
- **WebElement**: يمثل عنصر HTML (مثل زر، حقل إدخال) على صفحة ويب.
- **أدوات تحديد المواقع (Locators)**: طرق للعثور على العناصر (مثل بواسطة المعرف (ID)، الاسم، الفئة، XPath، محدد CSS).
- **الإجراءات**: طرق للتفاعل مع العناصر (مثل النقر، إرسال المفاتيح، الحصول على النص).

##### أدوات تحديد المواقع الشائعة
يستخدم Selenium أدوات تحديد المواقع لتحديد العناصر على صفحة ويب:
- `find_element_by_id("id")`: يجد عنصرًا بواسطة معرفه.
- `find_element_by_name("name")`: يجد عنصرًا بواسطة سمة الاسم.
- `find_element_by_class_name("class")`: يجد عنصرًا بواسطة اسم فئته.
- `find_element_by_tag_name("tag")`: يجد عنصرًا بواسطة علامة HTML الخاصة به.
- `find_element_by_css_selector("selector")`: يجد عنصرًا باستخدام محدد CSS.
- `find_element_by_xpath("xpath")`: يجد عنصرًا باستخدام تعبير XPath.
- `find_elements_*`: يُرجع قائمة بجميع العناصر المطابقة (مثل `find_elements_by_tag_name`).

##### التفاعلات الأساسية
- `click()`: ينقر على عنصر.
- `send_keys("text")`: يكتب نصًا في حقل إدخال.
- `text`: يسترجع المحتوى النصي لعنصر.
- `get_attribute("attribute")`: يحصل على قيمة سمة العنصر (مثل `value`، `href`).
- `is_displayed()`, `is_enabled()`, `is_selected()`: يتحقق من حالة العنصر.

---

#### 4. **كتابة نص برمجي أساسي لـ Selenium**
إليك نموذج لنص برمجي يؤتمت عملية تسجيل الدخول إلى موقع ويب (باستخدام صفحة تسجيل دخول افتراضية للتوضيح).

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# تهيئة Chrome WebDriver
driver = webdriver.Chrome()

try:
    # الانتقال إلى صفحة تسجيل الدخول
    driver.get("https://example.com/login")
    
    # العثور على حقلي اسم المستخدم وكلمة المرور
    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")
    
    # إدخال بيانات الاعتماد
    username.send_keys("testuser")
    password.send_keys("testpassword")
    
    # إرسال النموذج
    password.send_keys(Keys.RETURN)
    
    # الانتظار حتى يتم تحميل الصفحة
    time.sleep(2)
    
    # التحقق من نجاح تسجيل الدخول (التحقق من وجود رسالة ترحيب)
    welcome_message = driver.find_element(By.CLASS_NAME, "welcome").text
    print(f"Login successful! Welcome message: {welcome_message}")
    
except Exception as e:
    print(f"An error occurred: {e}")
    
finally:
    # أغلق المتصفح
    driver.quit()
```

**ملاحظات**:
- استبدل `"https://example.com/login"` بالرابط الفعلي لموقع الويب المستهدف.
- اضبط أدوات تحديد المواقع (`By.ID`, `By.CLASS_NAME`) بناءً على هيكل HTML لموقع الويب.
- `time.sleep(2)` هو انتظار بسيط؛ للإنتاج، استخدم الانتظار الصريح (سيتم تغطيته لاحقًا).

---

#### 5. **الميزات المتقدمة**
يقدم Selenium ميزات متقدمة لأتمتة قوية.

##### أ. **آليات الانتظار**
يوفر Selenium نوعين من الانتظار للتعامل مع صفحات الويب الديناميكية:
- **الانتظار الضمني (Implicit Wait)**: يحدد وقت انتظار افتراضي لجميع عمليات البحث عن العناصر.
  ```python
  driver.implicitly_wait(10)  # انتظر حتى 10 ثوانٍ لظهور العناصر
  ```
- **الانتظار الصريح (Explicit Wait)**: ينتظر شرطًا محددًا (مثل أن يكون العنصر قابلاً للنقر).

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# تهيئة Chrome WebDriver
driver = webdriver.Chrome()

try:
    driver.get("https://example.com")
    
    # انتظر حتى يصبح العنصر قابلاً للنقر (حتى 10 ثوانٍ)
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "submit-button"))
    )
    button.click()
    
    print("Button clicked successfully!")
    
except Exception as e:
    print(f"An error occurred: {e}")
    
finally:
    driver.quit()
```

##### ب. **معالجة التنبيهات**
يمكن لـ Selenium التفاعل مع تنبيهات JavaScript والتأكيدات والطلبات:
```python
alert = driver.switch_to.alert
alert.accept()  # انقر فوق موافق
alert.dismiss()  # انقر فوق إلغاء
alert.send_keys("text")  # اكتب في المطالبة
```

##### ج. **التنقل بين الإطارات والنوافذ**
- **الإطارات/الإطارات المضمنة (Frames/Iframes)**: انتقل إلى إطار للتفاعل مع عناصره.
  ```python
  driver.switch_to.frame("frame-id")
  driver.switch_to.default_content()  # العودة إلى المحتوى الرئيسي
  ```
- **النوافذ/علامات التبويب**: التعامل مع نوافذ متصفح متعددة.
  ```python
  original_window = driver.current_window_handle
  for window_handle in driver.window_handles:
      driver.switch_to.window(window_handle)
  ```

##### د. **تنفيذ JavaScript**
شغّل كود JavaScript مباشرة في المتصفح:
```python
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # التمرير إلى الأسفل
```

##### هـ. **لقطات الشاشة**
التقاط لقطات الشاشة لأغراض التصحيح أو التوثيق:
```python
driver.save_screenshot("screenshot.png")
```

---

#### 6. **Selenium مع المتصفحات بلا واجهة رسومية (Headless)**
تعمل المتصفحات بلا واجهة رسومية بدون واجهة مستخدم رسومية، وهي مثالية لأنابيب CI/CD أو الخوادم.
مثال مع Chrome في الوضع بلا واجهة رسومية:

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# إعداد خيارات Chrome للوضع بلا واجهة رسومية
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

# تهيئة Chrome WebDriver في الوضع بلا واجهة رسومية
driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get("https://www.example.com")
    print(f"Page title: {driver.title}")
    
except Exception as e:
    print(f"An error occurred: {e}")
    
finally:
    driver.quit()
```

---

#### 7. **أفضل الممارسات**
- **استخدم الانتظار الصريح**: تجنب `time.sleep()` للصفحات الديناميكية؛ استخدم `WebDriverWait` مع `expected_conditions`.
- **تعامل مع الاستثناءات**: غلّف الكود في كتل `try-except` للتعامل مع الأخطاء بأمان.
- **أغلق WebDriver**: اطلب دائمًا `driver.quit()` لإغلاق المتصفح وإطلاق الموارد.
- **نظم أدوات تحديد المواقع**: خزن أدوات تحديد المواقع في ملف أو فئة منفصلة لسهولة الصيانة.
- **استخدم نموذج كائن الصفحة (Page Object Model - POM)**: ضع تفاعلات الصفحة في فئات لتحسين إعادة استخدام الكود.

مثال على نموذج كائن الصفحة:

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

# الاستخدام
from selenium import webdriver

driver = webdriver.Chrome()
login_page = LoginPage(driver)
try:
    driver.get("https://example.com/login")
    login_page.login("testuser", "testpassword")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()
```

---

#### 8. **Selenium Grid**
يسمح Selenium Grid بتشغيل الاختبارات عبر متصفحات أو أنظمة تشغيل أو أجهزة متعددة بالتوازي. يتكون من **محور (hub)** (خادم مركزي) و**عقد (nodes)** (أجهزة تشغل المتصفحات).
- **الإعداد**: قم بتكوين محور وعقد باستخدام ملف JAR الخاص بـ Selenium Grid أو Docker.
- **حالة الاستخدام**: اختيار التوافق بين المتصفحات (مثل Chrome على Windows، وFirefox على Linux).
- **مثال**: الاتصال بـ WebDriver عن بُعد:
  ```python
  from selenium.webdriver.remote.webdriver import WebDriver
  driver = WebDriver(command_executor="http://hub-ip:4444/wd/hub", desired_capabilities={"browserName": "chrome"})
  ```

---

#### 9. **التحديات الشائعة والحلول**
- **العنصر غير موجود**: استخدم الانتظار الصريح أو تحقق من أدوات تحديد المواقع باستخدام أدوات المطور في المتصفح.
- **مرجع عنصر قديم (Stale Element Reference)**: أعد تحديد موقع العناصر بعد تحديثات الصفحة أو تغييرات DOM.
- **أداء بطيء**: حسّن أدوات تحديد المواقع (افضل ID/CSS على XPath) واستخدم الوضع بلا واجهة رسومية.
- **محتوى ديناميكي**: استخدم تنفيذ JavaScript أو آليات الانتظار للتعامل مع المحتوى المحمل بـ AJAX.

---

#### 10. **الموارد**
- التوثيق الرسمي: [selenium.dev](https://www.selenium.dev/documentation/)
- ربط Selenium بـ Python: [selenium-python.readthedocs.io](https://selenium-python.readthedocs.io/)
- برامج تشغيل المتصفح: ChromeDriver، GeckoDriver
- المجتمع: Stack Overflow، منشورات X (ابحث عن #Selenium أو #WebDriver)

---

يغطي هذا الدليل الأساسيات الخاصة بـ Selenium WebDriver، من الإعداد إلى الاستخدام المتقدم. دعني أعلم إذا كنت بحاجة إلى مساعدة في مهمة Selenium محددة أو أمثلة أكثر تقدمًا!