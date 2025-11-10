---
audio: false
generated: true
image: false
lang: hi
layout: post
title: लॉगिंग के लिए जावा अनुरोध रैपर
translated: true
type: note
---

Java वेब एप्लिकेशन में, आप आमतौर पर **`HttpServletRequestWrapper`** का उपयोग तब करते हैं जब आप सर्वलेट कंटेनर के इम्प्लीमेंटेशन को छुए बिना स्टैंडर्ड `HttpServletRequest` के व्यवहार को डेकोरेट या मॉडिफ़ाई करना चाहते हैं।

### `HttpServletRequestWrapper` कैसे काम करता है

* यह मूल `HttpServletRequest` के चारों ओर एक **डेकोरेटर** है।
* आप `HttpServletRequestWrapper` का सबक्लास बनाते हैं और `getInputStream()`, `getReader()`, या `getParameter()` जैसी मेथड्स को ओवरराइड करते हैं।
* यह तब उपयोगी होता है जब आप **रिक्वेस्ट बॉडी को पढ़ना या कैश करना** चाहते हैं (जिसे डिफ़ॉल्ट रूप से केवल एक बार पढ़ा जा सकता है) या रिक्वेस्ट पैरामीटर्स को मॉडिफ़ाई/क्वेरी करना चाहते हैं।

### लॉगिंग के लिए इसकी आवश्यकता क्यों है

* डिफ़ॉल्ट रूप से, सर्वलेट रिक्वेस्ट बॉडी (`InputStream`) को केवल एक बार कंज़्यूम किया जा सकता है। यदि आप इसे सीधे एक फ़िल्टर में लॉग करते हैं, तो कंट्रोलर इसे बाद में नहीं पढ़ पाएगा।
* रैपिंग आपको **बॉडी को कैश करने** की अनुमति देती है ताकि इसे कई बार पढ़ा जा सके: एक बार लॉगिंग के लिए, एक बार डाउनस्ट्रीम प्रोसेसिंग के लिए।
* URL पैरामीटर्स को `request.getParameterMap()` या `request.getQueryString()` तक पहुंचकर लॉग किया जा सकता है।

---

### उदाहरण: बॉडी और URL पैरामीटर्स को लॉग करना

यहाँ एक कस्टम रैपर का उपयोग करते हुए एक फ़िल्टर है:

```java
public class CachedBodyHttpServletRequest extends HttpServletRequestWrapper {
    private byte[] cachedBody;

    public CachedBodyHttpServletRequest(HttpServletRequest request) throws IOException {
        super(request);
        InputStream requestInputStream = request.getInputStream();
        this.cachedBody = requestInputStream.readAllBytes();
    }

    @Override
    public ServletInputStream getInputStream() {
        ByteArrayInputStream byteArrayInputStream = new ByteArrayInputStream(this.cachedBody);
        return new ServletInputStream() {
            @Override
            public int read() {
                return byteArrayInputStream.read();
            }
            @Override
            public boolean isFinished() {
                return byteArrayInputStream.available() == 0;
            }
            @Override
            public boolean isReady() {
                return true;
            }
            @Override
            public void setReadListener(ReadListener readListener) {}
        };
    }

    @Override
    public BufferedReader getReader() {
        return new BufferedReader(new InputStreamReader(this.getInputStream()));
    }

    public String getBody() {
        return new String(this.cachedBody, StandardCharsets.UTF_8);
    }
}
```

फिर इसे एक फ़िल्टर में उपयोग करें:

```java
@WebFilter("/*")
public class LoggingFilter implements Filter {
    @Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)
            throws IOException, ServletException {

        CachedBodyHttpServletRequest wrappedRequest = new CachedBodyHttpServletRequest((HttpServletRequest) request);

        // URL लॉग करें
        String url = wrappedRequest.getRequestURL().toString();
        String query = wrappedRequest.getQueryString();

        // पैरामीटर्स लॉग करें
        Map<String, String[]> params = wrappedRequest.getParameterMap();

        // बॉडी लॉग करें
        String body = wrappedRequest.getBody();

        System.out.println("Request URL: " + url + (query != null ? "?" + query : ""));
        System.out.println("Parameters: " + params);
        System.out.println("Body: " + body);

        // फ़िल्टर चेन जारी रखें
        chain.doFilter(wrappedRequest, response);
    }
}
```

---

### मुख्य बिंदु

* **`HttpServletRequestWrapper`** आपको बॉडी को सुरक्षित रूप से कई बार पढ़ने देता है।
* URL पैरामीटर्स के लिए: `getParameterMap()` या `getQueryString()` पर्याप्त है।
* **बड़ी बॉडी** के साथ सावधान रहें (आप स्ट्रीमिंग या साइज़ लिमिट चाह सकते हैं)।
* प्रोडक्शन में, `System.out` के बजाय एक लॉगिंग फ़्रेमवर्क (SLF4J + Logback/Log4J2) का उपयोग करें।

---

क्या आप चाहते हैं कि मैं आपको एक **Spring Boot–स्टाइल सॉल्यूशन** ( `OncePerRequestFilter` और `ContentCachingRequestWrapper` का उपयोग करके) भी दिखाऊं, क्योंकि वह बहुत सरल है?