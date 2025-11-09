---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Krieg versus Ohr Verpackungsvergleich
translated: true
type: note
---

### Übersicht

In Java EE (jetzt Jakarta EE) sind WAR (Web Archive) und EAR (Enterprise Archive) standardisierte Paketierungsformate für die Bereitstellung von Anwendungen auf Application Servern wie Tomcat, WildFly oder GlassFish. WAR konzentriert sich auf Web-Tier-Komponenten, während EAR mehrere Module für vollständige Enterprise-Anwendungen bündelt. Nachfolgend finden Sie einen detaillierten Vergleich.

| Aspekt               | WAR (Web Archive)                                                                 | EAR (Enterprise Archive)                                                                 |
|----------------------|-----------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| **Zweck**           | Stellt Webanwendungen (z.B. Servlets, JSPs, statische Inhalte) als eine Einheit für die Web-Tier-Funktionalität bereit. | Stellt Enterprise-Anwendungen bereit, indem mehrere Untermodule (z.B. WARs, EJB-JARs) für mehrschichtige, verteilte Systeme gepackt werden. |
| **Inhalt**          | - Web-App-Dateien: JSPs, HTML/CSS/JS, Servlets.<br>- Bibliotheken: WEB-INF/lib JARs.<br>- Deployment Descriptor: web.xml (optional in modernen Versionen). | - Mehrere Module: WARs, EJB-JARs, Client-JARs.<br>- Gemeinsam genutzte Bibliotheken.<br>- Deployment Descriptor: application.xml.<br>- RARs für Resource Adapter (optional). |
| **Struktur**         | - Root: Statische Ressourcen (z.B. index.html).<br>- WEB-INF/: classes, lib, web.xml. | - Root: META-INF/application.xml.<br>- Unterverzeichnisse für jedes Modul (z.B. myapp.war, myejb.jar). |
| **Dateierweiterung** | .war                                                                             | .ear                                                                                     |
| **Bereitstellungsumfang** | Einzelmodul; wird auf Web-Container (z.B. Tomcat) oder vollständige Application Server bereitgestellt. | Multi-Modul; wird nur auf vollständigen Application Servern (z.B. JBoss, WebLogic) für Enterprise-Features wie Transaktionen bereitgestellt. |
| **Größe & Komplexität** | Kleiner und einfacher; ideal für eigenständige Webanwendungen.                  | Größer und komplexer; unterstützt Modularität und gemeinsam genutzte Ressourcen über Module hinweg. |
| **Anwendungsfälle** | Web-Portale, REST-APIs, einfache Dienste (z.B. Spring Boot Web-Apps, die als WAR gepackt sind). | Komplexe Enterprise-Systeme (z.B. Banking-Apps mit Web-UI + Geschäftslogik + Datenzugriff). |
| **Abhängigkeiten**  | Baut auf Container für Web-Dienste; keine eingebaute EJB-Unterstützung.          | Unterstützt EJBs, JMS und modulübergreifende Abhängigkeiten; fördert lose Kopplung.       |

### Zusammenfassung der wichtigsten Unterschiede

- **Modularität**: WAR ist monolithisch für Web-Schichten; EAR ermöglicht die Zusammensetzung mehrerer WARs/JARs.
- **Serveranforderungen**: WAR funktioniert auf schlanken Web-Servern; EAR benötigt einen vollständigen JEE-Server.
- **Evolution**: Mit Microservices und Cloud-native Trends (z.B. Spring Boot, Quarkus) werden WARs oft für containerisierte Bereitstellungen (Docker) verwendet, während EARs seltener geworden sind, aber für Legacy-Enterprise-Apps nach wie vor wichtig sind.

Für praktische Beispiele siehe die offizielle Jakarta EE-Dokumentation: [Jakarta EE Tutorial](https://jakartaee.github.io/tutorial/) oder Oracles Java EE-Archive: [Java EE Packaging](https://docs.oracle.com/javaee/7/tutorial/packaging.htm).