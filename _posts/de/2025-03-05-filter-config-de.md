---
audio: false
generated: true
lang: de
layout: post
title: Filterkonfiguration in Java-Servlets
translated: true
---

### Wie funktioniert `javax.servlet.FilterConfig`?

In Java-Webanwendungen, die mit der Servlet-API erstellt wurden, spielt das Interface `javax.servlet.FilterConfig` eine zentrale Rolle bei der Konfiguration von Filtern. Filter sind Komponenten, die HTTP-Anfragen und -Antworten abfangen und verarbeiten, bevor sie einen Servlet erreichen oder nachdem sie ihn verlassen haben. `FilterConfig` bietet eine standardisierte Möglichkeit, Konfigurationsinformationen an einen Filter zu übergeben, wenn dieser vom Web-Container (z.B. Tomcat, Jetty) initialisiert wird. Im Folgenden wird erklärt, wie `FilterConfig` funktioniert, wofür es verwendet wird und wie es eingesetzt wird.

---

#### **Was ist `FilterConfig`?**
`FilterConfig` ist ein Interface im `javax.servlet`-Paket. Es wird vom Web-Container verwendet, um einem Filter während seiner Initialisierungsphase Konfigurationsdaten zu liefern. Wenn ein Filter in einer Webanwendung definiert wird (über `web.xml` oder Annotationen), erstellt der Container eine Instanz des Filters und übergibt ein `FilterConfig`-Objekt an dessen `init`-Methode. Dieses Objekt ermöglicht es dem Filter, auf Folgendes zuzugreifen:
- Seine eigenen Initialisierungsparameter.
- Den `ServletContext` der Webanwendung.
- Seinen eigenen Namen, wie in der Konfiguration definiert.

Filter implementieren das Interface `javax.servlet.Filter`, das drei Methoden enthält: `init`, `doFilter` und `destroy`. Das `FilterConfig`-Objekt wird speziell in der `init`-Methode verwendet, um den Filter vor der Verarbeitung von Anfragen einzurichten.

---

#### **Lebenszyklus eines Filters und `FilterConfig`**
Um zu verstehen, wie `FilterConfig` funktioniert, betrachten wir seine Rolle im Lebenszyklus des Filters:
1. **Container-Start**: Wenn die Webanwendung startet, liest der Container die Filterdefinitionen (aus `web.xml` oder `@WebFilter`-Annotationen) und erstellt eine Instanz jedes Filters.
2. **Filter-Initialisierung**: Für jeden Filter ruft der Container die `init`-Methode auf und übergibt ein `FilterConfig`-Objekt als Parameter. Dies ist ein einmaliger Vorgang pro Filterinstanz.
3. **Anforderungsverarbeitung**: Nach der Initialisierung wird die `doFilter`-Methode des Filters für jede passende Anfrage aufgerufen. Während `FilterConfig` nicht an `doFilter` übergeben wird, kann der Filter Konfigurationsdaten von `FilterConfig` in Instanzvariablen während `init` für spätere Verwendung speichern.
4. **Filter-Shutdown**: Wenn die Anwendung heruntergefahren wird, wird die `destroy`-Methode aufgerufen, aber `FilterConfig` ist hier nicht beteiligt.

Das `FilterConfig`-Objekt ist während der Initialisierungsphase entscheidend, da es dem Filter ermöglicht, sich auf die Verarbeitung von Anfragen vorzubereiten.

---

#### **Wichtige Methoden von `FilterConfig`**
Das Interface `FilterConfig` definiert vier Methoden, die Zugriff auf Konfigurationsinformationen bieten:

1. **`String getFilterName()`**
   - Gibt den Namen des Filters zurück, wie in der `web.xml`-Datei (unter `<filter-name>`) oder in der `@WebFilter`-Annotation angegeben.
   - Dies ist nützlich für Protokollierung, Debugging oder Identifikation des Filters in einer Filterkette.

2. **`ServletContext getServletContext()`**
   - Gibt das `ServletContext`-Objekt zurück, das die gesamte Webanwendung darstellt.
   - Der `ServletContext` ermöglicht es dem Filter, auf anwendungsweite Ressourcen zuzugreifen, wie z.B. Kontextattribute, Protokollierungsmöglichkeiten oder einen `RequestDispatcher`, um Anfragen weiterzuleiten.

3. **`String getInitParameter(String name)`**
   - Ruft den Wert eines bestimmten Initialisierungsparameters anhand seines Namens ab.
   - Initialisierungsparameter sind Schlüssel-Wert-Paare, die für den Filter in `web.xml` (unter `<init-param>`) oder im `initParams`-Attribut der `@WebFilter`-Annotation definiert sind.
   - Gibt `null` zurück, wenn der Parameter nicht existiert.

4. **`Enumeration<String> getInitParameterNames()`**
   - Gibt eine `Enumeration` aller für den Filter definierten Initialisierungsparameter-Namen zurück.
   - Dies ermöglicht es dem Filter, über alle seine Parameter zu iterieren und deren Werte mit `getInitParameter` abzurufen.

Diese Methoden werden von einer konkreten Klasse implementiert, die vom Web-Container bereitgestellt wird (z.B. `FilterConfigImpl` von Tomcat). Als Entwickler interagieren Sie mit `FilterConfig` ausschließlich über dieses Interface.

---

#### **Wie `FilterConfig` konfiguriert wird**
Filter und deren Konfiguration können auf zwei Arten definiert werden:
1. **Verwendung von `web.xml` (Deployment Descriptor)**:
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
   - `<filter-name>` definiert den Namen des Filters.
   - `<init-param>` gibt Initialisierungsparameter als Schlüssel-Wert-Paare an.

2. **Verwendung von Annotationen (Servlet 3.0 und später)**:
   ```java
   import javax.servlet.annotation.WebFilter;
   import javax.servlet.annotation.WebInitParam;

   @WebFilter(
       filterName = "MyFilter",
       urlPatterns = "/*",
       initParams = @WebInitParam(name = "excludeURLs", value = "/login,/signup")
   )
   public class MyFilter implements Filter {
       // Implementierung
   }
   ```
   - Die `@WebFilter`-Annotation definiert den Namen des Filters, URL-Muster und Initialisierungsparameter.

In beiden Fällen verwendet der Container diese Konfiguration, um ein `FilterConfig`-Objekt zu erstellen und es an die `init`-Methode des Filters zu übergeben.

---

#### **Praktisches Beispiel**
Hier ist ein Beispiel, wie ein Filter `FilterConfig` in der Praxis verwenden könnte:

```java
import javax.servlet.*;
import java.io.IOException;

public class MyFilter implements Filter {
    private String excludeURLs; // Instanzvariable zur Speicherung von Konfigurationsdaten

    @Override
    public void init(FilterConfig filterConfig) throws ServletException {
        // Hole den Namen des Filters
        String filterName = filterConfig.getFilterName();
        System.out.println("Initialisiere Filter: " + filterName);

        // Hole einen Initialisierungsparameter
        excludeURLs = filterConfig.getInitParameter("excludeURLs");
        if (excludeURLs != null) {
            System.out.println("Exclude URLs: " + excludeURLs);
        }

        // Optional: Speichere ServletContext für spätere Verwendung
        ServletContext context = filterConfig.getServletContext();
        context.log("Filter " + filterName + " initialisiert");
    }

    @Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)
            throws IOException, ServletException {
        // Verwende excludeURLs, um zu entscheiden, ob die Anfrage gefiltert werden soll
        chain.doFilter(request, response); // Fortfahren zum nächsten Filter oder Servlet
    }

    @Override
    public void destroy() {
        // Aufräumcode
    }
}
```

- **In `init`**: Der Filter ruft seinen Namen, einen Initialisierungsparameter (`excludeURLs`) und den `ServletContext` ab. Er speichert `excludeURLs` in einer Instanzvariablen für die Verwendung in `doFilter`.
- **In `doFilter`**: Der Filter kann die gespeicherte Konfiguration (z.B. `excludeURLs`) verwenden, um Anfragen zu verarbeiten.

---

#### **Wichtige Punkte zu `FilterConfig`**
- **Filter-spezifischer Geltungsbereich**: Initialisierungsparameter in `FilterConfig` sind spezifisch für die Filterinstanz. Verschiedene Filter können Parameter mit demselben Namen, aber unterschiedlichen Werten haben.
- **Kontrast zu `ServletContext`**: Der `ServletContext` (über `getServletContext()` zugänglich) bietet anwendungsweite Initialisierungsparameter und Ressourcen, die sich von den filter-spezifischen Parametern in `FilterConfig` unterscheiden.
- **Einmalige Verwendung im Lebenszyklus**: `FilterConfig` wird nur an `init` übergeben. Wenn der Filter seine Daten später benötigt (z.B. in `doFilter`), muss er die Daten in Instanzvariablen speichern.
- **Vom Container bereitgestellt**: `FilterConfig` ist ein Interface, und der Web-Container stellt die konkrete Implementierung bereit.

---

#### **Zusammenfassung**
`javax.servlet.FilterConfig` funktioniert, indem es einem Filter während seiner Initialisierung Konfigurationsinformationen bereitstellt. Der Web-Container übergibt ein `FilterConfig`-Objekt an die `init`-Methode des Filters, wodurch der Filter:
- Auf seinen Namen zugreifen kann (`getFilterName`).
- Initialisierungsparameter abrufen kann (`getInitParameter`, `getInitParameterNames`).
- Mit der Webanwendung über den `ServletContext` interagieren kann (`getServletContext`).

Dies ermöglicht es Filtern, flexibel konfiguriert zu werden – über `web.xml` oder Annotationen – und bereitet sie darauf vor, HTTP-Anfragen und -Antworten effektiv zu verarbeiten. Ob Sie bestimmte URLs ausschließen, Zeitüberschreitungen festlegen oder Nachrichten protokollieren, `FilterConfig` ist die Brücke zwischen der Konfiguration des Filters und seinem Laufzeitverhalten.