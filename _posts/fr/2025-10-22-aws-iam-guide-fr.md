---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Guide de Gestion des Accès AWS IAM
translated: true
type: note
---

AWS Identity and Access Management (IAM) est un service gratuit qui vous aide à contrôler de manière sécurisée l'accès aux ressources AWS. Il vous permet de gérer les utilisateurs et leurs autorisations, en veillant à ce que les bonnes personnes et applications aient un accès approprié aux bonnes ressources. IAM gère l'authentification (qui peut se connecter) et l'autorisation (quelles actions ils peuvent effectuer).

## Composants principaux d'IAM

- **Utilisateurs** : Représentent des individus ou des applications qui ont besoin d'accéder à AWS. Chaque utilisateur possède des informations d'identification de sécurité uniques (par exemple, des mots de passe ou des clés d'accès).
- **Groupes** : Collections d'utilisateurs pour faciliter la gestion des autorisations. Les autorisations sont attachées aux groupes, et non directement aux utilisateurs individuels.
- **Rôles** : Identités temporaires avec des autorisations qui peuvent être assumées par des utilisateurs, des services ou des applications. Les rôles n'ont pas d'informations d'identification permanentes ; ils fournissent des jetons de sécurité de courte durée.
- **Politiques** : Documents JSON qui définissent les autorisations. Ils spécifient les actions (par exemple, lire, écrire), les ressources (par exemple, les compartiments S3) et les conditions (par exemple, les restrictions d'adresse IP). Il existe des politiques gérées par AWS, des politiques gérées par le client et des politiques inline.

## Pour commencer : Guide étape par étape

### Prérequis
- Connectez-vous à la AWS Management Console en tant qu'utilisateur racine (l'adresse e-mail et le mot de passe de votre compte). **Important** : Évitez d'utiliser l'utilisateur racine pour les tâches quotidiennes — créez immédiatement un utilisateur administrateur.
- Activez l'authentification multi-facteur (MFA) pour l'utilisateur racine pour une sécurité renforcée.

### 1. Créer un utilisateur IAM
Utilisez la AWS Management Console pour plus de simplicité (des options CLI ou API sont disponibles pour l'automatisation).

1. Ouvrez la console IAM à l'adresse https://console.aws.amazon.com/iam/.
2. Dans le volet de navigation, choisissez **Users** > **Create user**.
3. Saisissez un nom d'utilisateur (par exemple, "admin-user") et sélectionnez **Next**.
4. Sous **Set permissions**, choisissez **Attach policies directly** et sélectionnez une politique gérée par AWS comme "AdministratorAccess" pour un accès complet (commencez avec le principe du moindre privilège en production).
5. (Optionnel) Définissez un mot de passe pour la console : Choisissez **Custom password** et activez **Require password reset**.
6. Vérifiez et choisissez **Create user**.
7. Fournissez à l'utilisateur son URL de connexion (par exemple, https://[account-alias].signin.aws.amazon.com/console), son nom d'utilisateur et son mot de passe temporaire.

Pour un accès par programmation, générez des clés d'accès (mais préférez les rôles pour les applications).

### 2. Créer et gérer des groupes
Les groupes simplifient la mise à l'échelle des autorisations.

1. Dans la console IAM, choisissez **User groups** > **Create group**.
2. Saisissez un nom de groupe (par exemple, "Developers").
3. Attachez des politiques (par exemple, "AmazonEC2ReadOnlyAccess").
4. Choisissez **Create group**.
5. Pour ajouter des utilisateurs : Sélectionnez le groupe > **Add users to group** > Choisissez les utilisateurs existants.

Les utilisateurs héritent de toutes les autorisations du groupe. Un utilisateur peut appartenir à plusieurs groupes.

### 3. Créer et attacher des politiques
Les politiques définissent les actions autorisées.

- **Types** :
  - Gérées par AWS : Préconstruites pour des tâches courantes (par exemple, "ReadOnlyAccess").
  - Gérées par le client : JSON personnalisé pour vos besoins.
  - Inline : Intégrées directement dans un utilisateur/groupe/rôle (à utiliser avec parcimonie).

Pour créer une politique personnalisée :
1. Dans la console IAM, choisissez **Policies** > **Create policy**.
2. Utilisez l'éditeur visuel ou l'onglet JSON (par exemple, autoriser "s3:GetObject" sur un compartiment spécifique).
3. Nommez-la et choisissez **Create policy**.
4. Attachez-la aux utilisateurs/groupes/rôles via **Attach policy**.

Meilleure pratique : Accordez le privilège minimum — commencez large, puis affinez en utilisant des outils comme IAM Access Analyzer.

### 4. Utiliser les rôles IAM
Les rôles sont idéaux pour un accès temporaire, évitant les informations d'identification à long terme.

1. Dans la console IAM, choisissez **Roles** > **Create role**.
2. Sélectionnez l'entité de confiance (par exemple, "AWS service" pour EC2, ou "Another AWS account" pour un accès inter-comptes).
3. Attachez les politiques d'autorisations.
4. Ajoutez une politique de confiance (JSON définissant qui peut assumer le rôle, par exemple, le principal de service EC2).
5. Nommez-le et choisissez **Create role**.

**Scénarios courants** :
- **Instances EC2** : Attachez un rôle à une instance pour un accès sécurisé à d'autres services (par exemple, S3) sans intégrer de clés.
- **Accès inter-comptes** : Dans le Compte A (qui fait confiance), créez un rôle avec une politique de confiance autorisant les principaux du Compte B. Les utilisateurs de B assument le rôle via AWS STS pour accéder aux ressources de A.

Assumez un rôle via la console, la CLI (`aws sts assume-role`) ou les SDK pour obtenir des informations d'identification temporaires.

### 5. Activer MFA et la sécurité supplémentaire
- Pour les utilisateurs : Dans la console IAM > Users > Sélectionnez l'utilisateur > **Security credentials** > Manage MFA.
- Utilisez des MFA virtuels (basés sur une application) ou des appareils MFA matériels.

## Meilleures pratiques pour la sécurité
- **Verrouiller l'utilisateur racine** : Utilisez-le uniquement pour les tâches qui l'exigent (par exemple, modifier les paramètres du compte). Activez MFA et ne créez pas de clés d'accès.
- **Utiliser des informations d'identification temporaires** : Préférez la fédération (par exemple, via IAM Identity Center) et les rôles aux clés à long terme. Faites tourner les clés si elles sont utilisées.
- **Principe du moindre privilège** : Accordez des autorisations minimales ; utilisez des conditions (par exemple, limites de temps/adresse IP) dans les politiques.
- **Surveiller et auditer** : Activez AWS CloudTrail, utilisez IAM Access Analyzer pour détecter les autorisations inutilisées ou les accès non intentionnels, et examinez les informations de dernière utilisation.
- **Supprimer les ressources inutilisées** : Supprimez régulièrement les utilisateurs/rôles/politiques inactifs.
- **Pour les multi-comptes** : Utilisez AWS Organizations avec les service control policies (SCPs) comme garde-fous.
- **Valider les politiques** : Utilisez les vérifications de politiques d'IAM Access Analyzer avant de les appliquer.

Pour un apprentissage pratique, explorez les tutoriels IAM dans la console ou la documentation pour des scénarios comme le contrôle d'accès basé sur les attributs (ABAC).

## Références
- [What is IAM?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html)
- [Create an IAM User](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html)
- [IAM Groups](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups.html)
- [IAM Roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)
- [IAM Best Practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
- [IAM Tutorials](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorials.html)