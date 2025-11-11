---
audio: false
generated: true
lang: fr
layout: post
title: Extension Liberty Tools dans Visual Studio Code
translated: true
type: note
---

Voici un aperçu de la façon dont vous pouvez utiliser l'extension Liberty Tools dans Visual Studio Code pour travailler avec un serveur WebSphere Liberty :

---

### 1. Installer l'extension Liberty Tools
- **Trouver et Installer :**  
  Ouvrez la vue Extensions de VS Code, recherchez **"IBM WebSphere Liberty Tools"** et installez-la.
- **Avantages de l'extension :**  
  Cette extension intègre la gestion du serveur, le déploiement d'applications et le débogage dans VS Code.

---

### 2. Préparer votre serveur WebSphere Liberty
- **Installer ou pointer vers un runtime Liberty :**  
  Si vous n'avez pas déjà un serveur Liberty installé, téléchargez-en un et installez-le depuis IBM. S'il est déjà installé, notez son répertoire d'installation.
- **Vérifier la compatibilité :**  
  Vérifiez que la version de votre runtime Liberty est compatible avec l'extension.

---

### 3. Configurer votre serveur Liberty dans VS Code
- **Créer une nouvelle instance de serveur :**  
  Ouvrez la Palette de commandes (`Ctrl+Shift+P` ou `Cmd+Shift+P`) et exécutez la commande :  
  `Liberty: Create Server`  
  Suivez les invites pour :
  - Sélectionner le dossier d'installation du runtime.
  - Spécifier le fichier de configuration du serveur (généralement le `server.xml`).
- **Projets existants :**  
  Si vous avez déjà une application basée sur Liberty, ouvrez l'espace de travail pour que l'extension puisse détecter et aider à gérer les paramètres de votre serveur.

---

### 4. Ajouter votre application
- **Déployer l'application :**  
  Vous pouvez ajouter votre application au serveur soit en :
  - Modifiant le `server.xml` pour inclure le contexte et les détails de déploiement de votre application, ou
  - Utilisant les options de l'interface utilisateur de l'extension (souvent disponibles dans la vue Liberty) pour "Add Application" ou "Deploy Application".
- **Intégration de build :**  
  Si vous utilisez Maven ou Gradle, l'extension peut également proposer des tâches qui construisent votre application avant le déploiement.

---

### 5. Démarrer, arrêter et déboguer le serveur
- **Démarrer le serveur :**  
  Dans la vue Liberty (souvent disponible sous forme de panneau dédié ou d'arborescence dans VS Code), faites un clic droit sur votre serveur configuré et sélectionnez **"Start Server"**.  
  Le volet de sortie affichera les journaux de démarrage et tous les messages de configuration.
- **Arrêter le serveur :**  
  De même, faites un clic droit et choisissez **"Stop Server"** pour arrêter votre instance.
- **Débogage :**  
  Si vous avez besoin de déboguer votre application :
  - Définissez des points d'arrêt dans votre code.
  - Utilisez la palette de commandes pour exécuter **"Liberty: Debug Server"** (ou utilisez les options de débogage fournies dans la vue Liberty) pour attacher le débogueur de VS Code à votre serveur en cours d'exécution.
  - Vos points d'arrêt devraient maintenant être atteints lorsque votre application traite les requêtes.

---

### 6. Fonctionnalités supplémentaires et conseils
- **Surveillance des journaux en direct :**  
  L'extension permet de visualiser les journaux du serveur Liberty en temps réel, facilitant ainsi le diagnostic des problèmes.
- **Édition de la configuration du serveur :**  
  Bénéficiez d'IntelliSense et de suggestions lors de l'édition de votre `server.xml` directement dans VS Code.
- **Intégration des tâches :**  
  Utilisez les tâches de VS Code si vous exécutez des builds ou des déploiements automatisés dans le cadre de votre flux de travail de développement.
- **Support des conteneurs et des environnements distants :**  
  Selon votre configuration, vous pourriez également être en mesure de configurer Liberty pour qu'il s'exécute dans des conteneurs ou des environnements distants, avec des commandes supplémentaires disponibles dans l'extension.

---

### Notes finales
L'utilisation de l'extension Liberty Tools rationalise le processus de développement, de déploiement et de débogage de vos applications WebSphere Liberty directement dans VS Code. Cette intégration aide à réduire les changements de contexte et accélère votre cycle de développement.

N'hésitez pas à consulter la documentation officielle d'IBM sur l'extension Liberty Tools pour toute configuration avancée ou étape de dépannage.