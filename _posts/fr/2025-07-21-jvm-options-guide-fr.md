---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Guide rapide des options JVM par catégorie
translated: true
type: note
---

Dans le monde de la JVM, il existe **de nombreuses options** que vous pouvez configurer, et l'ensemble exact dépend de l'implémentation de la JVM (HotSpot, OpenJ9, GraalVM, etc.) et de sa version. Globalement, les options JVM se répartissent en ces catégories :

---

## 1. Options Standard

Ces options sont stables, indépendantes de la version, officiellement documentées et garanties de fonctionner. Exemples :

* `-classpath` / `-cp` → spécifier le classpath.
* `-Dproperty=value` → définir les propriétés système.
* `-version` → afficher la version de la JVM.
* `-Xms` / `-Xmx` → taille initiale et maximale du tas.
* `-ea` → activer les assertions.

---

## 2. Options Non-Standard (`-X`)

Ces options sont spécifiques à la JVM et ne sont pas garanties de rester stables. Exemples (HotSpot) :

* `-Xint` → mode interprété uniquement (pas de JIT).
* `-Xcomp` → compiler toutes les méthodes dès leur première utilisation.
* `-Xbatch` → désactiver la compilation en arrière-plan.
* `-Xss512k` → définir la taille de la pile des threads.

---

## 3. Options Avancées (`-XX`)

Elles permettent un réglage fin du GC, du JIT et du comportement à l'exécution. Exemples :

* `-XX:+UseG1GC` → activer le garbage collector G1.
* `-XX:+PrintGCDetails` → journaliser l'activité du GC.
* `-XX:MaxMetaspaceSize=256m` → limiter l'espace méta.
* `-XX:+HeapDumpOnOutOfMemoryError` → dump le tas en cas d'erreur OutOfMemory.
* `-XX:+UnlockExperimentalVMOptions` → autoriser les flags expérimentaux.
* `-XX:+UseStringDeduplication` → réduire l'utilisation de la mémoire en dédupliquant les chaînes.

---

## 4. Options de Diagnostic & Expérimentales

Certains flags sont cachés et nécessitent un déverrouillage :

* `-XX:+UnlockDiagnosticVMOptions` → activer les flags de diagnostic.
* `-XX:+UnlockExperimentalVMOptions` → autoriser le réglage expérimental.

Vous pouvez ensuite utiliser des options comme :

* `-XX:+PrintFlagsFinal` → lister toutes les options JVM et leurs valeurs.
* `-XX:+LogCompilation` → journaliser l'activité du compilateur JIT.

---

## 5. Outils pour Travailler avec les Options JVM

* **`java -X`** → liste les options non standard pour votre build JVM.
* **`java -XX:+PrintFlagsFinal`** → affiche toutes les options reconnues avec leurs valeurs par défaut et actuelles.
* **`jcmd <pid> VM.flags`** → affiche les flags JVM pour un processus en cours d'exécution.
* **`jcmd <pid> VM.uptime`**, `jcmd <pid> VM.system_properties` → inspection à l'exécution.
* **`jps` + `jinfo`** → lister les processus Java et afficher leurs options JVM.
* **VisualVM / JConsole** → surveiller le tas, le GC et les paramètres d'exécution.

---

👉 Une manière pratique d'explorer votre environnement est d'exécuter :

```bash
java -XX:+PrintFlagsFinal | grep GC
```

pour voir toutes les options liées au GC, ou simplement :

```bash
java -X
```

pour vérifier les flags non standard disponibles.

---

Souhaitez-vous que je vous fournisse **un aide-mémoire catégorisé des options JVM les plus utiles** (GC, mémoire, débogage, réglage des performances) pour que vous n'ayez pas à analyser l'énorme liste de `PrintFlagsFinal` ?