---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Guide de Gestion des Accès Microsoft Entra ID
translated: true
type: note
---

Microsoft Entra ID est un service de gestion des identités et des accès basé sur le cloud qui aide à sécuriser l'accès aux ressources telles que les applications, les données et les appareils. Il prend en charge l'authentification (par exemple, les méthodes de connexion, MFA), l'autorisation (par exemple, l'accès basé sur les rôles) et l'intégration avec les services Azure. Pour commencer, vous aurez besoin d'un abonnement Azure et des autorisations appropriées (par exemple, le rôle Administrateur général).

## Prise en main
1.  **Connectez-vous au portail Azure** : Allez sur [portal.azure.com](https://portal.azure.com) et connectez-vous avec votre compte Microsoft.
2.  **Accédez à Microsoft Entra ID** : Recherchez "Microsoft Entra ID" dans la barre de recherche en haut ou trouvez-le sous "Services Azure".
3.  **Explorez le tableau de bord** : Consultez la vue d'ensemble de votre locataire, y compris les utilisateurs, les groupes et les applications. Configurez les bases comme les domaines personnalisés si nécessaire.
4.  **Activez les fonctionnalités clés** :
    - **Authentification** : Configurez la réinitialisation de mot de passe en libre-service ou l'authentification multifacteur (MFA) sous "Méthodes d'authentification".
    - **Accès conditionnel** : Créez des stratégies sous "Sécurité" > "Accès conditionnel" pour appliquer des règles basées sur l'utilisateur, l'appareil ou l'emplacement.

## Gestion des utilisateurs et des groupes
- **Ajouter des utilisateurs** : Allez dans "Utilisateurs" > "Nouvel utilisateur". Saisissez les détails comme le nom, le nom d'utilisateur (par exemple, user@votredomaine.com) et attribuez des rôles ou des licences.
- **Créer des groupes** : Sous "Groupes" > "Nouveau groupe", choisissez le type de sécurité ou Microsoft 365, ajoutez des membres et utilisez-les pour les attributions d'accès.
- **Attribuer des licences** : Dans les détails de l'utilisateur/du groupe, allez dans "Licences" pour attribuer Entra ID P1/P2 pour des fonctionnalités avancées comme Privileged Identity Management (PIM).
- **Meilleure pratique** : Suivez le principe du privilège minimum - attribuez des autorisations minimales et utilisez des groupes pour la gestion en vrac.

## Gestion des applications
- **Enregistrer une application** : Sous "Inscriptions d'applications" > "Nouvelle inscription", fournissez un nom, des URI de redirection et les types de comptes pris en charge (locataire unique, multi-locataire, etc.).
- **Ajouter des applications d'entreprise** : Pour les applications tierces, allez dans "Applications d'entreprise" > "Nouvelle application" pour parcourir la galerie ou créer des applications hors galerie.
- **Configurer l'accès** : Attribuez des utilisateurs/groupes à l'application sous "Utilisateurs et groupes", et configurez l'authentification unique (SSO) via SAML ou OAuth.
- **Approvisionner les identités** : Automatisez la synchronisation des utilisateurs vers les applications sous "Approvisionnement" pour un accès juste-à-temps.

Pour les configurations hybrides (AD local), utilisez Microsoft Entra Connect pour synchroniser les identités. Surveillez l'utilisation via les journaux sous "Supervision" > "Journaux de connexion".

# Comment vérifier l'accès à une base de données, Kubernetes (AKS) ou autre ressource

L'accès dans Azure est géré via le Contrôle d'accès en fonction du rôle (RBAC), intégré à Entra ID. Les utilisateurs s'authentifient avec les informations d'identification Entra, et les rôles définissent les autorisations. Pour vérifier l'accès, utilisez les outils IAM (Identity and Access Management) du portail Azure. Ceci liste les attributions directes, héritées des étendues parentes (par exemple, l'abonnement), et les attributions de refus.

## Étapes générales pour toute ressource Azure
1.  **Ouvrez la ressource** : Dans le portail Azure, accédez à la ressource (par exemple, groupe de ressources, machine virtuelle, compte de stockage).
2.  **Allez dans Contrôle d'accès (IAM)** : Sélectionnez "Contrôle d'accès (IAM)" dans le menu de gauche.
3.  **Vérifier l'accès** :
    - Pour votre propre accès : Cliquez sur "Vérifier l'accès" > "Afficher mon accès" pour voir les attributions à cette étendue et celles héritées.
    - Pour un utilisateur/groupe/principal de service spécifique :
        - Cliquez sur "Vérifier l'accès" > "Vérifier l'accès".
        - Sélectionnez "Utilisateur, groupe ou principal de service".
        - Recherchez par nom ou e-mail.
        - Consultez le volet des résultats pour les attributions de rôles (par exemple, Propriétaire, Contributeur) et les autorisations effectives.
4.  **Afficher les attributions éligibles** (si vous utilisez PIM) : Basculez vers l'onglet "Attributions éligibles" pour les rôles juste-à-temps.
5.  **Alternative PowerShell/CLI** : Utilisez `az role assignment list --assignee <user> --scope <resource-id>` pour des vérifications scriptées.

Remarque : Cela n'inclut pas les attributions d'étendue enfant ; approfondissez si nécessaire.

## Vérification de l'accès à une base de données Azure SQL
Azure SQL utilise l'authentification Entra pour les utilisateurs de base de données autonome (liés aux identités Entra, pas aux connexions SQL).
1.  **Configurer l'administrateur Entra (si non défini)** : Dans la vue d'ensemble du serveur SQL > "Microsoft Entra ID" sous Paramètres > "Définir l'administrateur". Recherchez et sélectionnez un utilisateur/groupe, puis enregistrez. Ceci active l'authentification Entra à l'échelle du cluster.
2.  **Vérifier l'accès au niveau du serveur** :
    - Dans le volet du serveur SQL > "Microsoft Entra ID", consultez le champ administrateur pour voir l'identité attribuée.
    - Interrogez la base de données `master` : `SELECT name, type_desc FROM sys.database_principals WHERE type IN ('E', 'X');` (E pour les utilisateurs externes, X pour les groupes externes).
3.  **Vérifier l'accès au niveau de la base de données** :
    - Connectez-vous à la base de données en utilisant SSMS avec l'authentification Entra (sélectionnez "Microsoft Entra - Universel avec MFA" dans la boîte de dialogue de connexion).
    - Exécutez `SELECT * FROM sys.database_principals;` ou `EXEC sp_helprolemember;` pour lister les utilisateurs et les rôles.
4.  **Dépannage** : Si la connexion échoue (par exemple, erreur 33134), vérifiez que les stratégies d'Accès Conditionnel Entra autorisent l'accès à l'API Microsoft Graph.

Les utilisateurs obtiennent `CONNECT` par défaut ; accordez des rôles comme `db_datareader` via T-SQL : `ALTER ROLE db_datareader ADD MEMBER [user@domain.com];`.

## Vérification de l'accès à AKS (Cluster Kubernetes)
AKS intègre Entra ID pour l'authentification et utilise Azure RBAC ou Kubernetes RBAC pour l'autorisation.
1.  **Accès au niveau Azure (à la ressource AKS)** :
    - Suivez les étapes générales ci-dessus sur la ressource du cluster AKS.
    - Rôles courants : "Administrateur de cluster Azure Kubernetes Service" pour un accès complet kubeconfig ; "Lecteur" pour la consultation seule.
2.  **Accès à l'API Kubernetes** :
    - Authentifiez-vous via `az login` (utilise le jeton Entra).
    - Obtenez le kubeconfig : `az aks get-credentials --resource-group <rg> --name <cluster>`.
    - Vérifiez les liaisons : `kubectl auth can-i <verb> <resource> --as <user@domain.com> -n <namespace>`.
    - Listez les rôles de cluster : `kubectl get clusterrolebindings | grep <user-or-group>`.
3.  **Utilisation des groupes Entra** : Attribuez des Rôles/Liaisons Kubernetes à des groupes pour l'évolutivité. Exemple YAML pour un rôle d'espace de noms (appliquez avec `kubectl apply -f file.yaml`) :
    ```
    apiVersion: rbac.authorization.k8s.io/v1
    kind: RoleBinding
    metadata:
      name: example-binding
      namespace: default
    subjects:
    - kind: Group
      name: finance-group  # Groupe Entra
      apiGroup: rbac.authorization.k8s.io
    roleRef:
      kind: Role
      name: example-role
      apiGroup: rbac.authorization.k8s.io
    ```
4.  **Meilleures pratiques** : Utilisez des rôles à privilège minimum, intégrez avec PIM pour une élévation juste-à-temps, et évitez les informations d'identification fixes - utilisez les identités de charge de travail pour les pods.

Pour les pods accédant à des ressources (par exemple, SQL depuis AKS), attribuez des identités managées et vérifiez via Azure RBAC sur ces identités.

[Documentation Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/)  
[Vérifier l'accès à une seule ressource Azure](https://learn.microsoft.com/en-us/azure/role-based-access-control/check-access)  
[Configurer l'authentification Entra pour Azure SQL](https://learn.microsoft.com/en-us/azure/azure-sql/database/authentication-aad-configure?view=azuresql)  
[Meilleures pratiques pour l'identité et l'accès AKS](https://learn.microsoft.com/en-us/azure/aks/operator-best-practices-identity)