---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: आईबीएम वेबस्फीयर मुफ्त विकास विकल्प
translated: true
type: note
---

### IBM WebSphere Application Server (WAS) मुफ्त या कम्युनिटी संस्करण

IBM WebSphere Application Server (WAS), जो एक पारंपरिक पूर्ण-सुविधाओं वाला एंटरप्राइज़ एप्लिकेशन सर्वर है, अक्टूबर 2025 तक प्रोडक्शन उपयोग के लिए स्थायी रूप से मुफ्त या कम्युनिटी संस्करण प्रदान नहीं करता है। ऐतिहासिक WebSphere Application Server Community Edition (WASCE), जो एक मुफ्त Java EE 6-संगत सर्वर था, लगभग 2012 में बंद कर दिया गया था और अब IBM से समर्थित या उपलब्ध नहीं है।

हालाँकि, IBM विकास और परीक्षण के लिए **मुफ्त विकल्प** प्रदान करता है:
- **WebSphere Application Server Developer Tools**: यह Eclipse-आधारित टूल्स का एक हल्का, मुफ्त सेट है जो Java EE, OSGi, और वेब एप्लिकेशन्स को विकसित करने, असेंबल करने और डिप्लॉय करने के लिए है। इन्हें सीधे IBM से डाउनलोड किया जा सकता है और Eclipse जैसे IDE के साथ एकीकृत किया जा सकता है।
- **मुफ्त डेवलपर रनटाइम**: IBM डेवलपर्स को एप्लिकेशन्स का परीक्षण करने के लिए विशेष रूप से WAS का एक बिना लागत वाला रनटाइम संस्करण प्रदान करता है (जैसे, WebSphere 9)। यह IBM के डेवलपर संसाधनों के माध्यम से डाउनलोड के लिए उपलब्ध है और गैर-प्रोडक्शन वातावरण जैसे स्थानीय विकास या आंतरिक R&D के लिए उपयुक्त है।

प्रोडक्शन डिप्लॉयमेंट के लिए, पारंपरिक WAS के लिए एक भुगतान युक्त लाइसेंस की आवश्यकता होती है, हालाँकि IBM मूल्यांकन के लिए 60-दिन का ट्रायल प्रदान करता है।

### विकल्प: WebSphere Liberty
यदि आप WebSphere परिवार के भीतर एक आधुनिक, हल्के विकल्प के लिए खुले हैं, तो **WebSphere Liberty** अधिकांश उपयोग के मामलों के लिए IBM द्वारा अत्यधिक अनुशंसित है:
- **Liberty Core**: यह विकास और प्रोडक्शन दोनों उपयोग के लिए मुफ्त है (IBM सपोर्ट के बिना)। यह Jakarta EE सुविधाओं के एक सबसेट का समर्थन करता है और माइक्रोसर्विसेज, क्लाउड-नेटिव ऐप्स, और सरल वर्कलोड के लिए आदर्श है।
- पूर्ण Liberty संस्करण (क्लस्टरिंग या प्रीमियम सुरक्षा जैसी उन्नत सुविधाओं के साथ) के लिए प्रोडक्शन में लाइसेंसिंग की आवश्यकता होती है, लेकिन आधार संस्करण मुफ्त बना रहता है।
- Liberty ओपन-सोर्स **Open Liberty** प्रोजेक्ट से उत्पन्न हुआ है, जो पूरी तरह से मुफ्त और कम्युनिटी-चालित है।

आप गैर-वाणिज्यिक परीक्षण के लिए बिना किसी प्रतिबंध के Liberty को डेवलपर्स के लिए IBM की साइट से डाउनलोड कर सकते हैं।

नवीनतम डाउनलोड और लाइसेंसिंग विवरण के लिए, IBM की आधिकारिक पेज या Passport Advantage (एक IBM ID की आवश्यकता होती है) पर जाएँ।

**संदर्भ**:
- [WebSphere Application Server Developer Tools Releases](https://www.ibm.com/support/pages/websphere-application-server-developer-tools-and-liberty-developer-tools-releases)
- [Installing WebSphere 9 for Developers](https://www.genuitec.com/docs/servers/installing-websphere-9-developers/)
- [WebSphere Liberty for Developers](https://www.ibm.com/support/pages/websphere-liberty-developers)
- [IBM WebSphere Application Server Community Edition (Wikipedia)](https://en.wikipedia.org/wiki/IBM_WebSphere_Application_Server_Community_Edition)
- [Exploring IBM WebSphere Application Server](https://www.jrebel.com/blog/exploring-ibm-websphere-application-server)
- [Open Liberty](https://openliberty.io/)