---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4.1-fast
title: Spring Boot hat Liberty überholt
translated: true
type: note
---

IBM WebSphere Application Server Liberty Profile (oft abgekürzt als WLP oder einfach Liberty) war IBMs Versuch, seinen schwergewichtigen traditionellen WebSphere Application Server (WAS) zu modernisieren, indem ab etwa 2012–2013 eine leichtgewichtige, zusammensetzbare, cloud-freundliche Jakarta EE (ehemals Java EE) Laufzeitumgebung geschaffen wurde. Obwohl technisch solide und in einigen Bereichen sogar überlegen (schneller Start, geringer Speicherbedarf, exzellente MicroProfile-Unterstützung via Open Liberty), **hat Liberty den Popularitätskampf für neue Java-Web-/Microservices-Entwicklungen ab Mitte der 2010er Jahre größtenteils "verloren"** gegenüber Spring Boot.

### Hauptgründe für die Dominanz von Spring Boot gegenüber Liberty

| Grund | Vorteil von Spring Boot | Nachteil von Liberty / Traditionellem App-Server |
|--------|-----------------------|-------------------------------------------|
| **Developer Productivity & Benutzerfreundlichkeit** | Convention-over-Configuration, Auto-Konfiguration, eingebetteter Server (standardmäßig Tomcat/Jetty/Undertow), `spring-boot-starter-*` beseitigen Boilerplate-Code. Null-Konfiguration, produktionsreife Apps in Minuten. | Erfordert immer noch server.xml-Konfiguration, Feature-Aktivierung und mehr manuellen Aufbau, auch wenn es leichter als der vollständige WAS ist. Fühlt sich für viele Entwickler "altmodisch" an. |
| **Eigenständiges Ausführbares Modell** | Fat JAR / Uber-JAR mit eingebettetem Server → überall ausführbar mit `java -jar`, perfekt für Docker/Kubernetes und DevOps. Kein externes Server-Management. | Primär ein separater Server, in den WAR/EAR bereitgestellt werden (obwohl Liberty später Unterstützung für ausführbare JARs hinzufügte, wirkte es aufgesetzt und wurde nie der Standard-Workflow). |
| **Ökosystem & Community** | Massive Open-Source-Community (Pivotal/VMware), riesige Anzahl von Drittanbieter-Startern, exzellente Dokumentation, Stack Overflow-Antworten, Tutorials. | Kleinere Community; hauptsächlich IBM-Dokumentation und kostenpflichtiger Support. Weniger fertige Integrationen. |
| **Timing & Mindshare** | Spring Boot 1.0 erschien 2014 – genau zu der Zeit, als Microservices, Docker und Cloud-native explodierten. Es wurde der De-facto-Standard für neue Java-Services. | Liberty startete früher (2012–2013), wurde aber immer noch als "IBMs App-Server" wahrgenommen, zu einer Zeit, als Entwickler schwergewichtige kommerzielle Server (WebSphere, WebLogic) mieden. |
| **Anbieterneutralität & Kosten** | Vollständig kostenlos und Open-Source, keine Angst vor Vendor-Lock-in. | IBM-Produkt → Wahrnehmung teurer Lizenzen (obwohl Liberty Core einen kostenlosen Tier hatte und Open Liberty vollständig Open-Source ist, trug die Marke Ballast aus der traditionellen WAS-Welt). |
| **Microservices & Cloud-Tauglichkeit** | Von Anfang an für Microservices designed; Actuatoren, Health Checks, externalisierte Konfiguration, einfache 12-Faktor-Apps. | Sehr cloud-freundlich (insbesondere Open Liberty), aber die meisten Entwickler hatten sich bereits für Spring Boot entschieden, bevor sie die Stärken von Liberty entdeckten. |
| **Marktschwung** | Um ~2018–2020 zeigten Umfragen, dass Tomcat (eingebettet in Spring Boot) einen ~60 % Anteil an Java-Laufzeitumgebungen hatte und damit alle vollständigen App-Server zusammen in den Schatten stellte. Im Jahr 2025 wird Spring Boot von >18.000 bekannten Unternehmen genutzt; traditionelle App-Server sind eine Nische. | Liberty/Open Liberty bleibt in IBM-lastigen Unternehmen und für Jakarta EE/MicroProfile beliebt, liegt aber bei Greenfield-Adoption weit zurück. |

### Wo Liberty immer noch gewinnt (Nischenfälle)
- Reine Jakarta EE / MicroProfile-Apps ohne Spring-Abhängigkeiten.
- Unternehmen, die bereits im IBM-Stack festgelegt sind (Red Hat OpenShift mit WebSphere-Lizenzen, IBM Cloud Pak).
- Optimierte Spring Boot-Deployments (Liberty kann Spring Boot-Apps in einigen Benchmarks mit kleineren Docker-Images und höherem Durchsatz ausführen als eingebetteter Tomcat).
- Regulierte Branchen, die kommerziellen Support/Zertifizierungen benötigen.

Kurz gesagt: **Liberty verlor nicht, weil es technisch unterlegen war — es verlor, weil Spring Boot eine dramatisch höhere Entwicklerproduktivität bot, im perfekten kulturellen Moment ankam und einen unaufhaltsamen Ökosystem-Schwung aufbaute.** Die meisten neuen Java-Backend-Projekte im Jahr 2025 beginnen mit Spring Boot (oder Quarkus/Helidon/Micronaut), nicht mit einem separaten Application Server.

[Spring Boot vs Websphere Liberty | What are the differences?](https://stackshare.io/stackups/spring-boot-vs-websphere-liberty)  
[2020 Java Technology Report | JRebel](https://www.jrebel.com/blog/2020-java-technology-report)  
[How does Open Liberty’s performance compare to other cloud-native Java runtimes](https://openliberty.io/blog/2022/10/17/memory-footprint-throughput-update.html)  
[Spring Boot market share data (6sense)](https://6sense.com/tech/programming-framework/spring-boot-market-share)