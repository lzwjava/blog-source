---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Éviter les boucles de proxy du démon Docker
translated: true
type: note
---

### Pourquoi `"no-proxy": "localhost,127.0.0.1,.local"` est crucial dans `daemon.json` de Docker

Lorsque vous configurez le démon Docker avec des paramètres de proxy comme `"http-proxy": "http://localhost:7890"` (courant pour des outils comme Clash fonctionnant localement), le démon applique ces règles par défaut à **tout** le trafic réseau sortant. Cela inclut les connexions aux registres externes (par exemple, `registry-1.docker.io` pour télécharger des images comme `hello-world`).

Cependant, sans la directive `no-proxy`, le démon Docker tente aussi de router **les connexions locales**—telles que la poignée de main TCP initiale vers votre serveur proxy lui-même sur `localhost:7890`—via le même proxy. Cela crée une **boucle de proxy** classique :

1.  Docker a besoin de récupérer une image depuis `registry-1.docker.io`.
2.  Il tente de se connecter via le proxy sur `localhost:7890`.
3.  Mais pour atteindre `localhost:7890`, les paramètres du proxy s'appliquent à nouveau, forçant Docker à... se connecter via le proxy sur `localhost:7890`.
4.  Cette récursion infinie échoue au niveau TCP car le proxy ne peut pas proxyfier une connexion à lui-même (cela conduit à une boucle auto-référentielle sans résolution).
5.  La connexion est abandonnée de manière inattendue, ce qui entraîne l'erreur `proxyconnect tcp: EOF` (EOF signifie "end of file", signalant une fermeture prématurée pendant la négociation/poignée de main du proxy).

L'ajout de `"no-proxy": "localhost,127.0.0.1,.local"` indique explicitement au démon de **contourner le proxy** pour le trafic destiné à :
- `localhost` (le nom d'hôte de loopback de votre machine),
- `127.0.0.1` (l'adresse de loopback IPv4),
- les domaines `.local` (courants pour la résolution mDNS/réseau local).

Cela permet à Docker de se connecter **directement** au serveur proxy sur localhost sans passer par lui-même. Une fois connecté, le proxy peut alors gérer correctement la requête externe vers le registre Docker (par exemple, via HTTP CONNECT pour le trafic HTTPS).

En bref : Cela empêche le démon de "proxyfier le proxy", garantissant que l'accès au proxy local fonctionne tout en routant le trafic destiné à Internet (comme les téléchargements d'images) à travers lui.

Si votre configuration implique d'autres services locaux (par exemple, des registres internes ou des conteneurs communiquant localement), étendre `no-proxy` avec ces domaines/IP peut éviter des problèmes similaires.

[Configuration du Proxy du Démon Docker](https://docs.docker.com/engine/daemon/proxy/)  
[Discussion sur le Forum des Paramètres de Proxy Docker](https://forums.docker.com/t/proxy-settings-for-the-docker-daemon/132089)  
[Guide du Proxy Docker pour les Pare-feu d'Entreprise](https://www.datacamp.com/tutorial/docker-proxy)