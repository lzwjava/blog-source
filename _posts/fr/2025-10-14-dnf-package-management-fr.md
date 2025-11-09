---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Gestion des paquets DNF dans RHEL
translated: true
type: note
---

### Introduction à DNF dans Red Hat Enterprise Linux

DNF (Dandified YUM) est l'outil principal de gestion des paquets dans Red Hat Enterprise Linux (RHEL), à partir de RHEL 8 et continuant avec RHEL 9. Il succède à l'ancien outil YUM (Yellowdog Updater, Modified), en offrant de meilleures performances, une meilleure résolution des dépendances et une prise en charge du contenu modulaire. Dans RHEL, DNF gère l'installation, la mise à jour et la suppression des paquets logiciels distribués via les dépôts RPM (Red Hat Package Manager). Il garantit l'accès à des ensembles de contenu essentiels comme BaseOS (pour les fonctionnalités de base du système d'exploitation) et AppStream (pour les applications, les runtimes et les outils en espace utilisateur), le tout étant géré via votre abonnement RHEL.

L'objectif de DNF est de simplifier la gestion du cycle de vie des logiciels tout en maintenant la stabilité du système. Il permet aux administrateurs et aux utilisateurs de travailler avec des paquets RPM traditionnels aux côtés de formats modulaires modernes, où des composants comme les langages ou les bases de données peuvent avoir plusieurs versions parallèles (appelées « streams ») sans perturber le système d'exploitation de base.

#### Fonctionnalités principales
- **Prise en charge du contenu modulaire** : Gère les modules (groupes de RPM liés), les streams (dépôts spécifiques à une version) et les profils (ensembles de paquets préconfigurés pour des cas d'utilisation spécifiques, par exemple un serveur web ou un environnement de développement).
- **Gestion des dépôts** : Permet de rechercher, d'activer/désactiver les dépôts et de configurer les sources comme BaseOS, AppStream et les dépôts supplémentaires.
- **Installation et mises à jour** : Résout automatiquement les dépendances lors de l'installation de paquets, de groupes ou de modules entiers ; prend en charge la vérification des mises à jour, la mise à niveau de paquets spécifiques ou de l'ensemble du système.
- **Suppression et annulation** : Supprime les logiciels en toute sécurité et fournit un historique des transactions pour annuler les modifications.
- **Personnalisation et automatisation** : Configurable via `/etc/dnf/dnf.conf` pour les exclusions, les plugins ou la mise en cache ; s'intègre à des outils comme DNF Automatic pour les mises à jour planifiées.
- **Compatibilité ascendante** : La commande `yum` est un alias de `dnf` dans RHEL, facilitant la transition depuis les anciennes versions.

Pour commencer, les commandes de base incluent `dnf install <paquet>` pour l'installation, `dnf update` pour les mises à niveau et `dnf search <terme>` pour rechercher un logiciel. Pour une utilisation plus avancée, reportez-vous à la documentation officielle.

[Red Hat Enterprise Linux 9 : Gestion des logiciels avec l'outil DNF](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/managing_software_with_the_dnf_tool/index)