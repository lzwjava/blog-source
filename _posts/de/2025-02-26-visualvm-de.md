---
audio: false
generated: true
lang: de
layout: post
title: Profilerstellung für Java-Anwendungen mit VisualVM
translated: true
type: note
---

Hier ist eine klare und prägnante Anleitung zur Verwendung von **VisualVM** zur Überwachung und Profilerstellung von Java-Anwendungen. VisualVM ist ein kostenloses, leistungsstarkes Tool, das im JDK enthalten ist und Ihnen hilft, die Leistung, Speichernutzung und Thread-Aktivität Ihrer Java-Anwendungen zu analysieren.

---

### Schritt 1: VisualVM installieren und starten
- **Prüfen, ob VisualVM installiert ist**: VisualVM ist typischerweise im JDK (ab Version 6 Update 7) enthalten. Suchen Sie danach im `bin`-Verzeichnis Ihrer JDK-Installation (z. B. `jdk/bin/visualvm.exe` unter Windows).
- **Bei Bedarf herunterladen**: Falls es nicht enthalten ist, laden Sie es von der [offiziellen VisualVM-Website](https://visualvm.github.io/) herunter.
- **VisualVM starten**: Führen Sie die `visualvm`-Executable aus. Nach dem Start sehen Sie eine Liste der Java-Prozesse, die derzeit auf Ihrem lokalen Rechner ausgeführt werden.

---

### Schritt 2: Mit Ihrer Java-Anwendung verbinden
- **Lokale Anwendungen**: VisualVM erkennt automatisch laufende Java-Prozesse auf Ihrem Rechner. Doppelklicken Sie auf den Prozess, den Sie überwachen möchten, um eine Verbindung herzustellen.
- **Remote-Anwendungen**: Um einen Java-Prozess auf einem anderen Rechner zu überwachen:
  1. Starten Sie die Remote-JVM mit aktiviertem JMX (fügen Sie z. B. `-Dcom.sun.management.jmxremote` zu den JVM-Argumenten hinzu).
  2. Klicken Sie in VisualVM im linken Bereich mit der rechten Maustaste auf **Remote**, wählen Sie **Add Remote Host** und geben Sie die Details des Remote-Rechners ein.
  3. Wählen Sie nach erfolgreicher Verbindung den zu überwachenden Remote-Prozess aus.

---

### Schritt 3: Anwendungsleistung überwachen
Nach dem Verbinden zeigt die Registerkarte **Overview** grundlegende Details wie Prozess-ID und JVM-Argumente an. Wechseln Sie zur Registerkarte **Monitor**, um Echtzeit-Leistungsdaten zu sehen:
- **CPU-Auslastung**: Zeigt, wie viel CPU Ihre Anwendung verwendet.
- **Speichernutzung**: Zeigt die Heap- und Metaspace-Auslastung über die Zeit.
- **Threads**: Zeigt die Anzahl der aktiven Threads.
- **Garbage Collection**: Überwacht die GC-Aktivität.

Diese Diagramme geben Ihnen einen Überblick über den Gesundheitszustand Ihrer Anwendung.

---

### Schritt 4: CPU- und Speichernutzung profilieren
Für eine tiefgehende Analyse verwenden Sie die Registerkarte **Profiler**:
- **CPU-Profiling**: Identifiziert Methoden, die die meiste CPU-Zeit verbrauchen.
  1. Gehen Sie zur Registerkarte **Profiler** und klicken Sie auf **CPU**.
  2. Klicken Sie auf **Start**, um mit der Profilerstellung zu beginnen.
  3. Verwenden Sie Ihre Anwendung, um die gewünschte Arbeitslast zu erzeugen.
  4. Klicken Sie auf **Stop** und überprüfen Sie die Ergebnisse, um die langsamsten Methoden zu sehen.
- **Memory-Profiling**: Verfolgt Objektallokationen und erkennt Memory Leaks.
  1. Klicken Sie in der Registerkarte **Profiler** auf **Memory**.
  2. Klicken Sie auf **Start**, verwenden Sie Ihre Anwendung und klicken Sie dann auf **Stop**.
  3. Überprüfen Sie die Ergebnisse hinsichtlich Objektanzahlen und -größen, um potenzielle Speicherprobleme zu erkennen.

**Hinweis**: Die Profilerstellung verursacht Overhead. Verwenden Sie sie daher in Entwicklungs- oder Testumgebungen, nicht in der Produktion.

---

### Schritt 5: Heap- und Thread-Dumps analysieren
- **Heap-Dumps**: Erstellen Sie Speicherschnappschüsse für eine detaillierte Analyse.
  1. Klicken Sie in der Registerkarte **Monitor** auf **Heap Dump**.
  2. Untersuchen Sie den Dump in den Ansichten **Classes** oder **Instances**, um die Objektallokationen zu sehen.
  3. Suchen Sie nach ungewöhnlichen Mustern (z. B. zu viele Objekte), die auf Memory Leaks hindeuten könnten.
- **Thread-Dumps**: Diagnostizieren Sie Threading-Probleme wie Deadlocks.
  1. Klicken Sie in der Registerkarte **Threads** auf **Thread Dump**.
  2. Überprüfen Sie die Thread-Zustände (z. B. RUNNABLE, WAITING), um Probleme zu identifizieren.

---

### Schritt 6: Zusätzliche Funktionen erkunden
- **Sampler**: Befindet sich in der Registerkarte **Sampler** und bietet eine leichtgewichtige CPU- und Speicheranalyse mit weniger Overhead als die vollständige Profilerstellung.
- **Visual GC**: Installieren Sie das Visual GC-Plugin (über **Tools > Plugins**), um das Garbage Collection-Verhalten zu visualisieren.
- **MBeans**: Verwenden Sie die Registerkarte **MBeans**, um JMX-Beans für benutzerdefinierte Metriken anzuzeigen und zu verwalten.

---

### Best Practices
- **Vermeiden Sie Profiling in der Produktion**: Die Profilerstellung verlangsamt Ihre Anwendung. Beschränken Sie sich daher auf Entwicklungs- oder Testumgebungen.
- **Beginnen Sie einfach**: Verwenden Sie zuerst die Registerkarte **Monitor**, um eine Baseline zu erhalten, bevor Sie mit der Profilerstellung beginnen.
- **Konzentrieren Sie sich auf spezifische Probleme**: Fokussieren Sie die Profilerstellung auf vermutete Problembereiche, um den Overhead zu minimieren.
- **Überprüfen Sie GC-Daten**: Analysieren Sie die Garbage Collection-Statistiken, um die Speichernutzung zu optimieren.

---

### Problembehandlung
- **Anwendung wird nicht angezeigt**: Stellen Sie sicher, dass sie mit einer kompatiblen JVM läuft und dass VisualVM Zugriff darauf hat.
- **Probleme mit Remote-Verbindungen**: Stellen Sie sicher, dass die Remote-JVM für JMX konfiguriert ist und dass die Netzwerkeinstellungen (z. B. Firewalls) die Verbindung erlauben.
- **Leistungsbeeinträchtigung**: Wenn die Profilerstellung zu langsam ist, wechseln Sie zum **Sampler** für eine leichtgewichtige Alternative.

---

VisualVM ist ein hervorragendes Tool, um Ihre Java-Anwendungen zu verstehen und zu optimieren. Befolgen Sie diese Schritte, um die Leistung zu überwachen, Engpässe zu identifizieren und Probleme effektiv zu diagnostizieren. Weitere Details finden Sie in der [offiziellen VisualVM-Dokumentation](https://visualvm.github.io/documentation.html).