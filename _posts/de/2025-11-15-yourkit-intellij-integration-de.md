---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: YourKit Profiler integriert sich nahtlos in IntelliJ
translated: true
type: note
---

Ja, YourKit Java Profiler lässt sich sehr gut in IntelliJ IDEA integrieren (sowohl in der Community- als auch in der Ultimate Edition), und es ist eine der reibungslosesten Profiler-zu-IDE-Erfahrungen, die für Java verfügbar ist.

Hier sind die wichtigsten Integrationsfunktionen, nach denen Sie gefragt haben:

- Direkter Start aus IDEA  
  Sobald Sie das YourKit-Plugin installieren (verfügbar im JetBrains Marketplace oder als eigenes Plugin von YourKit), erhalten Sie neue Run-Konfigurationen wie "YourKit Snapshot", "YourKit Profiling (CPU)", "YourKit Profiling (Memory)" usw. direkt neben Ihren normalen Run/Debug-Schaltflächen.

- Profiling direkt aus der IDE-Symbolleiste starten/stoppen  
  Sie können das Profiling mit einem Klick starten und es stoppen + die aufgenommene Momentaufnahme automatisch öffnen, ohne IDEA verlassen zu müssen.

- Klick in der Profiler-UI → sofortiger Sprung zum Quellcode in IDEA  
  YourKit erkennt, dass IDEA läuft, und richtet automatisch die Dekompilierungs-/Quellcode-Navigation ein. Wenn Sie in der YourKit-UI auf eine Methode, einen Stack-Frame, einen Allocation-Hotspot usw. doppelklicken, wird die exakte Zeile in Ihrem IDEA-Editor geöffnet (funktioniert auch, wenn Sie nur Bytecode haben, dank der integrierten Dekompilierer-Unterstützung).

- Automatische Momentaufnahme beim Beenden der Anwendung  
  Sie können YourKit so konfigurieren, dass beim Beenden Ihrer Anwendung automatisch eine Momentaufnahme erstellt wird, die IDEA sofort öffnet.

Aktueller Status (Stand YourKit 2024.9, das Ende 2025 das neueste stabile Release ist):
- Volle Unterstützung für IntelliJ IDEA 2023.3–2025.2+  
- Funktioniert einwandfrei mit Java 8–24 (einschließlich Profiling von virtuellen Threads ab Java 21+)  
- Unterstützt auch Kotlin, Scala, Groovy usw. und springt zur korrekten Quelle.

Installationsschritte (schnell):
1. In IDEA → Einstellungen → Plugins → Marketplace → nach "YourKit" suchen
2. Installieren/Neustarten
3. Der YourKit-Agent ist im Plugin gebündelt, sodass für die grundlegende Nutzung keine separate YourKit-Installation erforderlich ist (Sie können jedoch die vollständige eigenständige YourKit-App installieren, wenn Sie die umfangreichere UI außerhalb von IDEA wünschen).

Die meisten Java-Entwickler, die YourKit täglich nutzen, verlassen IDEA für das Profiling nicht mehr, sobald dieses Plugin eingerichtet ist.

Also ja – genau der von Ihnen beschriebene Workflow funktioniert sofort und ist sehr ausgereift.