---
audio: false
generated: true
lang: de
layout: post
title: Implementierung von Zig Quick Sort
translated: true
type: note
---

Hier ist die entsprechende Quick-Sort-Implementierung in Zig.

```zig
const std = @import("std");

// Quick-Sort-Funktion
fn quickSort(arr: []i32) void {
    if (arr.len <= 1) {
        return;
    }

    const pivot_index = partition(arr);

    // Teile das Array in linke und rechte Partitionen auf
    // Hinweis: Die Slice-Aufteilung in Zig unterscheidet sich leicht von der in Rust
    // Wir müssen das Pivot-Element sorgfältig behandeln
    var left_slice = arr[0..pivot_index];
    var right_slice = arr[pivot_index + 1 .. arr.len]; // Schließe das Pivot aus dem rechten Slice aus

    quickSort(left_slice);
    quickSort(right_slice);
}

// Partition-Funktion
fn partition(arr: []i32) usize {
    const len = arr.len;
    // Der Einfachheit halber verwenden wir das letzte Element als Pivot, ähnlich wie im Rust-Beispiel.
    // In einem Produktions-Quicksort könnte man für eine bessere durchschnittliche Leistung ein zufälliges Pivot oder Median-of-Three wählen.
    const pivot = arr[len - 1];
    var i: usize = 0; // Index des kleineren Elements

    for (0..(len - 1)) |j| {
        if (arr[j] <= pivot) {
            std.mem.swap(i32, &arr[i], &arr[j]);
            i += 1;
        }
    }

    // Platziere das Pivot an seiner korrekten Position
    std.mem.swap(i32, &arr[i], &arr[len - 1]);

    return i;
}

pub fn main() !void {
    var arr = [_]i32{ 3, 6, 8, 10, 1, 2, 1 };

    // Erstelle einen veränderlichen Slice aus dem Array für die Quicksort-Funktion
    var slice: []i32 = &arr;

    std.debug.print("Vorher: {any}\n", .{slice});

    quickSort(slice);

    std.debug.print("Nachher: {any}\n", .{slice});
}

```

### Erklärung der Änderungen und Zig-Konzepte:

1.  **`const std = @import("std");`**: Diese Zeile importiert die Zig-Standardbibliothek, die nützliche Utilities wie `std.debug.print` für die Ausgabe und `std.mem.swap` zum Vertauschen von Elementen bereitstellt.
2.  **`fn quickSort(arr: []i32) void`**:
      * `fn` deklariert eine Funktion.
      * `arr: []i32` deklariert `arr` als einen Slice von `i32` (32-Bit-Ganzzahlen). In Zig bezeichnet `[]T` einen veränderlichen Slice des Typs `T`. Es gibt kein separates `&mut` wie in Rust; Veränderbarkeit ergibt sich daraus, ob die Variable, die den Slice hält, veränderlich ist.
      * `void` zeigt an, dass die Funktion keinen Wert zurückgibt.
3.  **`if (arr.len <= 1)`**: Bedingte Anweisungen verwenden Klammern um die Bedingung.
4.  **`const pivot_index = partition(arr);`**: `const` wird für unveränderliche Variablen verwendet.
5.  **Slice-Aufteilung in Zig**:
      * `var left_slice = arr[0..pivot_index];`
      * `var right_slice = arr[pivot_index + 1 .. arr.len];`
      * Anders als Rusts `split_at_mut`, das zwei veränderliche Slices erstellt, die sich nicht überlappen, erzeugt Zigs Slicing `arr[start..end]` neue Slices (Ansichten) in das ursprüngliche Array.
      * Entscheidend ist, dass wir in den rekursiven Aufrufen das Pivot *ausschließen* müssen, sowohl aus dem linken als auch aus dem rechten Sub-Array, da das Pivot nach `partition` bereits in seiner endgültigen sortierten Position ist. Im Rust-Code erreicht `right[1..]` dies, indem effektiv das erste Element des `right`-Slices übersprungen wird, welches das Pivot ist. Wir replizieren dies, indem wir `pivot_index + 1` für den Start des `right_slice` verwenden.
6.  **`std.mem.swap(i32, &arr[i], &arr[j]);`**:
      * `std.mem.swap` wird zum Vertauschen von Elementen verwendet.
      * Das erste Argument (`i32`) ist der Typ der zu tauschenden Elemente.
      * Die nachfolgenden Argumente sind Zeiger auf die Speicherstellen, die getauscht werden sollen (`&arr[i]` und `&arr[j]`).
7.  **`for (0..(len - 1)) |j| { ... }`**: Dies ist eine `for`-Schleife, die von `0` bis (aber ausschließlich) `len - 1` iteriert. Die Schleifenvariable wird als `j` erfasst.
8.  **`pub fn main() !void { ... }`**:
      * `pub` macht die `main`-Funktion öffentlich zugänglich.
      * `!void` zeigt an, dass die Funktion einen Fehler zurückgeben kann, aber in diesem Fall behandeln wir keine explizit. Für einfache Programme ist `void` in Ordnung, aber `!void` wird in Zig oft gesehen, da es robuste Fehlerbehandlung fördert.
9.  **`var arr = [_]i32{ 3, 6, 8, 10, 1, 2, 1 };`**:
      * `[_]i32` deklariert ein Array fester Größe von `i32`. Der `_` weist den Compiler an, die Größe aus der Initialisierungsliste abzuleiten.
10. **`var slice: []i32 = &arr;`**: Wir erstellen einen veränderlichen Slice (`[]i32`) aus dem Array fester Größe `arr`, weil `quickSort` einen Slice erwartet.
11. **`std.debug.print("Vorher: {any}\n", .{slice});`**:
      * `std.debug.print` ist Zigs Äquivalent zu `println!` für Debugging-Ausgaben.
      * `{any}` ist ein Formatbezeichner, der Zig anweist, den Wert in einem menschenlesbaren, debug-freundlichen Format auszugeben.
      * `.{slice}` ist ein "Struct Literal" (anonymes Struct), das verwendet wird, um die Argumente an die Formatzeichenkette zu übergeben.

Um diesen Zig-Code zu kompilieren und auszuführen:

1.  Speichere ihn als `quick_sort.zig`.
2.  Öffne dein Terminal im selben Verzeichnis.
3.  Führe aus: `zig run quick_sort.zig`