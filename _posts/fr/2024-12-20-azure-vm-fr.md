---
audio: false
generated: false
lang: fr
layout: post
title: Configuration d'un Serveur Azure
translated: true
---

Configurer un serveur sur Microsoft Azure et le configurer pour ouvrir des ports spécifiques est essentiel pour diverses applications, y compris l'hébergement de services, les proxys, et bien plus encore. Ce guide vous expliquera étape par étape comment créer une machine virtuelle (VM) sur Azure et configurer le pare-feu pour ouvrir le port 1080.

## Table des matières

1. [Prérequis](#prerequisites)
2. [Création d'une machine virtuelle Azure](#creating-an-azure-virtual-machine)
3. [Configuration du pare-feu pour ouvrir le port 1080](#configuring-the-firewall-to-open-port-1080)
4. [Test de la configuration](#testing-the-configuration)
5. [Conclusion](#conclusion)

## Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants :

- Un compte [Microsoft Azure](https://azure.microsoft.com/) actif.
- Connaissances de base sur l'utilisation du portail Azure.
- Un client SSH (comme Terminal sur macOS/Linux ou PuTTY sur Windows) pour accéder à la machine virtuelle.

## Création d'une machine virtuelle Azure

1. Connectez-vous au Portail Azure :
   Accédez au [Portail Azure](https://portal.azure.com/) et connectez-vous avec vos identifiants.

2. Créer une nouvelle machine virtuelle :
   - Cliquez sur "Créer une ressource" dans le coin supérieur gauche.
   - Sélectionnez "Machine virtuelle" dans la liste des ressources disponibles.

3. Configurer les bases de la machine virtuelle :
   - Abonnement : Choisissez votre abonnement Azure.
   - Groupe de ressources : Créez un nouveau groupe de ressources ou sélectionnez-en un existant.
   - Nom de la machine virtuelle : Entrez un nom pour votre machine virtuelle (par exemple, `AzureServer`).
   - Région : Sélectionnez la région la plus proche de votre public cible.
   - Image : Choisissez une image de système d'exploitation (par exemple, Ubuntu 22.04 LTS).
   - Taille : Sélectionnez une taille de machine virtuelle en fonction de vos besoins en performance.
   - Authentification : Choisissez une clé publique SSH pour un accès sécurisé. Téléversez votre clé publique SSH.

4. Configurer le réseau :
   - Assurez-vous que la machine virtuelle est placée dans le réseau virtuel et le sous-réseau appropriés.
   - Laissez l'adresse IP publique activée pour permettre un accès externe.

5. Vérifiez et Créez :
   - Vérifiez vos configurations.
   - Cliquez sur "Créer" pour déployer la machine virtuelle. Le déploiement peut prendre quelques minutes.

## Configuration du pare-feu pour ouvrir le port 1080

Une fois que votre machine virtuelle est opérationnelle, vous devrez configurer le groupe de sécurité réseau (NSG) d'Azure pour autoriser le trafic sur le port 1080.

1. Accédez aux Paramètres de Réseau de Votre Machine Virtuelle :
   - Dans le Portail Azure, allez à "Machines Virtuelles".
   - Sélectionnez votre machine virtuelle (`AzureServer`).
   - Cliquez sur "Réseau" dans la barre latérale gauche.

2. Identifier le groupe de sécurité réseau (NSG) :
   - Sous "Interface réseau", localisez le NSG associé.
   - Cliquez sur le NSG pour gérer ses règles.

3. Ajouter une règle de sécurité entrante :
   - Dans les paramètres du NSG, allez à "Règles de sécurité entrantes".
   - Cliquez sur "Ajouter" pour créer une nouvelle règle.

4. Configurez la Règle :
   - Source : Toute (ou spécifiez une plage pour une sécurité renforcée).
   - Plages de ports source : `*`
   - Destination : Toute
   - Plages de ports de destination : `1080`
   - Protocole : TCP
   - Action : Autoriser
   - Priorité : `1000` (assurez-vous qu'elle ne rentre pas en conflit avec les règles existantes).
   - Nom : `Allow-1080-TCP`

5. Enregistrer la Règle :
   - Cliquez sur "Ajouter" pour appliquer la nouvelle règle.

## Tester la Configuration

Après avoir configuré le pare-feu, il est essentiel de vérifier que le port 1080 est ouvert et accessible.

1. Utilisez Telnet pour vérifier l'accessibilité du port :
   Depuis votre machine locale, exécutez :

   ```bash
   telnet <VOTRE_IP_VM> 1080
   ```

   - Remplacez `<YOUR_VM_IP>` par l'adresse IP publique de votre machine virtuelle.
   - Si la connexion est réussie, le port est ouvert et accessible.

2. Outils alternatifs de vérification des ports :
   - Netcat (`nc`) :
     ```bash
     nc -zv <VOTRE_IP_VM> 1080
     ```
   - Vérificateurs de ports en ligne :
     Utilisez des services en ligne comme [canyouseeme.org](https://canyouseeme.org/) pour vérifier si le port 1080 est ouvert.

3. Dépannage :
   - Problèmes de connexion : Vérifiez que les règles du NSG sont correctement configurées et que les pare-feu locaux sur la VM sont configurés pour autoriser le trafic sur le port 1080.
   - IP incorrecte : Assurez-vous d'utiliser la bonne adresse IP publique de votre VM.

## Conclusion

En suivant ce guide, vous avez réussi à configurer une machine virtuelle Azure et à configurer le pare-feu pour ouvrir le port 1080. Cette configuration pose les bases pour déployer diverses applications ou services nécessitant un accès à des ports spécifiques.

Pour des configurations supplémentaires, comme la mise en place de services proxy ou d'autres applications sur le port 1080, consultez nos articles dédiés sur [Configuration du Proxy V2Ray](#) et [Génération d'une URL vmess personnalisée](#).