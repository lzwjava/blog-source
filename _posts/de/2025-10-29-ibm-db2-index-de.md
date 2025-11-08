---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: IBM DB2 Indexstruktur erklärt
translated: true
type: note
---

### Wie IBM DB2-Indizes funktionieren

IBM DB2 verwendet **B+-Bäume** als primäre Datenstruktur für seine Indizes. Dies ist eine Variante eines balancierten Baums, die für speicherbasierte Speicherung und Bereichsabfragen optimiert ist, was in relationalen Datenbanken üblich ist. B+-Bäume gewährleisten effiziente Suchen, Einfügungen und Löschungen mit logarithmischer Zeitkomplexität (O(log n)), was sie ideal für große Datensätze macht. Im Folgenden werde ich die Struktur, Schlüsseloperationen und DB2-spezifische Hinweise aufschlüsseln.

#### B+-Baum-Struktur in DB2
Ein B+-Baum in DB2 ist in eine Hierarchie von **Seiten** (auch Knoten genannt) organisiert, jede typischerweise 4 KB groß auf der Festplatte. Der Baum ist selbstbalancierend, was bedeutet, dass alle Blattknoten auf derselben Tiefe sind, und er wächst oder schrumpft dynamisch, wenn sich Daten ändern. Hier die Aufschlüsselung:

- **Wurzelseite**: Der Einstiegspunkt an der Spitze des Baums. Sie enthält sortierte Schlüsselwerte und Zeiger auf untergeordnete Seiten. Bei kleinen Indizes kann die Wurzel direkt auf Blattseiten zeigen.
  
- **Interne (Nicht-Blatt-) Seiten**: Diese Zwischenebenen fungieren als Verzeichnisse. Jede Seite enthält:
  - Eine sortierte Liste von **Indexschlüsseln** (die Werte der indizierten Spalte(n), z.B. Mitarbeiter-IDs).
  - Zeiger auf untergeordnete Seiten (ein Zeiger mehr als Schlüssel, um Bereiche zu trennen).
  - Insbesondere ist jeder Eintrag der **höchste Schlüsselwert** im Teilbaum darunter, gepaart mit einer **Record Identifier (RID)** – einem eindeutigen Zeiger auf die Seite und den Slot, wo die eigentliche Datenzeile in der Tabelle lebt.
  
  Nicht-Blatt-Seiten speichern *keine* tatsächlichen Datenzeiger; sie leiten die Traversierung.

- **Blattseiten**: Die unterste Ebene, bidirektional (vorwärts und rückwärts) verknüpft für effiziente Bereichsscans. Jede Blattseite enthält:
  - Vollständige sortierte **Schlüsselwerte** aus der/den indizierten Spalte(n).
  - Zugehörige **RIDs**, die direkt auf die Tabellenzeilen zeigen.
  - Zeiger auf benachbarte Blattseiten, die sequenziellen Zugriff ermöglichen (z.B. für `WHERE Spalte BETWEEN x AND y`).

Der Baum beginnt mit mindestens 2 Ebenen (Wurzel + Blätter) und kann für massive Tabellen (Millionen von Zeilen) auf 3–5+ Ebenen wachsen. Die Anzahl der Ebenen (NLEVELS) ist über `SYSCAT.INDEXES` abfragbar und beeinflusst die Leistung – weniger Ebenen bedeuten schnellere Traversierungen, aber DB2 verwaltet dies automatisch.

Indizes werden getrennt von Tabellen in ihrem eigenen Tablespace gespeichert und verbrauchen Speicherplatz proportional zu den indizierten Daten (z.B. könnte ein eindeutiger Index auf einer 1-Million-Zeilen-Tabelle ~10–20 % der Tabellengröße beanspruchen).

#### Wie das Suchen funktioniert
1. Beginnen bei der **Wurzelseite** und laden sie in den Speicher.
2. Vergleichen des Suchschlüssels (z.B. `WHERE id = 123`) mit den sortierten Schlüsseln in der aktuellen Seite.
3. Auswählen des entsprechenden untergeordneten Zeigers (z.B. wenn Suchschlüssel > aktueller Schlüssel, dann nach rechts gehen).
4. Wiederholen entlang des Baums nach unten (typischerweise 1–5 I/O-Operationen), bis eine **Blattseite** erreicht wird.
5. In der Blattseite die sortierten Schlüssel scannen, um Übereinstimmungen zu finden, dann die RID verwenden, um die genaue Zeile aus der Tabelle zu holen (eine weitere I/O).

Diese Pfadkomprimierung hält die Traversierungen flach. Für Bereichsabfragen, sobald man bei der Start-Blattseite ist, den Geschwister-Links folgen, um sequenziell zu scannen, ohne im Baum zurückzuspringen.

#### Einfügen und Löschen
- **Einfügen**:
  1. Zur korrekten Blattseite traversieren (wie bei der Suche).
  2. Den neuen Schlüssel + RID in die sortierte Blattseite einfügen.
  3. Wenn die Seite überläuft (die maximale Anzahl von Einträgen überschreitet, ~200–500, abhängig von der Schlüsselgröße), teilt man sie in zwei Seiten und fügt einen Trennschlüssel in die übergeordnete (interne) Seite ein.
  4. Wenn die übergeordnete Seite überläuft, teilt man sie nach oben (kann eine neue Wurzel erzeugen). DB2 sperrt Seiten kurzzeitig für Nebenläufigkeit.

- **Löschen**:
  1. Zur Blattseite traversieren und den Schlüssel + RID entfernen.
  2. Wenn die Seite unterläuft (zu wenige Einträge), von einer Geschwisterseite borgen oder mit ihr zusammenführen und den Trennschlüssel aus der übergeordneten Seite entfernen.
  3. Bei Bedarf Zusammenführungen nach oben fortpflanzen. DB2 kann die Reorganisation verzögern, um Änderungen für Effizienz zu bündeln.

Diese Operationen erhalten das Gleichgewicht automatisch, mit minimalen Seitenaufteilungen/-zusammenführungen (~1 % der Operationen).

#### DB2-spezifische Funktionen
- **Optimierte B+-Bäume** (in DB2 für z/OS): Erweitert für Mainframe-Nebenläufigkeit, mit fraktalem Prefetching, um Seiten vorherzusagen und vorzuladen, was I/O reduziert.
- **Clustering**: Indizes können "geclustert" sein (Daten physisch nach Indexreihenfolge sortiert) für bessere Bereichsleistung.
- **Typen**: Unterstützt eindeutige, zusammengesetzte (mehrspaltige) und Bitmap-Indizes, alle B+-basiert. Keine nativen Hash-Indizes.
- **Wartung**: `RUNSTATS` nach Massenänderungen ausführen, um die Statistiken für den Optimierer zu aktualisieren. Tools wie `INSPECT` prüfen auf Probleme.

B+-Bäume sind in DB2 hervorragend, weil sie zufälligen I/O minimieren (entscheidend für speichergebundene Systeme) und sortierten Zugriff ohne vollständige Tabellenscans unterstützen.

[Indexstruktur - IBM](https://www.ibm.com/docs/en/db2/11.1.0?topic=indexes-index-structure)  
[DB2 LUW-Indizes: B-Baum-Details](https://datageek.blog/2013/09/19/db2-luw-basics-indexes/)  
[Inside Db2 for z/OS: Wie optimierte B+-Bäume Hochgeschwindigkeits-Indizierung antreiben](https://planetmainframe.com/2025/06/inside-db2-for-z-os-how-optimized-b-trees-power-high-speed-indexing/)  
[Wie man die DB2-B-Baum-Indexstruktur schnell versteht](https://srinimf.com/2021/07/26/db2-how-to-understand-b-tree-structure-of-index/)  
[Db2-Index-Überblick](https://www.idug.org/news/db2-index-overview)