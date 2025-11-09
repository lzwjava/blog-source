---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Einführung in den Union-Find-Algorithmus
translated: true
type: note
---

### Einführung in den Union-Find (Disjoint Set Union) Algorithmus

Der **Union-Find** Algorithmus (auch **Disjoint Set Union** oder **DSU** genannt) ist eine Datenstruktur und eine Reihe von Operationen, die verwendet werden, um eine Sammlung disjunkter Mengen (Gruppen von Elementen, die sich nicht überschneiden) zu verwalten. Er ist effizient für Probleme, die Gruppierung, Zusammenführung oder Konnektivitätsprüfung beinhalten, wie z.B. in Graphalgorithmen oder Clustering.

Wichtige Operationen:
- **Find**: Bestimmt, zu welcher Menge ein Element gehört (oft durch Finden der "Wurzel" oder des Repräsentanten der Menge).
- **Union**: Führt zwei Mengen zu einer zusammen.

Der Algorithmus glänzt durch Optimierungen wie **Pfadkompression** (Abflachen der Baumstruktur während `find`-Operationen) und **Union by Rank/Size** (Zusammenführen kleinerer Bäume in größere, um die Struktur balanciert zu halten). Dies macht ihn nahezu O(1) amortisierte Zeit pro Operation – sehr schnell für große Datensätze.

#### Kern-Datenstruktur
- Ein Array `p[]` (Eltern-Array): `p[i]` zeigt auf das Elternelement des Elements `i`. Anfangs ist jedes Element sein eigenes Elternelement (`p[i] = i`).
- Optional: Ein `rank[]` Array für Union by Rank, um Zusammenführungen auszugleichen.

#### Die Find-Operation (mit Pfadkompression)
Die `find`-Funktion verfolgt die Pfade von einem Element zurück zu seiner Wurzel. Die von Ihnen erwähnte Zeile – `if (p[i] != -1) i = p[i]` – ist ein rekursiver oder iterativer Schritt in diesem Prozess. Sie folgt den Elternzeigern, bis die Wurzel erreicht ist (wo `p[root] == root` oder `p[root] == -1` für einen Sentinel-Wert).

Hier ist eine einfache iterative Implementierung in Pseudocode:

```
function find(i):
    if p[i] != -1:  # Nicht die Wurzel (oder Sentinel)
        i = p[i]     # Zum Elternelement wechseln (das ist Ihre Zeile!)
        return find(i)  # Rekursiv: weitergehen bis zur Wurzel
    else:
        return i     # Wurzel gefunden
```

**Mit vollständiger Pfadkompression** (um zukünftige `find`-Operationen zu optimieren), flachen wir den Pfad ab, indem wir alle Knoten direkt auf die Wurzel setzen:

```
function find(i):
    if p[i] != i:  # Nicht die Wurzel
        p[i] = find(p[i])  # Komprimieren: Elternelement auf die gefundene Wurzel setzen
    return p[i]
```

- `-1` wird oft als Sentinel-Wert für Wurzeln verwendet (anstelle von `i` für Selbst-Elternschaft), insbesondere in einigen Implementierungen, um nicht initialisierte oder ungültige Knoten zu unterscheiden.
- Ohne Kompression können wiederholte `find`-Operationen die Struktur zu einer langen Kette machen (O(n) Worst Case). Kompression macht sie fast flach.

#### Die Union-Operation
Um die Mengen von `x` und `y` zusammenzuführen:
1. Wurzeln finden: `rootX = find(x)`, `rootY = find(y)`.
2. Wenn `rootX != rootY`, verlinke eine mit der anderen (z.B. nach Rang: hänge den kleineren Rang an den größeren).

Pseudocode:
```
function union(x, y):
    rootX = find(x)
    rootY = find(y)
    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            p[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            p[rootX] = rootY
        else:
            p[rootY] = rootX
            rank[rootX] += 1  # Rang für das neue Elternelement erhöhen
```

#### Verwendung des Algorithmus
Union-Find ist ideal für dynamische Konnektivitätsprobleme. Hier ist eine Schritt-für-Schritt-Anleitung mit Beispielen:

1. **Initialisierung**:
   - Erstelle `p[]` der Größe `n` (Anzahl der Elemente): `for i in 0 to n-1: p[i] = -1` (oder `i` für Selbst-Elternschaft).
   - Optional: `rank[]` alle auf 0 oder 1 setzen.

2. **Grundlegender Ablauf**:
   - Um zu prüfen, ob zwei Elemente in derselben Menge sind: `if find(a) == find(b)`.
   - Um zusammenzuführen: `union(a, b)`.
   - Verarbeite Abfragen/Zusammenführungen in beliebiger Reihenfolge – es ist dynamisch!

3. **Beispiel: Erkennen verbundener Komponenten in einem Graph**
   Stell dir einen Graphen mit 5 Knoten (0-4) und Kanten wie (0-1), (1-2), (3-4) vor.
   ```
   // Init
   p = [-1, -1, -1, -1, -1]
   rank = [0, 0, 0, 0, 0]

   // Kanten zusammenführen
   union(0, 1)  // Führt 0 und 1 zusammen, z.B. p[0]=-1, p[1]=0
   union(1, 2)  // Führt 2 in {0,1} ein, p[2]=0
   union(3, 4)  // Führt {3,4} zusammen, z.B. p[3]=-1, p[4]=3

   // Abfrage: Sind 0 und 2 verbunden? find(0)=0, find(2)=0 → Ja
   // Sind 2 und 3 verbunden? find(2)=0, find(3)=-1 → Nein
   ```

4. **Praktische Anwendungen**:
   - **Kruskals Algorithmus für minimalen Spannbaum**: Kanten nach Gewicht sortieren, nicht-zyklusbildende Kanten zusammenführen (überspringen, wenn `find(u) == find(v)`).
   - **Freunde in sozialen Netzwerken**: Freunde zusammenführen, gemeinsame Verbindungen finden.
   - **Bildsegmentierung**: Benachbarte Pixel mit ähnlicher Farbe zusammenführen.
   - **Zyklenerkennung in ungerichteten Graphen**: Endpunkte zusammenführen; wenn bereits in derselben Menge, existiert ein Zyklus.

#### Einfache Python-Implementierung
```python
class UnionFind:
    def __init__(self, n):
        self.p = [-1] * n
        self.rank = [0] * n
    
    def find(self, i):
        if self.p[i] != -1 and self.p[i] != i:  # Behandelt Sentinel + Selbst-Elternschaft
            self.p[i] = self.find(self.p[i])  # Pfadkompression
        return self.p[i] if self.p[i] != -1 else i
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            if self.rank[px] > self.rank[py]:
                self.p[py] = px
            elif self.rank[px] < self.rank[py]:
                self.p[px] = py
            else:
                self.p[py] = px
                self.rank[px] += 1

# Verwendung
uf = UnionFind(5)
uf.union(0, 1)
uf.union(1, 2)
print(uf.find(0) == uf.find(2))  # True
```

Dies hält die Dinge effizient – probiere es mit größerem `n` aus, um die Geschwindigkeit zu sehen!

Für mehr Tiefe, siehe [GeeksforGeeks: Union-Find Algorithm](https://www.geeksforgeeks.org/union-find-algorithm-set-2-union-by-rank-and-path-compression/) oder [CP-Algorithms: DSU](https://cp-algorithms.com/data_structures/disjoint_set_union.html).