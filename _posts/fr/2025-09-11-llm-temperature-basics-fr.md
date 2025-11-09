---
audio: false
date: 2025-09-11
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: Comprendre les bases du paramètre de température des LLM
translated: true
type: note
---

Dans les API de LLM (comme OpenAI, Copilot API, Anthropic, etc.), le **temperature** est un paramètre qui contrôle à quel point la sortie du modèle est *aléatoire* ou *déterministe*.

---

### Fonction de la Temperature

* **Temperature faible (proche de 0) :**
  Le modèle devient déterministe, choisissant toujours le jeton suivant le plus probable.
  Exemple : Si vous demandez une définition, il donnera la réponse la plus standard/attendue à chaque fois.

* **Temperature élevée (plus proche de 1 ou au-dessus) :**
  Le modèle échantillonne plus librement, explorant des jetons moins probables. Cela augmente la variété, la créativité et l'imprévisibilité.
  Exemple : Pour le brainstorming, la narration ou la génération de variations de code, une température plus élevée peut être préférable.

---

### Signification de « 0.7 »

* `temperature = 0.7` est un **équilibre modéré**.

  * Elle permet une certaine part d'aléatoire et de diversité.
  * Le modèle ne sera pas aussi rigide qu'avec `0`, mais pas aussi « sauvage » qu'avec `1.2`.
  * C'est pourquoi **0.7 est souvent utilisé comme valeur par défaut** dans de nombreuses API, y compris les systèmes de type Copilot — cela donne des résultats créatifs mais toujours fiables.

---

### Comment l'Utiliser

Dans la plupart des API, vous la transmettez en tant que paramètre dans la requête. Par exemple :

**API OpenAI (chat completion) :**

```json
{
  "model": "gpt-4.1",
  "messages": [
    {"role": "user", "content": "Écris une petite histoire sur un dragon et un robot."}
  ],
  "temperature": 0.7
}
```

**API GitHub Copilot :**
Le paramètre fonctionne de manière similaire. Copilot utilise la température en interne pour choisir entre des complétions plus littérales et des suggestions plus exploratoires. La plupart des intégrations IDE la définissent autour de `0.7`, mais certains contextes (comme la complétion de code) peuvent utiliser des valeurs plus faibles pour la stabilité.

---

✅ **Règle générale :**

* **0–0,3** → Déterministe, factuel, prévisible. Bon pour les mathématiques, la documentation d'API, la configuration, les tests unitaires.
* **0,4–0,7** → Équilibre, écriture naturelle, codage standard. Bonne valeur par défaut pour la plupart des cas.
* **0,8–1,2** → Créatif, exploratoire, prise de risque. Bon pour le brainstorming, les histoires, la poésie.

---

Souhaitez-vous que je vous montre également comment la **temperature interagit avec le `top_p` (échantillonnage du noyau)**, puisque les deux sont souvent disponibles dans les API Copilot/LLM ?