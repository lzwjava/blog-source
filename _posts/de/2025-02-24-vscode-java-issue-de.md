---
audio: false
generated: true
lang: de
layout: post
title: Java Language Server und Maven Build
translated: true
type: note
---

Es klingt so, als hättest du zwei verwandte Probleme in Visual Studio Code (VSCode): eine Fehlermeldung, die mindestens Java 21 erfordert, und Probleme damit, dass VSCode einige Objektdefinitionen in deinem Java-Code nicht erkennt, obwohl dein Maven-Build erfolgreich kompiliert. Lassen wir das Schritt für Schritt lösen.

Das Problem tritt auf, weil sich die Java-Erweiterungen von VSCode (insbesondere der Java Language Server) und dein Maven-Build in Bezug auf die Java Development Kit (JDK)-Version oder die Projektkonfiguration nicht abstimmen. VSCode meldet, dass es JDK 21 für ein einwandfreies Funktionieren benötigt, und die Parsing-Fehler deuten darauf hin, dass es deinen Code nicht so interpretiert wie Maven. So kannst du das beheben:

---

### Schritt 1: JDK 21 installieren
Da VSCode explizit nach Java 21 verlangt, musst du sicherstellen, dass es auf deinem System installiert ist.

- **JDK 21 herunterladen**: Lade es von einer vertrauenswürdigen Quelle wie [Oracle’s Website](https://www.oracle.com/java/technologies/javase-jdk21-downloads.html) oder [Adoptium](https://adoptium.net/) herunter.
- **Installiere es**: Befolge die Installationsanweisungen und notiere den Installationspfad (z.B. `C:\Program Files\Java\jdk-21` unter Windows oder `/usr/lib/jvm/java-21-openjdk` unter Linux).
- **Überprüfen**: Öffne ein Terminal und führe `java -version` aus. Du solltest etwas sehen wie:
  ```
  java version "21.0.1" ...
  ```

---

### Schritt 2: VSCode für die Verwendung von JDK 21 konfigurieren
Du musst den Java-Erweiterungen von VSCode mitteilen, JDK 21 zu verwenden. So geht's:

1. **Öffne die VSCode-Einstellungen**:
   - Gehe zu `File > Preferences > Settings` (oder drücke `Strg + ,`).
2. **Lege den JDK-Pfad fest**:
   - Suche nach `java.jdt.ls.java.home`.
   - Gib den Pfad zu deiner JDK-21-Installation ein (z.B. `C:\Program Files\Java\jdk-21`).
   - Optional: Suche nach `java.home` und setze ihn für Konsistenz auf denselben Pfad.
3. **Bearbeite `settings.json` (Alternative)**:
   - Öffne die Befehlspalette (`Strg + Umschalt + P`), tippe "Preferences: Open Settings (JSON)" ein und füge hinzu:
     ```json
     {
         "java.jdt.ls.java.home": "C:\\Program Files\\Java\\jdk-21",
         "java.home": "C:\\Program Files\\Java\\jdk-21"
     }
     ```
   - Passe den Pfad entsprechend deinem System an (verwende Schrägstriche `/` für Linux/Mac).

Dadurch wird sichergestellt, dass der Java Language Server in VSCode JDK 21 verwendet und die Mindestanforderung erfüllt.

---

### Schritt 3: Das JDK des Projekts in VSCode festlegen
Um die Parsing-Probleme (z.B. nicht gefundene Objektdefinitionen) zu beheben, stelle sicher, dass dein Projekt in VSCode ebenfalls JDK 21 verwendet:

- Füge in `settings.json` Folgendes hinzu, um JDK 21 für dein Projekt festzulegen:
  ```json
  "java.configuration.runtimes": [
      {
          "name": "JavaSE-21",
          "path": "C:\\Program Files\\Java\\jdk-21",
          "default": true
      }
  ]
  ```
- Dies bringt die Laufzeitumgebung des Projekts in VSCode mit JDK 21 in Einklang, was ihm helfen sollte, deinen Code korrekt zu parsen.

---

### Schritt 4: Die JDK-Konfiguration von Maven überprüfen
Da dein Maven-Build (`mvn compile`) einwandfrei funktioniert, verwendet er wahrscheinlich ein kompatibles JDK. Lass uns das bestätigen und mit VSCode abstimmen:

1. **Überprüfe das von Maven verwendete JDK**:
   - Führe `mvn -version` in deinem Terminal aus. Suche nach der Zeile "Java version" (z.B. `Java version: 21.0.1`).
   - Falls es JDK 21 nicht verwendet, setze die Umgebungsvariable `JAVA_HOME` auf deinen JDK-21-Pfad:
     - **Windows**: `set JAVA_HOME=C:\Program Files\Java\jdk-21`
     - **Linux/Mac**: `export JAVA_HOME=/usr/lib/jvm/java-21-openjdk`
   - Führe `mvn -version` erneut aus, um es zu bestätigen.
2. **Gib das JDK in `pom.xml` an** (optional):
   - Wenn du JDK 21 in deinem Maven-Projekt erzwingen möchtest, füge dies deiner `pom.xml` hinzu:
     ```xml
     <properties>
         <maven.compiler.source>21</maven.compiler.source>
         <maven.compiler.target>21</maven.compiler.target>
     </properties>
     ```

---

### Schritt 5: VSCode aktualisieren
Nach diesen Änderungen muss VSCode aktualisiert werden, um sie zu übernehmen:

- Lade VSCode neu:
  - Öffne die Befehlspalette (`Strg + Umschalt + P`) und wähle "Developer: Reload Window".
- Alternativ: Schließe VSCode und öffne es wieder.

---

### Schritt 6: Sicherstellen, dass Abhängigkeiten geladen sind
Wenn VSCode immer noch keine Objektdefinitionen findet, hat es möglicherweise deine Maven-Abhängigkeiten nicht korrekt geladen:

1. **Bereinige den Arbeitsbereich**:
   - Öffne die Befehlspalette (`Strg + Umschalt + P`).
   - Führe "Java: Clean Java Language Server Workspace" aus.
2. **Erzwinge die Kompilierung**:
   - Führe "Java: Force Java Compilation" aus der Befehlspalette aus.
3. **Überprüfe die Imports**:
   - Stelle sicher, dass die Maven-Abhängigkeiten deines Projekts importiert wurden, indem du in VSCode mit der rechten Maustaste auf deine `pom.xml` klickst und "Update Project Configuration" auswählst.

---

### Fehlerbehebung
Wenn das Problem weiterhin besteht:
- **Überprüfe die Protokolle**:
  - Füge `"java.trace.server": "verbose"` zu `settings.json` hinzu.
  - Öffne das Ausgabefenster (`Strg + Umschalt + U`) und wähle "Java Language Server", um detaillierte Protokolle einzusehen.
- **Überprüfe den Code**:
  - Stelle sicher, dass die fehlenden Objektdefinitionen aus deinem Code oder den in `pom.xml` aufgeführten Abhängigkeiten stammen und keine externen Probleme vorliegen.

---

### Zusammenfassung
Durch die Installation von JDK 21, die Konfiguration von VSCode für dessen Verwendung, die Abstimmung deiner Projekt- und Maven-Einstellungen und die Aktualisierung der Umgebung sollte VSCode aufhören, sich über Java 21 zu beschweren, und deinen Code korrekt parsen, so wie es der erfolgreiche Maven-Build tut. Lass mich wissen, wenn du auf weitere Probleme stößt!