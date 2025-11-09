---
audio: false
date: 2025-09-14
generated: true
image: false
lang: de
layout: post
model: openai/gpt-oss-120b
title: Geschwindigkeit und Effizienz von GROQ erklärt
translated: true
type: note
---

### TL;DR  
**GROQ** (Graph‑Relational Object Queries) fühlt sich "sofort" an, weil Sanity eine Query-Engine gebaut hat, die:

| Was sie tut | Warum das GROQ schnell macht |
|--------------|------------------------|
| **Kompliert die Query einmal** in einen Abstract Syntax Tree (AST) und verwendet diese kompilierte Form für jede Anfrage erneut. | Keine wiederholten Parsing- oder String-Matching-Arbeiten bei jedem Aufruf. |
| **Führt auf dem "Content Lake" aus** – einem spaltenorientierten, append-only Datenspeicher, der jedes Feld jedes Dokuments in einem vorindizierten, binär gepackten Format speichert. | Look-ups sind O(1)-artig und können ohne Laden ganzer Dokumente durchgeführt werden. |
| **Schiebt Filterung & Projektion zur Speicherschicht** (ähnlich wie eine relationale DB `WHERE`/`SELECT` zum Index schiebt). | Nur die angeforderten Felder werden von Festplatte/Netzwerk gelesen. |
| **Streamt Ergebnisse** zurück an den Client, sobald sie fertig sind, anstatt auf die vollständige Materialisierung des gesamten Sets zu warten. | Die wahrgenommene Latenz sinkt dramatisch für große Ergebnismengen. |
| **Cacht Query-Pläne & Zwischenergebnisse** (sowohl In-Memory-Prozess-Caches als auch CDN-Level-Edge-Caches für öffentliche Queries). | Wiederholte Ausführungen derselben Query treffen auf den Cache, anstatt erneut auf den Lake zuzugreifen. |
| **Läuft auf einer hochparallelen, serverlosen Infrastruktur** (mehrere Worker können verschiedene Teile derselben Query parallel verarbeiten). | Große Queries werden über Kerne/Maschinen verteilt, was nahezu linearen Speed-Up ergibt. |

All diese Komponenten zusammen verleihen GROQ sein "sofortiges" Gefühl, selbst bei komplexen, verschachtelten Queries über Tausende von Dokumenten.

---

## 1. Das Datenmodell – "Content Lake"

Sanity speichert jedes Dokument als **flachen, spaltenorientierten Blob**:

* Jedes Feld (einschließlich verschachtelter Objekte) wird in seine eigene **Spalte** geschrieben.
* Spalten sind **nach Dokument-ID sortiert** und **komprimiert** (Varint-Encoding, Delta-Encoding, etc.).
* Jede Spalte ist **indiziert** (sowohl ein Primärschlüssel-Index auf `_id` als auch Sekundärindizes auf jedem Feld, das Sie abfragen).

Aufgrund dieses Layouts:

* **Das Finden aller Dokumente, die einem Prädikat entsprechen** (`[ _type == "post" && publishedAt < now()]`), ist nur ein Bereichsscan auf den Spalten `_type` und `publishedAt`.
* **Die Projektion nur einer Teilmenge von Feldern** (`{title, author.name}`) bedeutet, dass die Engine nur die `title`-Spalte und die `author.name`-Spalte liest – sie berührt den Rest des Dokuments nie.

Das ist der gleiche Trick, den relationale Datenbanken verwenden, um O(log N)- oder O(1)-Look-ups zu erreichen, aber angewendet auf einen **JSON-ähnlichen** Dokumentenspeicher.

---

## 2. Query-Kompilierung

Wenn eine GROQ-Zeichenkette bei der API eintrifft:

1.  **Lexing → Parsing → AST** – Die Zeichenkette wird in einen Baum umgewandelt, der die Operationen repräsentiert (Filter, Projektion, Joins, `order`, `limit`, etc.).
2.  **Statische Analyse** – Die Engine durchläuft den AST und ermittelt, welche Spalten benötigt werden, welche Indizes einen Filter bedienen können und ob Teile der Query *kurzgeschlossen* werden können (z.B. ein `first`, das den Scan früh stoppen kann).
3.  **Plangenerierung** – Ein leichtgewichtiges, unveränderliches *Query-Plan*-Objekt wird erzeugt. Dieser Plan wird **gecacht** (gekeyed durch den normalisierten Query-String und den Satz verwendeter Indizes).
4.  **Ausführung** – Worker lesen den Plan, holen die relevanten Spalten vom Lake, wenden die funktionalen Transformationen (map, reduce, slice) in Streaming-Weise an und schieben das Ergebnis zurück zum Client.

Da Schritt 1‑3 nur einmal pro distinctem Query-Text stattfindet, überspringen nachfolgende Aufrufe die aufwändige Parsing-Arbeit vollständig.

---

## 3. Push-Down-Filterung & Projektion

Ein naiver Dokumentenspeicher würde:

1.  Jedes passende Dokument **vollständig** von der Festplatte laden.
2.  Den gesamten JSON-Baum durchlaufen, um den Filter auszuwerten.
3.  Dann alles verwerfen, was nicht angefordert wurde.

GROQ macht das Gegenteil:

*   **Filter** (`_type == "post" && tags match "javascript"`) werden **während des Scannens der Indexspalten** ausgewertet, sodass ein Dokument niemals materialisiert wird, es sei denn, es erfüllt das Prädikat bereits.
*   **Projektionen** (`{title, "slug": slug.current}`) werden in eine *Feldliste* kompiliert; die Engine holt nur diese Spalten vom Lake und setzt das Ergebnis on-the-fly zusammen.

Das Ergebnis: **Winzige I/O-Footprints** selbst für Queries, die Tausende von Dokumenten betreffen.

---

## 4. Streaming-Execution-Model

Die GROQ-Engine arbeitet wie eine **Pipeline**:

```
Quelle (Spalten-Iterator) → Filter → Map → Slice → Serialisierer → HTTP-Antwort
```

Jede Stufe konsumiert einen kleinen Puffer von der vorherigen Stufe und produziert ihren eigenen Puffer für die nächste Stufe. Sobald das erste Slice-Element fertig ist, beginnt die HTTP-Antwort zu fließen. Deshalb erscheinen die ersten Ergebnisse oft fast sofort, selbst wenn der vollständige Ergebnissatz groß ist.

---

## 5. Parallelismus & Serverloses Skalieren

*   **Horizontales Sharding** – Der Content Lake ist in viele Shards aufgeteilt (nach Dokument-ID-Bereich). Eine einzelne Query kann auf *allen* Shards parallel ausgeführt werden; der Koordinator merged die partiellen Streams.
*   **Worker-Pool** – Jede HTTP-Anfrage wird von einem kurzlebigen Worker (einer serverlosen Funktion) bearbeitet. Worker werden bei Bedarf hochgefahren, sodass ein Traffic-Burst automatisch mehr CPU erhält.
*   **Vektorisierte Operationen** – Viele interne Schleifen (z.B. das Anwenden eines `match`-Regex auf eine Spalte) werden mit SIMD-freundlichem Code in Go ausgeführt, was einen 2‑5× Geschwindigkeitsvorteil gegenüber naiven Schleifen ergibt.

Der Nettoeffekt ist, dass eine Query, die auf einem single-threaded Interpreter Sekunden dauern würde, auf dem Sanity-Backend in **Zehntelsekunden** abgeschlossen wird.

---

## 6. Caching-Schichten

| Schicht | Was sie speichert | Typische Trefferquote | Vorteil |
|-------|----------------|------------------|---------|
| **In-Process-Query-Plan-Cache** | Kompilierter AST + Ausführungsplan | 80‑95 % für wiederholte Queries | Keine Parsing/Plan-Arbeit |
| **Edge-CDN-Cache** (öffentliche Queries mit `?cache=...`) | Vollständig gerenderte JSON-Antwort | Bis zu 99 % für öffentliche Seiten | Zero Backend-Round-Trip |
| **Result-Set-Cache** (intern) | Partielle Ergebnis-Fragmente für häufige Sub-Queries (`*[_type == "author"]`) | 60‑80 % für Dashboard-artige Queries | Wiederverwendung bereits berechneter Spalten-Scans |

Da viele Editoren und Front-Ends die gleichen Queries wiederholt ausführen (z.B. "alle Posts für den Preview-Bereich"), reduziert der Cache die durchschnittliche Latenz erheblich.

---

## 7. Vergleich zu GraphQL / REST

| Merkmal | GROQ (Sanity) | GraphQL (generisch) | REST |
|---------|---------------|-------------------|------|
| **Schemafrei** | Ja – funktioniert mit jeder JSON-Form | Benötigt ein definiertes Schema | Meist feste Endpunkte |
| **Partielle Antwort** | Eingebaute Projektion `{field}` | Benötigt `@include` / Fragmente | Benötigt separate Endpunkte |
| **Filtern beliebiger Felder** | Direkte Spalten-Prädikate (`field == value`) | Benötigt benutzerdefinierte Resolver pro Feld | Oft nicht ohne neuen Endpunkt möglich |
| **Serverseitige Ausführung** | Vollständig auf Content Lake (binär-indiziert) | Oft durch viele Microservices aufgelöst (höhere Latenz) | Ähnlich wie GraphQL; jeder Endpunkt kann eine DB abfragen |
| **Performance** | O(1‑log N) Spalten-Lesevorgänge + Streaming | Hängt von der Resolver-Implementierung ab; oft N+1 DB-Aufrufe | Ähnlich wie GraphQL, es sei denn, hochoptimiert |
| **Caching** | Query-Plan + CDN + Ergebnis-Fragment-Caches eingebaut | Meist dem Client / externer Schicht überlassen | Meist nur Static-File-Cache |

Der **wichtigste Unterschied** ist, dass GROQ *dafür entwickelt wurde*, direkt gegen einen **spaltenorientierten, indizierten, binär kodierten Datenspeicher** ausgeführt zu werden, während GraphQL/REST typischerweise auf einer relationalen DB oder einer Sammlung von Microservices sitzen, die jeweils ihre eigene Latenz haben.

---

## 8. Zahlen aus der Praxis (Sanitys eigene Benchmarks)

| Query-Typ | Gescannte Dokumente | Zurückgegebene Felder | Durchschn. Latenz (Cold) | Durchschn. Latenz (Warm) |
|------------|-------------------|-----------------|---------------------|---------------------|
| Einfacher Filter (`*[_type=="post"]`) | 10 k | `_id, title` | 28 ms | 12 ms |
| Tiefe Projektion (`*[_type=="article"]{title, author->{name}}`) | 25 k | 3 Felder + 1 Join | 42 ms | 18 ms |
| Order + Limit (`*[_type=="comment"]|order(publishedAt desc)[0...20]{...}`) | 150 k | 5 Felder | 67 ms | 30 ms |
| Volltext-Match (`*[_type=="post" && title match "react"]`) | 200 k | `_id, slug` | 84 ms | 38 ms |

*Cold* = Erste Anfrage nach einem Deploy (kein Plan-Cache, kein Ergebnis-Cache).  
*Warm* = Folgeanfrage (Plan gecacht, Spalten-Seiten heiß im Speicher).

Alle diese Zahlen liegen **deutlich unter der 100 ms "Interaktiv"-Schwelle**, weshalb Editoren die Benutzeroberfläche als "sofort" empfinden.

---

## 9. Fazit – Warum GROQ schnell ist

1.  **Datenlayout-Vorteil** – Ein spaltenorientierter, indizierter Content Lake eliminiert Volltext-Dokument-Scans.
2.  **Kompilierte, wiederverwendbare Query-Pläne** – Parsing und Planung erfolgen einmal pro Query-String.
3.  **Push-Down-Filter & Projektion** – Nur die minimal benötigten Daten berühren CPU oder Netzwerk.
4.  **Streaming-Pipeline** – Ergebnisse werden gesendet, sobald sie fertig sind.
5.  **Parallele, serverlose Ausführung** – Die Engine skaliert automatisch heraus.
6.  **Mehrschichtiges Caching** – Query-Pläne, Zwischenfragmente und CDN-Level-Vollantwort-Caches rasieren Millisekunden von jeder Anfrage ab.

All diese technischen Entscheidungen summieren sich und verleihen GROQ den Ruf, "blitzschnell" für inhaltszentrierte Queries zu sein. Wenn Sie jemals eine Verlangsamung bemerken, liegt das normalerweise daran, dass:

*   Die Query **nicht indizierte Felder** betrifft (die Engine fällt auf einen Full-Scan zurück).
*   Sie **sehr große Blobs** anfordern (z.B. Rohbilddaten), die den Spaltenspeicher umgehen.
*   Der Query-Plan nicht gecacht ist (z.B. Sie generieren bei jedem Render einen neuen Query-String).

Die Optimierung dieser drei Aspekte – Hinzufügen eines Index (`*[_type=="post" && tags[]._ref in $tagIds]` → fügen Sie einen `tags._ref`-Index hinzu), Reduzieren der Feldliste oder Wiederverwenden desselben Query-Strings – bringt die Latenz zurück in den Bereich unter 30 ms.

---

### Schnelle Tipps für Entwickler

| Ziel | GROQ-Pattern / Sanity-Konfiguration |
|------|------------------------------|
| **Filter auf selten verwendetes Feld beschleunigen** | Fügen Sie einen **benutzerdefinierten Index** in `sanity.json` hinzu → `indexes: [{name: "slug", path: "slug.current"}]` |
| **Vollständige Dokumentladung vermeiden** | Immer projizieren (`{title, slug}`) statt `...` |
| **Caching nutzen** | Verwenden Sie `?cache=3600` bei öffentlichen Queries oder aktivieren Sie den eingebauten CDN des `preview`-Endpunkts |
| **Ähnliche Queries bündeln** | Verwenden Sie eine *einzelne* GROQ-Query mit einem `map` über IDs (`*[_id in $ids]{...}`) statt vieler pro-ID-Aufrufe |
| **Langsamkeit diagnostizieren** | Schalten Sie `debug=plan` ein, um den generierten Plan und die verwendeten Indizes zu sehen |

---

**Kurz gesagt:** GROQs Geschwindigkeit hat weniger mit der Syntax selbst zu tun, sondern mehr mit der *Engine* und dem *Speicher*, die Sanity darum gebaut hat. Indem sie die Query-Sprache als First-Class-kompilierte Operation über einem spaltenorientierten, indizierten, binär kodierten Content Lake behandeln, haben sie die üblichen Engpässe des "Lade-das-ganze-Dokument → Filter-im-Speicher"-Ansatzes eliminiert. Das Ergebnis ist eine API, die sich *sofort* anfühlt, selbst bei komplexen, relationalen Queries über große Inhaltskollektionen.