---
audio: false
generated: true
lang: de
layout: post
title: Stream-API in Java
translated: true
type: note
---

Um `java.util.stream` in Java zu verwenden, können Sie die in Java 8 eingeführte Stream API nutzen, um Sammlungen von Daten auf funktionale und deklarative Weise zu verarbeiten. Streams ermöglichen es Ihnen, Operationen wie Filtern, Abbilden und Reduzieren auf Sequenzen von Elementen (wie Listen oder Arrays) effizient und prägnant durchzuführen. Im Folgenden werde ich erklären, wie Sie `java.util.stream` verwenden können, indem ich ein konkretes Beispiel durchgehe: das Finden des Durchschnitts aller geraden Zahlen größer als 10 aus einer Liste von Ganzzahlen. Dies demonstriert wichtige Stream-Operationen und Konzepte.

---

### **Überblick über `java.util.stream`**
Das Paket `java.util.stream` stellt die `Stream`-Schnittstelle und verwandte Klassen (wie `IntStream`, `DoubleStream` etc.) zur Datenverarbeitung bereit. Ein Stream ist eine Sequenz von Elementen, die Operationen unterstützt, die in einer Pipeline ausgeführt werden. Diese Operationen sind:
- **Intermediate Operations**: Transformieren oder filtern den Stream (z.B. `filter`, `map`) und geben einen neuen Stream zurück. Sie sind lazy und werden nur ausgeführt, wenn eine Terminaloperation aufgerufen wird.
- **Terminale Operationen**: Erzeugen ein Ergebnis oder einen Seiteneffekt (z.B. `average`, `collect`) und lösen die Verarbeitung der Daten durch die Pipeline aus.

Um Streams zu verwenden, gehen Sie typischerweise wie folgt vor:
1. Erstellen Sie einen Stream aus einer Datenquelle (z.B. einer Liste).
2. Wenden Sie intermediate Operations an, um die Daten zu transformieren oder zu filtern.
3. Verwenden Sie eine terminale Operation, um ein Ergebnis zu erzeugen.

---

### **Beispielproblem**
Lösen wir dieses Problem: Gegeben eine `List<Integer>`, berechne den Durchschnitt aller geraden Zahlen größer als 10. Falls keine solchen Zahlen existieren, gib 0.0 zurück. So kann man es mit `java.util.stream` machen.

#### **Schritt-für-Schritt-Lösung**
1. **Einen Stream erstellen**
   - Beginnen Sie mit einer `List<Integer>` (z.B. `List.of(1, 2, 12, 15, 20, 25, 30)`).
   - Verwenden Sie die Methode `stream()`, um einen `Stream<Integer>` zu erstellen:
     ```java
     list.stream()
     ```

2. **Den Stream filtern**
   - Verwenden Sie die Methode `filter`, um nur Zahlen zu behalten, die gerade und größer als 10 sind.
   - Die `filter`-Methode nimmt ein `Predicate` (eine Funktion, die einen booleschen Wert zurückgibt) als Lambda-Ausdruck entgegen:
     ```java
     .filter(number -> number % 2 == 0 && number > 10)
     ```
     - `number % 2 == 0` prüft, ob eine Zahl gerade ist.
     - `number > 10` stellt sicher, dass die Zahl größer als 10 ist.
     - Für die Beispiel-Liste `[1, 2, 12, 15, 20, 25, 30]` behält dies `[12, 20, 30]`.

3. **In einen `IntStream` umwandeln**
   - Da `average()` auf primitiven Streams wie `IntStream` verfügbar ist (nicht auf `Stream<Integer>`), wandeln Sie den `Stream<Integer>` mit `mapToInt` in einen `IntStream` um:
     ```java
     .mapToInt(i -> i)
     ```
     - `i -> i` entpackt jedes `Integer` zu einem `int`. Alternativ könnte man `Integer::intValue` verwenden.
     - Dies ergibt einen `IntStream` von `[12, 20, 30]`.

4. **Den Durchschnitt berechnen**
   - Verwenden Sie die Methode `average()` auf dem `IntStream`, die ein `OptionalDouble` zurückgibt (da der Stream leer sein könnte):
     ```java
     .average()
     ```
     - Für `[12, 20, 30]` berechnet dies `(12 + 20 + 30) / 3 = 20.666...`.
     - Wenn der Stream leer ist, wird ein leeres `OptionalDouble` zurückgegeben.

5. **Den leeren Fall behandeln**
   - Verwenden Sie `orElse(0.0)` auf dem `OptionalDouble`, um 0.0 zurückzugeben, falls keine Zahlen den Filter erfüllen:
     ```java
     .orElse(0.0)
     ```
     - Für `[12, 20, 30]` gibt dies `20.666...` zurück.
     - Für eine Liste wie `[1, 3, 5]` (keine geraden Zahlen > 10) gibt es `0.0` zurück.

#### **Vollständiger Code**
Hier ist die vollständige Lösung als Methode:
```java
import java.util.List;

public class Main {
    public static double averageOfEvenGreaterThanTen(List<Integer> list) {
        return list.stream()
                   .filter(number -> number % 2 == 0 && number > 10)
                   .mapToInt(i -> i)
                   .average()
                   .orElse(0.0);
    }

    public static void main(String[] args) {
        // Testfälle
        System.out.println(averageOfEvenGreaterThanTen(List.of(1, 2, 12, 15, 20, 25, 30)));  // ~20.666
        System.out.println(averageOfEvenGreaterThanTen(List.of(1, 3, 5)));                    // 0.0
        System.out.println(averageOfEvenGreaterThanTen(List.of(12)));                         // 12.0
        System.out.println(averageOfEvenGreaterThanTen(List.of()));                           // 0.0
        System.out.println(averageOfEvenGreaterThanTen(List.of(10, 8, 6)));                   // 0.0
        System.out.println(averageOfEvenGreaterThanTen(List.of(11, 13, 14, 16)));             // 15.0
    }
}
```

---

### **Wichtige Merkmale von `java.util.stream`, die demonstriert wurden**
- **Verkettung**: Operationen werden in einem flüssigen Stil verkettet (z.B. `.filter().mapToInt().average()`).
- **Laziness**: Intermediate Operations (wie `filter` und `mapToInt`) werden nur ausgeführt, wenn die terminale Operation (`average`) aufgerufen wird.
- **Primitive Streams**: `IntStream` bietet Methoden wie `average()`, die für numerische Operationen zugeschnitten sind und Boxing-Overhead vermeiden.
- **Optional Handling**: `OptionalDouble` behandelt Fälle, in denen kein Ergebnis existiert, wobei `orElse` einen Standardwert bereitstellt.

---

### **Alternativer Ansatz**
Man könnte auch die `Collectors`-Klasse verwenden:
```java
import java.util.stream.Collectors;

double average = list.stream()
                     .filter(number -> number % 2 == 0 && number > 10)
                     .collect(Collectors.averagingInt(i -> i));
```
- Dies gibt direkt ein `Double` zurück und gibt `0.0` für einen leeren Stream zurück. Jedoch ist `mapToInt().average()` in diesem einfachen Fall direkter und entspricht der Verwendung primitiver Streams.

---

### **Wann man Streams verwenden sollte**
- Verwenden Sie `java.util.stream` für prägnanten, lesbaren Code bei der Verarbeitung von Sammlungen.
- Für große Datensätze ziehen Sie `parallelStream()` anstelle von `stream()` in Betracht, um Parallelität zu nutzen, obwohl dies für kleine Listen aufgrund des Overheads übertrieben ist.

---

Dieses Beispiel zeigt, wie Sie `java.util.stream` verwenden können, um ein praktisches Problem zu lösen. Sie können diese Schritte – Erstellen eines Streams, Filtern, Abbilden und Reduzieren – an andere Szenarien anpassen, wie benötigt!