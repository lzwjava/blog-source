---
audio: false
generated: true
lang: de
layout: post
title: Installation Des YourKit Java Profilers Unter Ubuntu
translated: true
type: note
---

Um den YourKit Java Profiler auf Ubuntu zu installieren, befolgen Sie diese Schritte basierend auf den Informationen von der YourKit-Website:

1. **Profiler herunterladen**:
   - Besuchen Sie die YourKit Java Profiler Download-Seite unter [https://www.yourkit.com/java/profiler/download/](https://www.yourkit.com/java/profiler/download/).
   - Wählen Sie die Linux-Version des YourKit Java Profiler 2025.3, der Java 8 bis Java 24 unterstützt und mit Linux (einschließlich Ubuntu) auf Architekturen wie arm32, arm64, ppc64le, x64 und x86 kompatibel ist. Stellen Sie sicher, dass Ihr System die [Systemanforderungen](https://www.yourkit.com/docs/java/system-requirements/) für Kompatibilität erfüllt.

2. **Archiv herunterladen**:
   - Laden Sie das `.zip`-Archiv für Linux herunter (z.B. `YourKit-JavaProfiler-2025.3-<Build>.zip`). Der Download-Link ist auf der YourKit Download-Seite verfügbar.

3. **Archiv entpacken**:
   - Öffnen Sie ein Terminal und navigieren Sie zu dem Verzeichnis, in dem sich die heruntergeladene Datei befindet (z.B. `~/Downloads`).
   - Entpacken Sie das Archiv mit dem folgenden Befehl:
     ```bash
     unzip YourKit-JavaProfiler-2025.3-<Build>.zip -d /opt/yourkit
     ```
     Ersetzen Sie `<Build>` durch die tatsächliche Build-Nummer aus der heruntergeladenen Datei. Dieser Befehl extrahiert den Profiler nach `/opt/yourkit`. Sie können ein anderes Verzeichnis wählen, wenn Sie möchten.

4. **Profiler ausführen**:
   - Navigieren Sie in das extrahierte Verzeichnis:
     ```bash
     cd /opt/yourkit
     ```
   - Führen Sie den Profiler mit dem bereitgestellten Skript aus:
     ```bash
     ./bin/profiler.sh
     ```
     Dadurch wird die Benutzeroberfläche des YourKit Java Profilers gestartet.

5. **Optional: Unbeaufsichtigte Installation mit Lizenzschlüssel**:
   - Wenn Sie einen Lizenzschlüssel haben und die Installation automatisieren möchten, können Sie Befehlszeilenoptionen verwenden, um die EULA zu akzeptieren und den Lizenzschlüssel anzuwenden. Zum Beispiel:
     ```bash
     ./bin/profiler.sh -accept-eula -license-key=<Schlüssel>
     ```
     Ersetzen Sie `<Schlüssel>` durch Ihren tatsächlichen Lizenzschlüssel. Dies ist nützlich für Automatisierung oder scriptbasierte Einrichtungen.

6. **In Entwicklungsumgebung integrieren (Optional)**:
   - Wenn Sie eine IDE wie Eclipse, IntelliJ IDEA oder NetBeans verwenden, bietet YourKit Plugins für nahtlose Integration. Für Eclipse zum Beispiel:
     - Öffnen Sie Eclipse und gehen Sie zu **Hilfe > Neue Software installieren**.
     - Fügen Sie das YourKit Plugin-Repository hinzu: `https://www.yourkit.com/download/yjp2025_3_for_eclipse/`.
     - Wählen Sie das YourKit Java Profiler Plugin aus, folgen Sie den Installationsaufforderungen und starten Sie Eclipse bei Bedarf neu.
     - Alternativ können Sie das Offline-Archiv unter `<Profiler Installationsverzeichnis>/lib/eclipse-plugin/yjp2025_3_for_eclipse.zip` verwenden.
   - Nach der Installation erscheint die Aktion "Profile" in der Symbolleiste, im Hauptmenü oder in den Kontextmenüs von Eclipse für einfaches Profiling.

7. **Installation überprüfen**:
   - Sobald der Profiler läuft, ermöglicht Ihnen der Begrüßungsbildschirm, lokal laufende Java-Anwendungen zu überwachen, eine Verbindung zu Remote-Anwendungen herzustellen oder vorhandene Snapshots zu öffnen. Sie können auch eine Demo-Anwendung laden, um die Funktionen des Profilers zu erkunden.

8. **Zusätzliche Hinweise**:
   - Wenn Sie auf Probleme stoßen, stellen Sie sicher, dass Java (Version 8 oder höher) auf Ihrem System installiert ist, da der YourKit Java Profiler eine kompatible JVM benötigt. Sie können Ihre Java-Version mit folgendem Befehl überprüfen:
     ```bash
     java -version
     ```
   - Für Remote-Profiling stellen Sie sicher, dass SSH-Zugriff konfiguriert ist, wenn Sie Anwendungen auf Remote-Servern profilieren.
   - YourKit bietet eine 15-tägige kostenlose Testversion an, sodass zunächst kein Lizenzschlüssel erforderlich ist. Für nicht-kommerzielle Open-Source-Projekte können Sie sich für eine kostenlose Lizenz an den YourKit-Vertrieb wenden.
   - Wenn der Profiler nicht startet (z.B. aufgrund von Leerzeichen im Installationsverzeichnis), verschieben Sie den extrahierten Ordner in einen Pfad ohne Leerzeichen, wie z.B. `/opt/yourkit`.

Für weitere Hilfe konsultieren Sie die [YourKit-Dokumentation](https://www.yourkit.com/docs/java/) oder kontaktieren Sie den Support über die [YourKit-Website](https://www.yourkit.com/support/).

Lassen Sie mich wissen, wenn Sie Hilfe bei einem bestimmten Schritt benötigen!