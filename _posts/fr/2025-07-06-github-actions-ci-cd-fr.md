---
audio: false
generated: true
lang: fr
layout: post
title: 'GitHub Actions : L''Évolution CI/CD'
translated: true
type: note
---

GitHub Actions est une **plateforme d’intégration continue et de livraison continue (CI/CD)** puissante, directement intégrée à GitHub. Elle permet aux développeurs d’automatiser différentes étapes de leur flux de développement logiciel, de la compilation et des tests du code au déploiement des applications.

### Comment cela s’est développé et quand cela a été publié

GitHub lui-même a été fondé en **2007**, son site web étant lancé en **avril 2008**. Le développement de la plateforme GitHub a commencé en **octobre 2005**, et elle a été officiellement lancée par Tom Preston-Werner, Chris Wanstrath, P. J. Hyett et Scott Chacon.

GitHub Actions, en tant que plateforme CI/CD spécifique, a été annoncé pour la première fois en **octobre 2018** et publié officiellement pour une disponibilité générale en **novembre 2019**. Il a évolué à partir de la mission principale de GitHub qui est de fournir des outils qui simplifient la collaboration et l’automatisation pour les développeurs.

### Combien d’utilisateurs cela a-t-il ?

Bien qu’il soit difficile d’obtenir un nombre exact et en temps réel des *utilisateurs* de GitHub Actions spécifiquement, il est important de noter que **GitHub lui-même compte plus de 100 millions de développeurs** début 2023. Compte tenu de l’intégration profonde de GitHub Actions et de la demande croissante pour le CI/CD, une part importante de ces utilisateurs l’utilisent pour leurs projets. De nombreuses équipes de développement dans diverses industries, des petites startups aux grandes entreprises, l’utilisent.

### Quels dépôts ont beaucoup d’Actions ?

Les GitHub Actions sont définies dans des dépôts individuels, généralement dans le répertoire `.github/workflows`. Les dépôts qui utilisent abondamment GitHub Actions incluent souvent :

* **Les dépôts officiels de GitHub Actions :** L’organisation `github/actions` sur GitHub contient de nombreuses actions fondamentales et couramment utilisées comme `actions/checkout`, `actions/setup-python`, `actions/setup-node`, `actions/upload-artifact` et `actions/download-artifact`. Celles-ci sont essentielles pour de nombreux workflows.
* **Les grands projets open source :** Les grands projets open source dans différents langages de programmation (par exemple pour Python, JavaScript, Go, C++) utilisent massivement GitHub Actions pour leurs pipelines de build, de test et de release. On trouve souvent des exemples parmi les projets de sociétés comme Google, Microsoft et d’autres géants technologiques, ainsi que des frameworks et bibliothèques populaires.
* **Les projets axés sur l’automatisation et le DevOps :** Les dépôts démontrant des pratiques DevOps, automatisant divers aspects de l’infrastructure, des tests ou du déploiement, auront naturellement un ensemble riche de workflows GitHub Actions.
* **Les dépôts tendance :** De nombreux dépôts tendance sur GitHub aujourd’hui (que l’on peut trouver sur la page des tendances de GitHub) mettent souvent en avant des utilisations innovantes de GitHub Actions pour des choses comme la génération de contenu, l’exécution d’analyses de sécurité ou l’automatisation des releases.

En substance, tout dépôt qui bénéficie de processus automatisés pour la qualité du code, les tests, le déploiement ou la gestion générale du dépôt est un candidat pour avoir un ensemble robuste de GitHub Actions.