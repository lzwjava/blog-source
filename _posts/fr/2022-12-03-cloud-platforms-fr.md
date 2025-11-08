---
audio: false
generated: false
image: true
lang: fr
layout: post
title: Certaines Plateformes Cloud Mondiales
translated: true
type: post
---

<div align="center"><img src="/assets/images/cloud/platform.jpg" width="400px"/><img/></div>

* [Azure](#azure)
* [AWS Lightsail](#aws-lightsail)
* [Digital Ocean](#digital-ocean)
* [Vultr](#vultr)
* [Google Cloud - Échec](#google-cloud---échec)
* [Aperçu](#aperçu)
* [Résumé](#résumé)

J'ai récemment essayé quelques plateformes cloud. Je les ai utilisées pour configurer mon serveur proxy. Auparavant, j'utilisais un serveur proxy tiers. Ce serveur est utilisé par de nombreux utilisateurs, donc la vitesse est parfois lente. J'ai essayé de configurer le mien pour résoudre ce problème.

## Azure

Azure est une bonne option. J'ai créé 3 machines virtuelles ici. Parce que la plateforme m'a offert 200 dollars de crédit gratuitement. Mes machines sont situées au Qatar, aux États-Unis et à Hong Kong. Le temps de ping depuis mon ordinateur portable à Guangzhou vers le serveur au Qatar est de 150 ms. Actuellement, les paquets de ping vers le serveur aux États-Unis sont perdus à 100 %. Il y a deux jours, je pouvais le pinguer avec succès. Et les paquets de ping vers le serveur de Hong Kong sont également perdus à 100 %. Je les ai testés dans mon client proxy iOS et ils ne pouvaient pas se connecter. Je dois les arrêter. Bien que le coût soit gratuit, un serveur perdu ne m'est d'aucune utilité.

<div align="center"><img src="/assets/images/cloud/azure.png" /><img/></div>

Voyons la console et l'onglet réseau, ci-dessus et ci-dessous.

<div align="center"><img src="/assets/images/cloud/network.png" /><img/></div>

Ma configuration réseau personnalisée est simple. Je laisse simplement tous les ports entre 1024 et 65535 ouverts pour tous les protocoles. Comme il s'agit de mon serveur proxy, je n'ai aucune donnée secrète ou programme sensible à l'intérieur. Je suis donc la suggestion de l'application Outline pour procéder ainsi.

## AWS Lightsail

Lightsail est un produit léger d'AWS. AWS propose de nombreux produits. Parfois, nous souhaitons simplement créer quelques machines virtuelles à l'intérieur. C'est pourquoi ils nous offrent AWS Lightsail.

<div align="center"><img src="/assets/images/cloud/lightsail.png" /><img/></div>

## Digital Ocean

J'ai beaucoup utilisé Digital Ocean parmi les plateformes cloud à l'étranger, en particulier entre 2016 et 2018. Je dépensais 5 dollars chaque mois.

Nous créons un droplet comme ceci :

<div align="center"><img src="/assets/images/cloud/do.png" /><img/></div>

Voici mon historique de facturation :

<div align="center"><img src="/assets/images/cloud/bill.png" /><img/></div>

## Vultr

J'ai utilisé Vultr de 2018 à 2020.

<div align="center"><img src="/assets/images/cloud/vultr.png" /><img/></div>

## Google Cloud - Échec

Je veux aussi essayer Google Cloud. Cependant, j'ai échoué. Ils ne prennent pas en charge les utilisateurs en Chine. Bien que nous puissions fournir de fausses informations en prétendant être des citoyens d'autres pays, nous n'avons pas la carte de crédit correspondante pour nous inscrire avec succès.

<div align="center"><img src="/assets/images/cloud/google.png" /><img/></div>

## Plan

Outline n'est pas une plateforme cloud. C'est un outil de proxy. Parce qu'il m'aide à configurer mon serveur proxy, je dois écrire un paragraphe séparé pour le féliciter. Il est vraiment utile. Vous pouvez en apprendre plus en le recherchant en ligne.

<div align="center"><img src="/assets/images/cloud/outline.png" /><img/></div>

## Résumé

Le serveur le moins cher avec la configuration la plus basse coûte généralement environ 5 dollars par mois. Cela suffit pour servir de serveur proxy à utiliser par quelques utilisateurs. Les serveurs situés à Singapour, Hong Kong ou dans d'autres régions d'Asie sont généralement connectés plus rapidement que les serveurs aux États-Unis ou en Europe. Et parfois, lorsque vous configurez le serveur juste après son installation, il fonctionne parfaitement. Cependant, après quelques jours, il fonctionne comme un zombie. Donc, en ce qui concerne la vitesse et la stabilité, vous ne pouvez découvrir la vérité qu'à travers votre utilisation quotidienne.