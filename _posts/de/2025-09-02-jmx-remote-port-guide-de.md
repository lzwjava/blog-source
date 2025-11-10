---
audio: false
generated: true
image: false
lang: de
layout: post
title: Leitfaden zum JMX-Remote-Agent-Port
translated: true
type: note
---

Der **JMX-Remote-Agent** ist Teil der Java Management Extensions (JMX)-Technologie. Er ermöglicht Administratoren oder Monitoring-Tools, eine Verbindung zu einer laufenden Java-Anwendung von außerhalb des JVM-Prozesses herzustellen, typischerweise über TCP/IP. Dies wird häufig für die Überwachung, Diagnose und Verwaltung von Java-Anwendungen in Produktionsumgebungen verwendet.

Hier eine Aufschlüsselung:

### 1. Was der JMX-Remote-Agent ist

* Er stellt JVM-Interne (Speichernutzung, Thread-Aktivität, Garbage Collection, Klassenladung, etc.) als *Managed Beans (MBeans)* bereit.
* Er ermöglicht es Ihnen, sich remote zu verbinden (z.B. via **jconsole**, **VisualVM** oder Monitoring-Tools wie Prometheus Exporters).
* Er wird normalerweise durch JVM-Startflags aktiviert, wie:

  ```bash
  -Dcom.sun.management.jmxremote
  -Dcom.sun.management.jmxremote.port=9091
  -Dcom.sun.management.jmxremote.authenticate=false
  -Dcom.sun.management.jmxremote.ssl=false
  ```
* Einmal aktiviert, führt die JVM einen RMI (Remote Method Invocation)-Connector-Server aus, der an den angegebenen Port gebunden ist.

### 2. Über Port 9091

* Die Nummer **9091** selbst ist nicht speziell; es ist nur ein TCP-Port, den Sie für JMX-Verbindungen konfigurieren.
* Oft wählen Administratoren 9091 (oder 9010, 9999, etc.) aus Bequemlichkeit und um Konflikte mit Standardports zu vermeiden.
* Wenn auf `9091` gelauscht wird, akzeptiert die JVM remote JMX-Verbindungen an diesem Port.
* Wenn er ungesichert bleibt (`authenticate=false, ssl=false`), kann jeder mit Netzwerkzugriff Ihre JVM steuern oder beobachten – was ein erhebliches Sicherheitsrisiko darstellt.

### 3. Typische Verwendung

* Monitoring mit **JConsole**:

  ```bash
  jconsole host:9091
  ```
* Integration in Monitoring-Systeme (z.B. Prometheus JMX Exporter).
* Remote-Management während der Fehlerbehebung (z.B. Prüfen von Heap Dumps, Threads, GC-Verhalten).

### 4. Sicherheitsüberlegungen

* Schützen Sie den JMX-Port immer mit:

  * Netzwerk-Firewalls (Zugriff einschränken).
  * Authentifizierung (`password` und `access` Dateien).
  * SSL falls erforderlich.
* Andernfalls ist das Exponieren auf 9091 ohne Sicherheit gleichbedeutend mit der Vergabe von Remote-Shell-Level-Kontrolle über Ihre JVM.

---

✅ Kurz gesagt: **JMX-Remote-Agent auf Port 9091** bedeutet, dass Ihre JVM eine Management- und Monitoring-Schnittstelle über TCP-Port 9091 bereitstellt, die von Tools wie JConsole oder Prometheus genutzt werden kann, aber gesichert werden muss.

Möchten Sie, dass ich Ihnen die **exakten JVM-Flags** zeige, um ihn mit Passwort-Authentifizierung (anstatt des ungesicherten Modus) zu aktivieren?