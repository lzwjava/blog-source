---
audio: false
generated: true
lang: de
layout: post
title: Warum ist Redis schnell
translated: true
type: note
---

### Wichtige Punkte
- Es scheint wahrscheinlich, dass das YouTube-Video "System Design: Why is single-threaded Redis so fast?" von ByteByteGo die Geschwindigkeit von Redis auf In-Memory-Speicherung, IO-Multiplexing und effiziente Datenstrukturen zurückführt.
- Recherchen deuten darauf hin, dass diese Faktoren es Redis ermöglichen, bis zu 100.000 Abfragen pro Sekunde zu verarbeiten, obwohl es für die Anfrageverarbeitung single-threaded ist.
- Die Beweislage deutet darauf hin, dass neuere Redis-Versionen Multi-Threading für bestimmte Aufgaben hinzugefügt haben, der Kern jedoch single-threaded bleibt.

---

### Einführung
Dieser Blogbeitrag basiert auf dem YouTube-Video "System Design: Why is single-threaded Redis so fast?" von ByteByteGo, das Teil ihrer System-Design-Serie ist. Redis, bekannt für seine hohe Leistung, kann auf einem einzelnen Rechner bis zu 100.000 Abfragen pro Sekunde verarbeiten, was für ein single-threaded System beeindruckend ist. Lassen Sie uns untersuchen, warum dies möglich ist und was Redis so schnell macht.

### Gründe für die Geschwindigkeit von Redis
Die Geschwindigkeit von Redis kann mehreren Schlüsselfaktoren zugeschrieben werden, die wahrscheinlich im Video behandelt werden:

- **In-Memory-Speicherung**: Redis speichert Daten im RAM, der viel schneller als Festplattenspeicher ist. Dies reduziert die Latenz und erhöht den Durchsatz, da Speicherzugriffszeiten im Nanosekundenbereich liegen, verglichen mit Millisekunden für Festplattenzugriffe.

- **IO-Multiplexing und Single-Threaded-Ausführung**: IO-Multiplexing, unter Verwendung von Mechanismen wie epoll unter Linux, ermöglicht es einem einzelnen Thread, mehrere Client-Verbindungen effizient zu handhaben. Dies vermeidet den Overhead von Kontextwechseln, und die single-threaded Schleife vereinfacht Operationen, indem sie Synchronisationsprobleme eliminiert.

- **Effiziente Datenstrukturen**: Redis verwendet optimierte Datenstrukturen wie Hash-Tabellen (O(1)-Lookups), verknüpfte Listen und Skip-Listen, die die Leistung steigern, indem sie den Speicherverbrauch minimieren und Operationen beschleunigen.

### Skalierung und Entwicklung
Für hohe Nebenläufigkeit kann Redis horizontal skaliert werden, indem mehrere Instanzen oder Clustering verwendet werden. Ein unerwartetes Detail ist, dass, während die Kern-Anfrageverarbeitung single-threaded bleibt, neuere Versionen (seit 4.0) Multi-Threading für Aufgaben wie das Löschen von Objekten im Hintergrund eingeführt haben, was die Leistung weiter verbessert, ohne das primäre Modell zu ändern.

---

### Umfragehinweis: Detaillierte Analyse der Single-Threaded-Leistung von Redis

Dieser Abschnitt bietet eine umfassende Analyse, warum single-threaded Redis so schnell ist, basierend auf dem YouTube-Video "System Design: Why is single-threaded Redis so fast?" von ByteByteGo und verwandten Recherchen. Das Video, veröffentlicht am 13. August 2022, ist Teil einer Serie, die sich auf System Design konzentriert und von den Autoren der Bestseller System Design Interview Bücher erstellt wurde. Angesichts des Fokus des Kanals bietet das Video wahrscheinlich detaillierte Einblicke, die für technische Interviews und System-Design-Diskussionen geeignet sind.

#### Hintergrund und Kontext
Redis, ein Open-Source In-Memory Key-Value Store, wird häufig als Cache, Message Broker und Streaming-Engine verwendet. Es unterstützt Datenstrukturen wie Strings, Listen, Sets, Hashes, Sorted Sets und probabilistische Strukturen wie Bloom Filter und HyperLogLog. Der Titel des Videos lässt eine Untersuchung erwarten, warum Redis trotz seiner single-threaded Anfrageverarbeitung eine hohe Leistung beibehält, was zentral für sein Design ist.

Verwandten Artikeln zufolge kann Redis auf einem einzelnen Rechner bis zu 100.000 Queries Per Second (QPS) verarbeiten, eine Zahl, die oft in Performance-Benchmarks zitiert wird. Diese Geschwindigkeit ist angesichts des single-threaded Modells überraschend, aber Recherchen deuten darauf hin, dass sie auf mehrere architektonische Entscheidungen zurückzuführen ist.

#### Wichtige Faktoren, die zur Geschwindigkeit von Redis beitragen

1. **In-Memory-Speicherung**  
   Redis speichert Daten im RAM, der mindestens 1000-mal schneller als wahlfreier Festplattenzugriff ist. Dies beseitigt die Latenz von Disk-I/O, mit RAM-Zugriffszeiten von etwa 100-120 Nanosekunden im Vergleich zu 50-150 Mikrosekunden für SSDs und 1-10 Millisekunden für HDDs. Das Video betont dies wahrscheinlich als Hauptgrund, da es mit dem Fokus des Kanals auf System-Design-Grundlagen übereinstimmt.

   | Aspekt                | Details                                      |
   |-----------------------|----------------------------------------------|
   | Speichermedium        | RAM (In-Memory)                              |
   | Zugriffszeit          | ~100-120 Nanosekunden                       |
   | Vergleich zu Festplatte| 1000x schneller als wahlfreier Festplattenzugriff |
   | Auswirkung auf Leistung| Reduziert Latenz, erhöht Durchsatz          |

2. **IO-Multiplexing und Single-Threaded-Ausführungsschleife**  
   IO-Multiplexing ermöglicht es einem einzelnen Thread, mehrere I/O-Ströme gleichzeitig mit Systemaufrufen wie `select`, `poll`, `epoll` (Linux), `kqueue` (Mac OS) oder `evport` (Solaris) zu überwachen. Dies ist entscheidend für die Handhabung mehrerer Client-Verbindungen ohne Blockierung, ein Punkt, der wahrscheinlich im Video detailliert behandelt wird. Die single-threaded Ausführungsschleife vermeidet Kontextwechsel- und Synchronisations-Overhead und vereinfacht Entwicklung und Debugging.

   | Mechanismus           | Beschreibung                                  |
   |-----------------------|----------------------------------------------|
   | epoll/kqueue          | Effizient für hohe Nebenläufigkeit, nicht-blockierend |
   | select/poll           | Älter, weniger skalierbar, O(n)-Komplexität  |
   | Auswirkung            | Reduziert Verbindungs-Overhead, ermöglicht Pipelining |

   Jedoch können client-blockierende Befehle wie `BLPOP` oder `BRPOP` den Verkehr verzögern, ein potenzieller Nachteil, der in verwandten Artikeln erwähnt wird. Das Video könnte diskutieren, wie diese Designentscheidung Einfachheit mit Leistung in Einklang bringt.

3. **Effiziente low-level Datenstrukturen**  
   Redis nutzt Datenstrukturen wie Hash-Tabellen für O(1)-Schlüssel-Lookups, verknüpfte Listen für Listen und Skip-Listen für Sorted Sets. Diese sind für In-Memory-Operationen optimiert, minimieren den Speicherverbrauch und maximieren die Geschwindigkeit. Das Video enthält wahrscheinlich Diagramme oder Beispiele, wie etwa, wie Hash-Tabellen schnelle Key-Value-Operationen ermöglichen, ein häufiges Thema in System-Design-Interviews.

   | Datenstruktur         | Anwendungsfall                               | Zeitkomplexität |
   |-----------------------|----------------------------------------------|-----------------|
   | Hash-Tabelle          | Key-Value-Speicher                          | O(1) im Durchschnitt |
   | Verknüpfte Liste      | Listen, effizient an den Enden              | O(1) für Enden  |
   | Skip-Liste            | Sorted Sets, geordnete Speicherung          | O(log n)        |

   Diese Optimierung ist kritisch, da die meisten Redis-Operationen speicherbasiert sind, wobei Engpässe typischerweise im Speicher oder Netzwerk liegen, nicht in der CPU.

#### Zusätzliche Überlegungen und Entwicklung
Während die Kern-Anfrageverarbeitung single-threaded ist, haben neuere Versionen von Redis Multi-Threading für bestimmte Aufgaben eingeführt. Seit Redis 4.0 wurde asynchrone Speicherfreigabe (lazy-free) implementiert, und seit 6.0 wurde Multi-Threading für Protokollparsing unter hoher Nebenläufigkeit hinzugefügt. Diese Änderungen, die wahrscheinlich im Video erwähnt werden, verbessern die Leistung, ohne das single-threaded Modell für Hauptoperationen zu verändern.

Für die Skalierung über eine einzelne Instanz hinaus unterstützt Redis Clustering und das Ausführen mehrerer Instanzen, eine Strategie, die diskutiert werden könnte, um hohe Nebenläufigkeitsanforderungen zu adressieren. Dies ist ein wichtiger Aspekt für das System Design, der sich mit dem Fokus des Kanals auf großangelegte Systeme deckt.

#### Potenzielle Nachteile und Vergleiche
Das single-threaded Modell hat Vorteile wie keine Lock-Konflikte und einfacheres Debugging, kann aber Herausforderungen mit blockierenden Operationen und Speicher-/Netzwerk-Engpässen unter hoher Last haben. Verwandte Artikel legen nahe, dass für CPU-intensive Aufgaben mehrfädige Datenbanken besser abschneiden könnten, aber für die typischen Anwendungsfälle von Redis ist das single-threaded Design optimal.

#### Fazit
Das Video "System Design: Why is single-threaded Redis so fast?" von ByteByteGo behandelt wahrscheinlich In-Memory-Speicherung, IO-Multiplexing und effiziente Datenstrukturen als Hauptgründe für die Geschwindigkeit von Redis. Diese Faktoren ermöglichen es, hohe QPS zu handhaben, wobei neuere Versionen Multi-Threading für spezifische Optimierungen hinzugefügt haben. Diese Analyse bietet ein umfassendes Verständnis, das sowohl für technische Lernende als auch für System-Design-Profis geeignet ist.

---

### Wichtige Zitate
- [Why is redis so fast blog post](https://blog.bytebytego.com/p/why-is-redis-so-fast)
- [Why is Redis So Fast Despite Being Single-Threaded article](https://medium.com/@aditimishra_541/why-is-redis-so-fast-despite-being-single-threaded-dc06ba33fc75)
- [Interview on Redis thread model article](https://medium.com/javarevisited/interview-why-is-redis-so-fast-even-though-it-is-single-threaded-bfe663dabe08)
- [Why is single threaded Redis so fast article](https://www.pixelstech.net/article/1677580861-Why-is-single-threaded-Redis-so-fast)