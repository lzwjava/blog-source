---
audio: false
generated: true
lang: de
layout: post
title: Java Language Server in Visual Studio Code
translated: true
type: note
---

Hallo! Die Einstellung `java.jdt.ls.java.home` in Visual Studio Code (VSCode) ist eine spezifische Konfigurationsoption, die vom Java Language Server (Teil der Erweiterung "Language Support for Java(TM) by Red Hat", enthalten im Java Extension Pack) verwendet wird. Lass uns das genauer betrachten:

---

### Was es bedeutet
- **JDT**: Steht für "Java Development Tools" und war ursprünglich Teil der Eclipse IDE. Der Java Language Server in VSCode basiert auf Eclipses JDT, welches Funktionen wie Code-Vervollständigung, Debugging und Kompilierung bereitstellt.
- **LS**: Steht für "Language Server", einen Hintergrundprozess, der die Java-Unterstützung in VSCode antreibt (z.B. IntelliSense, Fehlerüberprüfung).
- **`java.jdt.ls.java.home`**: Diese Einstellung teilt dem Java Language Server exakt mit, welches Java Development Kit (JDK) es für seine Operationen verwenden soll. Sie unterscheidet sich von der allgemeineren `java.home` Einstellung, obwohl sie verwandt sind.

Kurz gesagt, `java.jdt.ls.java.home` spezifiziert den JDK-Pfad, den der Java Language Server verwendet, um:
- Ihren Java-Code zu parsen.
- Sprachfunktionen bereitzustellen (z.B. Autovervollständigung, Gehe zu Definition).
- Code in manchen Fällen zu kompilieren und auszuführen (obwohl die Kompilierung oft von anderen Einstellungen oder Build-Tools abhängt).

---

### Unterschiede zu `java.home`
- **`java.home`**: Eine allgemeine VSCode-Einstellung, die auf das JDK für alle Java-bezogenen Erweiterungen und Aufgaben in VSCode verweist. Sie wird verwendet, sofern sie nicht durch spezifischere Einstellungen überschrieben wird.
- **`java.jdt.ls.java.home`**: Eine spezifischere Einstellung, die `java.home` nur für den Java Language Server überschreibt. Wenn diese nicht gesetzt ist, greift der Language Server auf `java.home` zurück.

Wenn Sie also `java.jdt.ls.java.home` setzen, hat dies Vorrang für die Operationen des Language Servers, sodass Sie ein anderes JDK für Sprachfunktionen verwenden können als z.B. für Lauf- oder Debugging-Aufgaben.

---

### Wie man es konfiguriert
Da Sie Windows verwenden und VSCode 1.96.4 mit dem Java Extension Pack, hier die Vorgehensweise:

1. **Einstellungen öffnen:**
   - Drücken Sie `Strg + ,` für die Einstellungs-UI, oder verwenden Sie `Strg + Umschalt + P` und tippen Sie **"Open Settings (JSON)"**, um die `settings.json` zu bearbeiten.

2. **Den Pfad setzen:**
   - **In der Einstellungs-UI:**
     - Suchen Sie nach **"java.jdt.ls.java.home"**.
     - Geben Sie den vollständigen Pfad zu Ihrem JDK ein (z.B. `C:\Program Files\Java\jdk-17.0.1`).
   - **In der settings.json:**
     - Fügen Sie diese Zeile hinzu (ersetzen Sie den Pfad mit Ihrem JDK-Pfad):
       ```json
       "java.jdt.ls.java.home": "C:\\Program Files\\Java\\jdk-17.0.1"
       ```
     - Beispiel `settings.json`:
       ```json
       {
           "java.jdt.ls.java.home": "C:\\Program Files\\Java\\jdk-17.0.1"
       }
       ```

3. **JDK-Pfad überprüfen:**
   - Stellen Sie sicher, dass der Pfad auf einen JDK-Ordner verweist, der ein `bin` Verzeichnis mit `javac.exe` und `java.exe` enthält.

4. **VSCode neu laden:**
   - Laden Sie das Fenster neu (`Strg + Umschalt + P` > "Reload Window") oder starten Sie VSCode neu, um die Änderung zu übernehmen.

---

### Wann man es verwendet
Sie würden `java.jdt.ls.java.home` typischerweise setzen, wenn:
- Sie mehrere JDKs installiert haben und möchten, dass der Language Server ein spezifisches verwendet (z.B. JDK 17), während andere Java-Aufgaben (wie das Ausführen von Code) möglicherweise ein anderes JDK über `java.home` verwenden.
- Sie Probleme mit dem Language Server beheben (z.B. wenn er nicht automatisch das richtige JDK erkennt).
- Ihr Projekt spezifische JDK-Versionsanforderungen für Sprachfunktionen hat.

Wenn Sie es nicht setzen, verwendet der Language Server das JDK von `java.home` (oder als letzte Rückfalloption die `JAVA_HOME` Umgebungsvariable des Systems).

---

### Praktisches Beispiel
Angenommen, Sie haben JDK 8 und JDK 17 installiert:
- Setzen Sie `"java.home": "C:\\Program Files\\Java\\jdk1.8.0_291"` für die allgemeine Verwendung.
- Setzen Sie `"java.jdt.ls.java.home": "C:\\Program Files\\Java\\jdk-17.0.1"`, um sicherzustellen, dass der Language Server JDK 17 für die Unterstützung moderner Java-Syntax verwendet.

Auf diese Weise können Sie mit JDK 8 debuggen/ausführen, aber gleichzeitig Sprachunterstützung für JDK 17-Features erhalten.

---

Klärt das die Sache? Wenn Sie wissen möchten, wie das zu Ihrem Setup passt oder weitere Hilfe bei Anpassungen benötigen, lassen Sie es mich einfach wissen! 😊