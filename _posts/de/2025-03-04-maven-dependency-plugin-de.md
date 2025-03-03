---
audio: false
generated: true
lang: de
layout: post
title: Maven Abhängigkeits-Plugin
translated: true
---

Das **Maven Dependency Plugin** ist ein leistungsfähiges Werkzeug in Maven, einem weit verbreiteten Build-Automatisierungstool für Java-Projekte, das Ihnen hilft, Abhängigkeiten zu verwalten und zu manipulieren. Abhängigkeiten in einem Maven-Projekt sind externe Bibliotheken oder Module, die in der `pom.xml`-Datei deklariert werden, die Maven aus Repositories herunterlädt und während der Kompilierung, Laufzeit oder des Testens verfügbar macht. Das Dependency Plugin erweitert diese Funktionalität, indem es verschiedene Ziele (Aufgaben) bereitstellt, um diese Abhängigkeiten zu analysieren, zu kopieren, aufzulisten oder anderweitig zu verwalten. Hier erfahren Sie, wie Sie es effektiv nutzen können:

---

#### **1. Überblick über die Verwendung**
Sie können das Maven Dependency Plugin auf zwei Hauptweisen verwenden:
- **Konfigurieren Sie es in der `pom.xml`-Datei**: Dies ermöglicht es Ihnen, spezifische Plugin-Ziele an Phasen des Maven-Build-Lebenszyklus (z. B. `package`, `install`) zu binden, um eine automatische Ausführung während des Build-Prozesses zu gewährleisten.
- **Führen Sie Ziele direkt von der Befehlszeile aus**: Dies ist ideal für Einmalaufgaben oder wenn Sie die `pom.xml` nicht ändern möchten.

Das Plugin wird durch seine Koordinaten identifiziert: `groupId: org.apache.maven.plugins`, `artifactId: maven-dependency-plugin`. Sie müssen eine Version (z. B. `3.2.0`) angeben, wenn Sie es konfigurieren, obwohl Maven die neueste Version oft auflösen kann, wenn sie in der Befehlszeilenverwendung weggelassen wird.

---

#### **2. Hinzufügen des Plugins zu `pom.xml`**
Um das Plugin als Teil Ihres Build-Prozesses zu verwenden, fügen Sie es dem Abschnitt `<build><plugins>` Ihrer `pom.xml` hinzu. Hier ist ein grundlegendes Beispiel:

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-dependency-plugin</artifactId>
            <version>3.2.0</version>
        </plugin>
    </plugins>
</build>
```

Mit dieser Einrichtung können Sie spezifische Ziele konfigurieren, die während des Build-Lebenszyklus ausgeführt werden sollen, indem Sie `<executions>`-Blöcke hinzufügen.

---

#### **3. Häufige Ziele und deren Verwendung**
Das Plugin bietet mehrere Ziele zur Verwaltung von Abhängigkeiten. Hier sind einige der am häufigsten verwendeten Ziele, zusammen mit Beispielen zu deren Verwendung:

##### **a. `copy-dependencies`**
- **Zweck**: Kopiert Projektabhängigkeiten in ein angegebenes Verzeichnis (z. B. zum Verpacken in einen `lib`-Ordner).
- **In `pom.xml` konfiguriert**:
  Binden Sie dieses Ziel an die `package`-Phase, um Abhängigkeiten während `mvn package` zu kopieren:

  ```xml
  <build>
      <plugins>
          <plugin>
              <groupId>org.apache.maven.plugins</groupId>
              <artifactId>maven-dependency-plugin</artifactId>
              <version>3.2.0</version>
              <executions>
                  <execution>
                      <id>copy-dependencies</id>
                      <phase>package</phase>
                      <goals>
                          <goal>copy-dependencies</goal>
                      </goals>
                      <configuration>
                          <outputDirectory>${project.build.directory}/lib</outputDirectory>
                          <includeScope>runtime</includeScope>
                      </configuration>
                  </execution>
              </executions>
          </plugin>
      </plugins>
  </build>
  ```

  - `${project.build.directory}/lib` wird zu `target/lib` in Ihrem Projekt aufgelöst.
  - `<includeScope>runtime</includeScope>` begrenzt das Kopieren auf Abhängigkeiten mit den Bereichen `compile` und `runtime`, ausschließend `test` und `provided`.

- **Befehlszeile**:
  Führen Sie es direkt aus, ohne die `pom.xml` zu ändern:

  ```bash
  mvn dependency:copy-dependencies -DoutputDirectory=lib
  ```

##### **b. `tree`**
- **Zweck**: Zeigt den Abhängigkeitsbaum an, der alle direkten und transitiven Abhängigkeiten und deren Versionen zeigt. Dies ist nützlich, um Versionskonflikte zu identifizieren.
- **Befehlszeile**:
  Führen Sie einfach aus:

  ```bash
  mvn dependency:tree
  ```

  Dies gibt eine hierarchische Ansicht der Abhängigkeiten in der Konsole aus.
- **In `pom.xml` konfiguriert** (optional):
  Wenn Sie dies während einer Build-Phase (z. B. `verify`) ausführen möchten, konfigurieren Sie es ähnlich wie `copy-dependencies`.

##### **c. `analyze`**
- **Zweck**: Analysiert Abhängigkeiten, um Probleme zu identifizieren, wie:
  - Verwendete, aber nicht deklarierte Abhängigkeiten.
  - Deklarierte, aber nicht verwendete Abhängigkeiten.
- **Befehlszeile**:
  Führen Sie aus:

  ```bash
  mvn dependency:analyze
  ```

  Dies erzeugt einen Bericht in der Konsole.
- **Hinweis**: Dieses Ziel kann für komplexe Projekte zusätzliche Konfigurationen erfordern, um seine Analyse zu verfeinern.

##### **d. `list`**
- **Zweck**: Listet alle aufgelösten Abhängigkeiten des Projekts auf.
- **Befehlszeile**:
  Führen Sie aus:

  ```bash
  mvn dependency:list
  ```

  Dies bietet eine flache Liste von Abhängigkeiten, die für einen schnellen Bezug nützlich ist.

##### **e. `unpack`**
- **Zweck**: Extrahiert den Inhalt einer bestimmten Abhängigkeit (z. B. einer JAR-Datei) in ein Verzeichnis.
- **Befehlszeile**:
  Beispiel zum Extrahieren einer bestimmten Artefakt:

  ```bash
  mvn dependency:unpack -Dartifact=groupId:artifactId:version -DoutputDirectory=target/unpacked
  ```

  Ersetzen Sie `groupId:artifactId:version` durch die Koordinaten der Abhängigkeit (z. B. `org.apache.commons:commons-lang3:3.12.0`).

##### **f. `purge-local-repository`**
- **Zweck**: Entfernt bestimmte Abhängigkeiten aus Ihrem lokalen Maven-Repository (`~/.m2/repository`), wodurch ein frischer Download aus Remote-Repositories erzwungen wird.
- **Befehlszeile**:
  Führen Sie aus:

  ```bash
  mvn dependency:purge-local-repository
  ```

  Dies ist hilfreich, um beschädigte Abhängigkeitsdateien zu beheben.

---

#### **4. Anpassungsoptionen**
Viele Ziele unterstützen Konfigurationsparameter, um ihr Verhalten anzupassen:
- **`outputDirectory`**: Gibt an, wohin Dateien kopiert oder extrahiert werden sollen (z. B. `target/lib`).
- **`includeScope` oder `excludeScope`**: Filtert Abhängigkeiten nach Bereich (z. B. `runtime`, `test`).
- **`artifact`**: Zielt eine bestimmte Abhängigkeit für Ziele wie `unpack` an.

Diese können im Abschnitt `<configuration>` der `pom.xml` oder als Befehlszeilenargumente mit `-D` (z. B. `-DincludeScope=runtime`) festgelegt werden.

---

#### **5. Praktische Beispiele**
- **Szenario 1: Verpacken einer eigenständigen Anwendung**
  Verwenden Sie `copy-dependencies`, um alle Laufzeitabhängigkeiten in einen `lib`-Ordner zu sammeln:

  ```bash
  mvn dependency:copy-dependencies -DoutputDirectory=lib -DincludeScope=runtime
  ```

- **Szenario 2: Debuggen von Abhängigkeitskonflikten**
  Führen Sie `dependency:tree` aus, um transitive Abhängigkeiten zu inspizieren:

  ```bash
  mvn dependency:tree
  ```

  Wenn Sie mehrere Versionen einer Bibliothek (z. B. `commons-logging`) erkennen, lösen Sie den Konflikt, indem Sie einen `<dependencyManagement>`-Abschnitt in der `pom.xml` hinzufügen.

- **Szenario 3: Extrahieren von Ressourcen**
  Packen Sie eine Abhängigkeit aus, um auf deren Inhalte zuzugreifen:

  ```bash
  mvn dependency:unpack -Dartifact=org.example:my-lib:1.0.0 -DoutputDirectory=target/resources
  ```

---

#### **6. Zusammenfassung**
Um das Maven Dependency Plugin zu verwenden:
- Fügen Sie es Ihrer `pom.xml` mit spezifischen Zielen und Konfigurationen hinzu, wenn Sie es in Ihren Build-Prozess integrieren möchten.
- Führen Sie Ziele wie `copy-dependencies`, `tree`, `analyze`, `list` oder `unpack` direkt von der Befehlszeile aus für Ad-hoc-Aufgaben aus.
- Passen Sie das Verhalten mit Konfigurationsoptionen an, um den Bedürfnissen Ihres Projekts gerecht zu werden.

Dieses Plugin ist ein vielseitiges Werkzeug zur Verwaltung von Abhängigkeiten über einfache Deklarationen hinaus, was es unverzichtbar für das Bauen, Debuggen und Verteilen von Maven-Projekten macht.