---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Guide de Navigation de la Console d'Administration IBM WebSphere
translated: true
type: note
---

### Console d'administration IBM WebSphere Application Server (WAS) : Volet de navigation gauche

La vue de gauche dans la console d'administration d'IBM WebSphere Application Server (WAS) (également appelée Integrated Solutions Console) est une arborescence de navigation hiérarchique qui organise les tâches de configuration et de gestion. Elle fournit un accès rapide aux domaines clés pour administrer l'environnement serveur, les applications et les ressources. La structure exacte peut varier légèrement selon la version de WAS (par exemple, 8.5, 9.0) et l'édition (Base vs. Network Deployment), mais les catégories principales de haut niveau sont cohérentes.

Voici une liste des principales sections de haut niveau dans l'arborescence de navigation, avec de brèves descriptions de leurs objectifs principaux. Les sous-sections sont déployables (en utilisant les icônes +/−) pour des tâches plus granulaires.

#### Sections principales de haut niveau
- **Applications**  
  Utilisé pour déployer, installer, mettre à jour, démarrer/arrêter et gérer les applications (par exemple, les fichiers EAR/WAR).  
  *Sous-sections clés* : Applications d'entreprise, Applications d'entreprise WebSphere, Modules Web, Bibliothèques partagées.  
  *Tâches courantes* : Installer de nouvelles applications, mapper des modules sur des serveurs, configurer les chargeurs de classes.

- **Ressources**  
  Configure les ressources partagées comme les bases de données, la messagerie et les pools de connexion que les applications peuvent utiliser.  
  *Sous-sections clés* : JDBC (sources de données/fournisseurs), JMS (files d'attente/sujets), Sessions JavaMail, Fournisseurs d'URL.  
  *Tâches courantes* : Configurer des sources de données JDBC, créer des fabriques de connexions JMS.

- **Services**  
  Gère les services à l'échelle du serveur tels que la sécurité, la messagerie et les protocoles de communication.  
  *Sous-sections clés* : Sécurité (sécurité globale, utilisateurs/groupes, authentification), Fournisseurs de messagerie, Ports, Service ORB, Service de transactions.  
  *Tâches courantes* : Activer SSL, configurer les registres d'utilisateurs, ajuster les assignations de ports.

- **Serveurs**  
  Gère les instances de serveur, le clustering et les définitions de serveur web.  
  *Sous-sections clés* : Types de serveurs (serveurs d'applications WebSphere, serveurs proxy WebSphere), Clusters, Serveurs Web.  
  *Tâches courantes* : Démarrer/arrêter des serveurs, configurer les paramètres JVM, créer des clusters pour la haute disponibilité.

- **Administration système**  
  Supervise la topologie globale, y compris les nœuds, les cellules et les paramètres de la console.  
  *Sous-sections clés* : Nœuds, Cellules, Deployment Manager, Préférences de la console.  
  *Tâches courantes* : Synchroniser les nœuds, gérer le gestionnaire de déploiement, définir les thèmes/périmètres de la console.

- **Environnement**  
  Définit les variables et alias spécifiques à l'environnement.  
  *Sous-sections clés* : Variables WebSphere, Alias d'hôtes.  
  *Tâches courantes* : Définir des variables système pour les chemins ou les propriétés.

- **Surveillance et réglage**  
  Surveille les performances et règle le comportement à l'exécution.  
  *Sous-sections clés* : Infrastructure de surveillance des performances (PMI), Services personnalisés, Journalisation et traçage.  
  *Tâches courantes* : Activer les métriques, ajuster les pools de threads, consulter les métriques de requêtes.

- **Dépannage**  
  Accède aux outils de diagnostic et aux journaux.  
  *Sous-sections clés* : Journaux et traces, Premières étapes.  
  *Tâches courantes* : Télécharger les journaux, activer les spécifications de trace.

#### Notes supplémentaires
- **Sélection du périmètre** : En haut de nombreuses pages, vous pouvez filtrer par périmètre (Cellule, Nœud, Serveur) pour limiter la visibilité.
- **Activités guidées** : Apparaît parfois comme une section de haut niveau ou contextuelle pour les assistants (par exemple, sécuriser l'environnement).
- Pour accéder à la console : Généralement via `https://<hôte>:<port>/ibm/console` (port par défaut 9060 pour l'admin, 9043 pour le sécurisé).
- Pour les détails spécifiques à une version (par exemple, WAS 9.0), reportez-vous à la documentation officielle d'IBM, car des modifications mineures de l'interface utilisateur se produisent dans les mises à jour.

[Console d'administration WebSphere - 101](https://www.ibm.com/community/101/websphere/administrative-console/)  
[Introduction : Console d'administration (WAS 9.0.5)](https://www.ibm.com/docs/en/was-nd/9.0.5?topic=administration-introduction-administrative-console)  
[WebSphere Application Server V7: Administration Consoles (Redpaper)](https://www.redbooks.ibm.com/redpapers/pdfs/redp4573.pdf)