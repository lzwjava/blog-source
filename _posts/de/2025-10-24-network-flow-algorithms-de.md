---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Netzflussalgorithmen erklärt
translated: true
type: note
---

### Grundlagen von Netzwerkfluss-Algorithmen

Netzwerkfluss-Algorithmen sind ein grundlegendes Thema in der Graphentheorie und Informatik. Sie werden verwendet, um Probleme zu modellieren und zu lösen, die den Fluss von Ressourcen durch ein Netzwerk betreffen (wie z.B. Rohre, Straßen oder Datenströme). Sie sind entscheidend für Optimierungsaufgaben wie den maximalen Fluss (z.B. wie viel Wasser durch ein System von Rohren fließen kann), den minimalen Schnitt (z.B. das Auffinden von Engpässen) und finden Anwendung in den Bereichen Transport, Ablaufplanung und Matching.

Ich werde dies Schritt für Schritt aufschlüsseln: Schlüsselkonzepte, ein einfaches Beispiel, Hauptalgorithmen und Tipps für ein tieferes Verständnis. Wir konzentrieren uns auf das Max-Flow-Problem, da es den Kern darstellt.

#### 1. Schlüsselkonzepte
- **Graph-Darstellung**: Ein Netzwerk ist ein gerichteter Graph \\( G = (V, E) \\) mit Knoten \\( V \\) und Kanten \\( E \\) (Verbindungen). Jede Kante hat eine **Kapazität** \\( c(u, v) \\), den maximalen Fluss, den sie von Knoten \\( u \\) zu \\( v \\) transportieren kann.
- **Quelle und Senke**: Ein Knoten ist die **Quelle** \\( s \\) (wo der Fluss beginnt) und ein Knoten ist die **Senke** \\( t \\) (wo er endet).
- **Fluss**: Eine Funktion \\( f(u, v) \\), die jedem Kantenpaar einen Fluss zuweist und folgende Bedingungen erfüllt:
  - **Kapazitätsbeschränkung**: \\( 0 \leq f(u, v) \leq c(u, v) \\).
  - **Flusserhaltung**: Für jeden Knoten, der nicht \\( s \\) oder \\( t \\) ist, gilt: Zufluss = Abfluss (keine Ansammlung).
- **Nettofluss**: Der Fluss ist antisymmetrisch: \\( f(u, v) = -f(v, u) \\).
- **Residualgraph**: Zeichnet die verbleibende Kapazität nach dem Senden von Fluss auf. Wenn man einen Fluss \\( f \\) auf eine Kante mit Kapazität \\( c \\) sendet, ist die verbleibende Kapazität in Vorwärtsrichtung \\( c - f \\) und in Rückwärtsrichtung \\( f \\) (um Fluss "rückgängig" zu machen).
- **Ziele**:
  - **Maximaler Fluss**: Maximieren des Gesamtflusses von \\( s \\) nach \\( t \\).
  - **Minimaler Schnitt**: Partitioniere die Knoten in \\( S \\) (mit \\( s \\)) und \\( T \\) (mit \\( t \\)); minimiere die Summe der Kapazitäten von \\( S \\) nach \\( T \\). Nach dem Max-Flow-Min-Cut-Theorem gilt: max flow = min cut capacity.

#### 2. Ein einfaches Beispiel
Stellen Sie sich ein kleines Netzwerk für den Warentransport vor:

- Knoten: \\( s \\) (Quelle), A, B, \\( t \\) (Senke).
- Kanten:
  - \\( s \to A \\): Kapazität 10
  - \\( s \to B \\): Kapazität 10
  - \\( A \to B \\): Kapazität 2
  - \\( A \to t \\): Kapazität 8
  - \\( B \to t \\): Kapazität 9

ASCII-Visualisierung:
```
  s
 / \
10  10
A   B
| \ / |
8  2  9
 \ /  
  t
```

Was ist der maximale Fluss? Intuitiv: Sende 10 zu A und 10 zu B, aber A kann nur 8 zu t schieben (2 gehen zu B, was B hilft, 9+2=11 zu schieben, aber Bs Limit ist 9? Warten Sie, rechnen wir es korrekt aus.

Mit einem Algorithmus (siehe unten) beträgt der maximale Fluss 17:
- Pfad 1: s→A→t (Fluss 8), Residualgraphen aktualisieren.
- Pfad 2: s→B→t (Fluss 9), Residualgraphen aktualisieren.
- Pfad 3: s→A→B→t (Fluss 0? Warten Sie, nach dem ersten hat A noch 2 übrig für B, aber B zu t hat 0 übrig – tatsächlich, anpassen).

Besser: Gesamt von s ist 20, aber Engpässe begrenzen auf 17 (8 direkt von A + 9 von B, mit 2 umgeleitet? Nein – Algorithmus für Genauigkeit ausführen.

#### 3. Hauptalgorithmen
Beginnen Sie mit den Grundlagen; arbeiten Sie sich zu effizienteren vor. Alle Algorithmen erhöhen den Fluss entlang von Pfaden im Residualgraphen, bis keine augmentierenden Pfade mehr existieren.

- **Ford-Fulkerson-Methode** (1956, grundlegend):
  - Wiederholtes Finden eines beliebigen Pfades von s nach t im Residualgraphen (z.B. via DFS/BFS).
  - Erhöhe den Fluss um die minimale Residualkapazität auf diesem Pfad.
  - Wiederhole, bis kein Pfad mehr existiert.
  - **Zeit**: Hängt von der Implementierung ab; kann langsam sein, wenn Kapazitäten irrational sind (aber für Ganzzahlen: O(|E| * max_flow)).
  - **Vorteile**: Einfach. **Nachteile**: Ineffizient für große Graphen.
  - Pseudocode:
    ```
    while there is a path P from s to t in residual graph:
        bottleneck = min residual capacity on P
        augment flow along P by bottleneck
        update residuals
    return total flow
    ```

- **Edmonds-Karp** (1972, BFS-Variante von Ford-Fulkerson):
  - Verwende BFS, um den kürzesten augmentierenden Pfad zu finden (vermeidet lange Pfade).
  - **Zeit**: O(|V| * |E|^2) — polynomiell, praktisch für kleine Graphen.
  - Großartig zum Lernen; in ~50 Codezeilen implementierbar.

- **Dinic's Algorithmus** (1970, schneller):
  - Baut einen **Level-Graphen** via BFS auf (Schichten nach Entfernung von s).
  - Verwendet DFS, um blockierende Flüsse zu finden (mehrere Pfade pro Level).
  - **Zeit**: O(|V|^2 * |E|) im schlimmsten Fall, aber O(|V| * |E|) für Einheitskapazitäten; sehr schnell in der Praxis.
  - **Wann zu verwenden**: Mittelgroße bis große Graphen.

- **Push-Relabel (oder Preflow-Push)** (1980er, Goldberg-Tarjan):
  - "Schiebt" überschüssigen Fluss von Knoten in Richtung Senke unter Verwendung von Heuristiken.
  - **Zeit**: O(|V|^3) oder besser mit FIFO/Gap-Heuristiken.
  - **Vorteile**: Bewältigt sehr große Graphen (z.B. Internet-Routing).

Für den minimalen Schnitt: Nach der Max-Flow-Berechnung ist der Schnitt die im finalen Residualgraphen von s aus erreichbaren Knoten vs. die anderen.

#### 4. Implementierungstipps
- Verwenden Sie Adjazenzlisten für Graphen.
- Im Code (Python-ähnlich): Stellen Sie Residualkapazitäten als ein Dictionary von Dictionaries dar.
- Bibliotheken: NetworkX (Python) hat eingebaute Funktionen wie `maximum_flow`.
- Testen Sie an kleinen Beispielen; visualisieren Sie mit Tools wie Graphviz.

#### 5. Häufige Fallstricke & Erweiterungen
- **Zyklen**: Residualgraphen behandeln "Rückfluss" zur Anpassung.
- **Mehrere Quellen/Senken**: Fügen Sie eine Super-Quelle/Senke hinzu.
- **Kosten**: Für Min-Cost-Flow, fügen Sie Kantenkosten hinzu und verwenden Sie successive shortest paths.
- **Anwendungen**: Flugplanerstellung (Airline Scheduling), Bildsegmentierung (Computer Vision), bipartites Matching (setze Fluss=1).

#### Lernpfad
- Lesen Sie CLRS (Cormen et al.) Kapitel 26.
- Üben Sie auf LeetCode/HackerRank (z.B. "Minimum Cost to Make at Least One Valid Path").
- Visualisieren Sie: Zeichnen Sie die Residualgraphen nach jeder Augmentierung.

[Introduction to Network Flows](https://www.geeksforgeeks.org/maximum-bipartite-matching/)  
[Max Flow Min Cut Theorem](https://en.wikipedia.org/wiki/Max-flow_min-cut_theorem)  
[NetworkX Tutorial](https://networkx.org/documentation/stable/tutorial.html)