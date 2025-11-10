---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Utilisation d'outils contre appel de fonction expliqué
translated: true
type: note
---

Décomposons la différence entre **l'utilisation d'outils (tool use)** et **l'appel de fonctions (function calling)** dans le contexte des API de LLM :

---

## 1. Utilisation d'outils (Tool Use)

* **Concept** : L'utilisation d'outils est un concept large où le LLM est augmenté par des capacités externes. Au lieu de simplement générer du texte, il peut « utiliser un outil » pour récupérer des informations, exécuter du code, interroger une base de données ou générer une image.
* **Implémentation** : En pratique, les « outils » sont des API ou systèmes externes enregistrés auprès de l'environnement d'exécution du LLM (par exemple, une API de recherche, un environnement d'exécution Python ou une API de calendrier).
* **Rôle du LLM** : Le modèle décide quand appeler l'outil, avec quels arguments, et intègre les résultats dans la conversation.
* **Exemple** :

  * Utilisateur : « Quel temps fait-il à Guangzhou ? »
  * LLM : Appelle l'outil `weather` avec `{city: "Guangzhou"}` → obtient `28°C, ensoleillé`.
  * LLM : Répond : « Il fait 28°C et il fait beau. »

Considérez **l'utilisation d'outils** comme un cadre d'orchestration général où le LLM ne se contente pas de répondre avec des mots – il coordonne des actions avec des systèmes externes.

---

## 2. Appel de fonctions (Function Calling)

* **Concept** : L'appel de fonctions est un mécanisme *structuré* fourni par certaines API de LLM (comme OpenAI, Anthropic, etc.), où vous définissez des fonctions (avec des noms, paramètres, schémas), et le LLM peut renvoyer des arguments JSON pour les appeler.
* **Implémentation** : Vous fournissez au modèle des schémas JSON décrivant les fonctions. La sortie du modèle est ensuite soit du texte, soit un objet d'appel de fonction structuré.
* **Rôle du LLM** : Au lieu de « halluciner » l'utilisation d'une API, le modèle produit des arguments structurés valides pour des fonctions prédéfinies.
* **Exemple** :

  * Vous définissez une fonction :

    ```json
    {
      "name": "getWeather",
      "description": "Obtenir la météo actuelle",
      "parameters": {
        "type": "object",
        "properties": {
          "city": {"type": "string"}
        },
        "required": ["city"]
      }
    }
    ```
  * Utilisateur : « Quel temps fait-il à Guangzhou ? »
  * LLM : Produit → `{ "name": "getWeather", "arguments": {"city": "Guangzhou"} }`
  * Votre système exécute la fonction et renvoie les résultats.

Cela fait de **l'appel de fonctions** une manière spécifique, sûre et pilotée par schéma de réaliser **l'utilisation d'outils**.

---

## 3. Différences Clés

* **Portée** :

  * Utilisation d'outils = concept général (LLM augmenté par des systèmes externes).
  * Appel de fonctions = une conception d'API standardisée spécifique pour les appels structurés.
* **Contrôle** :

  * L'utilisation d'outils peut être plus libre (le LLM décide et formate).
  * L'appel de fonctions impose des schémas stricts, réduisant l'ambiguïté et les hallucinations.
* **Interopérabilité** :

  * L'utilisation d'outils peut impliquer de nombreux systèmes externes (recherche, exécution de code, génération d'image).
  * L'appel de fonctions est préférable lorsque vous voulez des arguments précis et structurés (comme pour les API ou les requêtes de base de données).

---

## 4. Modèle Mental

* L'appel de fonctions est un **sous-ensemble** de l'utilisation d'outils.
* Si l'utilisation d'outils est la *stratégie générale*, l'appel de fonctions est la *méthode sûre et structurée* que la plupart des API exposent.

---

Souhaitez-vous que je vous montre également **un exemple de workflow côte à côte** (comme requête utilisateur → sortie LLM → exécution) pour illustrer la différence de manière plus concrète ?