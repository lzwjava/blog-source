---
audio: false
generated: true
lang: de
layout: post
title: Filterkonfiguration in Java Servlets
translated: true
type: note
---

### Wie funktioniert `javax.servlet.FilterConfig`?

In Java-Webanwendungen, die mit der Servlet-API erstellt wurden, spielt das Interface `javax.servlet.FilterConfig` eine Schlüsselrolle bei der Konfiguration von Filtern. Filter sind Komponenten, die HTTP-Anfragen und -Antworten abfangen und verarbeiten, bevor sie ein Servlet erreichen oder nachdem sie es verlassen haben. `FilterConfig` bietet eine standardisierte Möglichkeit, Konfigurationsinformationen an einen Filter zu übergeben, wenn er vom Web-Container (z.B. Tomcat, Jetty) initialisiert wird. Im Folgenden werde ich erklären, wie `FilterConfig` funktioniert, welchen Zweck es hat und wie es verwendet wird.

---

#### **Was ist `FilterConfig`?**
`FilterConfig` ist ein Interface im Paket `javax.servlet`. Es wird vom Web-Container verwendet, um einem Filter während seiner Initialisierungsphase Konfigurationsdaten bereitzustellen. Wenn ein Filter in einer Webanwendung definiert ist (über `web.xml` oder Annotationen), erstellt der Container eine Instanz des Filters und übergibt ein `FilterConfig`-Objekt an dessen `init`-Methode. Dieses Objekt ermöglicht es dem Filter, auf Folgendes zuzugreifen:
- Seine eigenen Initialisierungsparameter.
- Den `ServletContext` der Webanwendung.
- Seinen eigenen Namen, wie in der Konfiguration definiert.

Filter implementieren das Interface `javax.servlet.Filter`, das drei Methoden umfasst: `init`, `doFilter` und `destroy`. Das `FilterConfig`-Objekt wird speziell in der `init`-Methode verwendet, um den Filter einzurichten, bevor er mit der Verarbeitung von Anfragen beginnt.

---

#### **Lebenszyklus eines Filters und `FilterConfig`**
Um zu verstehen, wie `FilterConfig` funktioniert, betrachten wir seine Rolle im Lebenszyklus eines Filters:
1. **Container-Start**: Wenn die Webanwendung startet, liest der Container die Filterdefinitionen (aus `web.xml` oder `@WebFilter`-Annotationen) und erstellt eine Instanz jedes Filters.
2. **Filter-Initialisierung**: Für jeden Filter ruft der Container die `init`-Methode auf und übergibt ein `FilterConfig`-Objekt als Parameter. Dies ist ein einmaliger Vorgang pro Filterinstanz.
3. **Anfrageverarbeitung**: Nach der Initialisierung wird die `doFilter`-Methode des Filters für jede passende Anfrage aufgerufen. Während `FilterConfig` nicht an `doFilter` übergeben wird, kann der Filter während `init` Konfigurationsdaten aus `FilterConfig` in Instanzvariablen speichern, um sie später zu verwenden.
4. **Filter-Beendigung**: Wenn die Anwendung heruntergefahren wird, wird die `destroy`-Methode aufgerufen, aber `FilterConfig` ist hier nicht beteiligt.

Das `FilterConfig`-Objekt ist während der Initialisierungsphase entscheidend, da es dem Filter ermöglicht, sich auf die Anfrageverarbeitung vorzubereiten.

---

#### **Wichtige Methoden von `FilterConfig`**
Das `FilterConfig`-Interface definiert vier Methoden, die Zugriff auf Konfigurationsinformationen bieten:

1. **`String getFilterName()`**
   - Gibt den Namen des Filters zurück, wie in der `web.xml`-Datei (unter `<filter-name>`) oder in der `@WebFilter`-Annotation angegeben.
   - Dies ist nützlich für Protokollierung, Debugging oder zur Identifizierung des Filters in einer Filterkette.

2. **`ServletContext getServletContext()`**
   - Gibt das `ServletContext`-Objekt zurück, das die gesamte Webanwendung repräsentiert.
   - Der `ServletContext` ermöglicht es dem Filter, auf anwendungsweite Ressourcen zuzugreifen, wie z.B. Kontextattribute, Protokollierungseinrichtungen oder einen `RequestDispatcher` zum Weiterleiten von Anfragen.

3. **`String getInitParameter(String name)`**
   - Ruft den Wert eines bestimmten Initialisierungsparameters anhand seines Namens ab.
   - Initialisierungsparameter sind Schlüssel-Wert-Paare, die für den Filter in `web.xml` (unter `<init-param>`) oder im `initParams`-Attribut der `@WebFilter`-Annotation definiert sind.
   - Gibt `null` zurück, wenn der Parameter nicht existiert.

4. **`Enumeration<String> getInitParameterNames()`**
   - Gibt eine `Enumeration` aller für den Filter definierten Initialisierungsparameternamen zurück.
   - Dies ermöglicht es dem Filter, über alle seine Parameter zu iterieren und ihre Werte mit `getInitParameter` abzurufen.

Diese Methoden werden von einer konkreten Klasse implementiert, die vom Web-Container bereitgestellt wird (z.B. Tomcats interne `FilterConfigImpl`). Als Entwickler interagieren Sie mit `FilterConfig` ausschließlich über dieses Interface.

---

#### **Wie `FilterConfig` konfiguriert wird**
Filter und ihre Konfiguration können auf zwei Arten definiert werden:
1. **Verwendung von `web.xml` (Bereitstellungsdeskriptor)**:
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

2. **Verwendung von Annotationen (Servlet 3.0 und höher)**:
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
    private String excludeURLs; // Instanzvariable zum Speichern von Konfigurationsdaten

    @Override
    public void init(FilterConfig filterConfig) throws ServletException {
        // Den Namen des Filters abrufen
        String filterName = filterConfig.getFilterName();
        System.out.println("Initializing filter: " + filterName);

        // Einen Initialisierungsparameter abrufen
        excludeURLs = filterConfig.getInitParameter("excludeURLs");
        if (excludeURLs != null) {
            System.out.println("Exclude URLs: " + excludeURLs);
        }

        // Optional ServletContext für spätere Verwendung speichern
        ServletContext context = filterConfig.getServletContext();
        context.log("Filter " + filterName + " initialized");
    }

    @Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)
            throws IOException, ServletException {
        // excludeURLs verwenden, um zu entscheiden, ob die Anfrage gefiltert werden soll
        chain.doFilter(request, response); // Zum nächsten Filter oder Servlet fortfahren
    }

    @Override
    public void destroy() {
        // Bereinigungscode
    }
}
```

- **In `init`**: Der Filter ruft seinen Namen, einen Initialisierungsparameter (`excludeURLs`) und den `ServletContext` ab. Er speichert `excludeURLs` in einer Instanzvariable für die Verwendung in `doFilter`.
- **In `doFilter`**: Der Filter kann die gespeicherte Konfiguration (z.B. `excludeURLs`) verwenden, um Anfragen zu verarbeiten.

---

#### **Wichtige Punkte zu `FilterConfig`**
- **Filterspezifischer Gültigkeitsbereich**: Initialisierungsparameter in `FilterConfig` sind spezifisch für die Filterinstanz. Verschiedene Filter können Parameter mit demselben Namen, aber unterschiedlichen Werten haben.
- **Unterschied zu `ServletContext`**: Der `ServletContext` (abgerufen über `getServletContext()`) bietet anwendungsweite Initialisierungsparameter und Ressourcen, die sich von den filterspezifischen Parametern in `FilterConfig` unterscheiden.
- **Einmalige Verwendung im Lebenszyklus**: `FilterConfig` wird nur an `init` übergeben. Wenn der Filter seine Daten später benötigt (z.B. in `doFilter`), muss er die Daten in Instanzvariablen speichern.
- **Vom Container bereitgestellt**: `FilterConfig` ist ein Interface, und der Web-Container stellt die konkrete Implementierung bereit.

---

#### **Zusammenfassung**
`javax.servlet.FilterConfig` funktioniert, indem es einem Filter während seiner Initialisierung Konfigurationsinformationen bereitstellt. Der Web-Container übergibt ein `FilterConfig`-Objekt an die `init`-Methode des Filters, was dem Filter ermöglicht:
- Auf seinen Namen zuzugreifen (`getFilterName`).
- Initialisierungsparameter abzurufen (`getInitParameter`, `getInitParameterNames`).
- Mit der Webanwendung über den `ServletContext` zu interagieren (`getServletContext`).

Dies ermöglicht es, Filter flexibel zu konfigurieren – über `web.xml` oder Annotationen – und bereitet sie darauf vor, HTTP-Anfragen und -Antworten effektiv zu verarbeiten. Egal, ob Sie bestimmte URLs ausschließen, Timeouts setzen oder Nachrichten protokollieren, `FilterConfig` ist die Brücke zwischen der Konfiguration des Filters und seinem Laufzeitverhalten.