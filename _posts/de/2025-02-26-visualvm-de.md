---
audio: false
lang: de
layout: post
title: Profiling Java-Anwendungen mit VisualVM
translated: true
---

Hier ist eine klare und prägnante Anleitung zur Verwendung von **VisualVM** zum Überwachen und Profilieren von Java-Anwendungen. VisualVM ist ein kostenloses, leistungsfähiges Tool, das mit dem JDK geliefert wird und Ihnen hilft, die Leistung, den Speicherverbrauch und die Thread-Aktivität Ihrer Java-Anwendungen zu analysieren.

---

### Schritt 1: Installieren und Starten von VisualVM
- **Überprüfen Sie, ob VisualVM installiert ist**: VisualVM ist normalerweise im JDK enthalten (ab Version 6 Update 7). Suchen Sie es im `bin`-Verzeichnis Ihrer JDK-Installation (z.B. `jdk/bin/visualvm.exe` unter Windows).
- **Herunterladen, falls erforderlich**: Wenn es nicht enthalten ist, laden Sie es von der [offiziellen VisualVM-Website](https://visualvm.github.io/) herunter.
- **VisualVM starten**: Führen Sie die `visualvm`-Ausführbare Datei aus. Beim Start sehen Sie eine Liste der Java-Prozesse, die derzeit auf Ihrem lokalen Computer laufen.

---

### Schritt 2: Verbinden mit Ihrer Java-Anwendung
- **Lokale Anwendungen**: VisualVM erkennt automatisch laufende Java-Prozesse auf Ihrem Computer. Doppelklicken Sie auf den Prozess, den Sie überwachen möchten, um eine Verbindung herzustellen.
- **Remote-Anwendungen**: Um einen Java-Prozess auf einem anderen Computer zu überwachen:
  1. Starten Sie die entfernte JVM mit aktiviertem JMX (z.B. fügen Sie `-Dcom.sun.management.jmxremote` zu den JVM-Argumenten hinzu).
  2. Klicken Sie in VisualVM mit der rechten Maustaste auf **Remote** im linken Bereich, wählen Sie **Remote Host hinzufügen** und geben Sie die Details des entfernten Computers ein.
  3. Nach dem Verbinden wählen Sie den entfernten Prozess zur Überwachung aus.

---

### Schritt 3: Überwachen der Anwendungsleistung
Nach dem Verbinden zeigt die Registerkarte **Übersicht** grundlegende Details wie Prozess-ID und JVM-Argumente an. Wechseln Sie zur Registerkarte **Überwachen**, um Echtzeit-Leistungsdaten zu erhalten:
- **CPU-Nutzung**: Verfolgt, wie viel CPU Ihre Anwendung verwendet.
- **Speichernutzung**: Zeigt den Heap- und Metaspace-Verbrauch im Laufe der Zeit an.
- **Threads**: Zeigt die Anzahl der aktiven Threads an.
- **Garbage Collection**: Überwacht die GC-Aktivität.

Diese Diagramme geben Ihnen einen Überblick über den Zustand Ihrer Anwendung.

---

### Schritt 4: Profilieren der CPU- und Speichernutzung
Für eine tiefere Analyse verwenden Sie die Registerkarte **Profiler**:
- **CPU-Profiling**: Identifiziert Methoden, die die meiste CPU-Zeit verbrauchen.
  1. Gehen Sie zur Registerkarte **Profiler** und klicken Sie auf **CPU**.
  2. Klicken Sie auf **Start**, um das Profiling zu beginnen.
  3. Verwenden Sie Ihre Anwendung, um die Arbeitslast zu erzeugen, die Sie analysieren möchten.
  4. Klicken Sie auf **Stop** und überprüfen Sie die Ergebnisse, um zu sehen, welche Methoden am langsamsten sind.
- **Speicherprofiling**: Verfolgt Objektzuweisungen und erkennt Speicherlecks.
  1. Klicken Sie in der Registerkarte **Profiler** auf **Speicher**.
  2. Klicken Sie auf **Start**, verwenden Sie Ihre Anwendung und klicken Sie dann auf **Stop**.
  3. Überprüfen Sie die Ergebnisse auf Objektanzahlen und -größen, um mögliche Speicherprobleme zu erkennen.

**Hinweis**: Profiling verursacht Overhead, verwenden Sie es daher in Entwicklungs- oder Testumgebungen, nicht in der Produktion.

---

### Schritt 5: Analysieren von Heap- und Thread-Dumps
- **Heap-Dumps**: Erfassen Sie Speicherschnappschüsse für eine detaillierte Analyse.
  1. Klicken Sie in der Registerkarte **Überwachen** auf **Heap-Dump**.
  2. Untersuchen Sie den Dump in den Ansichten **Klassen** oder **Instanzen**, um Objektzuweisungen zu sehen.
  3. Achten Sie auf ungewöhnliche Muster (z.B. zu viele Objekte), die auf Lecks hinweisen könnten.
- **Thread-Dumps**: Diagnostizieren Sie Thread-Probleme wie Deadlocks.
  1. Klicken Sie in der Registerkarte **Threads** auf **Thread-Dump**.
  2. Überprüfen Sie die Thread-Zustände (z.B. RUNNABLE, WAITING), um Probleme zu identifizieren.

---

### Schritt 6: Zusätzliche Funktionen erkunden
- **Sampler**: In der Registerkarte **Sampler** finden Sie eine leichtere CPU- und Speicheranalyse mit weniger Overhead als beim vollständigen Profiling.
- **Visual GC**: Installieren Sie das Visual GC-Plugin (über **Tools > Plugins**), um das Verhalten der Garbage Collection zu visualisieren.
- **MBeans**: Verwenden Sie die Registerkarte **MBeans**, um JMX-Bean für benutzerdefinierte Metriken anzuzeigen und zu verwalten.

---

### Best Practices
- **Vermeiden Sie das Profiling in der Produktion**: Profiling verlangsamt Ihre Anwendung, daher sollten Sie es nur in Entwicklungs- oder Testumgebungen verwenden.
- **Fangen Sie einfach an**: Verwenden Sie die Registerkarte **Überwachen**, um eine Basislinie zu erhalten, bevor Sie profilieren.
- **Zielen Sie auf spezifische Probleme**: Fokussieren Sie das Profiling auf vermutete Problembereiche, um den Overhead zu minimieren.
- **Überprüfen Sie GC-Daten**: Analysieren Sie die Garbage Collection-Statistiken, um den Speicherverbrauch zu optimieren.

---

### Fehlerbehebung
- **Anwendung wird nicht angezeigt**: Stellen Sie sicher, dass sie mit einer kompatiblen JVM läuft und dass VisualVM Zugriff hat.
- **Remote-Probleme**: Stellen Sie sicher, dass die entfernte JVM für JMX konfiguriert ist und dass die Netzwerkeinstellungen (z.B. Firewalls) die Verbindung zulassen.
- **Leistungseinfluss**: Wenn das Profiling zu langsam ist, wechseln Sie zum **Sampler** für eine leichtere Option.

---

VisualVM ist ein hervorragendes Tool, um Ihre Java-Anwendungen zu verstehen und zu optimieren. Folgen Sie diesen Schritten, um die Leistung zu überwachen, Engpässe zu profilieren und Probleme effektiv zu diagnostizieren. Für weitere Details besuchen Sie die [offizielle VisualVM-Dokumentation](https://visualvm.github.io/documentation.html).