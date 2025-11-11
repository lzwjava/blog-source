---
audio: false
generated: true
lang: fr
layout: post
title: Extension Copilot pour Visual Studio Code
translated: true
type: note
---

Non, le plugin Copilot de Visual Studio Code (VSCode) ne peut pas utiliser une clé API personnalisée, telle que votre clé Gemini. GitHub Copilot, développé par GitHub (détenu par Microsoft), est un outil de complétion de code alimenté par l'IA, étroitement intégré à l'infrastructure de GitHub et à des modèles d'IA spécifiques, initialement basé sur Codex d'OpenAI. Il repose sur une authentification via un compte GitHub et un abonnement Copilot, et il n'offre pas d'option intégrée pour le configurer avec des clés API personnalisées provenant d'autres fournisseurs, comme Gemini de Google.

Cependant, puisque vous disposez d'une clé Gemini, il existe des alternatives pour l'utiliser dans VSCode :

- **Gemini Code Assist** : Google propose un assistant de codage alimenté par l'IA appelé Gemini Code Assist, qui dispose d'une extension officielle pour VSCode. Cette extension est conçue pour fonctionner avec les modèles Gemini de Google et permet probablement de saisir votre clé API Gemini pour l'authentification. Vous pouvez installer cette extension depuis le Marketplace de VSCode et la configurer avec votre clé pour obtenir des complétions de code propulsées par Gemini.

- **Plugins tiers** : Il peut également exister d'autres extensions VSCode tierces disponibles dans le Marketplace qui prennent en charge plusieurs fournisseurs d'IA et vous permettent d'utiliser des clés API personnalisées, y compris pour Gemini. Ces plugins vous permettraient de vous connecter à l'API Gemini pour obtenir des suggestions de code, bien qu'ils puissent nécessiter une configuration supplémentaire.

### Pourquoi Copilot ne prend pas en charge les clés personnalisées
GitHub Copilot est un outil propriétaire optimisé pour son propre écosystème. Bien que des développements récents aient vu GitHub s'associer à Google pour intégrer les modèles Gemini dans Copilot, cette intégration est gérée par GitHub et ne permet pas aux utilisateurs de saisir directement leurs propres clés API Gemini. Au lieu de cela, l'accès à tout modèle pris en charge (y compris Gemini, le cas échéant) est fourni par le service Copilot lui-même, sous le contrôle de GitHub.

### Recommandation pratique
Si votre objectif est d'utiliser votre clé Gemini dans VSCode, l'installation de **l'extension Gemini Code Assist** est l'option la plus directe et officiellement prise en charge. Voici comment procéder :

1. Ouvrez VSCode.
2. Accédez à la vue Extensions (`Ctrl+Shift+X` ou `Cmd+Shift+X` sur macOS).
3. Recherchez "Gemini Code Assist" (ou consultez la documentation officielle de Google pour le nom exact).
4. Installez l'extension et suivez ses instructions de configuration pour saisir votre clé API Gemini.

Cette approche garantit que vous utilisez l'outil comme prévu, en évitant les problèmes potentiels tels que la violation des conditions d'utilisation ou la gestion de modifications non prises en charge de Copilot.

En résumé, bien que le plugin Copilot de VSCode lui-même ne puisse pas utiliser votre clé Gemini, vous pouvez toujours atteindre votre objectif d'utiliser Gemini dans VSCode en optant pour l'extension Gemini Code Assist ou un plugin tiers compatible.