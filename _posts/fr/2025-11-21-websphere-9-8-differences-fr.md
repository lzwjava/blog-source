---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Principales différences entre WebSphere 9.0 et 8.0
translated: true
type: note
---

### Principales différences entre IBM WebSphere Application Server (WAS) 9.0 et 8.0

IBM WebSphere Application Server (WAS) est un serveur d'applications Java EE de niveau entreprise. La version 8.0 (publiée en 2011) a introduit la conformité Java EE 6, tandis que la version 9.0 (publiée en 2017) est passée à Java EE 7 en se concentrant sur la modernisation du profil traditionnel pour l'aligner sur des exécutifs plus légers et adaptés au cloud, comme Liberty. Ci-dessous, je décrirai les différences clés dans un tableau pour plus de clarté, basé sur la documentation officielle d'IBM et les notes de publication. Celles-ci concernent le support Java, la conformité aux standards, l'architecture et le déploiement.

| Aspect                               | WAS 8.0                                                                 | WAS 9.0                                                                 |
|--------------------------------------|-------------------------------------------------------------------------|-------------------------------------------------------------------------|
| **Support Java SE**                 | Utilise par défaut Java SE 6 ; support optionnel pour Java SE 7 via configuration. | Utilise par défaut Java SE 8 comme plateforme principale, utilisant IBM SDK Java 8 pour une compatibilité totale avec Oracle Java 8. Cela permet les expressions lambda, les streams et autres fonctionnalités de SE 8. |
| **Conformité Java EE**              | Support complet de Java EE 6, incluant JPA 2.0, JSF 2.0 et Servlet 3.0. | Support complet de Java EE 7, ajoutant des fonctionnalités comme WebSocket 1.0, JSON-P 1.0, Batch 1.0 et des utilitaires de concurrence améliorés. Cela met l'édition traditionnelle au niveau des capacités de Liberty des versions antérieures. |
| **Intégration du profil Liberty**   | Liberty introduit dans la 8.5 (pas dans le cœur de la 8.0) ; la 8.0 se concentre uniquement sur le profil traditionnel complet. | Runtime Liberty profondément intégré (version 16.0.0.2) comme alternative légère et modulaire au profil complet, optimisé pour les applications cloud-native. Liberty est inclus et supporte la livraison continue. |
| **Modèle de déploiement**           | Principalement sur site ; installé via Installation Manager avec des éditions comme Base et Network Deployment (ND) pour le clustering. | Première version publiée simultanément sur site et en tant que service sur IBM Cloud. Prend en charge les déploiements hybrides cloud avec de meilleurs crochets pour la conteneurisation. |
| **Performance et Gestion**          | Jusqu'à 20-26 % de gains de débit par rapport à WAS 7 ; gestion intelligente dans l'édition ND. | S'appuie sur la 8.0 avec des optimisations supplémentaires pour l'efficacité des ressources ; outils administratifs améliorés pour la migration et la comparaison de configurations. |
| **Fin de support**                  | Support étendu terminé en 2019 ; ne reçoit plus de correctifs. | Support actif jusqu'au moins 2027, avec des correctifs réguliers (par exemple, 9.0.5.x) adressant la sécurité et la compatibilité. |
| **Considérations de migration**     | N/A (référence). | Migration facilitée depuis la 8.x via des outils comme l'outil de comparaison de configurations ; alignement automatique des ports et gestion des API obsolètes pour la transition vers Java SE 8. |

#### Points clés à retenir
- **Plus grand saut** : Le passage à Java EE 7 et Java SE 8 est le plus significatif, permettant les fonctionnalités et standards Java modernes qui étaient prévisualisés dans Liberty plus tôt. Si vous exécutez des applications Java EE 6 héritées, la migration vers la 9.0 est simple mais peut nécessiter des tests pour les changements spécifiques à SE 8.
- **Quand mettre à niveau** : Choisissez la 9.0 pour les besoins cloud/hybrides ou les fonctionnalités EE 7 ; restez sur la 8.0 (ou appliquez les correctifs vers la 8.5.5) uniquement pour la maintenance à court terme d'applications plus anciennes.
- Pour des guides de migration détaillés, consultez la documentation officielle d'IBM.

**Références** :
- [IBM WebSphere Application Server Wikipedia](https://en.wikipedia.org/wiki/IBM_WebSphere_Application_Server)
- [Java SE 8 in WAS Traditional V9](https://www.ibm.com/docs/en/was/9.0.5?topic=waso-java-se-8-in-websphere-application-server-traditional-v9)
- [WAS Version Comparison Slides](https://www.slideshare.net/ejlp12/ibm-websphere-application-server-version-to-version-comparison)
- [WAS Configuration Comparison Tool](https://www.ibm.com/support/pages/websphere-application-server-configuration-comparison-tool)