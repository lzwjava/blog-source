---
audio: false
generated: true
lang: de
layout: post
title: Konsolenanwendung
translated: true
type: note
---

Um den Fehler "Failed to open input stream in demuxing stream" in Infuse, einer Mac-App, zu beheben und detailliertere Logs einzusehen, können Sie auf Ihrem Mac verfügbare Tools verwenden. Da die Anfrage "iOS oder Xcode tool" erwähnt, aber Infuse als Mac-App spezifiziert, möchten Sie wahrscheinlich Xcode oder verwandte macOS-Tools verwenden, um die Logs für die Mac-Version von Infuse zu überprüfen. Im Folgenden finden Sie Schritt-für-Schritt-Anleitungen, um auf diese Logs zuzugreifen.

### Für Infuse auf dem Mac (Primäre Methode: Console App)
Da Infuse in Ihrer Anfrage als Mac-App identifiziert wird, ist der direkteste Weg, die Logs einzusehen, die Verwendung der **Console**-App, die in macOS integriert ist und dazu dient, System- und Anwendungsprotokolle anzuzeigen.

1. **Öffnen Sie die Console-App**:
   - Starten Sie die **Console**-App. Sie befindet sich unter **Programme** > **Dienstprogramme** > **Console**, oder suchen Sie danach mit Spotlight (Cmd + Leertaste, dann "Console" eingeben).

2. **Filtern Sie die Logs für Infuse**:
   - Verwenden Sie in der Console-App die Suchleiste oben rechts.
   - Geben Sie "Infuse" oder den Prozessnamen der App (wahrscheinlich "Infuse" oder ähnlich) ein, um die betreffenden Logs zu filtern.

3. **Reproduzieren Sie den Fehler**:
   - Während die Console-App geöffnet ist und die Filterung aktiv ist, spielen Sie das Video in Infuse ab, das den Fehler "Failed to open input stream in demuxing stream" auslöst.
   - Dies stellt sicher, dass die relevanten Logs in Echtzeit erfasst werden.

4. **Analysieren Sie die Logs**:
   - Suchen Sie nach Fehlermeldungen, Warnungen oder detaillierten Ausgaben, die erklären könnten, warum der Eingabestream beim Demuxing (dem Prozess der Trennung von Audio- und Videostreams) nicht geöffnet werden konnte.
   - Schlüsselwörter wie "error", "fail" oder "demux" können helfen, das Problem einzugrenzen.

### Falls Sie die iOS-Version von Infuse gemeint haben (Verwendung von Xcode)
Falls Sie die iOS-Version von Infuse debuggen wollten (obwohl die Anfrage "Mac-App" sagt), können Sie **Xcode**, das Entwicklungstool von Apple, verwenden, um auf die Logs eines iOS-Geräts zuzugreifen. So geht's:

1. **Verbinden Sie Ihr iOS-Gerät**:
   - Schließen Sie Ihr iPhone oder iPad über ein USB-Kabel an Ihren Mac an.

2. **Öffnen Sie Xcode**:
   - Starten Sie **Xcode** auf Ihrem Mac. Falls es nicht installiert ist, laden Sie es aus dem Mac App Store herunter.

3. **Greifen Sie auf Geräte und Simulatoren zu**:
   - Gehen Sie in Xcode zur Menüleiste und wählen Sie **Fenster** > **Devices and Simulators**.

4. **Wählen Sie Ihr Gerät aus**:
   - Suchen Sie in dem sich öffnenden Fenster Ihr verbundenes iOS-Gerät in der linken Seitenleiste und klicken Sie darauf.

5. **Sehen Sie sich die Logs an**:
   - Klicken Sie auf **Open Console** oder **View Device Logs** (die Option kann je nach Xcode-Version variieren).
   - Dies öffnet einen Log-Viewer, der alle Aktivitäten Ihres Geräts anzeigt.

6. **Filtern Sie nach Infuse**:
   - Verwenden Sie die Such- oder Filteroption im Log-Viewer, um die Einträge einzugrenzen, indem Sie "Infuse" oder die Bundle-ID der App (z.B. `com.firecore.Infuse`, falls bekannt) eingeben.
   - Reproduzieren Sie den Fehler auf Ihrem iOS-Gerät, während die Konsole geöffnet ist, um die relevanten Logs zu erfassen.

### Zusätzliche Optionen
- **Überprüfen Sie auf Absturzberichte**:
  - **Mac**: Wenn Infuse abstürzt, überprüfen Sie `~/Library/Logs/DiagnosticReports` oder `/Library/Logs/DiagnosticReports` auf Absturzprotokolle, die mit "Infuse" und einem Zeitstempel benannt sind.
  - **iOS**: In Xcodes **Devices and Simulators**-Fenster können Absturzprotokolle für Infuse unter den Logs Ihres Geräts erscheinen.

- **Aktivieren Sie die Debug-Protokollierung in Infuse**:
  - Einige Apps, einschließlich Infuse, bieten möglicherweise einen Debug-Modus oder eine Option für ausführliche Protokollierung. Öffnen Sie die Einstellungen oder Präferenzen von Infuse auf Ihrem Mac (oder iOS-Gerät), um zu sehen, ob es eine solche Funktion gibt. Wenn aktiviert, könnte dies detailliertere Logs generieren, die über die oben genannten Methoden einsehbar sind.

- **Alternative für iOS (Console-App)**:
  - Verbinden Sie Ihr iOS-Gerät mit Ihrem Mac, öffnen Sie die **Console**-App und wählen Sie Ihr Gerät aus der linken Seitenleiste aus. Filtern Sie die Logs nach "Infuse", um die Ausgabe in Echtzeit zu sehen, ohne Xcode zu benötigen.

### Hinweise
- Der Fehler "Failed to open input stream in demuxing stream" deutet auf ein Problem mit der Mediendatei oder dem Netzwerkstream hin, den Infuse verarbeiten möchte. Die Logs könnten Aufschluss darüber geben, ob es sich um eine Dateibeschädigung, eine Codec-Inkompatibilität oder ein Verbindungsproblem handelt.
- Da Infuse eine Drittanbieter-App ist, ist erweitertes Debugging (z.B. das Anhängen von Xcode an den Prozess) ohne Entwicklerzugriff unwahrscheinlich, daher sind die Console-App (für Mac) oder Geräteprotokolle (für iOS) Ihre besten Optionen.

Indem Sie diese Schritte befolgen, können Sie weitere Logs sammeln, um den Fehler in Infuse, sei es auf dem Mac oder iOS, zu diagnostizieren. Wenn das Problem weiterhin besteht, ziehen Sie in Betracht, die Support-Dokumentation oder die Foren von Infuse auf app-spezifische Protokollierungstipps zu überprüfen.