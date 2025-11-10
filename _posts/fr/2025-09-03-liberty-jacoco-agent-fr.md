---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Comparaison de Liberty Agent et JaCoCo Agent
translated: true
type: note
---

Dans WebSphere Liberty (WLP), le `ws-javaagent.jar` est l'agent d'instrumentation Java propre à IBM. Il est principalement utilisé pour la surveillance du runtime, les diagnostics et l'intégration avec des outils tels que Application Performance Management (APM), Health Center, ou les capacités de surveillance de Liberty elle-même. Lorsque vous l'activez, Liberty peut collecter automatiquement des métriques au niveau JVM, telles que le profilage, le garbage collection, les threads, etc.

L'agent `jacocoagent.jar` de JaCoCo, quant à lui, est spécifiquement un **agent de couverture de code**. Son but est d'instrumenter le bytecode au moment de l'exécution afin que les exécutions de tests ou d'applications produisent des données de couverture (par exemple, quelles classes, méthodes et branches ont été exécutées).

Ainsi, la distinction est la suivante :

* **`ws-javaagent.jar`** → surveillance générale, profilage, diagnostics pour Liberty et les outils IBM.
* **`jacocoagent.jar`** → reporting de couverture de code/test, indépendant de Liberty.

Vous ne devriez pas remplacer l'agent de JaCoCo par celui de Liberty. Si votre objectif est un **reporting de couverture de test** (pour les pipelines d'intégration continue, SonarQube, les rapports Maven/Gradle, etc.), vous devez continuer à utiliser l'**agent JaCoCo**. L'agent Liberty ne générera pas les fichiers de couverture `.exec` de JaCoCo.

Mais vous *pouvez* exécuter les deux agents simultanément si nécessaire — Java prend en charge plusieurs arguments `-javaagent`. Par exemple :

```bash
-javaagent:/chemin/vers/ws-javaagent.jar
-javaagent:/chemin/vers/jacocoagent.jar=destfile=jacoco.exec,output=file
```

👉 En bref :
Utilisez **`jacocoagent.jar`** pour la couverture de code.
Utilisez **`ws-javaagent.jar`** si vous avez besoin des diagnostics/profilage de Liberty.
Ils servent des objectifs différents et ne sont pas interchangeables.

Souhaitez-vous que je vous montre également comment les configurer ensemble dans un fichier d'options JVM du serveur Liberty ?