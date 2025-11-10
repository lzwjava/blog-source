---
audio: false
generated: true
lang: de
layout: post
title: Integration von YourKit Profiler mit WebSphere Liberty unter Windows
translated: true
type: note
---

Die Verwendung des YourKit Java Profilers mit einem WebSphere Liberty Server unter Windows umfasst die Integration des YourKit-Agenten in die WebSphere Liberty JVM und dessen Konfiguration für die Profilerstellung. Nachfolgend sind die Schritte zur Einrichtung aufgeführt, basierend auf verfügbaren Informationen und Best Practices für die Integration von YourKit und WebSphere Liberty:

### Voraussetzungen
- **YourKit Java Profiler**: Installiert auf Ihrem Windows-Rechner. Laden Sie ihn von der [offiziellen YourKit-Website](https://www.yourkit.com/) herunter und stellen Sie sicher, dass Sie einen gültigen Lizenzschlüssel oder Trial-Key besitzen.
- **WebSphere Liberty**: Installiert und ausgeführt auf Ihrem Windows-System. Stellen Sie sicher, dass Sie administrativen Zugriff auf die Server-Konfigurationsdateien haben.
- **Java JDK**: WebSphere Liberty verwendet eine Java-Laufzeitumgebung (IBM JDK oder OpenJDK). Stellen Sie sicher, dass die JDK-Version mit YourKit kompatibel ist (YourKit unterstützt Java 5 und höher, überprüfen Sie jedoch die Kompatibilität mit Ihrer spezifischen Version).
- **Administrative Berechtigungen**: Erforderlich, um die WebSphere Liberty Konfigurationsdateien zu ändern.

### Schritt-für-Schritt-Anleitung

1. **YourKit Java Profiler installieren**
   - Laden Sie den YourKit Java Profiler für Windows von der [YourKit-Website](https://www.yourkit.com/download) herunter und installieren Sie ihn.
   - Notieren Sie sich das Installationsverzeichnis, da Sie den Pfad zur YourKit-Agenten-Bibliothek (`yjpagent.dll`) benötigen.

2. **YourKit-Agenten lokalisieren**
   - Der YourKit-Agent für Windows befindet sich typischerweise unter:
     ```
     C:\Program Files\YourKit-Java-Profiler-<version>\bin\win64\yjpagent.dll
     ```
     (Verwenden Sie `win32` anstelle von `win64`, wenn Sie eine 32-Bit-JVM ausführen.)
   - Stellen Sie sicher, dass der Agent zur JVM-Architektur (32-Bit oder 64-Bit) passt, die von WebSphere Liberty verwendet wird.

3. **WebSphere Liberty für die Verwendung des YourKit-Agenten konfigurieren**
   - **Die Datei `jvm.options` lokalisieren**:
     - Navigieren Sie zum Konfigurationsverzeichnis Ihres WebSphere Liberty Servers, typischerweise:
       ```
       <LIBERTY_INSTALL_DIR>\usr\servers\<server_name>\jvm.options
       ```
       Ersetzen Sie `<LIBERTY_INSTALL_DIR>` durch den Pfad zu Ihrer WebSphere Liberty Installation (z.B. `C:\wlp`) und `<server_name>` durch den Namen Ihres Servers (z.B. `defaultServer`).
     - Wenn die Datei `jvm.options` nicht existiert, erstellen Sie sie im Serververzeichnis.
   - **Den YourKit-Agenten-Pfad hinzufügen**:
     - Öffnen Sie `jvm.options` in einem Texteditor mit administrativen Berechtigungen.
     - Fügen Sie die folgende Zeile hinzu, um den YourKit-Agenten einzubinden:
       ```
       -agentpath:C:\Program Files\YourKit-Java-Profiler-<version>\bin\win64\yjpagent.dll=disablestacktelemetry,disableexceptiontelemetry,delay=10000,probe_disable=*,sessionname=WebSphereLiberty
       ```
       - Ersetzen Sie `<version>` durch Ihre YourKit-Version (z.B. `2023.9`).
       - Die Optionen (`disablestacktelemetry`, `disableexceptiontelemetry`, `probe_disable=*`) reduzieren den Overhead, indem unnötige Telemetrie deaktiviert wird. Die Option `delay=10000` stellt sicher, dass der Agent startet, nachdem der Server initialisiert wurde, und `sessionname=WebSphereLiberty` identifiziert die Profiling-Sitzung.
       - Beispiel:
         ```
         -agentpath:C:\Program Files\YourKit-Java-Profiler-2023.9\bin\win64\yjpagent.dll=disablestacktelemetry,disableexceptiontelemetry,delay=10000,probe_disable=*,sessionname=WebSphereLiberty
         ```
   - **Datei speichern**: Stellen Sie sicher, dass Sie Schreibberechtigungen für die Datei `jvm.options` haben.

4. **JVM-Kompatibilität überprüfen**
   - WebSphere Liberty verwendet oft IBM JDK oder OpenJDK. YourKit ist mit beiden kompatibel, aber falls Sie auf Probleme stoßen (z.B. `NoSuchMethodError`, wie in einigen IBM JDK-Fällen dokumentiert), fügen Sie `probe_disable=*` zum Agent-Pfad hinzu, um Probes zu deaktivieren, die Konflikte mit dem IBM JDK verursachen könnten.[](https://www.yourkit.com/forum/viewtopic.php?f=3&t=8042)
   - Überprüfen Sie die von Liberty verwendete Java-Version:
     ```
     <LIBERTY_INSTALL_DIR>\java\bin\java -version
     ```
     Stellen Sie sicher, dass sie von YourKit unterstützt wird (Java 5 oder höher für ältere Versionen; moderne Versionen unterstützen Java 8+).

5. **WebSphere Liberty starten**
   - Starten Sie Ihren WebSphere Liberty Server wie gewohnt:
     ```
     <LIBERTY_INSTALL_DIR>\bin\server start <server_name>
     ```
     Beispiel:
     ```
     C:\wlp\bin\server start defaultServer
     ```
   - Überprüfen Sie die Server-Logs (`<LIBERTY_INSTALL_DIR>\usr\servers\<server_name>\logs\console.log` oder `messages.log`) auf Fehler im Zusammenhang mit dem YourKit-Agenten.
   - Suchen Sie nach dem YourKit-Agenten-Log in:
     ```
     %USERPROFILE%\.yjp\log\<session_name>-<pid>.log
     ```
     Beispiel:
     ```
     C:\Users\<IhrBenutzername>\.yjp\log\WebSphereLiberty-<pid>.log
     ```
     Das Log sollte anzeigen, dass der Agent geladen ist und auf einen Port lauscht (Standard: 10001):
     ```
     Profiler agent is listening on port 10001
     ```

6. **YourKit Profiler UI verbinden**
   - Starten Sie die YourKit Java Profiler UI auf Ihrem Windows-Rechner.
   - Wählen Sie in der YourKit-UI **Profile | Profile Local Java Server or Application** oder **Profile | Profile Remote Java Server or Application**.
     - Für lokales Profiling (da YourKit und Liberty auf demselben Rechner laufen), wählen Sie **Profile Local Java Server or Application**.
     - Die UI sollte den WebSphere Liberty Prozess erkennen (identifiziert durch `sessionname=WebSphereLiberty`).
   - Falls er nicht automatisch erkannt wird, verwenden Sie **Profile Remote Java Server or Application**, wählen Sie **Direct Connect** und geben Sie ein:
     - **Host**: `localhost`
     - **Port**: `10001` (oder den im Agenten-Log angegebenen Port).
   - Verbinden Sie sich mit dem Server. Die UI zeigt CPU-, Speicher- und Thread-Telemetriedaten an.

7. **Die Anwendung profilieren**
   - Verwenden Sie die YourKit-UI, um:
     - **CPU-Profiling**: Aktivieren Sie CPU-Sampling oder Tracing, um Performance-Engpässe zu identifizieren. Vermeiden Sie das Aktivieren von "Profile J2EE" für Systeme mit hoher Last, um den Overhead zu minimieren.[](https://www.jahia.com/blog/analyzing-system-performance-with-yourkit-java-profiler)
     - **Speicher-Profiling**: Analysieren Sie die Heap-Nutzung und erkennen Sie Speicherlecks, indem Sie Objekte nach Webanwendung gruppieren (nützlich für Liberty-gehostete Apps).[](https://www.yourkit.com/docs/java-profiler/latest/help/webapps.jsp)
     - **Thread-Analyse**: Überprüfen Sie im Threads-Tab auf Deadlocks oder eingefrorene Threads.[](https://www.yourkit.com/changes/)
   - Erstellen Sie bei Bedarf Snapshots für die Offline-Analyse (File | Save Snapshot).
   - Überwachen Sie die Speichernutzung, da Profiling den Speicherverbrauch erhöhen kann. Vermeiden Sie lange Profiling-Sitzungen ohne Überwachung.[](https://www.jahia.com/blog/analyzing-system-performance-with-yourkit-java-profiler)

8. **Fehlerbehebung**
   - **Server startet nicht oder ist nicht erreichbar**:
     - Überprüfen Sie die Logs (`console.log`, `messages.log` und YourKit-Agenten-Log) auf Fehler wie `OutOfMemoryError` oder `NoSuchMethodError`.[](https://www.yourkit.com/forum/viewtopic.php?t=328)[](https://www.yourkit.com/forum/viewtopic.php?t=16205)
     - Stellen Sie sicher, dass `-agentpath` zur korrekten `jvm.options`-Datei hinzugefügt wurde und mit dem Skript übereinstimmt, das zum Starten von Liberty verwendet wird.[](https://www.yourkit.com/forum/viewtopic.php?t=16205)
     - Falls IBM JDK verwendet wird, versuchen Sie, `probe_disable=*` zum Agent-Pfad hinzuzufügen, um Konflikte zu vermeiden.[](https://www.yourkit.com/forum/viewtopic.php?f=3&t=8042)
   - **ClassNotFoundException**:
     - Wenn Sie Fehler wie `java.lang.ClassNotFoundException` sehen (z.B. für `java.util.ServiceLoader`), stellen Sie sicher, dass die YourKit-Agenten-Version mit Ihrem JDK kompatibel ist. Für ältere IBM JDKs (z.B. Java 5) verwenden Sie YourKit 8.0 oder älter.[](https://www.yourkit.com/forum/viewtopic.php?f=3&t=7149)
   - **Keine Profiling-Daten**:
     - Stellen Sie sicher, dass die Versionen des YourKit-Agenten und der UI übereinstimmen. Unterschiedliche Versionen können Verbindungsprobleme verursachen.[](https://www.yourkit.com/forum/viewtopic.php?t=328)
     - Stellen Sie sicher, dass der Server über den Browser erreichbar ist (z.B. `https://localhost:9443` bei Verwendung von SSL). Falls nicht, überprüfen Sie die Firewall-Einstellungen oder die SSL-Konfiguration.[](https://www.yourkit.com/forum/viewtopic.php?t=16205)
   - **Log-Datei-Probleme**:
     - Falls kein YourKit-Log in `~/.yjp/log/` erstellt wird, stellen Sie sicher, dass der Prozess Schreibberechtigungen für das Home-Verzeichnis des Benutzers hat.[](https://www.yourkit.com/forum/viewtopic.php?f=3&t=3219)
   - **Performance-Auswirkungen**:
     - Profiling kann die Performance beeinträchtigen. Verwenden Sie minimale Einstellungen (z.B. Deaktivierung der Stack-Telemetrie) für produktionsähnliche Umgebungen.[](https://www.jahia.com/blog/analyzing-system-performance-with-yourkit-java-profiler)

9. **Optional: Den YourKit-Integrations-Assistenten verwenden**
   - YourKit bietet einen Java Server Integration Wizard zur Vereinfachung der Konfiguration:
     - Starten Sie die YourKit-UI und wählen Sie **Profile | Profile Local Java Server or Application**.
     - Wählen Sie **WebSphere Liberty** aus der Liste der unterstützten Server (oder "Other Java application", falls Liberty nicht aufgeführt ist).
     - Folgen Sie dem Assistenten, um die notwendigen `-agentpath`-Einstellungen zu generieren und `jvm.options` zu aktualisieren. Stellen Sie sicher, dass Sie Schreibberechtigungen für die Konfigurationsdateien haben.[](https://www.yourkit.com/docs/java-profiler/latest/help/java-server-integration-wizard.jsp)
   - Dies ist besonders nützlich, um korrekte Pfade und Einstellungen sicherzustellen.

10. **Profiling beenden**
    - Um Profiling zu deaktivieren, entfernen oder kommentieren Sie die `-agentpath`-Zeile in `jvm.options` aus und starten Sie den Server neu.
    - Alternativ stoppen Sie den Server:
      ```
      <LIBERTY_INSTALL_DIR>\bin\server stop <server_name>
      ```

### Zusätzliche Hinweise
- **Lizenz**: Für den YourKit-Agenten auf dem Server ist kein Lizenzschlüssel erforderlich; die Lizenz wird in der YourKit-UI angewendet. Für Remote-Profiling von einem anderen Windows-Rechner stellen Sie sicher, dass die UI über eine gültige Lizenz verfügt.[](https://www.yourkit.com/forum/viewtopic.php?f=3&t=11385)[](https://www.yourkit.com/forum/viewtopic.php?t=11385)
- **Remote-Profiling**: Falls Sie von einem anderen Rechner aus profilen, stellen Sie die Netzwerkverbindbarkeit zum Agenten-Port (Standard: 10001) sicher und verwenden Sie die Option **Profile Remote Java Server or Application** mit dem Hostnamen/die IP des Servers.
- **Performance-Überlegungen**: Profiling kann die Speicher- und CPU-Nutzung erhöhen. Für Produktionssysteme beginnen Sie mit minimalen Profiling-Optionen (z.B. CPU-Sampling) und überwachen Sie die Server-Gesundheit.[](https://www.jahia.com/blog/analyzing-system-performance-with-yourkit-java-profiler)
- **Kompatibilität**: Falls Sie eine ältere WebSphere Liberty-Version mit IBM JDK 1.4.2 oder 1.5 verwenden, benötigen Sie möglicherweise eine ältere YourKit-Version (z.B. 8.0 für Java 5).[](https://www.yourkit.com/forum/viewtopic.php?f=3&t=7149)[](https://stackoverflow.com/questions/61795/java-profiler-for-ibm-jvm-1-4-2-websphere-6-0-2)
- **Dokumentation**: Konsultieren Sie die offizielle YourKit-Dokumentation für detaillierte Profiling-Optionen: [YourKit Java Profiler Help](https://www.yourkit.com/docs/java/help/).[](https://www.jahia.com/blog/analyzing-system-performance-with-yourkit-java-profiler)

### Beispielkonfiguration
Hier ist eine Beispiel-`jvm.options`-Datei:
```
-Xmx4G
-Xms4G
-agentpath:C:\Program Files\YourKit-Java-Profiler-2023.9\bin\win64\yjpagent.dll=disablestacktelemetry,disableexceptiontelemetry,delay=10000,probe_disable=*,sessionname=WebSphereLiberty
```

### Testen des Setups
- Nachdem der Server gestartet wurde, greifen Sie auf Ihre Anwendung zu (z.B. `https://localhost:9443`), um sicherzustellen, dass sie läuft.
- Verifizieren Sie in der YourKit-UI, dass Telemetriedaten (CPU, Speicher, Threads) angezeigt werden.
- Falls Probleme auftreten, überprüfen Sie den YourKit-Agenten-Log und die Liberty-Logs auf Fehler.

Wenn Sie auf spezifische Fehler stoßen oder Hilfe bei einem bestimmten Schritt benötigen, lassen Sie es mich wissen, und ich kann weitere Unterstützung bieten!