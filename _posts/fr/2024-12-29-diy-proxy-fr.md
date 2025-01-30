---
audio: false
lang: fr
layout: post
title: Configurer Votre Serveur Proxy
translated: true
---

* Pour configurer un serveur, utilisez Outline Manager : [https://getoutline.org](https://getoutline.org).  

* Les fournisseurs d'hébergement recommandés incluent DigitalOcean, Google Cloud, Amazon Lightsail, Azure, Vultr ou Linode. Privilégiez les régions de Singapour ou de Tokyo. Évitez la région de Hong Kong, car des outils comme ChatGPT et Claude y sont interdits.  

* Si cela ne vous dérange pas que ChatGPT et Claude soient interdits à Hong Kong, c'est toujours une option viable. Vous pouvez utiliser des outils comme Deepseek, Mistral, Grok et l'API Gemini avec des serveurs à Hong Kong. Utilisez la pensée inverse ; d'autres peuvent éviter les serveurs de Hong Kong, ce qui les rend moins encombrés.  

* Prenez en compte l'emplacement du serveur et la distance. Pour ceux qui se trouvent à Guangzhou, Hong Kong est une bonne option pour héberger un serveur proxy. Utilisez Speedtest pour mesurer la vitesse du réseau.  

* Les protocoles tels que Shadowsocks, VMess et Trojan peuvent facilement être bannis.  

* Utilisez Linode pour une migration rapide des serveurs.  

* Vous pourriez avoir besoin d'un script pour renouveler automatiquement votre serveur chaque jour.  

* Si le serveur proxy est banni par le GFW ou rencontre d'autres problèmes, vous pouvez utiliser une carte SIM China Telecom Macau pour partager des données cellulaires avec votre ordinateur portable. Cela vous permet de configurer un nouveau serveur.  

* Pour les services cloud comme Google Cloud Platform, la configuration d'un nouveau serveur nécessite un serveur proxy existant. Cependant, des fournisseurs comme DigitalOcean ou Vultr peuvent être configurés directement sans avoir besoin d'un serveur proxy.  

* Utilisez [Auto SS Config](https://github.com/lzwjava/auto-ss-config) pour générer et télécharger les URL d'abonnement Shadowsocks ou Clash.  

* Utilisez la fonctionnalité de snapshot dans Digital Ocean. Si l'IP du serveur est bannie, créez un nouveau droplet à partir du snapshot du serveur et exécutez à nouveau `install.sh`.  

* Utilisez la fonctionnalité d'IP réservée dans Digital Ocean. Si l'IP du serveur est bannie, attribuez une nouvelle IP réservée.  

* Nous utilisons Outline Manager pour configurer nos propres serveurs car c'est rapide et cela nous permet de profiter du serveur nous-mêmes. Les nœuds des fournisseurs de VPN peuvent souvent être peu fiables. Nos serveurs peuvent également rencontrer des problèmes, mais nous avons une connaissance beaucoup plus détaillée de la situation. Nous pouvons également choisir différents fournisseurs de cloud. De plus, nous savons si nous utilisons China Telecom ou China Mobile, et si nous utilisons le Wi-Fi domestique ou les données cellulaires.  

* Il n'est probablement pas utile d'installer OpenWrt sur un routeur pour configurer un proxy. Le principal problème est que le GFW peut facilement bannir l'adresse IP de votre serveur proxy. Il est préférable d'utiliser une méthode d'abonnement, comme avec Clash, pour changer facilement les paramètres sur votre routeur.