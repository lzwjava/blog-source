---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Mise à jour d'août 2025 de Visual Studio Code
translated: true
type: note
---

### Visual Studio Code 1.104 (Août 2025)

Cette version se concentre principalement sur les améliorations de l'IA pour GitHub Copilot, une sécurité renforcée pour les outils d'IA et des gains de productivité dans l'éditeur et le terminal. Voici un résumé des principales mises à jour :

#### Fonctionnalités IA
- **Sélection Automatique du Modèle (Aperçu)** : La discussion choisit automatiquement le meilleur modèle (par exemple, Claude Sonnet 4, variantes GPT-5) en fonction des performances et des limites de débit lorsque "Auto" est sélectionné ; inclut une remise de 10 % sur les requêtes pour les utilisateurs payants.
- **Confirmer les Modifications des Fichiers Sensibles** : Le mode Agent nécessite l'approbation de l'utilisateur avant de modifier les fichiers système, les dotfiles ou tout élément en dehors de l'espace de travail ; personnalisable via les paramètres.
- **Prise en charge des Fichiers AGENTS.md (Expérimental)** : Intègre automatiquement le fichier `AGENTS.md` de l'espace de travail comme contexte pour les requêtes de discussion.
- **Collaboration Améliorée des Agents de Codage (Expérimental)** : Meilleure gestion des sessions, intégration GitHub et délégation à partir des commentaires TODO ou de la discussion.
- **Approbation Automatique du Terminal** : Option pour une exécution plus sûre des commandes avec des avertissements pour les actions risquées comme `curl` ou `wget` ; nouvelles règles pour les approbations.
- **Rendu Mathématique** : Les équations KaTeX sont maintenant rendues en ligne par défaut dans les réponses de la discussion.
- **Outil #codebase Amélioré** : Utilise un nouveau modèle d'incorporations pour une recherche sémantique de code plus rapide et plus efficace.
- **Désactiver les Fonctionnalités IA** : Nouveau paramètre pour masquer et désactiver la discussion Copilot, les complétions et les suggestions globalement ou par espace de travail.
- **Outils IA Spécifiques à Python (Expérimental/Aperçu)** : Résumés contextuels alimentés par l'IA pour les symboles non documentés et un outil "Exécuter l'Extrait de Code" pour une exécution en mémoire.

#### Sécurité
- **Protections des Outils IA** : Confirmations étendues pour les modifications sensibles, les commandes du terminal et les approbations automatiques globales, avec des avertissements et des règles configurables pour atténuer les risques.
- **Documentation** : Nouveaux conseils sur les considérations de sécurité pour le développement assisté par l'IA.

#### Productivité
- **Valeurs par Défaut de la Vue de Discussion** : La discussion s'ouvre maintenant par défaut dans la Barre Latérale Secondaire ; visibilité personnalisable.
- **Améliorations du Terminal** : Meilleure IntelliSense (par exemple, complétions git, icônes), défilement collant et actions dans les éditeurs/fenêtres du terminal.
- **Environnements Python** : Prise en charge améliorée de Pipenv, injection de variables d'environnement depuis les fichiers `.env` et IntelliSense complète dans tous les documents Python.
- **Ajustements de l'Éditeur** : Délai configurable des suggestions en ligne, index des onglets pour la navigation au clavier et couleurs des bordures de fenêtre sur Windows.
- **Demandes de Tirage GitHub** : Barre latérale rétractable, actions TODO pour Copilot et options d'ignorer les sous-modules.
- **Prise en charge des Tâches et du Terminal** : Gestion améliorée des entrées, affichage des erreurs et délais d'expiration de l'intégration du shell.

#### Autres Changements Notables
- **Accessibilité** : Commande de focus pour les confirmations de discussion pour aider les lecteurs d'écran.
- **Langages** : Suppression de l'IntelliSense intégrée pour Bower.json (outil obsolète ; migrer vers npm/yarn).
- **Création d'Extensions** : APIs proposées pour les défis d'authentification et les contributions à la barre latérale secondaire.
- **Obsolescences** : Paramètres comme `chat.mcp.enabled` migrés ; support de Bower abandonné.

Pour plus de détails, consultez les notes de version officielles.

[Août 2025 (version 1.104)](https://code.visualstudio.com/updates/v1_104)