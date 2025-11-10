---
audio: false
generated: true
lang: de
layout: post
title: Quicksort in Rust für erfahrene Entwickler
translated: true
type: note
---

In Ordnung, angesichts Ihres starken Hintergrunds in Algorithmen, Full-Stack-Entwicklung und sogar Mobile Engineering werden Sie Rusts Ansatz für Speichersicherheit und explizite Kontrolle konzeptionell recht vertraut finden, auch wenn die Syntax und Strenge neu sind. Lassen Sie uns diese Quicksort-Implementierung in Rust aufschlüsseln.

-----

### Quicksort in Rust: Ein Tiefer Einblick für erfahrene Entwickler

Dieser Rust-Code implementiert den klassischen **Quicksort-Algorithmus**. Die Kernidee von Quicksort ist es, ein Element als Pivot auszuwählen und das Array so um diesen Pivot herum zu partitionieren, dass Elemente kleiner als der Pivot auf der einen Seite und Elemente größer als der Pivot auf der anderen Seite liegen. Dieser Vorgang wird dann rekursiv auf die Sub-Arrays angewendet.

Gehen wir die Funktionen durch:

-----

### `fn quick_sort(arr: &mut [i32])`

```rust
fn quick_sort(arr: &mut [i32]) {
    if arr.len() <= 1 {
        return;
    }
    let pivot_index = partition(arr);
    let (left, right) = arr.split_at_mut(pivot_index);
    quick_sort(left);
    quick_sort(&mut right[1..]);
}
```

  * **`arr: &mut [i32]`**: Hier zeigt Rusts Typsystem sofort seine Stärken.
      * `&mut` kennzeichnet eine **veränderbare Referenz**. Das bedeutet, die `quick_sort`-Funktion erhält eine geliehene Referenz auf das Array `arr` und darf den Inhalt dieses Arrays *direkt an Ort und Stelle* modifizieren.
      * `[i32]` ist ein **Slice** von `i32`-Integern. In Rust ist `[T]` der Typ für einen Slice, was eine Sicht auf eine zusammenhängende Folge von Elementen darstellt. Er besitzt die Daten nicht; er zeigt lediglich auf einen Teil eines Arrays oder `Vec`. Dies ist entscheidend für die Effizienz, da es das Kopieren von Daten vermeidet. Sie kennen Zeiger und Array-Abschnitte aus Ihrem C/C++/Java-Hintergrund; betrachten Sie dies als Rusts sichere und explizite Art, damit umzugehen.
  * **Basisfall `if arr.len() <= 1`**: Standard-Basisfall für Quicksort. Wenn der Slice 0 oder 1 Element hat, ist er bereits sortiert, also einfach zurückkehren.
  * **`let pivot_index = partition(arr);`**: Ruft die `partition`-Funktion auf (die wir uns als nächstes ansehen), um den Slice neu anzuordnen. Sie gibt die Endposition des Pivot-Elements zurück.
  * **`let (left, right) = arr.split_at_mut(pivot_index);`**: Dies ist ein Schlüsselmerkmal von Rust für sicheres veränderbares Aliasing.
      * `split_at_mut` ist eine Methode auf veränderbaren Slices. Sie nimmt einen Index und teilt den veränderbaren Slice in zwei *disjunkte* veränderbare Slices auf.
      * `left` wird `arr[0..pivot_index]` sein und `right` wird `arr[pivot_index..len]` sein.
      * Dies ist fundamental für Rusts **Borrow Checker**. Man kann nicht zwei veränderbare Referenzen auf die *gleichen Daten* zur gleichen Zeit haben. `split_at_mut` stellt sicher, dass `left` und `right` auf vollständig getrennte Teile des ursprünglichen Arrays verweisen, was den Borrow Checker zufriedenstellt und Datenrennen in einem mehrthreadigen Kontext verhindert (auch wenn dies single-threaded ist, gilt das Prinzip).
  * **`quick_sort(left);`**: Sortiert den `left`-Sub-Slice rekursiv.
  * **`quick_sort(&mut right[1..]);`**: Sortiert den `right`-Sub-Slice rekursiv.
      * `right[1..]` ist wichtig: Der `right`-Slice beginnt bei `pivot_index`. Da `arr[pivot_index]` nun das korrekt positionierte Pivot-Element ist, schließen wir es vom rekursiven Aufruf auf der rechten Seite aus.
      * `&mut` leiht explizit einen veränderbaren Slice von `right` erneut.

-----

### `fn partition(arr: &mut [i32]) -> usize`

```rust
fn partition(arr: &mut [i32]) -> usize {
    let len = arr.len();
    let pivot = arr[len - 1];
    let mut i = 0;
    for j in 0..len - 1 {
        if arr[j] <= pivot {
            arr.swap(i, j);
            i += 1;
        }
    }
    arr.swap(i, len - 1);
    i
}
```

Diese Funktion implementiert das Lomuto-Partitionierungsschema, eine gängige Methode zur Partitionierung eines Arrays für Quicksort.

  * **`let len = arr.len();`**: Ermittelt die Länge des aktuellen Slices.
  * **`let pivot = arr[len - 1];`**: Das **letzte Element** des Slices wird als Pivot gewählt.
  * **`let mut i = 0;`**: `i` fungiert als ein Zeiger auf die "Grenze" zwischen Elementen kleiner oder gleich dem Pivot und Elementen größer als der Pivot. Elemente links von `i` werden kleiner oder gleich dem Pivot sein.
  * **`for j in 0..len - 1`**: Diese Schleife iteriert durch alle Elemente *außer* dem Pivot (der sich bei `len - 1` befindet).
  * **`if arr[j] <= pivot { ... }`**: Wenn das aktuelle Element `arr[j]` kleiner oder gleich dem Pivot ist:
      * **`arr.swap(i, j);`**: Tauscht `arr[j]` mit `arr[i]` aus. Dies bewegt das kleinere Element in den "kleiner oder gleich"-Abschnitt.
      * **`i += 1;`**: Erhöht `i`, um den "kleiner oder gleich"-Abschnitt zu erweitern.
  * **`arr.swap(i, len - 1);`**: Nach der Schleife ist `i` die korrekte Position für den Pivot. Wir tauschen den Pivot (der sich immer noch bei `len - 1` befindet) in seine endgültige sortierte Position. Nun sind alle Elemente links von `i` kleiner oder gleich `arr[i]` (dem Pivot), und alle Elemente rechts davon sind größer.
  * **`i`**: Die Funktion gibt `i` zurück, was der endgültige Index des Pivot-Elements ist.

-----

### `fn main()`

```rust
fn main() {
    let mut arr = [3, 6, 8, 10, 1, 2, 1];
    println!("Before: {:?}", arr);
    quick_sort(&mut arr);
    println!("After: {:?}", arr);
}
```

  * **`let mut arr = [3, 6, 8, 10, 1, 2, 1];`**:
      * `let mut` deklariert eine **veränderbare Variable**. Dies erlaubt es, die Variable neu zuzuweisen oder ihren Inhalt zu modifizieren (wenn es sich um einen veränderbaren Typ handelt).
      * `[3, ...]` erstellt ein **Array fester Größe** auf dem Stack. Seine Größe ist zur Kompilierzeit bekannt.
  * **`println!("Before: {:?}", arr);`**: Verwendet das `println!`-Makro für die Ausgabe.
      * `{:?}` ist der **Debug-Print**-Formatbezeichner. Er verwendet das `Debug`-Trait, um eine menschenlesbare Darstellung des Arrays auszugeben.
  * **`quick_sort(&mut arr);`**: Ruft die `quick_sort`-Funktion auf und übergibt eine veränderbare Referenz auf das `arr`-Array.
  * **`println!("After: {:?}", arr);`**: Gibt das Array erneut nach dem Sortieren aus.

-----

### Rust-spezifische Erkenntnisse für Sie

  * **Ownership und Borrowing**: Dieser Code ist ein Paradebeispiel für Rusts Kernkonzepte. Sie geben **Referenzen (`&` und `&mut`)** weiter, anstatt Daten zu kopieren. Die `&mut`-Referenzen sind entscheidend, um das Array direkt zu modifizieren, und der **Borrow Checker** (z.B. durch `split_at_mut` erzwungen) stellt sicher, dass Sie niemals mehrere veränderbare Referenzen auf die gleichen Daten haben, was eine ganze Klasse von Nebenläufigkeitsfehlern zur Kompilierzeit eliminiert. Dies ist wahrscheinlich der größte Paradigmenwechsel im Vergleich zu Sprachen wie Java oder Python, aber er bietet Speichersicherheit ohne einen Garbage Collector.
  * **Slices `[T]`**: Diese sind unglaublich mächtig für die Arbeit mit zusammenhängenden Daten. Sie bieten eine sichere, effiziente Sicht auf Teile von Arrays oder Vektoren, ohne neuen Speicher allozieren zu müssen.
  * **Makros (`println!`)**: Sie werden `!` nach vielen Standardbibliotheksfunktionen sehen (wie `println!`, `vec!`, `format!`). Dies zeigt an, dass es sich um **Makros** handelt, nicht um reguläre Funktionen. Makros erweitern Code zur Kompilierzeit und bieten mehr Flexibilität und Leistungsfähigkeit (wie variadische Argumente oder Code-Generierung zur Kompilierzeit) im Vergleich zu regulären Funktionen.

Angesichts Ihres Hintergrunds werden Sie wahrscheinlich die Leistungsmerkmale und Sicherheitsgarantien zu schätzen wissen, die Rust bietet, auch wenn die "Borrow Checker-Dance" etwas Gewöhnungszeit erfordert. Es ist eine andere Art, über Speicherverwaltung nachzudenken, die jedoch zu sehr robustem und effizientem Code führt.