---
audio: false
generated: true
image: false
lang: de
layout: post
title: Schnellübersicht JVM-Optionen nach Kategorien
translated: true
type: note
---

In der JVM-Welt gibt es **viele Optionen**, die Sie konfigurieren können, und der genaue Satz hängt von der JVM-Implementierung (HotSpot, OpenJ9, GraalVM, etc.) und Version ab. Grob lassen sich die JVM-Optionen in diese Kategorien einteilen:

---

## 1. Standard-Optionen

Dies sind stabile, versionsübergreifende Optionen, die offiziell dokumentiert und garantiert funktionsfähig sind. Beispiele:

* `-classpath` / `-cp` → Classpath angeben.
* `-Dproperty=value` → Systemeigenschaften setzen.
* `-version` → JVM-Version ausgeben.
* `-Xms` / `-Xmx` → Anfangs- und maximale Heap-Größe.
* `-ea` → Assertions aktivieren.

---

## 2. Nicht-Standard-Optionen (`-X`)

Diese sind JVM-spezifisch und nicht garantiert stabil. Beispiele (HotSpot):

* `-Xint` → Nur interpretieren (kein JIT).
* `-Xcomp` → Alle Methoden bei der ersten Verwendung kompilieren.
* `-Xbatch` → Hintergrundkompilierung deaktivieren.
* `-Xss512k` → Thread-Stack-Größe setzen.

---

## 3. Erweiterte Optionen (`-XX`)

Diese ermöglichen eine feinabstimmung für GC, JIT und Laufzeitverhalten. Beispiele:

* `-XX:+UseG1GC` → G1 Garbage Collector aktivieren.
* `-XX:+PrintGCDetails` → GC-Aktivität protokollieren.
* `-XX:MaxMetaspaceSize=256m` → Metaspace begrenzen.
* `-XX:+HeapDumpOnOutOfMemoryError` → Heap-Dump bei OOM erstellen.
* `-XX:+UnlockExperimentalVMOptions` → Experimentelle Flags erlauben.
* `-XX:+UseStringDeduplication` → Speichernutzung durch Deduplizierung von Strings reduzieren.

---

## 4. Diagnose & Experimentell

Einige Flags sind versteckt und müssen freigeschaltet werden:

* `-XX:+UnlockDiagnosticVMOptions` → Diagnose-Flags aktivieren.
* `-XX:+UnlockExperimentalVMOptions` → Experimentelle Einstellungen erlauben.

Anschließend können Sie Optionen wie diese verwenden:

* `-XX:+PrintFlagsFinal` → Alle JVM-Optionen und ihre Werte auflisten.
* `-XX:+LogCompilation` → JIT-Compiler-Aktivität protokollieren.

---

## 5. Tools für den Umgang mit JVM-Optionen

* **`java -X`** → Listet die nicht-standard Optionen für Ihren JVM-Build auf.
* **`java -XX:+PrintFlagsFinal`** → Gibt alle erkannten Optionen mit Standardwerten und aktuellen Werten aus.
* **`jcmd <pid> VM.flags`** → Zeigt JVM-Flags für einen laufenden Prozess an.
* **`jcmd <pid> VM.uptime`**, `jcmd <pid> VM.system_properties` → Laufzeit-Inspektion.
* **`jps` + `jinfo`** → Java-Prozesse auflisten und JVM-Optionen ausgeben.
* **VisualVM / JConsole** → Heap, GC und Laufzeitparameter überwachen.

---

👉 Ein praktischer Weg, um Ihre Umgebung zu erkunden, ist der Befehl:

```bash
java -XX:+PrintFlagsFinal | grep GC
```

um alle GC-bezogenen Optionen zu sehen, oder einfach:

```bash
java -X
```

um die verfügbaren nicht-standard Flags zu prüfen.

---

Möchten Sie, dass ich Ihnen eine **kategorierte Spickzettel der nützlichsten JVM-Optionen** (GC, Speicher, Debugging, Performance-Tuning) gebe, damit Sie nicht die riesige `PrintFlagsFinal`-Liste durchforsten müssen?