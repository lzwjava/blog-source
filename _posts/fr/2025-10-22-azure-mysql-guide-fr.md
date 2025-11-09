---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Guide du serveur flexible Azure Database pour MySQL
translated: true
type: note
---

Azure Database for MySQL est un service de base de données relationnelle entièrement managé, basé sur l'édition communautaire de MySQL. Il gère les tâches de routine telles que les sauvegardes, les correctifs et la surveillance, vous permettant ainsi de vous concentrer sur votre application. L'option de déploiement recommandée est **Flexible Server**, qui offre plus d'options de configuration et de meilleures performances que l'ancien Single Server (en cours de retrait).

Ce guide explique comment créer un serveur, s'y connecter et effectuer des opérations de base. Il est basé sur le portail Azure par souci de simplicité.

## Prérequis
- Un abonnement Azure actif (créez-en un sur [azure.microsoft.com](https://azure.microsoft.com/free/) si nécessaire).
- Un accès au portail Azure (portal.azure.com).
- Une connaissance de base des concepts MySQL.
- Un accès réseau sortant sur le port 3306 (port par défaut pour MySQL).
- MySQL Workbench installé pour la connexion (téléchargeable sur [mysql.com](https://dev.mysql.com/downloads/workbench/)).

## Étape 1 : Créer un serveur flexible dans le portail Azure
Suivez ces étapes pour provisionner votre serveur.

1. Connectez-vous au [portail Azure](https://portal.azure.com).

2. Recherchez "Azure Database for MySQL Flexible Servers" dans la barre de recherche en haut et sélectionnez-le.

3. Cliquez sur **Créer** pour démarrer l'assistant.

4. Sous l'onglet **Informations de base**, configurez :
   - **Abonnement** : Sélectionnez votre abonnement.
   - **Groupe de ressources** : Créez-en un nouveau (par exemple, `myresourcegroup`) ou choisissez-en un existant.
   - **Nom du serveur** : Un nom unique (par exemple, `mydemoserver`), entre 3 et 63 caractères, en lettres minuscules/chiffres/tirets. Le nom d'hôte complet sera `<nom>.mysql.database.azure.com`.
   - **Région** : Choisissez la région la plus proche de vos utilisateurs.
   - **Version de MySQL** : 8.0 (dernière version majeure).
   - **Type de charge de travail** : Développement (pour les tests ; utilisez Small/Medium pour la production).
   - **Calcul + stockage** : Niveau Burstable, Standard_B1ms (1 vCore), 10 Gio de stockage, 100 IOPS, sauvegardes de 7 jours. Ajustez selon les besoins (par exemple, augmentez les IOPS pour les migrations).
   - **Zone de disponibilité** : Aucune préférence (ou correspond à la zone de votre application).
   - **Haute disponibilité** : Désactivée pour débuter (activez la redondance interzone pour la production).
   - **Authentification** : MySQL et Microsoft Entra (pour la flexibilité).
   - **Nom d'utilisateur administrateur** : par exemple, `mydemouser` (pas root/admin/etc., max 32 caractères).
   - **Mot de passe** : Un mot de passe fort (8-128 caractères, mélange de majuscules/minuscules/chiffres/caractères spéciaux).

5. Passez à l'onglet **Mise en réseau** :
   - **Méthode de connectivité** : Accès public (pour la simplicité ; utilisez un VNet privé pour la sécurité en production).
   - **Règles de pare-feu** : Ajoutez l'adresse IP actuelle de votre client (ou autorisez les services Azure). Vous ne pourrez pas modifier cela ultérieurement.

6. Vérifiez les paramètres sous **Vérifier + créer**, puis cliquez sur **Créer**. Le déploiement prend 5 à 10 minutes. Surveillez via les notifications.

7. Une fois terminé, épinglez-le au tableau de bord et allez à la page **Vue d'ensemble** de la ressource. Les bases de données par défaut incluent `information_schema`, `mysql`, etc.

## Étape 2 : Se connecter à votre serveur
Utilisez MySQL Workbench pour une connexion graphique. (Alternatives : Azure Data Studio, l'interface CLI mysql, ou Azure Cloud Shell.)

1. Dans le portail, allez dans la **Vue d'ensemble** de votre serveur et notez :
   - Le nom du serveur (par exemple, `mydemoserver.mysql.database.azure.com`).
   - Le nom d'utilisateur administrateur.
   - Réinitialisez le mot de passe si nécessaire.

2. Ouvrez MySQL Workbench.

3. Cliquez sur **Nouvelle connexion** (ou modifiez une connexion existante).

4. Sous l'onglet **Paramètres** :
   - **Nom de la connexion** : par exemple, `Demo Connection`.
   - **Méthode de connexion** : Standard (TCP/IP).
   - **Nom d'hôte** : Le nom complet du serveur.
   - **Port** : 3306.
   - **Nom d'utilisateur** : Le nom d'utilisateur administrateur.
   - **Mot de passe** : Saisissez-le et stockez-le dans le coffre.

5. Cliquez sur **Tester la connexion**. En cas d'échec :
   - Vérifiez les détails du portail.
   - Assurez-vous que le pare-feu autorise votre IP.
   - TLS/SSL est appliqué (TLS 1.2) ; téléchargez le certificat d'autorité de certification depuis [DigiCert](https://dl.cacerts.digicert.com/DigiCertGlobalRootCA.crt.pem) et liez-le dans Workbench si nécessaire (sous l'onglet SSL : Utiliser SSL > Exiger et spécifier le fichier CA).

6. Cliquez sur **OK** pour sauvegarder. Double-cliquez sur la vignette de connexion pour ouvrir un éditeur de requêtes.

## Étape 3 : Créer et gérer des bases de données
Une fois connecté, gérez les bases de données via le portail ou le client.

### Via le portail Azure :
1. Sur la page de votre serveur, sélectionnez **Bases de données** dans le menu de gauche.
2. Cliquez sur **+ Ajouter** :
   - **Nom de la base de données** : par exemple, `testdb`.
   - **Jeu de caractères** : utf8 (par défaut).
   - **Collation** : utf8_general_ci.
3. Cliquez sur **Enregistrer**.

Pour supprimer : Sélectionnez la ou les bases de données, cliquez sur **Supprimer**.

### Via MySQL Workbench (Requêtes SQL) :
Exécutez ces commandes dans l'éditeur de requêtes :

- Créer une base de données : `CREATE DATABASE testdb CHARACTER SET utf8 COLLATE utf8_general_ci;`
- Lister les bases de données : `SHOW DATABASES;`
- Utiliser une base de données : `USE testdb;`
- Créer une table : `CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50));`
- Insérer des données : `INSERT INTO users (name) VALUES ('Alice');`
- Interroger : `SELECT * FROM users;`

Validez les modifications avec `COMMIT;` si la validation automatique n'est pas activée.

## Conseils d'utilisation de base
- **Mise à l'échelle** : Depuis **Vue d'ensemble** > **Calcul + stockage**, ajustez les vCores/stockage/IOPS (pas d'interruption pour la plupart des changements).
- **Sauvegardes** : Automatisées quotidiennement ; restauration jusqu'à une date et heure donnée jusqu'à 35 jours (configurable dans les paramètres de **Sauvegarde**).
- **Surveillance** : Utilisez **Métriques** pour les insights CPU/stockage ; définissez des alertes.
- **Sécurité** : Utilisez toujours SSL (appliqué). Pour la production, activez la haute disponibilité, le réseau privé et l'authentification Entra ID.
- **Migration** : Utilisez mysqldump pour les petites bases de données ; DMS pour les grandes.
- **Coûts** : Payez pour le calcul/stockage ; commencez petit et mettez à l'échelle. Utilisez le calculateur sur [azure.microsoft.com](https://azure.microsoft.com/pricing/calculator/).
- **Nettoyage** : Supprimez le groupe de ressources pour supprimer le serveur et éviter des frais.

Pour les fonctionnalités avancées comme les réplicas en lecture ou les paramètres du serveur, explorez le menu de gauche du portail.

## Références
- [Démarrage rapide : Créer un serveur flexible à l'aide du portail Azure](https://learn.microsoft.com/fr-fr/azure/mysql/flexible-server/quickstart-create-server-portal)
- [Se connecter à l'aide de MySQL Workbench](https://learn.microsoft.com/fr-fr/azure/mysql/flexible-server/connect-workbench)
- [Créer et gérer des bases de données](https://learn.microsoft.com/fr-fr/azure/mysql/flexible-server/how-to-create-manage-databases)
- [Documentation d'Azure Database for MySQL](https://learn.microsoft.com/fr-fr/azure/mysql/)