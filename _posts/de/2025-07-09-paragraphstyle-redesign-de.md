---
audio: false
generated: true
lang: de
layout: post
title: Absatzstil für mittlere Schriftstärke neu definieren
translated: true
type: note
---

Um die gesamte `cvparagraph`-Umgebung so zu ändern, dass sie `\mdseries` anstelle von `\bodyfontlight` verwendet, müssen Sie den Befehl `\paragraphstyle` neu definieren. Fügen Sie dies Ihrer Präambel hinzu, nachdem die awesome-cv-Klasse geladen wurde:

```latex
\renewcommand*{\paragraphstyle}{\fontsize{11pt}{1em}\mdseries\upshape\color{text}}
```

Dadurch ändert sich der Absatzstil von:
- `\bodyfontlight` (leichtes Gewicht)

zu:
- `\mdseries` (mittleres Gewicht, ähnlich dem `description`-Stil)

Auf diese Weise verwendet Ihre gesamte `cvparagraph`-Umgebung die mittlere Schriftstärke, so wie es der `\descriptionstyle` tut.