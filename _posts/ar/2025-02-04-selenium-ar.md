---
audio: false
generated: false
image: false
lang: ar
layout: post
title: أتمتة متصفح الويب باستخدام سيلينيوم
translated: true
type: post
---

Selenium أداة قوية لأتمتة متصفحات الويب.  تتيح لك التحكم في المتصفح برمجياً لأداء إجراءات مثل الانتقال إلى صفحات الويب، وملء النماذج، والنقر على الأزرار، واستخراج البيانات.  يمكن أن يكون هذا مفيدًا لمجموعة متنوعة من المهام، بما في ذلك استخراج بيانات الويب، واختبار تطبيقات الويب، وأتمتة المهام المتكررة.

فيما يلي مثال أساسي لكيفية استخدام Selenium مع Python لاستخراج بيانات مدونة CSDN:

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

def scrape_csdn_blog(url):
    """
    تقوم باستخراج جميع الروابط (علامات a) من مصدر الصفحة باستخدام Selenium،
    وتصفية الروابط التي تبدأ بـ "https://blog.csdn.net/lzw_java/article".

    Args:
        url (str): عنوان URL لمدونة CSDN.
    """
    try:
        # إعداد خيارات Chrome للتصفح بدون واجهة رسومية
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # تشغيل Chrome في وضع بدون واجهة رسومية
        chrome_options.add_argument("--disable-gpu")  # تعطيل تسريع وحدة معالجة الرسومات (موصى به للوضع بدون واجهة رسومية)
        chrome_options.add_argument("--no-sandbox")  # تجاوز نموذج أمان نظام التشغيل
        chrome_options.add_argument("--disable-dev-shm-usage")  # التغلب على مشاكل الموارد المحدودة

        # تهيئة برنامج تشغيل Chrome
        driver = webdriver.Chrome(options=chrome_options)

        # تحميل صفحة الويب
        driver.get(url)

        # البحث عن جميع عناصر علامة 'a'
        links = driver.find_elements(By.TAG_NAME, 'a')

        if not links:
            print("لم يتم العثور على روابط في الصفحة.")
            driver.quit()
            return

        for link in links:
            try:
                href = link.get_attribute('href')
                if href and href.startswith("https://blog.csdn.net/lzw_java/article"):
                    text = link.text.strip()

                    print(f"النص: {text}")
                    print(f"URL: {href}")
                    print("-" * 20)

            except Exception as e:
                print(f"خطأ في استخراج الرابط: {e}")
                continue

    except Exception as e:
        print(f"حدث خطأ: {e}")
    finally:
        # إغلاق المتصفح
        if 'driver' in locals():
            driver.quit()

if __name__ == "__main__":
    blog_url = "https://blog.csdn.net/lzw_java?type=blog"  # استبدل بـ URL الفعلي
    scrape_csdn_blog(blog_url)

```