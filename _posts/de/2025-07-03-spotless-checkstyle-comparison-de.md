---
audio: false
generated: true
lang: de
layout: post
title: Spotless vs. Checkstyle in Java
translated: true
type: note
---

Sie können das **Spotless Maven Plugin** und das **Checkstyle Maven Plugin** zusammen in einem Java-Projekt verwenden, da sie sich gegenseitig ergänzen. Ob Sie jedoch *beide* benötigen, hängt von den Anforderungen Ihres Projekts ab. Im Folgenden werde ich erklären, wie sie zusammenarbeiten können, worin sie sich unterscheiden und wann Sie sich möglicherweise für das eine oder das andere entscheiden.

### Hauptunterschiede zwischen Spotless und Checkstyle

| **Aspekt**            | **Spotless**                                                                 | **Checkstyle**                                                              |
|-----------------------|------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| **Zweck**             | Formatiert Code automatisch, um einen einheitlichen Stil durchzusetzen und Probleme zu beheben. | Analysiert Code statisch, um Coding-Standards durchzusetzen und Verstöße zu erkennen. |
| **Aktion**            | Modifiziert Code (z. B. korrigiert Einrückungen, Importreihenfolge, entfernt ungenutzte Imports). | Meldet Verstöße ohne Code zu modifizieren; bricht den Build bei Fehlschlägen ab. |
| **Konfiguration**     | Konfiguriert Formatierer wie `palantir-java-format`, `google-java-format` usw. | Verwendet einen Regelsatz (z. B. Google- oder Sun-Checks), um Coding-Standards zu definieren. |
| **Ausgabe**           | Formatierte Quelldateien (mit `mvn spotless:apply`).                         | Berichte (XML, HTML oder Konsole), die Stilverstöße auflisten.              |
| **Anwendungsfall**    | Stellt sicher, dass Code vor Commits oder Builds konsistent formatiert ist.  | Erzwingt Coding-Standards und erkennt Probleme wie Komplexität oder schlechte Praktiken. |

### Spotless und Checkstyle zusammen verwenden

Sie können Spotless und Checkstyle kombinieren, um sowohl **automatische Formatierung** als auch **Stilprüfung** zu erreichen. So ergänzen sie sich gegenseitig:

1. **Spotless für die Formatierung**:
   - Spotless wendet Formatierungsregeln an (z. B. Einrückung, Importreihenfolge) mit Tools wie `palantir-java-format`.
   - Es stellt sicher, dass Code konsistent formatiert ist und reduziert manuellen Aufwand.
   - Beispiel: Korrigiert 2- vs. 4-Leerzeichen Einrückung, sortiert Imports und entfernt ungenutzte Imports.

2. **Checkstyle für die Validierung**:
   - Checkstyle erzwingt Coding-Standards, die über die reine Formatierung hinausgehen, wie Methodenlänge, Namenskonventionen oder Komplexität.
   - Es erkennt Probleme, die Formatierer möglicherweise nicht ansprechen, wie fehlende Javadoc oder übermäßig komplexe Methoden.
   - Beispiel: Markiert eine Methode mit zu vielen Parametern oder erzwingt Javadoc bei öffentlichen Methoden.

3. **Workflow**:
   - Führen Sie zuerst Spotless aus (`mvn spotless:apply`), um den Code zu formatieren.
   - Führen Sie dann Checkstyle aus (`mvn checkstyle:check`), um die Einhaltung zusätzlicher Regeln zu überprüfen.
   - Dies stellt sicher, dass der Code sowohl formatiert ist als auch weiteren Stilrichtlinien entspricht.

### Beispielkonfiguration in `pom.xml`

So konfigurieren Sie beide Plugins in Ihrer `pom.xml`:

```xml
<build>
    <plugins>
        <!-- Spotless Plugin für Formatierung -->
        <plugin>
            <groupId>com.diffplug.spotless</groupId>
            <artifactId>spotless-maven-plugin</artifactId>
            <version>2.43.0</version>
            <configuration>
                <java>
                    <includes>
                        <include>src/main/java/**/*.java</include>
                        <include>src/test/java/**/*.java</include>
                    </includes>
                    <palantirJavaFormat>
                        <version>2.53.0</version>
                        <style>GOOGLE</style> <!-- Google-Stil verwenden -->
                    </palantirJavaFormat>
                    <indent>
                        <spacesPerTab>2</spacesPerTab> <!-- 2-Leerzeichen Einrückung -->
                    </indent>
                    <importOrder>
                        <order>java,javax,org,com,\\#</order>
                    </importOrder>
                    <removeUnusedImports/>
                    <trimTrailingWhitespace/>
                    <endWithNewline/>
                </java>
            </configuration>
            <executions>
                <execution>
                    <goals>
                        <goal>apply</goal>
                    </goals>
                    <phase>validate</phase>
                </execution>
            </executions>
        </plugin>

        <!-- Checkstyle Plugin für Validierung -->
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-checkstyle-plugin</artifactId>
            <version>3.4.0</version>
            <configuration>
                <configLocation>google_checks.xml</configLocation> <!-- Google-Stil oder benutzerdefinierte XML verwenden -->
                <includeTestSourceDirectory>true</includeTestSourceDirectory>
                <failOnViolation>true</failOnViolation> <!-- Build bei Verstößen abbrechen -->
                <consoleOutput>true</consoleOutput> <!-- Verstöße in der Konsole ausgeben -->
            </configuration>
            <executions>
                <execution>
                    <goals>
                        <goal>check</goal>
                    </goals>
                    <phase>validate</phase>
                </execution>
            </executions>
            <dependencies>
                <!-- Checkstyle-Version angeben -->
                <dependency>
                    <groupId>com.puppycrawl.tools</groupId>
                    <artifactId>checkstyle</artifactId>
                    <version>10.17.0</version>
                </dependency>
            </dependencies>
        </plugin>
    </plugins>
</build>
```

### Wichtige Konfigurationshinweise

1. **Gemeinsame Stilregeln**:
   - Um Konflikte zu vermeiden, sollten Sie die Spotless- und Checkstyle-Konfigurationen abstimmen. Verwenden Sie beispielsweise `palantirJavaFormat` mit `style>GOOGLE` in Spotless und `google_checks.xml` in Checkstyle.
   - Laden Sie `google_checks.xml` von [Checkstyle’s GitHub](https://github.com/checkstyle/checkstyle/blob/master/src/main/resources/google_checks.xml) herunter oder erstellen Sie einen benutzerdefinierten Regelsatz.

2. **Ausführungsreihenfolge**:
   - Führen Sie Spotless vor Checkstyle in der `validate`-Phase aus, um sicherzustellen, dass der Code vor der Validierung formatiert ist.
   - Beispiel: `mvn spotless:apply checkstyle:check`.

3. **Benutzerdefinierte Checkstyle-Regeln**:
   - Passen Sie `google_checks.xml` an oder erstellen Sie Ihre eigene (z. B. `my_checks.xml`), um spezifische Regeln durchzusetzen, wie z. B.:
     ```xml
     <module name="Indentation">
         <property name="basicOffset" value="2"/>
         <property name="lineWrappingIndentation" value="4"/>
     </module>
     <module name="ImportOrder">
         <property name="groups" value="java,javax,org,com"/>
         <property name="ordered" value="true"/>
         <property name="separated" value="true"/>
     </module>
     ```

4. **Redundanz vermeiden**:
   - Wenn Spotless die Formatierung übernimmt (z. B. Einrückung, Importreihenfolge), deaktivieren Sie überlappende Checkstyle-Regeln, um doppelte Prüfungen zu vermeiden. Deaktivieren Sie beispielsweise das `Indentation`-Modul von Checkstyle, wenn Spotless die Einrückung erzwingt:
     ```xml
     <module name="Indentation">
         <property name="severity" value="ignore"/>
     </module>
     ```

### Wann man eines vs. beide verwendet

- **Nur Spotless verwenden**:
  - Wenn Sie nur konsistente Code-Formatierung benötigen (z. B. Einrückung, Importreihenfolge, Leerzeichen).
  - Ideal für Teams, die automatisierte Formatierung ohne strenge Stilprüfung wünschen.
  - Beispiel: Kleine Projekte oder Teams mit IDE-basierter Formatierung.

- **Nur Checkstyle verwenden**:
  - Wenn Sie Coding-Standards durchsetzen müssen (z. B. Namenskonventionen, Javadoc, Methodenkomplexität) ohne Code zu modifizieren.
  - Geeignet für Projekte, bei denen Entwickler Code manuell formatieren, aber Validierung benötigen.

- **Beide verwenden**:
  - Für robuste Code-Qualität: Spotless formatiert Code automatisch und Checkstyle erkennt zusätzliche Probleme (z. B. fehlendes Javadoc, komplexe Methoden).
  - Üblich in großen Teams oder Projekten mit strengen Coding-Standards.
  - Beispiel: Enterprise-Projekte oder Open-Source-Repositories, die konsistenten Stil und Qualitätsprüfungen erfordern.

### Praktische Überlegungen

- **Performance**: Das Ausführen beider Plugins erhöht die Build-Zeit. Verwenden Sie `spotless:check` (anstelle von `apply`) und `checkstyle:check` in CI-Pipelines, um ohne Code-Modifikation zu validieren.
- **IDE-Integration**:
  - Spotless: Verwenden Sie die Spotless Gradle/Maven Tasks oder IDE-Plugins (z. B. `palantir-java-format` für IntelliJ).
  - Checkstyle: Verwenden Sie das Checkstyle-IDEA Plugin für IntelliJ oder das Eclipse Checkstyle Plugin, konfiguriert mit der gleichen `google_checks.xml`.
- **CI/CD**: Konfigurieren Sie beide Plugins in Ihrer CI-Pipeline (z. B. Jenkins, GitHub Actions), um Formatierungs- und Stilprüfungen bei Pull Requests durchzusetzen.
  ```yaml
  # Beispiel GitHub Actions Workflow
  name: CI
  on: [pull_request]
  jobs:
    build:
      runs-on: ubuntu-latest
      steps:
        - uses: actions/checkout@v3
        - name: Set up JDK 17
          uses: actions/setup-java@v3
          with: { java-version: '17' }
        - name: Run Spotless and Checkstyle
          run: mvn spotless:check checkstyle:check
  ```

### Mögliche Konflikte und Lösungen

- **Überlappende Regeln**: Wenn Spotless Code anders formatiert als Checkstyle-Regeln (z. B. 2- vs. 4-Leerzeichen Einrückung), können Builds fehlschlagen. Lösung: Konfigurationen abstimmen (z. B. `GOOGLE`-Stil für beide verwenden).
- **Build-Fehler**: Checkstyles `failOnViolation` kann Builds abbrechen, wenn Spotless nicht gelaufen ist. Lösung: Sicherstellen, dass Spotless zuerst läuft oder `spotless:check` zur Validierung der Formatierung verwenden.
- **Team-Akzeptanz**: Entwickler könnten sich gegen automatische Formatierung sträuben. Lösung: Verwenden Sie `spotless:check` in CI und schulen Sie das Team in der IDE-Integration.

### Quellen

- Spotless-Dokumentation: [GitHub](https://github.com/diffplug/spotless/tree/main/plugin-maven)
- Checkstyle Maven Plugin: [Maven Site](https://maven.apache.org/plugins/maven-checkstyle-plugin/)
- Community-Diskussionen auf Stack Overflow und GitHub Issues

### Fazit

Die gemeinsame Verwendung von Spotless und Checkstyle ist eine leistungsstarke Kombination zur Aufrechterhaltung der Code-Qualität: Spotless sorgt für konsistente Formatierung, während Checkstyle breitere Coding-Standards durchsetzt. Konfigurieren Sie sie so, dass sie übereinstimmen (z. B. gleiche Einrückungs- und Importreihenfolgen-Regeln) und führen Sie sie sequentiell in Ihrem Build-Prozess aus. Wenn Ihr Projekt nur Formatierung benötigt, reicht möglicherweise Spotless allein aus; wenn Sie strenge Validierung benötigen, ziehen Sie die Hinzufügung von Checkstyle in Betracht. Lassen Sie mich wissen, wenn Sie Hilfe bei spezifischen Konfigurationen oder einer Beispiel-`google_checks.xml`-Datei benötigen!