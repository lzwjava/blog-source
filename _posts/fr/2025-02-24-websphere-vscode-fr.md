---
audio: false
generated: false
lang: fr
layout: post
title: Utilisation du serveur WebSphere Liberty dans VSCode
translated: true
---

Pour utiliser le serveur WebSphere Liberty dans Visual Studio Code (VSCode), vous pouvez tirer parti de l'extension **Liberty Tools**, qui prend en charge à la fois Open Liberty et WebSphere Liberty. Cette extension vous permet de gérer votre serveur Liberty, de déployer des applications et de déboguer directement depuis VSCode, optimisant ainsi votre flux de travail de développement.

### Étapes pour utiliser WebSphere Liberty dans VSCode

#### 1. **Installer l'extension Liberty Tools**
   - Ouvrez VSCode et accédez à la vue Extensions en cliquant sur l'icône Extensions dans la barre d'activité ou en appuyant sur `Ctrl+Shift+X`.
   - Recherchez "Liberty Tools" dans le marché des extensions.
   - Cliquez sur "Installer" pour ajouter l'extension à VSCode.
   - Redémarrez VSCode si vous y êtes invité pour activer l'extension.

#### 2. **Configurer les prérequis**
   - **Java** : Assurez-vous d'avoir une version compatible de Java installée (Java 8 ou ultérieur est recommandé). Liberty est un serveur basé sur Java, donc Java est essentiel pour l'exécuter.
   - **WebSphere Liberty** : Téléchargez et installez le runtime WebSphere Liberty si ce n'est pas déjà fait. Vous pouvez l'obtenir depuis le [site officiel IBM](https://www.ibm.com/docs/en/was-liberty). Notez le répertoire d'installation, car vous en aurez besoin pour configurer l'extension.

#### 3. **Configurer l'extension Liberty Tools**
   - Après avoir installé l'extension, configurez-la pour qu'elle pointe vers votre installation Liberty.
   - Ouvrez la palette de commandes dans VSCode en appuyant sur `Ctrl+Shift+P`.
   - Tapez "Liberty: Add Liberty Runtime" et sélectionnez la commande.
   - Fournissez le chemin vers votre répertoire d'installation Liberty (par exemple, `/opt/ibm/wlp`).
   - L'extension détectera le runtime Liberty et le rendra disponible pour une utilisation dans VSCode.

#### 4. **Gérer votre serveur Liberty**
   - Une fois configuré, vous pouvez gérer votre serveur Liberty directement depuis VSCode.
   - **Tableau de bord Liberty** : Accédez à la vue du tableau de bord Liberty dans le panneau Explorer ou via la palette de commandes. Ce tableau de bord liste vos projets et serveurs Liberty.
   - **Démarrer/Arrêter le serveur** : Faites un clic droit sur votre serveur dans le tableau de bord pour le démarrer, l'arrêter ou le redémarrer.
   - **Déployer des applications** : Pour les projets Liberty (par exemple, les projets Maven ou Gradle avec des plugins Liberty), faites un clic droit sur le projet et sélectionnez "Déployer sur Liberty" pour déployer des applications.
   - **Mode Développement (Dev Mode)** : Pour les projets Maven ou Gradle, démarrez le serveur en mode dev, qui détecte automatiquement les modifications de code, recompile et redéploie l'application sans redémarrer le serveur. Cela est idéal pour le développement itératif.

#### 5. **Débogage et tests**
   - **Débogage** : Attachez un débogueur à votre serveur Liberty en cours d'exécution directement depuis VSCode. Utilisez l'option "Debug" dans le tableau de bord Liberty ou configurez une configuration de débogage dans la vue Exécuter et déboguer de VSCode.
   - **Exécuter des tests** : Si votre projet inclut des tests, exécutez-les depuis le tableau de bord et affichez les résultats dans VSCode.

#### 6. **Fonctionnalités supplémentaires**
   - **Assistance à la configuration** : L'extension fournit une complétion de code, une validation et des descriptions au survol pour les fichiers de configuration Liberty (par exemple, `server.xml`), simplifiant la configuration du serveur.
   - **Support de langage** : Elle prend en charge Java, les API MicroProfile et Jakarta EE, améliorant votre expérience de développement.

### Principaux avantages
- **Intégration sans couture** : Gérez votre serveur Liberty sans quitter VSCode, améliorant ainsi l'efficacité.
- **Déploiement automatique** : En mode dev, les modifications de code sont automatiquement détectées et déployées, économisant du temps pendant le développement.
- **Support de débogage** : Attachez facilement un débogueur à votre serveur pour le dépannage.
- **Léger et efficace** : Liberty Tools est conçu pour être léger, en accord avec la focalisation de Liberty sur la vitesse et l'efficacité.

### Ressources supplémentaires
- Pour des instructions détaillées, consultez la [documentation Open Liberty](https://openliberty.io/docs/) et la [documentation Liberty Tools VSCode](https://openliberty.io/docs/latest/develop/liberty-tools.html).
- Si vous rencontrez des problèmes, consultez la section de dépannage de l'extension ou demandez de l'aide à la communauté sur des plateformes comme Stack Overflow.

En suivant ces étapes, vous pouvez utiliser efficacement WebSphere Liberty dans VSCode, en tirant parti de ses fonctionnalités pour améliorer votre processus de développement.