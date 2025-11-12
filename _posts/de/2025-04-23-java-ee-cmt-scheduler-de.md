---
audio: false
generated: true
image: false
lang: de
layout: post
title: Java-EE-Container-verwalteter Aufgabenplaner
translated: true
type: note
---

Ein **ManagedScheduledExecutorService** ist eine Java EE- (Jakarta EE-) Ressource, die vom Application Server (z. B. WebSphere, WebLogic, WildFly) bereitgestellt wird. Sie ermöglicht es, Tasks für eine spätere oder periodische Ausführung zu planen, ähnlich wie `ScheduledExecutorService` im Standard-Java SE, jedoch mit **Container-gemanagten Vorteilen**:

---

### Funktionsweise

* **Integration mit dem Container**
  Er wird vom Application Server verwaltet, was bedeutet, dass Tasks im Sicherheitskontext, Classloader und innerhalb der Transaktionsgrenzen der Anwendung ausgeführt werden. Dies vermeidet häufige Probleme von nicht verwalteten Threads in Java EE.

* **Planungsfähigkeiten**
  Sie können Tasks so planen, dass sie:

  * Einmal nach einer Verzögerung ausgeführt werden.
  * In einem festen Intervall ausgeführt werden (z. B. alle 5 Sekunden).
  * Mit einer festen Verzögerung zwischen den Ausführungen laufen.

* **Lifecycle-Management**
  Der Container kümmert sich um den Thread-Pool-Lifecycle, die Bereinigung und das Ressourcenmanagement. Sie müssen ihn nicht manuell beenden, wie einen einfachen `ExecutorService`.

---

### Timeout

* Es gibt keine einzelne "Timeout"-Einstellung für den Pool selbst, aber zwei Dinge sind relevant:

  * **Task-Ausführungs-Timeout**: Sie können Tasks mit einem `ManagedTaskListener` versehen und Eigenschaften wie `ManagedTask.TIMEOUT` angeben (abhängig von der Herstellerunterstützung). Einige Server erlauben es, Standard-Task-Timeouts zu konfigurieren, sodass hängende Tasks vom Container abgebrochen werden.
  * **Future get()-Timeout**: Wie bei der regulären `ScheduledExecutorService` können Sie `future.get(timeout, unit)` verwenden, um zu begrenzen, wie lange Sie auf Ergebnisse warten.

"Timeout" bezieht sich also normalerweise auf den einzelnen Task, nicht auf die Pool-Ebene.

---

### Poolgrößen-Konfiguration

* Jeder Application Server hat seine eigene Konfiguration für den zugrundeliegenden Thread-Pool.
  Beispiele:

  * **WebSphere Liberty / Traditional**: Sie konfigurieren den Pool in der `server.xml` unter `<managedScheduledExecutorService>` mit Attributen wie `corePoolSize` und `maximumPoolSize`.
  * **WebLogic**: Sie konfigurieren ihn über die Admin Console oder `weblogic-managed-executor`.
  * **WildFly / JBoss EAP**: wird im EE-Subsystem konfiguriert.

* Typische Pool-Konfigurationen umfassen:

  * **Core Pool Size**: Minimale Anzahl an Threads, die aktiv gehalten werden.
  * **Maximale Poolgröße**: Maximale Anzahl gleichzeitiger Threads.
  * **Warteschlangengröße / Rejection Policy**: Was passiert, wenn alle Threads beschäftigt sind.
  * **Keep-Alive-Zeit**: Wie lange inaktive Threads gehalten werden, bevor sie freigegeben werden.

---

✅ **Zusammenfassend**:
`ManagedScheduledExecutorService` funktioniert wie der Scheduler von Java SE, ist aber Container-aware, sodass Sie sicheres Threading in Java EE-Apps erhalten. Timeout wird normalerweise pro Task angewendet (entweder über die API oder Server-Konfiguration), während die Poolgröße (Core/Max Threads) auf Container-Ebene konfiguriert wird, nicht in Ihrem Anwendungscode.

---

Möchten Sie, dass ich Ihnen ein **Konfigurationsbeispiel für WebSphere Liberty** für die Poolgröße und den Timeout zeige?