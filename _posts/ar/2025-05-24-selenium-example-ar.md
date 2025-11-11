---
audio: false
generated: true
lang: ar
layout: post
title: سكريبت السيلينيوم
translated: true
type: note
---

فيما يلي مثال متطور لبرنامج سيلينيوم في بايثون يوضح ميزات متقدمة، بما في ذلك نموذج كائن الصفحة (POM)، و FacetGrid صريح للتخطيطات المتجاوبة، والانتظار الصريح، والتعامل مع المحتوى الديناميكي، ومعالجة الأخطاء. يقوم البرنامج النصي بأتمتة سيناريو معقد: scraping بيانات المنتج من موقع تجارة إلكترونية، والتنقل عبر صفحات متعددة، وإنشاء تقرير ملخص. يفترض المثال موقع ويب افتراضي للتجارة الإلكترونية لأغراض التوضيح، ولكن يمكن تكييف المفاهيم لتناسب مواقع الويب الحقيقية.

هذا المثال يوضح:
- **نموذج كائن الصفحة (POM)** للحصول على كود منظم وسهل الصيانة.
- **الانتظار الصريح** للتعامل مع المحتوى الديناميكي.
- **FacetGrid** للتعامل مع الجداول المتجاوبة.
- **متصفح headless** للتنفيذ الفعال.
- **معالجة البيانات** لإنشاء تقرير JSON.
- **معالجة الأخطاء** لزيادة المتانة.

```python
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import Select
import time

# Page Object لصفحة قائمة المنتجات
class ProductListingPage:
    def __init__(self, driver):
        self.driver = driver
        self.product_cards = (By.CLASS_NAME, "product-card")
        self.product_name = (By.CLASS_NAME, "product-name")
        self.product_price = (By.CLASS_NAME, "product-price")
        self.next_page_button = (By.ID, "next-page")
        self.sort_dropdown = (By.ID, "sort-options")

    def sort_by_price(self):
        try:
            sort_select = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.sort_dropdown)
            )
            select = Select(sort_select)
            select.select_by_value("price-asc")
            time.sleep(2)  # السماح بتطبيق الفرز
        except TimeoutException:
            print("لم يتم العثور على قائمة الفرز أو انتهت المهلة")

    def get_products(self):
        try:
            cards = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located(self.product_cards)
            )
            products = []
            for card in cards:
                name = card.find_element(*self.product_name).text
                price = card.find_element(*self.product_price).text
                products.append({"name": name, "price": price})
            return products
        except (TimeoutException, NoSuchElementException) as e:
            print(f"خطأ في استرجاع المنتجات: {e}")
            return []

    def go_to_next_page(self):
        try:
            next_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.next_page_button)
            )
            next_button.click()
            time.sleep(2)  # الانتظار حتى يتم تحميل الصفحة
            return True
        except TimeoutException:
            print("لم يتم العثور على زر الصفحة التالية أو انتهت المهلة")
            return False

# Page Object لصفحة البحث
class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_input = (By.ID, "search-bar")
        self.search_button = (By.ID, "search-submit")

    def search(self, query):
        try:
            search_box = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.search_input)
            )
            search_box.clear()
            search_box.send_keys(query)
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.search_button)
            ).click()
            time.sleep(2)  # الانتظار لظهور نتائج البحث
        except TimeoutException as e:
            print(f"فشل البحث: {e}")

# البرنامج النصي الرئيسي
def scrape_ecommerce_site():
    # إعداد Chrome في وضع headless
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=chrome_options)
    all_products = []

    try:
        # الانتقال إلى موقع الويب
        driver.get("https://example.com")
        
        # تهيئة كائنات الصفحات
        search_page = SearchPage(driver)
        product_page = ProductListingPage(driver)
        
        # تنفيذ البحث
        search_page.search("laptop")
        
        # الفرز حسب السعر
        product_page.sort_by_price()
        
        # جمع البيانات من صفحات متعددة
        page_count = 0
        max_pages = 3  # حد لأغراض العرض التوضيحي
        
        while page_count < max_pages:
            products = product_page.get_products()
            all_products.extend(products)
            print(f"تم جمع البيانات من الصفحة {page_count + 1}: {len(products)} منتج")
            
            if not product_page.go_to_next_page():
                break
            page_count += 1

        # إنشاء الملخص
        summary = {
            "total_products": len(all_products),
            "average_price": calculate_average_price(all_products),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        
        # حفظ النتائج في ملف JSON
        with open("product_data.json", "w") as f:
            json.dump({"products": all_products, "summary": summary}, f, indent=2)
        print("تم حفظ النتائج في product_data.json")

    except Exception as e:
        print(f"حدث خطأ: {e}")
    
    finally:
        driver.quit()

def calculate_average_price(products):
    if not products:
        return 0
    prices = []
    for product in products:
        try:
            price_str = product["price"].replace("$", "").replace(",", "")
            prices.append(float(price_str))
        except (ValueError, AttributeError):
            continue
    return sum(prices) / len(prices) if prices else 0

if __name__ == "__main__":
    scrape_ecommerce_site()
```

### شرح المثال
1. **نموذج كائن الصفحة (POM)**:
   - يستخدم البرنامج النصي فئتين لكائن الصفحة (`SearchPage` و `ProductListingPage`) لتغليف المنطق المخصص لكل صفحة، مما يجعل الكود معياريًا وسهل الصيانة.
   - تحتوي كل فئة على عناصر التحديد location والطرق methods للتفاعل مع عناصر الصفحة المحددة.

2. **المتصفح headless**:
   - يتم تشغيل Chrome في وضع headless للكفاءة، وهو مناسب لخطوط أنابيب CI/CD أو الخوادم.

3. **الانتظار الصريح**:
   - يتم استخدام `WebDriverWait` و `expected_conditions` للتعامل مع المحتوى الديناميكي، مما يضمن وجود العناصر أو إمكانية النقر عليها قبل التفاعل معها.

4. **التعامل مع الجداول المتجاوبة**:
   - يستخدم البرنامج النصي منطقًا مشابهًا لـ FacetGrid لجمع البيانات من جدول قائمة المنتجات، حيث يستخرج أسماء المنتجات وأسعارها من كل بطاقة.
   - يتعامل مع ترقيم الصفحات من خلال التنقل عبر صفحات متعددة (حتى حد أقصى قدره 3 في هذا المثال).

5. **معالجة الأخطاء**:
   - يلتقط البرنامج النصي `TimeoutException` و `NoSuchElementException` للتعامل مع العناصر المفقودة أو حالات انتهاء المهلة بشكل متحكم.
   - تضمن كتلة `try-finally` إغلاق المتصفح حتى في حالة حدوث خطأ.

6. **معالجة البيانات**:
   - يتم تخزين البيانات التي تم جمعها في قائمة من القواميس وتلخيصها (مثل إجمالي المنتجات، متوسط السعر).
   - يتم حفظ النتائج في ملف JSON (`product_data.json`) لاستخدامها لاحقًا.

7. **الفرز الديناميكي**:
   - يتفاعل البرنامج النصي مع قائمة dropdown لفرز المنتجات حسب السعر، محاكيًا سلوك المستخدم الحقيقي.

### المخرجات
ينتج البرنامج النصي ملف JSON (`product_data.json`) بالهيكل التالي:
```json
{
  "products": [
    {"name": "Laptop Model A", "price": "$999.99"},
    {"name": "Laptop Model B", "price": "$1299.99"},
    ...
  ],
  "summary": {
    "total_products": 30,
    "average_price": 1099.45,
    "timestamp": "2025-05-24 21:33:00"
  }
}
```

### ملاحظات
- **تكييف موقع الويب**: عناصر التحديد location (مثل `By.ID`، `By.CLASS_NAME`) وعنوان URL (`https://example.com`) هي عناصر نائبة. استبدلها بقيم فعلية من هيكل HTML لموقع الويب المستهدف، والذي يمكنك فحصه باستخدام أدوات المطور في المتصفح.
- **التبعيات**: تأكد من تثبيت `selenium` (`pip install selenium`) وتوفر برنامج تشغيل المتصفح المناسب (مثل ChromeDriver) في المسار PATH الخاص بك.
- **التحسينات**:
  - إضافة التسجيل logging لتحسين تصحيح الأخطاء.
  - تنفيذ منطق إعادة المحاولة للطلبات الشبكية غير المستقرة.
  - استخدام ملف إعدادات لعناصر التحديد location والإعدادات.
  - التوسع للتعامل مع سيناريوهات أكثر تعقيدًا مثل المصادقة أو CAPTCHA.

### تشغيل البرنامج النصي
1. قم بتثبيت التبعيات: `pip install selenium`.
2. قم بتنزيل وتكوين ChromeDriver.
3. استبدل عنوان URL وعناصر التحديد location بقيم من موقع تجارة إلكترونية حقيقي (مثل Amazon، eBay).
4. قم بتشغيل البرنامج النصي: `python advanced_selenium_ecommerce_scraper.py`.

يوضح هذا المثال برنامج سيلينيوم جاهز للإنتاج مع أفضل الممارسات. أعلمني إذا كنت بحاجة إلى مساعدة في تكييفه لموقع ويب معين أو إضافة ميزات مثل المصادقة أو التنفيذ المتوازي مع Selenium Grid!