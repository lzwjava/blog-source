---
audio: false
generated: true
lang: de
layout: post
title: Checkstyle-Konfigurationsspeicherort
translated: true
type: note
---

Um die Probleme zu beheben, die du mit dem `maven-checkstyle-plugin` beim Ausführen von `mvn clean checkstyle:check` hast, bei denen es die `checks.xml`-Datei nicht findet und das Modul `SuppressWithNearbyTextFilter` nicht initialisieren kann, folge diesen Schritten. Die Probleme rühren vom Dateispeicherort und einer inkompatiblen Checkstyle-Version her. Hier ist eine vollständige Lösung:

---

### Schritt 1: Behebe den Dateispeicherort von `checks.xml`
Der Fehler zeigt an, dass das Plugin `checks.xml` nicht finden kann. Da sie sich im Projektstammverzeichnis befindet (nicht in `src/main/resources`, wo das Plugin typischerweise sucht), musst du dem Plugin explizit mitteilen, wo es zu finden ist.

- **Aktion**: Aktualisiere die `<configLocation>` in deiner `pom.xml`, damit sie auf das Projektstammverzeichnis zeigt.

---

### Schritt 2: Behebe den `SuppressWithNearbyTextFilter`-Fehler
Das Modul `SuppressWithNearbyTextFilter` kann nicht initialisiert werden, weil die vom Plugin verwendete Checkstyle-Version veraltet ist und diesen Filter nicht unterstützt. Du musst das Plugin upgraden und eine kompatible Checkstyle-Version angeben.

- **Aktion**: Upgrade das `maven-checkstyle-plugin` auf Version `3.3.1` und füge eine Abhängigkeit zur Checkstyle-Version `10.17.0` hinzu, die `SuppressWithNearbyTextFilter` unterstützt.

---

### Aktualisierte `pom.xml`-Konfiguration
Ändere den `maven-checkstyle-plugin`-Abschnitt in deiner `pom.xml` wie folgt:

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-checkstyle-plugin</artifactId>
    <version>3.3.1</version> <!-- Auf die neueste Version upgraden -->
    <configuration>
        <configLocation>${project.basedir}/checks.xml</configLocation> <!-- Zeigt auf checks.xml im Projektstammverzeichnis -->
    </configuration>
    <dependencies>
        <dependency>
            <groupId>com.puppycrawl.tools</groupId>
            <artifactId>checkstyle</artifactId>
            <version>10.17.0</version> <!-- Unterstützt SuppressWithNearbyTextFilter -->
        </dependency>
    </dependencies>
    <executions>
        <execution>
            <id>checkstyle-check</id>
            <phase>compile</phase>
            <goals>
                <goal>check</goal>
            </goals>
        </execution>
    </executions>
</plugin>
```

#### Erklärung:
- **`<configLocation>${project.basedir}/checks.xml</configLocation>`**: Gibt an, dass sich `checks.xml` im Projektstammverzeichnis befindet (`${project.basedir}` ist eine Maven-Property für das Stammverzeichnis).
- **`version 3.3.1`**: Verwendet eine neuere Plugin-Version für bessere Kompatibilität.
- **Checkstyle `10.17.0` dependency**: Stellt sicher, dass das Plugin eine Checkstyle-Version verwendet, die `SuppressWithNearbyTextFilter` enthält.

---

### Schritt 3: Überprüfe die `checks.xml`-Konfiguration
Stelle sicher, dass das Modul `SuppressWithNearbyTextFilter` in deiner `checks.xml` korrekt definiert ist. Eine Beispielkonfiguration könnte so aussehen:

```xml
<module name="SuppressWithNearbyTextFilter">
    <property name="nearbyTextPattern" value="@SuppressWarnings"/>
</module>
```

- **Aktion**: Überprüfe `checks.xml` auf Tippfehler oder falsche Properties. Siehe die [Checkstyle-Dokumentation](https://checkstyle.org/filters/suppresswithnearbytextfilter.html) für Details.
- **Troubleshooting-Tipp**: Wenn der Fehler bestehen bleibt, entferne das `SuppressWithNearbyTextFilter`-Modul vorübergehend aus `checks.xml` und führe `mvn checkstyle:check` aus, um zu sehen, ob das Problem spezifisch für diesen Filter ist.

---

### Schritt 4: Teste die Behebung
- Führe den folgenden Befehl zum Testen aus:
  ```bash
  mvn clean checkstyle:check
  ```
- Wenn es funktioniert, sollte das Plugin `checks.xml` finden und alle Module ohne Fehler verarbeiten.
- Um sicherzustellen, dass Checkstyle während der Kompilierung läuft, verwende:
  ```bash
  mvn compile
  ```

---

### Optional: Alternativer Dateispeicherort
Wenn du ein standardmäßigeres Maven-Setup bevorzugst:
- Verschiebe `checks.xml` nach `src/main/resources/checks.xml`.
- Aktualisiere `<configLocation>` auf:
  ```xml
  <configLocation>classpath:checks.xml</configLocation>
  ```
- Dies entspricht der Maven-Konvention, Ressourcen in `src/main/resources` abzulegen.

---

### Zusätzliche Hinweise
- **Unabhängige Warnung**: Wenn du eine Warnung über ein `<blocked>`-Tag in `/usr/share/maven/conf/settings.xml` siehst, steht dies nicht im Zusammenhang mit diesem Problem, deutet aber auf ein Problem in deiner Maven-Settings-Datei hin. Überprüfe diese gegebenenfalls separat.
- **Probleme bleiben bestehen?** Teile Folgendes für weitere Hilfe:
  - Den Inhalt (oder einen Ausschnitt) von `checks.xml`.
  - Die vollständige Ausgabe von `mvn clean checkstyle:check -X` (Debug-Modus).

---

Durch die Anwendung dieser Änderungen sollte das `maven-checkstyle-plugin` `checks.xml` korrekt finden und `SuppressWithNearbyTextFilter` unterstützen, wodurch deine Fehler behoben werden.


---

Der zuvor aufgetretene Fehler deutete darauf hin, dass das `maven-checkstyle-plugin` `checks.xml` nicht im Classpath finden konnte und dann aufgrund eines Problems mit dem `SuppressWithNearbyTextFilter`-Modul fehlschlug. Aus deiner aktualisierten Projektstruktur geht hervor, dass sich `checks.xml` im Projektstammverzeichnis (`~/Projects/blog-server/checks.xml`) befindet, nicht wie zuvor angenommen in `src/main/resources`. Dies erklärt, warum das Plugin sie nicht finden konnte, wenn es mit `<configLocation>classpath:checks.xml</configLocation>` oder `<configLocation>checks.xml</configLocation>` konfiguriert war, da diese Einstellungen die Datei im Classpath (typischerweise `src/main/resources`) erwarten.

Um dies zu beheben und sicherzustellen, dass das `maven-checkstyle-plugin` mit `mvn compile` unter Verwendung deiner benutzerdefinierten `checks.xml` im Projektstammverzeichnis läuft, musst du die `<configLocation>` so aktualisieren, dass sie auf den absoluten oder projektrelativen Pfad der Datei zeigt. Zusätzlich musst du das `SuppressWithNearbyTextFilter`-Problem behandeln, indem du die Kompatibilität mit der Checkstyle-Version sicherstellst. Nachfolgend findest du die Schritt-für-Schritt-Lösung.

### Aktualisierte `pom.xml`-Konfiguration
Ändere den `maven-checkstyle-plugin` in deiner `pom.xml` so ab, dass er auf `checks.xml` im Projektstammverzeichnis verweist und eine kompatible Checkstyle-Version für die Unterstützung von `SuppressWithNearbyTextFilter` verwendet.

```xml
<build>
    <resources>
        <resource>
            <directory>src/main/resources</directory>
            <includes>
                <include>**/*.xml</include>
                <include>**/*.yaml</include>
            </includes>
        </resource>
    </resources>
    <plugins>
        <plugin>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-maven-plugin</artifactId>
            <version>3.4.2</version>
            <executions>
                <execution>
                    <goals>
                        <goal>repackage</goal>
                    </goals>
                </execution>
            </executions>
        </plugin>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-surefire-plugin</artifactId>
            <version>3.0.0-M8</version>
        </plugin>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-checkstyle-plugin</artifactId>
            <version>3.3.1</version> <!-- Neueste Version für bessere Kompatibilität -->
            <configuration>
                <configLocation>${project.basedir}/checks.xml</configLocation> <!-- Zeigt auf checks.xml im Projektstammverzeichnis -->
            </configuration>
            <dependencies>
                <dependency>
                    <groupId>com.puppycrawl.tools</groupId>
                    <artifactId>checkstyle</artifactId>
                    <version>10.17.0</version> <!-- Unterstützt SuppressWithNearbyTextFilter -->
                </dependency>
            </dependencies>
            <executions>
                <execution>
                    <id>checkstyle-check</id>
                    <phase>compile</phase>
                    <goals>
                        <goal>check</goal>
                    </goals>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>
```

### Erklärung der Änderungen
1. **Aktualisierte `<configLocation>`**:
   - Geändert zu `${project.basedir}/checks.xml`, um auf `checks.xml` im Projektstammverzeichnis (`~/Projects/blog-server/checks.xml`) zu zeigen.
   - `${project.basedir}` wird in das Verzeichnis aufgelöst, das die `pom.xml` enthält, und stellt sicher, dass das Plugin die Datei unabhängig vom Classpath findet.

2. **Upgrade der Plugin-Version**:
   - `maven-checkstyle-plugin` auf `3.3.1` aktualisiert (Stand Juni 2025) für bessere Kompatibilität und Fehlerbehebungen.

3. **Checkstyle-Abhängigkeit hinzugefügt**:
   - `<dependency>` für Checkstyle `10.17.0` hinzugefügt, die Unterstützung für `SuppressWithNearbyTextFilter` enthält. Die standardmäßige Checkstyle-Version in `maven-checkstyle-plugin:3.1.1` (`8.29`) unterstützt diesen Filter nicht, was den vorherigen Fehler verursachte.

4. **Beibehaltung von `<phase>compile</phase>`**:
   - Stellt sicher, dass `checkstyle:check` während `mvn compile` ausgeführt wird, wie gewünscht.

5. **Resources-Abschnitt**:
   - Der `<resources>`-Abschnitt wurde beibehalten, um sicherzustellen, dass Dateien in `src/main/resources` (wie `application.yaml`) verarbeitet werden, obwohl dies nicht direkt mit `checks.xml` zusammenhängt, da sie sich jetzt im Projektstammverzeichnis befindet.

### Überprüfe den Inhalt von `checks.xml`
Der Fehler bezüglich `SuppressWithNearbyTextFilter` deutet darauf hin, dass deine `checks.xml` auf diesen Filter verweist. Stelle sicher, dass sie korrekt konfiguriert ist. Ein gültiges Beispiel:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE module PUBLIC
    "-//Checkstyle//DTD Checkstyle Configuration 1.3//EN"
    "https://checkstyle.org/dtds/configuration_1_3.dtd">
<module name="Checker">
    <module name="SuppressWithNearbyTextFilter">
        <!-- Beispiel-Properties, nach Bedarf anpassen -->
        <property name="nearbyTextPattern" value="@SuppressWarnings"/>
    </module>
    <module name="TreeWalker">
        <!-- Andere Checks -->
        <module name="ConstantName"/>
    </module>
</module>
```

- **Prüfung**: Öffne `checks.xml` unter `~/Projects/blog-server/checks.xml` und verifiziere, dass `SuppressWithNearbyTextFilter` korrekt geschrieben ist und alle erforderlichen Properties enthält (siehe [Checkstyle-Dokumentation](https://checkstyle.org/filters/suppresswithnearbytextfilter.html)).
- **Aktion**: Wenn du unsicher bist, entferne vorübergehend den Abschnitt `<module name="SuppressWithNearbyTextFilter"/>` und teste, um das Problem zu isolieren.

### Teste die Konfiguration
1. **Bereinige das Projekt**:
   ```bash
   mvn clean
   ```
   Dies entfernt das `target`-Verzeichnis, inklusive `checkstyle-checker.xml` und `checkstyle-result.xml`, und stellt sicher, dass keine veralteten Artefakte stören.

2. **Führe Checkstyle aus**:
   ```bash
   mvn checkstyle:check
   ```
   Dies testet die Checkstyle-Konfiguration unabhängig.

3. **Führe Compile aus**:
   ```bash
   mvn compile
   ```
   Dies sollte Checkstyle ausführen (aufgrund der Bindung an die `compile`-Phase) und dann kompilieren, falls keine Verstöße den Build abbrechen.

### Debugging bei anhaltenden Problemen
Wenn Fehler auftreten:
1. **Überprüfe den Dateipfad**:
   - Bestätige, dass `checks.xml` unter `~/Projects/blog-server/checks.xml` existiert.
   - Verifiziere, dass der Dateiname exakt `checks.xml` ist (case-sensitiv, keine versteckten Erweiterungen).

2. **Führe mit Debug-Logging aus**:
   ```bash
   mvn clean checkstyle:check -X
   ```
   Suche nach Meldungen zum Laden von `checks.xml` oder zur Initialisierung von `SuppressWithNearbyTextFilter`. Teile die relevante Ausgabe, wenn der Fehler bestehen bleibt.

3. **Teste mit einer minimalen `checks.xml`**:
   Ersetze `checks.xml` vorübergehend durch eine minimale Konfiguration, um Probleme mit dem Dateiinhalt auszuschließen:
   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <!DOCTYPE module PUBLIC
       "-//Checkstyle//DTD Checkstyle Configuration 1.3//EN"
       "https://checkstyle.org/dtds/configuration_1_3.dtd">
   <module name="Checker">
       <module name="TreeWalker">
           <module name="ConstantName"/>
       </module>
   </module>
   ```
   Führe dann `mvn checkstyle:check` aus. Wenn dies funktioniert, liegt das Problem bei `SuppressWithNearbyTextFilter` oder anderen Modulen in deiner ursprünglichen `checks.xml`.

### Zusätzliche Hinweise
- **Settings.xml-Warnung**: Deine Ausgabe zeigt eine Warnung über ein nicht erkanntes `<blocked>`-Tag in `/usr/share/maven/conf/settings.xml`. Dies hängt nicht mit dem Checkstyle-Problem zusammen, deutet aber auf ein potenzielles Problem mit deiner Maven-Konfiguration hin. Überprüfe Zeile 164 von `/usr/share/maven/conf/settings.xml` und entferne oder korrigiere das `<blocked>`-Tag, da es kein standardmäßiges Maven-Settings-Element ist.
- **Alternativer Dateispeicherort**: Wenn du bevorzugst, kannst du `checks.xml` nach `src/main/resources/checks.xml` verschieben und `<configLocation>` auf `classpath:checks.xml` zurücksetzen. Dies ist konventioneller für Maven-Projekte, da Ressourcen automatisch im Classpath enthalten sind.
- **Bei Verstoß fehlschlagen**: Wenn Checkstyle-Verstöße den Build abbrechen und du die Kompilierung dennoch fortsetzen möchtest, füge `<failOnViolation>false</failOnViolation>` zur `<configuration>` des Plugins hinzu:
  ```xml
  <configuration>
      <configLocation>${project.basedir}/checks.xml</configLocation>
      <failOnViolation>false</failOnViolation>
  </configuration>
  ```

### Verifikation
Nach Anwendung der Änderungen:
1. Führe `mvn clean compile` aus und bestätige, dass:
   - Checkstyle unter Verwendung von `checks.xml` aus dem Projektstammverzeichnis läuft.
   - Keine Fehler im Zusammenhang mit `checks.xml` oder `SuppressWithNearbyTextFilter` auftreten.
   - Die Kompilierung fortgesetzt wird, wenn Checkstyle erfolgreich ist oder so konfiguriert ist, dass es den Build nicht abbricht.
2. Überprüfe `target/checkstyle-result.xml` auf die Checkstyle-Ergebnisse.

Wenn der Fehler bestehen bleibt, teile bitte:
- Den Inhalt (oder relevanten Ausschnitt) von `checks.xml`.
- Die Debug-Ausgabe von `mvn clean checkstyle:check -X`.
- Alle spezifischen Checkstyle-Regeln, die du mit `SuppressWithNearbyTextFilter` durchsetzen möchtest.