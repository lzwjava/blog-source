---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Contrôle d'Accès Basé sur les Rôles dans Jenkins
translated: true
type: note
---

### Contrôle d’accès basé sur les rôles (RBAC) dans Jenkins Entreprise (CloudBees CI)

Jenkins Entreprise, propulsé par CloudBees CI, utilise le plugin CloudBees Role-Based Access Control (RBAC) pour mettre en œuvre des autorisations granulaires basées sur les rôles. Cela permet aux administrateurs de définir des rôles personnalisés, de les assigner à des utilisateurs ou des groupes, et de contrôler l'accès aux niveaux global, dossier ou job. Il s'intègre avec le plugin Folders pour l'isolation par équipe et prend en charge les fournisseurs d'identité externes comme LDAP ou Active Directory pour la gestion des groupes. Les autorisations sont agrégées à partir de tous les rôles assignés aux groupes d'un utilisateur, et elles peuvent se propager aux objets enfants (par exemple, les sous-dossiers) sauf si elles sont épinglées ou filtrées.

Le RBAC remplace ou améliore l'autorisation matricielle intégrée de Jenkins, permettant la délégation de l'administration sans un accès complet au système. Il est configuré sous **Gérer Jenkins > Gérer la sécurité > Autorisation**, où vous sélectionnez la "Stratégie d'autorisation matricielle basée sur les rôles".

#### Permissions et droits d'accès clés
Les permissions définissent les actions atomiques que les utilisateurs peuvent effectuer sur les objets Jenkins (par exemple, jobs, dossiers, agents, vues). Jenkins Entreprise inclut les permissions de base de Jenkins ainsi que celles étendues par les plugins. Les permissions sont hiérarchiques—certaines en impliquent d'autres (par exemple, `Job/Configurer` implique `Job/Lire`).

Voici un tableau des catégories de permissions courantes et des exemples, en se concentrant sur la construction/lecture comme mentionné :

| Catégorie          | Exemples de permissions                                                                 | Description |
|-------------------|-----------------------------------------------------------------------------------------|-------------|
| **Lecture/Read-Only** | - `Global/Lire`<br>- `Job/Lire`<br>- `Vue/Lire`<br>- `Agent/Lire`                     | Accorde un accès en lecture aux configurations, builds, journaux et artefacts sans modification. Utile pour les auditeurs ou les observateurs. Le plugin Extended Read Permission ajoute des contrôles de lecture granulaires (par exemple, voir l'espace de travail sans droits de build). |
| **Build/Exécuter** | - `Job/Build`<br>- `Job/Annuler`<br>- `Job/Espace de travail`<br>- `Job/Lire (pour les artefacts)`   | Permet de démarrer, arrêter ou d'accéder aux résultats des builds. Peut être limité à des jobs/dossiers spécifiques. |
| **Configurer/Modifier** | - `Job/Configurer`<br>- `Job/Créer`<br>- `Job/Supprimer`<br>- `Dossier/Configurer`            | Permet de modifier les paramètres du job, d'ajouter des déclencheurs ou de gérer les éléments enfants. |
| **Administratif** | - `Global/Administrer`<br>- `Global/Configurer`<br>- `Groupe/Gérer`<br>- `Rôle/Voir`     | Contrôle total du système ou tâches déléguées comme la gestion des rôles/groupes. `Global/Administrer` est la permission super-utilisateur. |
| **Autre**         | - `SCM/Étiqueter`<br>- `Identifiants/Voir`<br>- `Agent/Lancer`<br>- `ExécuterDesScripts`                | Opérations SCM, accès aux identifiants, gestion des nœuds, ou exécution de scripts. La négation (par exemple, `-Job/Build`) peut restreindre les droits hérités. |

Les droits d'accès sont contrôlés à plusieurs niveaux :
- **Global** : S'applique à l'instance entière (par exemple, via des groupes au niveau racine).
- **Spécifique à un objet** : Surchargé sur des jobs, dossiers ou agents (par exemple, une équipe ne peut builder que dans son dossier).
- **Propagation** : Les rôles sont hérités automatiquement par les enfants sauf s'ils sont "épinglés" (surcharge locale) ou filtrés (par exemple, masquer un projet pour un rôle).
- **Implications** : Certaines permissions accordent automatiquement des permissions subordonnées (configurable dans les versions récentes pour la sécurité).

Les administrateurs peuvent filtrer les rôles pour empêcher la propagation (par exemple, via **Rôles > Filtrer** sur un job) ou utiliser des rôles non filtrables pour un accès global imposé.

#### Gestion des rôles utilisateur
Les rôles sont des ensembles prédéfinis de permissions :
1. Allez dans **Gérer Jenkins > Gérer les Rôles**.
2. Cliquez sur **Ajouter un Rôle** et nommez-le (par exemple, "Développeur").
3. Assignez les permissions en cochant les cases (utilisez "Tout cocher" ou "Tout décocher" pour des actions groupées). Les rôles système comme "anonymous" (pour les utilisateurs non authentifiés) et "authenticated" (utilisateurs connectés) sont prédéfinis et ne peuvent pas être supprimés.
4. Sauvegardez. Les rôles peuvent être marqués comme "non filtrables" pour toujours s'appliquer globalement.

Les utilisateurs héritent des permissions des rôles assignés à leurs groupes—il n'y a pas d'assignation directe utilisateur-rôle ; c'est basé sur les groupes pour une meilleure évolutivité.

#### Assignation des rôles aux groupes et utilisateurs
Les groupes regroupent les utilisateurs et les rôles, permettant une délégation facile :
1. Sur un objet (par exemple, racine, dossier, ou job), allez dans **Groupes > Nouveau Groupe**.
2. Entrez un nom de groupe (par exemple, "ÉquipeDev").
3. Assignez les rôles en les cochant (se propagent aux enfants par défaut ; décochez pour épingler localement).
4. Ajoutez des membres (voir ci-dessous).
5. Sauvegardez.

Les groupes prennent en charge l'imbrication (par exemple, sous-groupes) et l'intégration externe (par exemple, groupes LDAP).

#### Comment les administrateurs ajoutent un utilisateur à un groupe
Les administrateurs avec la permission `Groupe/Gérer` peuvent modifier les appartenances :
1. Naviguez vers la configuration du groupe (par exemple, **Groupes** sur la racine ou l'objet).
2. Dans la section "Membres", cliquez sur **Ajouter un utilisateur** (ou **Ajouter un groupe** pour un groupe externe/imbriqué).
3. Entrez l'identifiant utilisateur (par exemple, nom d'utilisateur de la base de données utilisateur de Jenkins, DN LDAP, ou nom de groupe externe). Utilisez `/whoAmI` pour vérifier les identifiants.
4. Cliquez sur **Ajouter** et sauvegardez. Confirmez la suppression par une invite si nécessaire.
5. Pour les actions groupées/automatisées :
   - Utilisez la CLI : `java -jar jenkins-cli.jar group-membership <chemin-objet> <nom-groupe> <id-utilisateur>` (liste/définit les membres).
   - API REST : POST vers `/rbac/api/v1/groups/<groupe>/members` avec un payload JSON.

Évitez les appartenances circulaires aux groupes pour prévenir les boucles