---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: ईक्लिप्स के साथ वेबस्फीयर विकास
translated: true
type: note
---

### Eclipse में IBM WebSphere Application Server (WAS) के साथ विकास

IBM WebSphere Application Server (WAS) एक Java EE एप्लिकेशन सर्वर है, और Eclipse इस पर एप्लिकेशन विकसित करने, असेंबल करने और डिप्लॉय करने के लिए एक उत्कृष्ट IDE के रूप में कार्य करता है। इस एकीकरण के लिए प्राथमिक टूल **IBM WebSphere Application Server Developer Tools for Eclipse** (जिसे अक्सर WDT संक्षिप्त किया जाता है) है। यह प्लगइन Eclipse के भीतर ही सर्वर प्रबंधन, प्रोजेक्ट निर्माण, डिप्लॉयमेंट और डीबगिंग क्षमताएं प्रदान करता है। यह पारंपरिक WAS (जैसे, v8.5 और v9.x) और हल्के वजन वाले Liberty प्रोफाइल दोनों को सपोर्ट करता है।

#### आवश्यक प्लगइन
- **IBM WebSphere Application Server Developer Tools for Eclipse**: यह आवश्यक प्लगइन है। अपने WAS रनटाइम (जैसे, V8.5x या V9.x टूल्स) से मेल खाता संस्करण चुनें। यह Eclipse Marketplace पर निःशुल्क उपलब्ध है और हाल के Eclipse रिलीज़ जैसे 2024-06 या 2025-03 को सपोर्ट करता है।

कोई अन्य प्लगइन सख्ती से आवश्यक नहीं है, लेकिन पूर्ण Java EE विकास के लिए, सुनिश्चित करें कि आपकी Eclipse इंस्टॉलेशन में Web Tools Platform (WTP) शामिल है, जो Eclipse IDE for Java EE Developers पैकेज में मानक है।

#### पूर्वापेक्षाएँ
- Eclipse IDE for Java EE Developers (संगतता के लिए संस्करण 2023-09 या बाद वाला अनुशंसित)।
- परीक्षण और डिप्लॉयमेंट के लिए IBM WAS रनटाइम स्थानीय रूप से इंस्टॉल किया गया (पारंपरिक या Liberty)।
- Marketplace इंस्टॉलेशन के लिए इंटरनेट एक्सेस (या ऑफ़लाइन फ़ाइलें डाउनलोड करें)।

#### इंस्टॉलेशन चरण
आप WDT को Eclipse Marketplace (सबसे आसान तरीका), अपडेट साइट, या डाउनलोड की गई फ़ाइलों के माध्यम से इंस्टॉल कर सकते हैं। इंस्टॉलेशन के बाद Eclipse को पुनरारंभ करें।

1. **Eclipse Marketplace के माध्यम से** (अनुशंसित):
   - Eclipse खोलें और **Help > Eclipse Marketplace** पर जाएं।
   - "IBM WebSphere Application Server Developer Tools" खोजें।
   - उपयुक्त संस्करण चुनें (जैसे, V9.x या V8.5x के लिए)।
   - **Install** पर क्लिक करें और संकेतों का पालन करें। लाइसेंस स्वीकार करें और हो जाने पर Eclipse को पुनरारंभ करें।

2. **अपडेट साइट के माध्यम से**:
   - **Help > Install New Software** पर जाएं।
   - **Add** पर क्लिक करें और अपडेट साइट URL दर्ज करें (जैसे, `https://public.dhe.ibm.com/ibmdl/export/pub/software/websphere/wasdev/updates/wdt/2025-03_comp/` हाल के संस्करणों के लिए—नवीनतम के लिए IBM डॉक्स देखें)।
   - WDT फीचर्स चुनें (जैसे, WebSphere Application Server V9.x Developer Tools) और इंस्टॉल करें।

3. **डाउनलोड की गई फ़ाइलों से** (ऑफ़लाइन विकल्प):
   - [IBM Developer साइट](https://www.ibm.com/docs/en/wasdtfe?topic=installing-websphere-developer-tools) से ZIP आर्काइव डाउनलोड करें (जैसे, `wdt-update-site_<version>.zip`)।
   - एक स्थानीय फ़ोल्डर में निकालें।
   - Eclipse में, **Help > Install New Software > Add > Archive** पर जाएं और निकाले गए साइट का `site.xml` चुनें।
   - वांछित फीचर्स चुनें और इंस्टॉल करें, फिर पुनरारंभ करें।

इंस्टॉलेशन के बाद, **Window > Show View > Servers** जांचकर सत्यापित करें—WAS एक सर्वर प्रकार विकल्प के रूप में दिखाई देना चाहिए।

#### WAS एप्लिकेशन विकसित करने और डिप्लॉय करने के मूल चरण
एक बार इंस्टॉल हो जाने पर, आप WAS को लक्षित करने वाले Java EE एप्लिकेशन बना, बिल्ड और रन कर सकते हैं।

1. **एक नया प्रोजेक्ट बनाएँ**:
   - **File > New > Project** पर जाएं।
   - **Web > Dynamic Web Project** (वेब ऐप्स के लिए) या **Java EE > Enterprise Application Project** (पूर्ण EARs के लिए) चुनें।
   - प्रोजेक्ट विज़ार्ड में, टार्गेट रनटाइम को अपने स्थानीय WAS इंस्टॉलेशन पर सेट करें (यदि सूचीबद्ध नहीं है, तो **Window > Preferences > Server > Runtime Environments > Add > WebSphere** के माध्यम से इसे जोड़ें)।
   - अपने WAS से मेल खाते Java EE संस्करण (जैसे, 7 या 8) के लिए फ़ैसेट्स कॉन्फ़िगर करें।

2. **सर्वर सेट अप करें**:
   - **Servers** व्यू खोलें (**Window > Show View > Servers**)।
   - व्यू में राइट-क्लिक करें और **New > Server** चुनें।
   - **WebSphere Application Server** (पारंपरिक या Liberty) चुनें और अपने स्थानीय WAS इंस्टॉलेशन डायरेक्टरी की ओर इशारा करें।
   - समाप्त करें और सर्वर शुरू करें (राइट-क्लिक > Start)।

3. **अपना एप्लिकेशन विकसित करें**:
   - अपने प्रोजेक्ट में Java क्लासेस, JSPs, servlets, EJBs, आदि जोड़ें।
   - XML कॉन्फ़िग्स (जैसे, web.xml, ibm-web-bnd.xml WAS-विशिष्ट बाइंडिंग्स के लिए) के लिए Eclipse के एडिटर्स का उपयोग करें।
   - प्रोजेक्ट बिल्ड करें (**Project > Build Project**)।

4. **डिप्लॉय और रन करें**:
   - अपने प्रोजेक्ट पर राइट-क्लिक करें > **Run As > Run on Server** (अपना WAS सर्वर चुनें)।
   - Eclipse ऐप को प्रकाशित करता है (डेव मोड के लिए ऑटो-पब्लिश) और सर्वर शुरू करता है।
   - ब्रेकपॉइंट्स सेट करके और Debug मोड में चलाकर डीबग करें।
   - हॉट डिप्लॉयमेंट (रीस्टार्ट के बिना त्वरित अपडेट) के लिए, सर्वर कॉन्फ़िग में "Publish server changes immediately" सक्षम करें।

5. **उन्नत सुझाव**:
   - त्वरित स्थानीय परीक्षण के लिए Liberty प्रोफाइल का उपयोग करें—यह WDT में शामिल है और पारंपरिक WAS व्यवहार की नकल करता है।
   - OSGi या माइक्रोसर्विसेज के लिए, प्लगइन के माध्यम से OSGi Bundle Projects बनाएं।
   - रनटाइम के दौरान **Console** व्यू में लॉग्स की निगरानी करें।

यदि आपको कोई समस्या आती है (जैसे, संगतता त्रुटियाँ), IBM का ज्ञात समस्याओं वाला पृष्ठ जांचें या सुनिश्चित करें कि आपके Eclipse और WAS संस्करण मेल खाते हों।

#### संदर्भ
- [IBM WebSphere Application Server Developer Tools अवलोकन](https://www.ibm.com/docs/en/wasdtfe?topic=websphere-developer-tools-overview)
- [Eclipse Marketplace: V9.x टूल्स](https://marketplace.eclipse.org/content/ibm-websphere-application-server-v9x-developer-tools)
- [Eclipse Marketplace: V8.5x टूल्स](https://marketplace.eclipse.org/content/ibm-websphere-application-server-v85x-developer-tools)
- [IBM डॉक्स से इंस्टॉलेशन गाइड](https://www.ibm.com/docs/en/wasdtfe?topic=installing-websphere-developer-tools)