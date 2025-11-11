---
audio: false
generated: true
lang: de
layout: post
title: Handel mit linearer Regression
translated: true
type: note
---

Gute Frage! Du kombinierst hier zwei Aufgaben:

1.  **Aktienhistorische Daten abrufen (z. B. Tencent) mit der TigerOpen API**
2.  **Diese Daten mit deinem bestehenden numpy-basierten linearen Regressionscode verwenden**

---

## Wird es sofort funktionieren?

**Nein, nicht direkt.** Dein aktueller ML-Code erwartet `x_train` und `y_train` als numpy-Arrays numerischer Werte, die Merkmale und Labels darstellen (z. B. Bevölkerung vs. Gewinn). Aber die TigerOpen API gibt **historische Aktien-Bars** zurück (OHLCV-Daten), was eine Zeitreihe mit mehreren Feldern pro Zeitstempel ist.

Du musst:

-   Die Aktiendaten korrekt extrahieren und in geeignete `x_train`- und `y_train`-Arrays aufbereiten.
-   Dein Modell und deinen Code an den Aktiendaten-Kontext anpassen (z. B. Vorhersage des Schlusskurses basierend auf vorherigen Tagen).

---

## Wie passt man die Aktiendaten für das lineare Regressionsmodell an?

### Schritt 1: Historische Daten für Tencent (Symbol `'00700'`) abrufen

```python
bars_dict = quote_client.get_bars(
    symbols=['00700'],
    period=BarPeriod.DAY,
    begin_time='2024-01-01',
    end_time=datetime.now().strftime('%Y-%m-%d'),
    limit=100,
    right=QuoteRight.BR
)

bars = bars_dict.get('00700', [])
```

### Schritt 2: Merkmale und Labels extrahieren

Ein einfacher Ansatz:

-   Verwende den Tagesindex als `x_train` (z. B. 0, 1, 2, ...)
-   Verwende den Schlusskurs als `y_train`

```python
import numpy as np

x_train = np.array([i for i in range(len(bars))])
y_train = np.array([bar.close for bar in bars])
```

Alternativ kannst du den Schlusskurs des Vortages als Merkmal verwenden, um den Schlusskurs des nächsten Tages vorherzusagen, oder komplexere Merkmale.

### Schritt 3: Deinen linearen Regressionscode verwenden

Jetzt sind dein `x_train` und `y_train` numpy-Arrays mit Zahlen, also sollte dein Code funktionieren, nachdem du deine `compute_cost`- und `compute_gradient`-Funktionen korrigiert hast (die derzeit Null oder Null-Gradienten zurückgeben).

---

## Beispiel: Implementierung von compute_cost und compute_gradient

```python
def compute_cost(x, y, w, b):
    m = x.shape[0]
    total_cost = 0.5 * np.sum((w * x + b - y) ** 2) / m
    return total_cost

def compute_gradient(x, y, w, b):
    m = x.shape[0]
    error = w * x + b - y
    dj_dw = np.sum(error * x) / m
    dj_db = np.sum(error) / m
    return dj_dw, dj_db
```

---

## Zusammenfassung

-   Rufe historische Aktiendaten mit der TigerOpen API ab
-   Konvertiere die Zeitreihendaten in numerische Arrays (`x_train`, `y_train`)
-   Implementiere oder korrigiere deine Kosten- und Gradientenfunktionen
-   Dann wird dein Gradientenabstiegs- und Plotting-Code funktionieren, um ein lineares Modell an die Aktienkursdaten anzupassen

---

## Bonus: Plotten der Aktienkurse

Dein Streudiagramm zeigt den Schlusskurs über die Tage, und die Regressionslinie passt einen Trend an.

---

Falls du möchtest, kann ich dir helfen, ein vollständiges Beispiel zu schreiben, das das Abrufen von TigerOpen-Daten mit deinem numpy linearen Regressionscode integriert! Frag einfach.