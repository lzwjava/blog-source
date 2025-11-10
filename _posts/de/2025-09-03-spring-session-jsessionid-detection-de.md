---
audio: false
generated: true
image: false
lang: de
layout: post
title: Frühlingssitzung, JSESSIONID und Servererkennung
translated: true
type: note
---

Unterteilen wir dies in zwei Teile: wie **Spring Session/JSESSIONID** funktioniert und wie man erkennt, ob Spring auf **Tomcat oder Netty** läuft.

---

## 1. Wie Spring Session und `JSESSIONID` funktionieren

* **JSESSIONID** ist der standardmäßige HTTP-Session-Identifier, der von Servlet-Containern (Tomcat, Jetty, Undertow, etc.) verwendet wird.
* Wenn ein Client die erste Anfrage stellt, die eine Session erfordert, generiert der Container (oder Spring Session, falls verwendet) eine zufällige Session-ID, speichert die Sitzungsdaten auf dem Server und sendet die ID über einen `Set-Cookie`-Header an den Client zurück.
* Der Client sendet dieses `JSESSIONID`-Cookie bei nachfolgenden Anfragen mit, damit der Server die richtige Session finden kann.
* Standardmäßig werden die Sitzungsdaten **im Arbeitsspeicher des Servlet-Containers** gespeichert. Zum Beispiel:

  * Tomcat speichert Sessions im Arbeitsspeicher (sofern keine Persistenz konfiguriert ist).
  * Wenn Sie **Spring Session** verwenden, kann die Session-Speicherung externalisiert werden (Redis, JDBC, Hazelcast, etc.), während weiterhin das `JSESSIONID`-Cookie zur Identifizierung der Benutzer dient.
* Spring Security und andere Spring-Funktionen verlassen sich auf diesen Session-Mechanismus für Authentifizierung und Zustandsverwaltung.

---

## 2. Wie man erkennt, ob Spring Tomcat oder Netty verwendet

Spring Boot kann mit verschiedenen eingebetteten Servern laufen:

* **Tomcat** (Standard für Spring Boot Starter-Web)
* **Jetty** (wenn Abhängigkeiten getauscht werden)
* **Undertow** (alternativer Servlet-Container)
* **Netty** (wird von Spring WebFlux verwendet, nicht servlet-basiert)

### Möglichkeiten zur Überprüfung:

1. **Abhängigkeiten prüfen**

   * Wenn Ihre `pom.xml` oder `build.gradle` `spring-boot-starter-web` enthält, wird standardmäßig **Tomcat** verwendet.
   * Wenn sie `spring-boot-starter-webflux` enthält, wird standardmäßig **Netty** verwendet.

2. **Startprotokolle prüfen**

   * Wenn die Anwendung startet, protokolliert Spring Boot den eingebetteten Server.
   * Beispiel (Tomcat):

     ```
     Tomcat started on port(s): 8080 (http)
     ```
   * Beispiel (Netty):

     ```
     Netty started on port(s): 8080
     ```

3. **Laufzeitklassen prüfen**

   * Über Code oder den Actuator prüfen, welche Serverklassen geladen sind.
   * Tomcat-Klassen beginnen mit `org.apache.catalina.`
   * Netty-Klassen beginnen mit `io.netty.`

---

✅ **Zusammenfassung**:

* `JSESSIONID` ist lediglich das Cookie, das auf eine serverseitige Session verweist, verwaltet von Tomcat (Standard) oder von Spring Session (Redis/DB).
* Sie können erkennen, ob Spring **Tomcat oder Netty** verwendet, indem Sie die Abhängigkeiten, Startprotokolle oder Laufzeitklassen prüfen.

---

Möchten Sie, dass ich auch erkläre, **wie sich die Session-Behandlung zwischen Spring MVC (Tomcat) und Spring WebFlux (Netty) unterscheidet**? Dort ist der Unterschied am bedeutendsten.