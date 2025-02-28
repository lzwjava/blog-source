---
audio: false
lang: de
layout: post
title: Warum ist Redis schnell?
translated: true
---

### Wichtige Punkte
- Es scheint wahrscheinlich, dass das YouTube-Video "System Design: Warum ist single-threaded Redis so schnell?" von ByteByteGo die Geschwindigkeit von Redis aufgrund von In-Memory-Speicherung, IO-Multiplexing und effizienten Datenstrukturen erklärt.
- Forschung deutet darauf hin, dass diese Faktoren es Redis ermöglichen, bis zu 100.000 Abfragen pro Sekunde zu verarbeiten, obwohl es für die Anforderungsverarbeitung single-threaded ist.
- Die Beweise deuten darauf hin, dass neuere Redis-Versionen Multi-Threading für spezifische Aufgaben hinzugefügt haben, aber der Kern bleibt single-threaded.

---

### Einführung
Dieser Blogbeitrag basiert auf dem YouTube-Video "System Design: Warum ist single-threaded Redis so schnell?" von ByteByteGo, Teil ihrer Systemdesign-Serie. Redis, bekannt für seine hohe Leistung, kann bis zu 100.000 Abfragen pro Sekunde auf einer einzigen Maschine verarbeiten, was für ein single-threaded System beeindruckend ist. Lassen Sie uns untersuchen, warum dies möglich ist und was Redis so schnell macht.

### Gründe für die Geschwindigkeit von Redis
Die Geschwindigkeit von Redis lässt sich auf mehrere Schlüsselfaktoren zurückführen, die wahrscheinlich im Video behandelt werden:

- **In-Memory-Speicherung**: Redis speichert Daten im RAM, was viel schneller ist als Festplattenspeicherung. Dies reduziert die Latenz und erhöht den Durchsatz, da die Zugriffszeiten auf den Speicher im Nanosekundenbereich liegen, verglichen mit Millisekunden für den Zugriff auf die Festplatte.

- **IO-Multiplexing und Single-Threaded-Ausführung**: IO-Multiplexing, unter Verwendung von Mechanismen wie epoll auf Linux, ermöglicht es einem einzigen Thread, mehrere Clientverbindungen effizient zu verwalten. Dies vermeidet den Overhead des Kontextwechsels, und die single-threaded-Schleife vereinfacht die Operationen, indem Synchronisationsprobleme eliminiert werden.

- **Effiziente Datenstrukturen**: Redis verwendet optimierte Datenstrukturen wie Hash-Tabellen (O(1)-Lookups), verknüpfte Listen und Skip-Listen, die die Leistung durch Minimierung des Speicherverbrauchs und Beschleunigung der Operationen verbessern.

### Skalierung und Entwicklung
Für hohe Konkurrenz kann Redis horizontal skaliert werden, indem mehrere Instanzen oder Clustering verwendet werden. Eine unerwartete Einzelheit ist, dass, während die Kernanforderungsverarbeitung single-threaded bleibt, neuere Versionen (seit 4.0) Multi-Threading für Aufgaben wie Hintergrundobjektlöschung eingeführt haben, was die Leistung weiter verbessert, ohne das primäre Modell zu ändern.

---

### Umfragehinweis: Detaillierte Analyse der Single-Threaded-Leistung von Redis

Dieser Abschnitt bietet eine umfassende Analyse, warum single-threaded Redis so schnell ist, basierend auf dem YouTube-Video "System Design: Warum ist single-threaded Redis so schnell?" von ByteByteGo und verwandter Forschung. Das Video, veröffentlicht am 13. August 2022, ist Teil einer Serie, die sich auf Systemdesign konzentriert, verfasst von den Autoren der Bestseller-Systemdesign-Interview-Bücher. Aufgrund des Fokus des Kanals bietet das Video wahrscheinlich detaillierte Einblicke, die für technische Interviews und Systemdesign-Diskussionen geeignet sind.

#### Hintergrund und Kontext
Redis, ein Open-Source-In-Memory-Key-Value-Speicher, wird weit verbreitet als Cache, Message-Broker und Streaming-Engine verwendet. Es unterstützt Datenstrukturen wie Strings, Listen, Sets, Hashes, sortierte Sets und probabilistische Strukturen wie Bloom-Filter und HyperLogLog. Der Titel des Videos deutet auf eine Untersuchung hin, warum Redis trotz seiner single-threaded-Anforderungsverarbeitung eine hohe Leistung beibehält, was zentral für sein Design ist.

Aus verwandten Artikeln kann Redis bis zu 100.000 Queries Per Second (QPS) auf einer einzigen Maschine verarbeiten, eine Zahl, die oft in Leistungsbenchmarks zitiert wird. Diese Geschwindigkeit ist überraschend, wenn man das single-threaded-Modell betrachtet, aber Forschung zeigt, dass dies auf mehrere architektonische Entscheidungen zurückzuführen ist.

#### Schlüsselfaktoren, die zur Geschwindigkeit von Redis beitragen

1. **In-Memory-Speicherung**
   Redis speichert Daten im RAM, der mindestens 1000 Mal schneller ist als der zufällige Zugriff auf die Festplatte. Dies eliminiert die Latenz der Festplatten-E/A, mit RAM-Zugriffszeiten von etwa 100-120 Nanosekunden im Vergleich zu 50-150 Mikrosekunden für SSDs und 1-10 Millisekunden für HDDs. Das Video betont dies wahrscheinlich als einen primären Grund, da es sich auf die Grundlagen des Systemdesigns konzentriert.

   | Aspekt               | Details                                      |
   |----------------------|----------------------------------------------|
   | Speichermedium       | RAM (In-Memory)                              |
   | Zugriffszeit          | ~100-120 Nanosekunden                        |
   | Vergleich zur Festplatte | 1000x schneller als zufälliger Festplattenzugriff |
   | Einfluss auf die Leistung | Reduziert die Latenz, erhöht den Durchsatz        |

2. **IO-Multiplexing und Single-Threaded-Ausführungsschleife**
   IO-Multiplexing ermöglicht es einem einzigen Thread, mehrere E/A-Streams gleichzeitig zu überwachen, indem Systemaufrufe wie `select`, `poll`, `epoll` (Linux), `kqueue` (Mac OS) oder `evport` (Solaris) verwendet werden. Dies ist entscheidend für die Verwaltung mehrerer Clientverbindungen ohne Blockierung, ein Punkt, der wahrscheinlich im Video detailliert beschrieben wird. Die single-threaded-Ausführungsschleife vermeidet den Overhead des Kontextwechsels und der Synchronisation, was die Entwicklung und das Debugging vereinfacht.

   | Mechanismus            | Beschreibung                                  |
   |----------------------|----------------------------------------------|
   | epoll/kqueue         | Effizient für hohe Konkurrenz, nicht blockierend |
   | select/poll          | Älter, weniger skalierbar, O(n)-Komplexität        |
   | Einfluss               | Reduziert den Verbindungs-Overhead, ermöglicht Pipelining |

   Allerdings können client-blockierende Befehle wie `BLPOP` oder `BRPOP` den Verkehr verzögern, ein potenzieller Nachteil, der in verwandten Artikeln erwähnt wird. Das Video könnte diskutieren, wie diese Designentscheidung Einfachheit und Leistung ausbalanciert.

3. **Effiziente Datenstrukturen auf niedriger Ebene**
   Redis nutzt Datenstrukturen wie Hash-Tabellen für O(1)-Schlüssel-Lookups, verknüpfte Listen für Listen und Skip-Listen für sortierte Sets. Diese sind für In-Memory-Operationen optimiert, minimieren den Speicherverbrauch und maximieren die Geschwindigkeit. Das Video enthält wahrscheinlich Diagramme oder Beispiele, wie Hash-Tabellen schnelle Schlüssel-Wert-Operationen ermöglichen, ein häufiges Thema in Systemdesign-Interviews.

   | Datenstruktur       | Anwendungsfall                                     | Zeitkomplexität |
   |----------------------|----------------------------------------------|-----------------|
   | Hash-Tabelle           | Schlüssel-Wert-Speicherung                           | O(1) durchschnittlich    |
   | Verknüpfte Liste          | Listen, effizient an den Enden                    | O(1) für Enden   |
   | Skip-List            | Sortierte Sets, geordnete Speicherung                | O(log n)        |

   Diese Optimierung ist entscheidend, da die meisten Redis-Operationen speicherbasiert sind, mit Engpässen, die typischerweise im Speicher oder Netzwerk, nicht in der CPU liegen.

#### Zusätzliche Überlegungen und Entwicklung
Während die Kernanforderungsverarbeitung single-threaded bleibt, haben neuere Versionen von Redis Multi-Threading für spezifische Aufgaben eingeführt. Seit Redis 4.0 wurde die asynchrone Speicherfreigabe (lazy-free) implementiert, und seit 6.0 wurde Multi-Threading für das Protokollparsing unter hoher Konkurrenz hinzugefügt. Diese Änderungen, die wahrscheinlich im Video erwähnt werden, verbessern die Leistung, ohne das single-threaded-Modell für Hauptoperationen zu ändern.

Für die Skalierung über eine einzelne Instanz hinaus unterstützt Redis Clustering und das Ausführen mehrerer Instanzen, eine Strategie, die möglicherweise diskutiert wird, um hohe Konkurrenzbedürfnisse zu adressieren. Dies ist ein wichtiger Aspekt für das Systemdesign, der sich auf große Skalensysteme konzentriert.

#### Potenzielle Nachteile und Vergleiche
Das single-threaded-Modell hat Vorteile wie keine Sperrkonkurrenz und einfacheres Debugging, kann aber Herausforderungen mit blockierenden Operationen und Speicher-/Netzwerk-Engpässen unter hoher Last haben. Verwandte Artikel deuten darauf hin, dass für CPU-intensive Aufgaben möglicherweise multi-threaded-Datenbanken besser abschneiden, aber für die typischen Anwendungsfälle von Redis ist das single-threaded-Design optimal.

#### Schlussfolgerung
Das Video "System Design: Warum ist single-threaded Redis so schnell?" von ByteByteGo behandelt wahrscheinlich In-Memory-Speicherung, IO-Multiplexing und effiziente Datenstrukturen als Hauptgründe für die Geschwindigkeit von Redis. Diese Faktoren ermöglichen es ihm, eine hohe QPS zu verarbeiten, wobei neuere Versionen Multi-Threading für spezifische Optimierungen hinzugefügt haben. Diese Analyse bietet ein umfassendes Verständnis, das sowohl für technische Lernende als auch für Systemdesign-Profis geeignet ist.

---

### Wichtige Zitate
- [Why is redis so fast blog post](https://blog.bytebytego.com/p/why-is-redis-so-fast)
- [Why is Redis So Fast Despite Being Single-Threaded article](https://medium.com/@aditimishra_541/why-is-redis-so-fast-despite-being-single-threaded-dc06ba33fc75)
- [Interview on Redis thread model article](https://medium.com/javarevisited/interview-why-is-redis-so-fast-even-though-it-is-single-threaded-bfe663dabe08)
- [Why is single threaded Redis so fast article](https://www.pixelstech.net/article/1677580861-Why-is-single-threaded-Redis-so-fast)