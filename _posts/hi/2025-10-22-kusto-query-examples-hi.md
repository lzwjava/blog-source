---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: उन्नत कुस्टो क्वेरी भाषा उदाहरण
translated: true
type: note
---

कुस्तो क्वेरी लैंग्वेज (KQL) Azure डेटा एक्सप्लोरर और Azure मॉनिटर जैसी Azure सेवाओं में बड़े डेटासेट को क्वेरी करने के लिए एक शक्तिशाली टूल है। नीचे कई जटिल उदाहरण दिए गए हैं जो टाइम-सीरीज़ विश्लेषण, एनोमली डिटेक्शन, पिवटिंग, और यूजर-डिफाइंड फ़ंक्शन जैसी उन्नत सुविधाओं के साथ कई ऑपरेटरों और फ़ंक्शन को जोड़ते हैं। ये स्टॉर्म इवेंट्स या सेल्स डेटा के विश्लेषण जैसे वास्तविक दुनिया के परिदृश्यों से लिए गए हैं। प्रत्येक में क्वेरी और एक संक्षिप्त व्याख्या शामिल है।

### 1. टाइम-सीरीज़ डेटा में एनोमली डिटेक्शन
यह क्वेरी मेट्रिक्स टेबल से दैनिक औसत एकत्रित करती है और लॉग्स या टेलीमेट्री में असामान्य पैटर्न की निगरानी के लिए आदर्श, एनोमली की पहचान करने के लिए सीरीज़ डिकम्पोज़िशन का उपयोग करती है।

```
TableName
| make-series Metric = avg(Value) on Timestamp step 1d
| extend Anomalies = series_decompose_anomalies(Metric)
```

### 2. पैरामीटराइज्ड फ़िल्टरिंग और सारांशीकरण के लिए यूजर-डिफाइंड फ़ंक्शन
यहाँ, एक पुन: प्रयोज्य फ़ंक्शन क्षेत्र और थ्रेशोल्ड द्वारा सेल्स डेटा को फ़िल्टर करता है, फिर कुल योग की गणना करता है—Azure डेटा एक्सप्लोरर डैशबोर्ड में डायनामिक रिपोर्टिंग के लिए उपयोगी।

```
let CalculateSales = (region: string, minSales: int) {
    SalesData
    | where Region == region and Sales > minSales
    | summarize TotalSales = sum(Sales)
};
CalculateSales("North America", 1000)
```

### 3. क्रॉस-टैब्युलर विश्लेषण के लिए एकत्रित डेटा को पिवट करना
यह श्रेणी और क्षेत्र द्वारा मूल्यों का सारांश तैयार करता है, फिर आसान तुलना के लिए क्षेत्रों को कॉलम में बदल देता है, जो व्यावसायिक बुद्धिमत्ता क्वेरीज़ में आम है।

```
TableName
| summarize Total = sum(Value) by Category, Region
| evaluate pivot(Region, sum(Total))
```

### 4. टाइम-सीरीज़ मेट्रिक्स के बीच सहसंबंध विश्लेषण
स्टॉर्म इवेंट्स डेटा का उपयोग करते हुए, यह दो मेट्रिक्स के लिए दैनिक श्रृंखला बनाता है और क्षति और मौतों के बीच संबंधों को उजागर करने के लिए उनके सहसंबंध की गणना करता है।

```
StormEvents
| make-series PropertyDamage = avg(DamageProperty), Fatalities = avg(Fatalities) on BeginTime step 1d
| extend Correlation = series_correlation(PropertyDamage, Fatalities)
```

### 5. इवेंट विश्लेषण के लिए फ़िल्टरिंग, शीर्ष चयन और अवधि गणना
यह टेक्सास की बाढ़ की घटनाओं को फ़िल्टर करता है, क्षति के आधार पर शीर्ष 5 का चयन करता है, और एक गणना की गई अवधि कॉलम जोड़ता है—Azure सेंटिनल में घटना प्रतिक्रिया के लिए बहुत अच्छा।

```
StormEvents
| where State == 'TEXAS' and EventType == 'Flood'
| top 5 by DamageProperty
| project StartTime, EndTime, Duration = EndTime - StartTime, DamageProperty
```

### 6. डेटा ट्रांसफॉर्मेशन के लिए लेट स्टेटमेंट के साथ स्थिर मान मैपिंग
स्रोत प्रकारों को मैप करने के लिए एक शब्दकोश को परिभाषित करता है, घटनाओं को फ़िल्टर करता है, और मित्रवत नाम प्रोजेक्ट करता है—लॉग्स में श्रेणीबद्ध डेटा को सामान्य बनाने में सहायक।

```
let sourceMapping = dynamic(
  {
    "Emergency Manager" : "Public",
    "Utility Company" : "Private"
  });
StormEvents
| where Source == "Emergency Manager" or Source == "Utility Company"
| project EventId, Source, FriendlyName = sourceMapping[Source]
```

इन उदाहरणों को सीधे Azure डेटा एक्सप्लोरर वेब UI या लॉग एनालिटिक्स में चलाया जा सकता है। अधिक के लिए, आधिकारिक नमूना गैलरी का अन्वेषण करें।

[कुस्तो क्वेरी लैंग्वेज (KQL) की व्यापक मार्गदर्शिका](https://medium.com/@danushidk507/comprehensive-guide-to-kusto-query-language-kql-from-beginner-to-advanced-8dff3bd7568e)  
[ट्यूटोरियल: सामान्य कुस्तो क्वेरी लैंग्वेज ऑपरेटर सीखें](https://learn.microsoft.com/en-us/kusto/query/tutorials/learn-common-operators?view=microsoft-fabric)