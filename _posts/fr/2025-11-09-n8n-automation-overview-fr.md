---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Présentation de la Plateforme d'Automatisation des Flux de Travail N8N
translated: true
type: note
---

n8n (prononcé "n-eight-n") est une plateforme open source d'automatisation de workflows conçue pour les équipes techniques et les développeurs. Elle vous permet de connecter différentes applications, services et API pour automatiser les tâches répétitives, les flux de données et les processus complexes sans dépendre massivement du code personnalisé — bien qu'elle prenne en charge le code lorsque cela est nécessaire. Considérez-la comme une alternative auto-hébergée à des outils comme Zapier ou Make, mais avec plus de flexibilité, incluant la capacité à créer des agents IA multi-étapes, à intégrer n'importe quel grand modèle de langage (LLM), et à exécuter le tout sur votre propre infrastructure pour une meilleure confidentialité et un meilleur contrôle des données.

Au cœur de n8n se trouve une interface visuelle basée sur des nœuds où les workflows sont construits en faisant glisser et en connectant des "nœuds" (des blocs de construction qui représentent des déclencheurs, des actions ou des transformations). Elle est sous licence fair-code (code source disponible sur GitHub), prend en charge plus de 400 intégrations pré-construites (par exemple, Google Sheets, Slack, OpenAI, GitHub), et peut gérer tout, des notifications simples aux automatisations avancées pilotées par l'IA comme la synthèse de tickets ou la génération de contenu.

### Fonctionnalités Clés
- **Constructeur de Workflow Visuel** : Glisser-déposer des nœuds pour des configurations sans code, avec des options pour intégrer JavaScript, Python, ou même des bibliothèques npm/Python pour une logique personnalisée.
- **Intégration IA** : Construisez des agents multi-étapes avec des outils comme LangChain, connectez-vous à n'importe quel LLM (local ou cloud), et créez des interfaces de chat pour interroger des données ou exécuter des tâches via Slack, SMS ou la voix.
- **Auto-hébergement & Sécurité** : Déploiement sur site complet via Docker ou npm ; prend en charge le SSO, les secrets chiffrés, le RBAC et les journaux d'audit. Pas de lock-in fournisseur — hébergez également vos propres modèles d'IA.
- **Développement Hybride** : Mélangez l'interface utilisateur avec le code ; rejouez les données pour les tests, journaux inline pour le débogage, et 1 700+ modèles pour des démarrages rapides.
- **Évolutivité** : Fonctionnalités entreprise comme l'historique des workflows, le contrôle de version Git, les environnements isolés et l'intégration pour les automatisations client.
- **Exemples de Performance** : Des entreprises comme Delivery Hero économisent 200+ heures mensuelles ; StepStone condense des semaines de travail en quelques heures.

Comparé à Zapier, n8n est plus adapté aux développeurs (accès au code, auto-hébergement), rentable (noyau gratuit, pas de frais par tâche) et axé sur la confidentialité (pas de données acheminées via des tiers). C'est idéal pour les équipes manipulant des données sensibles dans la finance, la santé ou les opérations internes.

# Comment Utiliser n8n : Guide Complet

Ce guide vous accompagne sur tout, de l'installation à l'utilisation avancée. Nous utiliserons un exemple pratique : un moniteur de flux RSS qui envoie par e-mail les nouveaux articles quotidiennement (pouvant être étendu à des résumés IA). Supposez un confort technique de base ; n8n s'exécute sur Node.js.

## 1. Installation et Configuration

n8n est léger et démarre rapidement. Prérequis : Node.js (v18+ recommandée) pour les installations locales ; Docker pour les conteneurs. Pour la production, utilisez un VPS comme DigitalOcean ou AWS.

### Démarrage Local Rapide (Développement/Test)
1. Ouvrez votre terminal.
2. Exécutez : `npx n8n`
   - Cela télécharge et lance n8n temporairement.
3. Accédez à l'éditeur à l'adresse `http://localhost:5678` dans votre navigateur.
   - Connexion par défaut : Aucun identifiant nécessaire initialement (définissez-les plus tard pour la sécurité).

### Installation Locale Persistante (npm)
1. Installez globalement : `npm install n8n -g`
2. Démarrez : `n8n start`
3. Accédez à `http://localhost:5678`.

### Docker (Recommandé pour la Production)
1. Tirez l'image : `docker run -it --rm --name n8n -p 5678:5678 -v ~/.n8n:/home/node/.n8n n8nio/n8n`
   - Cela mappe un volume pour la persistance des données.
2. Pour les configurations avancées (par exemple, base de données PostgreSQL) : Utilisez `docker-compose.yml` depuis la documentation.
3. Accédez à `http://localhost:5678`.

### Options Cloud
- **n8n Cloud** : Hébergement managé sur n8n.io — inscrivez-vous, déployez en quelques minutes, démarrage gratuit avec limites.
- **PaaS Tiers** : Utilisez Render, Railway ou Sevalla (modèles en un clic). Exemple sur Sevalla :
  1. Inscrivez-vous sur sevalla.com.
  2. Sélectionnez le modèle "n8n", déployez les ressources (par exemple, 1 CPU, 1GB RAM).
  3. Obtenez une URL comme `https://your-n8n.sevalla.app`.

**Conseils** : Pour l'auto-hébergement, sécurisez avec HTTPS (via un proxy inverse comme Nginx), définissez les variables d'environnement (par exemple, `N8N_BASIC_AUTH_ACTIVE=true`), et sauvegardez le dossier `~/.n8n`. Mettez à l'échelle avec le mode queue pour les workflows à volume élevé.

## 2. Aperçu de l'Interface Utilisateur

Une fois ouvert :
- **Canvas** : Espace de travail vide pour les workflows. Cliquez sur "+" pour ajouter des nœuds.
- **Panneau des Nœuds** : Bibliothèque consultable de 400+ nœuds (par exemple, "Schedule Trigger").
- **Panneau d'Exécution** : Montre le flux de données en temps réel pendant les tests.
- **Barre Latérale** : Paramètres du workflow, historique des exécutions, modèles.
- **Barre Supérieure** : Sauvegarder, activer/désactiver, options de partage/export.

Les workflows se sauvegardent automatiquement ; utilisez Git pour le contrôle de version en équipe.

## 3. Concepts de Base

- **Workflow** : Une séquence de nœuds connectés définissant la logique d'automatisation. Les workflows actifs s'exécutent sur des déclencheurs ; les inactifs sont pour les tests.
- **Nœuds** : Blocs modulaires :
  - **Déclencheurs** : Lancent les workflows (par exemple, Schedule pour les tâches cron, Webhook pour les événements HTTP, RSS Read pour les flux).
  - **Actions** : Effectuent le travail (par exemple, Send Email, HTTP Request pour les APIs, Function pour le code personnalisé).
  - **Nœuds de Base** : IF (conditionnels), Merge (combiner des données), Set (manipuler des variables).
- **Connexions** : Les flèches entre les nœuds montrent le flux de données (format JSON). Les données d'un nœud alimentent le suivant.
- **Expressions** : Espaces réservés dynamiques comme `{{ $json.title }}` pour extraire des données (par exemple, le titre d'un article) dans les champs. Utilisez `$now` pour les horodatages ou `$input.all()` pour les lots.
- **Identifiants** : Stockage sécurisé pour les clés API/OAuth. Définissez-les une fois par service (par exemple, OAuth Gmail) et réutilisez-les sur tous les nœuds.
- **Exécutions** : Lancements d'un workflow ; visualisez les journaux, rejouez les données ou déboguez les erreurs.

## 4. Créer Votre Premier Workflow : Étape par Étape

Construisons "E-mail de Résumé RSS Quotidien".

1. **Créer un Nouveau Workflow** :
   - Cliquez sur "New" > Nommez-le "RSS Digest".
   - Le Canvas s'ouvre.

2. **Ajouter un Nœud Déclencheur** :
   - Cliquez sur "+" > Recherchez "Schedule Trigger".
   - Configurez : Déclenchement "Every Day" à 9:00 AM (cron : `0 9 * * *`).
   - Testez : Cliquez sur "Execute Node" (s'exécute une fois maintenant).

3. **Ajouter un Nœud de Récupération de Données** :
   - Cliquez sur "+" après le déclencheur > "RSS Read".
   - URL : `https://blog.cloudflare.com/rss/`.
   - Exécutez : Récupère les éléments (par exemple, JSON avec title, link, pubDate).

4. **Transformer les Données (Nœud Function Optionnel)** :
   - "+" > "Function".
   - Code :
     ```
     // Limiter aux 3 premiers éléments
     return items.slice(0, 3);
     ```
   - Cela exécute du JS sur les données entrantes.

5. **Ajouter un Nœud d'Action** :
   - "+" > "Gmail" (ou "Email Send" pour SMTP).
   - Identifiants : Cliquez sur "Create New" > OAuth pour Gmail (suivez le flux d'authentification Google).
   - À : Votre e-mail.
   - Sujet : `Daily Digest: {{ $input.first().json.title }}`
   - Message : Boucle sur les éléments avec l'expression :
     ```
     {{#each $input.all()}}
     - {{ $json.title }}: {{ $json.link }} ({{ $json.pubDate }})
     {{/each}}
     ```
   - (Utilise une syntaxe de type Handlebars pour les boucles.)

6. **Connecter & Tester** :
   - Faites glisser les flèches : Déclencheur → RSS → Function → Email.
   - "Execute Workflow" : Observez le flux de données ; vérifiez la boîte de réception.
   - Corrigez les erreurs : Les nœuds rouges mettent en évidence les problèmes (par exemple, identifiants invalides).

7. **Activer** :
   - Basculez "Active" sur ON. Il s'exécute maintenant quotidiennement.

Sauvegardez et exportez en JSON pour le partage.

## 5. Construire des Workflows Plus Complexes

- **Conditionnels** : Ajoutez un nœud "IF" après RSS : `{{ $json.pubDate }} > {{ $now.minus({days:1}) }}` pour filtrer les nouveaux éléments.
- **Boucles & Lots** : Utilisez "Split In Batches" pour traiter de grands ensembles de données.
- **Gestion des Erreurs** : Ajoutez un workflow "Error Trigger" ou "IF" pour les nouvelles tentatives. Utilisez "Set" pour journaliser les erreurs.
- **Intégrations API** : Nœud "HTTP Request" pour les endpoints personnalisés (par exemple, POST vers un webhook Slack).
- **Manipulation de Données** : Nœuds "Edit Fields" ou Function pour ajuster le JSON.
- **Test** : Rejouez des exécutions spécifiques ; simulez des données dans les nœuds.

Exemple : Moniteur Twitter
1. Déclencheur : "Twitter Trigger" sur les mentions.
2. Nœud IA : "OpenAI" pour classer le sentiment.
3. IF : Positif → Ajout CRM ; Négatif → Alerte Slack.

## 6. Utilisation Avancée & Bonnes Pratiques

- **Workflows IA** : Ajoutez un nœud "AI Agent" > Enchaînez avec des outils (par exemple, recherche, synthèse). Intégrez des LLM locaux via le nœud "Ollama".
- **Nœuds Personnalisés** : Développez via JS (tutoriel de la documentation) ; publiez dans la communauté.
- **Mise à l'Échelle** : Utilisez le mode queue (`N8N_WORKER=1`), une base de données externe (PostgreSQL) et les webhooks pour le temps réel.
- **Sécurité** : Chiffrez les secrets, utilisez RBAC pour les équipes, journaux d'audit.
- **Débogage** : Journaux inline dans les Functions (`console.log(items)`) ; versionnez avec Git.
- **Pièges Courants** : Surveillez les types de données (tout JSON) ; gérez les limites de débit dans les nœuds ; commencez simplement avant l'IA.
- **Extensions** : Intégrez dans les applications, utilisez les modèles (1700+ disponibles), ou npm pour les extras.

Pour la production, surveillez via des outils externes ; l'auto-hébergement économise les coûts (contre 20 $/mois+ pour Zapier).

## Références
- [Site Officiel n8n](https://n8n.io/)
- [Documentation n8n - Installation](https://docs.n8n.io/hosting/installation/)
- [Guide Débutant freeCodeCamp](https://www.freecodecamp.org/news/a-beginners-guide-to-automation-with-n8n/)
- [Documentation n8n Workflows](https://docs.n8n.io/workflows/)
- [Medium : Guide Maîtriser n8n](https://medium.com/data-science-collective/mastering-n8n-from-scratch-a-step-by-step-guide-for-beginners-its-easier-than-you-think-2d7ca5d47277)
- [Wikipedia : n8n](https://en.wikipedia.org/wiki/N8n)