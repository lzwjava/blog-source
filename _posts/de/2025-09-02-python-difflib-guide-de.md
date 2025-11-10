---
audio: false
generated: true
image: false
lang: de
layout: post
title: Python Difflib Sequenzvergleich Leitfaden
translated: true
type: note
---

In Python bietet das Modul **`difflib`** Werkzeuge zum Vergleichen von Sequenzen – Strings, Listen oder beliebige iterierbare Objekte. Es wird oft für Aufgaben wie das Erkennen von Unterschieden zwischen Texten (ähnlich wie `diff` in Unix) oder zum Erstellen von Auto-Vervollständigungs- und Ähnlichkeitstools verwendet.

---

### Wie `difflib` funktioniert

Im Kern versucht `difflib`, die längsten zusammenhängenden übereinstimmenden Teilsequenzen zwischen zwei Eingaben zu finden. Anschließend nutzt es diese Übereinstimmungen, um Ähnlichkeiten und Unterschiede hervorzuheben. Die Bibliothek kann:

* Menschenlesbare Diffs erzeugen (`ndiff`, `unified_diff`, `context_diff`).
* Ähnlichkeitsverhältnisse zwischen Sequenzen berechnen.
* Enge Treffer aus einer Liste vorschlagen (`get_close_matches`).

---

### `SequenceMatcher`

Die wichtigste Klasse ist **`difflib.SequenceMatcher`**.

**So funktioniert es**:

* Es vergleicht zwei Sequenzen Element für Element.
* Es sucht nach der *längsten gemeinsamen Teilsequenz* (muss aber nicht unbedingt zusammenhängend sein).
* Es erzeugt eine Liste von Operationen (`replace`, `delete`, `insert`, `equal`), die beschreiben, wie eine Sequenz in die andere transformiert werden kann.

**Wichtige Methoden**:

1. **`ratio()`**
   Gibt einen Float-Wert in `[0, 1]` zurück, der die Ähnlichkeit misst.
   Formel:

   $$
   \text{ratio} = \frac{2 \times M}{T}
   $$

   wobei `M` = Anzahl der übereinstimmenden Elemente und `T` = Gesamtelemente in beiden Sequenzen ist.

2. **`quick_ratio()`** und **`real_quick_ratio()`**
   Schnellere Approximationen der Ähnlichkeit, die Geschwindigkeit über Genauigkeit stellen.

3. **`get_opcodes()`**
   Gibt eine Liste von Operationen zurück, um `a` in `b` zu transformieren. Beispiel: `[('replace', 0, 2, 0, 1), ('equal', 2, 4, 1, 3)]`.

4. **`get_matching_blocks()`**
   Gibt alle übereinstimmenden Teilsequenzen mit ihren Positionen zurück.

---

### Beispiel

```python
import difflib

a = "hello world"
b = "helo wrld"

s = difflib.SequenceMatcher(None, a, b)

print("Similarity ratio:", s.ratio())
print("Operations:", s.get_opcodes())
print("Matching blocks:", s.get_matching_blocks())
```

**Ausgabe**:

```
Similarity ratio: 0.9090909090909091
Operations: [('equal', 0, 1, 0, 1), ('delete', 1, 2, 1, 1),
             ('equal', 2, 5, 1, 4), ('delete', 5, 6, 4, 4),
             ('equal', 6, 11, 4, 9)]
Matching blocks: [Match(a=0, b=0, size=1),
                  Match(a=2, b=1, size=3),
                  Match(a=6, b=4, size=5),
                  Match(a=11, b=9, size=0)]
```

---

👉 Kurz gesagt:

* `difflib` ist ein Toolkit für den Sequenzvergleich.
* `SequenceMatcher` ist die Kern-Engine – es findet übereinstimmende Teilsequenzen und berechnet Ähnlichkeiten.
* Es ist nützlich für Diffs, Rechtschreibprüfungen, Plagiatserkennung, Auto-Vorschläge usw.

Möchtest du, dass ich dir auch zeige, wie man `get_close_matches()` (das intern `SequenceMatcher` verwendet) für Fuzzy String Matching verwendet, wie z.B. in der Rechtschreibprüfung oder Suchvorschlägen?