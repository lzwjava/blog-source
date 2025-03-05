---
audio: false
generated: true
lang: hi
layout: post
title: Java Servlets में Filter Configuration
translated: true
---

### `javax.servlet.FilterConfig` कैसे काम करता hai?

Java web applications में Servlet API का उपयोग karte hue banaye gaye, `javax.servlet.FilterConfig` interface filters ko configure karne mein ek key role play karta hai. Filters components hain jo HTTP requests aur responses ko intercept aur process karte hain pehle se ki yeh ek servlet tak pahunch sake ya baad mein se ki yeh usse chhut jaye. `FilterConfig` ek standardized way provide karta hai jo configuration information ko ek filter ko pass karne ke liye jab yeh web container (e.g., Tomcat, Jetty) dwara initialize kiya jaata hai. Niche, main samjhata hoon ki `FilterConfig` kaise kaam karta hai, uska purpose aur uska use.

---

#### **`FilterConfig` kya hai?**
`FilterConfig` ek interface hai `javax.servlet` package mein. Yeh web container dwara ek filter ko configuration data supply karne ke liye use hota hai uske initialization phase mein. Jab ek filter ek web application mein define kiya jaata hai (`web.xml` ya annotations ke dwara), container ek instance of the filter create karta hai aur ek `FilterConfig` object ko uske `init` method mein pass karta hai. Yeh object filter ko access karne deta hai:
- Apne initialization parameters ko.
- Web application ka `ServletContext`.
- Apne configuration mein define kiya gaya apna naam.

Filters `javax.servlet.Filter` interface ko implement karte hain, jo teen methods ko include karta hai: `init`, `doFilter`, aur `destroy`. `FilterConfig` object specifically `init` method mein use hota hai filter ko setup karne ke liye pehle se ki yeh requests ko process karne shuru kare.

---

#### **Filter aur `FilterConfig` ka Lifecycle**
`FilterConfig` kaam kaise karta hai, chalo uske filter lifecycle mein uske role ko dekhte hain:
1. **Container Startup**: Jab web application start hoti hai, container filter definitions ko read karta hai (`web.xml` ya `@WebFilter` annotations se) aur har filter ka ek instance create karta hai.
2. **Filter Initialization**: Har filter ke liye, container `init` method ko call karta hai, ek `FilterConfig` object ko parameter ke roop mein pass karke. Yeh ek filter instance ke liye ek one-time operation hai.
3. **Request Processing**: Initialization ke baad, filter ka `doFilter` method har matching request ke liye call hota hai. `FilterConfig` ko `doFilter` mein pass nahi kiya jaata, lekin filter `FilterConfig` se configuration data ko `init` mein instance variables mein store kar sakta hai baad mein use ke liye.
4. **Filter Shutdown**: Jab application shutdown hoti hai, `destroy` method call hota hai, lekin `FilterConfig` yahan involve nahi hota.

`FilterConfig` object initialization phase mein critical hota hai, filter ko request processing ke liye prepare karne mein madad karte hue.

---

#### **`FilterConfig` ke Key Methods**
`FilterConfig` interface define karta hai chaar methods jo configuration information ko access karne ke liye provide karte hain:

1. **`String getFilterName()`**
   - `web.xml` file mein define kiya gaya filter ka naam return karta hai (`<filter-name>` ke under) ya `@WebFilter` annotation mein.
   - Yeh logging, debugging, ya filter chain mein filter ko identify karne mein useful hota hai.

2. **`ServletContext getServletContext()`**
   - `ServletContext` object ko return karta hai, jo entire web application ko represent karta hai.
   - `ServletContext` filter ko application-wide resources ko access karne deta hai, jaise context attributes, logging facilities, ya ek `RequestDispatcher` ko requests ko forward karne ke liye.

3. **`String getInitParameter(String name)`**
   - Ek specific initialization parameter ka value uske naam ke dwara retrieve karta hai.
   - Initialization parameters key-value pairs hain jo filter ke liye `web.xml` mein define kiya gaya hai (`<init-param>` ke under) ya `@WebFilter` annotation ke `initParams` attribute mein.
   - Agar parameter exist nahi karta, to `null` return karta hai.

4. **`Enumeration<String> getInitParameterNames()`**
   - Filter ke liye define kiya gaya sab initialization parameter names ka ek `Enumeration` return karta hai.
   - Yeh filter ko apne parameters par iterate karne deta hai aur unke values ko retrieve karne ke liye `getInitParameter` ka use karke.

Yeh methods ek concrete class dwara implement kiya jaata hai jo web container dwara provide kiya jaata hai (e.g., Tomcat ka internal `FilterConfigImpl`). Ek developer ke roop mein, aap `FilterConfig` ke saath sirf is interface ke dwara interact karte hain.

---

#### **`FilterConfig` kaise configure kiya jaata hai**
Filters aur unka configuration do tarah se define kiya ja sakta hai:
1. **`web.xml` (Deployment Descriptor) ka use karke**:
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
   - `<filter-name>` filter ka naam define karta hai.
   - `<init-param>` initialization parameters ko key-value pairs ke roop mein specify karta hai.

2. **Annotations ka use karke (Servlet 3.0 aur baad mein)**:
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
   - `@WebFilter` annotation filter ka naam, URL patterns, aur initialization parameters define karta hai.

Dono cases mein, container is configuration ko use karta hai ek `FilterConfig` object create karne ke liye aur usko filter ke `init` method mein pass karne ke liye.

---

#### **Practical Example**
Yeh hai ki ek filter `FilterConfig` ko practical mein kaise use kar sakta hai:

```java
import javax.servlet.*;
import java.io.IOException;

public class MyFilter implements Filter {
    private String excludeURLs; // Instance variable to store config data

    @Override
    public void init(FilterConfig filterConfig) throws ServletException {
        // Get the filter's name
        String filterName = filterConfig.getFilterName();
        System.out.println("Initializing filter: " + filterName);

        // Get an initialization parameter
        excludeURLs = filterConfig.getInitParameter("excludeURLs");
        if (excludeURLs != null) {
            System.out.println("Exclude URLs: " + excludeURLs);
        }

        // Optionally store ServletContext for later use
        ServletContext context = filterConfig.getServletContext();
        context.log("Filter " + filterName + " initialized");
    }

    @Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)
            throws IOException, ServletException {
        // Use excludeURLs to decide whether to filter the request
        chain.doFilter(request, response); // Proceed to next filter or servlet
    }

    @Override
    public void destroy() {
        // Cleanup code
    }
}
```

- **In `init`**: Filter apne naam, ek initialization parameter (`excludeURLs`), aur `ServletContext` ko retrieve karta hai. Yeh `excludeURLs` ko ek instance variable mein store karta hai `doFilter` ke liye use ke liye.
- **In `doFilter`**: Filter stored configuration (e.g., `excludeURLs`) ko use kar sakta hai requests ko process karne ke liye.

---

#### **`FilterConfig` ke Key Points**
- **Filter-Specific Scope**: Initialization parameters in `FilterConfig` filter instance ke liye specific hain. Alag-alag filters ke paas parameters ke same name ke saath alag values ho sakte hain.
- **Contrast with `ServletContext`**: `ServletContext` (`getServletContext()` dwara access kiya jaata hai) application-wide initialization parameters aur resources provide karta hai, alag se filter-specific parameters `FilterConfig` mein.
- **Single Use in Lifecycle**: `FilterConfig` sirf `init` mein pass kiya jaata hai. Agar filter ko apne data ko baad mein chahiye hai (e.g., `doFilter` mein), toh yeh data ko instance variables mein store karna padta hai.
- **Container-Provided**: `FilterConfig` ek interface hai, aur web container concrete implementation provide karta hai.

---

#### **Summary**
`javax.servlet.FilterConfig` kaam karta hai ek filter ko configuration information provide karke uske initialization ke dauran. Web container ek `FilterConfig` object ko filter ke `init` method mein pass karta hai, filter ko:
- Apne naam ko access karne ke liye (`getFilterName`).
- Initialization parameters ko retrieve karne ke liye (`getInitParameter`, `getInitParameterNames`).
- Web application ke saath interact karne ke liye `ServletContext` (`getServletContext`).

Yeh filters ko flexibly configure karne deta hai—`web.xml` ya annotations ke dwara—aur unhe HTTP requests aur responses ko effectively process karne ke liye prepare karta hai. Chahiye ki aap certain URLs ko exclude kar rahe hain, timeouts set kar rahe hain, ya messages ko log kar rahe hain, `FilterConfig` filter ke configuration aur uske runtime behavior ke beech ka bridge hai.