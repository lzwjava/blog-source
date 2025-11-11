---
audio: false
generated: true
image: false
lang: de
layout: post
title: ASCII Hex UTF-8 Einfach Erklärt
translated: true
type: note
---

Hier eine klare Aufschlüsselung:

---

### ASCII

* **Definition**: ASCII (American Standard Code for Information Interchange) ist eine der frühesten Zeichenkodierungen.
* **Bereich**: Verwendet **7 Bits** (Werte 0–127).
* **Bedeutung**: Jede Zahl entspricht einem Zeichen.
  Zum Beispiel:

  * `65` → `"A"`
  * `97` → `"a"`
  * `48` → `"0"`
* **Einschränkung**: Deckt nur englische Buchstaben, Ziffern, Satzzeichen und Steuercodes (wie Zeilenumbruch) ab.

---

### Hex (Hexadezimale Darstellung)

* **Definition**: Hex ist selbst kein Zeichensatz, sondern eine **numerische Darstellung** (Basis-16) von Daten.
* **Verwendung**: Wird häufig verwendet, um Bytes kompakt und für Menschen lesbar darzustellen.
* **Beispiel**:

  * ASCII `"A"` = dezimal `65` = hex `41`.
  * ASCII `"B"` = dezimal `66` = hex `42`.
  * Also sieht der Text `"AB"` in Hex wie `41 42` aus.

---

### UTF-8

* **Definition**: UTF-8 ist ein **Unicode-Kodierungsstandard**.
* **Merkmale**:

  * Variable Länge: Kodiert jedes Zeichen in **1 bis 4 Bytes**.
  * Abwärtskompatibel mit ASCII: Zeichen `0–127` sind identisch mit ASCII (1 Byte).
  * Kann alle Unicode-Zeichen darstellen (Buchstaben, Symbole, Emojis, chinesische Zeichen usw.).
* **Beispiele**:

  * `"A"` → `41` (gleich wie ASCII).
  * `"中"` → `E4 B8 AD` (drei Bytes in Hex).
  * `"😊"` → `F0 9F 98 8A` (vier Bytes in Hex).

---

✅ **Zusammengefasst**:

* ASCII = alter 7-Bit-Code für englische Zeichen.
* Hex = eine Art, Zahlen/Bytes zu schreiben (Basis-16).
* UTF-8 = moderne Kodierung, die ASCII beinhaltet, aber auch jede Sprache und jedes Symbol unterstützt.

---

Möchtest du, dass ich dir auch ein **direktes Gegenbeispiel desselben Textes** (`"Hello 世界😊"`) in ASCII (wo möglich), Hex und UTF-8 zeige, damit du den Unterschied direkt sehen kannst?