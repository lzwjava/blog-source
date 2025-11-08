---
audio: false
generated: true
image: false
lang: de
layout: post
model: anthropic/claude-4.5-sonnet
title: IBM WebSphere Request Routing Erklärt
translated: true
type: note
---

Lassen Sie mich erklären, wie IBM WebSphere Application Server (WAS) eingehende Anfragen und Routing behandelt:

## Anfragefluss in IBM WAS

Wenn eine Anfrage bei IBM WAS eintrifft, ist hier der typische Ablauf:

**1. Web Server Layer (Optional)**
- Die Anfrage trifft zuerst auf IBM HTTP Server (IHS) oder einen anderen Webserver
- Das Web Server Plugin leitet zur entsprechenden WAS-Instanz weiter

**2. Web Container Einstiegspunkt**
Die Anfrage tritt in WAS durch den **Web Container** ein, der Teil der Haupt-Servlet-Engine ist. Die Schlüsselpaketstruktur ist:

```
com.ibm.ws.webcontainer.*
```

**3. Anfrageverarbeitungskette**

Das Routing erfolgt über mehrere Komponenten:

**Transport Channel Framework**
- `com.ibm.ws.channel.*` - behandelt die Netzwerkkommunikation
- HTTP-Transportkanäle empfangen die Anfrage

**Web Container Verarbeitung**
```
com.ibm.ws.webcontainer.servlet.ServletWrapper
com.ibm.ws.webcontainer.filter.WebAppFilterManager
```

**4. Filterkettenausführung**

Filter funktionieren genau wie standardmäßige Java Servlet Filter, werden aber von WAS verwaltet:

- **Definiert in web.xml** Ihrer Anwendung
- Filter werden in der angegebenen Reihenfolge verkettet
- Jeder Filter kann Anfrage und Antwort prüfen/modifizieren
- Verwendet die standardmäßige `javax.servlet.Filter`-Schnittstelle

```xml
<filter>
    <filter-name>MyFilter</filter-name>
    <filter-class>com.example.MyFilter</filter-class>
</filter>

<filter-mapping>
    <filter-name>MyFilter</filter-name>
    <url-pattern>/*</url-pattern>
</filter-mapping>
```

**Filterausführungsreihenfolge:**
1. WAS lädt Filterkonfigurationen beim Anwendungsstart
2. WebAppFilterManager erstellt die Filterkette
3. Bei jeder Anfrage: Anfrage → Filter1 → Filter2 → ... → Servlet

## Hauptpakete in IBM WAS

**Kernpakete:**
- `com.ibm.ws.webcontainer.*` - Web Container Implementierung
- `com.ibm.ws.runtime.*` - Laufzeitdienste
- `com.ibm.websphere.servlet.*` - WAS-spezifische Servlet-Erweiterungen
- `com.ibm.ws.channel.*` - Transportschicht
- `com.ibm.ejs.*` - EJB Container Services
- `com.ibm.ws.naming.*` - JNDI Implementierung

## Routing-Mechanismus

**Virtual Host Routing:**
- Konfiguriert in der WAS Admin Console
- Ordnet `Hostname:Port`-Kombinationen Anwendungen zu
- Konfiguration: `VirtualHost → Host Aliases → Applications`

**Context Root Routing:**
- Jede Anwendung hat einen Kontextroot (z.B. `/myapp`)
- WAS verwaltet eine Registry der bereitgestellten Anwendungen
- URI-Mapping: `http://server:port/contextRoot/servletPath`

**Servlet Mapping:**
- Definiert in web.xml oder Annotationen
- Musterabgleich (exakt, Pfad, Erweiterung, Standard)

## Anwendungsstartsequenz

Wenn die Anwendung startet:
1. **ClassLoader Initialisierung** - App erhält ihren eigenen ClassLoader
2. **web.xml Parsing** - Filter, Servlets, Listener geladen
3. **ServletContextListeners feuern** - `contextInitialized()`
4. **Filter instanziiert** - `init()`-Methode aufgerufen
5. **Load-on-startup Servlets** - Initialisiert eifrige Servlets
6. **Anwendung als GESTARTET markiert** - Bereit zum Empfangen von Anfragen

Die Routing-Registry wird aktualisiert und die Anwendung ist jetzt unter ihrem Kontextroot verfügbar.

Klärt dies, wie WAS Anfrage-Routing und Filterung behandelt?