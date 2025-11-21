---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4.1-fast
title: 'Vergleich von Anforderungsfiltern: WebSphere vs. Spring Boot'
translated: true
type: note
---

### Übersicht
Sowohl IBM WebSphere Application Server (WAS, traditionell oder Liberty) als auch Spring Boot unterstützen das Konzept einer **Anforderungsverarbeitungskette** basierend auf dem Standard-Java-Servlet-API `javax.servlet.Filter` und `FilterChain`. Hierbei durchlaufen eingehende HTTP-Anforderungen eine Reihe von Filtern, bevor sie Servlets (oder Controller/Handler) erreichen, und Antworten können auf dem Rückweg modifiziert werden.

- Filter ermöglichen Vorverarbeitung (z.B. Authentifizierung, Protokollierung, Komprimierung) und Nachverarbeitung von Anforderungen/Antworten.
- Der Kernmechanismus — Implementieren von `Filter`, Aufrufen von `chain.doFilter(request, response)` um fortzufahren — ist **identisch**, da beide in einem Servlet-Container laufen (WAS hat seinen eigenen vollständigen Java-EE-Web-Container; Spring Boot bettet standardmäßig Tomcat/Jetty/Undertow ein).

Es gibt keinen grundlegenden Unterschied in der Funktionsweise eines grundlegenden "Request-Chain-Filters". Die Art und Weise, wie Sie Filter konfigurieren, anordnen und integrieren, unterscheidet sich jedoch erheblich aufgrund der Architektur der jeweiligen Plattform.

### Wichtiger Vergleich

| Aspekt                   | IBM WebSphere Application Server (Traditional/Liberty) | Spring Boot |
|--------------------------|---------------------------------------------------------|-------------|
| **Zugrunde liegender Mechanismus** | Standard-Servlet-Filter (`javax.servlet.Filter`). WAS hat auch proprietäre Erweiterungen wie `ChainedRequest`/`ChainedResponse` für interne Request-Weiterleitung/Verkettung in einigen Szenarien (z.B. Portal oder benutzerdefinierte IBM-APIs). | Standard-Servlet-Filter. Spring Boot registriert automatisch jede `@Component` Filter-Bean oder Sie registrieren explizit via `FilterRegistrationBean`. |
| **Konfiguration**         | Primär via `web.xml` (deklarativ) oder programmatische Registrierung. Für globale Filter (applikationsübergreifend): komplex — erfordert Shared Libraries, benutzerdefinierte Listener oder IBM-spezifische Erweiterungen (keine einfache serverweite web.xml wie bei Tomcat). | Convention-over-Configuration: Mit `@Component` + `@Order` annotieren für automatische Registrierung, oder `FilterRegistrationBean` für feinere Kontrolle verwenden (URL-Muster, Dispatcher-Typen). Sehr entwicklerfreundlich. |
| **Reihenfolge**           | Definiert in `web.xml`-Reihenfolge oder via `@Order` wenn programmatisch. Globale Reihenfolge ist schwierig. | Einfach mit `@Order(n)` (niedriger = früher) oder `Ordered`-Interface. Spring Boot verwaltet die Kette automatisch. |
| **Sicherheits-Filter-Kette** | Verwendet Standard-Servlet-Filter oder IBM-spezifische Sicherheit (z.B. TAI, JEE-Rollen). Keine eingebaute Sicherheitskette wie Spring Security. | Spring Security bietet eine leistungsstarke `SecurityFilterChain` (via `FilterChainProxy`) mit 15+ geordneten Filtern (CSRF, Authentifizierung, Session-Management, etc.). Hochgradig anpassbar mit mehreren Ketten pro Pfad. |
| **Einfachheit beim Hinzufügen benutzerdefinierter Filter** | Umständlicher, besonders für globale/applikationsübergreifende Filter. Oft sind Admin-Konsolen-Anpassungen oder Shared Libraries erforderlich. | Extrem einfach — nur eine `@Component` Bean oder Konfigurationsklasse. Automatisch in den eingebetteten Container integriert. |
| **Bereitstellungsmodell** | Traditioneller vollständiger Java-EE-Server. Apps als WAR/EAR bereitgestellt. Unterstützt umfangreiche Enterprise-Features (Clustering, Transaktionen, JMS). | Eingebetteter Container (standardmäßig eigenständige ausführbare JAR). Kann als WAR auf externen Servern (einschließlich WAS) bereitgestellt werden. Leichtgewichtig/Microservice-orientiert. |
| **Performance/Overhead**  | Höherer Overhead (vollständiger Applikationsserver). Transportketten, Web-Container-Kanäle fügen Ebenen hinzu. | Geringerer Overhead (eingebetteter Leichtgewichts-Container). Schnellerer Start, geringerer Ressourcenverbrauch. |
| **Wenn Filter laufen**     | In der eingehenden Kette des WAS-Web-Containers. Kann Server-Level-Transportfilter haben (z.B. IP-Filterung auf TCP-Kanälen). | In der Filterkette des eingebetteten Containers. Spring Boot fügt eigene Filter hinzu (Fehlerbehandlung, Zeichenkodierung, etc.). |
| **Häufige Anwendungsfälle** | Enterprise-Monolithen, Portale, Legacy-Java-EE-Apps, die globale Sicherheit/Protokollierung benötigen. | Moderne Microservices, REST-APIs, schnelle Entwicklung mit Spring Security. |

### Praktische Beispiele

**Standard benutzerdefinierter Filter (derselbe Code funktioniert in beiden):**
```java
@Component  // Nur Spring Boot; in WAS in web.xml deklarieren
@Order(1)
public class LoggingFilter implements Filter {
    public void doFilter(ServletRequest req, ServletResponse res, FilterChain chain)
            throws IOException, ServletException {
        System.out.println("Request: " + ((HttpServletRequest) req).getRequestURI());
        chain.doFilter(req, res);  // Kritisch: leitet an nächsten Filter/Servlet weiter
    }
    // init/destroy...
}
```

**In Spring Boot (automatisch registriert):**
Einfach die Klasse oben + `@Component`.

**In WAS:**
Hinzufügen in `web.xml`:
```xml
<filter>
    <filter-name>LoggingFilter</filter-name>
    <filter-class>com.example.LoggingFilter</filter-class>
</filter>
<filter-mapping>
    <filter-name>LoggingFilter</filter-name>
    <url-pattern>/*</url-pattern>
</filter-mapping>
```

### Wann man was wählt
- **Verwenden Sie WAS-Filter**, wenn Sie sich in einer Legacy-IBM-Umgebung befinden, vollständige Java-EE-Features benötigen oder Filter global über viele Apps hinweg ohne Codeänderungen anwenden müssen.
- **Verwenden Sie Spring-Boot-Filter** (insbesondere mit Spring Security) für neue/Greenfield-Projekte, Microservices, schnelle Iteration oder wenn Sie mehrere Sicherheitsketten und einfache Reihenfolgensteuerung wünschen.

Zusammenfassend ist das **Konzept der Request-Chain-Filter dasselbe** (Servlet-Spezifikation), aber **Spring Boot macht es für die meisten modernen Anwendungsfälle viel einfacher und leistungsfähiger**, während WAS eher Enterprise-lastig und konfigurationsintensiv ist.

[IBM WAS Servlet Filtering Dokumentation](https://www.ibm.com/docs/en/was/9.0.5?topic=extensions-servlet-filtering)
[Spring Boot Custom Filters](https://www.baeldung.com/spring-boot-add-filter)
[Spring Security Filter Chain](https://docs.spring.io/spring-security/reference/servlet/architecture.html)