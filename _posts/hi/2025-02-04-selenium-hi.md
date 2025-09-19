---
audio: false
generated: false
image: false
lang: hi
layout: post
title: सेलेनियम के साथ वेब ब्राउज़र स्वचालन
translated: true
---

सेलेनियम वेब ब्राउज़रों को स्वचालित करने का एक शक्तिशाली उपकरण है। यह आपको प्रोग्रामेटिक रूप से एक ब्राउज़र को नियंत्रित करने की अनुमति देता है ताकि वेब पेजों पर नेविगेट करने, फॉर्म भरने, बटन क्लिक करने और डेटा निकालने जैसे कार्य किए जा सकें। यह वेब स्क्रैपिंग, वेब एप्लिकेशन का परीक्षण करने और दोहराए जाने वाले कार्यों को स्वचालित करने सहित कई कार्यों के लिए उपयोगी हो सकता है।

यहाँ पायथन के साथ सेलेनियम का उपयोग करके CSDN ब्लॉग को स्क्रैप करने का एक बुनियादी उदाहरण दिया गया है:

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

def scrape_csdn_blog(url):
    """
    सेलेनियम का उपयोग करके पृष्ठ स्रोत से सभी लिंक (a टैग) निकालता है और उन लिंक को फ़िल्टर करता है जो "https://blog.csdn.net/lzw_java/article" से शुरू होते हैं।

    Args:
        url (str): CSDN ब्लॉग का URL।
    """
    try:
        # हेडलेस ब्राउज़िंग के लिए क्रोम विकल्प सेट करें
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # क्रोम को हेडलेस मोड में चलाएँ
        chrome_options.add_argument("--disable-gpu")  # GPU त्वरण अक्षम करें (हेडलेस के लिए अनुशंसित)
        chrome_options.add_argument("--no-sandbox")  # OS सुरक्षा मॉडल को बायपास करें
        chrome_options.add_argument("--disable-dev-shm-usage")  # सीमित संसाधन समस्याओं को दूर करें

        # क्रोम ड्राइवर को इनिशियलाइज़ करें
        driver = webdriver.Chrome(options=chrome_options)

        # वेबपेज लोड करें
        driver.get(url)

        # सभी 'a' टैग तत्व खोजें
        links = driver.find_elements(By.TAG_NAME, 'a')

        if not links:
            print("पृष्ठ पर कोई लिंक नहीं मिला।")
            driver.quit()
            return

        for link in links:
            try:
                href = link.get_attribute('href')
                if href and href.startswith("https://blog.csdn.net/lzw_java/article"):
                    text = link.text.strip()

                    print(f"पाठ: {text}")
                    print(f"URL: {href}")
                    print("-" * 20)

            except Exception as e:
                print(f"लिंक निकालते समय त्रुटि: {e}")
                continue

    except Exception as e:
        print(f"एक त्रुटि हुई: {e}")
    finally:
        # ब्राउज़र बंद करें
        if 'driver' in locals():
            driver.quit()

if __name__ == "__main__":
    blog_url = "https://blog.csdn.net/lzw_java?type=blog"  # वास्तविक URL से बदलें
    scrape_csdn_blog(blog_url)

```
