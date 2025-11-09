---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: شرح كود استخراج البيانات باستخدام سيلينيوم
translated: true
type: note
---

### شرح استخدام واجهة برمجة تطبيقات Selenium في الكود المقدم

يستخدم هذا النص البرمجي Python مكتبة **Selenium WebDriver** لأتمتة متصفح ويب (تحديدًا Chrome) للتفاعل مع موقع ويب (على الأرجح بوابة بيانات/تجارة على الرابط `https://xxdata.com/index.aspx`). الهدف يبدو أنه **جلب البيانات من الويب**: تسجيل الدخول، والبحث عن بيانات التجارة/الطلبات (باستخدام رمز HS مثل '8449')، والتقلب عبر النتائج المقسمة إلى صفحات، والنقر على التفاصيل، واستخراج البيانات المنظمة من جداول HTML، وتخزينها في قاعدة بيانات SQLite (`data.db`).

يُستخدم Selenium هنا من أجل **أتمتة المتصفح**، مما يسمح للنص البرمجي بمحاكاة التفاعلات البشرية مثل الكتابة والنقل والتمرير والانتظار حتى يتم تحميل الصفحات — وهو أمر يصعب أو يستحيل تحقيقه باستخدام طلبات HTTP البسيطة (على سبيل المثال، بسبب الصفحات الغنية بـ JavaScript، أو iframes، أو المحتوى الديناميكي). يتعامل مع عناصر الويب الديناميكية، والجلسات، والتبديل بين النوافذ أو iframes المتعددة، وهي أمور شائعة في تطبيقات الويب الحديثة.

سأقوم بتفصيله **قسمًا بقسم**، مع تسليط الضوء على واجهات برمجة تطبيقات Selenium الرئيسية، والغرض منها، وكيفية استخدامها. ملاحظة: بعض الطرق في الكود (مثل `find_element_by_css_selector`) تعود لإصدارات Selenium القديمة (ما قبل 4.0) وهي مهملة. في Selenium الحديث (4+)، يجب استخدام `find_element(By.CSS_SELECTOR, ...)` بدلاً من ذلك، ولكن الوظيفة تبقى كما هي. يستورد النص البرمجي أيضًا الوحدات النمطية الضرورية للانتظار، والاستثناءات، والتعامل مع العناصر.

#### 1. **الاستيراد والإعداد (تهيئة Selenium)**
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
   - **الغرض**: تستورد هذه المكونات الأساسية لـ Selenium:
     - `webdriver`: الوحدة النمطية الرئيسية للتحكم في المتصفح.
     - `WebDriver`: تلميح نوع لمثيل المتصفح (يضمن سلامة النوع).
     - `Keys`: لمحاكاة مدخلات لوحة المفاتيح (مثل Page Up).
     - الاستثناءات: للتعامل مع الأخطاء الشائعة مثل انتهاء المهلة أو العناصر غير الطازجة (العناصر التي تتغير بعد تحديث الصفحة).
     - `WebDriverWait` و `EC` (الشروط المتوقعة): للانتظارات الصريحة — الانتظار حتى يستوفي العنصر شرطًا معينًا (مثل وجوده في الصفحة).
     - `By`: استراتيجيات تحديد الموقع (مثل محدد CSS، المعرف، اسم العلامة) للعثور على العناصر.
     - `WebElement`: يمثل عناصر HTML للتفاعل.

   في دالة `run()`:
   ```python
   options = webdriver.ChromeOptions()
   options.add_argument("--start-maximized")  # يفتح المتصفح في وضع ملء الشاشة.
   options.add_argument('--log-level=3')      # يكبت سجلات وحدة التحكم للحصول على نتائج أكثر نظافة.
   browser: WebDriver = webdriver.Chrome(executable_path="./chromedriver", options=options)
   ```
   - **واجهة برمجة تطبيقات Selenium المستخدمة**: `webdriver.Chrome(options=...)`
     - يقوم بتهيئة مثيل متصفح Chrome باستخدام ملف `chromedriver` محلي (يجب أن يكون في دليل النص البرمجي).
     - `ChromeOptions`: يخصص جلسة المتصفح (على سبيل المثال، يمكن إضافة الوضع headless باستخدام `options.add_argument("--headless")` للتشغيل في الخلفية).
     - ينشئ هذا نافذة متصفح حية يمكن التحكم فيها. يعمل Selenium كجسر بين Python وبروتوكول DevTools الخاص بالمتصفح.

   ```python
   browser.get('https://xxdata.com/index.aspx')
   ```
   - **واجهة برمجة تطبيقات Selenium المستخدمة**: `WebDriver.get(url)`
     - يتنقل إلى عنوان URL البداية، ويحمل الصفحة كما يفعل المستخدم عند كتابتها في شريط العناوين.

#### 2. **عملية تسجيل الدخول**
   ```python
   input_username = browser.find_element_by_css_selector('input[name=username]')
   input_username.send_keys('name')
   input_password = browser.find_element_by_css_selector('input[name=password]')
   input_password.send_keys('password')
   btn_login = browser.find_element_by_css_selector('div.login-check')
   btn_login.click()
   ```
   - **واجهات برمجة تطبيقات Selenium المستخدمة**:
     - `WebDriver.find_element_by_css_selector(css)` (مهملة؛ الطريقة الحديثة: `find_element(By.CSS_SELECTOR, css)`): يحدد موقع عنصر HTML واحد باستخدام محدد CSS (على سبيل المثال، حسب السمة مثل `name="username"`). يُرجع `WebElement`.
     - `WebElement.send_keys(text)`: يحاكي الكتابة في حقل إدخال (مثل اسم المستخدم/كلمة المرور).
     - `WebElement.click()`: يحاكي النقر بالماوس على زر أو رابط.
   - **كيفية استخدام Selenium**: يؤتمت إرسال النموذج. بدون Selenium، ستحتاج إلى هندسة عكسية لطلبات POST، ولكن هذا يتعامل مع التحقق من صحة JavaScript أو النماذج الديناميكية بسلاسة. بيانات الاعتماد مثبتة في الكود (غير آمنة في الإنتاج — استخدم متغيرات البيئة).

   بعد تسجيل الدخول:
   ```python
   wait_element(browser, 'div.dsh_01')
   ```
   - يستدعي دالة `wait_element` المخصصة (سيتم شرحها لاحقًا) لإيقاف التنفيذ مؤقتًا حتى يتم تحميل لوحة التحكم.

#### 3. **التنقل والبحث**
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
   - **واجهات برمجة تطبيقات Selenium المستخدمة**:
     - `find_element_by_css_selector`: يحدد موقع عناصر التنقل (مثل div لوحة التحكم، رابط الأيقونة).
     - `WebElement.click()`: ينقر للتنقل (على سبيل المثال، إلى قسم "التجارة").
     - `WebElement.get_attribute('id')`: يسترد سمة HTML (هنا، معرف iframe).
     - `WebDriver.switch_to.frame(frame_id)`: يحول سياق السائق إلى `<iframe>` (شائع في التطبيقات لتضمين المحتوى). بدون هذا، تصبح العناصر داخل iframe غير قابلة للوصول.
   - **كيفية استخدام Selenium**: يتعامل مع التنقل متعدد الخطوات والمحتوى المضمن. تعزل Iframes DOMs، لذا يعد التبديل ضروريًا لجلب البيانات من الصفحات الداخلية.

   عملية البحث:
   ```python
   input_search = browser.find_element_by_id('_easyui_textbox_input7')  # يستخدم محدد المعرف.
   input_search.send_keys('8449')
   time.sleep(10)
   enter = browser.find_element_by_css_selector('a#btnOk > div.enter-bt')
   enter.click()
   ```
   - **واجهات برمجة تطبيقات Selenium المستخدمة**:
     - `find_element_by_id(id)` (مهملة؛ الطريقة الحديثة: `find_element(By.ID, id)`): يحدد الموقع بواسطة سمة HTML `id`.
     - `send_keys`: يكتب استعلام البحث (رمز HS للمنتجات).
     - `time.sleep(10)`: انتظار ضمني (بدائي؛ من الأفضل استخدام الانتظارات الصريحة).
     - `click()`: يرسل البحث.
   - **كيفية استخدام Selenium**: يحاكي بحث المستخدم. يقوم `time.sleep` بإيقاف التنفيذ مؤقتًا لتحميل نتائج AJAX/JavaScript.

#### 4. **ترقيم الصفحات ومعالجة النتائج**
   ```python
   result_count_span = browser.find_element_by_css_selector('span#ResultCount')
   page = math.ceil(int(result_count_span.text) / 20)  # يحسب إجمالي الصفحات (20 نتيجة/صفحة).
   skip = 0
   page = page - skip

   for p in range(page):
       input_page = browser.find_element_by_css_selector('input.laypage_skip')
       input_page.send_keys(str(p + skip + 1))
       btn_confirm = browser.find_element_by_css_selector('button.laypage_btn')
       btn_confirm.click()
       time.sleep(2)

       locates = browser.find_elements_by_css_selector('div.rownumber-bt')  # عناصر متعددة.
       print('page ' + str(p) + ' size: ' + str(len(locates)))
       for locate in locates:
           browser.execute_script("arguments[0].scrollIntoView();", locate)  # تمرير JavaScript.
           time.sleep(1)
           browser.find_element_by_tag_name('html').send_keys(Keys.PAGE_UP)  # تمرير بلوحة المفاتيح.
           time.sleep(1)
           try:
               locate.click()
           except ElementClickInterceptedException:
               print('ElementClickInterceptedException')
               continue
           except StaleElementReferenceException:
               print('StaleElementReferenceException')
               continue
           # ... (المزيد أدناه)
   ```
   - **واجهات برمجة تطبيقات Selenium المستخدمة**:
     - `find_element_by_css_selector`: يحصل على عدد النتائج من عنصر span.
     - `WebElement.text`: يستخرج النص المرئي من عنصر (مثل العدد مثل "100").
     - `find_elements_by_css_selector` (الجمع؛ مهملة: `find_elements(By.CSS_SELECTOR, ...)`): يجد عناصر متعددة (مثل روابط الصفوف في الصفحة). يُرجع قائمة من `WebElement`s.
     - `WebDriver.execute_script(js_code, *args)`: يشغل JavaScript مخصص في المتصفح (هنا، يقوم بالتمرير إلى عنصر لتجنب مشاكل النقر).
     - `WebDriver.find_element_by_tag_name('html').send_keys(Keys.PAGE_UP)`: يحاكي التمرير بلوحة المفاتيح (باستخدام تعداد `Keys`).
     - الاستثناءات: تلتقط حالات فشل النقر (مثل عندما يحجب overlay النقر) أو العناصر غير الطازجة (تم تحديث DOM، مما يجعل المراجع غير صالحة — شائع في واجهات المستخدم الديناميكية).
   - **كيفية استخدام Selenium**: يؤتمت ترقيم الصفحات عن طريق كتابة أرقام الصفحات والنقر على "انتقال". لكل صف نتيجة (`div.rownumber-bt`)، يقوم بالتمرير لضمان الرؤية، ثم ينقر لفتح التفاصيل في نافذة جديدة. يتعامل هذا مع السلوك المشابه للتحميل البطيء أو التمرير اللانهائي.

#### 5. **تبديل النوافذ/Iframes واستخراج البيانات**
   متابعة من الحلقة:
   ```python
   time.sleep(1)
   browser.switch_to.window(browser.window_handles[1])  # التبديل إلى علامة تبويب/نافذة جديدة.
   wait_element(browser, 'div#content')
   try:
       save_page(browser)
   except IndexError:
       print('IndexError')
       continue
   browser.close()  # يغلق نافذة التفاصيل.
   browser.switch_to.window(browser.window_handles[0])  # العودة إلى النافذة الرئيسية.
   browser.switch_to.frame(iframe_id)  # العودة إلى سياق iframe.
   ```
   - **واجهات برمجة تطبيقات Selenium المستخدمة**:
     - `WebDriver.window_handles`: قائمة بمعرفات النوافذ/علامات التبويب المفتوحة.
     - `WebDriver.switch_to.window(handle)`: يحول التركيز إلى نافذة محددة (المؤشر 0 = الرئيسية، 1 = علامة التبويب الجديدة التي فتحها النقر).
     - `WebDriver.close()`: يغلق النافذة الحالية.
   - **كيفية استخدام Selenium**: تفتح النقرات التفاصيل في علامات تبويب جديدة، لذا يقوم بتبديل السياقات لجلب البيانات منها، ثم يعود. هذا أمر بالغ الأهمية للتطبيقات متعددة علامات التبويب.

#### 6. **استخراج البيانات في دالة `save_page(browser: WebDriver)`**
   هذا هو منطق جلب البيانات الأساسي:
   ```python
   ts = browser.find_elements_by_css_selector('table')  # جميع الجداول في الصفحة.
   t0 = ts[0]
   tds0 = t0.find_elements_by_tag_name('td')  # خلايا TD في الجدول الأول.
   order_number = tds0[2].text  # يستخرج النص من خلايا محددة.
   # ... (مشابه لجداول أخرى: t1, t2, إلخ.)
   ```
   - **واجهات برمجة تطبيقات Selenium المستخدمة**:
     - `find_elements_by_css_selector('table')` / `find_elements_by_tag_name('td')` (مهملة: استخدم `By.TAG_NAME`): يجد جميع `<table>`s وخلايا `<td>` الخاصة بها.
     - `WebElement.text`: يسحب محتوى النص من الخلايا (مثل رقم الطلب، اسم المستورد).
     - المخصص `tds_to_text(tds: list[WebElement])`: يربط النص من أزواج `<td>` (مثل التسمية + القيمة).
   - **كيفية استخدام Selenium**: يحلل بنية DOM للصفحة (جداول تحتوي على تفاصيل الطلب/المستورد/المصدر). يتعامل مع أعداد الجداول المتغيرة (على سبيل المثال، إذا كان `len(ts) == 8`، فهناك جداول إضافية). ثم يتم إدخال البيانات في SQLite (جزء غير مرتبط بـ Selenium).

   يستخرج المنطق الشرطي حقولاً مثل `order_number`, `importer`, `exporter`، إلخ، بناءً على فهارس الجداول — بافتراض تخطيط ثابت.

#### 7. **الانتظارات ومعالجة الأخطاء (دالة `wait_element`)**
   ```python
   def wait_element(browser, css):
       timeout = 30
       try:
           element_present = EC.presence_of_element_located((By.CSS_SELECTOR, css))
           WebDriverWait(browser, timeout).until(element_present)
       except TimeoutException:
           print('Timed out waiting for page to load')
   ```
   - **واجهات برمجة تطبيقات Selenium المستخدمة**:
     - `expected_conditions.presence_of_element_located(locator)`: ينتظر حتى يوجد العنصر في DOM (ليس بالضرورة مرئيًا).
     - `WebDriverWait(driver, timeout).until(condition)`: يطلب كل 0.5 ثانية حتى 30 ثانية لتحقق الشرط.
     - `TimeoutException`: يتم رفعه إذا فشل الانتظار.
   - **كيفية استخدام Selenium**: يمنع ظروف السباق (مثل النقر قبل تحميل الصفحة). أفضل من `time.sleep` لأنه محدد للعنصر وأكثر كفاءة.

#### 8. **التنظيف**
   ```python
   time.sleep(1000)  # توقف طويل (لأغراض التصحيح؟).
   browser.quit()    # يغلق المتصفح وينهي الجلسة.
   ```
   - **واجهة برمجة تطبيقات Selenium المستخدمة**: `WebDriver.quit()`: ينهي السائق، ويغلق جميع النوافذ، ويحرر الموارد.

#### كيف يتناسب Selenium بشكل عام
- **تدفق الأتمتة**: يطلق Selenium متصفحًا حقيقيًا، ويحمل الصفحات، ويتفاعل عبر استعلامات DOM (محددات المواقع مثل CSS/ID)، ويتعامل مع السلوكيات الديناميكية (تنفيذ JS، الانتظارات، التبديلات). إنه مثالي لتطبيقات الصفحة الواحدة أو المواقع المحمية ذات الجلسات/الكوكيز.
- **نقاط القوة هنا**: يتعامل مع حالة تسجيل الدخول، و iframes، وعلامات التبويب الجديدة، والتمرير — حيث لا يمكن لأدوات جلب البيانات مثل BeautifulSoup/Requests القيام بذلك وحدها.
- **القيود/المشاكل في الكود**:
  - محددات مواقع مهملة: قم بالتحديث إلى `By` لضمان استمرارية العمل في المستقبل.
  - أوقات انتظار مثبتة في الكود: استبدل المزيد منها بالانتظارات لتسريع العمل/تقليل عدم الموثوقية.
  - الاستثناءات: معالجة جيدة، ولكن يمكن إعادة المحاولة عند حدوث StaleElement.
  - الأخلاقيات/القانونية: قد يخالف جلب البيانات شروط الخدمة؛ أضف رؤوس user-agent أو وكلاء للتحايل لمحاكاة المستخدمين البشريين.
  - الأداء: يعمل في الوضع headful (متصفح مرئي)；اجعله headless للإنتاج.
- **تشغيله**: يتطلب ChromeDriver (قم بتنزيله من موقع Selenium، وطابقه مع إصدار Chrome). قم بتثبيت Selenium عبر `pip install selenium`.

إذا كانت لديك أسئلة حول أجزاء محددة، أو تحديث الكود، أو تصحيح الأخطاء، فأخبرني!