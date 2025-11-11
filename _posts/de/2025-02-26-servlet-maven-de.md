---
audio: false
generated: true
lang: de
layout: post
title: Java Servlet-Anwendung mit Maven
translated: true
type: note
---

Hier ist eine vollständige Anleitung zum Erstellen und Bereitstellen einer einfachen Java Servlet-Anwendung auf WebSphere Liberty Profile (WLP) unter Verwendung von Maven für den Projektbuild und des Liberty Maven Plugins für die Bereitstellung. Dieses Beispiel erstellt ein grundlegendes Servlet, das bei Aufruf "Hello World!" zurückgibt, baut es mit Maven in eine WAR-Datei und stellt es auf WLP bereit. Wir gehen davon aus, dass Sie WLP bereits mit der aktivierten `servlet-4.0`-Funktion eingerichtet haben, da diese die notwendige Servlet-Unterstützung bereitstellt.

---

## Schritt-für-Schritt-Anleitung

### 1. Erstellen der Maven-Projektstruktur
Beginnen Sie mit dem Aufbau einer standardmäßigen Maven-Webanwendungsstruktur. Sie können diese manuell erstellen oder Maven zur Generierung verwenden.

- **Verzeichnisstruktur:**
  ```
  SimpleServletApp/
  ├── pom.xml
  └── src/
      └── main/
          ├── java/
          │   └── com/
          │       └── example/
          │           └── HelloServlet.java
          └── webapp/
              └── WEB-INF/
                  └── web.xml
  ```

- **Optional mit Maven generieren:**
  Führen Sie diesen Befehl aus, um die Struktur zu erstellen, und passen Sie sie dann bei Bedarf an:
  ```bash
  mvn archetype:generate -DgroupId=com.example -DartifactId=simple-servlet-app -DarchetypeArtifactId=maven-archetype-webapp -DinteractiveMode=false
  ```
  Dies erstellt eine grundlegende Webapp-Struktur, die Sie in den nächsten Schritten anpassen werden.

### 2. Schreiben des Servlet-Codes
Erstellen Sie eine Datei namens `HelloServlet.java` in `src/main/java/com/example/` mit folgendem Inhalt:

```java
package com.example;

import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

public class HelloServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws IOException {
        resp.setContentType("text/plain");
        resp.getWriter().write("Hello World!");
    }
}
```

- **Erklärung:** Dieses Servlet antwortet auf HTTP-GET-Anfragen mit "Hello World!" im Klartext. Es verwendet eine einfache `doGet`-Methode und vermeidet Annotationen für Kompatibilität mit der expliziten `web.xml`-Konfiguration.

### 3. Erstellen des `web.xml`-Bereitstellungsdeskriptors
Erstellen Sie eine Datei namens `web.xml` in `src/main/webapp/WEB-INF/` mit folgendem Inhalt:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
         version="4.0">
    <servlet>
        <servlet-name>HelloServlet</servlet-name>
        <servlet-class>com.example.HelloServlet</servlet-class>
    </servlet>
    <servlet-mapping>
        <servlet-name>HelloServlet</servlet-name>
        <url-pattern>/hello</url-pattern>
    </servlet-mapping>
</web-app>
```

- **Erklärung:** Die `web.xml`-Datei definiert die `HelloServlet`-Klasse und weist sie dem URL-Muster `/hello` zu. Dies ist notwendig, da wir keine `@WebServlet`-Annotationen verwenden.

### 4. Konfigurieren der Maven `pom.xml`
Erstellen oder aktualisieren Sie `pom.xml` im Verzeichnis `SimpleServletApp/` mit folgendem Inhalt:

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.example</groupId>
    <artifactId>simple-servlet-app</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>war</packaging>

    <properties>
        <maven.compiler.source>1.8</maven.compiler.source>
        <maven.compiler.target>1.8</maven.compiler.target>
    </properties>

    <dependencies>
        <!-- Servlet API (provided by WLP) -->
        <dependency>
            <groupId>javax.servlet</groupId>
            <artifactId>javax.servlet-api</artifactId>
            <version>4.0.1</version>
            <scope>provided</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <!-- Maven WAR Plugin to build the WAR file -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-war-plugin</artifactId>
                <version>3.3.1</version>
                <configuration>
                    <finalName>myapp</finalName>
                </configuration>
            </plugin>
            <!-- Liberty Maven Plugin for deployment -->
            <plugin>
                <groupId>io.openliberty.tools</groupId>
                <artifactId>liberty-maven-plugin</artifactId>
                <version>3.3.4</version>
                <configuration>
                    <installDirectory>/opt/ibm/wlp</installDirectory>
                    <serverName>myServer</serverName>
                    <appsDirectory>dropins</appsDirectory>
                    <looseApplication>false</looseApplication>
                    <stripVersion>true</stripVersion>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```

- **Erklärung:**
  - **Koordinaten:** Definiert das Projekt mit `groupId`, `artifactId` und `version`. Die `packaging` ist auf `war` für eine Webanwendung gesetzt.
  - **Properties:** Setzt Java 8 als Quell- und Zielversion.
  - **Dependencies:** Beinhaltet die Servlet-API mit `provided`-Scope, da sie zur Laufzeit von WLP bereitgestellt wird.
  - **Maven WAR Plugin:** Konfiguriert den WAR-Dateinamen auf `myapp.war` mittels `<finalName>`.
  - **Liberty Maven Plugin:** Konfiguriert die Bereitstellung auf einem Liberty-Server unter `/opt/ibm/wlp`, Servername `myServer`, Bereitstellung im `dropins`-Verzeichnis.

### 5. Bauen des Projekts
Führen Sie aus dem Verzeichnis `SimpleServletApp/` den Build der WAR-Datei mit Maven durch:

```bash
mvn clean package
```

- **Ergebnis:** Dies kompiliert das Servlet, verpackt es mit `web.xml` in `target/myapp.war` und bereitet es für die Bereitstellung vor.

### 6. Bereitstellen und Ausführen auf WebSphere Liberty
Stellen Sie sicher, dass Ihr Liberty-Server (`myServer`) mit der aktivierten `servlet-4.0`-Funktion eingerichtet ist. Überprüfen Sie Ihre `server.xml` auf:
```xml
<featureManager>
    <feature>servlet-4.0</feature>
</featureManager>
```

Stellen Sie die Anwendung bereit und führen Sie sie mit dem Liberty Maven Plugin aus:

```bash
mvn liberty:run
```

- **Was passiert:**
  - Startet den Liberty-Server im Vordergrund (falls nicht bereits laufend).
  - Stellt `myapp.war` automatisch im `dropins`-Verzeichnis bereit.
  - Hält den Server laufend, bis er gestoppt wird.

- **Bereitstellung überprüfen:** Suchen Sie nach einer Log-Meldung wie:
  ```
  [AUDIT   ] CWWKT0016I: Web application available (default_host): http://localhost:9080/myapp/
  ```
  Logs befinden sich typischerweise in `/opt/ibm/wlp/usr/servers/myServer/logs/console.log`.

### 7. Auf die Anwendung zugreifen
Öffnen Sie einen Browser und navigieren Sie zu:

```
http://localhost:9080/myapp/hello
```

- **Erwartete Ausgabe:**
  ```
  Hello World!
  ```

- **URL-Aufschlüsselung:**
  - `9080`: Standard-HTTP-Port für WLP.
  - `/myapp`: Kontext-Root vom WAR-Dateinamen (`myapp.war`).
  - `/hello`: URL-Muster aus `web.xml`.

### 8. Server stoppen
Da `mvn liberty:run` den Server im Vordergrund ausführt, stoppen Sie ihn durch Drücken von `Strg+C` im Terminal.

---

## Hinweise
- **Voraussetzungen:**
  - Maven muss auf Ihrem System installiert und konfiguriert sein.
  - Liberty muss unter `/opt/ibm/wlp` installiert sein, und die Serverinstanz `myServer` muss existieren. Passen Sie `installDirectory` und `serverName` in `pom.xml` an, falls Ihr Setup abweicht (z.B. `/usr/local/wlp` oder `defaultServer`).
  - Die `servlet-4.0`-Funktion muss in `server.xml` aktiviert sein.

- **Alternative Bereitstellung:**
  - Um separat zu bauen und bereitzustellen:
    ```bash
    mvn clean package
    mvn liberty:deploy
    ```
    Starten Sie den Server bei Bedarf manuell:
    ```bash
    /opt/ibm/wlp/bin/server start myServer
    ```

- **Port-Konfiguration:** Wenn Ihr Liberty-Server einen anderen HTTP-Port verwendet, überprüfen Sie `server.xml` auf `<httpEndpoint>` und passen Sie die URL entsprechend an.

- **Kontext-Root:** Benennen Sie `<finalName>` in `pom.xml` um (z.B. `<finalName>app</finalName>`), um den Kontext-Root auf `/app` zu ändern.

- **Fehlerbehebung:**
  - Wenn die Bereitstellung fehlschlägt, überprüfen Sie `installDirectory` und `serverName` in `pom.xml`.
  - Überprüfen Sie die Logs unter `/opt/ibm/wlp/usr/servers/myServer/logs/messages.log` auf Fehler.
  - Stellen Sie sicher, dass Java 8 oder höher verwendet wird, entsprechend den `maven.compiler`-Einstellungen.

---

## Zusammenfassung
Diese Anleitung demonstriert, wie man:
1. Ein Maven-Projekt mit einem einfachen Servlet (`HelloServlet.java`) und `web.xml` einrichtet.
2. `pom.xml` mit der Servlet-API, dem Maven WAR Plugin und dem Liberty Maven Plugin konfiguriert.
3. Die Anwendung mit `mvn clean package` in `myapp.war` baut.
4. Sie auf WLP mit `mvn liberty:run` bereitstellt und ausführt.
5. "Hello World!" unter `http://localhost:9080/myapp/hello` aufruft.

Dies bietet einen optimierten, Maven-basierten Ansatz zur Entwicklung und Bereitstellung einer Servlet-Anwendung auf WebSphere Liberty Profile.

---