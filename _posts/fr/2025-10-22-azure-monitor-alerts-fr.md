---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Vue d'ensemble des alertes Azure Monitor
translated: true
type: note
---

### Présentation des alertes dans Azure

Les alertes Azure Monitor sont une fonctionnalité d'Azure Monitor qui vous notifie de manière proactive lorsque des conditions spécifiques sont remplies dans vos ressources Azure, vous aidant ainsi à détecter et à résoudre les problèmes avant qu'ils n'affectent les utilisateurs. Elles fonctionnent en évaluant les données provenant des métriques, des journaux ou des journaux d'activité par rapport à des règles prédéfinies. Lorsqu'une condition est déclenchée (par exemple, l'utilisation du processeur dépasse 80 %), une alerte se déclenche, ce qui peut envoyer des notifications par e-mail, SMS ou déclencher des actions automatisées comme l'exécution d'un script.

Les alertes sont avec état (elles se résolvent automatiquement lorsque le problème est résolu) ou sans état (elles se déclenchent de manière répétée jusqu'à ce qu'elles soient fermées manuellement), selon votre configuration. Elles prennent en charge la surveillance sur une ou plusieurs ressources et sont facturées en fonction du nombre de séries chronologiques surveillées.

#### Types d'alertes
Azure Monitor prend en charge plusieurs types d'alertes adaptés à différentes sources de données :

| Type d'alerte | Description | Idéal pour |
|---|---|---|
| **Alertes de métrique** | Évaluent les métriques numériques (par exemple, le pourcentage d'UC, l'espace disque) à intervalles réguliers. Prend en charge les seuils statiques ou dynamiques (basés sur l'IA). | Surveillance des performances des machines virtuelles, des bases de données ou des applications. |
| **Alertes de recherche dans les journaux** | Exécutent des requêtes sur les données de Log Analytics pour détecter des modèles dans les journaux. | Analyse d'événements complexes, comme des pics d'erreur dans les journaux d'application. |
| **Alertes de journal d'activité** | Se déclenchent sur des événements administratifs ou opérationnels (par exemple, la création/suppression de ressources). | Audit de sécurité et de conformité. |
| **Alertes de détection intelligente** | Détection d'anomalies pilotée par l'IA pour les applications web via Application Insights. | Détection automatique des problèmes dans les applications. |
| **Alertes Prometheus** | Interrogent les métriques Prometheus dans les services managés comme AKS. | Environnements de conteneurs et Kubernetes. |

Pour la plupart des cas d'usage, commencez par les alertes de métrique ou de journal.

### Prérequis
- Un abonnement Azure avec des ressources actives à surveiller.
- Autorisations : Rôle Lecteur sur la ressource cible, Contributeur sur le groupe de ressources pour la règle d'alerte et Lecteur sur tous les groupes d'actions.
- Une familiarité avec le portail Azure (portal.azure.com).

### Comment créer et utiliser une règle d'alerte de métrique (étape par étape)
Les alertes de métrique sont un point de départ courant. Voici comment en créer une dans le portail Azure. Ce processus prend environ 5 à 10 minutes.

1.  **Connectez-vous au portail Azure** : Allez sur [portal.azure.com](https://portal.azure.com) et connectez-vous.

2.  **Accédez à Alertes** :
    - À partir de la page d'accueil, recherchez et sélectionnez **Monitor**.
    - Dans le menu de gauche, sous **Insights**, sélectionnez **Alertes**.
    - Cliquez sur **+ Créer** > **Règle d'alerte**.

    *Alternative* : À partir d'une ressource spécifique (par exemple, une machine virtuelle), sélectionnez **Alertes** dans le menu de gauche, puis **+ Créer** > **Règle d'alerte**. Cela définit automatiquement l'étendue.

3.  **Définissez l'étendue** :
    - Dans le volet **Sélectionner une ressource**, choisissez votre abonnement, le type de ressource (par exemple, Machines virtuelles) et la ressource spécifique.
    - Cliquez sur **Appliquer**. (Pour les alertes multi-ressources, sélectionnez plusieurs ressources du même type dans une seule région.)

4.  **Configurez la condition** :
    - Dans l'onglet **Condition**, cliquez sur **Nom du signal** et sélectionnez une métrique (par exemple, "Percentage CPU" pour une machine virtuelle).
        - Utilisez **Voir tous les signaux** pour filtrer par type (par exemple, Métriques de plateforme).
    - Aperçu des données : Définissez une plage de temps (par exemple, les dernières 24 heures) pour voir les valeurs historiques.
    - Définissez la **Logique d'alerte** :
        - **Seuil** : Statique (par exemple, > 80) ou Dynamique (ajusté par IA en fonction de l'historique).
        - **Opérateur** : Supérieur à, Inférieur à, etc.
        - **Agrégation** : Moyenne, Somme, Min, Max sur la période d'évaluation.
        - Pour le seuil dynamique : Choisissez la sensibilité (Faible/Moyenne/Élevée).
    - (Optionnel) **Fractionner par dimensions** : Filtrez par attributs comme le nom d'instance pour des alertes granulaires (par exemple, par machine virtuelle dans un ensemble).
    - **Évaluation** : Vérifiez toutes les 1 à 5 minutes ; examinez les 5 à 15 dernières minutes.
    - Cliquez sur **Terminé**.

5.  **Ajoutez des actions (optionnel mais recommandé)** :
    - Dans l'onglet **Actions**, sélectionnez **Ajouter des groupes d'actions**.
    - Choisissez un groupe existant (pour les e-mails/SMS) ou créez-en un :
        - Ajoutez des destinataires (par exemple, les e-mails des administrateurs).
        - Ajoutez des actions comme Logic Apps pour l'automatisation ou des webhooks pour les intégrations.
    - Cliquez sur **Terminé**.

6.  **Définissez les détails de la règle** :
    - Dans l'onglet **Détails** :
        - **Abonnement** et **Groupe de ressources** : Pré-remplis ; modifiez si nécessaire.
        - **Gravité** : Sev 0 (Critique) à Sev 4 (Verbose).
        - **Nom de la règle d'alerte** : par exemple, "Alerte CPU Élevé - VM Prod".
        - **Description** : Notes optionnelles.
    - **Options avancées** :
        - Activez la règle lors de la création.
        - Résolution automatique des alertes (la rend avec état).
    - Ajoutez des étiquettes si nécessaire pour l'organisation.

7.  **Passez en revue et créez** :
    - Allez dans **Vérifier + créer**.
    - Validez (corrigez les erreurs, comme des seuils invalides).
    - Cliquez sur **Créer**. La règle s'active immédiatement si elle est activée.

Une fois créée, l'alerte se déclenchera lorsque les conditions sont remplies, envoyant des notifications et mettant à jour son statut (par exemple, de "Déclenchée" à "Résolue").

#### Gestion des alertes
-   **Voir les alertes** : Dans Monitor > Alertes, consultez les alertes actives/déclenchées. Filtrez par heure, gravité ou ressource.
-   **Modifier une règle** : Allez dans Monitor > Alertes > Règles d'alerte, sélectionnez la règle et cliquez sur **Modifier**.
-   **Tester** : Utilisez l'aperçu à l'étape 4 pour simuler.
-   **Mettre à l'échelle** : Pour plusieurs ressources, utilisez Azure CLI/PowerShell ou des modèles ARM. Activez les règles recommandées intégrées via les insights des ressources.

### Bonnes pratiques
-   Commencez simplement : Une condition par règle initialement.
-   Utilisez des seuils dynamiques pour les métriques bruyantes afin de réduire les faux positifs.
-   Intégrez avec des groupes d'actions pour la correction automatisée (par exemple, scale up d'une machine virtuelle).
-   Surveillez les coûts : Basés sur les séries surveillées (gratuit pour l'usage basique ; vérifiez la tarification).
-   Pour les journaux, suivez des étapes similaires mais sélectionnez **Alertes de journal** lors de la création et écrivez une requête KQL.

Pour les alertes de journal ou d'autres types, le processus est analogue — remplacez la condition par une requête.

[Présentation des alertes Azure Monitor](https://learn.microsoft.com/fr-fr/azure/azure-monitor/alerts/alerts-overview)  
[Créer une règle d'alerte de métrique](https://learn.microsoft.com/fr-fr/azure/azure-monitor/alerts/alerts-create-metric-alert-rule)  
[Créer une règle d'alerte de journal](https://learn.microsoft.com/fr-fr/azure/azure-monitor/alerts/alerts-create-log-alert-rule)  
[Tarification Azure Monitor](https://azure.microsoft.com/fr-fr/pricing/details/monitor/)