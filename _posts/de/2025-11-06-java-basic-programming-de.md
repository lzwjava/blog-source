---
audio: false
generated: true
image: false
lang: de
layout: post
model: openai/gpt-5
title: Java Grundlagen Programmierhandbuch
translated: true
type: note
---

Hier ist ein gezielter Leitfaden für **Teil II: Grundlagen der Programmierung** von *08553 Einführung in die Programmierung — Java*, zugeschnitten auf die **National Higher Education Self-study Examination (自考)**. Dieser Abschnitt trainiert Sie darin, kleine, korrekte Java-Programme zu schreiben und zu verstehen, wie Java mit Daten und Ausdrücken umgeht.

---

## 1. Eingabe von der Konsole lesen

### 1.1 Verwendung von `Scanner`

Java liest Eingaben mit der `Scanner`-Klasse aus `java.util`.

```java
import java.util.Scanner;

public class InputExample {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Geben Sie Ihren Namen ein: ");
        String name = sc.nextLine();
        System.out.print("Geben Sie Ihr Alter ein: ");
        int age = sc.nextInt();
        System.out.println("Hallo " + name + ", Sie sind " + age + " Jahre alt.");
        sc.close();
    }
}
```

**Wichtige Punkte:**

* Immer `import java.util.Scanner;` verwenden.
* Verwenden Sie `nextInt()`, `nextDouble()`, `nextLine()` entsprechend dem Datentyp.
* Schließen Sie den `Scanner`, um Ressourcen freizugeben.
* Vorsicht: `nextLine()` liest den Rest einer Zeile, daher kann das Vermischen mit `nextInt()` zu übersprungenen Eingaben führen.

---

## 2. Bezeichner, Variablen, Ausdrücke, Zuweisungen und Konstanten

### 2.1 Bezeichner

Namen, die Sie Variablen, Methoden oder Klassen geben.
**Regeln:**

* Müssen mit einem Buchstaben, `_` oder `$` beginnen.
* Dürfen nicht mit einer Zahl beginnen.
* Groß- und Kleinschreibung wird unterschieden (`score` ≠ `Score`).
* Dürfen kein Schlüsselwort sein (`int`, `class`, `if`, etc.).

**Beispiele:**
`studentName`, `_total`, `$price`

### 2.2 Variablen

Eine Variable hält Daten eines bestimmten **Typs**.
Deklarationsbeispiele:

```java
int age = 20;
double price = 12.5;
char grade = 'A';
boolean passed = true;
```

### 2.3 Zuweisungsanweisungen

Weist einen Wert mit `=` zu (rechts → links):

```java
x = 5;
y = x + 2;
```

### 2.4 Konstanten

Werden mit `final` deklariert und können später nicht geändert werden:

```java
final double PI = 3.14159;
```

Verwenden Sie Großbuchstaben für Konstantennamen.

---

## 3. Numerische Datentypen und Operationen

### 3.1 Häufige numerische Typen

* `byte` (8-Bit-Ganzzahl)
* `short` (16-Bit)
* `int` (32-Bit, am gebräuchlichsten)
* `long` (64-Bit)
* `float` (32-Bit-Dezimalzahl)
* `double` (64-Bit-Dezimalzahl, genauer)

**Beispiel:**

```java
int count = 5;
double price = 19.99;
```

### 3.2 Grundlegende arithmetische Operatoren

`+`, `-`, `*`, `/`, `%`

Beispiele:

```java
int a = 10, b = 3;
System.out.println(a / b);  // 3 (Ganzzahldivision)
System.out.println(a % b);  // 1
System.out.println((double)a / b); // 3.3333 (Typkonvertierung)
```

---

## 4. Typkonvertierung (Casting)

### 4.1 Automatische Konvertierung (Widening)

Kleiner → großer Typ automatisch:
`int` → `long` → `float` → `double`

Beispiel:

```java
int i = 10;
double d = i;  // automatische Konvertierung
```

### 4.2 Manuelle Konvertierung (Casting)

Explizites Konvertieren eines größeren → kleineren Typs:

```java
double d = 9.7;
int i = (int) d; // i = 9 (Nachkommastellen gehen verloren)
```

Vorsicht bei **Genauigkeitsverlust**.

---

## 5. Ausdrucksauswertung und Operatorrangfolge

### 5.1 Reihenfolge der Operationen

Java befolgt eine definierte Reihenfolge:

1. Klammern `( )`
2. Unär `+`, `-`, `++`, `--`
3. Multiplikation, Division, Modulus `* / %`
4. Addition und Subtraktion `+ -`
5. Zuweisung `=`

Beispiel:

```java
int x = 2 + 3 * 4;   // 14, nicht 20
int y = (2 + 3) * 4; // 20
```

### 5.2 Gemischte Ausdrücke

Wenn ein Operand `double` ist, wird das Ergebnis zu `double`:

```java
double result = 5 / 2;     // 2.0 (zuerst Ganzzahldivision)
double result2 = 5.0 / 2;  // 2.5 (Gleitkommadivision)
```

---

## 6. Kombinierte Zuweisung und Inkrement/Dekrement

### 6.1 Kombinierte Zuweisung

Kurzschreibweise:

```java
x += 3;  // gleichbedeutend mit x = x + 3
y *= 2;  // gleichbedeutend mit y = y * 2
```

### 6.2 Inkrement und Dekrement

`++` erhöht um 1, `--` verringert um 1.
Zwei Formen:

```java
int a = 5;
System.out.println(a++); // gibt 5 aus, dann a = 6
System.out.println(++a); // a = 7, dann gibt 7 aus
```

**Merke:**

* Postfix (`a++`) → zuerst verwenden, dann erhöhen
* Prefix (`++a`) → zuerst erhöhen, dann verwenden

---

## 7. Häufige Fehler, die zu vermeiden sind

* Verwendung von `=` anstelle von `==` in Vergleichen.
* Ganzzahldivision, wenn Dezimalzahlen erwartet werden.
* Vergessen, eine Variable vor der Verwendung zu initialisieren.
* Datenverlust bei Typkonvertierung (z.B. `(int) 3.9` → 3).

---

## 8. Typische Prüfungsfragen

**Beispiel 1:**

> Was ist die Ausgabe des folgenden Codes?
>
> ```java
> int x = 5, y = 2;
> double z = x / y;
> System.out.println(z);
> ```

**Antwort:** `2.0` (zuerst Ganzzahldivision, dann Zuweisung)

**Beispiel 2:**

> Welcher Operator hat die höchste Priorität?
> A. `+`
> B. `*`
> C. `=`
> D. `++`
> **Antwort:** D

**Beispiel 3:**

> Was ist die Ausgabe dieses Codes?
>
> ```java
> int a = 3;
> int b = ++a + a++;
> System.out.println(b);
> ```

**Erklärung:**
`++a` macht `a = 4`, addiert `4`, dann verwendet `a++` den Wert `4` und erhöht anschließend auf `5`.
Also `b = 8`.

---

Möchten Sie, dass ich mit **Teil III: Steuerstrukturen (Auswahl- und Schleifenanweisungen)** fortfahre? Dieser behandelt `if`, `switch`, `for`, `while` und bildet den Kern der prozeduralen Logik in der Java-Prüfung.