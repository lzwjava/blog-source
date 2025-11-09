---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Gestion des accès aux ordinateurs portables avec Active Directory
translated: true
type: note
---

### Qu'est-ce qu'Active Directory (AD) dans Windows ?

Active Directory (AD) est un service d'annuaire développé par Microsoft pour les réseaux en domaine Windows. Il agit comme une base de données centralisée qui stocke et organise les informations sur les objets du réseau, tels que les comptes d'utilisateurs, les comptes d'ordinateurs, les imprimantes, les dossiers partagés et d'autres ressources. Cette structure hiérarchique permet aux administrateurs de gérer et de sécuriser efficacement l'accès à ces ressources au sein d'une organisation.

Le composant principal est **Active Directory Domain Services (AD DS)**, qui gère le stockage des données de l'annuaire et leur mise à disposition pour les utilisateurs et les administrateurs. Les principales fonctionnalités incluent :
- **Intégration de la sécurité** : Utilise un nom d'utilisateur et un mot de passe uniques pour l'authentification et le contrôle d'accès sur l'ensemble du réseau.
- **Schéma** : Définit les règles pour les types d'objets (par exemple, utilisateurs, ordinateurs) et leurs attributs.
- **Catalogue global** : Un index consultable de tous les objets de l'annuaire, permettant des recherches rapides indépendamment de l'emplacement.
- **Réplication** : Synchronise automatiquement les modifications entre les contrôleurs de domaine pour maintenir la cohérence des données.
- **Mécanismes de requête et d'indexation** : Permet aux utilisateurs et aux applications de rechercher et de récupérer des informations de l'annuaire.

Un **compte AD** fait généralement référence à un compte utilisateur (ou compte d'ordinateur) créé et stocké dans AD. Ces comptes incluent des détails tels que les noms d'utilisateur, les mots de passe, les adresses e-mail et les appartenances aux groupes, permettant des connexions sécurisées et l'accès aux ressources.

En substance, AD simplifie la gestion informatique en fournissant un point de contrôle unique pour les identités et les permissions dans un environnement Windows, remplaçant ainsi les comptes locaux dispersés sur des machines individuelles.

### Comment utiliser Active Directory pour gérer les droits d'accès aux ordinateurs portables des employés

AD est puissant pour gérer l'accès aux ordinateurs portables car il centralise les identités des utilisateurs et les stratégies, garantissant une application cohérente même pour les appareils mobiles ou distants. Cela empêche les employés d'avoir des droits d'administrateur local complets (réduisant les risques de sécurité) tout en permettant un accès contrôlé aux outils nécessaires. Voici un guide étape par étape :

1. **Configurer un domaine AD** :
   - Installez AD DS sur un serveur Windows (agissant comme un contrôleur de domaine).
   - Créez votre domaine (par exemple, entreprise.local) via le Gestionnaire de serveur ou PowerShell.

2. **Joindre les ordinateurs portables au domaine** :
   - Sur chaque ordinateur portable d'employé (exécutant Windows 10/11 Pro ou Enterprise), allez dans **Paramètres > Système > À propos de > Joindre un domaine** (ou utilisez `sysdm.cpl` dans la boîte de dialogue Exécuter).
   - Saisissez le nom de domaine et fournissez les informations d'identification de l'administrateur du domaine pour rejoindre.
   - Redémarrez l'ordinateur portable. Une fois joint, les ordinateurs portables s'authentifient auprès d'AD au lieu des comptes locaux, permettant une gestion à l'échelle du domaine.

3. **Créer et organiser les comptes utilisateurs** :
   - Utilisez **Utilisateurs et ordinateurs Active Directory** (dsa.msc) sur le contrôleur de domaine pour créer des comptes utilisateur pour les employés.
   - Affectez les utilisateurs à des **groupes de sécurité** (par exemple, "Équipe de vente" ou "Travailleurs à distance") pour une gestion plus facile des autorisations. Ajoutez des groupes via l'onglet "Membre de" dans les propriétés de l'utilisateur.

4. **Appliquer des stratégies de groupe pour le contrôle d'accès** :
   - Utilisez **Objets de stratégie de groupe (GPO)** — le moteur de stratégie d'AD — pour appliquer des paramètres sur les ordinateurs portables joints au domaine.
     - Ouvrez **Gestion des stratégies de groupe** (gpmc.msc) sur le contrôleur de domaine.
     - Créez un nouveau GPO (par exemple, "Restrictions utilisateur des ordinateurs portables") et liez-le à une Unité d'organisation (UO) contenant les ordinateurs portables (créez des UO comme "Ordinateurs portables des employés" dans AD pour regrouper les appareils).
     - Stratégies courantes à définir :
       - **Droits de l'utilisateur** : Sous Configuration ordinateur > Stratégies > Paramètres Windows > Paramètres de sécurité > Stratégies locales > Attribution des droits utilisateur, supprimez "Administrateurs" des utilisateurs standard pour empêcher l'élévation des privilèges administrateur local.
       - **Restrictions logicielles** : Bloquez les installations d'applications non autorisées via les Stratégies de restriction logicielle.
       - **Accès aux dossiers/imprimantes** : Accordez des autorisations NTFS/partage en fonction de l'appartenance au groupe (par exemple, le groupe Ventes obtient un accès en lecture/écriture aux lecteurs partagés).
       - **Accès à distance** : Configurez un VPN ou un accès conditionnel pour les ordinateurs portables hors réseau.
     - Appliquez le GPO — il se propage automatiquement (ou forcez avec `gpupdate /force` sur les ordinateurs portables).
   - Pour un contrôle avancé, intégrez le **Contrôle d'accès basé sur les rôles (RBAC)** via Windows Admin Center :
     - Installez Windows Admin Center sur un serveur.
     - Activez RBAC sur les ordinateurs portables (installe les points de terminaison Just Enough Administration).
     - Affectez des groupes AD à des rôles comme "Administrateurs" (accès complet) ou "Lecteurs" (accès en lecture seule).

5. **Surveiller et maintenir** :
   - Utilisez des outils comme l'Observateur d'événements ou PowerShell (par exemple, `Get-ADUser` ou `Get-GPResultantSetOfPolicy`) pour auditer l'accès.
   - Pour l'automatisation, scriptez les modifications en bloc avec PowerShell (par exemple, l'ajout d'utilisateurs à des groupes).
   - Si vous utilisez des configurations hybrides (par exemple, avec Microsoft Entra ID), synchronisez AD pour des stratégies cloud comme l'authentification multifacteur.

Cette configuration garantit que les employés se connectent avec des informations d'identification AD, héritent des droits basés sur les groupes et ne peuvent pas contourner les restrictions — idéal pour la conformité et la sécurité. Commencez petit avec une UO de test pour éviter les perturbations.

[Vue d'ensemble d'Active Directory Domain Services](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview)  
[Configuration du contrôle d'accès utilisateur et des autorisations](https://learn.microsoft.com/en-us/windows-server/manage/windows-admin-center/configure/user-access-control)  
[Vue d'ensemble de la stratégie de groupe pour Windows Server](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/group-policy/group-policy-overview)