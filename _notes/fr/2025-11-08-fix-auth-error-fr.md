---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Correction de l'erreur d'authentification de l'API de traduction
translated: true
---

### Analyse du flux de travail et cause de l'erreur

Votre flux de travail GitHub Actions pour "Translate Recent Notes" semble globalement bien structuré — il vérifie le dépôt, configure Python, installe les dépendances, exécute un script de traduction sur les N notes les plus récentes et valide les modifications dans `_notes/`. Cependant, d'après les journaux que vous avez partagés précédemment (avec les erreurs 401 lors de la traduction vers des langues comme ar, de, fr, etc.), le problème se situe au niveau de l'authentification pour les appels d'API de traduction dans le script `scripts/translation/update_lang_notes.py`.

#### Cause racine
- L'erreur `"No cookie auth credentials found"` (HTTP 401) est spécifique à l'**API OpenRouter** (ou à un client/bibliothèque Python interagissant avec elle, comme LiteLLM ou un SDK non officiel). Cela se produit lorsque la requête API manque les en-têtes d'authentification appropriés.
- OpenRouter attend `Authorization: Bearer <votre_clé_api_openrouter>` dans les requêtes. Si la clé n'est pas transmise correctement, certains clients reviennent à (ou interprètent à tort comme nécessitant) une authentification par cookie de session, déclenchant cette erreur exacte.
- Dans votre flux de travail :
  - Vous définissez `OPENROUTER_API_KEY: ${{ secrets.DEEPSEEK_API_KEY }}`, ce qui transmet une valeur secrète à l'environnement du script.
  - Mais le script ne lit/n'utilise probablement pas correctement cette variable d'environnement. Les incompatibilités courantes sont :
    - Le script attend `OPENAI_API_KEY` (pour les points de terminaison compatibles OpenAI comme OpenRouter).
    - Ou il utilise une bibliothèque (par exemple, le SDK Python `openai`) sans définir l'URL de base sur `https://openrouter.ai/api/v1`.
    - Le secret `DEEPSEEK_API_KEY` pourrait en réalité contenir votre **clé API OpenRouter** (routée vers les modèles DeepSeek/Grok), mais s'il s'agit d'une clé DeepSeek directe, elle ne fonctionnera pas pour OpenRouter.
- D'après les journaux, le script utilise le modèle `'x-ai/grok-4-fast'` (Grok 4 via OpenRouter), et il traite avec succès le front matter/les titres mais échoue sur la traduction du contenu par langue.
- Ce n'est pas un problème GitHub Actions — il se situe dans la configuration du client API du script Python. Le flux de travail continue jusqu'à l'étape de validation (d'où le journal `git config user.name "github-actions[bot]"`), mais sans les traductions, seuls les fichiers anglais sont ajoutés.

#### Correctifs recommandés
1. **Mettre à jour les variables d'environnement dans le flux de travail** :
   - Alignez-vous sur les configurations courantes d'OpenRouter (compatible OpenAI). Modifiez le bloc `env` dans l'étape "Translate posts" comme suit :
     ```
     env:
       GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
       OPENAI_API_KEY: ${{ secrets.DEEPSEEK_API_KEY }}  # Renommer la variable selon ce qu'attend le script
       OPENAI_BASE_URL: https://openrouter.ai/api/v1   # Requis pour le routage vers OpenRouter
     ```
   - Si `DEEPSEEK_API_KEY` est votre clé OpenRouter, parfait. Si c'est une clé DeepSeek directe, créez un nouveau secret `OPENROUTER_API_KEY` dans les paramètres du dépôt avec votre véritable clé OpenRouter (obtenez-en une sur [openrouter.ai/keys](https://openrouter.ai/keys)).
   - Test : Ajoutez `echo $OPENAI_API_KEY` (masqué) à l'étape d'exécution pour le débogage dans les journaux.

2. **Corriger le script Python (`update_lang_notes.py`)** :
   - Assurez-vous qu'il initialise le client OpenAI comme ceci (en supposant la bibliothèque `openai`) :
     ```python
     import os
     from openai import OpenAI

     client = OpenAI(
         api_key=os.getenv("OPENAI_API_KEY"),
         base_url=os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")  # Retourne par défaut vers OpenAI si non défini
     )

     # Puis utilisez client.chat.completions.create(..., model="x-ai/grok-4-fast")
     ```
   - Si vous utilisez LiteLLM (courant pour les multi-fournisseurs) : Installez-la si elle n'est pas dans `requirements.txt`, et appelez `completion(model="openrouter/x-ai/grok-4-fast", api_key=os.getenv("OPENAI_API_KEY"), api_base="https://openrouter.ai/api/v1", ...)`.
   - Pour la boucle de traduction : Ajoutez la gestion des erreurs par langue (par exemple, `try/except` autour des appels API, journalisez les échecs, ignorez en cas de 401).
   - Gérer explicitement les cookies ? Probablement pas nécessaire — utilisez les clés API. Si le script contient du code navigateur/Selenium, supprimez-le pour la fiabilité de l'intégration continue.

3. **Améliorations du flux de travail** :
   - **Validation des entrées** : Ajoutez une vérification pour N=0 ou `--n` invalide pour éviter de ne rien traiter.
   - **Validation conditionnelle** : Votre `git diff --cached --quiet || git commit` est bon, mais mettez à jour le message pour refléter toutes les langues : `-m "Add translated posts (ar, de, es, fr, hi, ja, zh, hant)"`.
   - **Mise en cache** : Ajoutez `actions/cache` pour `pip` afin d'accélérer les installations.
   - **Mode débogage** : Ajoutez une entrée optionnelle `debug: true` et un drapeau `--debug` au script pour une journalisation détaillée.
   - **Permissions** : Assurez-vous que l'environnement `github-pages` a un accès en lecture/écriture si nécessaire.
   - Extrait YAML mis à jour complet pour l'étape "Translate posts" :
     ```
     - name: Translate posts
       run: |
         python scripts/translation/update_lang_notes.py --n ${{ inputs.n }}
       env:
         GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
         OPENAI_API_KEY: ${{ secrets.DEEPSEEK_API_KEY }}
         OPENAI_BASE_URL: https://openrouter.ai/api/v1
     ```

4. **Étapes de test** :
   - **Test local** : Exécutez `python scripts/translation/update_lang_notes.py --n 1` localement avec les variables d'environnement exportées (par exemple, `export OPENAI_API_KEY=votre_clé`).
   - **Test du flux de travail** : Déclenchez-le avec `workflow_dispatch` et N=1, vérifiez les journaux pour les appels API.
   - **Vérifier le secret** : Dans les paramètres du dépôt > Secrets, confirmez que `DEEPSEEK_API_KEY` contient une clé OpenRouter valide (commençant par `sk-or-...`).
   - Si cela échoue toujours, ajoutez `--verbose` au script et inspectez les en-têtes des requêtes (par exemple, via `print(client.api_key)`).

Cela devrait résoudre les erreurs 401 et permettre aux traductions de fonctionner. Si vous partagez des extraits de `update_lang_notes.py` (par exemple, l'initialisation du client API), je peux identifier plus précisément.

#### Références
- [Démarrage rapide OpenRouter (Configuration de l'authentification API)](https://openrouter.ai/docs/quickstart)
- [Intégration LiteLLM OpenRouter](https://docs.litellm.ai/docs/providers/openrouter) (si utilisé)
- [Problème GitHub sur une erreur d'authentification OpenRouter similaire](https://github.com/mendableai/firecrawl/issues/1352)
- [Fil de discussion Reddit sur les erreurs 401 OpenRouter](https://www.reddit.com/r/openrouter/comments/1oqiaol/error_401_no_cookie_auth_credentials_found/)