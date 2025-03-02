---
audio: false
generated: true
lang: fr
layout: post
title: Utiliser WebSphere Liberty avec Eclipse
translated: true
---

Pour utiliser les outils de plugin WebSphere dans Eclipse et les intégrer pour travailler avec WebSphere Liberty, vous pouvez choisir entre deux options principales : **IBM Liberty Developer Tools** et **Liberty Tools**. Les deux sont disponibles via le marché Eclipse et fournissent des fonctionnalités pour construire, déployer et gérer des applications sur WebSphere Liberty, un serveur léger, prêt pour la production pour les applications Java EE et natives au cloud. Voici un guide détaillé sur la manière d'utiliser et d'intégrer ces outils.

---

### **Aperçu des Outils**
- **IBM Liberty Developer Tools** : Un plugin traditionnel fourni par IBM pour gérer les serveurs Liberty dans Eclipse. Il vous permet de créer et de gérer des serveurs Liberty, de déployer des applications et de déboguer directement depuis l'IDE. Cet outil est idéal pour un flux de travail centré sur le serveur ou pour des projets qui n'utilisent pas Maven ou Gradle.
- **Liberty Tools** : Une alternative open-source de nouvelle génération axée sur les projets Maven et Gradle. Elle offre une expérience plus intégrée avec les outils de construction, une détection automatique des projets Liberty et un support pour le mode de développement de Liberty (mode dev). Cet outil est mieux adapté aux flux de travail modernes centrés sur les outils de construction.

Les deux outils rationalisent le développement pour WebSphere Liberty, mais ils diffèrent dans leur approche. Choisissez celui qui convient le mieux à votre type de projet et à vos préférences de développement.

---

### **Installation**
1. **Installer Eclipse** :
   - Utilisez une version compatible, telle que **Eclipse pour les développeurs Java d'entreprise et Web**.
   - Assurez-vous que votre version d'Eclipse prend en charge le plugin que vous choisissez (vérifiez la compatibilité dans la liste du marché).

2. **Installer le Plugin** :
   - Ouvrez Eclipse et allez dans **Aide > Eclipse Marketplace**.
   - Recherchez :
     - "IBM Liberty Developer Tools" pour l'ensemble d'outils traditionnel d'IBM, ou
     - "Liberty Tools" pour l'alternative open-source.
   - Installez le plugin souhaité en suivant les instructions.

---

### **Configuration du Runtime Liberty**
- **Télécharger Liberty** :
  - Si ce n'est pas déjà fait, téléchargez le runtime WebSphere Liberty depuis le [site officiel IBM](https://www.ibm.com/docs/en/was-liberty).
  - Assurez-vous que la version de Liberty est compatible avec le plugin que vous avez installé.

- **Configurer le Runtime dans Eclipse** :
  - Pour **IBM Liberty Developer Tools** :
    - Allez dans **Fenêtre > Préférences > Serveur > Environnements d'exécution**.
    - Cliquez sur "Ajouter", sélectionnez "Serveur Liberty" et spécifiez le chemin vers votre répertoire d'installation de Liberty.
  - Pour **Liberty Tools** :
    - Aucune configuration explicite du runtime n'est nécessaire. Liberty Tools détecte les projets Liberty via les configurations Maven ou Gradle, alors assurez-vous que votre projet est correctement configuré (voir ci-dessous).

---

### **Intégration avec Votre Projet**
Le processus d'intégration diffère légèrement entre les deux outils. Suivez les étapes ci-dessous en fonction de l'outil que vous avez installé.

#### **Pour IBM Liberty Developer Tools**
1. **Créer un Serveur Liberty** :
   - Ouvrez la vue **Serveurs** (**Fenêtre > Afficher la vue > Serveurs**).
   - Faites un clic droit dans la vue Serveurs et sélectionnez **Nouveau > Serveur**.
   - Choisissez "Serveur Liberty" dans la liste et suivez l'assistant pour configurer le serveur, y compris la spécification du chemin vers votre installation de Liberty.

2. **Ajouter Votre Projet** :
   - Faites un clic droit sur le serveur dans la vue Serveurs et sélectionnez **Ajouter et Supprimer...**.
   - Sélectionnez votre projet et déplacez-le vers le côté "Configuré".

3. **Démarrer le Serveur** :
   - Faites un clic droit sur le serveur et choisissez **Démarrer** ou **Déboguer** pour exécuter votre application.
   - Accédez à votre application à l'URL spécifiée (par défaut : `http://localhost:9080/<context-root>`).

#### **Pour Liberty Tools (Projets Maven/Gradle)**
1. **Assurer la Configuration du Projet** :
   - Votre projet doit inclure le plugin Liberty nécessaire :
     - Pour Maven : Ajoutez le `liberty-maven-plugin` à votre `pom.xml`.
     - Pour Gradle : Ajoutez le `liberty-gradle-plugin` à votre `build.gradle`.
   - Le fichier de configuration `server.xml` doit se trouver à l'emplacement standard :
     - Pour Maven : `src/main/liberty/config`.
     - Pour Gradle : Ajustez en fonction de la structure de votre projet.

2. **Utiliser le Tableau de Bord Liberty** :
   - Cliquez sur l'icône Liberty dans la barre d'outils Eclipse pour ouvrir le **Tableau de Bord Liberty**.
   - Liberty Tools détecte automatiquement et liste vos projets Liberty dans le tableau de bord.
   - Faites un clic droit sur votre projet dans le tableau de bord pour accéder aux commandes telles que :
     - "Démarrer en mode dev" (redeploie automatiquement les modifications sans redémarrer le serveur).
     - "Exécuter des tests".
     - "Afficher les rapports de tests".

3. **Accéder à Votre Application** :
   - Une fois le serveur en cours d'exécution, accédez à votre application à l'URL spécifiée (par défaut : `http://localhost:9080/<context-root>`).
   - En mode dev, apportez des modifications à votre code et Liberty redeploiera automatiquement les modifications.

---

### **Fonctionnalités Clés**
Les deux outils offrent des fonctionnalités puissantes pour améliorer la productivité :

- **Gestion des Serveurs** :
  - Démarrez, arrêtez et déboguez les serveurs Liberty directement depuis Eclipse.
- **Déploiement des Applications** :
  - Déployez et redeployez facilement les applications.
- **Assistance à la Configuration** :
  - Les deux outils fournissent une complétion de code, une validation et des descriptions au survol pour les fichiers de configuration Liberty (par exemple, `server.xml`).
- **Mode Développement** :
  - Détecte et redeploie automatiquement les modifications de code sans redémarrer le serveur (surtout avec Liberty Tools en mode dev).
- **Débogage** :
  - Attachez le débogueur Eclipse au serveur Liberty pour le dépannage.

---

### **Considérations et Problèmes Potentiels**
- **Compatibilité des Versions** :
  - Assurez-vous que vos versions d'Eclipse, du plugin et du runtime Liberty sont compatibles. Consultez la documentation pour les exigences spécifiques.
- **Configuration du Projet** :
  - Pour Liberty Tools, votre projet doit être un projet Maven ou Gradle correctement configuré avec le plugin Liberty inclus.
  - Assurez-vous que `server.xml` se trouve à l'emplacement attendu pour que les outils reconnaissent votre projet.
- **Paramètres Réseau** :
  - Assurez-vous que les ports Liberty par défaut (par exemple, 9080 pour HTTP, 9443 pour HTTPS) sont ouverts et non bloqués par les pare-feu.
- **Compatibilité Java** :
  - Liberty est un serveur basé sur Java, alors assurez-vous d'avoir une version de Java compatible installée pour votre runtime Liberty.

---

### **Démarrage Rapide avec Liberty Tools (Maven/Gradle)**
Si vous utilisez Maven ou Gradle, Liberty Tools offrent une expérience rationalisée. Voici un guide étape par étape :

1. Installez **Eclipse pour les développeurs Java d'entreprise et Web**.
2. Allez dans **Aide > Eclipse Marketplace**, recherchez "Liberty Tools" et installez le plugin.
3. Créez ou importez un projet Maven/Gradle configuré pour Liberty :
   - Vous pouvez utiliser le [Open Liberty Starter](https://openliberty.io/start/) pour générer un projet d'exemple.
4. Assurez-vous que votre projet dispose du `liberty-maven-plugin` (pour Maven) ou `liberty-gradle-plugin` (pour Gradle) configuré.
5. Ouvrez le **Tableau de Bord Liberty** en cliquant sur l'icône Liberty dans la barre d'outils.
6. Votre projet devrait apparaître dans le tableau de bord. Faites un clic droit dessus et sélectionnez "Démarrer en mode dev".
7. Accédez à votre application à l'URL spécifiée (par défaut : `http://localhost:9080/<context-root>`).
8. Apportez des modifications à votre code ; le mode dev de Liberty redeploiera automatiquement les modifications.
9. Utilisez le tableau de bord pour exécuter des tests ou afficher des rapports de tests selon les besoins.

---

### **Choisir entre les Outils**
- **IBM Liberty Developer Tools** :
  - Idéal pour une approche de gestion de serveur traditionnelle ou pour des projets qui n'utilisent pas Maven ou Gradle.
  - Offre une vue Serveurs pour gérer les serveurs Liberty explicitement.
- **Liberty Tools** :
  - Mieux adapté aux projets Maven ou Gradle, avec une intégration plus étroite avec ces systèmes de construction.
  - Fournit un tableau de bord Liberty pour une gestion centrée sur le projet et un support pour le mode dev.
  - Open-source, permettant des contributions et des mises à jour de la communauté.

Les deux outils sont disponibles depuis le marché Eclipse, vous pouvez donc essayer les deux et choisir celui qui convient le mieux à votre flux de travail.

---

En résumé, l'utilisation des outils de plugin WebSphere dans Eclipse implique l'installation du plugin approprié, la configuration du runtime Liberty et la configuration de votre projet pour travailler avec Liberty. Que vous choisissiez IBM Liberty Developer Tools ou Liberty Tools, les deux offrent des fonctionnalités robustes pour rationaliser le développement pour WebSphere Liberty dans l'IDE Eclipse.