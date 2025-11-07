---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Zentrieren gestapelter Formularelemente mit Flexbox
translated: true
---

```css
.sort-container {
    display: flex;
    flex-direction: column; /* Elemente vertikal stapeln */
    align-items: center; /* Zentriert Elemente horizontal in der Spalte */
    justify-content: center; /* Zentriert die Spalte vertikal */
    gap: 10px;
    margin-bottom: 1rem;
}

.sort-container select {
    padding: 5px;
    font-size: 16px;
}

.sort-container .post-number {
    font-size: 16px;
}
```

### Erklärung
- **flex-direction: column**: Ändert die Hauptachse von horizontal (row) zu vertikal, wodurch die `select` und `.post-number` Elemente von oben nach unten gestapelt werden.
- **align-items: center**: Behält die horizontale Zentrierung der untergeordneten Elemente bei.
- **justify-content: center**: Zentriert den gesamten vertikalen Stapel innerhalb des Containers.
- Ich habe auch die verschachtelte Selektor-Syntax korrigiert (habe `select` und `.post-number` aus dem Hauptblock verschoben, falls es sich um direkte Kindelemente handelt - bei Bedarf anpassen). Der `gap` wirkt nun vertikal zwischen den Elementen.