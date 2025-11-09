---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: B-Bäume für effiziente Datenbankindizierung
translated: true
type: note
---

### Was ist ein B-Baum?

Ein B-Baum (kurz für „Balanced Tree“) ist eine selbstbalancierende Baum-Datenstruktur, die für die effiziente Speicherung, Einfügung, Löschung und Abfrage großer Datenmengen entwickelt wurde. Sie ist besonders für Systeme optimiert, in denen Daten auf der Festplatte gespeichert werden (wie z.B. in Datenbanken), da sie die Anzahl der teuren Festplatten-E/A-Operationen minimiert, indem der Baum so flach wie möglich gehalten wird.

#### Wichtige Eigenschaften eines B-Baums
- **Ordnung (oder Grad)**: Definiert durch einen Parameter *t* (Mindestgrad), wobei jeder Knoten zwischen *t-1* und *2t-1* Schlüssel (und bis zu *2t* Kinder) haben kann. Dies ermöglicht es den Knoten, mehrere Schlüssel zu halten, was den Baum breiter und flacher macht.
- **Balancierte Struktur**: Alle Blattknoten befinden sich auf derselben Ebene, was eine logarithmische Zeitkomplexität für Operationen (O(log n), wobei n die Anzahl der Schlüssel ist) gewährleistet.
- **Sortierte Schlüssel**: Die Schlüssel in jedem Knoten sind in sortierter Reihenfolge gespeichert, und der Baum hält diese Invariante aufrecht. Teilbäume links von einem Schlüssel enthalten kleinere Werte und rechts davon größere.
- **Knotenstruktur**: Interne Knoten haben Schlüssel, die die Suche zu den Kindknoten lenken. Blattknoten speichern die eigentlichen Daten (oder Zeiger darauf).

Im Gegensatz zu binären Suchbäumen (BSTs), die auf zwei Kinder pro Knoten beschränkt sind und unbalanciert werden können (was zu O(n) im schlimmsten Fall führt), sind B-Bäume Mehrweg-Bäume, die durch Aufteilen und Zusammenführen von Knoten während des Einfügens/Löschens balanciert bleiben.

#### Einfaches Beispiel
Stellen Sie sich einen B-Baum der Ordnung 3 vor (*t=3*, also 2-5 Schlüssel pro Knoten). Ein kleiner Baum könnte in Textform so aussehen:

```
       [10, 20, 30]
      /    |    |    \
 [5,7]  [15] [22,25] [35,40]
```

- Suche nach 25: Beginne an der Wurzel, vergleiche mit 10/20/30 → gehe rechts zu [22,25] → gefunden.

Diese Struktur ermöglicht effiziente Bereichsabfragen (z.B. alle Schlüssel zwischen 15 und 25), indem nur wenige Knoten durchlaufen werden.

### Wie Datenbanken B-Bäume verwenden

Datenbanken (wie relationale Datenbanken: MySQL, PostgreSQL, SQL Server) verlassen sich stark auf B-Bäume (oder Varianten wie B+-Bäume) für die **Indizierung**, um Abfragen auf großen, auf der Festplatte gespeicherten Tabellen zu beschleunigen. Ohne Indizes würden Abfragen vollständige Tabellenscans erfordern (O(n) Zeit, langsam für Millionen von Zeilen).

#### Hauptanwendungen in Datenbanken
1. **Primäre und sekundäre Indizes**:
   - Ein **primärer Index** wird auf dem Primärschlüssel (eindeutiger Identifikator) aufgebaut. Er organisiert die Zeilen der Tabelle in B-Baum-Reihenfolge für schnelle Lookups.
   - **Sekundäre Indizes** werden auf anderen Spalten (z.B. Name, Datum) erstellt. Die Blattknoten zeigen auf die tatsächlichen Zeilenpositionen (über Zeilen-IDs).

2. **Effizienter Festplattenzugriff**:
   - Festplatten lesen Daten in Blöcken (z.B. 4KB Seiten). B-Baum-Knoten sind so groß, dass sie in einen Festplattenblock passen, sodass eine Suche typischerweise nur das Lesen von 3-4 Blöcken (Baumhöhe) erfordert, im Gegensatz zu potenziell Tausenden in einer verknüpften Liste.
   - Die Höhe ist logarithmisch: Für 1 Milliarde Schlüssel könnte die Höhe nur 4-5 Ebenen betragen.

3. **B+-Baum-Variante (häufig in Datenbanken)**:
   - Die meisten Datenbanken verwenden **B+-Bäume**, eine Abwandlung des B-Baums, bei der:
     - Nur Blattknoten Daten/Zeiger speichern.
     - Interne Knoten nur Schlüssel für die Weiterleitung haben.
     - Blätter verknüpft sind (doppelt verkettete Liste) für effiziente sequenzielle Scans und Bereichsabfragen (z.B. `SELECT * WHERE age BETWEEN 20 AND 30`).
   - Dies verbessert Bereichsoperationen und Cache-Effizienz.

4. **Operationen in der Praxis**:
   - **INSERT/UPDATE/DELETE**: Der Baum teilt oder fusioniert Knoten, um die Balance zu erhalten. Datenbanken handhaben Nebenläufigkeit mit Latches/Locks.
   - **Abfrageoptimierung**: Der Abfrageplaner verwendet Indexstatistiken, um B-Baum-Indizes anstelle von Tabellenscans zu wählen.
   - **Clustered vs. Non-Clustered**: Bei geclusterten Indizes (z.B. InnoDB in MySQL) sind die Tabellendaten physisch in der Blattreihenfolge des B-Baums gespeichert. Nicht-geclusterte zeigen nur auf die Daten.

#### Vorteile und Kompromisse
- **Vorteile**: Schnell für Gleichheits-, Bereichs- und sortierte Abfragen; kommt gut mit wachsenden Datenmengen zurecht.
- **Nachteile**: Overhead für Einfügungen/Löschungen (Baumwartung); nicht ideal für sehr häufige Updates ohne Batching.

Zusammenfassend sind B-Bäume das Rückgrat der Datenbankleistung für indizierten Zugriff, da sie lineare Suchen durch ihre balancierte, festplattenfreundliche Konstruktion in nahezu konstante Zeitoperationen verwandeln.

#### Referenzen
- [B-tree - Wikipedia](https://en.wikipedia.org/wiki/B-tree)
- [B+ Tree in DBMS - GeeksforGeeks](https://www.geeksforgeeks.org/introduction-of-b-tree/)
- [How Indexes Work in SQL Databases - Use The Index, Luke](https://use-the-index-luke.com/sql/anatomy/index-btree)