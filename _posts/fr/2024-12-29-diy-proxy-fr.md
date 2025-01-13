---
audio: true
lang: fr
layout: post
title: Configurer Votre Serveur Proxy
translated: true
---

* Pour configurer un serveur, utilisez Outline Manager : [https://getoutline.org](https://getoutline.org).  
* Les fournisseurs d'hébergement recommandés incluent DigitalOcean, Google Cloud, Amazon Lightsail, Azure, Vultr ou Linode. Privilégiez les régions de Singapour ou Tokyo. Évitez la région de Hong Kong, car des outils comme ChatGPT et Claude y sont interdits.  
* Les protocoles tels que Shadowsocks, VMess et Trojan peuvent facilement être bloqués.  
* Utilisez Linode pour une migration rapide du serveur.  
* Vous pourriez avoir besoin d'un script pour renouveler automatiquement votre serveur chaque jour.  
* Si le serveur proxy est bloqué par le GFW ou rencontre d'autres problèmes, vous pouvez utiliser une carte SIM China Telecom Macau pour partager les données cellulaires avec votre ordinateur portable. Cela vous permet de configurer un nouveau serveur.  
* Pour les services cloud comme Google Cloud Platform, la configuration d'un nouveau serveur nécessite un serveur proxy existant. Cependant, des fournisseurs comme DigitalOcean ou Vultr peuvent être configurés directement sans avoir besoin d'un serveur proxy.
* Utilisez [Auto SS Config](https://github.com/lzwjava/auto-ss-config) pour générer et télécharger les URL d'abonnement Shadowsocks ou Clash.
* Utilisez la fonctionnalité de snapshot dans Digital Ocean. Si l'IP du serveur est bloquée, créez un nouveau droplet à partir du snapshot du serveur et exécutez à nouveau `install.sh`.
* Utilisez la fonctionnalité d'IP réservée dans Digital Ocean. Si l'IP du serveur est bloquée, attribuez une nouvelle IP réservée.