---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Comparaison des Emballages WAR et EAR
translated: true
type: note
---

### Présentation
Dans Java EE (maintenant Jakarta EE), WAR (Web Archive) et EAR (Enterprise Archive) sont des formats de packaging standard pour déployer des applications sur des serveurs d'applications comme Tomcat, WildFly ou GlassFish. WAR se concentre sur les composants de la couche web, tandis que EAR regroupe plusieurs modules pour des applications d'entreprise complètes. Vous trouverez ci-dessous une comparaison détaillée.

| Aspect               | WAR (Web Archive)                                                                 | EAR (Enterprise Archive)                                                                 |
|----------------------|-----------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| **Objectif**         | Déploie des applications web (p. ex., servlets, JSP, contenu statique) comme une unité unique pour la fonctionnalité de la couche web. | Déploie des applications d'entreprise en empaquetant plusieurs sous-modules (p. ex., WARs, EJB JARs) pour des systèmes distribués multi-couches. |
| **Contenu**          | - Fichiers d'application web : JSP, HTML/CSS/JS, servlets.<br>- Bibliothèques : JARs dans WEB-INF/lib.<br>- Descripteur de déploiement : web.xml (optionnel dans les versions modernes). | - Modules multiples : WARs, EJB JARs, JARs clients.<br>- Bibliothèques partagées.<br>- Descripteur de déploiement : application.xml.<br>- RARs pour les adaptateurs de ressources (optionnel). |
| **Structure**        | - Racine : ressources statiques (p. ex., index.html).<br>- WEB-INF/ : classes, lib, web.xml. | - Racine : META-INF/application.xml.<br>- Sous-répertoires pour chaque module (p. ex., myapp.war, myejb.jar). |
| **Extension de fichier** | .war                                                                             | .ear                                                                                     |
| **Portée de déploiement** | Module unique ; se déploie sur des conteneurs web (p. ex., Tomcat) ou des serveurs d'applications complets. | Multi-modules ; se déploie uniquement sur des serveurs d'applications complets (p. ex., JBoss, WebLogic) pour des fonctionnalités d'entreprise comme les transactions. |
| **Taille et Complexité** | Plus petit et plus simple ; idéal pour les applications web autonomes.                              | Plus grand et plus complexe ; prend en charge la modularité et les ressources partagées entre les modules.        |
| **Cas d'utilisation** | Portails web, API REST, services simples (p. ex., applications web Spring Boot empaquetées en WAR). | Systèmes d'entreprise complexes (p. ex., applications bancaires avec interface utilisateur web + logique métier + accès aux données). |
| **Dépendances**      | S'appuie sur le conteneur pour les services web ; pas de support EJB intégré.                    | Prend en charge les EJB, JMS et les dépendances inter-modules ; favorise le couplage lâche.              |

### Résumé des différences clés
- **Modularité** : WAR est monolithique pour les couches web ; EAR permet la composition de plusieurs WARs/JARs.
- **Exigences du serveur** : WAR fonctionne sur des serveurs web légers ; EAR nécessite un serveur JEE complet.
- **Évolution** : Avec les tendances des microservices et du cloud natif (p. ex., Spring Boot, Quarkus), les WAR sont souvent utilisés pour les déploiements conteneurisés (Docker), tandis que les EAR sont moins courants mais restent vitaux pour les applications d'entreprise héritées.

Pour des exemples pratiques, reportez-vous à la documentation officielle de Jakarta EE : [Jakarta EE Tutorial](https://jakartaee.github.io/tutorial/) ou aux archives Java EE d'Oracle : [Java EE Packaging](https://docs.oracle.com/javaee/7/tutorial/packaging.htm).