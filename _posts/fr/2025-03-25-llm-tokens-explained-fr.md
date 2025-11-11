---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Les jetons des LLM simplement expliqués
translated: true
type: note
---

Excellente question — les tokens dans les API de LLM peuvent prêter à confusion au début. Laissez-moi vous l'expliquer clairement.

---

## Que sont les tokens

* Un **token** est la plus petite unité de texte que le modèle traite.
* Ce **n'est pas exactement un mot**. Les tokens sont généralement des fragments de mots, des mots entiers, des signes de ponctuation, ou même des espaces, selon la langue et le tokenizer.
* Les LLM (comme les modèles GPT d'OpenAI) divisent le texte en tokens en utilisant un **tokenizer** prédéfini.

Par exemple :

* `"chat"` → 1 token
* `"chats"` → pourrait être divisé en `"chat"` + `"s"` → 2 tokens
* `"Tu es beau."` → se divise en quelque chose comme `"Tu"`, `" es"`, `" beau"`, `"."` → **4 tokens**

Ainsi, les tokens sont des **unités de sous-mots**, optimisées pour que le modèle puisse gérer de nombreuses langues et des mots rares efficacement.

---

## Pourquoi les tokens sont importants dans les API

1. **Facturation** – La plupart des API de LLM facturent au token (entrée + sortie).
2. **Limites** – Les modèles ont des limites maximales de tokens (par exemple, GPT-4 Turbo 128k signifie jusqu'à 128 000 tokens au total pour l'entrée + la sortie).
3. **Efficacité** – Vous voulez minimiser les tokens lors de l'envoi des prompts pour réduire les coûts et rester dans les limites.

---

## Gérer les tokens en pratique

* **Estimer les tokens** : Une règle approximative est \~4 caractères par token en anglais. Ainsi, une dissertation anglaise de 1 000 mots (≈5 000 caractères) fait \~1 200–1 300 tokens.
* **Vérifier les tokens précisément** : La plupart des SDK (comme `tiktoken` en Python pour OpenAI) vous permettent de compter les tokens avant de les envoyer.
* **Optimiser les prompts** :

  * Supprimez les espaces/mots inutiles.
  * Utilisez des instructions concises.
  * Résumez le contexte au lieu de vider le texte brut.

---

## Exemple

```python
import tiktoken

enc = tiktoken.get_encoding("cl100k_base")
text = "Tu es beau."
tokens = enc.encode(text)
print(tokens)        # liste des ID de tokens
print(len(tokens))   # nombre de tokens
```

Cela donnerait quelque chose comme `[9125, 3938, 13]` → 3 tokens (en fonction de la version exacte du tokenizer).

---

✅ Donc : **tokens ≠ mots**. Ce sont les éléments de base que le LLM voit. `"Tu es beau."` représente environ 3–4 tokens, et non 2 mots.

---

Voulez-vous que je vous montre **comment compter les tokens avec votre propre texte (par ex. des transcriptions, des essais, du code)** pour que vous puissiez voir le coût/les limites avant d'appeler l'API ?