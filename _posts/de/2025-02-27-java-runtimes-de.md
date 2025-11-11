---
audio: false
generated: true
lang: de
layout: post
title: Java-Laufzeitumgebungen in Visual Studio Code
translated: true
type: note
---

Um `java.configuration.runtimes` in den Visual Studio Code (VS Code) Einstellungen zu verwenden, müssen Sie es in Ihrer `settings.json` Datei konfigurieren. Diese Einstellung ermöglicht es Ihnen, mehrere Java Development Kit (JDK) Versionen anzugeben, die VS Code für Ihre Java-Projekte verwenden kann. Dies ist besonders nützlich, wenn Sie mit verschiedenen Projekten arbeiten, die spezifische Java-Versionen erfordern. Hier ist eine Schritt-für-Schritt-Anleitung zur Einrichtung:

### Schritte zum Konfigurieren von `java.configuration.runtimes`

1. **Öffnen Sie die VS Code Einstellungen**:
   - Unter Windows/Linux: Gehen Sie zu `Datei > Einstellungen > Einstellungen` oder drücken Sie `Strg + ,`.
   - Unter macOS: Gehen Sie zu `Code > Einstellungen > Einstellungen` oder drücken Sie `Cmd + ,`.

2. **Greifen Sie auf die JSON-Einstellungsdatei zu**:
   - Suchen Sie in der Einstellungs-UI nach `java.configuration.runtimes`.
   - Sie sehen eine Option wie "Java: Configuration: Runtimes". Klicken Sie auf "Edit in settings.json" (normalerweise ein Link unter der Einstellungsbeschreibung), um die `settings.json` Datei zu öffnen.

3. **Bearbeiten Sie `settings.json`**:
   - Fügen Sie in der `settings.json` Datei das Array `java.configuration.runtimes` hinzu oder ändern Sie es. Dieses Array enthält Objekte, die jeweils eine JDK-Version repräsentieren, die VS Code erkennen soll.
   - Jedes Objekt enthält typischerweise:
     - `name`: Der Java-Versionsbezeichner (z.B. `JavaSE-1.8`, `JavaSE-11`, `JavaSE-17`).
     - `path`: Der absolute Pfad zum JDK-Installationsverzeichnis auf Ihrem System.
     - `default` (optional): Setzen Sie dies auf `true`, um dieses JDK zum Standard für unverwaltete Ordner (Projekte ohne Build-Tools wie Maven oder Gradle) zu machen.

   Hier ist eine Beispielkonfiguration:

   ```json
   {
       "java.configuration.runtimes": [
           {
               "name": "JavaSE-1.8",
               "path": "C:/Program Files/Java/jdk1.8.0_351",
               "default": true
           },
           {
               "name": "JavaSE-11",
               "path": "C:/Program Files/Java/jdk-11.0.15"
           },
           {
               "name": "JavaSE-17",
               "path": "C:/Program Files/Java/jdk-17.0.6"
           }
       ]
   }
   ```

4. **Überprüfen Sie die JDK-Pfade**:
   - Stellen Sie sicher, dass der `path` auf das Stammverzeichnis Ihrer JDK-Installation zeigt (z.B. wo sich der `bin`-Ordner mit `java.exe` oder `java` befindet).
   - Unter Windows verwenden Sie Schrägstriche (`/`) oder maskieren Sie die Backslashes (`\\`) im Pfad.
   - Unter macOS/Linux verwenden Sie den entsprechenden Dateisystempfad (z.B. `/usr/lib/jvm/java-17-openjdk`).

5. **Speichern und neu laden**:
   - Speichern Sie die `settings.json` Datei.
   - Starten Sie VS Code neu oder laden Sie das Fenster neu (`Strg + R` oder `Cmd + R`), um die Änderungen zu übernehmen.

6. **Überprüfen Sie die Konfiguration**:
   - Öffnen Sie die Befehlspalette (`Umschalt + Strg + P` oder `Umschalt + Cmd + P`) und führen Sie den Befehl `Java: Configure Java Runtime` aus.
   - Dies öffnet eine Ansicht, die die für Ihre Projekte verfügbaren JDKs anzeigt. Vergewissern Sie sich, dass Ihre konfigurierten Laufzeiten unter dem Tab "Project JDKs" erscheinen.

### So funktioniert es
- **Unverwaltete Ordner**: Für Projekte ohne Build-Tools (z.B. reine Java-Dateien) verwendet VS Code das in `java.configuration.runtimes` angegebene `default` JDK.
- **Verwaltete Projekte (Maven/Gradle)**: Für Projekte mit Build-Tools wird die JDK-Version durch die Build-Konfiguration bestimmt (z.B. `pom.xml` oder `build.gradle`), aber VS Code erkennt die hier aufgeführten Laufzeiten dennoch für die Kompatibilität.
- **Language Server**: Der Java Language Server (Teil der Java-Erweiterungen) benötigt JDK 17+ zum Ausführen. Sie können dies separat mit `java.jdt.ls.java.home` angeben, falls erforderlich (z.B. `"java.jdt.ls.java.home": "C:/Program Files/Java/jdk-17.0.6"`).

### Beispiel mit mehreren JDKs
Wenn Sie auf einem Mac arbeiten und JDK 8 und 17 via Homebrew installiert haben, könnte Ihre Konfiguration so aussehen:

```json
{
    "java.configuration.runtimes": [
        {
            "name": "JavaSE-1.8",
            "path": "/Library/Java/JavaVirtualMachines/jdk1.8.0_351.jdk/Contents/Home",
            "default": true
        },
        {
            "name": "JavaSE-17",
            "path": "/Library/Java/JavaVirtualMachines/jdk-17.0.6.jdk/Contents/Home"
        }
    ]
}
```

### Tipps
- Verwenden Sie das korrekte `name`-Format (`JavaSE-<version>`), das der Java-Version entspricht (z.B. `JavaSE-11` für Java 11).
- Wenn Sie nur ein JDK haben, können Sie es dennoch auflisten, um sicherzustellen, dass VS Code es explizit verwendet.
- Um Ihren JDK-Pfad zu finden, führen Sie `java -version` in einem Terminal aus und überprüfen Sie das Installationsverzeichnis (z.B. via `where java` unter Windows oder `which java` auf Unix-ähnlichen Systemen und gehen Sie dann zur JDK-Stammverzeichnis zurück).

Dieses Setup gibt Ihnen die Flexibilität, nahtlos mit mehreren Java-Versionen in VS Code zu arbeiten! Lassen Sie mich wissen, wenn Sie Hilfe beim Finden Ihrer JDK-Pfade oder bei der Fehlerbehebung benötigen.