---
audio: false
generated: true
lang: de
layout: post
title: Maven Dependency Plugin
translated: true
type: note
---

Das **Maven Dependency Plugin** ist ein leistungsfähiges Werkzeug in Maven, einem weit verbreiteten Build-Automatisierungstool für Java-Projekte, das Ihnen hilft, Projektabhängigkeiten zu verwalten und zu manipulieren. Abhängigkeiten in einem Maven-Projekt sind externe Bibliotheken oder Module, die in der `pom.xml`-Datei deklariert sind. Maven lädt diese aus Repositories herunter und stellt sie während der Kompilierung, Laufzeit oder Tests zur Verfügung. Das Dependency Plugin erweitert diese Funktionalität, indem es verschiedene Goals (Aufgaben) bereitstellt, um diese Abhängigkeiten zu analysieren, zu kopieren, aufzulisten oder anderweitig zu handhaben. So können Sie es effektiv nutzen:

---

#### **1. Überblick zur Verwendung**
Sie können das Maven Dependency Plugin auf zwei primäre Arten verwenden:
- **Konfigurieren in der `pom.xml`-Datei**: Dies ermöglicht es Ihnen, spezifische Plugin-Goals an Phasen des Maven Build-Lifecycles (z.B. `package`, `install`) zu binden, um sie während des Build-Prozesses automatisch ausführen zu lassen.
- **Goals direkt über die Kommandozeile ausführen**: Dies ist ideal für einmalige Aufgaben oder wenn Sie die `pom.xml` nicht modifizieren möchten.

Das Plugin wird durch seine Koordinaten identifiziert: `groupId: org.apache.maven.plugins`, `artifactId: maven-dependency-plugin`. Sie müssen eine Version (z.B. `3.2.0`) bei der Konfiguration angeben, obwohl Maven oft die neueste Version auflösen kann, wenn sie in der Kommandozeilenverwendung weggelassen wird.

---

#### **2. Hinzufügen des Plugins zur `pom.xml`**
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

Mit diesem Setup können Sie spezifische Goals konfigurieren, die während des Build-Lifecycles ausgeführt werden sollen, indem Sie `<executions>`-Blöcke hinzufügen.

---

#### **3. Häufig verwendete Goals und ihre Verwendung**
Das Plugin bietet mehrere Goals zur Verwaltung von Abhängigkeiten. Nachfolgend sind einige der am häufigsten verwendeten aufgeführt, zusammen mit Beispielen für ihre Verwendung:

##### **a. `copy-dependencies`**
- **Zweck**: Kopiert Projektabhängigkeiten in ein bestimmtes Verzeichnis (z.B. für die Paketierung in einen `lib`-Ordner).
- **Konfiguriert in `pom.xml`**:
  Binden Sie dieses Goal an die `package`-Phase, um Abhängigkeiten während `mvn package` zu kopieren:

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

  - `${project.build.directory}/lib` wird in Ihrem Projekt zu `target/lib` aufgelöst.
  - `<includeScope>runtime</includeScope>` beschränkt das Kopieren auf Abhängigkeiten mit `compile`- und `runtime`-Scopes und schließt `test` und `provided` aus.

- **Kommandozeile**:
  Führen Sie es direkt aus, ohne die `pom.xml` zu modifizieren:

  ```bash
  mvn dependency:copy-dependencies -DoutputDirectory=lib
  ```

##### **b. `tree`**
- **Zweck**: Zeigt den Abhängigkeitsbaum an, der alle direkten und transitiven Abhängigkeiten sowie ihre Versionen anzeigt. Dies ist nützlich, um Versionskonflikte zu identifizieren.
- **Kommandozeile**:
  Führen Sie einfach aus:

  ```bash
  mvn dependency:tree
  ```

  Dies gibt eine hierarchische Ansicht der Abhängigkeiten in der Konsole aus.
- **Konfiguriert in `pom.xml`** (optional):
  Wenn Sie möchten, dass dies während einer Build-Phase (z.B. `verify`) läuft, konfigurieren Sie es ähnlich wie `copy-dependencies`.

##### **c. `analyze`**
- **Zweck**: Analysiert Abhängigkeiten, um Probleme zu identifizieren, wie z.B.:
  - Verwendete, aber nicht deklarierte Abhängigkeiten.
  - Deklarierte, aber ungenutzte Abhängigkeiten.
- **Kommandozeile**:
  Führen Sie aus:

  ```bash
  mvn dependency:analyze
  ```

  Dies erzeugt einen Bericht in der Konsole.
- **Hinweis**: Dieses Goal erfordert möglicherweise zusätzliche Konfiguration für komplexe Projekte, um seine Analyse zu verfeinern.

##### **d. `list`**
- **Zweck**: Listet alle aufgelösten Abhängigkeiten des Projekts auf.
- **Kommandozeile**:
  Führen Sie aus:

  ```bash
  mvn dependency:list
  ```

  Dies liefert eine flache Liste der Abhängigkeiten, nützlich für einen schnellen Überblick.

##### **e. `unpack`**
- **Zweck**: Extrahiert den Inhalt einer spezifischen Abhängigkeit (z.B. einer JAR-Datei) in ein Verzeichnis.
- **Kommandozeile**:
  Beispiel zum Entpacken eines bestimmten Artifacts:

  ```bash
  mvn dependency:unpack -Dartifact=groupId:artifactId:version -DoutputDirectory=target/unpacked
  ```

  Ersetzen Sie `groupId:artifactId:version` durch die Koordinaten der Abhängigkeit (z.B. `org.apache.commons:commons-lang3:3.12.0`).

##### **f. `purge-local-repository`**
- **Zweck**: Entfernt bestimmte Abhängigkeiten aus Ihrem lokalen Maven-Repository (`~/.m2/repository`), um einen erneuten Download aus Remote-Repositories zu erzwingen.
- **Kommandozeile**:
  Führen Sie aus:

  ```bash
  mvn dependency:purge-local-repository
  ```

  Dies ist hilfreich zur Fehlerbehebung bei korrupten Abhängigkeitsdateien.

---

#### **4. Anpassungsoptionen**
Viele Goals unterstützen Konfigurationsparameter, um ihr Verhalten anzupassen:
- **`outputDirectory`**: Gibt an, wohin Dateien kopiert oder entpackt werden sollen (z.B. `target/lib`).
- **`includeScope` oder `excludeScope`**: Filtert Abhängigkeiten nach Scope (z.B. `runtime`, `test`).
- **`artifact`**: Ziel eine spezifische Abhängigkeit für Goals wie `unpack` an.

Diese können im `<configuration>`-Abschnitt der `pom.xml` gesetzt oder als Kommandozeilenargumente mit `-D` übergeben werden (z.B. `-DincludeScope=runtime`).

---

#### **5. Praktische Beispiele**
- **Szenario 1: Paketierung einer eigenständigen Anwendung**
  Verwenden Sie `copy-dependencies`, um alle Laufzeitabhängigkeiten in einem `lib`-Ordner zu sammeln:

  ```bash
  mvn dependency:copy-dependencies -DoutputDirectory=lib -DincludeScope=runtime
  ```

- **Szenario 2: Debugging von Abhängigkeitskonflikten**
  Führen Sie `dependency:tree` aus, um transitive Abhängigkeiten zu inspizieren:

  ```bash
  mvn dependency:tree
  ```

  Wenn Sie mehrere Versionen einer Bibliothek (z.B. `commons-logging`) entdecken, lösen Sie den Konflikt, indem Sie einen `<dependencyManagement>`-Abschnitt in der `pom.xml` hinzufügen.

- **Szenario 3: Extrahieren von Ressourcen**
  Entpacken Sie eine Abhängigkeit, um auf deren Inhalte zuzugreifen:

  ```bash
  mvn dependency:unpack -Dartifact=org.example:my-lib:1.0.0 -DoutputDirectory=target/resources
  ```

---

#### **6. Zusammenfassung**
So verwenden Sie das Maven Dependency Plugin:
- Fügen Sie es Ihrer `pom.xml` mit spezifischen Goals und Konfigurationen hinzu, wenn Sie es in Ihren Build-Prozess integrieren möchten.
- Führen Sie Goals wie `copy-dependencies`, `tree`, `analyze`, `list` oder `unpack` direkt von der Kommandozeile für Ad-hoc-Aufgaben aus.
- Passen Sie das Verhalten mit Konfigurationsoptionen an die Bedürfnisse Ihres Projekts an.

Dieses Plugin ist ein vielseitiges Werkzeug zur Verwaltung von Abhängigkeiten über die einfache Deklaration hinaus und macht es unverzichtbar für das Erstellen, Debuggen und Verteilen von Maven-Projekten.