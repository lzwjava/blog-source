---
audio: false
generated: true
lang: fr
layout: post
title: Pourquoi les opérations Git échouent sur les réseaux mobiles chinois
translated: true
type: note
---

C'est un problème courant lors de l'utilisation de certains réseaux mobiles en Chine, en particulier avec des services comme Git qui reposent sur des ports et protocoles spécifiques. Voici une explication des raisons pour lesquelles cela se produit et comment le résoudre :

**Pourquoi les opérations Git échouent sur les réseaux mobiles chinois :**

* **Blocage/limitation de port :**
    * Les opérateurs de réseaux mobiles en Chine mettent parfois en place du shaping de trafic ou du blocage de ports, en particulier pour les ports non standard utilisés par Git (comme le port SSH 22). Cela est souvent fait pour gérer la bande passante du réseau ou pour des raisons de sécurité.
    * Même si le port 22 n'est pas complètement bloqué, il peut être fortement limité, entraînant des connexions extrêmement lentes ou des timeouts, qui apparaissent comme des opérations Git "bloquées".
* **Problèmes DNS :**
    * Bien que vous puissiez accéder à des sites web comme GitHub et Google, les opérations Git reposent sur la résolution d'hôtes spécifiques (par exemple, `github.com`) via le DNS. Si la résolution DNS est lente ou peu fiable, cela peut faire planter Git.
* **Perte de paquets/latence :**
    * Les réseaux mobiles, en particulier lorsqu'ils sont utilisés comme hotspots, peuvent avoir une latence et une perte de paquets plus élevées que les connexions filaires. Cela peut perturber la connexion SSH utilisée par Git, entraînant des échecs.
* **Interférence du pare-feu :**
    * Le "Grand Firewall" de Chine peut interférer avec les connexions SSH, même si elles ne sont pas explicitement bloquées. L'inspection approfondie des paquets du pare-feu peut parfois provoquer une instabilité de la connexion.
* **Problèmes de MTU :**
    * Les problèmes d'Unité de Transmission Maximale (MTU) peuvent causer des problèmes de transfert de données, et les réseaux mobiles ont parfois des valeurs MTU plus petites que les réseaux filaires.

**Comment résoudre les problèmes de push/pull Git sur les réseaux mobiles chinois :**

1.  **Utiliser HTTPS au lieu de SSH :**
    * Git via HTTPS utilise le port 443, qui est généralement ouvert pour le trafic web. C'est la solution de contournement la plus fiable.
    * Pour changer votre remote Git en HTTPS :
        * Ouvrez votre terminal.
        * Accédez à votre dépôt Git.
        * Exécutez la commande suivante, en remplaçant `your_username` et `your_repository` par vos informations GitHub :
            ```bash
            git remote set-url origin https://github.com/your_username/your_repository.git
            ```
    * Si vous devez fournir un nom d'utilisateur et un mot de passe, vous pouvez utiliser l'assistant d'identification Git ou utiliser un jeton d'accès personnel.
2.  **Utiliser un VPN :**
    * Un VPN fiable peut contourner les restrictions du réseau et fournir une connexion plus stable.
    * Connectez-vous à un serveur VPN en dehors de la Chine avant de tenter des opérations Git.
    * Soyez conscient que les VPN peuvent également connaître des instabilités et des problèmes de vitesse.
3.  **Configurer le port SSH (si SSH est nécessaire) :**
    * Si vous devez absolument utiliser SSH, essayez de configurer Git pour utiliser un port différent (par exemple, 443) qui pourrait être moins susceptible d'être bloqué.
    * Modifiez votre fichier `~/.ssh/config` :
        ```
        Host github.com
            Hostname ssh.github.com
            Port 443
            User git
        ```
    * Ensuite, changez votre URL remote Git pour utiliser ssh.github.com :
        ```bash
        git remote set-url origin git@ssh.github.com:your_username/your_repository.git
        ```
4.  **Vérifier les paramètres MTU :**
    * Si vous soupçonnez des problèmes de MTU, essayez de réduire la taille de votre MTU.
    * Sur macOS, vous pouvez utiliser la commande `networksetup` pour ajuster le MTU.
    * Cependant, modifier le MTU est généralement une étape de dépannage plus avancée et doit être effectuée avec prudence.
5.  **Vérifier les paramètres DNS :**
    * Essayez d'utiliser un serveur DNS public, comme Google DNS (8.8.8.8 et 8.8.4.4) ou Cloudflare DNS (1.1.1.1 et 1.0.0.1).
    * Vous pouvez configurer les paramètres DNS dans les préférences réseau de votre macOS.
6.  **Utiliser un proxy Git :**
    * Si vous avez accès à un serveur proxy, vous pouvez configurer Git pour l'utiliser.
    * Définissez les variables de configuration Git `http.proxy` et `https.proxy` :
        ```bash
        git config --global http.proxy http://proxy_address:proxy_port
        git config --global https.proxy https://proxy_address:proxy_port
        ```
    * Si le proxy nécessite une authentification, vous pouvez inclure le nom d'utilisateur et le mot de passe dans l'URL du proxy.
7.  **Essayer d'utiliser SSH via Websockets :**
    * Certains outils et services vous permettent de tunneliser le trafic SSH via des websockets, ce qui peut être utile si les ports SSH standard sont bloqués.
    * Il s'agit d'une technique plus avancée qui nécessite la configuration d'un serveur prenant en charge SSH via websockets.

**Considérations importantes :**

* Les conditions des réseaux mobiles peuvent varier considérablement, donc ce qui fonctionne à un endroit ou à un moment donné pourrait ne pas fonctionner ailleurs.
* Soyez conscient des conditions d'utilisation de votre fournisseur de réseau mobile et des restrictions potentielles sur l'utilisation de VPN ou d'autres solutions de contournement.
* HTTPS est généralement la meilleure solution pour la plupart des utilisateurs.