---
audio: false
generated: true
image: false
lang: de
layout: post
title: Lösungen für Probleme mit dem Maven Tomcat Plugin
translated: true
type: note
---

Du hast den entscheidenden Hinweis bereits in deinem eigenen Log:

> `[INFO] Skipping non-war project`

Nichts hat gestartet, weil **das tomcat7-maven-Plugin nur Webapps ausführt, die als WAR** mit der klassischen `src/main/webapp`-Struktur gepackt sind. Dein Projekt ist mit hoher Wahrscheinlichkeit derzeit als JAR gepackt, also beendet sich das Plugin einfach nach dem Build.

Es gibt noch eine zweite Falle: Du verwendest **Tomcat 11** (Jakarta `jakarta.*` APIs), aber deine Abhängigkeiten sind **Spring 5.2.x** (verwendet `javax.*`). Diese Fehlanpassung bedeutet, dass selbst wenn Tomcat starten würde, ein einfaches Deployment auf Tomcat 11 ohne Migration fehlschlagen würde. Verwende Tomcat 9 (javax) für Spring 5, oder upgrade die App auf Spring 6/Jakarta für Tomcat 10/11.

Hier sind saubere Wege, die du wählen kannst – nimm einen davon und er wird funktionieren:

### Pfad 1 — Behalte Spring 5, führe lokal mit Jetty-Plugin aus (schnellste Methode)

Kein WAR nötig; gut für Experimente.

1. Plugin hinzufügen:

   ```xml
   <plugin>
     <groupId>org.eclipse.jetty</groupId>
     <artifactId>jetty-maven-plugin</artifactId>
     <version>9.4.54.v20240208</version>
   </plugin>
   ```
2. Ausführen:

   ```bash
   mvn jetty:run -Djetty.port=8080
   ```

Dies verwendet `javax.*`, was zu Spring 5 passt.

### Pfad 2 — Behalte Spring 5, baue ein WAR und verwende das Tomcat7-Plugin

1. Im `pom.xml` WAR-Packaging setzen:

   ```xml
   <packaging>war</packaging>
   ```
2. Sicherstellen, dass die Webapp-Struktur existiert:

   ```
   src/main/webapp/
   src/main/webapp/WEB-INF/web.xml   # optional, falls du einen Servlet 3 Initializer hast
   ```
3. (Optional) Plugin-Konfiguration hinzufügen:

   ```xml
   <plugin>
     <groupId>org.apache.tomcat.maven</groupId>
     <artifactId>tomcat7-maven-plugin</artifactId>
     <version>2.2</version>
     <configuration>
       <path>/</path>
       <port>8080</port>
     </configuration>
   </plugin>
   ```
4. Ausführen:

   ```bash
   mvn tomcat7:run            # für explodierte Webapp
   # oder
   mvn package && mvn tomcat7:run-war
   ```

### Pfad 3 — Behalte Spring 5, deploye auf einen eigenständigen Tomcat 9

Dies passt zu `javax.*`, ohne Code zu ändern.

```bash
brew install tomcat@9
/opt/homebrew/opt/tomcat@9/bin/catalina start
```

Baue dein WAR und lege es in `.../tomcat@9/libexec/webapps/` ab.

### Pfad 4 — Upgrade die App auf Spring 6/Jakarta, bleibe bei Tomcat 11

Wenn du einen modernen Tomcat möchtest:

* Upgrade auf Spring Framework 6.x / Spring Boot 3.x.
* Ändere die Imports von `javax.*` zu `jakarta.*`.
* Dann ist Tomcat 10/11 in Ordnung.

---

#### Warum `mvn tomcat7:run` Erfolg meldete, aber "nichts passierte"

* Die Maven-Phasen wurden erfolgreich abgeschlossen, aber das Plugin sah **Nicht-WAR-Packaging**, also hat es **keinen eingebetteten Tomcat gestartet**. Das ist genau die Bedeutung von "Skipping non-war project".

---

Wenn du mir sagst, welchen Pfad du bevorzugst, gebe ich dir die genaue `pom.xml` und die minimalen Dateien für diesen Setup (einschließlich eines kleinen Controllers und wie man ihn unter `http://localhost:8080/hello` erreicht).