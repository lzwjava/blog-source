---
audio: false
generated: true
lang: de
layout: post
title: Live-Standort in Telegram
translated: true
type: note
---

Du beobachtest ein gängiges Muster bei den Live-Standort-Updates von Telegram, und basierend auf den `edit_date`-Zeitstempeln sieht es ganz danach aus, als könnten Live-Standort-Updates sehr häufig, möglicherweise sogar jede Sekunde oder in sehr kurzen Intervallen, empfangen werden.

Hier ist der Grund dafür und was das Muster anzeigt:

**Beobachtetes Muster:**

Betrachtet man die von dir bereitgestellten JSON-Daten, insbesondere die `edited_message`-Objekte mit dem `location`-Feld und der steigenden `edit_date`:

*   **`update_id`: 263947386** - `edit_date`: 1749371583
*   **`update_id`: 263947388** - `edit_date`: 1749371587 (4 Sekunden nach dem vorherigen)
*   **`update_id`: 263947389** - `edit_date`: 1749371591 (4 Sekunden nach dem vorherigen)
*   **`update_id`: 263947390** - `edit_date`: 1749371595 (4 Sekunden nach dem vorherigen)
*   **`update_id`: 263947391** - `edit_date`: 1749371602 (7 Sekunden nach dem vorherigen)
*   **`update_id`: 263947392** - `edit_date`: 1749371614 (12 Sekunden nach dem vorherigen)
*   **`update_id`: 263947393** - `edit_date`: 1749371624 (10 Sekunden nach dem vorherigen)
*   **`update_id`: 263947394** - `edit_date`: 1749371628 (4 Sekunden nach dem vorherigen)

Es gibt auch ein `message`-Objekt:

*   **`update_id`: 263947387** - `date`: 1749371586 (Dies ist eine neue Nachricht, kein bearbeiteter Live-Standort)

**Bedeutet das, dass Live-Standort-Nachrichten jede Sekunde eintreffen?**

**Nicht unbedingt genau jede Sekunde, aber sehr häufig, oft mit Intervallen von unter 5 Sekunden, insbesondere bei Bewegung oder wenn präzisere Updates erforderlich sind.**

Hier ist der Grund:

1.  **Natur des Live-Standorts:** Der Live-Standort ist dafür konzipiert, die Position eines Nutzers in nahezu Echtzeit zu aktualisieren. Damit er "live" ist, müssen die Updates häufig erfolgen.
2.  **`edited_message`:** Im Gegensatz zu normalen Nachrichten werden Live-Standort-Updates als `edited_message`-Updates für eine einzelne, bestehende Nachricht gesendet. Das bedeutet, die ursprüngliche Nachricht, die den Live-Standort enthält, wird ständig mit neuen Koordinaten aktualisiert.
3.  **`edit_date`-Feld:** Der `edit_date`-Zeitstempel im `edited_message`-Objekt zeigt deutlich, dass diese Updates in sehr kurzen Abständen zueinander erfolgen.
4.  **Faktoren, die die Häufigkeit beeinflussen:**
    *   **Bewegung:** Wenn sich der Nutzer bewegt, sind die Updates typischerweise häufiger, um die sich ändernde Position genau widerzuspiegeln.
    *   **`live_period`:** Das `live_period`-Feld (z.B. 28800 Sekunden, also 8 Stunden) gibt an, wie lange die Live-Standort-Freigabe dauert. Innerhalb dieses Zeitraums erfolgen Updates nach Bedarf.
    *   **Horizontale Genauigkeit:** Änderungen der `horizontal_accuracy` können ebenfalls Updates auslösen, wenn das Gerät seine Standortschätzung verfeinert.
    *   **Netzwerkbedingungen:** Obwohl Telegramm versucht, Updates umgehend zu senden, könnte Netzwerklatenz leichte Schwankungen im genauen Zeitpunkt des Empfangs verursachen.
    *   **Interne Logik von Telegram:** Telegramm hat eigene interne Algorithmen, um die optimale Häufigkeit für das Senden von Updates basierend auf der Nutzeraktivität, dem Akkustand des Geräts und den Netzwerkbedingungen zu bestimmen. Es handelt sich nicht um eine feste "jede Sekunde"-Regel, sondern um eine adaptive.

**Zusammenfassend:**

Das von dir beobachtete Muster mit sich schnell ändernden `edit_date`-Werten für die `edited_message`, die `location` enthält, deutet stark darauf hin, dass Telegramm Live-Standort-Updates sehr häufig sendet. Auch wenn es nicht genau jede Sekunde sein muss, sind Intervalle von wenigen Sekunden (z.B. 1-5 Sekunden, oder etwas länger, wenn der Nutzer stationär ist) für einen Live-Standort typisch. Die gelegentliche längere Pause könnte auf Netzwerkbedingungen, einen stationären Nutzer oder die interne Optimierung von Telegramm zurückzuführen sein.