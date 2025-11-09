---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Prise en Charge Multi-Répertoire de Claude Code
translated: true
type: note
---

Claude Code, l'assistant de codage alimenté par l'IA d'Anthropic, fonctionne principalement dans son répertoire de travail initialisé pour des raisons de sécurité et de concentration, mais il prend désormais entièrement en charge la fonctionnalité inter-projets grâce à une fonction multi-répertoire introduite dans les mises à jour récentes (par exemple, la version 1.0.18 et ultérieures). Cela permet à une seule session d'accéder et de travailler avec des fichiers dans plusieurs projets ou répertoires non liés en dehors de l'original, permettant des tâches comme la référence à des configurations partagées, l'intégration de code frontend/backend, ou la gestion de configurations monorepo sans changement de contexte.[1][2][3]

### Fonctionnement de la Fonctionnalité Inter-Projets
- **Mécanisme de Base** : Claude Code démarre dans un répertoire racine (votre projet "principal") mais peut étendre les autorisations pour lire, modifier et exécuter des commandes dans des répertoires supplémentaires. Cela se fait via le flag `--add-dir` ou la commande interactive `/add-dir` pendant une session. Les répertoires ajoutés sont traités comme des extensions de l'espace de travail, permettant des opérations sur les fichiers transparentes (par exemple, vous pouvez linter des fichiers du Projet A tout en modifiant dans le Projet B).[3][4]
- **Portée de la Session** : Chaque ajout de projet est temporaire sauf s'il est conservé via la configuration. Les worktrees Git peuvent permettre des sessions simultanées sur des parties d'un projet pour une collaboration plus approfondie.[5][6]
- **Limitations** : Claude Code restreint l'accès aux fichiers aux répertoires ajoutés uniquement - il ne découvrira pas automatiquement des chemins non liés. Pour des configurations multi-projets persistantes (par exemple, les monorepos), exécutez-le à partir d'un répertoire parent contenant des sous-dossiers.[3][7]
- **Cas d'Usage** :
  - **Monorepos** : Ajoutez des sous-répertoires pour les séparations frontend/backend.[3][5][7][8]
  - **Ressources Partagées** : Référencez des configs ou des bibliothèques depuis un projet séparé.[3][6]
  - **Collaboration Inter-Projets** : Intégrez du code provenant de bibliothèques ou d'outils dans différents dépôts.[1][3]

### Comment Demander à Claude Code d'Impliquer un Autre Projet
Pour ajouter un projet en dehors du répertoire actuel (par exemple, `${another_project_path}`) :

1. **Démarrez Claude Code** dans votre répertoire de projet principal (par exemple, `cd /chemin/vers/projet/principal && claude`).
2. **Ajoutez le Répertoire Supplémentaire de Manière Interactive** :
   - Pendant la session, tapez `/add-dir /chemin/complet/vers/un/autre/projet` ou un chemin relatif (par exemple, `../autre-projet`).
   - Claude Code confirmera l'accès - répondez "yes" si vous y êtes invité.[2][3][4]
3. **Au Démarrage via un Flag CLI** (pour une configuration multi-répertoire immédiate) :
   - Exécutez : `claude --add-dir /chemin/vers/un/autre/projet` (ajoutez-en plusieurs avec des flags répétés).[4][5][7]
4. **Donnez des Instructions aux Bots/Agents Claude** : Une fois ajouté, donnez des invites en langage naturel comme "Référence les fichiers API du répertoire ajouté dans `/chemin/vers/un/autre/projet`" ou "Intègre cette config partagée du Projet B." La conception agentique de Claude comprend ces demandes dans le contexte élargi.[3][5][6]

### Bonnes Pratiques et Conseils
- **Spécification des Chemins** : Utilisez des chemins absolus pour plus de clarté entre les environnements. Évitez d'ajouter trop de répertoires pour éviter les impacts sur les performances.[3][7]
- **Configuration de l'Espace de Travail** : Pour les équipes, envisagez des fichiers de configuration pour des configurations réutilisables. Combinez avec des outils comme Apidog pour les tests d'API entre les répertoires.[3][8]
- **Dépannage** : Si la résolution du chemin échoue, assurez-vous des autorisations d'écriture. Redémarrez les sessions pour les changements. Pour les problèmes persistants, vérifiez les logs ou exécutez depuis un répertoire de niveau supérieur.[3][7]
- **Flux de Travail d'Équipe** : Utilisez cette fonction pour les microservices ou les bibliothèques partagées ; synchronisez via Git pour le versioning.[5][6][8]

Cette fonctionnalité transforme les flux de travail pour les configurations complexes, réduisant les frictions par rapport à l'exécution de sessions séparées dans chaque répertoire.[3][6] Si vous rencontrez des problèmes ou avez besoin d'exemples pour des outils spécifiques, fournissez plus de détails !

Citations :
[1] https://www.reddit.com/r/ClaudeAI/comments/1l896ek/claude_code_v1018_we_can_now_specify_additional/
[2] https://www.threads.com/@boris_cherny/post/DMtFLWOzKAS/video-claude-code-can-now-work-across-multiple-directories-in-a-single-sessiontype-add?hl=en
[3] https://apidog.com/blog/claude-code-multi-directory-support/
[4] https://claudelog.com/faqs/--add-dir/
[5] https://www.anthropic.com/engineering/claude-code-best-practices
[6] https://www.linkedin.com/posts/valokafor_how-to-set-up-claude-code-the-right-way-for-activity-7353146981034201089-dhdX
[7] https://stackoverflow.com/questions/79763754/best-practices-for-multi-project-workspaces-in-claude-code
[8] https://www.siddharthbharath.com/claude-code-the-complete-guide/