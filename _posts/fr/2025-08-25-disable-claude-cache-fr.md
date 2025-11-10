---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Désactiver le cache dans Claude Code
translated: true
type: note
---

Dans **Claude Code**, cet extrait

```json
"cache_control": {
  "type": "ephemeral"
}
```

signifie que la réponse (ou l'artefact) produite par le modèle **n'est pas mise en cache pour être réutilisée**.

### Pourquoi cela existe

Normalement, Claude Code (et les autres SDKs Anthropic) peuvent mettre les réponses en cache pour accélérer les choses si vous envoyez à nouveau le même prompt. Mais lorsque vous définissez `"cache_control": { "type": "ephemeral" }`, vous indiquez à l'API :

* **Ne persiste pas ce résultat dans le cache**.
* **Ne le réutilise pas** si une autre requête identique arrive plus tard.
* Traite la réponse comme **éphémère** — uniquement pour cet appel.

### Quand l'utiliser

Ceci est utile si :

* Votre requête contient **des données sensibles ou personnelles** que vous ne voulez pas voir mises en cache.
* Vous envoyez **des requêtes ponctuelles** qui ne bénéficieraient pas d'une réutilisation.
* Vous voulez **une sortie fraîche** à chaque fois, même si le texte de la requête est identique.

En bref, `"ephemeral"` rend la sortie de Claude *transitoire* — privée à cette interaction, sans mise en cache entre les appels.

Souhaitez-vous que j'explique également en quoi cela diffère du comportement par défaut de `cache_control` dans Claude Code (par exemple `type: "default"` vs `"none"` vs `"ephemeral"`) ?