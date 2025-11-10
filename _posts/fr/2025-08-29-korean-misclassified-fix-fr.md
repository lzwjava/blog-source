---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Correctif pour le validateur coréen incorrectement classé comme chinois
translated: true
type: note
---

Compris — dans cette sortie de débogage :

```
Debug: raw langdetect output: [('ko', 0.9999995211930662)]
...
Langues détectées : [('ko', 0.9999995211930662)]
```

Le code **`ko`** est le code de langue ISO 639-1 pour le **coréen**. 🇰🇷

Donc `langdetect` indique :

* Il pense que le texte est en coréen (`ko`)
* Avec une probabilité ≈ **0,9999995** (essentiellement 100 %)

Cela explique l'erreur : votre validateur attendait `"zh-tw"` (chinois traditionnel), mais le détecteur a décidé que l'entrée ressemblait plutôt à du coréen.

👉 Petit rappel de correspondance de `langdetect` / ISO 639-1 :

* `zh` → Chinois (non spécifié)
* `zh-cn` → Chinois simplifié (Chine)
* `zh-tw` (ou `hant` dans votre correspondance) → Chinois traditionnel (Taïwan)
* `ja` → Japonais
* `ko` → Coréen
* `ne` → Népalais
* `hi` → Hindi

Souhaitez-vous que je suggère comment vous pourriez **renforcer votre validateur** pour qu'il ne plante pas lorsque `langdetect` classe mal le texte (par exemple, en autorisant une solution de repli si les caractères de l'écriture cible sont clairement chinois mais que le code ressort comme `ko`) ?