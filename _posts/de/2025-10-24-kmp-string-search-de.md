---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: KMP-Algorithmus für effiziente Zeichenkettensuche
translated: true
type: note
---

### Den Knuth-Morris-Pratt (KMP)-Algorithmus verstehen

Deine Intuition ist absolut richtig: Beim KMP-Algorithmus geht es darum, **partielle Übereinstimmungen nicht zu verschwenden**. Wenn du nach einem Muster (wie "abc") in einem längeren Text (wie "ababcabc") suchst, beginnt der naive Ansatz bei jedem Nichtübereinstimmung wieder von vorne, was ineffizient ist. KMP "merkt" sich clever, wie viel des Musters bereits übereingestimmt hat, und springt vorwärts, wodurch redundante Vergleiche vermieden werden. Das macht ihn superschnell – lineare Zeit, O(n + m), wobei n die Textlänge und m die Musterlänge ist.

Ich werde es Schritt für Schritt mit einem einfachen Beispiel erklären. Wir suchen nach dem Muster `P = "abab"` im Text `T = "ababababc"`. (Es erscheint an den Positionen 0, 2 und 4.)

#### Schritt 1: Das Problem und der naive Ansatz
- **Ziel**: Finde alle Startpositionen, an denen `P` vollständig in `T` übereinstimmt.
- **Naive Methode**: Bewege `P` über `T`, vergleiche Zeichen für Zeichen. Wenn eine Nichtübereinstimmung an Position i in `P` auftritt, verschiebe `P` um 1 und versuche es erneut vom Anfang von `P` aus.
  - Für unser Beispiel:
    - Start bei T[0]: "a"=="a" (Übereinstimmung), "b"=="b" (Übereinstimmung), "a"=="a" (Übereinstimmung), "b"=="b" (Übereinstimmung) → Gefunden bei 0.
    - Verschiebe zu T[1]: "b"=="a"? Nein → Starte `P` vom Anfang. Verschwendung!
    - T[2]: "a"=="a", "b"=="b", "a"=="a", "b"=="b" → Gefunden bei 2.
    - T[3]: "a"=="a", "b"=="b", "a"=="a", "b"=="a"? Nein → Starte neu.
    - Und so weiter. Viel Backtracking zu Zeichen 0 von `P`.

Dies kann im schlimmsten Fall O(n*m) sein (z.B. die Suche nach "aaa...ab" in "aaaaa...a").

#### Schritt 2: Die Kernidee von KMP – Die Präfixtabelle (oder "Failure Function")
KMP berechnet im Voraus eine Tabelle `π` (pi) für das Muster `P`. Diese Tabelle sagt dir für jede Position i in `P`, **das längste echte Präfix von `P[0..i]`, das auch ein Suffix ist**. Mit anderen Worten: "Wenn wir hier eine Nichtübereinstimmung haben, wie viel der partiellen Übereinstimmung können wir wiederverwenden, indem wir zu diesem überlappenden Präfix springen?"

- **Echtes Präfix/Suffix**: Ein Präfix/Suffix, das nicht die gesamte Zeichenkette ist (z.B. für "aba" stimmt Präfix "a" mit Suffix "a" überein).
- Warum? Es erlaubt dir, das Muster bei einer Nichtübereinstimmung um mehr als 1 zu verschieben und die Überlappung wiederzuverwenden, anstatt neu zu starten.

Für `P = "abab"`:
- Baue `π` Schritt für Schritt auf (wir werden dies bald codieren).

| Position i | P[0..i] | Längstes echtes Präfix = Suffix | π[i] |
|------------|---------|--------------------------------|------|
| 0          | "a"     | Keines (einzelnes Zeichen)     | 0    |
| 1          | "ab"    | Keines                         | 0    |
| 2          | "aba"   | "a" (Präfix "a" == Suffix "a") | 1    |
| 3          | "abab"  | "ab" (Präfix "ab" == Suffix "ab") | 2  |

- π[2] = 1 bedeutet: Wenn du "aba" gematcht hast, aber das nächste Zeichen nicht übereinstimmt, tue so, als hättest du bisher das Präfix "a" (Länge 1) gematcht.
- π[3] = 2 bedeutet: Für das volle "abab", Überlappung von "ab".

#### Schritt 3: Aufbau der Präfixtabelle (π)
Dies geschieht in O(m) Zeit. Es ist, als ob man `P` gegen sich selbst durchsucht, mit einer ähnlichen Logik.

Pseudocode:
```
def compute_prefix_function(P):
    m = len(P)
    pi = [0] * m
    k = 0  # Länge des aktuellen Präfix-Suffix-Matches
    for i in range(1, m):
        while k > 0 and P[k] != P[i]:
            k = pi[k-1]  # Springe zum vorherigen Overlap (Wiederverwenden!)
        if P[k] == P[i]:
            k += 1
        pi[i] = k
    return pi
```

- Starte mit π[0] = 0.
- Für jedes i=1 bis m-1:
  - Versuche, die aktuelle Match-Länge k zu erweitern.
  - Bei Nichtübereinstimmung, falle zurück auf π[k-1] (verschwende nicht – verwende vorherigen Overlap wieder).
  - Bei Übereinstimmung, k++.

Für "abab":
- i=1: P[0]='a' != P[1]='b' → k=0, π[1]=0.
- i=2: P[0]='a' == P[2]='a' → k=1, π[2]=1.
- i=3: P[1]='b' == P[3]='b' → k=2, π[3]=2.

#### Schritt 4: Suche mit der Präfixtabelle
Jetzt durchsuche `T` mit `P` und `π`:
- Behalte eine Variable `q` = aktueller Zustand (Länge des bisher gematchten Präfix).
- Für jedes Zeichen in `T`:
  - Während Nichtübereinstimmung und q>0, setze q = π[q-1] (springe clever zurück).
  - Bei Übereinstimmung, q++.
  - Wenn q == m, gefunden! Dann q = π[q-1], um nach Overlaps weiterzusuchen.

Pseudocode:
```
def kmp_search(T, P):
    n, m = len(T), len(P)
    if m == 0: return []
    pi = compute_prefix_function(P)
    q = 0
    matches = []
    for i in range(n):
        while q > 0 and P[q] != T[i]:
            q = pi[q-1]
        if P[q] == T[i]:
            q += 1
        if q == m:
            matches.append(i - m + 1)  # Startposition
            q = pi[q-1]  # Overlap für nächste Suche
    return matches
```

Für `T = "ababababc"`, `P = "abab"`:
- i=0: 'a'=='a' → q=1
- i=1: 'b'=='b' → q=2
- i=2: 'a'=='a' → q=3
- i=3: 'b'=='b' → q=4 == m → Match bei 0, q=π[3]=2
- i=4: Jetzt q=2, T[4]='a' == P[2]='a' → q=3
- i=5: 'b'=='b' → q=4 == m → Match bei 2, q=2
- i=6: q=2, 'a'=='a' → q=3
- i=7: q=3, 'b' == P[3]='b' → q=4 == m → Match bei 4, q=2
- i=8: 'c' != P[q=2]='a'? Während q>0: q = π[1]=0. Dann 'c' != P[0]='a' → q=0.

Ergebnis: Matches bei 0, 2, 4.

Siehst du? Bei Nichtübereinstimmungen springt es zu q=π[q-1] anstatt zu q=0.

#### Warum es sich magisch anfühlt
- Kein Backtracking in `T` – du gehst nur vorwärts.
- Die "while"-Schleife für Nichtübereinstimmungen läuft amortisiert O(1) Mal insgesamt, weil jeder Sprung q verringert und q höchstens n Mal zunimmt.

#### Probiere es selbst: Einfacher Python-Code
```python
def compute_prefix_function(P):
    m = len(P)
    pi = [0] * m
    k = 0
    for i in range(1, m):
        while k > 0 and P[k] != P[i]:
            k = pi[k - 1]
        if P[k] == P[i]:
            k += 1
        pi[i] = k
    return pi

def kmp_search(T, P):
    n, m = len(T), len(P)
    if m == 0: return []
    pi = compute_prefix_function(P)
    q = 0
    matches = []
    for i in range(n):
        while q > 0 and P[q] != T[i]:
            q = pi[q - 1]
        if P[q] == T[i]:
            q += 1
        if q == m:
            matches.append(i - m + 1)
            q = pi[q - 1]
    return matches

# Test
T = "ababababc"
P = "abab"
print(kmp_search(T, P))  # Ausgabe: [0, 2, 4]
```

Führe dies aus – ändere P/T, um die Sprünge in Aktion zu sehen (füge prints für q hinzu).

#### Häufige Fallstricke & Tipps
- π[0] ist immer 0.
- Für Muster ohne Selbstüberlappung (z.B. "abc") ist π nur 0en – fällt auf naiven Ansatz zurück.
- Großartig für DNA-Sequenzen oder Code-Autovervollständigung.
- Wenn es immer noch unklar ist, stelle dir π als "Zustandsmaschine" vor: Jeder Zustand ist die gematchte Länge, Übergänge bei Match/Mismatch.

Jetzt sollte es klick machen – es ist nur cleveres Überspringen via vorberechneter Overlaps. Wenn du ein bestimmtes Beispiel hast, bei dem du hängen bleibst, teile es mir mit!

[GeeksforGeeks: KMP Algorithm](https://www.geeksforgeeks.org/dsa/kmp-algorithm-for-pattern-searching/)  
[Wikipedia: Knuth–Morris–Pratt Algorithm](https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm)