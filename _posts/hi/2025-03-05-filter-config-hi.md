---
audio: false
generated: true
lang: hi
layout: post
title: जावा सर्वलेट में फिल्टर कॉन्फ़िगरेशन
translated: true
type: note
---

### `javax.servlet.FilterConfig` कैसे काम करता है?

Servlet API का उपयोग करके बनाए गए Java वेब एप्लिकेशन में, `javax.servlet.FilterConfig` इंटरफेस फिल्टर को कॉन्फ़िगर करने में एक महत्वपूर्ण भूमिका निभाता है। फिल्टर ऐसे कंपोनेंट्स हैं जो HTTP अनुरोधों और प्रतिक्रियाओं को सर्वलेट तक पहुंचने से पहले या उसके बाद इंटरसेप्ट और प्रोसेस करते हैं। `FilterConfig` वेब कंटेनर (जैसे, Tomcat, Jetty) द्वारा फिल्टर को इनिशियलाइज़ करते समय कॉन्फ़िगरेशन जानकारी पास करने का एक मानकीकृत तरीका प्रदान करता है। नीचे, मैं समझाऊंगा कि `FilterConfig` कैसे काम करता है, इसका उद्देश्य क्या है, और इसका उपयोग कैसे किया जाता है।

---

#### **`FilterConfig` क्या है?**
`FilterConfig` `javax.servlet` पैकेज में एक इंटरफेस है। इसका उपयोग वेब कंटेनर द्वारा फिल्टर को उसके इनिशियलाइज़ेशन चरण के दौरान कॉन्फ़िगरेशन डेटा सप्लाई करने के लिए किया जाता है। जब एक फिल्टर को वेब एप्लिकेशन में परिभाषित किया जाता है (`web.xml` या एनोटेशन के माध्यम से), कंटेनर फिल्टर का एक इंस्टेंस बनाता है और उसके `init` मेथड में एक `FilterConfig` ऑब्जेक्ट पास करता है। यह ऑब्जेक्ट फिल्टर को एक्सेस करने की अनुमति देता है:
- इसके अपने इनिशियलाइज़ेशन पैरामीटर्स।
- वेब एप्लिकेशन का `ServletContext`।
- कॉन्फ़िगरेशन में परिभाषित इसका अपना नाम।

फिल्टर `javax.servlet.Filter` इंटरफेस को इम्प्लीमेंट करते हैं, जिसमें तीन मेथड्स शामिल हैं: `init`, `doFilter`, और `destroy`। `FilterConfig` ऑब्जेक्ट का विशेष रूप से उपयोग अनुरोधों को प्रोसेस करना शुरू करने से पहले फिल्टर को सेट अप करने के लिए `init` मेथड में किया जाता है।

---

#### **एक फिल्टर और `FilterConfig` का लाइफसाइकल**
`FilterConfig` कैसे काम करता है, यह समझने के लिए, आइए फिल्टर लाइफसाइकल में इसकी भूमिका देखें:
1.  **कंटेनर स्टार्टअप**: जब वेब एप्लिकेशन शुरू होता है, कंटेनर फिल्टर परिभाषाओं (`web.xml` या `@WebFilter` एनोटेशन से) को पढ़ता है और प्रत्येक फिल्टर का एक इंस्टेंस बनाता है।
2.  **फिल्टर इनिशियलाइज़ेशन**: प्रत्येक फिल्टर के लिए, कंटेनर `init` मेथड को कॉल करता है, एक `FilterConfig` ऑब्जेक्ट को पैरामीटर के रूप में पास करते हुए। यह फिल्टर इंस्टेंस प्रति एक-बार का ऑपरेशन है।
3.  **अनुरोध प्रोसेसिंग**: इनिशियलाइज़ेशन के बाद, फिल्टर की `doFilter` मेथड को प्रत्येक मिलान वाले अनुरोध के लिए कॉल किया जाता है। हालांकि `FilterConfig` को `doFilter` में पास नहीं किया जाता है, फिल्टर `init` के दौरान `FilterConfig` से कॉन्फ़िगरेशन डेटा को इंस्टेंस वेरिएबल्स में स्टोर कर सकता है ताकि बाद में उपयोग किया जा सके।
4.  **फिल्टर शटडाउन**: जब एप्लिकेशन शट डाउन होता है, तो `destroy` मेथड को कॉल किया जाता है, लेकिन `FilterConfig` यहां शामिल नहीं होता है।

`FilterConfig` ऑब्जेक्ट इनिशियलाइज़ेशन चरण के दौरान महत्वपूर्ण है, जो फिल्टर को अनुरोध प्रोसेसिंग के लिए खुद को तैयार करने में सक्षम बनाता है।

---

#### **`FilterConfig` की प्रमुख विधियाँ**
`FilterConfig` इंटरफेस चार विधियों को परिभाषित करता है जो कॉन्फ़िगरेशन जानकारी तक पहुंच प्रदान करती हैं:

1.  **`String getFilterName()`**
    - `web.xml` फ़ाइल ( `<filter-name>` के तहत) या `@WebFilter` एनोटेशन में निर्दिष्ट फिल्टर का नाम लौटाता है।
    - यह लॉगिंग, डिबगिंग, या फिल्टर की एक श्रृंखला में फिल्टर की पहचान करने के लिए उपयोगी है।

2.  **`ServletContext getServletContext()`**
    - `ServletContext` ऑब्जेक्ट लौटाता है, जो संपूर्ण वेब एप्लिकेशन का प्रतिनिधित्व करता है।
    - `ServletContext` फिल्टर को एप्लिकेशन-वाइड रिसोर्सेज तक पहुंचने की अनुमति देता है, जैसे कि कॉन्टेक्स्ट एट्रिब्यूट्स, लॉगिंग फैसिलिटीज, या अनुरोधों को फॉरवर्ड करने के लिए एक `RequestDispatcher`।

3.  **`String getInitParameter(String name)`**
    - किसी विशिष्ट इनिशियलाइज़ेशन पैरामीटर का उसके नाम से मान प्राप्त करता है।
    - इनिशियलाइज़ेशन पैरामीटर की-वैल्यू पेयर होते हैं जो फिल्टर के लिए `web.xml` ( `<init-param>` के तहत) या `@WebFilter` एनोटेशन के `initParams` एट्रिब्यूट में परिभाषित होते हैं।
    - यदि पैरामीटर मौजूद नहीं है तो `null` लौटाता है।

4.  **`Enumeration<String> getInitParameterNames()`**
    - फिल्टर के लिए परिभाषित सभी इनिशियलाइज़ेशन पैरामीटर नामों का एक `Enumeration` लौटाता है।
    - यह फिल्टर को उसके सभी पैरामीटर्स पर इटरेट करने और `getInitParameter` का उपयोग करके उनके मान प्राप्त करने की अनुमति देता है।

इन विधियों को वेब कंटेनर (जैसे, Tomcat की आंतरिक `FilterConfigImpl`) द्वारा प्रदान किए गए एक कंक्रीट क्लास द्वारा इम्प्लीमेंट किया जाता है। एक डेवलपर के रूप में, आप `FilterConfig` के साथ सिर्फ इस इंटरफेस के माध्यम से इंटरैक्ट करते हैं।

---

#### **`FilterConfig` कैसे कॉन्फ़िगर किया जाता है**
फिल्टर और उनकी कॉन्फ़िगरेशन को दो तरीकों से परिभाषित किया जा सकता है:
1.  **`web.xml` (Deployment Descriptor) का उपयोग करना**:
    ```xml
    <filter>
        <filter-name>MyFilter</filter-name>
        <filter-class>com.example.MyFilter</filter-class>
        <init-param>
            <param-name>excludeURLs</param-name>
            <param-value>/login,/signup</param-value>
        </init-param>
    </filter>
    <filter-mapping>
        <filter-name>MyFilter</filter-name>
        <url-pattern>/*</url-pattern>
    </filter-mapping>
    ```
    - `<filter-name>` फिल्टर का नाम परिभाषित करता है।
    - `<init-param>` की-वैल्यू पेयर के रूप में इनिशियलाइज़ेशन पैरामीटर्स को निर्दिष्ट करता है।

2.  **एनोटेशन का उपयोग करना (Servlet 3.0 और बाद में)**:
    ```java
    import javax.servlet.annotation.WebFilter;
    import javax.servlet.annotation.WebInitParam;

    @WebFilter(
        filterName = "MyFilter",
        urlPatterns = "/*",
        initParams = @WebInitParam(name = "excludeURLs", value = "/login,/signup")
    )
    public class MyFilter implements Filter {
        // Implementation
    }
    ```
    - `@WebFilter` एनोटेशन फिल्टर का नाम, URL पैटर्न और इनिशियलाइज़ेशन पैरामीटर्स को परिभाषित करता है।

दोनों ही मामलों में, कंटेनर इस कॉन्फ़िगरेशन का उपयोग एक `FilterConfig` ऑब्जेक्ट बनाने और इसे फिल्टर की `init` मेथड में पास करने के लिए करता है।

---

#### **प्रैक्टिकल उदाहरण**
यहां बताया गया है कि एक फिल्टर व्यवहार में `FilterConfig` का उपयोग कैसे कर सकता है:

```java
import javax.servlet.*;
import java.io.IOException;

public class MyFilter implements Filter {
    private String excludeURLs; // कॉन्फ़िग डेटा स्टोर करने के लिए इंस्टेंस वेरिएबल

    @Override
    public void init(FilterConfig filterConfig) throws ServletException {
        // फिल्टर का नाम प्राप्त करें
        String filterName = filterConfig.getFilterName();
        System.out.println("Initializing filter: " + filterName);

        // एक इनिशियलाइज़ेशन पैरामीटर प्राप्त करें
        excludeURLs = filterConfig.getInitParameter("excludeURLs");
        if (excludeURLs != null) {
            System.out.println("Exclude URLs: " + excludeURLs);
        }

        // बाद में उपयोग के लिए वैकल्पिक रूप से ServletContext स्टोर करें
        ServletContext context = filterConfig.getServletContext();
        context.log("Filter " + filterName + " initialized");
    }

    @Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)
            throws IOException, ServletException {
        // अनुरोध को फिल्टर करने या न करने का निर्णय लेने के लिए excludeURLs का उपयोग करें
        chain.doFilter(request, response); // अगले फिल्टर या सर्वलेट पर आगे बढ़ें
    }

    @Override
    public void destroy() {
        // Cleanup code
    }
}
```

-   **`init` में**: फिल्टर अपना नाम, एक इनिशियलाइज़ेशन पैरामीटर (`excludeURLs`), और `ServletContext` प्राप्त करता है। यह `excludeURLs` को `doFilter` में उपयोग के लिए एक इंस्टेंस वेरिएबल में स्टोर करता है।
-   **`doFilter` में**: फिल्टर संग्रहीत कॉन्फ़िगरेशन (जैसे, `excludeURLs`) का उपयोग अनुरोधों को प्रोसेस करने के लिए कर सकता है।

---

#### **`FilterConfig` के बारे में मुख्य बिंदु**
-   **फिल्टर-विशिष्ट स्कोप**: `FilterConfig` में इनिशियलाइज़ेशन पैरामीटर फिल्टर इंस्टेंस के लिए विशिष्ट होते हैं। अलग-अलग फिल्टर में समान नाम लेकिन अलग-अलग मान वाले पैरामीटर हो सकते हैं।
-   **`ServletContext` के साथ विरोधाभास**: `ServletContext` (जिसे `getServletContext()` के माध्यम से एक्सेस किया जाता है) एप्लिकेशन-वाइड इनिशियलाइज़ेशन पैरामीटर्स और रिसोर्सेज प्रदान करता है, जो `FilterConfig` में फिल्टर-विशिष्ट पैरामीटर्स से अलग होता है।
-   **लाइफसाइकल में एकल उपयोग**: `FilterConfig` केवल `init` में पास किया जाता है। यदि फिल्टर को बाद में इसके डेटा की आवश्यकता होती है (जैसे, `doFilter` में), तो उसे डेटा को इंस्टेंस वेरिएबल्स में स्टोर करना होगा।
-   **कंटेनर-प्रदत्त**: `FilterConfig` एक इंटरफेस है, और वेब कंटेनर कंक्रीट इम्प्लीमेंटेशन प्रदान करता है।

---

#### **सारांश**
`javax.servlet.FilterConfig` फिल्टर को उसके इनिशियलाइज़ेशन के दौरान कॉन्फ़िगरेशन जानकारी प्रदान करके काम करता है। वेब कंटेनर फिल्टर की `init` मेथड में एक `FilterConfig` ऑब्जेक्ट पास करता है, जो फिल्टर को निम्न करने की अनुमति देता है:
- इसका नाम एक्सेस करें (`getFilterName`)।
- इनिशियलाइज़ेशन पैरामीटर्स प्राप्त करें (`getInitParameter`, `getInitParameterNames`)।
- `ServletContext` के माध्यम से वेब एप्लिकेशन के साथ इंटरैक्ट करें (`getServletContext`)।

यह फिल्टर को लचीले ढंग से कॉन्फ़िगर करने में सक्षम बनाता है—`web.xml` या एनोटेशन के माध्यम से—और उन्हें HTTP अनुरोधों और प्रतिक्रियाओं को प्रभावी ढंग से प्रोसेस करने के लिए तैयार करता है। चाहे आप कुछ URL को बाहर कर रहे हों, टाइमआउट सेट कर रहे हों, या संदेश लॉग कर रहे हों, `FilterConfig` फिल्टर की कॉन्फ़िगरेशन और उसके रनटाइम व्यवहार के बीच का सेतु है।