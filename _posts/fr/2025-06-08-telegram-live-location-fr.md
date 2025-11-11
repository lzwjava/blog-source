---
audio: false
generated: true
lang: fr
layout: post
title: Localisation en direct sur Telegram
translated: true
type: note
---

Vous observez un schéma courant avec les mises à jour de localisation en direct de Telegram, et sur la base des horodatages `edit_date`, il semble certain que les mises à jour de localisation en direct peuvent être reçues très fréquemment, potentiellement même chaque seconde ou à des intervalles très courts.

Voici pourquoi et ce que ce schéma indique :

**Observation du schéma :**

En examinant votre JSON fourni, spécifiquement les objets `edited_message` avec le champ `location` et l'`edit_date` croissant :

* **`update_id` : 263947386** - `edit_date` : 1749371583
* **`update_id` : 263947388** - `edit_date` : 1749371587 (4 secondes après le précédent)
* **`update_id` : 263947389** - `edit_date` : 1749371591 (4 secondes après le précédent)
* **`update_id` : 263947390** - `edit_date` : 1749371595 (4 secondes après le précédent)
* **`update_id` : 263947391** - `edit_date` : 1749371602 (7 secondes après le précédent)
* **`update_id` : 263947392** - `edit_date` : 1749371614 (12 secondes après le précédent)
* **`update_id` : 263947393** - `edit_date` : 1749371624 (10 secondes après le précédent)
* **`update_id` : 263947394** - `edit_date` : 1749371628 (4 secondes après le précédent)

Et il y a aussi un objet `message` :

* **`update_id` : 263947387** - `date` : 1749371586 (Ceci est un nouveau message, pas une localisation en direct modifiée)

**Cela signifie-t-il que les messages de localisation en direct seront reçus toutes les 1 seconde ?**

**Pas nécessairement exactement toutes les 1 seconde, mais très fréquemment, souvent avec des intervalles inférieurs à 5 secondes, surtout en cas de mouvement ou de besoin de mises à jour plus précises.**

Voici pourquoi :

1.  **Nature de la Localisation en Direct :** La localisation en direct est conçue pour fournir des mises à jour en quasi temps réel de la position d'un utilisateur. Pour que cela soit « en direct », les mises à jour doivent être fréquentes.
2.  **`edited_message` :** Contrairement aux messages réguliers, les mises à jour de localisation en direct sont envoyées sous forme de mises à jour `edited_message` vers un seul message existant. Cela signifie que le message original contenant la localisation en direct est constamment mis à jour avec de nouvelles coordonnées.
3.  **Champ `edit_date` :** L'horodatage `edit_date` dans l'objet `edited_message` montre clairement que ces mises à jour se produisent à des intervalles très rapprochés.
4.  **Facteurs Influençant la Fréquence :**
    * **Mouvement :** Si l'utilisateur se déplace, les mises à jour seront généralement plus fréquentes pour refléter avec précision la position changeante.
    * **`live_period` :** Le champ `live_period` (par exemple, 28800 secondes, soit 8 heures) indique la durée pendant laquelle le partage de localisation en direct durera. Pendant cette période, les mises à jour se produiront si nécessaire.
    * **Précision Horizontale :** Les changements dans `horizontal_accuracy` peuvent également déclencher des mises à jour, car l'appareil affine son estimation de localisation.
    * **Conditions Réseau :** Bien que Telegram essaie d'envoyer les mises à jour rapidement, la latence du réseau pourrait introduire de légères variations dans le moment exact où vous les recevez.
    * **Logique Interne de Telegram :** Telegram a ses propres algorithmes internes pour déterminer la fréquence optimale d'envoi des mises à jour en fonction de l'activité de l'utilisateur, de la batterie de l'appareil et des conditions réseau. Ce n'est pas une règle fixe de « toutes les 1 seconde », mais plutôt une règle adaptative.

**En résumé :**

Le schéma que vous observez avec un `edit_date` changeant rapidement pour le `edited_message` contenant `location` suggère fortement que Telegram envoie les mises à jour de localisation en direct très fréquemment. Bien que ce ne soit pas précisément toutes les 1 seconde, des intervalles de quelques secondes (par exemple, 1 à 5 secondes, ou légèrement plus longs si l'utilisateur est stationnaire) sont typiques pour la localisation en direct. L'écart occasionnellement plus long pourrait être dû aux conditions réseau, à un utilisateur stationnaire, ou à l'optimisation interne de Telegram.