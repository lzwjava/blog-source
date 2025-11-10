---
audio: false
generated: true
image: false
lang: de
layout: post
title: Angular Dunkelmodus Elemente-Checkliste
translated: true
type: note
---

Wenn du einen Dark Mode in einem Angular Frontend implementierst, beginnst du normalerweise mit `body`, `select` und `option`, aber es gibt eine ganze Reihe weiterer häufiger HTML-Elemente, die du neu gestalten solltest, damit sich das Theme konsistent anfühlt. Hier ist eine praktische Checkliste:

### Seitenebene und Container

* `html`, `body` → Hintergrund- und Textfarbe.
* `div`, `section`, `article`, `aside`, `header`, `footer`, `main`, `nav` → Hintergrund- und Textfarben setzen (besonders wenn sie standardmäßig weiße Hintergründe haben).

### Text und Überschriften

* `h1, h2, h3, h4, h5, h6` → sicherstellen, dass der Text vor dunklem Hintergrund sichtbar ist.
* `p`, `span`, `a` → Textfarbe, Link-Hover-Farben und Zustände für besuchte Links anpassen.

### Formulare und Eingabefelder

* `input[type="text"], input[type="password"], input[type="email"], textarea` → Hintergrund, Textfarbe und Rand.
* `input[type="checkbox"], input[type="radio"]` → benötigen manchmal eine spezielle Behandlung für die Sichtbarkeit.
* `select, option` → wie du erwähnt hast, sowohl Hintergrund- als auch Textfarbe.
* `button` → Hintergrund, Rand und Textfarbe, plus Hover-/Active-Zustände.
* `label` → sicherstellen, dass der Text mit dem dunklen Hintergrund kontrastiert.
* `fieldset, legend` → Hintergrund und Rand.

### Listen und Tabellen

* `ul, ol, li` → Textfarbe.
* `table` → Hintergrund, Randfarbe und Textfarbe.
* `thead, tbody, tr, th, td` → individuelle Anpassungen für Hintergründe und Ränder.

### Interaktive Elemente

* `details, summary` → Hintergrund und Text.
* `dialog` → Hintergrund und Text.
* `mark` → Hervorhebungsfarben sollten auf Dunkel funktionieren (Standard-Gelb ist vielleicht zu hell).

### Medien und Sonstiges

* `hr` → Randfarbe (Standard ist oft zu hell auf Dunkel).
* `code, pre` → Hintergrund- und Textfarbe für Lesbarkeit.
* `blockquote` → Hintergrund- und Randfarbe.
* `progress, meter` → Farben für Spur und Wert.

---

💡 **Beste Praxis**: Anstatt überall `!important` zu verwenden, definiere CSS-Variablen für Farben (`--bg-color`, `--text-color`, etc.) und tausche sie aus, wenn der Dark Mode aktiv ist (z.B. durch Hinzufügen einer `.dark-mode`-Klasse zum `body`). Auf diese Weise können auch Angular Components und benutzerdefinierte Elemente sauber in das Theme eingebunden werden.

Möchtest du, dass ich einen **Basis-CSS-Snippet** für den Dark Mode (mit Variablen) entwerfe, den du als Ausgangspunkt in dein Angular-Projekt einfügen kannst?