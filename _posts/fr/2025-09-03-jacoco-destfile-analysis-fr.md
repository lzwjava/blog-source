---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Utilisation et analyse de JaCoCo Destfile
translated: true
type: note
---

Bonne question — décomposons le fonctionnement du `destfile` de JaCoCo lorsque vous exécutez une application Java ou Spring Boot.

### 1. Ce qu'est `destfile`

`destfile` est un paramètre de l'agent Java JaCoCo (`jacocoagent.jar`) qui indique à l'agent **où écrire ses données d'exécution**.
Par défaut, c'est quelque chose comme `jacoco.exec`, mais vous pouvez le définir explicitement :

```bash
-javaagent:jacocoagent.jar=destfile=/chemin/vers/jacoco.exec
```

### 2. Ce qui est écrit

Lorsque votre application Spring Boot s'exécute avec l'agent JaCoCo attaché, l'agent instrumente le bytecode de vos classes.
Pendant l'exécution, JaCoCo enregistre les informations de couverture telles que :

* Quelles classes et méthodes ont été chargées
* Quelles lignes ont été exécutées
* La couverture des branches (si les chemins `if`/`else` ont été parcourus, etc.)

Ces données de couverture runtime sont stockées en mémoire et périodiquement écrites dans le fichier défini par `destfile`.

Donc oui — la JVM, via l'agent JaCoCo, écrit les informations d'exécution au niveau des fonctions et des lignes dans ce fichier.

### 3. Comment fonctionne l'analyse

Le fichier `.exec` lui-même **n'est pas lisible par un humain**. Ce sont juste des données binaires de couverture.
Une fois votre application terminée, vous exécutez généralement une tâche de rapport (par exemple, Maven `jacoco:report` ou Gradle `jacocoTestReport`) qui :

* Lit les données du `destfile`
* Lit vos fichiers `.class` compilés et votre code source
* Génère un rapport de couverture en HTML, XML ou CSV

C'est à cette étape que vous voyez les pourcentages, les lignes de code colorées, etc.

### 4. Runtime vs. moment du rapport

* **Runtime :** L'agent enregistre l'exécution en mémoire et l'écrit dans `destfile`.
* **Moment du rapport :** Vous utilisez les outils JaCoCo (Maven, Gradle, CLI ou Ant) pour interpréter ce fichier `.exec` et générer des rapports lisibles.

Ainsi, le `destfile` lui-même est **juste des données d'exécution brutes** — il n'est pas analysé avant que vous n'exécutiez l'étape de rapport.

---

👉 En bref : Oui, lorsque votre application Spring Boot s'exécute avec l'agent JaCoCo, les informations de couverture sur les méthodes et les lignes sont enregistrées dans le `destfile`. Plus tard, les outils de rapport JaCoCo l'utilisent (avec les fichiers de classes/source) pour produire des rapports compréhensibles.

Voulez-vous que je vous montre également comment cela fonctionne étape par étape avec Spring Boot (par exemple, la configuration Maven + exécution + génération de rapport) ?