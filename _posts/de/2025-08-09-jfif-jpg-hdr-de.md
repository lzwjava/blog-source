---
audio: false
generated: true
image: false
lang: de
layout: post
title: 'JFIF: JPEG mit Header'
translated: true
type: note
---

JFIF steht für **JPEG File Interchange Format** – im Grunde ist es eine Möglichkeit, JPEG-komprimierte Bilddaten so zu verpacken, dass verschiedene Software und Geräte sie zuverlässig austauschen können.

Hier die wesentlichen Punkte:

* **Zweck** – JFIF wurde in den frühen 1990er Jahren entwickelt, um zu standardisieren, wie JPEG-Bilder gespeichert und übertragen werden, da reine JPEG-Daten allein keine wichtigen Details wie Pixeldichte oder Farbraum definierten.
* **Dateierweiterung** – Normalerweise `.jfif`, aber viele JPEG-Bilder (`.jpg` / `.jpeg`) sind intern tatsächlich im JFIF-Format gespeichert.
* **Struktur** –

  1. **JPEG-kodierte Bilddaten** (die komprimierten Pixel)
  2. **JFIF APP0-Markierungssegment** (Metadaten wie Auflösung, Seitenverhältnis und Farbraum)
* **Metadaten** – Enthält Informationen wie DPI (dots per inch), Vorschaubild und Hinweise zum Seitenverhältnis.
* **Kompatibilität** – JFIF ist im Wesentlichen eine Teilmenge des breiteren JPEG-Standards, daher können die meisten Bildbetrachter, Browser und Kameras es problemlos lesen.

Kurz gesagt:
Eine `.jfif`-Datei ist nur ein JPEG-Bild mit einem kleinen, standardisierten Header, der den Austausch zwischen Systemen erleichtert, ohne Verwirrung über Auflösung oder Farbinterpretation.

Falls du möchtest, kann ich auch erklären, **wie sich JFIF von EXIF-JPEGs unterscheidet**, die Kameras produzieren, da dies eine häufige Fehlerquelle ist. Soll ich darauf eingehen?