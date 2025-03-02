---
audio: false
generated: false
lang: de
layout: post
title: Erweiterte Verwendung von Markdown
translated: true
---

## Referenzen

Referenz [^1].

In Fußnoten denken Sie daran, nach der `[Nummer]` einen `:` hinzuzufügen, um eine korrekte Analyse zu gewährleisten.

---

## Bildklasse

Sie können Klassen auf Bilder in Markdown wie folgt anwenden:

```markdown
{: .zentriert }
![](assets/images/pin/pin.jpg){: .responsiv }
*Quelle: Telegram*{: .caption }
```

Dies rendert das Bild mit den angegebenen Klassen:

{: .centered }  
![](assets/images/pin/pin.jpg){: .responsive }  
*Quelle: Telegram*{: .caption }

## Inhaltsverzeichnis

- [Einführung](#introduction)
- [Kapitel 1](#chapter-1)
- [Fazit](#conclusion)

---

### Einführung

Hier ist die Einleitung.

---

### Kapitel 1

Hier ist Kapitel 1.

---

### Fazit

Hier ist die Schlussfolgerung.

## Mermaid

```mermaid
graph TD
    A[Ladebox] --> B[Powerbank]
    A --> C[Bluetooth-Lautsprecher]
    A --> D[Handy]
    A --> E[Elektrische Lampe]
    A --> F[Laptop]
    A --> G[Smartwatch]
    A --> H[Cloud-Server]
    B --> H
    C --> H
    D --> H
    E --> H
    F --> H
    G --> H
```

Es wird hier immer noch nicht gerendert, aber es funktioniert gut und kann in Mistral generiert werden. Lass uns etwas Zeit finden, um mehr zu lernen.

---

[^1]: Hier ist einer.
```