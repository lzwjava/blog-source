---
audio: false
generated: true
lang: de
layout: post
title: Anwendung von JMeter
translated: true
type: note
---

JMeter ist eine Open-Source-Software, die für Lasttests und die Leistungsmessung von Webanwendungen entwickelt wurde, kann aber auch andere Systemtypen wie Datenbanken und FTP-Server testen. Im Folgenden finden Sie eine klare, schrittweise Anleitung, die Ihnen den Einstieg in die Verwendung von JMeter für Performance-Tests erleichtert, mit Schwerpunkt auf Webanwendungen.

---

#### **Schritt 1: JMeter installieren**
- **Voraussetzungen**: JMeter ist eine Java-basierte Anwendung, daher muss Java (Version 8 oder höher) auf Ihrem Rechner installiert sein. Sie können dies überprüfen, indem Sie `java -version` in Ihrer Kommandozeile ausführen.
- **Download**: Besuchen Sie die [Apache JMeter Website](https://jmeter.apache.org/) und laden Sie die neueste Version herunter (eine .zip- oder .tgz-Datei).
- **Installation**: Extrahieren Sie die heruntergeladene Datei in ein Verzeichnis Ihrer Wahl (z. B. `C:\JMeter` unter Windows oder `/opt/jmeter` unter Linux/Mac). Es sind keine weiteren Installationsschritte erforderlich.

---

#### **Schritt 2: JMeter starten**
- Navigieren Sie in das `bin`-Verzeichnis innerhalb des JMeter-Ordners (z. B. `C:\JMeter\apache-jmeter-x.x\bin`).
- **Windows**: Doppelklicken Sie auf `jmeter.bat` oder führen Sie es über die Kommandozeile aus.
- **Linux/Mac**: Öffnen Sie ein Terminal, navigieren Sie in das `bin`-Verzeichnis und führen Sie `./jmeter.sh` aus.
- Eine grafische Benutzeroberfläche (GUI) wird geöffnet, die die JMeter-Arbeitsumgebung anzeigt.

---

#### **Schritt 3: Einen Testplan erstellen**
- Der **Testplan** ist die Grundlage Ihres Performance-Tests. Er legt fest, was und wie Sie testen möchten.
- In der JMeter-GUI ist der Testplan bereits im linken Bereich vorhanden. Klicken Sie mit der rechten Maustaste darauf, um ihn umzubenennen (z. B. "Web Performance Test"), oder belassen Sie ihn unverändert.

---

#### **Schritt 4: Eine Thread-Gruppe hinzufügen**
- Eine **Thread-Gruppe** simuliert Benutzer, die Anfragen an den Server senden.
- Klicken Sie mit der rechten Maustaste auf den Testplan > **Hinzufügen** > **Threads (Users)** > **Thread Group**.
- Konfigurieren Sie:
  - **Number of Threads (users)**: Legen Sie fest, wie viele virtuelle Benutzer Sie möchten (z. B. 10).
  - **Ramp-Up Period (seconds)**: Die Zeit, die benötigt wird, um alle Threads zu starten (z. B. 10 Sekunden bedeutet 1 Thread pro Sekunde).
  - **Loop Count**: Die Anzahl, wie oft der Test wiederholt werden soll (z. B. 1 oder "Forever" für kontinuierliches Testen aktivieren).

---

#### **Schritt 5: Sampler hinzufügen**
- **Sampler** definieren die an den Server gesendeten Anfragen. Für Webtests verwenden Sie den HTTP Request-Sampler.
- Klicken Sie mit der rechten Maustaste auf die Thread-Gruppe > **Hinzufügen** > **Sampler** > **HTTP Request**.
- Konfigurieren Sie:
  - **Server Name or IP**: Geben Sie die Ziel-Website ein (z. B. `example.com`).
  - **Path**: Geben Sie den Endpunkt an (z. B. `/login`).
  - **Method**: Wählen Sie `GET`, `POST` usw. basierend auf Ihrem Testszenario.

---

#### **Schritt 6: Listener hinzufügen**
- **Listener** zeigen Testergebnisse an und analysieren sie.
- Klicken Sie mit der rechten Maustaste auf die Thread-Gruppe > **Hinzufügen** > **Listener** > (z. B. **View Results Tree** oder **Summary Report**).
- Beliebte Optionen:
  - **View Results Tree**: Zeigt detaillierte Anfrage-/Antwortdaten an.
  - **Summary Report**: Bietet aggregierte Metriken wie durchschnittliche Antwortzeit und Fehlerrate.

---

#### **Schritt 7: Den Test konfigurieren**
- Verbessern Sie Ihren Test mit zusätzlichen Elementen (optional, aber nützlich):
  - **Timers**: Fügen Sie Verzögerungen zwischen Anfragen hinzu (z. B. Rechtsklick auf Thread-Gruppe > **Hinzufügen** > **Timer** > **Constant Timer**).
  - **Assertions**: Validieren Sie Serverantworten (z. B. Rechtsklick auf HTTP Request > **Hinzufügen** > **Assertions** > **Response Assertion**).
  - **Config Elements**: Setzen Sie Variablen oder HTTP-Standardwerte (z. B. **HTTP Request Defaults**).

---

#### **Schritt 8: Den Test ausführen**
- Speichern Sie Ihren Testplan (**Datei** > **Speichern**) als `.jmx`-Datei zur Wiederverwendung.
- Klicken Sie auf die grüne **Run**-Schaltfläche (Dreieck) in der Symbolleiste oder gehen Sie zu **Run** > **Start**.
- JMeter führt den Test basierend auf den Einstellungen Ihrer Thread-Gruppe aus.

---

#### **Schritt 9: Die Ergebnisse analysieren**
- Nach Abschluss des Tests überprüfen Sie die Listener:
  - **View Results Tree**: Überprüfen Sie Erfolge/Fehler einzelner Anfragen.
  - **Summary Report**: Prüfen Sie Metriken wie Durchsatz, Antwortzeiten und Fehlerprozentsätze.
- Suchen Sie nach Engpässen (z. B. langsame Antwortzeiten) oder Fehlern, die untersucht werden müssen.

---

#### **Schritt 10: Den Test verfeinern**
- Passen Sie Ihren Testplan basierend auf den Ergebnissen an:
  - Erhöhen/Verringern Sie die Anzahl der Threads.
  - Fügen Sie realistischere Szenarien hinzu (z. B. mehrere HTTP Requests).
  - Passen Sie Timers oder Assertions für mehr Genauigkeit an.
- Speichern Sie und führen Sie den Test erneut aus, um Verbesserungen zu validieren.

---

### Zusätzliche Tipps
- **Speichern und Laden**: Verwenden Sie `.jmx`-Dateien, um Ihren Testplan zu speichern und später über **Datei** > **Öffnen** zu laden.
- **GUI vs. Non-GUI**: Führen Sie für große Tests JMeter im Non-GUI-Modus aus (z. B. `jmeter -n -t test.jmx -l results.jtl`), um Systemressourcen zu sparen.
- **Mehr lernen**: Erkunden Sie fortgeschrittene Funktionen wie Parametrisierung (für dynamische Daten) oder Korrelation (für dynamische Web-Apps), während Sie Erfahrung sammeln.

Diese Anleitung vermittelt die Grundlagen, um JMeter effektiv zu nutzen. Mit etwas Übung können Sie Tests an spezifische Performance-Test-Anforderungen anpassen!