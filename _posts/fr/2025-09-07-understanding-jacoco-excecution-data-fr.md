---
audio: false
date: 2025-09-07
generated: true
image: false
lang: fr
layout: post
title: Comprendre les fichiers de données d'exécution JaCoCo
translated: true
type: note
---

Voici un guide pratique et complet avec tout ce que vous devez savoir.

# Qu'est-ce que `jacoco-it.exec` ?

* C'est un **fichier de données d'exécution JaCoCo** produit pendant les **tests d'intégration**.
* Le « `-it` » est simplement une **convention** (provenant de l'object *report-integration* du `jacoco-maven-plugin` et de la phase Failsafe). Les tests unitaires génèrent souvent `jacoco.exec`, tandis que les tests d'intégration génèrent `jacoco-it.exec`.
* Vous pouvez avoir plusieurs fichiers `.exec` (par module, par phase, par exécution) et les **fusionner** plus tard pour produire un seul rapport de couverture.

Configuration Maven typique :

```xml
<plugin>
  <groupId>org.jacoco</groupId>
  <artifactId>jacoco-maven-plugin</artifactId>
  <version>0.8.12</version>
  <executions>
    <!-- pour les tests unitaires -->
    <execution>
      <id>prepare-agent</id>
      <goals><goal>prepare-agent</goal></goals>
    </execution>
    <!-- pour les tests d'intégration -->
    <execution>
      <id>prepare-agent-integration</id>
      <goals><goal>prepare-agent-integration</goal></goals>
    </execution>
    <execution>
      <id>report</id>
      <phase>verify</phase>
      <goals><goal>report</goal></goals>
    </execution>
    <execution>
      <id>report-it</id>
      <phase>verify</phase>
      <goals><goal>report-integration</goal></goals>
    </execution>
  </executions>
</plugin>
```

Cette configuration écrit généralement `target/jacoco.exec` (unitaires) et `target/jacoco-it.exec` (intégration).

# Que contient un fichier `.exec` ?

* **Uniquement les hits des sondes**, indexés par classe.
* Concrètement : pour chaque classe chargée, JaCoCo calcule un **ID** (basé sur le bytecode) et stocke un **tableau booléen de sondes** (quelles instructions/branches ont été exécutées).
* Il stocke également un **id de session** et des horodatages.
* **Il ne contient *pas* le bytecode des classes, les noms de méthodes, les numéros de ligne, ou le code source**. Ces informations structurelles sont obtenues plus tard à partir de vos **fichiers de classe** et **sources** lorsque vous exécutez `jacoco:report` pour générer le HTML/XML.

Implications :

* Si vos classes changent après la génération du `.exec`, le fichier peut ne plus correspondre (les IDs ne correspondront pas). Générez toujours le rapport à partir de **la même build exacte** des fichiers de classe qui a produit le fichier exec.

# Contient-il des informations sur la structure des classes ?

* **Non.** Pas de méthodes, pas de numéros de ligne, pas de code source.
* C'est une **carte de hits** binaire et compacte par classe. L'étape de reporting lit vos **classes compilées** (et optionnellement les sources) pour mapper ces hits aux packages, classes, méthodes, lignes et branches.

# Sera-t-il mis à jour lors de l'attachement via `-javaagent` ?

Réponse courte : **Oui**, avec des détails :

* Lorsque vous démarrez votre JVM avec l'agent, celui-ci instrumente les classes **à la volée** et enregistre les hits des sondes **en mémoire**.
* L'agent **écrit** dans le `destfile` :

  * **À la fermeture de la JVM** (pour `output=file`, la valeur par défaut), ou
  * Lorsque vous effectuez explicitement un **dump** (TCP/JMX/API), ou
  * Lorsque `append=true` est défini, il va **ajouter/fusionner** avec un fichier existant au lieu de l'écraser.

Options courantes de l'agent :

```bash
-javaagent:/chemin/vers/org.jacoco.agent.jar=\
destfile=/chemin/vers/jacoco-it.exec,\
append=true,\
output=file
```

Autres modes utiles :

* `output=tcpserver` (écoute sur un port ; vous pouvez vous connecter et déclencher un dump)
* `output=tcpclient` (envoie vers un serveur)
* `jmx=true` (expose un MBean JMX pour dump/réinitialiser)
* Programmatique : `org.jacoco.agent.rt.RT.getAgent().dump(/*reset*/ true|false)`

Notes sur "mis à jour" :

* Avec `output=file` **et** `append=true`, **chaque dump** fusionne les tableaux de sondes dans le fichier existant (OU logique des hits).
* Sans `append=true`, la prochaine écriture **écrase** le fichier au dump/exit.
* Si vous avez **plusieurs JVM** (microservices, tests forkés), pointez chacune vers des **fichiers différents**, ou utilisez TCP/JMX pour collecter de manière centralisée, puis fusionnez.

# Flux de travail typiques

**Phase de test d'intégration (Failsafe) :**

* Maven attache l'agent à la/aux JVM(s) d'intégration-test avec `destfile=target/jacoco-it.exec`.
* À la fin, exécutez `jacoco:report-integration` qui lit :

  * `target/jacoco-it.exec` (hits)
  * `target/classes` (structure)
  * `src/main/java` (optionnel pour les lignes de source)
* Sortie : Couverture HTML/XML/CSV pour les *tests d'intégration uniquement*.

**Fusion de multiples exécutions :**

```bash
# via Maven
mvn jacoco:merge -Djacoco.destFile=target/merged.exec \
  -Djacoco.dataFileList="target/jacoco.exec,target/jacoco-it.exec,other.exec"
# puis
mvn jacoco:report -Djacoco.dataFile=target/merged.exec
```

# Pièges et conseils pratiques

* **Correspondance des builds** : générez les rapports à partir des **mêmes classes compilées** qui ont produit le `.exec`.
* **Forks parallèles** : lors de l'exécution de tests en parallèle ou dans plusieurs JVM, évitez que plusieurs processus n'écrivent dans le même fichier, sauf si `append=true` et que vous acceptez les ajouts concurrents (il est plus sûr d'avoir un fichier par JVM et de les fusionner ensuite).
* **Services de longue durée** : activez **TCP/JMX** ou appelez l'API runtime pour effectuer un **dump périodique** ; n'attendez pas la fin du processus.
* **Isolation du chargeur de classe** : certains serveurs d'application chargent la même classe deux fois ; JaCoCo déduplique par id de classe, mais soyez-en conscient dans les conteneurs complexes.
* **L'instrumentation hors ligne** existe, mais l'approche **javaagent** est généralement plus simple et plus robuste.

---

## Réponses directes à vos questions

* **« Qu'est-ce que `jacoco-it.exec` ? »**
  Le fichier de données d'exécution (hits des sondes) capturé pendant les **tests d'intégration**. Ce n'est qu'une convention de nommage ; fonctionnellement, c'est le même format que `jacoco.exec`.

* **« Contient-il des informations sur la structure des classes ? »**
  **Non.** Il stocke uniquement des **tableaux de hits de sondes** par classe et des métadonnées de session. Les informations sur les classes/méthodes/lignes proviennent de vos classes/sources compilées pendant l'étape de reporting.

* **« Sera-t-il mis à jour lors de l'attachement via `-javaagent` ? »**
  **Oui.** Avec `output=file`, l'agent écrit à la **fermeture de la JVM** ou **sur demande** (TCP/JMX/API). Avec `append=true`, il **fusionne** avec tout fichier existant ; sans cela, il l'**écrase**. Pour les exécutions multi-JVM, utilisez des fichiers séparés ou un dump distant et **fusionnez** ensuite.