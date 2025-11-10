---
audio: false
generated: true
image: false
lang: de
layout: post
title: Rusts `mut` und `&mut` erklärt
translated: true
type: note
---

In Rust haben die Schlüsselwörter `mut` und `&mut` verwandte, aber unterschiedliche Zwecke. Sie sind nicht direkt mit Javas Konzepten von tiefen/flachen Kopien oder C-Pointern gleichzusetzen – obwohl wir zur Veranschaulichung einige Analogien ziehen können. Ich werde dies Schritt für Schritt aufschlüsseln, die Unterschiede erklären und Ihre Fragen zur Wertübergabe vs. Referenzübergabe, Veränderbarkeit und wie Änderungen die Originaldaten beeinflussen, beantworten. Ich werde Beispiele auf Basis Ihres bereitgestellten Codes zur Veranschaulichung verwenden.

### 1. **`mut` in Variablendeklarationen verstehen**
- Wenn Sie eine Variable mit `let mut` deklarieren, machen Sie die *Bindung* (den Variablennamen) veränderbar. Das bedeutet, Sie können der Variable neu zuweisen oder ihren Inhalt direkt modifizieren, aber nur innerhalb des Gültigkeitsbereichs, in dem sie deklariert ist.
- Beispiel aus Ihrem Code:
  ```rust
  let mut arr = [3, 6, 8, 10, 1, 2, 1];
  ```
  Hier ist `arr` veränderbar, Sie könnten also `arr[0] = 99;` machen oder später sogar `arr = [1, 2, 3];` neu zuweisen. Ohne `mut` würde Rust sich beschweren, wenn Sie versuchen, eine unveränderliche Variable zu modifizieren (Rust standardisiert aus Sicherheitsgründen auf Unveränderlichkeit).
- Dieses `mut` betrifft die Variable selbst, nicht wie sie an Funktionen übergeben wird. Es impliziert kein Kopieren oder Referenzieren – es ist lediglich die Erlaubnis, die Variable direkt zu ändern.

### 2. **`&mut` in Funktionsparametern und Referenzen verstehen**
- `&mut` erzeugt eine *veränderbare Referenz* (auch mutable Borrow genannt). Dies ist wie ein Pointer in C, der das Lesen *und* Schreiben der gezeigten Daten erlaubt, aber mit Rusts strengem Borrow-Checker, der Sicherheit gewährleistet (keine Data Races, keine hängenden Zeiger).
- In Ihrem Code:
  ```rust
  fn quick_sort(arr: &mut [i32]) { ... }
  ```
  - Der Parameter `arr` ist eine veränderbare Referenz auf einen Slice von `i32`s (`&mut [i32]`). Slices in Rust sind Ansichten in Arrays oder Vektoren (wie ein Zeiger + Länge), und sie werden fast immer als Referenzen übergeben, da Slices "unsized"-Typen sind (ihre Größe ist zur Kompilierzeit nicht bekannt).
  - Wenn Sie `quick_sort(&mut arr);` aufrufen, übergeben Sie eine veränderbare Referenz auf das originale `arr`. Dies erlaubt der Funktion, die Elemente des originalen Arrays durch die Referenz zu modifizieren (z.B. via Swaps in `partition`).
  - Innerhalb der Funktion beeinflussen Operationen wie `arr.swap(i, j);` direkt die Originaldaten, weil `arr` eine Referenz ist, die darauf zeigt.
- Ohne das `&` könnten Sie einen Slice wie `[i32]` nicht direkt auf diese Weise als Parameter übergeben – Rust benötigt Referenzen für unsized-Typen. Aber allgemein ermöglicht `&mut` eine Referenzübergabe mit Schreibrechten.

### 3. **Wertübergabe vs. Referenzübergabe in Rust**
- Rust verwendet *Ownership* als sein Kernmodell, was sich von Java (das größtenteils referenzbasiert mit Garbage Collection ist) oder C (manuelle Zeiger) unterscheidet.
  - **Wertübergabe (Ownership-Transfer)**: Wenn Sie einen Wert ohne `&` übergeben (z.B. `fn foo(x: i32)` oder `fn bar(mut v: Vec<i32>)`), geht das Ownership der Daten an die Funktion über. Die Funktion kann sie lokal modifizieren, aber Änderungen beeinflussen das Original des Aufrufers nicht (weil der Aufrufer es nicht mehr besitzt). Wenn der Typ `Copy` implementiert (wie Primitive z.B. `i32`), wird er automatisch kopiert anstatt verschoben – kein Deep Copy, es sei denn, Sie klonen explizit.
    - Beispiel:
      ```rust
      fn foo(mut x: i32) {
          x += 1;  // Modifiziert lokales x, aber das Original des Aufrufers ist unverändert (oder verschoben/kopiert).
          println!("Inside: {}", x);
      }

      let y = 5;
      foo(y);  // Übergibt als Wert (Kopie, da i32 Copy ist).
      println!("After: {}", y);  // Immer noch 5.
      ```
    - Dies ist wie "Wertübergabe" in anderen Sprachen: Primitive werden kopiert, größere Typen (wie Arrays/Vektoren) werden verschoben (effizient, keine Kopie, es sei denn geklont).
  - **Referenzübergabe (Borrowing)**: Die Verwendung von `&` (unveränderbare Referenz) oder `&mut` (veränderbare Referenz) "borrowed" die Daten, ohne das Ownership zu transferieren. Die Funktion erhält eine temporäre Ansicht (wie ein Zeiger), und der originale Besitzer behält die Kontrolle.
    - `&`: Schreibgeschützter Borrow. Kann das Original nicht modifizieren.
    - `&mut`: Lese-Schreib-Borrow. *Kann* das Original modifizieren, wie Referenzübergabe in C++ oder ein veränderbarer Zeiger in C.
    - Beispiel:
      ```rust
      fn bar(x: &mut i32) {
          *x += 1;  // Dereferenziere und modifiziere das Original.
      }

      let mut y = 5;
      bar(&mut y);  // Übergibt veränderbare Referenz.
      println!("After: {}", y);  // Jetzt 6, Original wurde geändert.
      ```
    - In Ihrem Quicksort-Code handelt es sich um Referenzübergabe mit `&mut`, daher ändern Swaps das originale Array. Wenn es nur `& [i32]` wäre, könnten Sie es nicht modifizieren (unveränderlicher Borrow).

  - Zu Ihrem Punkt: Ja, `&mut` erlaubt das Ändern der Originalwerte (Referenzübergabe mit Mutation), während die Übergabe ohne `&` (Wertübergabe) die Daten entweder kopiert/verschiebt, sodass Modifikationen lokal sind und das Original nicht beeinflussen. Aber:
    - Nicht alle Typen kopieren automatisch – nur die, die `Copy` implementieren (z.B. `i32`, nicht Arrays oder Vektoren). Für Non-`Copy`-Typen wie Ihr Array würde die Übergabe als Wert das Ownership *verschieben*, und Sie müssten es zurückgeben, um es dem Aufrufer "zurückzugeben".
    - Rust vermeidet unnötige Kopien für Effizienz. Ihr Array wird nicht kopiert, wenn es als `&mut [i32]` übergeben wird – es ist nur eine Referenz (flach, wie ein Zeiger).

### 4. **Vergleich mit Java und C**
- **Java**: Alles Nicht-Primitive wird als Referenz übergeben (flach – Objekte werden geteilt, aber das Neuzuweisen des Parameters beeinflusst den Aufrufer nicht). Primitive werden als Wert übergeben (Kopie). Kein direktes Äquivalent zu `mut` oder `&mut`; Veränderbarkeit wird durch Klassendesign gesteuert (z.B. finale Felder). Java hat nicht Rusts Ownership, daher ist es anfälliger für Probleme mit gemeinsam genutztem veränderbarem Zustand. Tiefe Kopien erfordern manuelles Cloning.
- **C**: `&mut` ist wie das Übergeben eines Zeigers (`int*`), bei dem Sie dereferenzieren und modifizieren können (`*ptr = 10;`). Einfaches `mut` (in Deklarationen) ist wie nicht-konstante Variablen. Aber C hat keinen Borrow-Checker, daher verwalten Sie Lebenszeiten manuell (fehleranfällig). Wertübergabe in C kopiert die Daten (flach für Structs, es sei denn, Sie kopieren tief).
- Wichtiger Unterschied: Rust erzwingt "eine veränderbare Referenz gleichzeitig" (oder mehrere unveränderbare), was Bugs verhindert. Keine Null-Zeiger, keine wilden Zeiger.

### 5. **Warum manchmal `mut` und manchmal `&mut` in Ihrem Code?**
- `mut` allein: Wird für lokale Variablen verwendet, die änderbar sein müssen, wie `let mut arr` (damit Sie später `&mut arr` übergeben oder sie direkt modifizieren können).
- `&mut`: Wird in Parametern verwendet, wenn die Funktion die Daten des Aufrufers borrowen und modifizieren muss, ohne das Ownership zu übernehmen. In `quick_sort` und `partition` erlaubt `&mut [i32]` ihnen, das Array In-Place zu sortieren, ohne es zu verschieben/zu kopieren.
- Wenn Sie `fn quick_sort(mut arr: [i32])` versuchen würden, würde es nicht kompilieren – Slices können nicht so als Wert übergeben werden. Sie bräuchten ein Array fester Größe (z.B. `[i32; 7]`) und es würde das Ownership verschieben.
- In `partition` verwendet die Schleife intern `mut i` – das ist eine lokale veränderbare Variable, unabhängig von der Übergabe.

### 6. **Ändert es die Originalwerte?**
- Ja für `&mut`: Änderungen wirken sich auf das Original aus (Referenzübergabe).
- Nein für Wertübergabe (ohne `&`): Nur lokale Änderungen (es sei denn, Sie geben den modifizierten Wert zurück).
- In Ihrem `quick_sort_interact()` wird `println!("After: {:?}", arr);` das sortierte Array anzeigen, weil `&mut` verwendet wurde.

Wenn Sie Ihren Code ausführen, sollte er ausgeben:
```
Before: [3, 6, 8, 10, 1, 2, 1]
After: [1, 1, 2, 3, 6, 8, 10]
```
(Das `mod simple;` und `simple::run_simple();` scheinen unabhängig zu sein – vielleicht ein Platzhalter? Wenn es dort einen Fehler gibt, könnte es sein, dass `simple` nicht definiert ist.)

Wenn dies nicht klärt oder Sie einen spezifischen Teil des Codes zum Anpassen/Testen haben, lassen Sie es mich wissen!