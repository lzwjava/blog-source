---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4.1-fast
title: Maven-Profile für WAS-Umgebungskonfiguration
translated: true
type: note
---

Für IBM WebSphere Application Server (traditioneller WAS, nicht Liberty) ist die Standardverpackung eine **EAR**-Datei (selbst für einfache Web-Apps, da WAS EAR gegenüber eigenständigen WAR-Dateien bevorzugt). Die beste Praxis zur Handhabung verschiedener Umgebungen – wie lokale Entwicklung (fester/hartkodierter Login-Benutzer für Tests) gegenüber Server/Produktion (SSO oder ordentlicher Security Realm) – ist die Verwendung von **Maven Build Profilen** in einer einzelnen `pom.xml`. Dies vermeidet die Pflege mehrerer separater POM-Dateien (z.B. `pom.xml` und `build_pom.xml`), was fehleranfällig und nicht idiomatisch für Maven ist.

### Warum Profile statt mehrerer POMs?
- Eine einzige Quelle der Wahrheit (einzelne POM).
- Einfache Aktivierung: `mvn package -Plocal` oder `mvn package -Pserver`.
- Profile können Ressourcen filtern, Dateien überschreiben, Plugin-Konfigurationen ändern oder Bindungen anpassen (z.B. `ibm-web-bnd.xml`, `ibm-application-ext.xml` für WAS-spezifische Authentifizierung).
- Häufig verwendet für Dev/Test/Prod-Unterschiede, einschließlich Authentifizierungskonfigurationen.

### Empfohlene Struktur
Verwenden Sie das Maven Resources Plugin mit Filterung + profilspezifischen Ressourcenverzeichnissen, um Konfigurationsdateien auszutauschen (z.B. `web.xml`, `properties`-Dateien, Spring Security Konfiguration oder WAS-Bindings).

Verzeichnisstruktur-Beispiel:
```
src/
├── main/
│   ├── resources/          (gemeinsame Konfigurationen)
│   ├── webapp/
│   │   ├── WEB-INF/
│   │   │   ├── web.xml      (gemeinsame oder Basisversion)
│   │   │   └── ibm-web-bnd.xml (optional, für JNDI/Auth-Bindings)
│   └── ...
├── local/                   (profilspezifische Ressourcen, nur für lokal kopiert/gefiltert)
│   └── webapp/
│       └── WEB-INF/
│           ├── web.xml      (lokale Version mit Form-Login + hartkodiertem Benutzer/Rolle oder ohne Sicherheit)
│           └── ...
└── server/                  (profilspezifisch für Produktion/SSO)
    └── webapp/
        └── WEB-INF/
            ├── web.xml      (Server-Version mit <login-config><auth-method>CLIENT-CERT</auth-method> oder SPNEGO für SSO)
            └── ...
```

### Beispiel pom.xml Ausschnitt
```xml
<project ...>
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.example</groupId>
    <artifactId>my-was-app</artifactId>
    <version>1.0.0</version>
    <packaging>ear</packaging>   <!-- Oder war, wenn als WAR bereitgestellt, aber EAR wird für WAS bevorzugt -->

    <properties>
        <maven.compiler.source>11</maven.compiler.source> <!-- oder Ihre Java-Version -->
        <maven.compiler.target>11</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>

    <dependencies>
        <!-- Ihre App-Abhängigkeiten -->
        <!-- Für WAS Compile-Time-APIs (provided Scope) -->
        <dependency>
            <groupId>com.ibm.tools.target</groupId>
            <artifactId>was</artifactId>
            <version>9.0</version> <!-- Passen Sie Ihre WAS-Version an, z.B. 8.5.5 oder 9.0 -->
            <type>pom</type>
            <scope>provided</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <!-- EAR erstellen (anpassen für WAR falls nötig) -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-ear-plugin</artifactId>
                <version>3.3.0</version>
                <configuration>
                    <!-- Ihre EAR-Konfiguration, Module, etc. -->
                </configuration>
            </plugin>

            <!-- Ressourcen-Filterung & profilspezifische Überschreibungen -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-resources-plugin</artifactId>
                <version>3.3.1</version>
                <configuration>
                    <useDefaultDelimiters>true</useDefaultDelimiters>
                </configuration>
            </plugin>
        </plugins>
    </build>

    <!-- Profile -->
    <profiles>
        <!-- Lokales/Dev-Profil: Fester Benutzer, Form-Login oder keine Sicherheit -->
        <profile>
            <id>local</id>
            <activation>
                <activeByDefault>true</activeByDefault> <!-- Standard für lokale Builds -->
            </activation>
            <build>
                <resources>
                    <!-- Gemeinsame Ressourcen -->
                    <resource>
                        <directory>src/main/resources</directory>
                        <filtering>true</filtering>
                    </resource>
                    <!-- Überschreiben mit lokalspezifischen Dateien -->
                    <resource>
                        <directory>src/local/webapp</directory>
                        <targetPath>${project.build.directory}/${project.artifactId}/WEB-INF</targetPath>
                    </resource>
                </resources>
            </build>
            <properties>
                <!-- Beispiel gefilterte Properties für lokalen hartkodierten Benutzer -->
                <app.login.user>devuser</app.login.user>
                <app.login.password>devpass</app.login.password>
            </properties>
        </profile>

        <!-- Server/Prod-Profil: Echt-SSO (z.B. SPNEGO, LTPA oder OpenIDConnect) -->
        <profile>
            <id>server</id>
            <build>
                <resources>
                    <resource>
                        <directory>src/main/resources</directory>
                        <filtering>true</filtering>
                    </resource>
                    <resource>
                        <directory>src/server/webapp</directory>
                        <targetPath>${project.build.directory}/${project.artifactId}/WEB-INF</targetPath>
                    </resource>
                </resources>
            </build>
            <properties>
                <!-- Prod-Properties, z.B. SSO-Flags aktivieren -->
                <app.auth.method>SSO</app.auth.method>
            </properties>
        </profile>
    </profiles>
</project>
```

### Wichtige Punkte für Authentifizierungsunterschiede
- **Lokal**: Verwenden Sie FORM-Login mit einfachen Benutzern/Rollen in `web.xml` oder einer Properties-Datei, oder deaktivieren Sie die Sicherheit vollständig (`<security-constraint>` entfernt).
- **Server**: Konfigurieren Sie WAS-spezifisches SSO in `web.xml` (z.B. `<auth-method>FORM</auth-method>` mit SPNEGO, oder verwenden Sie die OpenID Connect-Funktionalität im Liberty-Stil, aber für traditionellen WAS oft LTPA + globaler Security Realm). WAS-Bindings (`ibm-web-bnd.xml`) können ebenfalls pro Profil für Benutzer-/Rollen-Mappings überschrieben werden.
- Falls Spring Security oder ähnliches verwendet wird, tauschen Sie `applicationContext-security.xml` oder Properties auf die gleiche Weise aus.
- Für hartkodierten lokalen Benutzer: Vermeiden Sie echte hartkodierte Anmeldedaten; verwenden Sie einen Testbenutzer, der in einer lokalen `users.properties` gemappt ist, oder deaktivieren Sie die Auth-Checks über ein Flag.

### Build-Befehle
- Lokal (Standard): `mvn clean package`
- Server/Prod: `mvn clean package -Pserver`

Dies produziert unterschiedliche EARs, die für jede Umgebung aus der **gleichen Codebasis** maßgeschneidert sind. Falls Sie wirklich separate Artefaktnamen benötigen (z.B. `myapp-local.ear` vs `myapp.ear`), fügen Sie `<finalName>${project.artifactId}-${profile}</finalName>` in den profilspezifischen `<build>`-Abschnitten hinzu.

[Maven Profiles Guide](https://maven.apache.org/guides/introduction/introduction-to-profiles.html)  
[Maven EAR Plugin](https://maven.apache.org/plugins/maven-ear-plugin/)  
[IBM WAS Maven Integration](https://www.ibm.com/docs/en/wasdtfe/9.7.0?topic=suye-configuring-dependency-pom-files-that-emulate-classpath-specific-websphere-runtime-environments)