---
audio: false
generated: false
lang: fr
layout: post
title: Configurez Votre Serveur Proxy
translated: true
---

* Pour configurer un serveur, utilisez Outline Manager : [https://getoutline.org](https://getoutline.org).

* Les fournisseurs d'hébergement recommandés incluent DigitalOcean, Google Cloud, Amazon Lightsail, Azure, Vultr et Linode. Pour des performances optimales, choisissez des emplacements de serveurs à Singapour ou Tokyo. Bien que Hong Kong soit également une option viable, sachez que certains outils d'IA comme ChatGPT et Claude sont restreints dans cette région.

* Vous pouvez encore utiliser des outils comme Deepseek, Mistral, Grok et l'API Gemini (via Cursor) avec des serveurs à Hong Kong. En utilisant la réflexion par inversion, puisque d'autres peuvent éviter les serveurs à Hong Kong, ils ont tendance à être moins congestionnés.

* Prenez en compte l'emplacement du serveur et la distance. Pour ceux à Guangzhou, Hong Kong est une bonne option pour héberger un serveur proxy. Utilisez Speedtest pour mesurer la vitesse du réseau.

* Si vous vous souciez de la vitesse, la meilleure option, à ma connaissance, est d'utiliser un serveur Aliyun Hong Kong avec une adresse IP élastique BGP (premium). L'IP est élastique, ce qui la rend facile à relier à une nouvelle si l'IP actuelle est bannie. De plus, cette connexion BGP (premium) est optimisée par Aliyun Cloud, offrant des vitesses rapides.

* Des protocoles comme Shadowsocks, VMess et Trojan peuvent être facilement bannis.

* Utilisez Linode pour une migration rapide de serveur.

* Vous pourriez avoir besoin d'un script pour renouveler automatiquement votre serveur chaque jour.

* Si le serveur proxy est banni par le GFW ou rencontre d'autres problèmes, vous pouvez utiliser une carte SIM China Telecom Macau pour partager les données cellulaires avec votre ordinateur portable. Cela vous permet de configurer un nouveau serveur.

* Pour les services cloud comme Google Cloud Platform, la configuration d'un nouveau serveur nécessite un serveur proxy existant. Cependant, des fournisseurs comme DigitalOcean ou Vultr peuvent être configurés directement sans besoin d'un serveur proxy.

* Utilisez [Auto SS Config](https://github.com/lzwjava/auto-ss-config) pour générer et télécharger des URL d'abonnement Shadowsocks ou Clash.

* Utilisez la fonctionnalité de snapshot dans Digital Ocean. Si l'IP du serveur est bannie, créez un nouveau droplet à partir du snapshot du serveur et exécutez `install.sh` à nouveau.

* Utilisez la fonctionnalité d'IP réservée dans Digital Ocean. Si l'IP du serveur est bannie, attribuez une nouvelle IP réservée.

* Nous utilisons Outline Manager pour configurer nos propres serveurs car il est rapide et nous permet de profiter du serveur par nous-mêmes. Les nœuds des fournisseurs VPN peuvent souvent être peu fiables. Nos serveurs peuvent également rencontrer des problèmes, mais nous avons une connaissance beaucoup plus détaillée de la situation. Nous pouvons également choisir différents fournisseurs de cloud. De plus, nous savons si nous utilisons China Telecom ou China Mobile, et si nous utilisons le Wi-Fi domestique ou les données cellulaires.

* Il est probablement inutile d'installer OpenWrt sur un routeur pour configurer un proxy. Le principal problème est que le GFW peut facilement bannir l'adresse IP de votre serveur proxy. Il est préférable d'utiliser une méthode d'abonnement, comme avec Clash, pour modifier facilement les paramètres sur votre routeur.