---
audio: false
generated: true
lang: de
layout: post
title: Codeforces 2108F
translated: true
type: note
---

Lassen Sie uns eintauchen, warum der bereitgestellte Java-Code das "Fallen Towers"-Problem löst. Das Problem beinhaltet ein Array von \\( n \\) Türmen, jeder mit einer Höhe \\( a_i \geq 0 \\). Sie können den Turm an Position \\( i \\) umwerfen, was die Höhen der nächsten \\( a_i \\) Türme um 1 erhöht (oder weniger, falls nicht genügend Türme übrig sind), und setzt dann \\( a_i \\) auf 0. Das Ziel ist es, alle \\( n \\) Türme genau einmal in beliebiger Reihenfolge umzuwerfen und sicherzustellen, dass das finale Array nicht fallend ist (d.h., für jedes \\( i < j \\) ist die Höhe an Position \\( i \\) höchstens so groß wie die Höhe an Position \\( j \\)). Die Ausgabe ist der maximale MEX des finalen Arrays, wobei der MEX die kleinste nicht-negative ganze Zahl ist, die nicht im Array vorkommt.

---

### Problem-Analyse

1.  **Operationsdefinition**:
    - Umwerfen des Turms \\( i \\) mit Höhe \\( a_i \\):
      - Erhöht die Höhen der Türme an den Positionen \\( i+1, i+2, \dots, i+a_i \\) um 1 (falls sie existieren).
      - Setzt \\( a_i = 0 \\).
    - Jeder Turm muss genau einmal, in beliebiger Reihenfolge, umgeworfen werden.
    - Wenn \\( a_i = 0 \\), hat das Umwerfen von Turm \\( i \\) keine Auswirkung auf andere Türme.

2.  **Nicht fallendes finales Array**:
    - Nach allen Operationen muss das finale Array \\( b_1, b_2, \dots, b_n \\) die Bedingung \\( b_i \leq b_{i+1} \\) für alle \\( i < n \\) erfüllen.

3.  **MEX**:
    - Der MEX des finalen Arrays ist die kleinste nicht-negative ganze Zahl \\( m \\), die nicht in \\( \{b_1, b_2, \dots, b_n\} \\) vorkommt.
    - Da das Array nicht fallend ist, wenn das Array die Werte \\( 0, 1, 2, \dots, k-1 \\) (möglicherweise mit Wiederholungen) enthält, aber nicht \\( k \\), dann ist der MEX \\( k \\).
    - Das Ziel ist es, diesen MEX zu maximieren.

4.  **Interpretation des MEX**:
    - Damit der MEX \\( m \\) ist, muss das finale Array alle ganzen Zahlen von 0 bis \\( m-1 \\) mindestens einmal enthalten, und \\( m \\) darf nicht vorkommen.
    - Da das Array nicht fallend ist, impliziert das Erreichen eines MEX von \\( m \\), dass das finale Array Werte wie \\( 0, 0, \dots, 1, 1, \dots, m-1, m-1 \\) hat, wobei jede ganze Zahl von 0 bis \\( m-1 \\) mindestens einmal vorkommt und kein Wert \\( m \\) oder höher vorhanden ist.

5.  **Schlüsseleinsicht**:
    - Der MEX \\( m \\) entspricht dem Vorhandensein von mindestens einer Position mit jedem Wert von 0 bis \\( m-1 \\).
    - Äquivalent dazu benötigen wir für einen MEX von \\( m \\) mindestens \\( m \\) Positionen im finalen Array, sodass Position \\( i \\) einen Wert von mindestens \\( i - (n - m) \\) hat, weil:
      - Die letzten \\( m \\) Positionen (von Index \\( n-m+1 \\) bis \\( n \\)) die Werte 0 bis \\( m-1 \\) abdecken müssen.
      - Position \\( n-m+1 \\) sollte mindestens den Wert 0 haben, Position \\( n-m+2 \\) mindestens 1, ..., Position \\( n \\) mindestens \\( m-1 \\).
    - Dies übersetzt sich in die Anforderung, dass die finale Höhe an Position \\( i \\) mindestens \\( \max(0, m - (n - i + 1)) = \max(0, m - n + i) \\) betragen muss.

---

### Lösungsansatz

Der Code verwendet eine binäre Suche, um den maximal möglichen MEX \\( m \\) zu finden. Für jeden Kandidaten \\( m \\) prüft er, ob es möglich ist, ein finales nicht fallendes Array zu erreichen, in dem jede Position \\( i \\) eine Höhe von mindestens \\( \max(0, m - n + i) \\) hat. Dies stellt sicher, dass die letzten \\( m \\) Positionen die Werte 0 bis \\( m-1 \\) abdecken können, was den MEX mindestens \\( m \\) macht.

#### Binäre Suche
- **Bereich**: Der MEX \\( m \\) ist mindestens 0 (Fall eines leeren Arrays) und höchstens \\( n \\) (da wir mindestens \\( m \\) Positionen benötigen, um die Werte 0 bis \\( m-1 \\) zu haben). Daher wird nach \\( m \\) in \\( [0, n] \\) gesucht.
- **Prüffunktion**: Für ein gegebenes \\( m \\) bestimmen, ob es eine Reihenfolge gibt, um die Türme umzuwerfen, sodass das finale Array erfüllt:
  - \\( b_i \geq \max(0, m - n + i) \\) für alle \\( i \\).
  - Das Array ist nicht fallend.

#### Prüffunktion
Die Prüffunktion simuliert mithilfe eines Differenz-Arrays, ob es möglich ist, die erforderlichen Höhen zu erreichen, unter der Annahme, dass die Türme in beliebiger Reihenfolge umgeworfen werden können.

1.  **Erforderliche Höhen**:
    - Für MEX \\( m \\) benötigt Position \\( i \\) eine finale Höhe \\( b_i \geq \text{need}_i \\), wobei:
      \\[
      \text{need}_i = \max(0, m - n + i)
      \\]
    - Dies stellt sicher, dass die Positionen \\( n-m+1 \\) bis \\( n \\) mindestens die Höhen 0, 1, ..., \\( m-1 \\) haben.

2.  **Differenz-Array**:
    - Der Code verwendet ein Differenz-Array \\( d \\), um den kumulativen Effekt der Operationen zu verfolgen.
    - Initialisiere \\( d[i] = 0 \\) für alle \\( i \\).
    - Für jede Position \\( i \\):
      - Berechne die kumulative Summe: \\( d[i] += d[i-1] \\) (falls \\( i > 0 \\)), was die aktuelle Anzahl extra Blöcke an Position \\( i \\) darstellt.
      - Prüfe, ob \\( d[i] \geq \text{need}_i \\). Wenn nicht, ist es unmöglich, die erforderliche Höhe zu erreichen, also gib \\( false \\) zurück.
      - Berechne die Länge des Bereichs, der durch das Umwerfen von Turm \\( i \\) beeinflusst wird:
        \\[
        \text{len} = d[i] - \text{need}_i + a_i
        \\]
        - \\( d[i] - \text{need}_i \\): Verfügbare extra Blöcke nach Erfüllung der Mindestanforderung.
        - \\( a_i \\): Die Anzahl der Blöcke, die durch die Höhe des Turms \\( i \\) beigetragen werden.
        - Diese \\( \text{len} \\) repräsentiert, wie viele Positionen rechts von \\( i \\) erhöht werden können, wenn Turm \\( i \\) umgeworfen wird.
      - Aktualisiere das Differenz-Array:
        - Erhöhe \\( d[i+1] \\) (falls \\( i+1 < n \\)), um den Effekt des Umwerfens von Turm \\( i \\) zu starten.
        - Verringere \\( d[i + \text{len} + 1] \\) (falls \\( i + \text{len} + 1 < n \\)), um den Effekt nach \\( \text{len} \\) Positionen zu beenden.

3.  **Machbarkeit**:
    - Die Prüffunktion simuliert nicht die tatsächliche Reihenfolge der Operationen, sondern verifiziert, ob es eine Reihenfolge gibt, die die Höhenanforderungen erfüllt.
    - Der Differenz-Array-Ansatz stellt sicher, dass die Anzahl der zu jeder Position hinzugefügten Blöcke konsistent mit einer gültigen Operationssequenz ist.
    - Die Bedingung für ein nicht fallendes Array ist implizit erfüllt, da die erforderlichen Höhen \\( \text{need}_i = \max(0, m - n + i) \\) nicht fallend sind (da \\( i \\) zunimmt, nimmt \\( m - n + i \\) zu oder bleibt 0).

#### Hauptschleife
- Lese die Anzahl der Testfälle \\( t \\).
- Für jeden Testfall:
  - Lese \\( n \\) und das Array \\( a \\).
  - Führe eine binäre Suche für \\( m \\) von 0 bis \\( n \\) durch.
  - Verwende die Prüffunktion, um zu bestimmen, ob MEX \\( m \\) erreichbar ist.
  - Aktualisiere \\( lo \\) (falls erreichbar) oder \\( hi \\) (falls nicht).
- Gib das maximale \\( m \\) (d.h. \\( lo \\)) für jeden Testfall aus.

---

### Warum der Code das Problem löst

1.  **Korrektheit der binären Suche**:
    - Die binäre Suche findet das maximale \\( m \\), für das die Prüffunktion \\( true \\) zurückgibt.
    - Da die Machbarkeit von MEX \\( m \\) die Machbarkeit für alle kleineren MEX-Werte impliziert (niedrigeres \\( m \\) erfordert weniger Positionen mit niedrigeren Höhen), identifiziert die binäre Suche korrekt den maximal möglichen MEX.

2.  **Genauigkeit der Prüffunktion**:
    - Die Prüffunktion stellt sicher, dass jede Position \\( i \\) nach allen Operationen mindestens \\( \max(0, m - n + i) \\) Blöcke haben kann.
    - Das Differenz-Array simuliert den kumulativen Effekt des Umwerfens der Türme und berücksichtigt, dass jeder Turm \\( a_i \\) Blöcke zu den nächsten \\( a_i \\) Positionen beiträgt.
    - Durch die Verarbeitung der Positionen von links nach rechts und die Anpassung des Differenz-Arrays verifiziert es, ob die initialen Höhen \\( a_i \\) neu verteilt werden können, um die erforderlichen Höhen zu erreichen.

3.  **Umgang mit der Nicht-Fallend-Bedingung**:
    - Die erforderlichen Höhen \\( \max(0, m - n + i) \\) sind nicht fallend, was sich mit der Problemforderung nach einem nicht fallenden finalen Array deckt.
    - Wenn die Prüffunktion erfolgreich ist, kann das resultierende Array nicht fallend gemacht werden, indem sichergestellt wird, dass jede Position die erforderliche Höhe erreicht oder überschreitet.

4.  **Effizienz**:
    - **Binäre Suche**: \\( O(\log n) \\) Iterationen (da \\( m \leq n \\)).
    - **Prüffunktion**: \\( O(n) \\) pro Aufruf, da jede Position einmal verarbeitet und das Differenz-Array in konstanter Zeit pro Position aktualisiert wird.
    - **Gesamt pro Testfall**: \\( O(n \log n) \\).
    - **Gesamt für alle Testfälle**: Da \\( \sum n \leq 10^5 \\), liegt die Gesamtkomplexität bei \\( O(t \cdot n \log n) \\), was innerhalb des 3-Sekunden-Zeitlimits liegt.

5.  **Randfälle**:
    - **\\( n = 1 \\)**: Wenn \\( a_1 = 0 \\), MEX = 1 (Array wird [0]). Wenn \\( a_1 > 0 \\), MEX = 0 (Array wird [0]). Der Code behandelt dies korrekt.
    - **Große \\( a_i \\)**: Da \\( a_i \leq 10^9 \\), aber nur die ersten \\( n-i \\) Positionen betroffen sind, begrenzt der Code den Effekt korrekt mithilfe von Array-Grenzen.
    - **Alle \\( a_i = 0 \\)**: Finales Array ist nur Nullen, MEX = 1. Die Prüffunktion bestätigt dies.
    - **Gemischte Werte**: Die binäre Suche und die Prüffunktion handhaben beliebige \\( a_i \geq 0 \\).

---

### Java-Code-Spezifika

Der Java-Code adaptiert die C++-Logik unter Verwendung von `BufferedReader` und `PrintWriter` für effiziente E/A, wie gewünscht. Wichtige Aspekte:

1.  **Eingabehandlung**:
    - Verwendet `BufferedReader`, um Zeilen zu lesen, und `StringTokenizer`, um Ganzzahlen zu parsen.
    - Liest \\( t \\), dann für jeden Testfall \\( n \\) und das Array \\( a \\).

2.  **Checker-Klasse**:
    - Kapselt die Prüflogik, um die C++-Lambda-Funktion nachzuahmen.
    - Verwendet ein Array \\( d \\), um den Differenz-Array-Ansatz zu simulieren.

3.  **Ausgabe**:
    - Verwendet `PrintWriter`, um das Ergebnis für jeden Testfall auszugeben, mit `out.flush()`, um sicherzustellen, dass die gesamte Ausgabe geschrieben wird.

4.  **Leistung**:
    - Der Java-Code behält die gleiche \\( O(n \log n) \\)-Komplexität pro Testfall bei.
    - `BufferedReader` und `PrintWriter` stellen sicher, dass die E/A schnell genug für \\( \sum n \leq 10^5 \\) ist.

---

### Fazit

Der Code löst das "Fallen Towers"-Problem durch:
- Verwendung einer binären Suche, um den maximalen MEX \\( m \\) zu finden.
- Einsatz einer auf einem Differenz-Array basierenden Prüffunktion, um zu verifizieren, ob die initialen Turmhöhen neu verteilt werden können, um ein nicht fallendes Array mit den erforderlichen Höhen zu erreichen.
- Sicherstellung der Korrektheit durch die nicht fallende Natur der erforderlichen Höhen und die Machbarkeit von Operationssequenzen.
- Handhabung aller Randfälle und Einhaltung der Zeit- und Speicherbeschränkungen.

Die Java-Implementierung übersetzt die C++-Logik treu und verwendet effiziente E/A, um den Anforderungen des Problems gerecht zu werden.