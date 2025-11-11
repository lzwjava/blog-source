---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Guide des Git Hooks Pré-commit Pré-push
translated: true
type: note
---

### Présentation des Git Hooks

Les Git hooks sont des scripts personnalisables qui automatisent des tâches à des moments spécifiques du flux de travail Git. Ils peuvent être côté client (exécutés sur votre machine locale) ou côté serveur (exécutés sur le dépôt distant). Les hooks sont stockés dans le répertoire `.git/hooks/` d'un dépôt. Ci-dessous, je vais détailler les hooks pre-commit, pre-push et les hooks côté serveur liés au push, en expliquant leur mode d'exécution.

### Hooks Côté Client : Pre-Commit et Pre-Push
Ces hooks s'exécutent localement sur votre machine avant que les actions ne soient finalisées, vous permettant d'appliquer des règles ou d'exécuter des vérifications.

- **Hook Pre-Commit** :
  - **Quand il s'exécute** : Déclenché automatiquement juste avant de valider les changements (par exemple, via `git commit`).
  - **Objectif** : Utile pour les vérifications de qualité de code, comme l'exécution de linters, de tests ou d'outils de formatage. Si le hook échoue (se termine avec un statut non nul), la validation est abandonnée.
  - **Exemple** : Un hook pre-commit exemple pourrait exécuter `eslint` sur les fichiers JavaScript. S'il y a des erreurs, la validation s'arrête.
  - **Fonctionnement** : Le script se trouve dans `.git/hooks/pre-commit`. Rendez-le exécutable avec `chmod +x .git/hooks/pre-commit`. Si vous utilisez des outils comme Husky (une bibliothèque populaire pour gérer les Git hooks), cela simplifie la configuration.

- **Hook Pre-Push** :
  - **Quand il s'exécute** : Déclenché automatiquement juste avant d'envoyer les changements vers un dépôt distant (par exemple, via `git push`).
  - **Objectif** : Vérifie des éléments comme l'exécution de tests, la vérification de la couverture de code ou la compatibilité avant d'envoyer les changements vers le dépôt distant. S'il échoue, le push est bloqué.
  - **Note sur "some prepush"** : Il n'existe pas de hook "prepush" standard dans Git – je suppose que vous faites référence au hook "pre-push" (avec un trait d'union). Vous pouvez créer des scripts pre-push personnalisés, souvent via des outils comme Husky, pour appliquer des règles comme "ne pousser que si tous les tests passent".
  - **Exemple** : Un hook pre-push pourrait exécuter `npm test` et abandonner le push si les tests échouent. S'il est ignoré (par exemple avec `git push --no-verify`), le hook ne s'exécutera pas.
  - **Fonctionnement** : Situé dans `.git/hooks/pre-push`. Des permissions d'exécution sont nécessaires. Il reçoit des arguments comme le nom du remote et la référence (ref) en cours de push.

Les hooks côté client garantissent que les problèmes sont détectés tôt, empêchant les mauvaises validations ou push de quitter votre machine.

### Hooks Côté Serveur Pendant un Push
Lorsque vous exécutez `git push`, le push est envoyé au dépôt distant (par exemple, GitHub, GitLab ou un serveur personnalisé). Le dépôt distant peut avoir ses propres hooks qui s'exécutent pendant ou après le processus de push. Ils sont stockés dans le répertoire `.git/hooks/` du dépôt Git distant et sont gérés par l'administrateur du serveur.

- **Processus Pendant un Push** :
  1. **Vérifications locales** : Le hook pre-push s'exécute en premier (s'il est présent).
  2. **Transfert des données** : Les changements sont envoyés vers le dépôt distant.
  3. **Exécution distante** : Les hooks côté serveur s'exécutent sur le serveur distant, et non sur votre machine.

- **Hook Pre-Receive** :
  - **Quand il s'exécute** : Sur le serveur distant, immédiatement après réception du push mais avant toute mise à jour des références (branches ou tags).
  - **Objectif** : Valide les changements entrants. Il peut rejeter l'intégralité du push si les vérifications échouent, comme pour appliquer des conventions de message de commit, des revues de code ou des analyses de sécurité.
  - **Fonctionnement** : Si le hook se termine avec un statut non nul, le push est refusé et vous verrez un message d'erreur. Exemple : Rejeter les pushes qui introduisent des fichiers dépassant une certaine taille.

- **Hook Update** (Similaire à Pre-Receive mais par référence) :
  - **Quand il s'exécute** : Pour chaque branche/tag en cours de mise à jour, après le hook pre-receive.
  - **Objectif** : Permet un contrôle granulaire, comme vérifier si le push provient d'un utilisateur autorisé ou si la branche suit les conventions de nommage.
  - **Fonctionnement** : Reçoit les détails sur la référence en cours de mise à jour.

- **Hook Post-Receive** :
  - **Quand il s'exécute** : Sur le serveur distant, après que le push a été entièrement accepté et que les références ont été mises à jour.
  - **Objectif** : Déclenche des actions en aval, comme le déploiement du code, l'envoi de notifications (par exemple, des alertes Slack) ou l'exécution de scripts post-déploiement comme "reconstruire l'application".
  - **Fonctionnement** : S'exécute de manière fiable après un push réussi. Exemple : Déclencher automatiquement un pipeline CI/CD ou mettre à jour un serveur web.

Les hooks côté serveur fournissent une application centralisée des règles, de sorte que même si vos hooks locaux sont contournés, le dépôt distant peut toujours valider ou réagir au push. Des plateformes comme GitHub utilisent des webhooks (équivalents basés sur une API) à des fins similaires, mais pour les serveurs Git bare ou les dépôts auto-hébergés, les hooks ci-dessus sont essentiels.

### Différences Clés et Bonnes Pratiques
- **Client vs Serveur** : Les hooks clients (comme pre-commit/pre-push) vous donnent un retour rapide localement. Les hooks serveur appliquent des règles à l'échelle du dépôt.
- **Personnalisation** : Les hooks sont des scripts shell (par exemple, Bash) mais peuvent invoquer Python, Node.js, etc. Utilisez des outils comme pre-commit (un framework) pour les gérer.
- **Contournement** : Validez avec `--no-verify`, poussez avec `--no-verify`, mais les hooks serveur ne peuvent pas être contournés à moins d'avoir un accès administrateur.
- **Conseils de Configuration** : Les hooks ne sont pas copiés entre les dépôts, ajoutez-les donc à un modèle de dépôt ou utilisez un outil pour les installer.

Si vous configurez cela, consultez la documentation de Git ou des outils comme Husky pour les projets node. Si vous avez un scénario spécifique (par exemple, un exemple de code), fournissez plus de détails pour un conseil personnalisé !