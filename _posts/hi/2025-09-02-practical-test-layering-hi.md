---
audio: false
generated: true
image: false
lang: hi
layout: post
title: प्रैक्टिकल टेस्ट लेयरिंग गाइड
translated: true
type: note
---

बढ़िया सवाल। एक समझदार परीक्षण रणनीति मुख्य रूप से **जोखिम और फीडबैक की गति** के बारे में है। यहाँ **किस परत पर क्या परीक्षण करें** यह तय करने का एक व्यावहारिक तरीका दिया गया है—कोई टेबल नहीं, बस स्पष्ट नियम और उदाहरण।

---

# मूल सिद्धांत

* **कार्यान्वयन (implementation) को नहीं, बल्कि व्यवहार (behavior) को परखें।** निजी विवरणों पर सार्वजनिक API को प्राथमिकता दें।
* **बग को पकड़ने वाली सबसे तेज परत** पर ज्यादातर जांचें धकेलें।
* **वास्तविक निर्भरताएं केवल तभी उपयोग करें जब जोखिम उचित हो** (डीबी, क्यू, ब्राउज़र)।
* **महत्वपूर्ण पथों को एंड-टू-एंड कवर करें, लेकिन संयम से।** UI टेस्ट सबसे नाजुक और धीमे होते हैं; उन्हें वास्तव में महत्वपूर्ण चीजों के लिए बचाकर रखें।

---

# क्या कहाँ जाता है (त्वरित अनुमान)

## 1) यूनिट टेस्ट (तेज, अलग-थलग)

**उपयोग करें जब:** शुद्ध/डोमेन लॉजिक को I/O (डीबी, HTTP, फाइलसिस्टम) के बिना परखा जा सके।

* बिजनेस नियम, मूल्य निर्धारण/फीस कैलकुलेशन, वैलिडेटर, मैपर, यूटिलिटीज।
* रेपो/क्लाइंट के साथ सर्विस मेथड्स को **मॉक** करके।
* लक्ष्य: बहुत सारे छोटे टेस्ट; मिलीसेकंड में फेल होना।

**Java/Spring उदाहरण**

```java
@ExtendWith(MockitoExtension.class)
class FeeServiceTest {
  @Mock AccountRepo repo;
  @InjectMocks FeeService svc;

  @Test void vipGetsDiscount() {
    when(repo.tier("u1")).thenReturn("VIP");
    assertEquals(Money.of(90), svc.charge("u1", Money.of(100)));
    verify(repo).tier("u1");
  }
}
```

## 2) इंटीग्रेशन / कंपोनेंट टेस्ट (वास्तविक वायरिंग, न्यूनतम मॉक)

**उपयोग करें जब:** आपको Spring वायरिंग, सीरियलाइजेशन, फिल्टर्स, DB क्वेरीज़, ट्रांजैक्शन्स को सत्यापित करने की आवश्यकता हो।

* **नेटवर्क के बिना HTTP लेयर**: `@WebMvcTest` (कंट्रोलर्स + json), या पूर्ण स्टैक के लिए `@SpringBootTest(webEnvironment=RANDOM_PORT)`।
* **DB शुद्धता**: वास्तविक DB चलाने के लिए **Testcontainers** का उपयोग करें; SQL, इंडेक्स, माइग्रेशन जांचें।
* **मैसेजिंग**: वास्तविक ब्रोकर कंटेनर (Kafka/RabbitMQ) के साथ कंज्यूमर/प्रोड्यूसर का परीक्षण करें।

**HTTP स्लाइस उदाहरण**

```java
@WebMvcTest(controllers = OrderController.class)
class OrderControllerTest {
  @Autowired MockMvc mvc;
  @MockBean OrderService svc;

  @Test void createsOrder() throws Exception {
    when(svc.create(any())).thenReturn(new Order("id1", 100));
    mvc.perform(post("/orders").contentType("application/json")
        .content("{\"amount\":100}"))
      .andExpect(status().isCreated())
      .andExpect(jsonPath("$.id").value("id1"));
  }
}
```

**Testcontainers के साथ DB**

```java
@Testcontainers
@SpringBootTest
class RepoIT {
  @Container static PostgreSQLContainer<?> db = new PostgreSQLContainer<>("postgres:16");
  @Autowired OrderRepo repo;

  @Test void persistsAndQueries() {
    var saved = repo.save(new OrderEntity(null, 100));
    assertTrue(repo.findById(saved.getId()).isPresent());
  }
}
```

## 3) API कॉन्ट्रैक्ट और एंड-टू-एंड API टेस्ट

**उपयोग करें जब:** आपको **बैकवर्ड-कम्पैटिबल कॉन्ट्रैक्ट्स** या पूर्ण सिस्टम वर्कफ़्लो की गारंटी देनी हो।

* **कॉन्ट्रैक्ट टेस्ट** (जैसे, OpenAPI स्कीमा वैलिडेशन या Pact) UI के बिना ब्रेकिंग चेंजेज को पकड़ते हैं।
* **एंड-टू-एंड API फ़्लो**: ऐप को वास्तविक DB के साथ स्पिन करें और HTTP (RestAssured) के माध्यम से हिट करें। हैप्पी पाथ + कुछ महत्वपूर्ण एज केस पर ध्यान केंद्रित करें।

**API E2E उदाहरण**

```java
@SpringBootTest(webEnvironment = WebEnvironment.RANDOM_PORT)
class ApiFlowIT {
  @LocalServerPort int port;
  @Test void happyPath() {
    given().port(port).contentType("application/json")
      .body("{\"amount\":100}")
      .when().post("/orders")
      .then().statusCode(201)
      .body("amount", equalTo(100));
  }
}
```

## 4) UI एंड-टू-एंड टेस्ट (ब्राउज़र)

**उपयोग करें जब:** केवल **कुछ** महत्वपूर्ण यूजर जर्नी को वास्तविक ब्राउज़र में सिद्ध करना हो:

* ऑथ + चेकआउट; पैसों का लेन-देन; PII फ़्लो; फ़ाइल अपलोड।
* **3–10 मुख्य परिदृश्यों** तक सीमित रखें। बाकी सब कुछ: यूनिट/इंटीग्रेशन/API लेयर पर कवर करें।

**Selenium vs. Playwright/Cypress?**

* **आधुनिक Angular ऐप्स के लिए Playwright** (या Cypress) को प्राथमिकता दें: ऑटो-वेटिंग, आसान सेलेक्टर्स, समानांतरता, बिल्ट-इन ट्रेस व्यूअर, Chromium/Firefox/WebKit में स्थिर हेडलेस रन।
* **Selenium का उपयोग करें** यदि आपको **कस्टम ग्रिड में वास्तविक वेंडर ब्राउज़र** चलाने हैं, **लेगेसी/एंटरप्राइज़** सेटअप के साथ इंटरैक्ट करना है, या आपके पास पहले से ही परिपक्व Selenium इन्फ्रा है। यह अधिक प्लंबिंग है; आपको स्पष्ट वेट और स्पीड के लिए ग्रिड की आवश्यकता होगी।

**Playwright (TypeScript) उदाहरण**

```ts
import { test, expect } from '@playwright/test';

test('checkout happy path', async ({ page }) => {
  await page.goto('http://localhost:4200');
  await page.getByRole('button', { name: 'Sign in' }).click();
  await page.getByLabel('Email').fill('u@example.com');
  await page.getByLabel('Password').fill('secret');
  await page.getByRole('button', { name: 'Login' }).click();

  await page.getByText('Add to cart', { exact: true }).first().click();
  await page.getByRole('button', { name: 'Checkout' }).click();
  await expect(page.getByText('Order confirmed')).toBeVisible();
});
```

**यदि आपको Selenium (Java) का उपयोग करना ही है**

```java
WebDriver d = new ChromeDriver();
d.get("http://localhost:4200");
new WebDriverWait(d, Duration.ofSeconds(10))
  .until(ExpectedConditions.elementToBeClickable(By.id("loginBtn"))).click();
```

---

# परत दर परत निर्णय लेना (त्वरित प्रवाह)

1. **क्या इसका I/O के बिना परीक्षण किया जा सकता है?**
   → हाँ: **यूनिट टेस्ट** करें।

2. **क्या यह फ्रेमवर्क वायरिंग/सीरियलाइजेशन या DB क्वेरीज़ पर निर्भर करता है?**
   → हाँ: **इंटीग्रेशन/कंपोनेंट** टेस्ट (Spring स्लाइस, Testcontainers)।

3. **क्या यह क्रॉस-सर्विस/पब्लिक API कॉन्ट्रैक्ट है?**
   → हाँ: **कॉन्ट्रैक्ट टेस्ट** (स्कीमा/Pact) + कुछ **API E2E** फ़्लो।

4. **क्या मूल्य केवल UI में दिखाई देता है या महत्वपूर्ण UX है?**
   → हाँ: **UI E2E**, लेकिन केवल मुख्य जर्नी।

---

# समझदार अनुपात और बजट

* लगभग **70–80% यूनिट**, **15–25% इंटीग्रेशन/API**, **5–10% UI E2E** का लक्ष्य रखें।
* प्रति-कमिट CI को तेज रखें: यूनिट <2–3 मिनट में, इंटीग्रेशन समानांतर; PRs पर **एक छोटा UI स्मोक** चलाएं, **व्यापक UI पैक रोजाना रात में**।

---

# किसे प्राथमिकता दें (जोखिम-आधारित चेकलिस्ट)

* पैसों का लेन-देन, ऑथ, परमिशन, कंप्लायंस → **API और एक UI हैप्पी पाथ**।
* जटिल गणना, मूल्य निर्धारण नियम → **यूनिट** (कई केस) + वास्तविक DB राउंडिंग/टाइमज़ोन के साथ **कुछ इंटीग्रेशन**।
* पर्सिस्टेंस लॉजिक, माइग्रेशन, ट्रिकी जॉइन → **Testcontainers के साथ रेपो टेस्ट**।
* क्रॉस-टीम कॉन्ट्रैक्ट → CI में **कॉन्ट्रैक्ट टेस्ट** ब्रेकिंग चेंजेज को ब्लॉक करने के लिए।
* एक्सेसिबिलिटी, i18n → ARIA/लोकेल के लिए **कंपोनेंट टेस्ट** + मुख्य पेजों पर **आवधिक UI स्कैन** (axe)।

---

# CI पाइपलाइन आकार (व्यावहारिक)

* **हर पुश पर:** यूनिट + स्लाइस टेस्ट; मुट्ठी भर API E2E; छोटा UI स्मोक (1–3)।
* **रोजाना रात में:** पूर्ण API E2E, व्यापक UI पैक, परफॉर्मेंस स्मोक (k6), बेसिक सिक्योरिटी स्कैन (ZAP)।
* **फ्लैकी टेस्ट को तुरंत क्वारंटाइन** करें; ठीक करें या हटाएं—नज़रअंदाज़ न करें।

---

# टेस्ट डेटा और फ्लैकीनेस टिप्स

* **फैक्टरी मेथड/बिल्डर** का उपयोग करें; साझा म्यूटेबल फिक्स्चर से बचें।
* **Testcontainers को स्टार्टअप पर SQL/डेटा से सीड** करें; टेस्ट को **निश्चल (idempotent)** रखें।
* UI में, CSS/XPath पर **रोल/लेबल सेलेक्टर** को प्राथमिकता दें; स्लीप से बचें, यूजर-विजिबल कंडीशन से जुड़े वेट का उपयोग करें।
* CI फेल्योर को डीबग करने के लिए **ट्रेस रिकॉर्ड** करें (Playwright ट्रेस, Selenium लॉग)।

---

# संक्षेप में: अनुमान के नियम

* यदि कोई बग किसी **तेज** परत द्वारा पकड़ा जा सकता था, तो **टेस्ट को नीचे की परत पर ले जाएं**।
* केवल **कुछ, महत्वपूर्ण** UI जर्नी रखें।
* इंटीग्रेशन को सार्थक बनाने के लिए **Testcontainers** का उपयोग करें।
* **Playwright** को प्राथमिकता दें, जब तक कि Selenium एक कठिन आवश्यकता न हो।

यदि आप चाहें, तो मुझे अपने **शीर्ष 3–5 व्यावसायिक-महत्वपूर्ण फ़्लो** बताएं और मैं प्रति परत सटीक टेस्ट सूची (टूल चुनाव और CI गेटिंग के साथ) का रूपरेखा तैयार कर दूंगा।