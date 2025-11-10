---
audio: false
generated: true
image: false
lang: hi
layout: post
title: जावा सर्वलेट एपीआई गाइड एसेंशियल्स
translated: true
type: note
---

यहाँ क्लासिक **`javax.servlet.*`** नेमस्पेस (Servlet 2.x–4.x युग) में Java **Servlet** API की एक व्यावहारिक, एंड-टू-एंड गाइड दी गई है। मैं **`jakarta.servlet.*`** में स्थानांतरण के बाद क्या बदला, यह भी नोट करूँगा ताकि आप भविष्य के लिए तैयार रहें।

# 1) Servlet क्या है?

एक **Servlet** एक Java क्लास है जो एक **Servlet कंटेनर** (Tomcat, Jetty, WebSphere, WebLogic, आदि) के अंदर चलती है और HTTP अनुरोधों/प्रतिक्रियाओं को संभालती है। कंटेनर प्रबंधित करता है:

* लाइफसाइकिल (लोडिंग, init, service, destroy)
* मल्टीथ्रेडिंग और अनुरोध रूटिंग
* सत्र, सुरक्षा, संसाधन, और कॉन्फ़िगरेशन

# 2) कोर पैकेज और की इंटरफेस (javax.\*)

* `javax.servlet.Servlet`, `ServletConfig`, `ServletContext`
* `javax.servlet.http.HttpServlet`, `HttpServletRequest`, `HttpServletResponse`, `HttpSession`, `Cookie`
* `javax.servlet.Filter`, `FilterChain`, `FilterConfig`
* `javax.servlet.ServletRequestListener` और अन्य लिसनर्स
* `javax.servlet.annotation.*` (3.0 से: `@WebServlet`, `@WebFilter`, `@WebListener`, `@MultipartConfig`)
* 3.0 से: **async** (`AsyncContext`), प्रोग्रामेटिक रजिस्ट्रेशन
* 3.1 से: **नॉन-ब्लॉकिंग I/O** (`ServletInputStream`/`ServletOutputStream` के साथ `ReadListener`/`WriteListener`)
* 4.0 से: HTTP/2 सपोर्ट (जैसे, `PushBuilder`)

> जकार्ता स्विच: **Servlet 5.0** (जकार्ता EE 9) से शुरू, पैकेजों का नाम बदलकर `jakarta.servlet.*` कर दिया गया। अधिकांश API समान हैं; माइग्रेट करते समय इम्पोर्ट्स और डिपेंडेंसीज़ अपडेट करें।

# 3) Servlet लाइफसाइकिल और थ्रेडिंग मॉडल

* **लोड**: कंटेनर क्लास लोड करता है, डिक्लेरेशन प्रति एकल इंस्टेंस बनाता है।
* **`init(ServletConfig)`**: एक बार कॉल होता है। Init पैरामीटर पढ़ें, भारी संसाधन कैश करें।
* **`service(req, res)`**: प्रति अनुरोध कॉल होता है। `HttpServlet`, `doGet`, `doPost` आदि को डिस्पैच करता है।
* **`destroy()`**: शटडाउन/रीडिप्लॉय पर एक बार कॉल होता है।

**थ्रेडिंग**: कंटेनर एक ही इंस्टेंस पर `service` को समवर्ती रूप से (concurrently) कॉल करता है।
**नियम**: परिवर्तनशील (mutable) इंस्टेंस फ़ील्ड से बचें; अगर ज़रूरी हो, तो थ्रेड-सुरक्षित संरचनाएँ या उचित सिंक्रोनाइज़ेशन का उपयोग करें। लोकल वेरिएबल को प्राथमिकता दें।

# 4) मिनिमल Servlet (एनोटेशन)

```java
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.*;
import javax.servlet.ServletException;
import java.io.IOException;

@WebServlet(name = "HelloServlet", urlPatterns = "/hello")
public class HelloServlet extends HttpServlet {
  @Override protected void doGet(HttpServletRequest req, HttpServletResponse resp)
      throws ServletException, IOException {
    resp.setContentType("text/plain;charset=UTF-8");
    resp.getWriter().println("Hello, Servlet!");
  }
}
```

# 5) `web.xml` बनाम एनोटेशन

**एनोटेशन (3.0+)** सरल ऐप्स के लिए सबसे आसान हैं।
**`web.xml`** ऑर्डरिंग, ओवरराइड्स, या लीगेसी कंटेनरों के लिए अभी भी उपयोगी है।

मिनिमल `web.xml`:

```xml
<web-app xmlns="http://java.sun.com/xml/ns/javaee" version="3.0">
  <servlet>
    <servlet-name>HelloServlet</servlet-name>
    <servlet-class>com.example.HelloServlet</servlet-class>
    <init-param>
      <param-name>greeting</param-name>
      <param-value>Hi</param-value>
    </init-param>
    <load-on-startup>1</load-on-startup>
  </servlet>
  <servlet-mapping>
    <servlet-name>HelloServlet</servlet-name>
    <url-pattern>/hello</url-pattern>
  </servlet-mapping>
</web-app>
```

# 6) HTTP अनुरोध/प्रतिक्रिया के मूल तत्व

## अनुरोध डेटा पढ़ना

```java
String q = req.getParameter("q");        // क्वेरी/फॉर्म फील्ड
Enumeration<String> names = req.getParameterNames();
BufferedReader reader = req.getReader(); // रॉ बॉडी टेक्स्ट
ServletInputStream in = req.getInputStream(); // बाइनरी बॉडी
String header = req.getHeader("X-Token");
```

**टिप**: पैरामीटर पढ़ने से पहले हमेशा एन्कोडिंग सेट करें:

```java
req.setCharacterEncoding("UTF-8");
```

## प्रतिक्रियाएँ लिखना

```java
resp.setStatus(HttpServletResponse.SC_OK);
resp.setContentType("application/json;charset=UTF-8");
resp.setHeader("Cache-Control", "no-store");
try (PrintWriter out = resp.getWriter()) {
  out.write("{\"ok\":true}");
}
```

# 7) doGet बनाम doPost बनाम अन्य

* `doGet`: इडेम्पोटेंट रीड्स; क्वेरी स्ट्रिंग का उपयोग करें।
* `doPost`: फॉर्म या JSON बॉडी के साथ बनाना/अपडेट करना।
* `doPut`/`doDelete`/`doPatch`: RESTful सेमेंटिक्स (क्लाइंट को सपोर्ट करना चाहिए)।
* हमेशा इनपुट वैलिडेट करें और कंटेंट टाइप्स को स्पष्ट रूप से हैंडल करें।

# 8) सत्र और कुकीज़

```java
HttpSession session = req.getSession(); // अगर अनुपस्थित हो तो बनाता है
session.setAttribute("userId", 123L);
Long userId = (Long) session.getAttribute("userId");
session.invalidate(); // लॉगआउट
```

कंटेनर के माध्यम से या प्रोग्रामेटिक रूप से सत्र कुकी फ्लैग्स कॉन्फ़िगर करें:

* `HttpOnly` (JS से सुरक्षा), `Secure` (HTTPS), `SameSite=Lax/Strict`
  हॉरिजॉन्टल स्केलिंग के लिए स्टेटलेस टोकन पर विचार करें; नहीं तो स्टिकी सत्र या एक्सटर्नल सत्र स्टोर का उपयोग करें।

# 9) फिल्टर (क्रॉस-कटिंग कंसर्न्स)

लॉगिंग, ऑथ, CORS, कम्प्रेशन, एन्कोडिंग, आदि के लिए **फिल्टर** का उपयोग करें।

```java
import javax.servlet.*;
import javax.servlet.annotation.WebFilter;
import java.io.IOException;

@WebFilter(urlPatterns = "/*")
public class LoggingFilter implements Filter {
  public void doFilter(ServletRequest req, ServletResponse res, FilterChain chain)
      throws IOException, ServletException {
    long start = System.nanoTime();
    try {
      chain.doFilter(req, res);
    } finally {
      long ms = (System.nanoTime() - start) / 1_000_000;
      req.getServletContext().log("Handled in " + ms + " ms");
    }
  }
}
```

# 10) लिसनर्स (ऐप और अनुरोध हुक्स)

सामान्य लिसनर्स:

* `ServletContextListener`: ऐप स्टार्टअप/शटडाउन (पूल इनिट करें, कैश वार्म करें)
* `HttpSessionListener`: सत्र बनाना/नष्ट करना (मेट्रिक्स, क्लीनअप)
* `ServletRequestListener`: प्रति-अनुरोध हुक्स (ट्रेस आईडी)

उदाहरण:

```java
@WebListener
public class AppBoot implements javax.servlet.ServletContextListener {
  public void contextInitialized(javax.servlet.ServletContextEvent sce) {
    sce.getServletContext().log("App starting...");
  }
  public void contextDestroyed(javax.servlet.ServletContextEvent sce) {
    sce.getServletContext().log("App stopping...");
  }
}
```

# 11) एसिंक और नॉन-ब्लॉकिंग I/O

## एसिंक (Servlet 3.0)

बैकेंड कॉल चलते समय कंटेनर थ्रेड्स को मुक्त करने की अनुमति देता है।

```java
@WebServlet(urlPatterns="/async", asyncSupported=true)
public class AsyncDemo extends HttpServlet {
  protected void doGet(HttpServletRequest req, HttpServletResponse resp) {
    AsyncContext ctx = req.startAsync();
    ctx.start(() -> {
      try {
        // धीमी सेवा को कॉल करें...
        ctx.getResponse().getWriter().println("done");
      } catch (Exception e) {
        ctx.complete();
      } finally {
        ctx.complete();
      }
    });
  }
}
```

## नॉन-ब्लॉकिंग (Servlet 3.1)

इवेंट-ड्रिवेन I/O के लिए स्ट्रीम्स पर `ReadListener`/`WriteListener` रजिस्टर करें। थ्रेड्स को ब्लॉक किए बिना बड़ी बॉडीज़ को स्ट्रीम करने के लिए उपयोगी।

# 12) फ़ाइल अपलोड (मल्टीपार्ट)

```java
import javax.servlet.annotation.MultipartConfig;

@MultipartConfig(maxFileSize = 10 * 1024 * 1024)
@WebServlet("/upload")
public class UploadServlet extends HttpServlet {
  protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws IOException, ServletException {
    Part file = req.getPart("file");
    String filename = file.getSubmittedFileName();
    try (InputStream is = file.getInputStream()) {
      // सेव करें...
    }
    resp.getWriter().println("Uploaded " + filename);
  }
}
```

सुनिश्चित करें कि क्लाइंट `Content-Type: multipart/form-data` भेजता है।

# 13) डिस्पैचिंग और टेम्प्लेटिंग

* **फॉरवर्ड**: सर्वर-साइड आंतरिक डिस्पैच; मूल URL रहता है।

  ```java
  req.getRequestDispatcher("/WEB-INF/view.jsp").forward(req, resp);
  ```
* **इंक्लूड**: किसी अन्य संसाधन का आउटपुट शामिल करें।

  ```java
  req.getRequestDispatcher("/fragment").include(req, resp);
  ```
* **रिडायरेक्ट**: क्लाइंट को नए URL पर 302/303/307।

  ```java
  resp.sendRedirect(req.getContextPath() + "/login");
  ```

# 14) कैरेक्टर एन्कोडिंग और i18n

एक छोटा **एन्कोडिंग फिल्टर** मोजीबेक (mojibake) को रोकता है:

```java
@WebFilter("/*")
public class Utf8Filter implements Filter {
  public void doFilter(ServletRequest req, ServletResponse res, FilterChain chain)
      throws IOException, ServletException {
    req.setCharacterEncoding("UTF-8");
    res.setCharacterEncoding("UTF-8");
    chain.doFilter(req, res);
  }
}
```

i18n के लिए `HttpServletRequest#getLocale()` से `Locale` और रिसोर्स बंडल का उपयोग करें।

# 15) सुरक्षा की मूल बातें

* **ट्रांसपोर्ट**: हमेशा HTTPS; `Secure` कुकीज़ सेट करें।
* **ऑथ**: कंटेनर-मैनेज्ड (FORM/BASIC/DIGEST), या JWT/सत्र के साथ कस्टम फिल्टर।
* **CSRF**: प्रति-सत्र टोकन जनरेट करें; स्टेट-चेंजिंग अनुरोधों पर वैलिडेट करें।
* **XSS**: आउटपुट को HTML-escape करें; `Content-Security-Policy` सेट करें।
* **क्लिकजैकिंग**: `X-Frame-Options: DENY` या CSP `frame-ancestors 'none'`।
* **CORS**: एक फिल्टर में हेडर जोड़ें:

  ```java
  resp.setHeader("Access-Control-Allow-Origin", "https://example.com");
  resp.setHeader("Access-Control-Allow-Methods", "GET,POST,PUT,DELETE");
  resp.setHeader("Access-Control-Allow-Headers", "Content-Type, Authorization");
  ```

# 16) एरर हैंडलिंग

* `web.xml` में या फ्रेमवर्क के माध्यम से एरर पेज मैप करें:

```xml
<error-page>
  <error-code>404</error-code>
  <location>/WEB-INF/errors/404.jsp</location>
</error-page>
<error-page>
  <exception-type>java.lang.Throwable</exception-type>
  <location>/WEB-INF/errors/500.jsp</location>
</error-page>
```

* कोड में, स्टेटस कोड सेट करें और API के लिए एक सुसंगत JSON एरर स्कीमा रेंडर करें।

# 17) लॉगिंग और ऑब्ज़र्वेबिलिटी

* `ServletContext#log` का उपयोग करें, या बेहतर: SLF4J + Logback/Log4j2।
* एक फिल्टर में रिक्वेस्ट-ID (UUID) जोड़ें; लॉग्स और प्रतिक्रिया हेडर में शामिल करें।
* हेल्थ एंडपॉइंट्स एक्सपोज़ करें; एक फिल्टर/सर्वलेट के माध्यम से Prometheus के साथ इंटीग्रेट करें।

# 18) पैकेजिंग और डिप्लॉयमेंट

**WAR लेआउट**:

```
myapp/
  WEB-INF/
    web.xml
    classes/            # कंपाइल्ड .class फाइलें
    lib/                # थर्ड-पार्टी जार
  index.html
  static/...
```

Maven/Gradle के साथ बिल्ड करें, एक **WAR** बनाएँ, कंटेनर के `webapps` (Tomcat) में डिप्लॉय करें या एडमिन कंसोल के माध्यम से। एम्बेडेड स्टाइल के लिए, सर्वर को बूटस्ट्रैप करने वाले `main()` के साथ **Jetty** या **Tomcat embedded** का उपयोग करें।

# 19) Servlet का टेस्टिंग

* **यूनिट**: मॉक `HttpServletRequest/Response`।

  * Spring का `org.springframework.mock.web.*` Spring के बिना भी सुविधाजनक है।
  * या Mockito से अपने स्टब्स बनाएँ।
* **इंटीग्रेशन**: एम्बेडेड Jetty/Tomcat स्टार्ट करें और HTTP क्लाइंट (REST Assured/HttpClient) के साथ एंडपॉइंट्स हिट करें।
* **एंड-टू-एंड**: पूर्ण फ्लो के लिए ब्राउज़र ऑटोमेशन (Selenium/WebDriver)।

# 20) परफॉर्मेंस टिप्स

* महंगे संसाधनों का पुन: उपयोग करें (DB पूल `DataSource` के माध्यम से); `destroy()` में क्लीन अप करें।
* स्टेटिक कंटेंट के लिए कैशिंग हेडर सेट करें; स्टेटिक एसेट्स को रिवर्स प्रॉक्सी/CDN पर ऑफलोड करें।
* GZIP कम्प्रेशन का उपयोग करें (कंटेनर सेटिंग या एक फिल्टर)।
* लंबे ऑपरेशन के लिए ब्लॉकिंग I/O से बचें; एसिंक या क्यूइंग पर विचार करें।
* एलोकेशन और GC प्रोफाइल करें; बड़े पेलोड के लिए प्रतिक्रियाओं को स्ट्रीमिंग रखें।

# 21) सामान्य गलतियाँ

* **इंस्टेंस फ़ील्ड** थ्रेड-सुरक्षित नहीं → रेस कंडीशन।
* पैरामीटर पढ़ने से पहले `req.setCharacterEncoding("UTF-8")` भूल जाना।
* बफरिंग के बिना बॉडी को दो बार पढ़ना।
* `5xx` स्टेटस सेट किए बिना एक्सेप्शन्स को स्वैलो करना।
* एक ही प्रतिक्रिया में `getWriter()` और `getOutputStream()` को मिलाना।

# 22) `javax.servlet.*` से `jakarta.servlet.*` की ओर

अगर/जब आप जकार्ता EE 9+ में अपग्रेड करते हैं:

* इम्पोर्ट्स बदलें `javax.servlet.*` → `jakarta.servlet.*`।
* जकार्ता को सपोर्ट करने वाले कंटेनर का उपयोग करें (Tomcat 10+, Jetty 11+)।
* रीबिल्ड करें; अधिकांश कोड परिवर्तन इम्पोर्ट रीनेम हैं।
* लाइब्रेरीज़ को भी जकार्ता-संगत होना चाहिए (ट्रांजिटिव डिपेंडेंसीज़ पर नज़र रखें)।

# 23) मिनिमल REST-स्टाइल उदाहरण

```java
@WebServlet(name="UsersApi", urlPatterns="/api/users/*")
public class UsersApi extends HttpServlet {
  @Override protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws IOException {
    resp.setContentType("application/json;charset=UTF-8");
    String id = pathParam(req, 1); // जैसे /api/users/42
    if (id == null) {
      resp.getWriter().write("[{\"id\":1,\"name\":\"A\"}]");
    } else {
      resp.getWriter().write("{\"id\":"+id+",\"name\":\"A\"}");
    }
  }
  private String pathParam(HttpServletRequest req, int idx) {
    String path = req.getPathInfo();        // "/42"
    if (path == null) return null;
    String[] parts = path.split("/");
    return parts.length > idx ? parts[idx] : null;
  }
}
```

# 24) बिल्ड डिपेंडेंसीज़ (क्लासिक `javax.servlet`)

Maven में **Provided** स्कोप क्योंकि कंटेनर रनटाइम पर API प्रदान करता है:

```xml
<dependency>
  <groupId>javax.servlet</groupId>
  <artifactId>javax.servlet-api</artifactId>
  <version>4.0.1</version>
  <scope>provided</scope>
</dependency>
```

**जकार्ता** के लिए:

```xml
<dependency>
  <groupId>jakarta.servlet</groupId>
  <artifactId>jakarta.servlet-api</artifactId>
  <version>6.0.0</version>
  <scope>provided</scope>
</dependency>
```

---

अगर आप मुझे अपना टार्गेट कंटेनर (Tomcat/Jetty/Liberty), Java वर्जन, और बताएँ कि आप सिंक्रोनस, एसिंक, या नॉन-ब्लॉकिंग I/O चाहते हैं, तो मैं आपके स्टैक के लिए तैयार एक प्रोडक्शन-रेडी स्केलेटन बना सकता हूँ (लॉगिंग, CORS, सिक्योरिटी हेडर, और एक साफ Maven/Gradle लेआउट) — कोई टेबल नहीं, बस संक्षिप्त कोड और चरण।