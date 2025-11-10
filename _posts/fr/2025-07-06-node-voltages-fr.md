---
audio: false
generated: true
lang: fr
layout: post
title: Résolution des tensions nodales par l'analyse nodale
translated: true
type: note
---

La variable inconnue principale résolue dans l'analyse nodale est **les tensions des nœuds**.

Voici une analyse de chaque option :

* **Courants de branche :** Bien que les courants de branche puissent être déterminés *après* avoir résolu les tensions des nœuds, ils ne sont pas les variables principales directement résolues dans l'analyse nodale. L'analyse nodale se concentre sur l'application de la Loi des Courants de Kirchhoff (LCK) à chaque nœud, qui est exprimée en termes de tensions et de résistances, et non directement en courants.

* **Courants de maille :** Les courants de maille sont les variables inconnues principales résolues dans **l'analyse par mailles** (également appelée analyse des boucles), et non dans l'analyse nodale. L'analyse par mailles applique la Loi des Tensions de Kirchhoff (LTK) autour des mailles indépendantes.

* **Tensions des nœuds :** C'est la bonne réponse. Dans l'analyse nodale, nous définissons un nœud de référence (souvent appelé masse) puis assignons des variables de tension inconnues aux autres nœuds indépendants du circuit. En appliquant la Loi des Courants de Kirchhoff (LCK) à chaque nœud indépendant, nous formons un système d'équations linéaires où les inconnues sont précisément ces tensions de nœud. Une fois les tensions des nœuds trouvées, toutes les autres quantités du circuit (comme les courants de branche, la dissipation de puissance, etc.) peuvent être facilement calculées.

* **Dissipation de puissance :** La dissipation de puissance est une quantité qui peut être calculée *après* que les tensions des nœuds (et par la suite les courants de branche) sont connus. C'est un résultat de l'analyse, et non une variable inconnue principale utilisée pour établir les équations initiales dans l'analyse nodale.