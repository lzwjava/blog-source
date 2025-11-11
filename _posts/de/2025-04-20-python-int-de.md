---
audio: false
generated: true
lang: de
layout: post
title: Python-Ganzzahl
translated: true
type: note
---

In Python hat der `int`-Typ **keinen festen Bereich** oder Größenlimit. Im Gegensatz zu Sprachen wie C oder Java, in denen Ganzzahlen durch bestimmte Bitgrößen beschränkt sind (z. B. 32-Bit oder 64-Bit), ist Pythons `int` beliebig genau, was bedeutet, dass es so groß werden kann, wie der verfügbare Speicher es zulässt. Dies gilt sowohl für Python 2 (seit Python 2.2, wo `long` und `int` vereinheitlicht wurden) als auch für Python 3.

### Wichtige Punkte:
- **Keine obere oder untere Grenze**: Python-Ganzzahlen können jede ganze Zahl, positiv oder negativ, darstellen, begrenzt nur durch den Speicher des Systems. Zum Beispiel können Sie extrem große Zahlen wie `10**100` oder sehr negative Zahlen wie `-10**100` haben.
- **Speicherverbrauch**: Der für einen `int` benötigte Speicher wächst dynamisch mit der Größe der Zahl. Python verwendet eine variabel lange Kodierung, um große Ganzzahlen zu speichern.
- **Leistung**: Operationen mit sehr großen Ganzzahlen (z. B. `2**1000000`) können aufgrund des erhöhten Speicher- und Rechenaufwands langsamer sein, werden aber dennoch unterstützt.

### Beispiel:
```python
# Kleine Ganzzahl
small = 42
print(small, type(small))  # 42 <class 'int'>

# Große Ganzzahl
large = 2**1000
print(large, type(large))  # 107150860718626732... <class 'int'>

# Negative Ganzzahl
negative = -10**100
print(negative, type(negative))  # -10000000000... <class 'int'>
```

### Bezug zu Ihrer vorherigen Anfrage:
In Ihrem TigerOpen API-Problem liegt die `order_id` (`359248847525015552`) gut innerhalb des Bereichs von Pythons `int`, daher besteht in Python selbst keine Sorge wegen Überlaufs oder Abschneidens. Der `biz param error` liegt wahrscheinlich an den Erwartungen der API (z. B. dass eine Zeichenkette `order_id` erforderlich ist) und nicht an einer Beschränkung von Pythons Ganzzahltyp. Der Vorschlag, `str(order_id)` im `get_order`-Aufruf zu versuchen, adressiert diese mögliche Ungleichheit.

### Zusätzliche Hinweise:
- **Systemlimiten**: Während Pythons `int` kein theoretisches Limit hat, ergeben sich praktische Grenzen aus dem verfügbaren RAM. Extrem große Ganzzahlen (z. B. `2**1000000`) können erheblichen Speicher verbrauchen.
- **Typüberprüfung**: Verwenden Sie `isinstance(x, int)`, um zu prüfen, ob eine Variable eine Ganzzahl ist.
- **Konvertierung**: Sie können Zeichenketten oder Fließkommazahlen mit `int()` in Ganzzahlen umwandeln, seien Sie jedoch bei Fließkommazahlen vorsichtig, um Genauigkeitsverlust zu vermeiden (z. B. ergibt `int(3.9)` `3`).

Wenn Sie weitere Fragen zu Ganzzahlen in Python haben oder Hilfe mit dem TigerOpen API-Problem benötigen, lassen Sie es mich wissen!