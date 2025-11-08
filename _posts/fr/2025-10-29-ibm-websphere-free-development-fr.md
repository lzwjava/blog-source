---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Options de développement gratuites pour IBM WebSphere
translated: true
type: note
---

### IBM WebSphere Application Server (WAS) - Versions Gratuites ou Communautaires

IBM WebSphere Application Server (WAS), le serveur d'applications d'entreprise traditionnel complet, ne propose pas d'édition perpétuellement gratuite ou communautaire pour une utilisation en production à compter d'octobre 2025. L'ancien WebSphere Application Server Community Edition (WASCE), qui était un serveur gratuit compatible Java EE 6, a été abandonné vers 2012 et n'est plus pris en charge ou disponible auprès d'IBM.

Cependant, IBM propose **des options gratuites pour le développement et les tests** :
- **WebSphere Application Server Developer Tools** : Un ensemble d'outils léger et gratuit, basé sur Eclipse, pour développer, assembler et déployer des applications Java EE, OSGi et web. Ils peuvent être téléchargés directement depuis IBM et intégrés à des EDI comme Eclipse.
- **Runtime Développeur Gratuit** : IBM propose une version runtime de WAS gratuite, spécifiquement pour les développeurs afin de tester les applications (par exemple, WebSphere 9). Elle est disponible au téléchargement via les ressources pour développeurs d'IBM et convient aux environnements de non-production comme le développement local ou la R&D interne.

Pour les déploiements en production, la version traditionnelle de WAS nécessite une licence payante, bien qu'IBM propose un essai de 60 jours pour l'évaluation.

### Alternative : WebSphere Liberty
Si vous êtes ouvert à une alternative moderne et légère au sein de la famille WebSphere, **WebSphere Liberty** est fortement recommandé par IBM pour la plupart des cas d'usage :
- **Liberty Core** : Cette version est gratuite pour le développement et la production (sans le support IBM). Elle prend en charge un sous-ensemble des fonctionnalités Jakarta EE et est idéale pour les microservices, les applications cloud-natives et les charges de travail plus simples.
- Les éditions Liberty complètes (avec des fonctionnalités avancées comme le clustering ou la sécurité premium) nécessitent une licence pour la production, mais la version de base reste gratuite.
- Liberty est issu du projet open source **Open Liberty**, qui est entièrement gratuit et piloté par la communauté.

Vous pouvez télécharger Liberty pour les développeurs depuis le site d'IBM sans restrictions pour des tests non commerciaux.

Pour les derniers téléchargements et les détails de licence, consultez les pages officielles d'IBM ou Passport Advantage (nécessite un identifiant IBM).

**Références** :
- [WebSphere Application Server Developer Tools Releases](https://www.ibm.com/support/pages/websphere-application-server-developer-tools-and-liberty-developer-tools-releases)
- [Installing WebSphere 9 for Developers](https://www.genuitec.com/docs/servers/installing-websphere-9-developers/)
- [WebSphere Liberty for Developers](https://www.ibm.com/support/pages/websphere-liberty-developers)
- [IBM WebSphere Application Server Community Edition (Wikipedia)](https://en.wikipedia.org/wiki/IBM_WebSphere_Application_SERVER_Community_Edition)
- [Exploring IBM WebSphere Application Server](https://www.jrebel.com/blog/exploring-ibm-websphere-application-server)
- [Open Liberty](https://openliberty.io/)