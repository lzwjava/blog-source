---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Création d'une instance Azure API Management
translated: true
type: note
---

### Création d'une passerelle API dans Azure à l'aide de Gestion des API

Azure API Management (APIM) est le service entièrement géré qui agit comme une passerelle API, fournissant des fonctionnalités telles que la publication d'API, la sécurité, l'analytique et les portails développeurs. Voici un guide étape par étape pour créer une instance APIM via le portail Azure.

#### Prérequis
- Un abonnement Azure actif. Si vous n'en avez pas, créez un [compte Azure gratuit](https://azure.microsoft.com/fr-fr/free/).

#### Étapes pour créer une instance Gestion des API

1. **Se connecter au portail Azure**  
   Accédez au [portail Azure](https://portal.azure.com) et connectez-vous avec votre compte Azure.

2. **Créer une nouvelle ressource**  
   - À partir du menu du portail Azure, sélectionnez **Créer une ressource**. (Alternativement, sélectionnez **Créer une ressource** depuis la page d'accueil d'Azure.)  
   - Sur la page **Créer une ressource**, recherchez et sélectionnez **Gestion des API** sous la catégorie **Intégration**.  
   - Cliquez sur **Créer**.

3. **Configurer les paramètres de base**  
   Sur la page **Créer un service Gestion des API**, passez à l'onglet **Informations de base** et renseignez les détails :  
   | Paramètre              | Description                                                                 |
   |----------------------|-----------------------------------------------------------------------------|
   | Abonnement         | Sélectionnez l'abonnement Azure pour cette instance.                            |
   | Groupe de ressources       | Choisissez un groupe de ressources existant ou créez-en un nouveau (par exemple, "APIM-RG").    |
   | Région               | Choisissez une région proche de vos utilisateurs ou services backend (par exemple, USA Est).      |
   | Nom de la ressource        | Entrez un nom unique (par exemple, "my-apim-instance"). Celui-ci fait partie du domaine par défaut : `<nom>.azure-api.net`. Il ne peut pas être modifié ultérieurement. |
   | Nom de l'organisation    | Le nom de votre organisation (utilisé dans le portail développeur et les e-mails).             |
   | E-mail de l'administrateur  | Votre e-mail pour les notifications système.                                        |
   | Niveau de tarification         | Commencez par **De base v2** pour le développement/les tests (déploiement rapide, ~30-40 minutes). D'autres niveaux comme Développeur ou Standard offrent plus de fonctionnalités. |
   | Unités                | La valeur par défaut est 1 pour l'évaluation.                                                |  
   Passez en revue et poursuivez.

4. **Optionnel : Configurer la surveillance et la sécurité**  
   Sur l'onglet **Surveiller + sécuriser** :  
   - Activez des modules complémentaires optionnels comme Log Analytics pour la journalisation (cela peut engendrer des coûts supplémentaires).  
   - Ignorez cette étape pour le moment si vous débutez.

5. **Vérifier et créer**  
   - Sur l'onglet **Vérifier + créer**, validez vos paramètres.  
   - Cliquez sur **Créer**. Le déploiement prend 30 à 40 minutes ou plus.  
   - Astuce : Épinglez la ressource à votre tableau de bord pour un accès facile une fois créée.

6. **Vérifier l'instance**  
   - Dans le portail Azure, recherchez **Services Gestion des API**.  
   - Sélectionnez votre nouvelle instance.  
   - Sur la page **Vue d'ensemble**, confirmez que le statut est "En ligne". Vous êtes maintenant prêt à importer des API, configurer des stratégies ou configurer le portail développeur.

#### Prochaines étapes
- Importez votre première API : Suivez le [tutoriel pour importer et publier une API](https://learn.microsoft.com/fr-fr/azure/api-management/import-and-publish).  
- Sécurisez-la : Ajoutez des stratégies pour l'authentification, la limitation du débit, etc.  
- Nettoyage : Si vous testez, supprimez le groupe de ressources via le portail pour éviter des frais (recherchez **Groupes de ressources** > sélectionnez le groupe > **Supprimer le groupe de ressources**).  

Pour les domaines personnalisés ou les configurations avancées, reportez-vous à la [documentation APIM](https://learn.microsoft.com/fr-fr/azure/api-management/).

[Démarrage rapide : Créer une instance Azure API Management - Portail](https://learn.microsoft.com/fr-fr/azure/api-management/get-started-create-service-instance)  
[Vue d'ensemble d'Azure API Management](https://learn.microsoft.com/fr-fr/azure/api-management/api-management-key-concepts)