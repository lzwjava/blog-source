---
audio: false
generated: true
image: false
lang: de
layout: post
title: Berechnung der Modellantwortzeit
translated: true
type: note
---

Wir können es Schritt für Schritt durchgehen.

Aus dem Datensatz:

* **tokens_completion** = 9532
* **throughput** wird hier nicht angezeigt, aber Sie haben nach "tokens ÷ tokens pro Sekunde" gefragt.

Die Anfrage enthält:

* `generation_time = 203477 ms` → 203,477 Sekunden
* `tokens_completion = 9532`

Berechnung des tatsächlichen Durchsatzes:

$$
\text{tokens pro Sekunde} = \frac{9532}{203.477} \approx 46.8
$$

Der Benutzer musste also etwa **203 Sekunden (~3 Minuten 23 Sekunden)** auf die Antwort warten.

Wenn Sie den Durchsatz des Modells (Tokens/Sekunde) bereits kennen, dann ist die Wartezeit einfach:

$$
\text{Wartezeit} = \frac{\text{tokens_completion}}{\text{tokens pro Sekunde}}
$$

In diesem Fall liefert das Protokoll bereits beide Werte (Zeit und Tokens), sodass die Berechnung übereinstimmt.

👉 Kurze Antwort: Der Benutzer wartete etwa **203 Sekunden (~3 Minuten 23 Sekunden)** auf die 9532 Tokens, bei ~47 Tokens/Sekunde.

Möchten Sie, dass ich Ihnen auch eine **allgemeine Formel** zeige, die Sie für andere Protokolle wiederverwenden können (unter Verwendung von Latenz, Durchsatz und Token-Anzahlen)?