---
audio: false
generated: true
image: false
lang: fr
layout: post
model: mistralai/mistral-medium-3.1
title: Résolution de l'Erreur de Modèle LibreChat OpenRouter
translated: true
type: note
---

Cette erreur se produit lors de l'utilisation de **LibreChat** avec **OpenRouter** comme backend, et que le modèle sélectionné (`gpt-5-chat` ou similaire) n'est pas disponible ou n'est pas correctement routé. Voici une explication du problème et comment le résoudre :

---

## **Pourquoi cette erreur se produit**
- **OpenRouter** agit comme un proxy vers divers modèles d'IA, mais tous les modèles ne sont pas disponibles ou activés par défaut.
- L'erreur `404 Aucun point de terminal trouvé prenant en charge l'utilisation d'outils` signifie que le modèle que vous avez sélectionné (`gpt-5-chat`) est soit :
  - Non pris en charge par OpenRouter.
  - Non configuré dans votre installation LibreChat.
  - Nécessite un autre fournisseur ou une autre clé API.

---

## **Comment la résoudre**

### 1. **Vérifier les modèles disponibles dans OpenRouter**
- Visitez [la liste des modèles d'OpenRouter](https://openrouter.ai/models) pour voir quels modèles sont disponibles.
- Actuellement, `gpt-5-chat` n'est pas un modèle officiel d'OpenAI (le dernier est GPT-4o). Si vous pensiez à GPT-4, utilisez `openai/gpt-4` ou similaire.

### 2. **Mettre à jour la configuration de LibreChat**
- Dans LibreChat, allez dans **Paramètres** > **Sélection du modèle**.
- Choisissez un modèle qui est **pris en charge par OpenRouter** (par exemple, `openai/gpt-4`, `mistralai/mistral-7b`, etc.).
- Si vous souhaitez utiliser OpenAI directement, changez le **Fournisseur d'API** pour **OpenAI** au lieu d'OpenRouter.

### 3. **Vérifier les clés API**
- Assurez-vous d'avoir une **clé API OpenRouter** valide (si vous utilisez OpenRouter) ou une **clé API OpenAI** valide (si vous utilisez OpenAI).
- Ajoutez la clé dans **Paramètres** > **Clés API** de LibreChat.

### 4. **Redémarrer LibreChat**
- Après avoir modifié les paramètres, redémarrez LibreChat pour appliquer les changements.

### 5. **Consulter la documentation de LibreChat**
- Référez-vous au [guide d'installation OpenRouter de LibreChat](https://github.com/danny-avila/LibreChat#openrouter) pour des instructions détaillées.

---

## **Solutions alternatives**
- Si vous souhaitez utiliser les modèles d'OpenAI, définissez le fournisseur sur **OpenAI** et sélectionnez `gpt-4`, `gpt-4o` ou `gpt-3.5-turbo`.
- Si vous souhaitez utiliser OpenRouter, choisissez un modèle dans leur [liste des modèles pris en charge](https://openrouter.ai/models).

---