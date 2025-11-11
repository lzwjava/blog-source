---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Afficher le code source JAR dans IntelliJ IDEA
translated: true
type: note
---

Dans IntelliJ IDEA, vous pouvez facilement consulter le code source d'un fichier JAR. Il existe plusieurs approches selon que le JAR contient des fichiers source ou seulement des fichiers compilés `.class` :

---

### 1. Ouvrir le JAR dans IDEA

* Allez dans **Fichier > Ouvrir…**
* Sélectionnez le fichier JAR.
* IDEA l'ouvrira dans la **vue Projet** comme une archive classique.
* Si le JAR contient des fichiers source `.java`, vous pouvez les parcourir directement.
* S'il ne contient que des fichiers `.class`, IDEA les décompilera automatiquement en code Java lisible.

---

### 2. Attacher les sources à un JAR de bibliothèque

Si le JAR fait partie d'une bibliothèque (comme les dépendances Maven ou Gradle) :

* Allez dans **Fichier > Structure du projet > Bibliothèques** (ou **Modules > Dépendances** si c'est spécifique à un module).
* Sélectionnez le JAR.
* Cliquez sur **Attacher les sources…** et indiquez à IDEA le chemin vers le `-sources.jar` (s'il est disponible).
* Maintenant, IDEA affichera la véritable source au lieu du simple bytecode décompilé.

---

### 3. Navigation rapide

* Maintenez **Ctrl (Cmd sur macOS)** et cliquez sur une classe ou une méthode provenant du JAR.
* Si aucune source n'est attachée, IDEA affiche la version décompilée.
* Si des sources sont attachées, vous verrez le code Java original.

---

### 4. Plugins de décompilation externes (Optionnel)

IDEA possède déjà un décompilateur intégré, mais vous pouvez installer des plugins comme **Fernflower** ou **CFR** si vous souhaitez une décompilation alternative.

---

👉 Généralement, s'il s'agit d'une dépendance gérée par Maven/Gradle, IDEA peut automatiquement télécharger et attacher le `-sources.jar` depuis le dépôt. S'il s'agit d'un JAR autonome, vous devrez attacher les sources manuellement ou vous fier au décompilateur.

Souhaitez-vous que j'explique également **comment extraire le code source du JAR en dehors d'IDEA** (en utilisant des outils comme `jd-gui` ou `jar xf`), ou voulez-vous principalement vous en tenir à travailler dans IDEA ?