---
audio: false
generated: true
image: false
lang: es
layout: post
title: Desalineación de Programación de GitHub Actions
translated: true
type: note
---

Este es un activador programado al estilo Git (por ejemplo, GitHub Actions). Vamos a desglosarlo:

* **`on: schedule:`**
  Le dice al flujo de trabajo que se ejecute en un horario de calendario, no solo en eventos de push o pull-request.

* **`- cron: '0 * * * *'`**
  Una expresión cron estándar de cinco campos:

  ```
  ┌──────── minuto (0)
  │ ┌────── hora (*, es decir, cada hora)
  │ │ ┌──── día-del-mes (*, es decir, todos los días)
  │ │ │ ┌── mes (*, es decir, todos los meses)
  │ │ │ │ ┌ día-de-la-semana (*, es decir, todos los días de la semana)
  │ │ │ │ │
  0 * * * *
  ```

  → **Se ejecuta en el minuto 0 de cada hora** (es decir, a las 00:00, 01:00, 02:00…23:00 UTC), todos los días.

* **Pero los comentarios encima dicen:**

  > Se ejecuta cada hora desde las 05:00–13:00 UTC, de Lun–Vie
  > 05:00–13:00 UTC = 13:00–21:00 hora de Pekín (UTC+8)

  Esa intención (solo días laborables, solo en esas horas) realmente requeriría una expresión cron más específica, por ejemplo:

  ```yaml
  on:
    schedule:
      - cron: '0 5-13 * * 1-5'
  ```

  lo que significa:

  * en el minuto 0,
  * durante las horas 5 a 13 UTC,
  * los días de Lunes (1) a Viernes (5).

  En la hora de Pekín (UTC+8), eso corresponde efectivamente a las 13:00–21:00 hora local, los días laborables.

---

**En resumen:**

* Tal como está escrito (`'0 * * * *'`), se activará **cada hora en punto**, 24×7.
* Los comentarios describen una ventana **solo en días laborables, de 05:00 a 13:00 UTC**—si eso es lo que quieres, cambia la expresión cron para incluir `5-13` para el campo de la hora y `1-5` para el campo del día de la semana.