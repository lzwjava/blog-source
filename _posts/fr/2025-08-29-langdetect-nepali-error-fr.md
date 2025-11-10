---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Le détecteur de langue a confondu le texte avec le népalais
translated: true
type: note
---

Ah, je vois — merci de cette précision.

Dans le journal que vous avez collé :

```
Debug: raw langdetect output: [('ne', 0.9999953270916105)]
Debug: normalized langdetect output: [('ne', 0.9999953270916105)]
Debug: Detected languages: [('ne', 0.9999953270916105)]
```

Ici, **`ne` n'est pas le mot français** — c'est en fait un **code de langue** émis par `langdetect`.

La bibliothèque `langdetect` retourne parfois `"ne"` comme code ISO 639-1 pour le **népalais**.

* `"en"` = Anglais
* `"fr"` = Français
* `"hi"` = Hindi
* `"ne"` = Népalais

Donc dans ce cas, `langdetect` a pensé que votre texte était du népalais avec une probabilité de `~0.99999`.

C'est pourquoi votre validation a échoué avec :

```
Translated text does not contain the target language 'hi' (detected: [('ne', 0.9999953270916105)])
```

👉 Pour résumer :

* `ne` ici = code de langue ISO **Népalais**, pas le mot de négation française `"ne"`.
* Il apparaît lorsque `langdetect` décide que votre entrée ressemble à du népalais.

Voulez-vous que je vous montre comment **normaliser ou re-mapper** `ne` (Népalais) dans votre `_map_target_code` pour que votre validateur ne plante pas lorsque des langues inattendues apparaissent ?