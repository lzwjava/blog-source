---
audio: false
generated: true
image: false
lang: de
layout: post
title: GitHub Actions Zeitplanfehlausrichtung
translated: true
type: note
---

Dies ist ein zeitgesteuerter Auslöser im Git-Stil (z.B. GitHub Actions). Lassen Sie uns das aufschlüsseln:

* **`on: schedule:`**  
  Weist den Workflow an, nach einem Zeitplan zu laufen, nicht nur bei Push- oder Pull-Request-Events.

* **`- cron: '0 * * * *'`**  
  Ein standardmäßiger Cron-Ausdruck mit fünf Feldern:

  ```
  ┌──────── Minute (0)
  │ ┌────── Stunde (*, d.h. jede Stunde)
  │ │ ┌──── Tag des Monats (*, d.h. jeden Tag)
  │ │ │ ┌── Monat (*, d.h. jeden Monat)
  │ │ │ │ ┌ Wochentag (*, d.h. jeden Tag der Woche)
  │ │ │ │ │
  0 * * * *
  ```

  → **Läuft um Minute 0 jeder Stunde** (d.h. um 00:00, 01:00, 02:00…23:00 UTC), jeden Tag.

* **Aber die Kommentare darüber sagen:**

  > Läuft jede Stunde von 05:00–13:00 UTC, Mo–Fr
  > 05:00–13:00 UTC = 13:00–21:00 Peking-Zeit (UTC+8)

  Diese Absicht (nur Werktage, nur zu diesen Stunden) würde eigentlich einen spezifischeren Cron-Ausdruck erfordern, zum Beispiel:

  ```yaml
  on:
    schedule:
      - cron: '0 5-13 * * 1-5'
  ```

  was bedeutet:

  * um Minute 0,
  * während der Stunden 5 bis 13 UTC,
  * an den Tagen Montag (1) bis Freitag (5).

  In Peking-Zeit (UTC+8) entspricht das tatsächlich 13:00–21:00 Ortszeit, an Werktagen.

---

**Kurz gesagt:**

* Wie geschrieben (`'0 * * * *'`) wird es **jede Stunde zur vollen Stunde** ausgelöst, 24×7.
* Die Kommentare beschreiben ein **zeitliches Fenster nur an Werktagen von 05:00–13:00 UTC** – wenn das gewünscht ist, ändern Sie den Cron-Ausdruck, um `5-13` für das Stundenfeld und `1-5` für das Wochentag-Feld einzubeziehen.