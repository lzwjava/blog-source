---
audio: false
generated: true
image: false
lang: en
layout: post
title: JVM Options Categorized Quick Guide
translated: false
---

In the JVM world, there are **many options** you can configure, and the exact set depends on the JVM implementation (HotSpot, OpenJ9, GraalVM, etc.) and version. Broadly, JVM options fall into these categories:

---

## 1. Standard Options

These are stable, cross-version options officially documented and guaranteed to work. Examples:

* `-classpath` / `-cp` → specify classpath.
* `-Dproperty=value` → set system properties.
* `-version` → print JVM version.
* `-Xms` / `-Xmx` → initial and maximum heap size.
* `-ea` → enable assertions.

---

## 2. Non-Standard Options (`-X`)

These are JVM-specific, not guaranteed to remain stable. Examples (HotSpot):

* `-Xint` → interpret only (no JIT).
* `-Xcomp` → compile all methods at first use.
* `-Xbatch` → disable background compilation.
* `-Xss512k` → set thread stack size.

---

## 3. Advanced Options (`-XX`)

These provide fine-grained tuning for GC, JIT, and runtime behavior. Examples:

* `-XX:+UseG1GC` → enable G1 garbage collector.
* `-XX:+PrintGCDetails` → log GC activity.
* `-XX:MaxMetaspaceSize=256m` → cap metaspace.
* `-XX:+HeapDumpOnOutOfMemoryError` → dump heap when OOM occurs.
* `-XX:+UnlockExperimentalVMOptions` → allow experimental flags.
* `-XX:+UseStringDeduplication` → reduce memory usage by deduplicating strings.

---

## 4. Diagnostic & Experimental

Some flags are hidden and require unlocking:

* `-XX:+UnlockDiagnosticVMOptions` → enable diagnostic flags.
* `-XX:+UnlockExperimentalVMOptions` → allow experimental tuning.

You can then use options like:

* `-XX:+PrintFlagsFinal` → list all JVM options and their values.
* `-XX:+LogCompilation` → log JIT compiler activity.

---

## 5. Tools to Work With JVM Options

* **`java -X`** → lists non-standard options for your JVM build.
* **`java -XX:+PrintFlagsFinal`** → prints all recognized options with defaults and current values.
* **`jcmd <pid> VM.flags`** → show JVM flags for a running process.
* **`jcmd <pid> VM.uptime`**, `jcmd <pid> VM.system_properties` → runtime inspection.
* **`jps` + `jinfo`** → list Java processes and print JVM options.
* **VisualVM / JConsole** → monitor heap, GC, and runtime parameters.

---

👉 A practical way to explore your environment is to run:

```bash
java -XX:+PrintFlagsFinal | grep GC
```

to see all GC-related options, or just:

```bash
java -X
```

to check available non-standard flags.

---

Would you like me to give you a **categorized cheat-sheet of the most useful JVM options** (GC, memory, debugging, performance tuning) so you don’t have to parse the huge `PrintFlagsFinal` list?