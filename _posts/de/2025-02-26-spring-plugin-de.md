---
audio: false
generated: true
lang: de
layout: post
title: Spring Boot Maven Plugin
translated: true
type: note
---

Um den `spring-boot-maven-plugin` in einem Maven-basierten Spring Boot-Projekt zu verwenden, befolgen Sie diese Schritte, um das Plugin für das Erstellen, Ausführen und Verwalten Ihrer Anwendung zu konfigurieren und zu nutzen. Nachfolgend finden Sie eine umfassende Anleitung:

---

### **1. Stellen Sie sicher, dass Ihr Projekt ein Spring Boot-Projekt ist**
Bevor Sie den `spring-boot-maven-plugin` verwenden, vergewissern Sie sich, dass Ihr Projekt als Spring Boot-Projekt eingerichtet ist. Dies umfasst typischerweise:

- **Ableiten von `spring-boot-starter-parent` (Empfohlen)**:
  - Setzen Sie in Ihrer `pom.xml` `spring-boot-starter-parent` als Parent, um Spring Boot-Abhängigkeiten und Plugin-Versionen zu verwalten.
  - Beispiel:
    ```xml
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.5.4</version> <!-- Ersetzen Sie dies durch Ihre Spring Boot-Version -->
        <relativePath/> <!-- Parent aus Repository suchen -->
    </parent>
    ```

- **Alternativ: Verwenden der `spring-boot-dependencies` BOM (Bill of Materials)**:
  - Wenn Sie `spring-boot-starter-parent` nicht verwenden können, importieren Sie die `spring-boot-dependencies` BOM im `dependencyManagement`-Abschnitt.
  - Beispiel:
    ```xml
    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-dependencies</artifactId>
                <version>2.5.4</version> <!-- Ersetzen Sie dies durch Ihre Spring Boot-Version -->
                <type>pom</type>
                <scope>import</scope>
            </dependency>
        </dependencies>
    </dependencyManagement>
    ```

Die Verwendung von `spring-boot-starter-parent` wird der Einfachheit halber empfohlen, da es Plugin-Versionen automatisch verwaltet.

---

### **2. Fügen Sie den `spring-boot-maven-plugin` zu Ihrer `pom.xml` hinzu**
Um das Plugin zu verwenden, müssen Sie es im `<build><plugins>`-Abschnitt Ihrer `pom.xml` deklarieren.

- **Bei Verwendung von `spring-boot-starter-parent`**:
  - Fügen Sie das Plugin hinzu, ohne die Version anzugeben, da sie vom Parent verwaltet wird.
  - Beispiel:
    ```xml
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>
    ```

- **Bei Nichtverwendung von `spring-boot-starter-parent`**:
  - Geben Sie die Version explizit an, entsprechend der verwendeten Spring Boot-Version.
  - Beispiel:
    ```xml
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <version>2.5.4</version> <!-- Ersetzen Sie dies durch Ihre Spring Boot-Version -->
            </plugin>
        </plugins>
    </build>
    ```

---

### **3. Nutzen Sie die Plugin-Goals**
Der `spring-boot-maven-plugin` bietet mehrere Goals, die Ihnen beim Erstellen, Ausführen und Verwalten Ihrer Spring Boot-Anwendung helfen. Nachfolgend sind die am häufigsten verwendeten Goals aufgeführt:

- **`spring-boot:run`**
  - Führt Ihre Spring Boot-Anwendung direkt aus Maven heraus unter Verwendung eines eingebetteten Webservers (z.B. Tomcat) aus.
  - Nützlich für Entwicklung und Tests.
  - Befehl:
    ```
    mvn spring-boot:run
    ```

- **`spring-boot:repackage`**
  - Verpackt die durch `mvn package` generierte JAR- oder WAR-Datei in eine ausführbare "Fat JAR" oder WAR um, die alle Abhängigkeiten enthält.
  - Dieses Goal wird automatisch während der `package`-Phase ausgeführt, wenn das Plugin konfiguriert ist.
  - Befehl:
    ```
    mvn package
    ```
  - Nach der Ausführung können Sie die Anwendung starten mit:
    ```
    java -jar target/meineapp.jar
    ```

- **`spring-boot:start` und `spring-boot:stop`**
  - Werden für Integrationstests verwendet, um die Anwendung während der `pre-integration-test`- bzw. `post-integration-test`-Phasen zu starten und zu stoppen.
  - Beispiel:
    ```
    mvn spring-boot:start
    mvn spring-boot:stop
    ```

- **`spring-boot:build-info`**
  - Erzeugt eine `build-info.properties`-Datei, die Build-Informationen enthält (z.B. Build-Zeit, Version).
  - Auf diese Informationen kann in Ihrer Anwendung über Spring Boots `BuildProperties`-Bean oder `@Value`-Annotations zugegriffen werden.
  - Befehl:
    ```
    mvn spring-boot:build-info
    ```

---

### **4. Passen Sie die Plugin-Konfiguration an (Optional)**
Sie können das Verhalten des `spring-boot-maven-plugin` anpassen, indem Sie Konfigurationsoptionen in der `pom.xml` hinzufügen. Nachfolgend sind einige gängige Anpassungen aufgeführt:

- **Hauptklasse angeben**:
  - Wenn das Plugin die Hauptklasse nicht automatisch erkennen kann, geben Sie sie manuell an.
  - Beispiel:
    ```xml
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <configuration>
                    <mainClass>com.example.MyApplication</mainClass>
                </configuration>
            </plugin>
        </plugins>
    </build>
    ```

- **Abhängigkeiten von der Fat JAR ausschließen**:
  - Schließen Sie Abhängigkeiten aus, die von der Laufzeitumgebung bereitgestellt werden (z.B. ein externer Servlet-Container).
  - Beispiel:
    ```xml
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <configuration>
                    <excludes>
                        <exclude>
                            <groupId>com.example</groupId>
                            <artifactId>some-dependency</artifactId>
                        </exclude>
                    </excludes>
                </configuration>
            </plugin>
        </plugins>
    </build>
    ```

- **Anwendungsargumente setzen**:
  - Konfigurieren Sie Argumente, die an die Anwendung übergeben werden sollen, wenn sie mit `spring-boot:run` ausgeführt wird.
  - Beispiel in `pom.xml`:
    ```xml
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <configuration>
                    <arguments>
                        <argument>--server.port=8081</argument>
                    </arguments>
                </configuration>
            </plugin>
        </plugins>
    </build>
    ```
  - Alternativ können Sie Argumente über die Kommandozeile übergeben:
    ```
    mvn spring-boot:run -Dspring-boot.run.arguments=--server.port=8081
    ```

- **Erstellen von WAR-Dateien**:
  - Wenn Sie eine WAR-Datei für die Bereitstellung in einem externen Servlet-Container erstellen, stellen Sie sicher, dass die Projekt-Packaging-Einstellung in `pom.xml` auf `war` gesetzt ist:
    ```xml
    <packaging>war</packaging>
    ```
  - Möglicherweise müssen Sie auch eingebettete Servlet-Container (z.B. Tomcat) ausschließen, wenn sie von der Umgebung bereitgestellt werden. Fügen Sie die folgende Abhängigkeit als `provided` hinzu:
    ```xml
    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-tomcat</artifactId>
            <scope>provided</scope>
        </dependency>
    </dependencies>
    ```

---

### **5. Wichtige Hinweise**
- **Standardverhalten**:
  - Wenn Sie `mvn package` ausführen, packt das Plugin die JAR/WAR während der `package`-Phase automatisch neu, um sie ausführbar zu machen.
  - Das neu verpackte Artefakt ist das Hauptartefakt, und die ursprüngliche JAR/WAR wird mit einem Klassifikator (z.B. `original`) angehängt.

- **Entwicklungs-Workflow**:
  - Verwenden Sie `mvn spring-boot:run` für schnelle Entwicklung und Tests.
  - Verwenden Sie `mvn package`, um eine bereitstellbare, ausführbare JAR oder WAR zu erstellen.

- **Integrationstests**:
  - Verwenden Sie `spring-boot:start` und `spring-boot:stop`, um den Anwendungslebenszyklus während der Integrationstests zu verwalten.

---

### **Zusammenfassung**
So verwenden Sie den `spring-boot-maven-plugin`:
1. Stellen Sie sicher, dass Ihr Projekt ein Spring Boot-Projekt ist, typischerweise durch Ableiten von `spring-boot-starter-parent` oder Verwenden der `spring-boot-dependencies` BOM.
2. Fügen Sie das Plugin dem `<build><plugins>`-Abschnitt Ihrer `pom.xml` hinzu.
3. Verwenden Sie Maven-Befehle wie:
   - `mvn spring-boot:run` zum Ausführen der Anwendung.
   - `mvn package` zum Erstellen einer ausführbaren JAR/WAR.
   - Andere Goals wie `spring-boot:start`, `spring-boot:stop` und `spring-boot:build-info` nach Bedarf.
4. Passen Sie optional die Konfiguration des Plugins in `pom.xml` für erweiterte Anwendungsfälle an.

Dieses Setup ermöglicht es Ihnen, Spring Boot-Anwendungen effizient mit Maven zu erstellen, auszuführen und zu verwalten.