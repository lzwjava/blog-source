---
audio: false
generated: true
lang: hi
layout: post
title: इंटेलीजे संरचनात्मक प्रतिस्थापन टेम्पलेट्स
translated: true
type: note
---

यहाँ स्पष्टता के लिए श्रेणीबद्ध IntelliJ के 10 स्ट्रक्चरल रिप्लेसमेंट टेम्पलेट के उदाहरण हैं। ये रीफैक्टरिंग, कोडिंग मानकों को लागू करने और सामान्य कोड परिवर्तनों को स्वचालित करने के लिए अविश्वसनीय रूप से शक्तिशाली हो सकते हैं।

**बेसिक रीफैक्टरिंग और सरलीकरण:**

1.  **`if (condition) return true; else return false;` को `return condition;` से बदलें**

      * **सर्च टेम्पलेट:**
        ```java
        if ($CONDITION$) {
            return true;
        } else {
            return false;
        }
        ```
      * **रिप्लेसमेंट टेम्पलेट:**
        ```java
        return $CONDITION$;
        ```
      * **संदर्भ:** बूलियन रिटर्न स्टेटमेंट्स को सरल बनाता है।

2.  **`if (condition) { statement; }` को `if (!condition) { continue/break/return; }` से बदलें (गार्ड क्लॉज)**

      * **सर्च टेम्पलेट:**
        ```java
        if ($CONDITION$) {
            $STATEMENTS$;
        }
        ```
      * **रिप्लेसमेंट टेम्पलेट:** (यह एक परिवर्तन का सुझाव देने के बारे में अधिक है, आप आंतरिक भाग को मैन्युअल रूप से समायोजित करेंगे)
        ```java
        if (!$CONDITION$) {
            // यहाँ continue, break, या return पर विचार करें
        }
        $STATEMENTS$;
        ```
      * **संदर्भ:** साफ़र कोड फ्लो के लिए गार्ड क्लॉज के उपयोग को प्रोत्साहित करता है। आमतौर पर आप संरचना ढूंढने के बाद "Replace with" एक्शन का उपयोग करेंगे।

**कलेक्शन और स्ट्रीम ऑपरेशंस:**

3.  **`for (Type item : collection) { if (item.getProperty() == value) { ... } }` को स्ट्रीम `filter` से बदलें**

      * **सर्च टेम्पलेट:**
        ```java
        for ($TYPE$ $ITEM$ : $COLLECTION$) {
            if ($ITEM$.$METHOD$($VALUE$)) {
                $STATEMENTS$;
            }
        }
        ```
      * **रिप्लेसमेंट टेम्पलेट:**
        ```java
        $COLLECTION$.stream()
            .filter($ITEM$ -> $ITEM$.$METHOD$($VALUE$))
            .forEach($ITEM$ -> $STATEMENTS$); // या .map().collect(), आदि।
        ```
      * **संदर्भ:** फिल्टरिंग के लिए पारंपरिक लूप्स से Java स्ट्रीम्स में माइग्रेट करना। यह एक सामान्य उदाहरण है; आपको `map`, `collect`, आदि के लिए संभवतः अधिक विशिष्ट टेम्पलेट्स की आवश्यकता होगी।

4.  **`new ArrayList<>().add(item1); new ArrayList<>().add(item2);` को `List.of(item1, item2);` से बदलें**

      * **सर्च टेम्पलेट:** (इसके लिए `add` कॉल्स की अलग-अलग संख्या के लिए कई टेम्पलेट्स की आवश्यकता हो सकती है, या `add` कॉल्स के लिए अधिक जटिल रेगेक्स। 2 आइटम्स के लिए एक सरल तरीका):
        ```java
        java.util.ArrayList<$TYPE$> $LIST$ = new java.util.ArrayList<>();
        $LIST$.add($ITEM1$);
        $LIST$.add($ITEM2$);
        ```
      * **रिप्लेसमेंट टेम्पलेट:**
        ```java
        java.util.List<$TYPE$> $LIST$ = java.util.List.of($ITEM1$, $ITEM2$);
        ```
      * **संदर्भ:** इम्यूटेबल लिस्ट्स के लिए Java 9+ `List.of()` का उपयोग करना।

**एरर हैंडलिंग और रिसोर्स मैनेजमेंट:**

5.  **`try { ... } catch (Exception e) { e.printStackTrace(); }` को अधिक विशिष्ट लॉगिंग से बदलें**

      * **सर्च टेम्पलेट:**
        ```java
        try {
            $STATEMENTS$;
        } catch (java.lang.Exception $EXCEPTION$) {
            $EXCEPTION$.printStackTrace();
        }
        ```
      * **रिप्लेसमेंट टेम्पलेट:**
        ```java
        try {
            $STATEMENTS$;
        } catch (java.lang.Exception $EXCEPTION$) {
            // अपने पसंदीदा लॉगिंग फ्रेमवर्क से बदलें, उदाहरण के लिए:
            // logger.error("An error occurred", $EXCEPTION$);
            throw new RuntimeException($EXCEPTION$); // या किसी विशिष्ट एक्सेप्शन को दोबारा throw करें
        }
        ```
      * **संदर्भ:** सिर्फ स्टैक ट्रेस प्रिंट करने के बजाय उचित एरर लॉगिंग को प्रोत्साहित करता है।

6.  **`try { ... } finally { closeable.close(); }` को `try-with-resources` से बदलें**

      * **सर्च टेम्पलेट:**
        ```java
        java.io.Closeable $CLOSEABLE$ = null;
        try {
            $CLOSEABLE$ = $INITIALIZATION$;
            $STATEMENTS$;
        } finally {
            if ($CLOSEABLE$ != null) {
                $CLOSEABLE$.close();
            }
        }
        ```
      * **रिप्लेसमेंट टेम्पलेट:**
        ```java
        try ($CLOSEABLE$ = $INITIALIZATION$) {
            $STATEMENTS$;
        }
        ```
      * **संदर्भ:** रिसोर्स मैनेजमेंट को आधुनिक बनाने के लिए `try-with-resources` (Java 7+) का उपयोग करना।

**क्लास और मेथड स्ट्रक्चर:**

7.  **ऐसे फील्ड्स ढूंढें जिन्हें `final` बनाया जा सकता है**

      * **सर्च टेम्पलेट:**
        ```java
        class $CLASS$ {
            $TYPE$ $FIELD$;
        }
        ```
      * **रिप्लेसमेंट टेम्पलेट:** (यह ढूंढने के लिए अधिक है, फिर क्विक फिक्स का उपयोग करने के लिए)
        ```java
        class $CLASS$ {
            // इस फील्ड को final बनाने पर विचार करें यदि यह केवल एक बार असाइन होती है
            final $TYPE$ $FIELD$;
        }
        ```
      * **संदर्भ:** इम्यूटेबिलिटी में सुधार के अवसरों की पहचान करना। आप मल्टीपल असाइनमेंट वाले फील्ड्स को न दिखाने के लिए एक फिल्टर सेट करेंगे।

8.  **`private static final Logger logger = LoggerFactory.getLogger(MyClass.class);` को कस्टम लॉगर यूटिलिटी से बदलें**

      * **सर्च टेम्पलेट:**
        ```java
        private static final org.slf4j.Logger $LOGGER_VAR$ = org.slf4j.LoggerFactory.getLogger($CLASS_NAME$.class);
        ```
      * **रिप्लेसमेंट टेम्पलेट:**
        ```java
        private static final org.slf4j.Logger $LOGGER_VAR$ = com.yourcompany.util.LoggerProvider.getLogger(); // या आपकी यूटिलिटी से अधिक विशिष्ट getLogger($CLASS_NAME$.class)
        ```
      * **संदर्भ:** आपके कोडबेस में एक विशिष्ट लॉगिंग इनिशियलाइज़ेशन पैटर्न को लागू करना।

**एनोटेशन्स और बॉयलरप्लेट:**

9.  **सुपरक्लास मेथड्स को ओवरराइड करने वाली मेथड्स में `@Override` जोड़ें (यदि गायब है)**

      * **सर्च टेम्पलेट:** (यह अधिक जटिल है और अक्सर IntelliJ के बिल्ट-इन इंस्पेक्शन द्वारा बेहतर तरीके से संभाला जाता है, लेकिन प्रदर्शन के लिए)
        ```java
        class $CLASS$ {
            $RETURN_TYPE$ $METHOD$($PARAMS$) {
                $STATEMENTS$;
            }
        }
        ```
      * **रिप्लेसमेंट टेम्पलेट:** (फिर से, ढूंढने के लिए, फिर क्विक फिक्स लागू करने के लिए)
        ```java
        class $CLASS$ {
            @Override // जोड़ें यदि यह सुपरक्लास मेथड को ओवरराइड करती है
            $RETURN_TYPE$ $METHOD$($PARAMS$) {
                $STATEMENTS$;
            }
        }
        ```
      * **संदर्भ:** अच्छे अभ्यास को लागू करना और टाइपोस को पकड़ना। आप यह जांचने के लिए एक फिल्टर का उपयोग करेंगे कि क्या मेथड सुपरक्लास/इंटरफेस में मौजूद है।

10. **दोहराव वाली `getter/setter` मेथड्स को Lombok एनोटेशन्स से बदलें**

      * **सर्च टेम्पलेट:** (एक सिंगल गेटर के लिए, यह एक क्लास के लिए अत्यधिक दोहराव वाला होगा)
        ```java
        public $TYPE$ get$PROPERTY_NAME$() {
            return this.$FIELD_NAME$;
        }
        ```
      * **रिप्लेसमेंट टेम्पलेट:** (यह वैचारिक है, क्योंकि आप गेटर को डिलीट करेंगे और फील्ड या क्लास पर `@Getter` जोड़ेंगे)
        ```java
        // फील्ड पर @lombok.Getter से बदलने पर विचार करें:
        // @lombok.Getter
        // private $TYPE$ $FIELD_NAME$;
        ```
      * **संदर्भ:** Lombok में ट्रांज़िशन को स्वचालित करना। एक पूरी क्लास के लिए, आप क्लास को ही टारगेट कर सकते हैं और इन मेथड्स की उपस्थिति के आधार पर `@Data` या `@Getter/@Setter` एनोटेशन्स का सुझाव दे सकते हैं। यह अधिक उन्नत और संभावित रूप से मल्टी-स्टेप परिवर्तनों में से एक है।

**IntelliJ में इनका उपयोग कैसे करें:**

1.  `Analyze` -> `Inspect Code...` पर जाएं।
2.  `Inspection Profile` विंडो में, प्रोफाइल नाम के आगे `...` पर क्लिक करके उसे एडिट करें।
3.  `Java` -> `General` -> `Structural Search Inspection` पर नेविगेट करें।
4.  नया सर्च/रिप्लेस टेम्पलेट जोड़ने के लिए `+` बटन पर क्लिक करें।
5.  अपना `Search Template` और `Replacement Template` डिफाइन करें।
6.  अपने वेरिएबल्स के लिए कंस्ट्रेंट्स (जैसे, टाइप, टेक्स्ट, काउंट) डिफाइन करने के लिए `Variables` टैब का उपयोग करें।
7.  अपने कोड पर इंस्पेक्शन चलाएं। IntelliJ रिप्लेसमेंट्स का सुझाव देगा या फाइंडिंग्स को हाइलाइट करेगा।

ये उदाहरण स्ट्रक्चरल सर्च एंड रिप्लेस की बहुमुखी प्रतिभा को प्रदर्शित करते हैं। आपके टेम्पलेट्स जितने अधिक विशिष्ट और कंस्ट्रेंड होंगे, रिप्लेसमेंट उतने ही सटीक और उपयोगी होंगे।