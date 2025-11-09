---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Quicksort versus Mergesort
translated: true
type: note
---

### Warum sich Quick Sort knifflig anfühlt (und Merge Sort nicht)

Du hast völlig recht – Quick Sort von Grund auf ohne Referenzen zu implementieren, fühlt sich an, als würde man mit einem eingefetteten Schwein ringen, während Merge Sort eher wie Wäschefalten ist: methodisch und vorhersehbar. Der "Teile, Herrsche, Kombiniere"-Fluss von Merge Sort ist linear und auf saubere Weise rekursiv, ohne Überraschungen im Zusammenführungs-Schritt. Quick Sort hingegen arbeitet *in-place* und verlässt sich auf einen cleveren Partitionierungs-Trick, bei dem Elemente um ein "Pivot"-Element (einen gewählten Teilungspunkt) herum vertauscht werden. Es fühlt sich zunächst chaotisch an, weil das Pivot-Element nicht feststeht – es ist eher wie ein Schiedsrichter, der während des Spiels herumgeschoben wird. Aber sobald man die Intuition verstanden hat, ist es elegant effizient (durchschnittlich O(n log n) Zeit, schlimmstenfalls O(n²) bei schlechten Pivots).

Lass mich Quick Sort mit einer natürlichen, geschichtenähnlichen Perspektive vorstellen: Stell dir vor, du sortierst einen unordentlichen Stapel Bücher in einem Regal nach ihrer Höhe. Anstatt den Stapel in der Mitte zu teilen, alles zu vermessen und dann zu mergen (das ist Merge Sort), wählst du ein Buch als "Benchmark" (das Pivot) und ordnest dann die anderen so um, dass alle kürzeren Bücher links davon und alle längeren rechts davon stehen. Das Pivot landet an seiner *endgültigen* Position, und du rufst die Funktion rekursiv nur für die linken und rechten Teil-Stapel auf. Kein zusätzlicher Platz nötig – nur Vertauschungen im Regal. Es ist wie die niederländische "Quicksort"-Flaggenhisszeremonie (daher der Name), bei der man in drei Gruppen partitioniert: kürzer, Benchmark, länger.

### Warum es funktioniert: Die Magie der Partitionierung

Quick Sort funktioniert wegen **Teile-und-Herrsche mit einer Garantie**: Jeder Partitionierungsschritt platziert *mindestens ein Element* (das Pivot) an seiner korrekten endgültigen Position und verkleinert das Problem damit jedes Mal um mindestens dieses eine Element. Im besten Fall teilt das Pivot das Array gleichmäßig (wie das Halbieren bei Merge Sort), was zu einer ausgeglichenen Rekursion führt. Im schlimmsten Fall (z.B. ein bereits sortiertes Array mit schlechter Pivot-Wahl) degeneriert es zu O(n²) wie Bubble Sort – aber gute Pivot-Wahlen machen es in der Praxis rasend schnell.

Die entscheidende Erkenntnis: **Partitionierung erzwingt Invarianten**. Nach einer Partitionierung:
- Alles links vom Pivot ≤ Pivot.
- Alles rechts vom Pivot ≥ Pivot.
- Das Pivot ist nun für immer sortiert – muss nicht mehr berührt werden.

Dies garantiert Fortschritt: Die Tiefe des Rekursionsbaums ist durchschnittlich höchstens log n, und jede Ebene erledigt insgesamt O(n) Arbeit (Scannen und Vertauschen).

### Wie man das Pivot wählt (und warum es sich "bewegt" während der Vergleiche)

Das Pivot ist nicht heilig – es ist einfach irgendein Element, das du als Benchmark wählst. Schlechte Wahl (wie immer das erste Element) kann die Balance stören, hier ist eine natürliche Progression von Strategien, von einfach zu robust:

1.  **Naiv: Wähle das erste (oder letzte) Element.**
    - Einfach zu programmieren, aber riskant. In einem sortierten Array `[1,2,3,4,5]` bedeutet Pivot=1, dass links leer ist und rechts 4 Elemente sind – die Rekursion wird tief und schief.
    - Die "Bewegung": Während der Partitionierung vergleichst du alles andere mit diesem Pivot-Wert, aber du vertauschst Elemente *um* seine Position herum. Das Pivot selbst wird an seinen Platz getauscht, wenn sich die Grenzen überkreuzen.

2.  **Besser: Wähle das mittlere Element.**
    - Tausche es vorübergehend ans Ende, nutze es als Pivot. Intuitiv ausgeglichener (näher am Median), aber immer noch anfällig für sortierte/umgekehrt sortierte Eingaben.

3.  **Am besten für die Praxis: Wähle ein zufälliges Element.**
    - Tausche es ans Ende, partitioniere. Zufälligkeit mittelt schlechte Fälle aus, macht den Worst-Case unwahrscheinlich (mit hoher Wahrscheinlichkeit immer noch O(n log n)). Das verwenden die meisten Bibliotheken.

4.  **Ausgefallen (für Interviews): Median-of-three.**
    - Wähle den Median von erstem/mittlerem/letztem Element als Pivot. Schnell zu berechnen, umgeht häufige Fallstricke.

Im Code "fixiert" man das Pivot oft, indem man es zunächst ans Ende tauscht, dann um seinen *Wert* (nicht seine Position) herum partitioniert und es dann dahin zurücktauscht, wo es hingehört. Deshalb fühlt es sich so an, als ob sich das Pivot "bewegt" – es ist nicht statisch; der Partitionierungsprozess findet seinen Platz dynamisch über zwei Zeiger (links und rechts), die sich springend aufeinander zubewegen und Regelverstöße vertauschen.

### Ein praktisches Beispiel: Sortieren von [3, 7, 1, 9, 4] mit letztem Element als Pivot

Lass uns einen Partitionsschritt durchgehen. Array: `[3, 7, 1, 9, 4]`. Pivot = letztes = 4. (Wir tauschen es bei Bedarf herum.)

- Starte mit linkem Zeiger bei Index 0 (Wert 3), rechtem Zeiger bei Index 3 (Wert 9, da Pivot bei 4 ist).
- Scanne von links: 3 < 4? Ja, lass es. Nächstes, 7 > 4? Ja, aber warte – wir tauschen mit dem ersten >4 von rechts.
- Eigentlich, Standard-Lomuto-Partition (einfacher Ein-Zeiger-Stil):
  1. i = -1 (Grenze für < Pivot).
  2. Für j von 0 bis n-2 (überspringe Pivot):
     - Wenn arr[j] ≤ Pivot (4), tausche arr[++i] mit arr[j]. (Vergrößere die linke Seite.)
  3. Tausche schließlich das Pivot mit arr[++i], um es zu platzieren.

Schritt-für-Schritt:
- j=0: 3 ≤4? Ja. i=0, tausche arr[0] mit arr[0] (keine Änderung). Array: [3,7,1,9,4]
- j=1: 7 ≤4? Nein. Überspringen.
- j=2: 1 ≤4? Ja. i=1, tausche arr[1] (7) mit arr[2] (1). Array: [3,1,7,9,4]
- j=3: 9 ≤4? Nein. Überspringen.
- Ende: Tausche Pivot (4 bei Index 4) mit arr[++i=2] (7). Array: [3,1,4,9,7]

Jetzt: Links von 4 (Index 2) ist [3,1] (beide ≤4, unsortiert), rechts [9,7] (beide ≥4, unsortiert). Pivot=4 ist *fertig*. Rekursion auf links [3,1] und rechts [9,7].

- Links: Pivot=1, partitioniert zu [1,3].
- Rechts: Pivot=7, partitioniert zu [7,9].

Vollständig sortiert: [1,3,4,7,9]. Siehst du? Jeder Schritt sichert Fortschritt, und Vertauschungen "bewegen" das Pivot nach Hause.

### Pseudocode-Skizze (um die Implementierung zu erleichtern)

```
quicksort(arr, low, high):
    if low < high:
        pivot_idx = partition(arr, low, high)
        quicksort(arr, low, pivot_idx-1)
        quicksort(arr, pivot_idx+1, high)

partition(arr, low, high):  # Lomuto-Stil, Pivot bei high
    pivot = arr[high]
    i = low - 1
    for j in low to high-1:
        if arr[j] <= pivot:
            i += 1
            swap arr[i], arr[j]
    swap arr[i+1], arr[high]
    return i+1
```

Die "Bewegung" passiert in diesen Vertauschungen: Elemente tanzen aneinander vorbei, bis sich das Pivot setzt. Übe es auf Papier mit 5-6 Elementen – sobald die Partitionierung klick macht, fühlt sich die Rekursion natürlich an. Wenn du auf Probleme stößt, versuche, es dir geistig als das Buch-Sortier-Regal vorzustellen.

Für vertiefende Einblicke:
[Quick Sort Visualization](https://visualgo.net/en/sorting?slide=9)
[CLRS Chapter on Quicksort](https://mitpress.mit.edu/sites/default/files/sicp/full-text/book/book-Z-H-20.html#%_sec_3.3)