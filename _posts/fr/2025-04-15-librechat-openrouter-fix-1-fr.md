---
audio: false
generated: true
image: false
lang: fr
layout: post
model: mistralai/mistral-medium-3.1
title: Résolution de l'Erreur de Recherche Web LibreChat OpenRouter
translated: true
type: note
---

L'erreur **"404 No endpoints found that support tool use"** lors de l'utilisation de la fonction de recherche web dans LibreChat avec OpenRouter est un problème connu. Voici ce qui se passe et comment le résoudre :

---

## **Pourquoi cela arrive**
- **Tous les modèles sur OpenRouter ne prennent pas en charge les "tools" (comme la recherche web, l'appel de fonctions, etc.)** — seul un sous-ensemble les supporte. Si vous sélectionnez un modèle qui ne prend pas en charge les outils, vous obtiendrez cette erreur 404.
- OpenRouter vous oblige à **choisir explicitement un modèle qui prend en charge l'appel d'outils/fonctions** pour que des fonctionnalités comme la recherche web fonctionnent.
- La configuration de LibreChat peut également remplacer les endpoints si elle n'est pas configurée correctement, ce qui entraîne des problèmes de routage.

---

## **Comment le résoudre**

### 1. **Sélectionnez un modèle qui prend en charge les outils**
- Allez sur la [liste des modèles OpenRouter](https://openrouter.ai/models) et **filtrez par "tools"** dans la barre latérale. Seuls les modèles avec support des outils fonctionneront avec la fonction de recherche web de LibreChat.
- Modèles recommandés : Cherchez ceux étiquetés comme prenant en charge le "function calling" ou les "tools" (par exemple, certaines versions de GPT-4, Claude, ou d'autres modèles avancés).

### 2. **Mettez à jour la configuration de LibreChat**
- **N'utilisez pas `OPENROUTER_API_KEY`** dans votre configuration LibreChat, car cela pourrait remplacer l'endpoint OpenAI et causer des conflits.
- Dans `librechat.yaml`, assurez-vous que votre endpoint OpenRouter est correctement configuré et n'est pas bloqué par "Ignored Providers" ou restreint par "Allowed Providers".

### 3. **Supprimez les restrictions de fournisseur**
- Dans les paramètres OpenRouter, **débloquez tous les "Ignored Providers"** et **videz les "Allowed Providers"** pour garantir que LibreChat puisse accéder à tous les endpoints disponibles.

### 4. **Redémarrez LibreChat**
- Après avoir effectué ces modifications, redémarrez LibreChat pour appliquer les nouveaux paramètres.

---

## **Toujours pas de résultat ?**
- Consultez la [documentation LibreChat sur les endpoints personnalisés](https://www.librechat.ai/docs/quick_start/custom_endpoints) pour une configuration avancée.
- Si le problème persiste, essayez de passer à l'API OpenAI officielle (si vous y avez accès) ou à un autre fournisseur qui prend en charge l'utilisation d'outils.