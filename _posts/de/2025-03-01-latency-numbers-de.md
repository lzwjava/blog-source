---
audio: false
generated: true
lang: de
layout: post
title: Latenzzahlen
translated: true
type: note
---

### Wichtige Punkte
- Es scheint wahrscheinlich, dass das Video die standardmäßigen Latenzzeiten behandelt, die Programmierer kennen sollten, basierend auf seinem Titel und verwandten Online-Inhalten.
- Recherchen deuten darauf hin, dass diese Zahlen Zeiten für Operationen wie L1-Cache-Zugriff (0,5 ns) und Netzwerk-Round-Trips (bis zu 150 ms) beinhalten, die je nach Hardware variieren.
- Die Beweislage deutet darauf hin, dass es sich bei diesen Zahlen um ungefähre Werte handelt, mit Aktualisierungen, die technologische Fortschritte widerspiegeln, insbesondere bei SSDs und Netzwerken.

### Einführung
Das Video "Latency Numbers Programmer Should Know: Crash Course System Design #1" behandelt wahrscheinlich essentielle Latenzwerte für Computeroperationen, die für das Systemdesign entscheidend sind. Diese Zahlen helfen Programmierern, Performance-Auswirkungen zu verstehen und Systeme zu optimieren.

### Latenzzeiten und ihre Bedeutung
Latenz ist die Verzögerung zwischen dem Starten und dem Abschließen einer Operation, wie dem Zugriff auf den Speicher oder dem Senden von Daten über ein Netzwerk. Das Video listet wahrscheinlich typische Latenzzeiten auf, wie zum Beispiel:
- L1-Cache-Referenz bei 0,5 Nanosekunden (ns), dem schnellsten Speicherzugriff.
- Ein Round-Trip innerhalb desselben Rechenzentrums bei 500 Mikrosekunden (us) oder 0,5 Millisekunden (ms), was verteilte Systeme beeinflusst.

Diese Zahlen, obwohl ungefähr, leiten Entscheidungen im Systemdesign, wie die Wahl zwischen Speicher- und Festplattenspeicher.

### Kontext im Systemdesign
Das Verständnis dieser Latenzzeiten hilft bei der Optimierung von Code, bei Abwägungen und bei der Verbesserung der Benutzererfahrung. Wenn man beispielsweise weiß, dass eine Plattenpositionierung (Disk Seek) 10 ms dauert, kann dies das Datenbankdesign beeinflussen, um solche Operationen zu minimieren.

### Unerwartetes Detail
Ein interessanter Aspekt ist, wie sich diese Zahlen, wie z.B. SSD-Lesezeiten, mit der Technologie verbessert haben, während Kern-CPU-Latenzen wie der L1-Cache-Zugriff stabil geblieben sind. Dies zeigt die ungleichmäßige Auswirkung der Hardware-Evolution.

---

### Umfragenotiz: Detaillierte Analyse der Latenzzeiten aus dem Video

Diese Notiz bietet eine umfassende Untersuchung der Latenzzeiten, die wahrscheinlich im Video "Latency Numbers Programmer Should Know: Crash Course System Design #1" diskutiert werden, basierend auf verfügbaren Online-Inhalten und verwandten Ressourcen. Die Analyse zielt darauf ab, Informationen für Programmierer und Systemdesigner zu synthetisieren und bietet sowohl eine Zusammenfassung als auch detaillierte Einblicke in die Bedeutung dieser Zahlen.

#### Hintergrund und Kontext
Das Video, abrufbar auf [YouTube](https://www.youtube.com/watch?v=FqR5vESuKe0), ist Teil einer Serie über Systemdesign und konzentriert sich auf Latenzzeiten, die für Programmierer kritisch sind. Latenz, definiert als die Zeitverzögerung zwischen dem Starten und dem Abschließen einer Operation, ist entscheidend für das Verständnis der Systemleistung. Angesichts des Titels des Videos und verwandter Suchen scheint es Standard-Latenzwerte zu behandeln, die von Persönlichkeiten wie Jeff Dean von Google popularisiert wurden und oft in Programmier-Communities referenziert werden.

Online-Recherchen haben mehrere Ressourcen zu diesen Zahlen aufgedeckt, darunter einen GitHub Gist mit dem Titel "Latency Numbers Every Programmer Should Know" ([GitHub Gist](https://gist.github.com/jboner/2841832)) und einen Medium-Artikel aus dem Jahr 2023 ([Medium Article](https://medium.com/@bojanskr/latency-numbers-every-programmer-should-know-d85f8d3f8e6a)). Diese Quellen, zusammen mit einem High Scalability-Post aus dem Jahr 2013 ([High Scalability](https://highscalability.com/more-numbers-every-awesome-programmer-must-know/)), bildeten eine Grundlage für die Zusammenstellung des wahrscheinlichen Inhalts des Videos.

#### Zusammenstellung der Latenzzeiten
Basierend auf den gesammelten Informationen fasst die folgende Tabelle die standardmäßigen Latenzzeiten zusammen, die wahrscheinlich im Video diskutiert werden, mit Erklärungen für jede Operation:

| Operation                                      | Latenz (ns) | Latenz (us) | Latenz (ms) | Erklärung                                                          |
|------------------------------------------------|--------------|--------------|--------------|----------------------------------------------------------------------|
| L1 cache reference                            | 0.5          | -            | -            | Zugriff auf Daten im Level-1-Cache, dem schnellsten Speicher in der Nähe der CPU. |
| Branch mispredict                              | 5            | -            | -            | Strafe, wenn die CPU einen bedingten Sprung falsch vorhersagt.       |
| L2 cache reference                            | 7            | -            | -            | Zugriff auf Daten im Level-2-Cache, größer als L1 aber langsamer.           |
| Mutex lock/unlock                              | 25           | -            | -            | Zeit zum Erlangen und Freigeben eines Mutex in multithreaded Programmen.        |
| Main memory reference                          | 100          | -            | -            | Zugriff auf Daten aus dem Hauptarbeitsspeicher (RAM).                  |
| Compress 1K bytes with Zippy                   | 10,000       | 10           | -            | Zeit zum Komprimieren von 1 Kilobyte mit dem Zippy-Algorithmus.                |
| Send 1 KB bytes over 1 Gbps network            | 10,000       | 10           | -            | Zeit zum Übertragen von 1 Kilobyte über ein 1 Gigabit pro Sekunde Netzwerk.      |
| Read 4 KB randomly from SSD                    | 150,000      | 150          | -            | Zufälliges Lesen von 4 Kilobyte von einer Solid-State-Drive.                  |
| Read 1 MB sequentially from memory             | 250,000      | 250          | -            | Sequentielles Lesen von 1 Megabyte aus dem Hauptspeicher.                       |
| Round trip within same datacenter              | 500,000      | 500          | 0.5          | Netzwerk-Round-Trip-Zeit innerhalb desselben Rechenzentrums.                   |
| Read 1 MB sequentially from SSD                | 1,000,000    | 1,000        | 1            | Sequentielles Lesen von 1 Megabyte von einer SSD.                            |
| HDD seek                                      | 10,000,000   | 10,000       | 10           | Zeit für eine Hard Disk Drive, um eine neue Position anzusteuern.                 |
| Read 1 MB sequentially from disk              | 20,000,000   | 20,000       | 20           | Sequentielles Lesen von 1 Megabyte von einer HDD.                            |
| Send packet CA->Netherlands->CA                | 150,000,000  | 150,000      | 150          | Round-Trip-Zeit für ein Netzwerkpaket von Kalifornien in die Niederlande.  |

Diese Zahlen, hauptsächlich aus dem Jahr 2012 mit einigen Aktualisierungen, spiegeln die typische Hardwareleistung wider, wobei in aktuellen Diskussionen Variationen festgestellt werden, insbesondere für SSDs und Netzwerke aufgrund technologischer Fortschritte.

#### Analyse und Implikationen
Die Latenzzeiten sind nicht fest und können je nach spezifischer Hardware und Konfiguration variieren. Beispielsweise stellte ein Blogpost von Ivan Pesin aus dem Jahr 2020 ([Pesin Space](http://pesin.space/posts/2020-09-22-latencies/)) fest, dass sich die Latenzzeiten von Festplatten und Netzwerken dank besserer SSDs (NVMe) und schnellerer Netzwerke (10/100Gb) verbessert haben, aber Kern-CPU-Latenzen wie der L1-Cache-Zugriff stabil geblieben sind. Diese ungleichmäßige Entwicklung unterstreicht die Bedeutung des Kontexts im Systemdesign.

In der Praxis leiten diese Zahlen mehrere Aspekte:
- **Performance-Optimierung**: Das Minimieren von Operationen mit hoher Latenz, wie Plattenpositionierungen (10 ms), kann die Anwendungsgeschwindigkeit erheblich verbessern. Das Zwischenspeichern häufig abgerufener Daten im Speicher (250 us für 1 MB Lesen) anstatt auf der Festplatte kann beispielsweise Wartezeiten reduzieren.
- **Abwägungsentscheidungen**: Systemdesigner stehen oft vor Entscheidungen, wie der Verwendung von In-Memory-Caches gegenüber Datenbanken. Die Kenntnis, dass ein Hauptspeicherzugriff (100 ns) 200-mal schneller ist als eine L1-Cache-Referenz (0,5 ns), kann solche Entscheidungen beeinflussen.
- **Benutzererfahrung**: In Webanwendungen können Netzwerklatenzen, wie ein Round-Trip innerhalb eines Rechenzentrums (500 us), die Seitenladezeiten beeinflussen und sich auf die Benutzerzufriedenheit auswirken. Ein Vercel-Blogpost aus dem Jahr 2024 ([Vercel Blog](https://vercel.com/blog/latency-numbers-every-web-developer-should-know)) betonte dies für die Frontend-Entwicklung und wies darauf hin, wie Netzwerk-Waterfalls Latenzzeiten verstärken können.

#### Historischer Kontext und Aktualisierungen
Die ursprünglichen Zahlen, die Jeff Dean zugeschrieben und von Peter Norvig popularisiert wurden, stammen aus etwa 2010, mit Aktualisierungen von Forschern wie Colin Scott ([Interactive Latencies](https://colin-scott.github.io/personal_website/research/interactive_latency.html)). Ein Medium-Post von Dan Hon aus dem Jahr 2019 ([Dan Hon Medium](https://medium.com/@hondanhon/more-latency-numbers-every-programmer-should-know-3142f0cf614d)) fügte humorvolle aber relevante Latenzzeiten hinzu, wie das Neustarten eines MacBook Pro (90 Sekunden), um breitere technikbezogene Verzögerungen zu veranschaulichen. Die Kern-Latenzzeiten haben jedoch nur minimale Änderungen erfahren, wobei der GitHub Gist nahelegt, dass sie Stand 2023 "ziemlich ähnlich" geblieben sind, basierend auf physikalischen Limitierungen.

#### Fazit und Empfehlungen
Für Programmierer und Systemdesigner bietet das Auswendiglernen dieser Latenzzeiten ein mentales Modell für die Performance-Optimierung. Sie sollten als Richtlinien behandelt werden, wobei für spezifische Hardware tatsächliche Benchmarks durchgeführt werden sollten. Auf dem Laufenden zu bleiben, insbesondere bei aufstrebenden Technologien wie Quantencomputing oder 5G-Netzwerken, wird entscheidend sein. Ressourcen wie der GitHub Gist und der Medium-Artikel bieten Ausgangspunkte für weitere Erkundungen.

Diese Analyse, die auf dem wahrscheinlichen Inhalt des Videos basiert und durch umfangreiche Online-Recherchen ergänzt wurde, unterstreicht die anhaltende Relevanz von Latenzzeiten in der Informatik, mit einem Aufruf zur Anpassung an technologische Verschiebungen für optimales Systemdesign.

#### Wichtige Zitate
- [Latency Numbers Every Programmer Should Know GitHub Gist](https://gist.github.com/jboner/2841832)
- [Latency Numbers Programmer Should Know YouTube Video](https://www.youtube.com/watch?v=FqR5vESuKe0)
- [Updated Latency Numbers Medium Article](https://medium.com/@bojanskr/latency-numbers-every-programmer-should-know-d85f8d3f8e6a)
- [More Numbers Every Awesome Programmer Must Know High Scalability](https://highscalability.com/more-numbers-every-awesome-programmer-must-know/)
- [Latency Numbers Every Web Developer Should Know Vercel Blog](https://vercel.com/blog/latency-numbers-every-web-developer-should-know)
- [Latency Numbers Every Engineer Should Know Pesin Space Blog](http://pesin.space/posts/2020-09-22-latencies/)
- [More Latency Numbers Every Programmer Should Know Dan Hon Medium](https://medium.com/@hondanhon/more-latency-numbers-every-programmer-should-know-3142f0cf614d)
- [Numbers Every Programmer Should Know By Year Interactive Latencies](https://colin-scott.github.io/personal_website/research/interactive_latency.html)