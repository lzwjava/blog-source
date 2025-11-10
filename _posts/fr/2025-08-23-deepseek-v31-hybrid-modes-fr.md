---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Modes Hybrides de DeepSeek V3.1 Expliqués
translated: true
type: note
---

Voici comment l’**API DeepSeek V3.1** gère sa nouvelle architecture d'inférence hybride (modes « Think » vs « Non‑Think ») :

---

### Aperçu des changements de l'API

#### 1. **Deux points de terminaison distincts (modes)**

* **`deepseek-chat`** correspond au **mode Non‑Thinking** — optimisé pour des réponses rapides.
* **`deepseek-reasoner`** correspond au **mode Thinking** — conçu pour des tâches de raisonnement plus délibérées et à plusieurs étapes.
  Les deux points de terminaison fonctionnent désormais sur le même modèle V3.1 avec une fenêtre de contexte de 128 K tokens. ([DeepSeek API Docs][1], [Data Science Dojo][2])

#### 2. **Prise en charge de contexte étendu**

* Les deux modes prennent en charge le contexte étendu de 128 K tokens, une amélioration majeure permettant de traiter des entrées très longues. ([DeepSeek API Docs][1], [Hugging Face][3])

#### 3. **Format et capacités améliorés**

* La **compatibilité avec l'API Anthropic** est désormais prise en charge, facilitant l'intégration de DeepSeek avec les bibliothèques client de type Anthropic. ([DeepSeek API Docs][1])
* **L'appel de fonction strict** est pris en charge (en version bêta), permettant une invocation d'outil plus robuste et validée via l'API. ([DeepSeek API Docs][1])

#### 4. **Bascule UI vs Appel API**

* Sur leur interface web (bouton « DeepThink »), les utilisateurs peuvent basculer entre les modes de manière interactive.
* Dans l'**API**, vous devez choisir explicitement le mode en définissant le paramètre `model` sur `"deepseek-chat"` (pour le non‑thinking) ou `"deepseek-reasoner"` (pour le thinking). ([DeepSeek API Docs][1])

#### 5. **Autres améliorations**

* **Plus de ressources API** et une expérience globale plus fluide pour les développeurs ont été introduites. ([DeepSeek API Docs][1])
* Le tokenizer sous-jacent et les modèles de chat ont été mis à jour pour prendre en charge le comportement basé sur le mode (par exemple, en insérant les tokens `` de manière appropriée). ([Hugging Face][3])

---

### Résumé : Ce qui a changé — Sans tableau

* **Nouvelle nomenclature** :

  * `deepseek-chat` → Mode Non‑Thinking
  * `deepseek-reasoner` → Mode Thinking

* **Architecture partagée** : Les deux sont construits sur le même modèle de 671B paramètres avec une longue fenêtre de contexte de 128 K tokens.

* **Options d'intégration améliorées** :

  * Prend en charge les API de type Anthropic.
  * Offre un appel de fonction strict (bêta), permettant des interactions avec les outils plus sûres et basées sur un schéma.

* **Mises à jour des modèles** : L'API utilise désormais des tokens spéciaux (``) dans les invites pour différencier les modes, et a revu la logique de modélisation des chats.

* **Expérience développeur** : La plateforme comprend plus de ressources, une documentation mise à jour et un processus d'intégration globalement plus fluide.

---

### Exemple d'utilisation (Python/HTTP)

**Non-Thinking (réponses rapides) :**

```python
import openai  # ou un SDK compatible DeepSeek
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role":"user","content":"Raconte-moi une blague."}],
)
```

**Thinking (raisonnement approfondi) :**

```python
response = client.chat.completions.create(
    model="deepseek-reasoner",
    messages=[{"role":"user","content":"Explique pourquoi le ciel est bleu."}],
)
```

**Appel de fonction (mode strict, bêta) :**
Vous pouvez définir des fonctions (outils) avec des schémas JSON et laisser le modèle les invoquer, recevant des appels structurés que vous pouvez exécuter et réinjecter — idéal pour créer des agents autonomes. ([DeepSeek API Docs][1], [Reddit][4], [apidog][5])

---

N'hésitez pas à me demander de l'aide pour créer des invites pour l'utilisation d'outils, optimiser les coûts ou la vitesse, ou explorer l'interface compatible Anthropic plus en détail !

[1]: https://api-docs.deepseek.com/news/news250821?utm_source=chatgpt.com "DeepSeek-V3.1 Release"
[2]: https://datasciencedojo.com/blog/deep-seek-v3-1/?utm_source=chatgpt.com "Deep Seek v3.1: The Next Leap in Open-Source Large ..."
[3]: https://huggingface.co/deepseek-ai/DeepSeek-V3.1?utm_source=chatgpt.com "deepseek-ai/DeepSeek-V3.1"
[4]: https://www.reddit.com/r/LocalLLaMA/comments/1munvj6/the_new_design_in_deepseek_v31/?utm_source=chatgpt.com "The new design in DeepSeek V3.1 : r/LocalLLaMA"
[5]: https://apidog.com/blog/deepseek-v3-1-api/?utm_source=chatgpt.com "How to Use DeepSeek-V3.1 API ?"