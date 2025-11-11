---
audio: false
generated: true
image: false
lang: de
layout: post
title: Profiling Liberty mit dem YourKit Java Profiler
translated: true
type: note
---

WebSphere Liberty lässt sich recht problemlos mit YourKit Java Profiler integrieren, da Liberty lediglich eine weitere JVM-basierte Laufzeitumgebung ist. So funktioniert es typischerweise:

---

### 1. Funktionsweise der Integration

YourKit Java Profiler benötigt keine Liberty-spezifischen Plugins; es funktioniert, indem es sich an den JVM-Prozess anhaftet, in dem Liberty läuft. Sobald es angehängt ist, fängt es Methodenaufrufe, Speicherzuweisungen, Thread-Aktivität und andere Laufzeit-Ereignisse ab.
Liberty läuft auf der OpenJ9- (oder HotSpot-) JVM, daher können Sie die Profilerstellung aktivieren, indem Sie den YourKit-Agenten zum Start von Liberty hinzufügen.

---

### 2. Anhängen des YourKit-Agenten

Es gibt zwei Hauptmethoden:

* **Startzeit-Anbindung (bevorzugt für Server)**
  Fügen Sie die YourKit-Agenten-Optionen zur `jvm.options`-Datei von Liberty hinzu (in `<wlp_home>/usr/servers/<server_name>/`).
  Beispiel:

  ```
  -agentpath:/pfad/zur/yourkit/bin/linux-x86-64/libyjpagent.so=port=10001,listen=all
  ```

  Dies lädt den Profiler-Agenten, sobald der Server startet.

* **Bedarfsgesteuerte (dynamische) Anbindung**
  Wenn Liberty bereits läuft, können Sie YourKit über die GUI anbinden. Es scannt nach laufenden JVMs und ermöglicht eine Verbindung ohne Neustart. Nützlich für Produktions-Debugging, erfordert aber Berechtigungen (gleicher Benutzer / JDK tools.jar).

---

### 3. Profilerstellung im Liberty-Kontext

Bei der Ausführung auf Liberty möchten Sie möglicherweise:

* **Nach Anwendungspaketen filtern**, um nicht im internen Liberty-Code unterzugehen.
* **Die Aufrufbaum- / Hotspots-Ansicht verwenden**, um langsame Servlets, JAX-RS-Endpunkte oder CDI-Beans zu analysieren.
* **JDBC- und Thread-Pools überwachen**, da Liberty-Anwendungen oft auf container-verwaltete Ressourcen angewiesen sind. YourKit kann JDBC-Aufrufe verfolgen und Wartezeiten messen.
* **Mehrere Apps behandeln** – wenn Liberty mehrere Apps hostet, verwenden Sie die Thread- und Klassenfilter von YourKit, um die Profilerstellung auf die gewünschte Anwendung einzugrenzen.

---

### 4. Leistungsüberlegungen

* Profilerstellung verursacht immer Overhead. Für die Entwicklung ist die volle CPU-/Speicher-Profilerstellung in Ordnung; in der Produktion verwenden Sie stattdessen den *Sampling*-Modus anstelle von Instrumentierung.
* Die modulare Klassenladung von Liberty kann manchmal zu doppelten Klassennamen führen; YourKit kommt damit generally zurecht, aber seien Sie bei der Filterung achtsam.
* Wenn Sie IBM JDK mit Liberty verwenden, stellen Sie sicher, dass Sie den YourKit-Agenten herunterladen, der für IBM J9/OpenJ9 erstellt wurde, und nicht nur für HotSpot.

---

### 5. Typischer Workflow

1. Installieren Sie YourKit auf Ihrem Entwicklungsrechner.
2. Modifizieren Sie Liberty's `jvm.options` mit dem Agenten-Pfad.
3. Starten Sie Liberty.
4. Verbinden Sie sich von der YourKit-GUI mit der Liberty-JVM (über Socket oder Anhängen).
5. Erstellen Sie Profile für Ihre Endpunkte, Speichernutzung oder Thread-Sperren.
6. Speichern Sie Snapshots für die Offline-Analyse.

---

👉 Möchten Sie, dass ich Ihnen ein **Schritt-für-Schritt-Konfigurationsbeispiel** für Liberty auf **OpenJ9** (der standardmäßigen Liberty-JVM) mit YourKit gebe, einschließlich beispielhafter `jvm.options`-Einstellungen für CPU- vs. Speicher-Profilerstellung?