---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Configuration de Codex CLI pour OpenRouter
translated: true
type: note
---

### Configuration de Codex CLI pour OpenRouter

Codex CLI (d'OpenAI) est un agent de codage en ligne de commande qui prend en charge des fournisseurs de modèles personnalisés comme OpenRouter via son fichier de configuration. OpenRouter fournit une API compatible avec OpenAI, vous pouvez donc router les requêtes via OpenRouter en définissant un fournisseur avec l'URL de base appropriée. Cela permet d'accéder à un plus large éventail de modèles (par exemple, d'Anthropic, Google ou des fournisseurs open source) tout en utilisant Codex.

La configuration est stockée dans un fichier TOML à l'emplacement `~/.codex/config.toml` (créez-le s'il n'existe pas). Vous allez définir une section **fournisseur de modèle** pour OpenRouter, puis y faire référence dans un **profil** pour des modèles spécifiques.

#### Étape 1 : Obtenir votre clé API OpenRouter
- Inscrivez-vous sur [openrouter.ai](https://openrouter.ai) si ce n'est pas déjà fait.
- Générez une clé API depuis votre tableau de bord.
- Définissez-la comme variable d'environnement :  
  ```
  export OPENROUTER_API_KEY=votre_clé_api_ici
  ```
  Ajoutez cette ligne à votre profil de shell (par exemple, `~/.bashrc` ou `~/.zshrc`) pour la rendre persistante.

#### Étape 2 : Modifier le fichier de configuration
Ouvrez `~/.codex/config.toml` dans votre éditeur et ajoutez les sections suivantes. Ceci définit l'URL de base sur le point de terminaison d'OpenRouter (`https://openrouter.ai/api/v1`), qui est compatible avec OpenAI (Codex ajoute automatiquement `/chat/completions`).

```toml
# Définir le fournisseur OpenRouter
[model_providers.openrouter]
name = "OpenRouter"
base_url = "https://openrouter.ai/api/v1"
env_key = "OPENROUTER_API_KEY"  # Lit la variable d'env pour l'authentification

# Définir un profil utilisant ce fournisseur (exemple : utilisation d'un modèle de type GPT)
[profiles.openrouter-gpt]
model_provider = "openrouter"
model = "openai/gpt-4o-mini"  # Remplacez par n'importe quel ID de modèle OpenRouter, par ex. "anthropic/claude-3.5-sonnet"
```

- **Champs clés expliqués** :
  - `base_url` : Pointe vers le point de terminaison de l'API OpenRouter. Cela remplace l'URL de base OpenAI par défaut.
  - `env_key` : Spécifie la variable d'environnement pour l'en-tête d'authentification Bearer token.
  - `model` : Utilisez les ID de modèles exacts de la [liste des modèles OpenRouter](https://openrouter.ai/models). Pour les tâches de codage, essayez "openai/codex-mini-latest" ou "meta-llama/llama-3.1-405b-instruct".
  - Vous pouvez ajouter plusieurs profils pour différents modèles (par exemple, `[profiles.openrouter-claude]` avec `model = "anthropic/claude-3.5-sonnet"`).

#### Étape 3 : Utiliser la configuration
- Installez Codex CLI si nécessaire : `npm install -g @openai/codex` (ou via Homebrew : `brew install codex`).
- Exécutez Codex avec votre profil :  
  ```
  codex --profile openrouter-gpt
  ```
  Ou définissez un profil par défaut dans la configuration :  
  ```toml
  [default_profile]
  name = "openrouter-gpt"
  ```
- Testez-le : Exécutez `codex` et donnez-lui une invite de codage simple. Vérifiez le tableau de bord d'OpenRouter pour l'utilisation.

#### Dépannage
- **Erreurs d'authentification** : Assurez-vous que `OPENROUTER_API_KEY` est définie et exportée.
- **Modèle non trouvé** : Vérifiez l'ID du modèle sur OpenRouter — il est sensible à la casse et préfixé (par exemple, "fournisseur/nom-du-modèle").
- **Vérification de la version** : Utilisez Codex CLI v0.13+ pour une prise en charge complète des fournisseurs. Mettez à jour avec `npm update -g @openai/codex`.
- **Routage avancé** : Pour les fonctionnalités spécifiques à OpenRouter comme le routage optimisé par le coût, ajoutez des paramètres optionnels comme `provider = { sort = "price" }` sous le profil (pris en charge dans les versions plus récentes).

Cette configuration maintient la compatibilité de vos requêtes avec l'API de style OpenAI de Codex tout en tirant parti de l'écosystème d'OpenRouter. Pour plus de détails, consultez la [documentation de Codex CLI sur npm](https://www.npmjs.com/package/@openai/codex) ou le [guide de l'API d'OpenRouter](https://openrouter.ai/docs). Si vous utilisez un fork comme Open Codex, la configuration est similaire mais peut avoir un support supplémentaire pour Gemini.