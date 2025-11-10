---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: Makellos in Multi-Module-Maven-Projekten
translated: true
type: note
---

### Spotless in Multi-Module Maven-Projekten

Spotless ist ein Code-Formatierungs-Plugin, das für Maven und Gradle verfügbar ist. Basierend auf Ihrer Erwähnung des `-pl`-Flags (Projektliste) von Maven gehe ich davon aus, dass Sie das **Spotless Maven-Plugin** in einem Multi-Module Java-Projekt verwenden. Dies ermöglicht es Ihnen, Formatierungsprüfungen (z. B. via `spotless:check`) oder Korrekturen (z. B. via `spotless:apply`) selektiv für bestimmte Module auszuführen, was bei großen Projekten effizient ist, bei denen Sie möglicherweise nur bestimmte Module formatieren müssen (z. B. während der Entwicklung an einem bestimmten Submodul).

#### Voraussetzungen
- Ihr Projekt verwendet Maven mit einer Multi-Module-Struktur (definiert in einer Parent-`pom.xml` mit `<modules>...</modules>`).
- Das Spotless Maven-Plugin ist in Ihrem Projekt konfiguriert (typischerweise in der Parent-POM oder in einzelnen Modul-POMs). Falls nicht, fügen Sie es Ihrer POM hinzu:
  ```xml
  <build>
    <plugins>
      <plugin>
        <groupId>com.diffplug.spotless</groupId>
        <artifactId>spotless-maven-plugin</artifactId>
        <version>2.43.0</version>  <!-- Verwenden Sie die neueste Version -->
        <configuration>
          <!-- Ihre Formatierungsregeln hier, z. B. für Java, Groovy -->
        </configuration>
      </plugin>
    </plugins>
  </build>
  ```
  - Gängige Regeln umfassen Google Java Format, Eclipse JDT für Java oder Anpassungen für Imports, Abstände etc.
  - Spotless unterstützt viele Dateitypen (Java, Kotlin, XML etc.) und integriert sich gut mit CI-Tools für Pre-Commit-Hooks (über das Goal `spotless:check`, das Builds bei nicht formatiertem Code fehlschlagen lässt).

#### Verwendung von `-pl` zur Steuerung der Modulformatierung
Mavens `-pl`-Flag (Projektliste) ermöglicht es Ihnen, eine kommagetrennte Liste von Modulen anzugeben, die in den Build/Plugin-Ausführung einbezogen werden sollen. Standardmäßig führt Maven die Aktion für alle Module aus, aber `-pl` schränkt dies ein, spart Zeit und vermeidet unnötige Arbeit an nicht betroffenen Modulen.

- **Grundlegende Befehlsstruktur**:
  - Um die Formatierung zu prüfen (ohne Änderungen anzuwenden): `mvn spotless:check -pl modul1,modul2`
  - Um Formatierungskorrekturen anzuwenden: `mvn spotless:apply -pl modul1,modul2`
  - Ersetzen Sie `modul1,modul2` durch die tatsächlichen Modulnamen (z. B. relative Pfade vom Root, wie `core,api`).

- **Beispiele**:
  1. **Formatierung nur im `core`-Modul prüfen**:
     ```
     mvn spotless:check -pl core
     ```
     - Dies scannt und validiert nur die Quelldateien von `core`. Wenn Formatierungsprobleme existieren, schlägt der Build fehl und gibt Details aus (z. B. "Bitte führen Sie `spotless:apply` aus, um dies zu beheben").

  2. **Formatierung auf mehrere Module anwenden (`api` und `utils`)**:
     ```
     mvn spotless:apply -pl api,utils
     ```
     - Dies modifiziert Dateien direkt, um Ihren Spotless-Regeln zu entsprechen. Committen Sie die Änderungen anschließend immer, um Überraschungen in der Versionskontrolle zu vermeiden.

  3. **Bestimmte Module während eines vollständigen Projektlaufs ausschließen**: Verwenden Sie `-pl !modulZumUeberspringen`, um die Aktion für alles *außer* bestimmten Modulen auszuführen (Maven 3.2.1+ unterstützt Negation mit `!`).
     - Beispiel: `mvn spotless:check -pl !legacy` (führt die Prüfung für alle Module außer `legacy` durch).

- **Tipps für Effizienz**:
  - **Parallele Ausführung**: Fügen Sie `-T 4` für Multithread-Builds hinzu (z. B. `mvn spotless:check -pl core,api -T 4`).
  - **Dry Run**: Verwenden Sie zuerst `spotless:check`, um Probleme ohne Änderungen in der Vorschau zu sehen – es ist idempotent und sicher.
  - **Integration mit IDE/Versionskontrolle**: Konfigurieren Sie Spotless, um es bei Speichern/Committen in Ihrer IDE auszuführen (z. B. IntelliJ über das Spotless Plugin) oder verwenden Sie es als Pre-Commit-Hook (über Tools wie pre-commit oder Git Hooks) für automatisierte Prüfungen.
  - **Umgang mit Reactor-Auflösung**: Wenn Modulabhängigkeiten komplex sind, löst Maven diese automatisch auf, wenn `-pl` verwendet wird, und stellt sicher, dass abhängige Module bei Bedarf zuerst verarbeitet werden.
  - **Häufige Probleme**:
    - Wenn `-pl` nicht funktioniert, stellen Sie sicher, dass die Module in `<modules>` definiert sind, und verwenden Sie bei Mehrdeutigkeiten vollqualifizierte Pfade (z. B. `-pl :core` für Multi-Repo-Setups).
    - Für Gradle-Benutzer (falls Sie das Spotless Gradle-Plugin meinten) ist das Äquivalent `-p` für Projektpfade, aber Ihre Anfrage spezifiziert `-pl`, daher wird Maven angenommen. Falls es Gradle ist, wechseln Sie zu Plugins wie `gradle task -p submodul`.

Die vollständige Dokumentation finden Sie in den [Spotless Maven Plugin docs](https://github.com/diffplug/spotless/tree/v2.43.0/plugin-maven). Falls Ihr Setup abweicht (z. B. Gradle), geben Sie bitte weitere Details für eine maßgeschneiderte Beratung an.