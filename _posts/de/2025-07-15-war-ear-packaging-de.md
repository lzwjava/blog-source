---
audio: false
generated: true
image: false
lang: de
layout: post
title: Krieg vs Ohr Verpackungsleitfaden
translated: true
type: note
---

Hier ist ein praktischer Vergleich von Maven **WAR**- vs. **EAR**-Packaging ohne Tabellen und wie Sie jedes in realen Projekten verwenden würden.

# Wofür jedes Packaging gedacht ist

* **WAR (`packaging: war`)** – Eine einzelne Webanwendung: Servlets/Jakarta REST, JSP/JSF, Spring MVC/Boot (als WAR), etc. Wird in einem Servlet-Container (Tomcat/Jetty) oder dem Web-Tier eines vollständigen App-Servers deployed.
* **EAR (`packaging: ear`)** – Ein Bundle aus mehreren Modulen, die zusammen auf einem vollständigen Java EE/Jakarta EE App-Server (WildFly/JBoss EAP, WebLogic, WebSphere) deployed werden. Enthält typischerweise ein oder mehrere WARs, EJB-JARs und gemeinsame Bibliotheken in einer Deployment-Einheit.

# Typische Auswahlkriterien

* Wählen Sie **WAR**, wenn Sie eine einzelne Web-App oder Spring Boot-App haben und keine EJBs oder Multi-Modul-Server-Features benötigen.
* Wählen Sie **EAR**, wenn Sie mehrere Module zusammen deployen müssen (z.B. EJBs + mehrere WARs + gemeinsame Bibliotheken), App-Server-Services (XA, zentralisierte Security Realms, JMS, verteilte Transaktionen) über Module hinweg benötigen oder Ihre Organisation EARs vorschreibt.

# Was sich im Artefakt befindet

* **WAR**-Inhalte: `/WEB-INF/classes`, `/WEB-INF/lib`, optional `web.xml` (oder Annotationen), statische Assets. Ein Classloader pro WAR in den meisten Servern.
* **EAR**-Inhalte: `*.war`, `*.jar` (EJBs/Utility), `META-INF/application.xml` (oder Annotationen/Skinny-Config), und optional `lib/` für Bibliotheken, die über Module hinweg geteilt werden. Bietet einen EAR-level Classloader, der für alle Module sichtbar ist.

# Abhängigkeiten & Classloading-Überlegungen

* **WAR**: Deklarieren Sie Servlet/Jakarta EE APIs als `provided`; alles andere gehört unter `/WEB-INF/lib`. Isolation ist einfacher; weniger Versionskonflikte.
* **EAR**: Legen Sie gemeinsame Bibliotheken in das `lib/`-Verzeichnis des EARs (via `maven-ear-plugin`), sodass alle Module eine Version teilen. Achten Sie auf Konflikte zwischen Modul-Bibliotheken und serverbereitgestellten APIs; passen Sie Versionen an und verwenden Sie `provided`, wo angebracht.

# Maven-Plugins, die Sie verwenden werden

* **WAR-Projekte**: `maven-war-plugin`
* **EAR-Aggregator**: `maven-ear-plugin`
* **EJB-Module (falls vorhanden)**: `maven-ejb-plugin`
* Parent/Aggregator verwendet oft `packaging: pom`, um Module zusammenzufassen.

# Minimale Beispiele

Einzelne Webanwendung (WAR):

```xml
<!-- pom.xml -->
<project>
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.example</groupId><artifactId>my-web</artifactId><version>1.0.0</version>
  <packaging>war</packaging>

  <dependencies>
    <!-- Use provided for server APIs -->
    <dependency>
      <groupId>jakarta.platform</groupId><artifactId>jakarta.jakartaee-web-api</artifactId>
      <version>10.0.0</version><scope>provided</scope>
    </dependency>
    <!-- Your app deps -->
  </dependencies>

  <build>
    <plugins>
      <plugin>
        <artifactId>maven-war-plugin</artifactId>
        <version>3.4.0</version>
        <!-- Optional: configure webResources, warName, filtering -->
      </plugin>
    </plugins>
  </build>
</project>
```

Multi-Modul-EAR mit einem WAR und einem EJB:

```xml
<!-- parent/pom.xml -->
<project>
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.example</groupId><artifactId>my-app</artifactId><version>1.0.0</version>
  <packaging>pom</packaging>
  <modules>
    <module>ejb-module</module>
    <module>web-module</module>
    <module>ear-assembly</module>
  </modules>
</project>
```

```xml
<!-- ejb-module/pom.xml -->
<project>
  <parent>…</parent>
  <artifactId>ejb-module</artifactId>
  <packaging>ejb</packaging>
  <dependencies>
    <dependency>
      <groupId>jakarta.platform</groupId><artifactId>jakarta.jakartaee-api</artifactId>
      <version>10.0.0</version><scope>provided</scope>
    </dependency>
  </dependencies>
</project>
```

```xml
<!-- web-module/pom.xml -->
<project>
  <parent>…</parent>
  <artifactId>web-module</artifactId>
  <packaging>war</packaging>
  <dependencies>
    <dependency>
      <groupId>jakarta.platform</groupId><artifactId>jakarta.jakartaee-web-api</artifactId>
      <version>10.0.0</version><scope>provided</scope>
    </dependency>
    <dependency>
      <groupId>com.example</groupId><artifactId>ejb-module</artifactId><version>1.0.0</version>
      <type>ejb</type> <!-- allows @EJB injection -->
    </dependency>
  </dependencies>
</project>
```

```xml
<!-- ear-assembly/pom.xml -->
<project>
  <parent>…</parent>
  <artifactId>ear-assembly</artifactId>
  <packaging>ear</packaging>

  <dependencies>
    <dependency>
      <groupId>com.example</groupId><artifactId>web-module</artifactId><version>1.0.0</version>
      <type>war</type>
    </dependency>
    <dependency>
      <groupId>com.example</groupId><artifactId>ejb-module</artifactId><version>1.0.0</version>
      <type>ejb</type>
    </dependency>
    <!-- Libraries to put in EAR/lib shared by all modules -->
    <dependency>
      <groupId>com.fasterxml.jackson.core</groupId><artifactId>jackson-databind</artifactId>
      <version>2.17.2</version>
    </dependency>
  </dependencies>

  <build>
    <plugins>
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-ear-plugin</artifactId>
        <version>3.4.0</version>
        <configuration>
          <defaultLibBundleDir>lib</defaultLibBundleDir>
          <modules>
            <webModule>
              <groupId>com.example</groupId>
              <artifactId>web-module</artifactId>
              <contextRoot>/myapp</contextRoot>
            </webModule>
            <ejbModule>
              <groupId>com.example</groupId>
              <artifactId>ejb-module</artifactId>
            </ejbModule>
          </modules>
          <!-- Optional: generate application.xml, or provide a custom one -->
          <generateApplicationXml>true</generateApplicationXml>
        </configuration>
      </plugin>
    </plugins>
  </build>
</project>
```

Build-Ergebnisse:

* `mvn -pl web-module -am clean package` → `web-module-1.0.0.war`
* `mvn -pl ear-assembly -am clean package` → `ear-assembly-1.0.0.ear` enthält das WAR, EJB und `lib/`.

# Betriebliche Unterschiede, die wichtig sind

* **Deployment-Ziel**

  * WAR: Servlet-Container oder App-Server-Web-Tier.
  * EAR: Vollständiger App-Server; deployed alle Module atomar.
* **Transaktionen & Messaging**

  * WAR allein verwendet das, was der Container bereitstellt; komplexe XA/JMS-Setups befinden sich oft in EJBs innerhalb von EARs.
* **Versionierung & Rollout**

  * WAR: Einfach eine einzelne App neu zu bauen und zu deployen.
  * EAR: Koordiniert Versionen vieler Module; eine Deployment-Einheit für Konsistenz.
* **Startzeit & lokale Entwicklung**

  * WAR: Schnelles Feedback, leichtgewichtige Laufzeit.
  * EAR: Schwergewichtiger; IDE/Server-Integration hilft, aber Zyklen sind langsamer.
* **Moderne Spring Boot-Notiz**

  * Boot bevorzugt ausführbare **JAR**s; WAR wird unterstützt, wenn Sie in einem externen Container deployen.
  * Boot zielt **nicht** auf EAR ab; wenn Sie einen App-Server verwenden müssen, deployen Sie Boot als WAR und vermeiden Sie EAR, es sei denn, Ihre Plattform erfordert es.

# Häufige Fallstricke & Tipps

* Verwenden Sie `provided` für Server-APIs, um das Bundling zu vermeiden.
* Für EARs: Legen Sie gemeinsame Bibliotheken in `defaultLibBundleDir`, um doppelte Kopien in jedem WAR/EJB zu vermeiden.
* Passen Sie Jakarta-EE-Versionen über Module hinweg an; Fehlanpassungen verursachen Classloading-Fehler.
* Auf WebLogic/WebSphere: Achten Sie auf Classloader-Richtlinien (Parent-First vs. Parent-Last); manchmal benötigen Sie vendorspezifische Descriptoren.
* Wenn Sie keine EJBs/XA benötigen, ist ein einfaches WAR (oder Boot-JAR) einfacher und meist portabler.

Wenn Sie mir Ihren App-Server (Tomcat vs. WildFly/WebLogic/etc.) mitteilen und ob Sie EJBs oder mehrere Web-Apps haben, kann ich die genauen POMs und Deployment-Deskriptoren skizzieren, die Sie benötigen.