---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: iPerf3 Netzwerkbandbreiten-Testtool
translated: true
type: note
---

### Was ist iPerf3?

iPerf3 ist ein Open-Source-Kommandozeilen-Tool, das für die Messung von Netzwerkbandbreite und -leistung entwickelt wurde. Es wird häufig verwendet, um den maximal erreichbaren Durchsatz in IP-Netzwerken zu testen, indem Datenverkehr zwischen zwei Endpunkten simuliert wird (einer agiert als Server, der andere als Client). Dies hilft bei der Diagnose von Problemen wie Latenz, Paketverlust und Engpässen in lokalen oder Weitverkehrsnetzen.

#### Wichtige Funktionen:
- **Unterstützte Protokolle**: TCP, UDP und SCTP für flexible Testszenarien.
- **Anpassung**: Ermöglicht das Anpassen von Parametern wie Puffergrößen, Testdauer und bidirektionalem Datenverkehr.
- **Ausgabe**: Liefert detaillierte Statistiken zu Bandbreite, Jitter und Datagrammverlust.

#### Einfaches Anwendungsbeispiel:
Um die Bandbreite zwischen zwei Rechnern zu testen:
1. Auf dem Server: `iperf3 -s` (startet den Server).
2. Auf dem Client: `iperf3 -c <Server-IP>` (verbindet und führt standardmäßig einen 10-Sekunden-Test durch).

Es ist leichtgewichtig, plattformübergreifend (läuft auf Linux, Windows, macOS) und wird häufig von Netzwerkadministratoren, Entwicklern und IT-Profis zur Problembehebung verwendet.

#### Geschichte:
iPerf3 ist eine komplette Neuimplementierung des ursprünglichen iPerf-Tools, die 2009 von ESnet (Energy Sciences Network) begonnen und 2014 erstmals veröffentlicht wurde. Das Redesign zielte auf eine kleinere, besser wartbare Codebasis bei gleichzeitiger Verbesserung der Genauigkeit ab.

Weitere Details finden Sie auf der offiziellen Website oder im GitHub-Repo.

### Referenzen
- [iPerf - The TCP, UDP and SCTP network bandwidth measurement tool](https://iperf.fr/)
- [iperf3: A TCP, UDP, and SCTP network bandwidth measurement tool](https://github.com/esnet/iperf)
- [Iperf - Wikipedia](https://en.wikipedia.org/wiki/Iperf)