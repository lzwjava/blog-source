---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Couches de Validation d'API LLM Sécurisée
translated: true
type: note
---

Lorsque vous construisez ou utilisez une **API LLM**, vous souhaitez généralement des garde-fous pour garantir que les réponses sont sûres, valides et utiles. Voici les principales méthodes pour ajouter des vérifications :

---

### 1. **Validation des entrées**

* **Vérifications de schéma** : S'assurer que le JSON de la requête suit le schéma attendu avant de l'envoyer au LLM.
* **Assainissement du prompt** : Supprimer ou échapper les caractères indésirables, les instructions malveillantes ou les tentatives d'injection.
* **Vérifications de longueur** : Appliquer des limites maximales de tokens/caractères pour les entrées afin d'éviter des coûts inutiles ou une troncation.

---

### 2. **Validation de la sortie**

* **Validation de schéma JSON** : Si le LLM est censé renvoyer du JSON, l'exécuter via `json.loads()` et le valider par rapport à un schéma (par exemple, avec `pydantic`, `jsonschema`).
* **Vérifications par regex/format** : Pour les e-mails, les URLs ou les nombres, imposer des modèles.
* **Vérification de type** : Vérifier que les champs sont du bon type (chaîne, entier, liste, etc.).
* **Vérifications de plage** : S'assurer que les valeurs numériques ou de date sont dans les limites attendues.

---

### 3. **Vérifications de sécurité et de contenu**

* **Filtres de toxicité ou de profanité** : Faire passer la sortie dans un classifieur (par exemple, Perspective API, OpenAI moderation API).
* **Filtres politiques** : Définir des règles pour bloquer les réponses contenant certains mots-clés ou catégories.
* **Détection d'hallucination** : Ajouter des étapes de vérification des faits (via des vérifications augmentées par retrieval, une validation croisée par multiple modèles, ou des vérifications de cohérence basées sur des règles).

---

### 4. **Contraintes de logique métier**

* **Règles de cohérence** : Si la réponse doit correspondre aux données du système (par exemple, le solde de compte disponible, les valeurs de configuration), effectuer une contre-vérification avant de la renvoyer à l'utilisateur.
* **Garde-fous** : Utiliser des bibliothèques comme **Guardrails AI**, **LMQL** ou **Instructor** pour imposer de manière déclarative des sorties structurées et des contraintes.
* **Hooks de post-traitement** : Envelopper les réponses du LLM avec une logique personnalisée (normaliser la casse, imposer des valeurs par défaut, rejeter des réponses inattendues).

---

### 5. **Redondance et contre-vérification**

* **Prompts d'auto-vérification** : Demander au LLM de re-valider ou d'expliquer sa propre réponse.
* **Vérification par double modèle** : Utiliser un LLM plus petit/rapide pour vérifier la sortie du modèle principal (par exemple, "est-ce que cette réponse est conforme au schéma X ?").
* **Vote/consensus** : Exécuter plusieurs appels et comparer les réponses pour la stabilité.

---

### 6. **Sauvegardes opérationnelles**

* **Limites de débit** : Empêcher l'abus de l'API.
* **Délais d'expiration** : Interrompre les requêtes qui pendent.
* **Journalisation et pistes d'audit** : Conserver un enregistrement des requêtes et des réponses filtrées.
* **Solutions de repli** : Si la validation échoue, soit réessayer avec un prompt ajusté, soit renvoyer une valeur par défaut/erreur sûre.

---

👉 En pratique, une bonne pile d'API LLM superpose ces éléments :

1. Valider l'entrée.
2. Appeler le LLM.
3. Valider la sortie par rapport au schéma + règles métier.
4. Exécuter les filtres de sécurité/contenu.
5. Renvoyer uniquement si les vérifications passent (sinon réessayer/utiliser une solution de repli).

---

Souhaitez-vous que je vous montre un **exemple Python** où nous encapsulons un appel d'API LLM avec une validation de schéma JSON et des vérifications de modération ?