---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Utiliser Amazon RDS pour MySQL
translated: true
type: note
---

Amazon RDS (Relational Database Service) pour MySQL est un service de base de données managé qui facilite la configuration, l'exploitation et la mise à l'échelle de bases de données MySQL dans le cloud. Il gère les tâches courantes comme les sauvegardes, les correctifs et la mise à l'échelle, vous permettant ainsi de vous concentrer sur votre application. Ce guide vous présente les bases : créer une instance de base de données MySQL, s'y connecter et effectuer des opérations simples. Nous utiliserons la AWS Management Console par souci de simplicité.

**Note sur les coûts :** L'AWS Free Tier offre un usage limité pour les nouveaux comptes, mais des frais s'appliquent pour les ressources au-delà de cette limite. Supprimez toujours les ressources une fois terminé pour éviter des factures inattendues. Pour la production, suivez les bonnes pratiques de sécurité comme l'utilisation de VPC, le chiffrement et le principe du moindre privilège.

## Prérequis
- Un compte AWS (inscrivez-vous sur [aws.amazon.com](https://aws.amazon.com) si nécessaire).
- Une familiarité basique avec la console AWS et MySQL.
- Pour tester une connexion sécurisée, nous créerons une instance EC2 dans le même VPC (Virtual Private Cloud). Déterminez votre adresse IP publique (par exemple via [checkip.amazonaws.com](https://checkip.amazonaws.com)) pour l'accès SSH.
- Choisissez une Région AWS proche de vous (par exemple, US East (N. Virginia)).

**Bonnes pratiques :** Utilisez une instance de base de données privée dans un VPC pour restreindre l'accès aux seules ressources de confiance. Activez SSL/TLS pour des connexions chiffrées.

## Étape 1 : Créer une instance EC2 pour la connexion
Ceci configure un simple serveur Linux pour se connecter à votre instance de base de données privée.

1. Connectez-vous à la [AWS Management Console](https://console.aws.amazon.com) et ouvrez la console EC2.
2. Sélectionnez votre Région.
3. Cliquez sur **Lancer une instance**.
4. Configurez :
   - **Nom :** `ec2-database-connect`.
   - **AMI :** Amazon Linux 2023 (éligible au free tier).
   - **Type d'instance :** t3.micro (éligible au free tier).
   - **Paire de clés :** Créez ou sélectionnez-en une existante pour l'accès SSH.
   - **Paramètres réseau :** Modifier > Autoriser le trafic SSH depuis **Mon IP** (ou votre IP spécifique, par exemple `192.0.2.1/32`). Évitez `0.0.0.0/0` pour la sécurité.
   - Conservez les valeurs par défaut pour le stockage et les étiquettes.
5. Cliquez sur **Lancer une instance**.
6. Notez l'ID de l'instance, le DNS IPv4 public et le nom de la paire de clés dans les détails de l'instance.
7. Attendez que le statut passe à **En cours d'exécution** (2-5 minutes).

**Conseil de sécurité :** Restreignez SSH à votre IP uniquement. Téléchargez la paire de clés (fichier .pem) de manière sécurisée.

## Étape 2 : Créer une instance de base de données MySQL
Utilisez "Création facile" pour une configuration rapide avec les paramètres par défaut.

1. Ouvrez la [console RDS](https://console.aws.amazon.com/rds/).
2. Sélectionnez la même Région que votre instance EC2.
3. Dans le volet de navigation, cliquez sur **Bases de données** > **Créer une base de données**.
4. Sélectionnez **Création facile**.
5. Sous **Configuration** :
   - Type de moteur : **MySQL**.
   - Modèles : **Free tier** (ou **Sandbox** pour les comptes payants).
   - Identifiant de l'instance de base de données : `database-test1` (ou votre choix).
   - Nom d'utilisateur principal : `admin` (ou personnalisé).
   - Mot de passe principal : Générer automatiquement ou définir un mot de passe robuste (enregistrez-le de manière sécurisée).
6. (Optionnel) Sous **Connectivité**, sélectionnez **Se connecter à une ressource de calcul EC2** et choisissez votre instance EC2 pour une configuration plus facile.
7. Cliquez sur **Créer une base de données**.
8. Consultez la fenêtre contextuelle des informations d'identification (nom d'utilisateur/mot de passe) — sauvegardez-les, car le mot de passe n'est pas récupérable ultérieurement.
9. Attendez que le statut passe à **Disponible** (jusqu'à 10-20 minutes). Notez le **Point de terminaison** (nom DNS) et le port (par défaut : 3306) dans l'onglet **Connectivité et sécurité**.

**Bonnes pratiques :** Pour la production, utilisez "Création standard" pour personnaliser le VPC, les sauvegardes (activer la sauvegarde automatisée) et le stockage. Activez la protection contre la suppression et Multi-AZ pour la haute disponibilité.

## Étape 3 : Se connecter à l'instance de base de données
Connectez-vous depuis votre instance EC2 en utilisant le client MySQL.

1. SSH vers votre instance EC2 :
   ```
   ssh -i /chemin/vers/votre-paire-de-clés.pem ec2-user@votre-dns-public-ec2
   ```
   (Remplacez par vos informations ; par exemple, `ssh -i ec2-database-connect-key-pair.pem ec2-user@ec2-12-345-678-90.compute-1.amazonaws.com`.)

2. Sur l'instance EC2, mettez à jour les paquets :
   ```
   sudo dnf update -y
   ```

3. Installez le client MySQL :
   ```
   sudo dnf install mariadb105 -y
   ```

4. Connectez-vous à la base de données :
   ```
   mysql -h votre-point-de-terminaison-db -P 3306 -u admin -p
   ```
   Saisissez le mot de passe principal lorsqu'il est demandé.

Si cela réussit, vous verrez l'invite MySQL (`mysql>`).

**Dépannage :** Assurez-vous que les groupes de sécurité autorisent le trafic entrant sur le port 3306 depuis l'instance EC2. Pour les connexions externes, rendez la base de données publique (non recommandé) ou utilisez des bastions hosts/VPN.

**Conseil de sécurité :** Utilisez `--ssl-mode=REQUIRED` pour des connexions chiffrées : `mysql -h point-de-terminaison -P 3306 -u admin -p --ssl-mode=REQUIRED`.

## Étape 4 : Utilisation de base
Une fois connecté, vous pouvez exécuter des commandes SQL. Exemples :

- Afficher les bases de données : `SHOW DATABASES;`
- Créer une base de données exemple : `CREATE DATABASE myapp;`
- L'utiliser : `USE myapp;`
- Créer une table :
  ```
  CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(100)
  );
  ```
- Insérer des données : `INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com');`
- Interroger : `SELECT * FROM users;`
- Quitter : `EXIT;`

Depuis les applications (par exemple, Python, Node.js), utilisez les pilotes MySQL standard avec le point de terminaison, le port, le nom d'utilisateur et le mot de passe comme chaînes de connexion.

**Bonnes pratiques :** Surveillez les performances via CloudWatch, activez les sauvegardes automatisées et mettez à l'échelle verticalement (taille de l'instance) ou horizontalement (réplicas de lecture) selon les besoins.

## Nettoyage : Supprimer les ressources
Pour arrêter les frais :

1. **Supprimer l'instance EC2 :** Console EC2 > Sélectionner l'instance > **État de l'instance** > **Arrêter** > Confirmer.
2. **Supprimer l'instance de base de données :** Console RDS > Sélectionner la base de données > **Actions** > **Supprimer** > Décocher la création de snapshot > Confirmer.

Vérifiez la console de facturation AWS pour toute ressource encore en cours d'exécution.

Pour des sujets plus avancés comme les migrations, le réglage des performances ou l'utilisation de l'API/CLI, reportez-vous à la documentation AWS.

## Références
- [Creating and connecting to a MySQL DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.MySQL.html)
- [Amazon RDS for MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_MySQL.html)
- [Getting started with Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.html)