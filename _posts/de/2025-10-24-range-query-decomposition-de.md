---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Quadratwurzel-Zerlegung für Bereichsabfragen
translated: true
type: note
---

### Square Root Decomposition

Square Root Decomposition (oft abgekürzt als √-decomposition) ist eine Technik in der Informatik und im Wettbewerbsprogrammieren, die verwendet wird, um Bereichsabfragen und Aktualisierungen auf großen Arrays oder Datenstrukturen zu optimieren. Sie ist besonders nützlich, wenn man Abfragen wie "finde die Summe/das Maximum/das Minimum der Elemente in einem Teilarray" effizient beantworten muss, ohne auf aufwändigere Strukturen wie Segment Trees oder Fenwick Trees zurückzugreifen, die komplexer zu implementieren sein können.

#### Warum sie verwenden?
- **Komplexitätsabwägung**: Für ein Array der Größe \\( n \\) benötigen naive Bereichsabfragen \\( O(n) \\) Zeit pro Abfrage. Square Root Decomposition reduziert dies auf \\( O(\sqrt{n}) \\) pro Abfrage und Aktualisierung, was für viele Probleme, bei denen \\( n \\) bis zu \\( 10^5 \\) oder \\( 10^6 \\) beträgt, eine gute Balance darstellt.
- **Einfachheit**: Sie ist einfacher zu programmieren und zu debuggen als fortgeschrittene Datenstrukturen.
- **Anwendungen**: Häufig bei Problemen mit Bereichssummenabfragen, Bereichsminimumabfragen (RMQ) oder Frequenzzählung in gleitenden Fenstern.

#### So funktioniert es
1. **In Blöcke aufteilen**: Teile das Array in Blöcke der Größe \\( \sqrt{n} \\) (abgerundet) auf. Wenn \\( n = 100 \\), ist die Blockgröße \\( b = 10 \\), sodass man 10 Blöcke erhält.
   - Jeder Block speichert vorberechnete Informationen (z.B. die Summe der Elemente in diesem Block für Summenabfragen).

2. **Abfrage eines Bereichs [L, R]**:
   - **Vollständige Blöcke**: Für komplette Blöcke, die vollständig innerhalb von [L, R] liegen, hole einfach den vorberechneten Wert in \\( O(1) \\) pro Block. Höchstens \\( O(\sqrt{n}) \\) volle Blöcke.
   - **Partielle Blöcke**: Für die Ränder (linke und rechte partielle Blöcke), durchlaufe die einzelnen Elemente manuell, was insgesamt \\( O(\sqrt{n}) \\) Zeit benötigt (da jeder partielle Block die Größe \\( \sqrt{n} \\) hat).
   - Gesamt: \\( O(\sqrt{n}) \\).

3. **Aktualisierungen**: Wenn ein Element aktualisiert wird, baue den vorberechneten Wert für seinen Block in \\( O(\sqrt{n}) \\) Zeit neu auf (durch erneutes Aufsummieren des Blocks).

#### Einfaches Beispiel: Bereichssummenabfrage
Angenommen, wir haben ein Array `A = [1, 3, 2, 4, 5]` und \\( n=5 \\), also Blockgröße \\( b = \sqrt{5} \approx 2 \\). Blöcke:
- Block 0: [1, 3] → Summe = 4
- Block 1: [2, 4] → Summe = 6
- Block 2: [5] → Summe = 5 (der letzte Block kann kleiner sein)

Abfrage der Summe von Index 1 bis 4 (0-basiert: Elemente 3,2,4,5):
- Partieller linker Block: Index 1 (in Block 0) → addiere 3
- Vollständiger Block 1: Addiere 6
- Partieller rechter Block: Index 4 (in Block 2) → addiere 5
- Gesamt: 3 + 6 + 5 = 14

Zur Implementierung im Code (Python-Pseudocode):
```python
import math

class SqrtDecomp:
    def __init__(self, arr):
        self.n = len(arr)
        self.b = int(math.sqrt(self.n))
        self.arr = arr[:]
        self.block_sums = [0] * ((self.n + self.b - 1) // self.b)
        self._build()
    
    def _build(self):
        for i in range(self.n):
            block_id = i // self.b
            self.block_sums[block_id] += self.arr[i]
    
    def update(self, idx, val):
        diff = val - self.arr[idx]
        self.arr[idx] = val
        block_id = idx // self.b
        self.block_sums[block_id] += diff
    
    def query(self, left, right):
        res = 0
        l_block, r_block = left // self.b, right // self.b
        
        if l_block == r_block:
            for i in range(left, right + 1):
                res += self.arr[i]
        else:
            # Linker partieller Block
            for i in range(left, (l_block + 1) * self.b):
                res += self.arr[i]
            # Vollständige Blöcke
            for blk in range(l_block + 1, r_block):
                res += self.block_sums[blk]
            # Rechter partieller Block
            for i in range(r_block * self.b, right + 1):
                res += self.arr[i]
        return res
```

Dies ist eine Basisversion – passe sie für Min/Max an, indem du Min/Max pro Block speicherst anstelle von Summen.

Für vertiefende Einblicke, siehe Ressourcen wie [GeeksforGeeks on Square Root Decomposition](https://www.geeksforgeeks.org/sqrt-decomposition-algorithm-square-root-decomposition-technique-set-1-introduction/) oder [CP-Algorithms](https://cp-algorithms.com/data_structures/sqrt_decomposition.html).