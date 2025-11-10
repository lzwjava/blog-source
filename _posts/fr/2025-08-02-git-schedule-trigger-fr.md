---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Décalage de la Planification des GitHub Actions
translated: true
type: note
---

Voici un déclencheur planifié de type Git (par exemple, GitHub Actions). Décomposons-le :

* **`on: schedule:`**
  Indique que le workflow s'exécute selon un calendrier planifié, et pas seulement lors d'événements de type `push` ou `pull-request`.

* **`- cron: '0 * * * *'`**
  Une expression cron standard à cinq champs :

  ```
  ┌──────── minute (0)
  │ ┌────── heure (*, c'est-à-dire toutes les heures)
  │ │ ┌──── jour du mois (*, c'est-à-dire tous les jours)
  │ │ │ ┌── mois (*, c'est-à-dire tous les mois)
  │ │ │ │ ┌ jour de la semaine (*, c'est-à-dire tous les jours de la semaine)
  │ │ │ │ │
  0 * * * *
  ```

  → **S'exécute à la minute 0 de chaque heure** (c'est-à-dire à 00:00, 01:00, 02:00…23:00 UTC), tous les jours.

* **Mais les commentaires au-dessus indiquent :**

  > S'exécute toutes les heures de 05:00 à 13:00 UTC, du lundi au vendredi
  > 05:00–13:00 UTC = 13:00–21:00 heure de Beijing (UTC+8)

  Cette intention (en semaine, uniquement pendant ces heures) nécessiterait en réalité une expression cron plus spécifique, par exemple :

  ```yaml
  on:
    schedule:
      - cron: '0 5-13 * * 1-5'
  ```

  ce qui signifie :

  * à la minute 0,
  * pendant les heures 5 à 13 UTC,
  * les jours du lundi (1) au vendredi (5).

  À l'heure de Beijing (UTC+8), cela correspond effectivement à 13:00–21:00 heure locale, en semaine.

---

**En résumé :**

* Tel qu'écrit (`'0 * * * *'`), le workflow se déclenchera **toutes les heures, pile**, 24h/24, 7j/7.
* Les commentaires décrivent une fenêtre **uniquement en semaine, de 05:00 à 13:00 UTC** — si c'est ce qui est souhaité, modifiez l'expression cron pour inclure `5-13` pour le champ `heure` et `1-5` pour le champ `jour de la semaine`.