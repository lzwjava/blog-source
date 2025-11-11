---
audio: false
generated: true
lang: hi
layout: post
title: सेलेनियम स्क्रिप्ट
translated: true
type: note
---

नीचे पायथन में एक उन्नत सेलेनियम स्क्रिप्ट का एक परिष्कृत उदाहरण दिया गया है जो उन्नत सुविधाओं को प्रदर्शित करता है, जिसमें पेज ऑब्जेक्ट मॉडल (POM), रिस्पॉन्सिव लेआउट के लिए एक्सप्लिसिट फेसेटग्रिड, एक्सप्लिसिट वेट्स, डायनामिक कंटेंट को हैंडल करना और एरर हैंडलिंग शामिल है। यह स्क्रिप्ट एक जटिल परिदृश्य को ऑटोमेट करती है: एक ई-कॉमर्स वेबसाइट से उत्पाद डेटा स्क्रैप करना, कई पेजों के माध्यम से नेविगेट करना और एक सारांश रिपोर्ट तैयार करना। यह उदाहरण प्रदर्शन उद्देश्यों के लिए एक काल्पनिक ई-कॉमर्स वेबसाइट मानता है, लेकिन इन अवधारणाओं को वास्तविक वेबसाइटों के लिए अनुकूलित किया जा सकता है।

यह उदाहरण प्रदर्शित करता है:
- **पेज ऑब्जेक्ट मॉडल (POM)** संगठित और रखरखाव योग्य कोड के लिए।
- **एक्सप्लिसिट वेट्स** डायनामिक कंटेंट को हैंडल करने के लिए।
- **फेसेटग्रिड** रिस्पॉन्सिव टेबल हैंडलिंग के लिए।
- **हेडलेस ब्राउज़र** कुशल एक्सेक्यूशन के लिए।
- **डेटा प्रोसेसिंग** एक JSON रिपोर्ट तैयार करने के लिए।
- **एरर हैंडलिंग** मजबूती के लिए।

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

# प्रोडक्ट लिस्टिंग पेज के लिए पेज ऑब्जेक्ट
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
            time.sleep(2)  # Allow sorting to apply
        except TimeoutException:
            print("Sort dropdown not found or timed out")

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
            print(f"Error retrieving products: {e}")
            return []

    def go_to_next_page(self):
        try:
            next_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.next_page_button)
            )
            next_button.click()
            time.sleep(2)  # Wait for page load
            return True
        except TimeoutException:
            print("No next page button found or timed out")
            return False

# सर्च पेज के लिए पेज ऑब्जेक्ट
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
            time.sleep(2)  # Wait for search results
        except TimeoutException as e:
            print(f"Search failed: {e}")

# मुख्य स्क्रिप्ट
def scrape_ecommerce_site():
    # Set up headless Chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=chrome_options)
    all_products = []

    try:
        # Navigate to the website
        driver.get("https://example.com")
        
        # Initialize page objects
        search_page = SearchPage(driver)
        product_page = ProductListingPage(driver)
        
        # Perform search
        search_page.search("laptop")
        
        # Sort by price
        product_page.sort_by_price()
        
        # Scrape multiple pages
        page_count = 0
        max_pages = 3  # Limit for demo
        
        while page_count < max_pages:
            products = product_page.get_products()
            all_products.extend(products)
            print(f"Scraped page {page_count + 1}: {len(products)} products")
            
            if not product_page.go_to_next_page():
                break
            page_count += 1

        # Generate summary
        summary = {
            "total_products": len(all_products),
            "average_price": calculate_average_price(all_products),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        
        # Save results to JSON
        with open("product_data.json", "w") as f:
            json.dump({"products": all_products, "summary": summary}, f, indent=2)
        print("Results saved to product_data.json")

    except Exception as e:
        print(f"An error occurred: {e}")
    
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

### उदाहरण की व्याख्या
1. **पेज ऑब्जेक्ट मॉडल (POM)**:
   - स्क्रिप्ट पेज-विशिष्ट लॉजिक को एनकैप्सुलेट करने के लिए दो पेज ऑब्जेक्ट क्लास (`SearchPage` और `ProductListingPage`) का उपयोग करती है, जिससे कोड मॉड्यूलर और रखरखाव योग्य बनता है।
   - प्रत्येक क्लास में विशिष्ट पेज एलिमेंट्स के साथ इंटरैक्ट करने के लिए लोकेटर्स और मेथड्स शामिल हैं।

2. **हेडलेस ब्राउज़र**:
   - स्क्रिप्ट दक्षता के लिए Chrome को हेडलेस मोड में चलाती है, जो CI/CD पाइपलाइन या सर्वर के लिए उपयुक्त है।

3. **एक्सप्लिसिट वेट्स**:
   - डायनामिक कंटेंट को हैंडल करने के लिए `WebDriverWait` और `expected_conditions` का उपयोग किया जाता है, यह सुनिश्चित करते हुए कि इंटरैक्शन से पहले एलिमेंट्स मौजूद या क्लिक करने योग्य हैं।

4. **रिस्पॉन्सिव टेबल हैंडलिंग**:
   - स्क्रिप्ट प्रत्येक कार्ड से उत्पाद नाम और कीमत निकालने के लिए फेसेटग्रिड-जैसे लॉजिक का उपयोग करती है।
   - यह कई पेजों के माध्यम से नेविगेट करके (इस उदाहरण के लिए अधिकतम 3 तक) पेजिनेशन को हैंडल करती है।

5. **एरर हैंडलिंग**:
   - स्क्रिप्ट गायब एलिमेंट्स या टाइमआउट को सहजता से हैंडल करने के लिए `TimeoutException` और `NoSuchElementException` को कैच करती है।
   - एक `try-finally` ब्लॉक यह सुनिश्चित करता है कि एरर होने पर भी ब्राउज़र बंद हो जाए।

6. **डेटा प्रोसेसिंग**:
   - स्क्रैप किया गया डेटा डिक्शनरी की एक लिस्ट में स्टोर किया जाता है और इसका सारांश तैयार किया जाता है (जैसे, कुल उत्पाद, औसत कीमत)।
   - परिणामों को आगे के उपयोग के लिए एक JSON फ़ाइल (`product_data.json`) में सेव किया जाता है।

7. **डायनामिक सॉर्टिंग**:
   - स्क्रिप्ट वास्तविक उपयोगकर्ता व्यवहार का अनुकरण करते हुए, उत्पादों को कीमत के आधार पर सॉर्ट करने के लिए एक ड्रॉपडाउन के साथ इंटरैक्ट करती है।

### आउटपुट
स्क्रिप्ट निम्नलिखित संरचना के साथ एक JSON फ़ाइल (`product_data.json`) तैयार करती है:
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

### नोट्स
- **वेबसाइट अनुकूलन**: लोकेटर्स (`By.ID`, `By.CLASS_NAME`) और URL (`https://example.com`) प्लेसहोल्डर हैं। लक्ष्य वेबसाइट की HTML संरचना से वास्तविक मानों के साथ उन्हें बदलें, जिसे आप ब्राउज़र डेवलपर टूल्स का उपयोग करके इंस्पेक्ट कर सकते हैं।
- **डिपेंडेंसीज़**: सुनिश्चित करें कि आपके पास `selenium` इंस्टॉल है (`pip install selenium`) और आपके PATH में उपयुक्त ब्राउज़र ड्राइवर (जैसे, ChromeDriver) है।
- **सुधार**:
  - बेहतर डीबगिंग के लिए लॉगिंग जोड़ें।
  - अस्थिर नेटवर्क अनुरोधों के लिए रिट्राई लॉजिक लागू करें।
  - लोकेटर्स और सेटिंग्स के लिए एक कॉन्फ़िगरेशन फ़ाइल का उपयोग करें।
  - प्रमाणीकरण या CAPTCHA जैसे अधिक जटिल परिदृश्यों को हैंडल करने के लिए विस्तारित करें।

### स्क्रिप्ट चलाना
1. डिपेंडेंसीज़ इंस्टॉल करें: `pip install selenium`.
2. ChromeDriver डाउनलोड और कॉन्फ़िगर करें।
3. URL और लोकेटर्स को किसी वास्तविक ई-कॉमर्स साइट (जैसे, Amazon, eBay) के साथ बदलें।
4. स्क्रिप्ट चलाएं: `python advanced_selenium_ecommerce_scraper.py`.

यह उदाहरण सर्वोत्तम प्रथाओं के साथ एक प्रोडक्शन-रेडी सेलेनियम स्क्रिप्ट प्रदर्शित करता है। यदि आपको इसे किसी विशिष्ट वेबसाइट के लिए अनुकूलित करने या प्रमाणीकरण या सेलेनियम ग्रिड के साथ समानांतर एक्सेक्यूशन जैसी सुविधाएँ जोड़ने में सहायता की आवश्यकता है, तो मुझे बताएं!