---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4.1-fast
title: Spring Boot a dépassé Liberty
translated: true
type: note
---

IBM WebSphere Application Server Liberty Profile (souvent abrégé WLP ou simplement Liberty) était la tentative d'IBM de moderniser son serveur d'applications WebSphere traditionnel et lourd en créant un runtime Jakarta EE (anciennement Java EE) léger, composable et adapté au cloud vers 2012-2013. Bien que techniquement solide et même supérieur dans certains domaines (démarrage rapide, faible empreinte mémoire, excellente prise en charge de MicroProfile via Open Liberty), **Liberty a largement "perdu" la bataille de la popularité face à Spring Boot** pour le nouveau développement d'applications web/microservices Java à partir du milieu des années 2010.

### Principales Raisons de la Domination de Spring Boot sur Liberty

| Raison | Avantage de Spring Boot | Inconvénient de Liberty / des Serveurs d'Applications Traditionnels |
|--------|-----------------------|-------------------------------------------|
| **Productivité des Développeurs & Facilité d'Utilisation** | Convention plutôt que configuration, auto-configuration, serveur embarqué (Tomcat/Jetty/Undertow par défaut), `spring-boot-starter-*` élimine le code boilerplate. Applications prêtes pour la production avec zéro configuration en quelques minutes. | Nécessite toujours une configuration server.xml, une activation des fonctionnalités et une configuration manuelle, même s'il est plus léger que WAS complet. Semble "dépassé" pour de nombreux développeurs. |
| **Modèle d'Exécutable Autonome** | JAR gras / uber-JAR avec serveur embarqué → exécutable partout avec `java -jar`, parfait pour Docker/Kubernetes et le DevOps. Aucune gestion de serveur externe. | Principalement un serveur séparé dans lequel vous déployez des WAR/EAR (bien que Liberty ait ajouté plus tard la prise en charge des JAR exécutables, cela semblait ajouté a posteriori et n'est jamais devenu le flux de travail par défaut). |
| **Écosystème & Communauté** | Communauté open-source massive (Pivotal/VMware), énormément de starters tiers, excellente documentation, réponses sur Stack Overflow, tutoriels. | Communauté plus réduite ; documentation principalement IBM et support payant. Moins d'intégrations prêtes à l'emploi. |
| **Timing & Part d'Esprit** | Spring Boot 1.0 publié en 2014 — exactement au moment où les microservices, Docker et le cloud-native ont explosé. Il est devenu le standard de facto pour les nouveaux services Java. | Liberty lancé plus tôt (2012–2013) mais était encore perçu comme le "serveur d'applications d'IBM" à une époque où les développeurs fuyaient les serveurs commerciaux lourds (WebSphere, WebLogic). |
| **Neutralité du Fournisseur & Coût** | Complètement gratuit et open-source, aucune crainte de lock-in vendor. | Produit IBM → perception de licences coûteuses (même si Liberty Core avait un niveau gratuit et qu'Open Liberty est entièrement open-source, la marque portait le bagage de WAS traditionnel). |
| **Adéquation Microservices & Cloud** | Conçu dès le premier jour pour les microservices ; actuators, contrôles de santé, configuration externalisée, applications 12-factor faciles. | Très adapté au cloud (surtout Open Liberty), mais la plupart des développeurs avaient déjà choisi Spring Boot avant de découvrir les forces de Liberty. |
| **Momentum du Marché** | Vers ~2018–2020, les enquêtes montraient que Tomcat (intégré dans Spring Boot) avait ~60% de part des runtimes Java, éclipsant tous les serveurs d'applications complets combinés. En 2025, Spring Boot est utilisé par >18 000 entreprises connues ; les serveurs d'applications traditionnels sont devenus de niche. | Liberty/Open Liberty reste populaire dans les entreprises fortement utilisatrices d'IBM et pour Jakarta EE/MicroProfile, mais est loin derrière en adoption pour les nouveaux projets (greenfield). |

### Où Liberty Gagne Encore (Cas de Niche)
- Applications Jakarta EE / MicroProfile pures sans dépendances Spring.
- Entreprises déjà enfermées dans l'écosystème IBM (Red Hat OpenShift avec licences WebSphere, IBM Cloud Pak).
- Déploiements Spring Boot optimisés (Liberty peut exécuter des applications Spring Boot avec des images Docker plus petites et un débit plus élevé que Tomcat embarqué dans certains benchmarks).
- Industries réglementées nécessitant un support commercial/des certifications.

En bref : **Liberty n'a pas perdu parce qu'il était techniquement inférieur — il a perdu parce que Spring Boot offrait une productivité des développeurs radicalement supérieure, est arrivé au moment culturel parfait et a construit un momentum d'écosystème irrésistible.** La plupart des nouveaux projets backend Java en 2025 commencent avec Spring Boot (ou Quarkus/Helidon/Micronaut), et non avec un serveur d'applications séparé.

[Spring Boot vs Websphere Liberty | What are the differences?](https://stackshare.io/stackups/spring-boot-vs-websphere-liberty)  
[2020 Java Technology Report | JRebel](https://www.jrebel.com/blog/2020-java-technology-report)  
[How does Open Liberty’s performance compare to other cloud-native Java runtimes](https://openliberty.io/blog/2022/10/17/memory-footprint-throughput-update.html)  
[Spring Boot market share data (6sense)](https://6sense.com/tech/programming-framework/spring-boot-market-share)