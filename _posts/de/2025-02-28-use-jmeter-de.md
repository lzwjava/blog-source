---
audio: false
lang: de
layout: post
title: Wie man JMeter verwendet
translated: true
---

JMeter ist ein Open-Source-Software-Tool, das für Lasttests und zur Messung der Leistung von Webanwendungen entwickelt wurde. Es kann jedoch auch andere Systemtypen wie Datenbanken und FTP-Server testen. Hier ist eine klare, schrittweise Anleitung, um Ihnen den Einstieg in die Verwendung von JMeter für Leistungstests zu erleichtern, mit dem Schwerpunkt auf Webanwendungen.

---

#### **Schritt 1: JMeter installieren**
- **Voraussetzungen**: JMeter ist eine Java-basierte Anwendung, daher müssen Sie Java (Version 8 oder höher) auf Ihrem Computer installiert haben. Dies können Sie überprüfen, indem Sie `java -version` in Ihrer Kommandozeile ausführen.
- **Herunterladen**: Besuchen Sie die [Apache JMeter-Website](https://jmeter.apache.org/) und laden Sie die neueste Version (eine .zip- oder .tgz-Datei) herunter.
- **Installieren**: Entpacken Sie die heruntergeladene Datei in ein Verzeichnis Ihrer Wahl (z.B. `C:\JMeter` unter Windows oder `/opt/jmeter` unter Linux/Mac). Keine zusätzlichen Installationsschritte erforderlich.

---

#### **Schritt 2: JMeter starten**
- Navigieren Sie zum `bin`-Verzeichnis im JMeter-Ordner (z.B. `C:\JMeter\apache-jmeter-x.x\bin`).
- **Windows**: Doppelklicken Sie auf `jmeter.bat` oder führen Sie es über die Kommandozeile aus.
- **Linux/Mac**: Öffnen Sie ein Terminal, navigieren Sie zum `bin`-Verzeichnis und führen Sie `./jmeter.sh` aus.
- Eine grafische Benutzeroberfläche (GUI) wird geöffnet, die die JMeter-Arbeitsumgebung anzeigt.

---

#### **Schritt 3: Einen Testplan erstellen**
- Der **Testplan** ist die Grundlage Ihres Leistungstests. Er legt fest, was Sie testen möchten und wie.
- In der JMeter-GUI ist der Testplan bereits in der linken Spalte vorhanden. Klicken Sie mit der rechten Maustaste darauf, um ihn umzubenennen (z.B. "Web Performance Test") oder lassen Sie ihn so, wie er ist.

---

#### **Schritt 4: Eine Thread-Gruppe hinzufügen**
- Eine **Thread-Gruppe** simuliert Benutzer, die Anfragen an den Server senden.
- Klicken Sie mit der rechten Maustaste auf den Testplan > **Hinzufügen** > **Threads (Benutzer)** > **Thread-Gruppe**.
- Konfigurieren Sie:
  - **Anzahl der Threads (Benutzer)**: Legen Sie fest, wie viele virtuelle Benutzer Sie möchten (z.B. 10).
  - **Ramp-Up-Periode (Sekunden)**: Zeit, die benötigt wird, um alle Threads zu starten (z.B. 10 Sekunden bedeutet 1 Thread pro Sekunde).
  - **Schleifenanzahl**: Anzahl der Wiederholungen des Tests (z.B. 1 oder "Für immer" für kontinuierliches Testen).

---

#### **Schritt 5: Sampler hinzufügen**
- **Sampler** definieren die Anfragen, die an den Server gesendet werden. Für Webtests verwenden Sie den HTTP Request Sampler.
- Klicken Sie mit der rechten Maustaste auf die Thread-Gruppe > **Hinzufügen** > **Sampler** > **HTTP Request**.
- Konfigurieren Sie:
  - **Servername oder IP**: Geben Sie die Ziel-Website ein (z.B. `example.com`).
  - **Pfad**: Geben Sie das Endpunkt an (z.B. `/login`).
  - **Methode**: Wählen Sie `GET`, `POST` usw., basierend auf Ihrem Test-Szenario.

---

#### **Schritt 6: Listener hinzufügen**
- **Listener** zeigen und analysieren die Testergebnisse an.
- Klicken Sie mit der rechten Maustaste auf die Thread-Gruppe > **Hinzufügen** > **Listener** > (z.B. **View Results Tree** oder **Summary Report**).
- Beliebte Optionen:
  - **View Results Tree**: Zeigt detaillierte Anfrage/Antwort-Daten an.
  - **Summary Report**: Bietet aggregierte Metriken wie durchschnittliche Antwortzeit und Fehlerrate.

---

#### **Schritt 7: Den Test konfigurieren**
- Verbessern Sie Ihren Test mit zusätzlichen Elementen (optional, aber nützlich):
  - **Timer**: Fügen Sie Verzögerungen zwischen Anfragen hinzu (z.B. Klicken Sie mit der rechten Maustaste auf Thread-Gruppe > **Hinzufügen** > **Timer** > **Constant Timer**).
  - **Assertions**: Validieren Sie Serverantworten (z.B. Klicken Sie mit der rechten Maustaste auf HTTP Request > **Hinzufügen** > **Assertions** > **Response Assertion**).
  - **Config Elements**: Legen Sie Variablen oder HTTP-Standardwerte fest (z.B. **HTTP Request Defaults**).

---

#### **Schritt 8: Den Test ausführen**
- Speichern Sie Ihren Testplan (**Datei** > **Speichern**) als `.jmx`-Datei zur Wiederverwendung.
- Klicken Sie auf die grüne **Ausführen**-Schaltfläche (Dreieck) in der Symbolleiste oder gehen Sie zu **Ausführen** > **Starten**.
- JMeter führt den Test basierend auf Ihren Thread-Gruppe-Einstellungen aus.

---

#### **Schritt 9: Die Ergebnisse analysieren**
- Nach Abschluss des Tests überprüfen Sie die Listener:
  - **View Results Tree**: Untersuchen Sie einzelne Anfrageerfolge/Fehler.
  - **Summary Report**: Überprüfen Sie Metriken wie Durchsatz, Antwortzeiten und Fehlerprozentsätze.
- Achten Sie auf Engpässe (z.B. langsame Antwortzeiten) oder Fehler, die untersucht werden müssen.

---

#### **Schritt 10: Den Test verfeinern**
- Basierend auf den Ergebnissen passen Sie Ihren Testplan an:
  - Erhöhen oder verringern Sie die Anzahl der Threads.
  - Fügen Sie realistischere Szenarien hinzu (z.B. mehrere HTTP-Anfragen).
  - Passen Sie Timer oder Assertions für Genauigkeit an.
- Speichern und führen Sie den Test erneut aus, um Verbesserungen zu validieren.

---

### Zusätzliche Tipps
- **Speichern und Laden**: Verwenden Sie `.jmx`-Dateien, um Ihren Testplan zu speichern und ihn später über **Datei** > **Öffnen** zu laden.
- **GUI vs. Non-GUI**: Für große Tests führen Sie JMeter im Non-GUI-Modus aus (z.B. `jmeter -n -t test.jmx -l results.jtl`), um Systemressourcen zu sparen.
- **Mehr erfahren**: Erkunden Sie erweiterte Funktionen wie Parameterisierung (für dynamische Daten) oder Korrelation (für dynamische Webanwendungen), wenn Sie Erfahrung sammeln.

Diese Anleitung bietet die Grundlagen, um JMeter effektiv zu nutzen. Mit Übung können Sie Tests anpassen, um spezifische Leistungstestanforderungen zu erfüllen!