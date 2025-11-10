---
audio: false
generated: true
lang: de
layout: post
title: Konfiguriere Palantir Java Format mit Spotless
translated: true
type: note
---

Um den **Palantir Java Format** mit dem **Spotless Maven Plugin** in einer `pom.xml`-Datei zu konfigurieren, müssen Sie das Plugin so einrichten, dass es `palantirJavaFormat` verwendet und Formatierungsoptionen wie Tabspace, Einrückung, Importreihenfolge und andere Einstellungen angibt. Im Folgenden finden Sie eine detaillierte Anleitung zur Konfiguration dieser Einstellungen und der verfügbaren Optionen basierend auf dem Spotless Plugin und Palantir Java Format.

### Hinzufügen des Spotless Maven Plugins mit Palantir Java Format

Fügen Sie das Spotless Maven Plugin in Ihre `pom.xml` ein und konfigurieren Sie es für die Verwendung von `palantirJavaFormat`. Hier ist ein grundlegender Setup mit gängigen Konfigurationen für Tabspace, Einrückung, Importreihenfolge und andere Optionen:

```xml
<plugin>
    <groupId>com.diffplug.spotless</groupId>
    <artifactId>spotless-maven-plugin</artifactId>
    <version>2.43.0</version> <!-- Verwenden Sie die neueste Version -->
    <configuration>
        <java>
            <!-- Dateien zur Formatierung angeben (optional, standardmäßig alle .java-Dateien) -->
            <includes>
                <include>src/main/java/**/*.java</include>
                <include>src/test/java/**/*.java</include>
            </includes>
            <!-- Palantir Java Format -->
            <palantirJavaFormat>
                <version>2.53.0</version> <!-- Gewünschte Version angeben -->
                <style>GOOGLE</style> <!-- Optionen: GOOGLE, AOSP oder PALANTIR -->
                <formatJavadoc>true</formatJavadoc> <!-- Optional: Javadoc formatieren -->
            </palantirJavaFormat>
            <!-- Einrückungseinstellungen -->
            <indent>
                <tabs>true</tabs> <!-- Tabs anstelle von Leerzeichen verwenden -->
                <spacesPerTab>4</spacesPerTab> <!-- Anzahl der Leerzeichen pro Tab -->
            </indent>
            <!-- Importreihenfolge konfigurieren -->
            <importOrder>
                <order>java,javax,org,com,\\#</order> <!-- Benutzerdefinierte Importreihenfolge -->
            </importOrder>
            <!-- Nicht verwendete Imports entfernen -->
            <removeUnusedImports/>
            <!-- Andere optionale Einstellungen -->
            <trimTrailingWhitespace/>
            <endWithNewline/>
            <toggleOffOn/> <!-- Aktiviert spotless:off und spotless:on Tags -->
        </java>
    </configuration>
    <executions>
        <execution>
            <goals>
                <goal>apply</goal> <!-- Code automatisch formatieren -->
            </goals>
            <phase>validate</phase> <!-- Während der Validate-Phase ausführen -->
        </execution>
    </executions>
</plugin>
```

### Erklärung der Konfigurationsoptionen

Hier ist eine Aufschlüsselung der wichtigsten Konfigurationsoptionen für den `java`-Abschnitt in Spotless mit `palantirJavaFormat`, mit Fokus auf Tabspace, Einrückung, Importreihenfolge und anderen relevanten Einstellungen:

#### 1. **Palantir Java Format (`<palantirJavaFormat>`)**

- **`<version>`**: Gibt die Version von `palantir-java-format` an, die verwendet werden soll. Überprüfen Sie die neueste Version im [Maven Repository](https://mvnrepository.com/artifact/com.palantir.java-format/palantir-java-format) oder auf [GitHub](https://github.com/palantir/palantir-java-format/releases). Beispiel: `<version>2.53.0</version>`.
- **`<style>`**: Definiert den Formatierungsstil. Optionen sind:
  - `GOOGLE`: Verwendet Google Java Style (2 Leerzeichen Einrückung, 100-Zeichen Zeilenlimit).
  - `AOSP`: Verwendet Android Open Source Project Style (4 Leerzeichen Einrückung, 100-Zeichen Zeilenlimit).
  - `PALANTIR`: Verwendet Palantirs Stil (4 Leerzeichen Einrückung, 120-Zeichen Zeilenlimit, Lambda-freundliche Formatierung).[](https://github.com/palantir/palantir-java-format)
- **`<formatJavadoc>`**: Boolean zum Aktivieren/Deaktivieren der Javadoc-Formatierung (erfordert Palantir Java Format Version ≥ 2.39.0). Beispiel: `<formatJavadoc>true</formatJavadoc>`.[](https://github.com/diffplug/spotless/blob/main/plugin-gradle/README.md)
- **Benutzerdefinierte Group Artifact**: Selten benötigt, aber Sie können eine benutzerdefinierte Group und Artifact für den Formatter angeben. Beispiel: `<groupArtifact>com.palantir.java-format:palantir-java-format</groupArtifact>`.

#### 2. **Einrückung (`<indent>`)**

- **`<tabs>`**: Boolean, um Tabs (`true`) oder Leerzeichen (`false`) für die Einrückung zu verwenden. Beispiel: `<tabs>true</tabs>`.[](https://dev.to/ankityadav33/standardize-code-formatting-with-spotless-2bdh)
- **`<spacesPerTab>`**: Anzahl der Leerzeichen pro Tab (wird verwendet, wenn `<tabs>` `false` ist oder für gemischte Einrückung). Übliche Werte sind `2` oder `4`. Beispiel: `<spacesPerTab>4</spacesPerTab>`.[](https://dev.to/ankityadav33/standardize-code-formatting-with-spotless-2bdh)
  - **Hinweis**: Der Stil von Palantir Java Format (z.B. `GOOGLE`, `AOSP`, `PALANTIR`) kann das Einrückungsverhalten beeinflussen. Zum Beispiel verwendet `GOOGLE` standardmäßig 2 Leerzeichen, während `AOSP` und `PALANTIR` 4 Leerzeichen verwenden. Die `<indent>`-Einstellungen in Spotless können diese Standardwerte überschreiben oder ergänzen, aber stellen Sie Konsistenz sicher, um Konflikte zu vermeiden.[](https://stackoverflow.com/questions/50027892/override-google-java-format-with-spotless-maven-plugin)

#### 3. **Importreihenfolge (`<importOrder>`)**

- **`<order>`**: Gibt die Reihenfolge der Importgruppen an, durch Kommas getrennt. Verwenden Sie `\\#` für statische Imports und einen leeren String (`""`) für nicht spezifizierte Imports. Beispiel: `<order>java,javax,org,com,\\#</order>` sortiert Imports, die mit `java` beginnen, dann `javax`, usw., mit statischen Imports zuletzt.[](https://stackoverflow.com/questions/71339562/spotless-java-google-format-vs-intellij-import-file)
- **`<file>`**: Alternativ können Sie eine Datei angeben, die die Importreihenfolge enthält. Beispiel: `<file>${project.basedir}/eclipse.importorder</file>`. Das Dateiformat entspricht der Importreihenfolge-Konfiguration von Eclipse (z.B. `java|javax|org|com|\\#`).[](https://stackoverflow.com/questions/71339562/spotless-java-google-format-vs-intellij-import-file)
  - Beispielhafter Dateiinhalt:
    ```
    #sort
    java
    javax
    org
    com
    \#
    ```

#### 4. **Andere nützliche Einstellungen**

- **`<removeUnusedImports>`**: Entfernt nicht verwendete Imports. Optional kann die Engine angegeben werden:
  - Standard: Verwendet `google-java-format` für die Entfernung.
  - Alternative: `<engine>cleanthat-javaparser-unnecessaryimport</engine>` für JDK8+ Kompatibilität mit neueren Java-Features (z.B. Java 17).[](https://stackoverflow.com/questions/77126927/spotless-eclipse-formatter-java-17-error-on-string-literals-removing-unu)
- **`<trimTrailingWhitespace>`**: Entfernt nachgestellte Leerzeichen von Zeilen. Beispiel: `<trimTrailingWhitespace/>`.[](https://dev.to/ankityadav33/standardize-code-formatting-with-spotless-2bdh)
- **`<endWithNewline>`**: Stellt sicher, dass Dateien mit einer neuen Zeile enden. Beispiel: `<endWithNewline/>`.[](https://dev.to/ankityadav33/standardize-code-formatting-with-spotless-2bdh)
- **`<toggleOffOn>`**: Aktiviert `// spotless:off` und `// spotless:on` Kommentare, um Codeabschnitte von der Formatierung auszuschließen. Beispiel: `<toggleOffOn/>`.[](https://dev.to/ankityadav33/standardize-code-formatting-with-spotless-2bdh)
- **`<licenseHeader>`**: Fügt eine Lizenzheader zu Dateien hinzu. Beispiel:
  ```xml
  <licenseHeader>
      <content>/* (C) $YEAR */</content>
  </licenseHeader>
  ```
  Sie können auch eine Datei verwenden: `<file>${project.basedir}/license.txt</file>`.[](https://www.baeldung.com/java-maven-spotless-plugin)
- **`<formatAnnotations>`**: Stellt sicher, dass Typ-Annotationen in derselben Zeile wie die Felder stehen, die sie beschreiben. Beispiel: `<formatAnnotations/>`.[](https://www.baeldung.com/java-maven-spotless-plugin)
- **`<ratchetFrom>`**: Beschränkt die Formatierung auf Dateien, die relativ zu einem Git-Branch geändert wurden (z.B. `origin/main`). Beispiel: `<ratchetFrom>origin/main</ratchetFrom>`.[](https://github.com/diffplug/spotless/blob/main/plugin-maven/README.md)

#### 5. **POM-spezifische Formatierung (`<pom>`)**

Um die `pom.xml`-Datei selbst zu formatieren, verwenden Sie den `<pom>`-Abschnitt mit `sortPom`:
```xml
<pom>
    <sortPom>
        <nrOfIndentSpace>2</nrOfIndentSpace> <!-- Einrückung für POM -->
        <predefinedSortOrder>recommended_2008_06</predefinedSortOrder> <!-- Standard POM Reihenfolge -->
        <sortDependencies>groupId,artifactId</sortDependencies> <!-- Dependencies sortieren -->
        <sortPlugins>groupId,artifactId</sortPlugins> <!-- Plugins sortieren -->
        <endWithNewline>true</endWithNewline>
    </sortPom>
</pom>
```
- **Optionen für `sortPom`**:
  - `<nrOfIndentSpace>`: Anzahl der Leerzeichen für die Einrückung (z.B. `2` oder `4`).
  - `<predefinedSortOrder>`: Optionen wie `recommended_2008_06` oder `custom_1` für die Elementreihenfolge.[](https://github.com/diffplug/spotless/blob/main/plugin-gradle/README.md)
  - `<sortDependencies>`: Sortieren nach `groupId`, `artifactId` oder anderen Kriterien.
  - `<sortPlugins>`: Plugins ähnlich sortieren.
  - `<endWithNewline>`: Sicherstellen, dass POM mit einer neuen Zeile endet.
  - `<expandEmptyElements>`: Leere XML-Tags erweitern (z.B. `<tag></tag>` vs `<tag/>`).[](https://github.com/diffplug/spotless/blob/main/plugin-gradle/README.md)

### Ausführen von Spotless

- **Formatierung prüfen**: `mvn spotless:check` – Validiert den Code anhand der konfigurierten Regeln und lässt den Build fehlschlagen, wenn Verstöße gefunden werden.
- **Formatierung anwenden**: `mvn spotless:apply` – Formatiert den Code automatisch, um den Regeln zu entsprechen.

### Hinweise und Best Practices

- **Konsistenz mit der IDE**: Um IntelliJ oder Eclipse mit Spotless abzugleichen, installieren Sie das `palantir-java-format` IntelliJ Plugin oder verwenden Sie eine Eclipse Formatter XML-Datei. Für IntelliJ importieren Sie eine kompatible Stildatei (z.B. `intellij-java-google-style.xml` für Google Style) oder konfigurieren Sie manuell, um die Palantir-Einstellungen zu entsprechen.[](https://plugins.jetbrains.com/plugin/13180-palantir-java-format)
- **Versionskompatibilität**: Stellen Sie sicher, dass die `palantir-java-format` Version Ihre Java-Version unterstützt. Für Java 17+ verwenden Sie eine aktuelle Version (z.B. 2.53.0). Einige Features wie Pattern Matching haben möglicherweise eingeschränkte Unterstützung.[](https://www.reddit.com/r/java/comments/1g8zu8c/codestyle_and_formatters/)
- **Benutzerdefinierte Formatierung**: Für erweiterte Anpassungen verwenden Sie eine Eclipse Formatter XML-Datei mit `<eclipse>` anstelle von `<palantirJavaFormat>`:
  ```xml
  <eclipse>
      <file>${project.basedir}/custom-style.xml</file>
  </eclipse>
  ```
  Beispiel `custom-style.xml`:
  ```xml
  <?xml version="1.0" encoding="utf-8"?>
  <profiles version="21">
      <profile kind="CodeFormatterProfile" name="custom" version="21">
          <setting id="org.eclipse.jdt.core.formatter.tabulation.char" value="space"/>
          <setting id="org.eclipse.jdt.core.formatter.indentation.size" value="4"/>
          <setting id="org.eclipse.jdt.core.formatter.tabulation.size" value="4"/>
      </profile>
  </profiles>
  ```
  [](https://www.baeldung.com/java-maven-spotless-plugin)
- **Einschränkungen**: Palantir Java Format ist weniger konfigurierbar als Eclipses Formatter, ist aber für Konsistenz und moderne Java-Features (z.B. Lambdas) konzipiert. Es behandelt möglicherweise nicht alle Grenzfälle (z.B. tief verschachtelte Lambdas).[](https://www.reddit.com/r/java/comments/18z151f/strict_code_formatter/)

### Zusammenfassung der verfügbaren Optionen

| **Option**                  | **Beschreibung**                                                                 | **Beispielwerte**                              |
|-----------------------------|---------------------------------------------------------------------------------|------------------------------------------------|
| `<palantirJavaFormat>`      | Konfiguriert Palantir Java Format.                                                | `<version>2.53.0</version>`, `<style>PALANTIR</style>` |
| `<indent>`                  | Legt Einrückungsstil (Tabs oder Leerzeichen) und Größe fest.                               | `<tabs>true</tabs>`, `<spacesPerTab>4</spacesPerTab>` |
| `<importOrder>`             | Definiert die Reihenfolge der Importgruppen oder verwendet eine Datei.                                      | `<order>java,javax,org,com,\\#</order>`        |
| `<removeUnusedImports>`     | Entfernt nicht verwendete Imports, mit optionaler Engine.                                   | `<engine>cleanthat-javaparser-unnecessaryimport</engine>` |
| `<trimTrailingWhitespace>`  | Entfernt nachgestellte Leerzeichen.                                                   | `<trimTrailingWhitespace/>`                    |
| `<endWithNewline>`         | Stellt sicher, dass Dateien mit einer neuen Zeile enden.                                              | `<endWithNewline/>`                           |
| `<toggleOffOn>`            | Aktiviert `spotless:off`/`spotless:on` Tags.                                     | `<toggleOffOn/>`                              |
| `<licenseHeader>`          | Fügt einen Lizenzheader hinzu.                                                         | `<content>/* (C) $YEAR */</content>`           |
| `<formatAnnotations>`       | Formatiert Annotationen, um in derselben Zeile wie Felder zu stehen.                          | `<formatAnnotations/>`                         |
| `<sortPom>`                | Formatiert `pom.xml` mit Sortierung und Einrückung.                                | `<nrOfIndentSpace>2</nrOfIndentSpace>`        |

### Quellen

- Spotless Maven Plugin Dokumentation: [GitHub](https://github.com/diffplug/spotless/tree/main/plugin-maven)[](https://github.com/diffplug/spotless/blob/main/plugin-maven/README.md)
- Palantir Java Format: [GitHub](https://github.com/palantir/palantir-java-format)[](https://github.com/palantir/palantir-java-format)
- Stack Overflow und Community-Beispiele für Spotless-Konfiguration[](https://stackoverflow.com/questions/50027892/override-google-java-format-with-spotless-maven-plugin)[](https://stackoverflow.com/questions/71339562/spotless-java-google-format-vs-intellij-import-file)[](https://stackoverflow.com/questions/77126927/spotless-eclipse-formatter-java-17-error-on-string-literals-removing-unu)

Diese Konfiguration stellt eine konsistente Codeformatierung mit Palantir Java Format sicher, angepasst an Ihre Präferenzen für Tabspace, Einrückung und Importreihenfolge. Lassen Sie mich wissen, wenn Sie weitere Erklärungen oder zusätzliche Optionen benötigen!