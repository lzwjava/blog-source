---
audio: false
generated: false
image: false
lang: fr
layout: post
title: Configuration d'un serveur Google Cloud
translated: true
type: post
---

La configuration d'un serveur proxy dans Google Cloud vous permet de router votre trafic internet de manière sécurisée via une instance cloud, améliorant ainsi la confidentialité et contournant les restrictions. Dans ce guide, nous allons vous expliquer étape par étape comment configurer un serveur proxy de base dans Google Cloud et définir les règles de pare-feu nécessaires pour autoriser le trafic.

## Table des matières
1. [Création d'une instance de machine virtuelle Google Cloud](#création-dune-instance-de-machine-virtuelle-google-cloud)
2. [Configuration du serveur proxy](#configuration-du-serveur-proxy)
3. [Configuration des règles de pare-feu](#configuration-des-règles-de-pare-feu)
4. [Test du serveur proxy](#test-du-serveur-proxy)
5. [Conclusion](#conclusion)

---

## Création d'une instance de machine virtuelle sur Google Cloud

Avant de configurer le serveur proxy, vous devrez créer une instance de machine virtuelle (VM) dans Google Cloud.

1. Connectez-vous à Google Cloud Console : Rendez-vous sur [Google Cloud Console](https://console.cloud.google.com/) et connectez-vous à votre compte.

2. Créez une nouvelle instance de machine virtuelle (VM) :
   - Accédez à Compute Engine > Instances de VM.
   - Cliquez sur Créer une instance.
   - Choisissez la région et le type de machine souhaités. Pour simplifier, vous pouvez utiliser les paramètres par défaut ou opter pour une configuration légère comme l'instance `e2-micro`.
   - Dans la section Pare-feu, cochez à la fois Autoriser le trafic HTTP et Autoriser le trafic HTTPS pour permettre l'accès web.

3. Configurez l'accès SSH :
   - Dans la section Clés SSH, ajoutez votre clé publique SSH pour accéder à distance à l'instance. Cela est essentiel pour configurer votre serveur proxy ultérieurement.

4. Cliquez sur Créer pour lancer votre VM.

Une fois la machine virtuelle configurée, vous pouvez vous y connecter en utilisant SSH depuis la Google Cloud Console ou via le terminal avec :

```bash
gcloud compute ssh <nom-de-votre-vm>
```

---

## Configuration du serveur proxy

Une fois votre machine virtuelle configurée, vous pouvez configurer n'importe quel logiciel de serveur proxy de votre choix. Le logiciel proxy doit être installé et configuré pour accepter les connexions sur le port souhaité (par exemple, `3128` pour les configurations proxy courantes). Assurez-vous que le logiciel autorise les connexions depuis des clients distants.

---

## Configuration des règles de pare-feu

Pour autoriser le trafic vers votre serveur proxy, vous devrez configurer les règles de pare-feu de Google Cloud afin d'ouvrir le port nécessaire.

1. Accédez aux règles de pare-feu dans la console Google Cloud :
   - Allez dans Réseau VPC > Règles de pare-feu dans la console Google Cloud.

2. Créez une nouvelle règle de pare-feu :
   - Cliquez sur Créer une règle de pare-feu.
   - Entrez un nom pour la règle, par exemple `allow-proxy-access`.
   - Définissez la Direction du trafic sur Entrant (trafic entrant).
   - Définissez l'Action en cas de correspondance sur Autoriser.
   - Définissez les Cibles sur Toutes les instances du réseau ou Balises de cible spécifiées (si vous préférez un contrôle plus précis).
   - Sous Plages d'adresses IP sources, vous pouvez définir `0.0.0.0/0` pour autoriser l'accès depuis toutes les adresses IP, ou le limiter à des IP ou plages spécifiques pour une meilleure sécurité.
   - Sous Protocoles et ports, sélectionnez Protocoles et ports spécifiés et entrez le port utilisé par votre serveur proxy (par exemple, `tcp:3128`).

3. Enregistrer la règle de pare-feu :
   Après avoir configuré la règle, cliquez sur Créer pour activer le pare-feu.

---

## Tester le serveur proxy

Après avoir configuré le pare-feu, il est temps de tester votre serveur proxy.

1. Tester le Proxy depuis votre Machine Locale :

Vous pouvez configurer les paramètres du proxy de votre navigateur ou système sur votre machine locale pour utiliser l'adresse IP externe de votre machine virtuelle Google Cloud et le port sur lequel votre serveur proxy écoute (par exemple, `3128`).

2. Tester avec la ligne de commande :

   Vous pouvez également tester le proxy avec `curl` en définissant les variables d'environnement du proxy :

```bash
export http_proxy=http://<votre-ip-externe-vm>:3128
export https_proxy=http://<votre-ip-externe-vm>:3128
curl -I http://example.com
```

Si la connexion est réussie, vous devriez voir une réponse du site web.

---

## Conclusion

En suivant ce guide, vous avez appris à configurer un serveur proxy sur Google Cloud et à définir des règles de pare-feu pour autoriser le trafic entrant. Cette configuration offre un moyen simple de router votre trafic internet de manière sécurisée via le cloud, de contourner les restrictions réseau et d'améliorer votre confidentialité.