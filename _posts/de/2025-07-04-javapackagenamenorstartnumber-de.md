---
audio: false
generated: true
lang: de
layout: post
title: Java-Paketnamen dürfen nicht mit Zahlen beginnen
translated: true
type: note
---

In Java darf ein Paketname **nicht mit einer Zahl beginnen**. Gemäß den Java-Namenskonventionen und der Java Language Specification:

- Paketnamen müssen gültige Bezeichner sein.
- Ein gültiger Bezeichner in Java muss mit einem Buchstaben (A-Z oder a-z), einem Unterstrich (`_`) oder einem Dollarzeichen (`$`) beginnen.
- Zahlen (0-9) sind in Bezeichnern erlaubt, aber nur **nach** dem ersten Zeichen.

Beispiele:
- Gültige Paketnamen: `com.example`, `my_package`, `a123`
- Ungültige Paketnamen: `123example`, `1package`

Wenn Sie versuchen, einen Paketnamen zu verwenden, der mit einer Zahl beginnt, wird der Java-Compiler einen Syntaxfehler werfen. Als Workaround können Sie:
- Den Paketnamen mit einem Buchstaben oder Unterstrich beginnen lassen, z.B. `a123.example` oder `_123.example`.
- Einen beschreibenden Namen verwenden, der den Konventionen folgt, wie `com.example.project123`.

Diese Regel gewährleistet Konsistenz und Kompatibilität im Namenssystem von Java.