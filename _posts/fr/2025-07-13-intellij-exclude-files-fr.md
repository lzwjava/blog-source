---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Exclure des fichiers dans IntelliJ IDEA
translated: true
type: note
---

Dans IntelliJ IDEA, vous pouvez exclure des fichiers ou des répertoires afin qu'ils n'apparaissent pas dans la recherche, l'indexation, la complétion de code ou les builds. Il existe plusieurs méthodes pour le faire, selon votre objectif :

---

### 1. Marquer un répertoire comme *Exclu*

* Dans la **vue Project**, faites un clic droit sur le dossier que vous souhaitez exclure.
* Choisissez **Mark Directory as → Excluded**.
* IDEA arrêtera de l'indexer, il n'apparaîtra donc pas dans les recherches, la navigation ou l'analyse de code.

Cette méthode est généralement utilisée pour les dossiers de sortie de build (`target/`, `out/`, `dist/`, etc.).

---

### 2. Exclure du contrôle de version (Ignorer VCS)

Si vous ne voulez pas qu'IDEA (et Git) suive certains fichiers :

* Créez ou modifiez un fichier `.gitignore` dans votre projet.
* Ajoutez-y les modèles de noms de répertoires ou de fichiers.
* IDEA reconnaîtra le `.gitignore` et les masquera des opérations VCS.

---

### 3. Exclure des fichiers de l'analyse de code / des inspections

* Allez dans **Settings → Editor → Inspections**.
* Vous pouvez y configurer des **Scopes** et assigner des inspections uniquement à certains ensembles de fichiers tout en en excluant d'autres.

---

### 4. Exclure du build (Gradle/Maven)

Si vous utilisez Gradle ou Maven, vous pouvez configurer `build.gradle` ou `pom.xml` pour exclure certains répertoires (comme le code généré ou les ressources). IDEA respecte ces configurations des outils de build.

---

### 5. Exclure des types de fichiers spécifiques

* Allez dans **Settings → Editor → File Types**.
* Ajoutez des modèles (comme `*.log`, `*.tmp`) à la liste "Ignore files and folders".

---

👉 Astuce rapide : Si votre objectif est simplement d'empêcher IDEA de gaspiller des ressources à indexer de gros dossiers (comme `node_modules/`), l'option **Mark Directory as Excluded** est la plus rapide et la plus efficace.

Souhaitez-vous que je vous montre également comment exclure les répertoires de test (comme `src/test/java`) des exécutions de **couverture de code** dans IDEA ?