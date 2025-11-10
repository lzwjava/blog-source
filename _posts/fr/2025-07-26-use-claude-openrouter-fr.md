---
audio: false
generated: true
lang: fr
layout: post
title: Accéder à Claude via OpenRouter
translated: true
type: note
---

### Comment utiliser les modèles Claude avec OpenRouter (en tant qu'utilisateur chinois sans accès à l'API Anthropic)

En tant qu'utilisateur chinois, vous pouvez rencontrer des restrictions pour accéder directement à l'API Claude d'Anthropic en raison de blocages régionaux. Cependant, OpenRouter est une alternative fiable qui agit comme une passerelle API unifiée vers plusieurs fournisseurs d'IA, y compris les modèles Claude d'Anthropic. OpenRouter est accessible en Chine (le site web et les points de terminaison API ne sont pas bloqués), vous permettant de router les requêtes vers Claude sans avoir besoin d'un compte Anthropic direct ou d'une clé API. C'est un service payant à l'utilisation (vous devrez ajouter un moyen de paiement), mais l'inscription est gratuite et il prend en charge un niveau gratuit pour une utilisation limitée.

L'API d'OpenRouter est compatible avec le format d'OpenAI, vous pouvez donc utiliser des bibliothèques familières comme le SDK Python d'OpenAI. Ci-dessous, je décrirai les étapes pour commencer et fournirai des exemples de code pour utiliser Claude en Python.

#### Étape 1 : S'inscrire sur OpenRouter
1. Visitez le site web d'OpenRouter : https://openrouter.ai.
2. Cliquez sur "Sign Up" ou "Get Started" (généralement en haut à droite).
3. Créez un compte en utilisant votre email (ou via GitHub/Google si disponible). Aucun VPN n'est nécessaire, car le site fonctionne en Chine.
4. Après l'inscription, vérifiez votre email si nécessaire.
5. Allez dans le tableau de bord et ajoutez un moyen de paiement (par exemple, une carte de crédit) pour financer votre compte. OpenRouter facture en fonction de l'utilisation de tokens, mais vous pouvez commencer avec un petit dépôt. Consultez leur page de tarification pour les détails sur les modèles Claude.

#### Étape 2 : Générer une clé API
1. Dans votre tableau de bord OpenRouter, naviguez vers la section "API Keys" ou "Keys".
2. Créez une nouvelle clé API (elle ressemblera à une longue chaîne, par exemple `sk-or-v1-...`).
3. Copiez-la et sauvegardez-la en lieu sûr — traitez-la comme un mot de passe. Vous l'utiliserez dans votre code à la place d'une clé Anthropic.

#### Étape 3 : Choisir un modèle Claude
OpenRouter liste les modèles Claude d'Anthropic avec des ID comme :
- `anthropic/claude-3.5-sonnet` (recommandé pour la plupart des tâches ; équilibré et capable).
- `anthropic/claude-3-opus` (plus puissant mais plus cher).
- Les versions plus récentes (par exemple, Claude 3.7 si disponible en 2025) seront listées sur https://openrouter.ai/models?providers=anthropic.

Vous pouvez parcourir la page des modèles pour voir les coûts, les limites de contexte et la disponibilité.

#### Étape 4 : Configurer votre environnement
- Installez Python si vous ne l'avez pas (version 3.8+ recommandée).
- Installez la bibliothèque OpenAI : Exécutez `pip install openai` dans votre terminal.

#### Étape 5 : Utiliser Claude dans le code
Utilisez le SDK OpenAI avec l'URL de base d'OpenRouter (`https://openrouter.ai/api/v1`). Spécifiez l'ID du modèle Claude dans vos requêtes.

Voici un exemple Python simple pour discuter avec Claude 3.5 Sonnet :

```python
from openai import OpenAI

# Initialiser le client avec le point de terminaison d'OpenRouter et votre clé API
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="VOTRE_CLÉ_API_OPENROUTER_ICI",  # Remplacez par votre vraie clé
)

# Faire une requête à Claude
completion = client.chat.completions.create(
    model="anthropic/claude-3.5-sonnet",  # Utilisez l'ID du modèle Claude
    messages=[
        {"role": "system", "content": "Vous êtes un assistant utile."},
        {"role": "user", "content": "Bonjour, quelle est la capitale de la Chine ?"}
    ],
    temperature=0.7,  # Optionnel : Ajustez pour la créativité (0-1)
    max_tokens=150    # Optionnel : Limitez la longueur de la réponse
)

# Imprimer la réponse
print(completion.choices[0].message.content)
```

- **Explication** : Ceci envoie une invite système et un message utilisateur à Claude, obtient une réponse et l'imprime. Remplacez la clé API et ajustez les paramètres selon les besoins.
- **Si vous préférez les requêtes HTTP brutes** (sans la bibliothèque OpenAI) :

```python
import requests
import json

response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": "Bearer VOTRE_CLÉ_API_OPENROUTER_ICI",
        "Content-Type": "application/json"
    },
    data=json.dumps({
        "model": "anthropic/claude-3.5-sonnet",
        "messages": [
            {"role": "system", "content": "Vous êtes un assistant utile."},
            {"role": "user", "content": "Bonjour, quelle est la capitale de la Chine ?"}
        ]
    })
)

# Analyser et imprimer la réponse
data = response.json()
print(data['choices'][0]['message']['content'])
```

- **Conseils** :
  - Ajoutez des en-têtes optionnelles comme `"HTTP-Referer": "votre-url-de-site"` et `"X-Title": "Le nom de votre application"` pour attribuer l'utilisation (aide pour les classements et les crédits gratuits potentiels).
  - Surveillez l'utilisation dans votre tableau de bord OpenRouter pour éviter des coûts inattendus.
  - Pour les réponses en streaming ou les fonctionnalités avancées (par exemple, les outils), référez-vous à la documentation complète d'OpenRouter.
  - Si vous rencontrez des limites de débit ou des erreurs, vérifiez votre solde ou essayez un autre modèle.

#### Dépannage
- **Erreurs d'API** : Assurez-vous que votre clé est correcte et financée. Testez d'abord avec un modèle peu coûteux.
- **Problèmes régionaux** : Si des blocages se produisent (peu probable), utilisez un VPN, mais OpenRouter est conçu pour contourner ces restrictions pour les modèles pris en charge.
- **Alternatives gratuites** : Pour un accès gratuit limité, explorez les proxys comme Puter.js (mais ils peuvent avoir des limitations).

Cette configuration vous permet d'utiliser Claude de manière programmatique sans accès direct à Anthropic. Si vous avez besoin d'une intégration avec des outils spécifiques (par exemple, Cursor IDE ou Make.com), recherchez des tutoriels à leur sujet.

Références :  
[Documentation OpenRouter](https://openrouter.ai/docs)  
[Anthropic Claude sur OpenRouter](https://openrouter.ai/anthropic/claude-3.5-sonnet)  
[Utiliser OpenRouter en Chine](https://medium.com/ai-simplified-in-plain-english/not-re-inventing-the-wheel-in-ai-2ec3e76ae2bd)  
[Comment utiliser Claude en Chine](https://www.comparitech.com/blog/vpn-privacy/how-to-use-claude-in-china/)