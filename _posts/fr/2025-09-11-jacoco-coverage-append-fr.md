---
audio: false
date: 2025-09-11
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: Fichier de Couverture JaCoCo et Mode Ajout
translated: true
type: note
---

C'est un détail subtil mais important dans le fonctionnement de JaCoCo.

### Comportement de `jacoco:prepare-agent`

* Lorsque Maven exécute le goal **`prepare-agent`**, il ne génère pas immédiatement le fichier de couverture.
* À la place, il **configure la JVM** (généralement via un argument `-javaagent:jacocoagent.jar`) pour que les données de couverture soient collectées pendant l'exécution de vos tests ou de votre application.
* L'emplacement du fichier `.exec` est contrôlé par la propriété `jacoco.destFile` (par défaut `target/jacoco.exec`, mais souvent personnalisé, par exemple `target/jacoco-it.exec`).

### Que se passe-t-il si le fichier existe déjà ?

* Par défaut, **JaCoCo écrasera le fichier** lorsque la JVM démarre avec l'agent.
* Cela signifie que chaque exécution de `prepare-agent` → exécution des tests produira un fichier `.exec` *neuf*.
* Il n'ajoute pas automatiquement les données — les anciennes données sont perdues sauf si vous configurez autrement.

### Comment ajouter au lieu d'écraser

Si vous souhaitez que plusieurs exécutions s'accumulent dans le même fichier exec, vous devez explicitement activer le mode append :

```xml
<plugin>
  <groupId>org.jacoco</groupId>
  <artifactId>jacoco-maven-plugin</artifactId>
  <version>0.8.12</version>
  <configuration>
    <destFile>${project.build.directory}/jacoco-it.exec</destFile>
    <append>true</append>   <!-- ✅ ajoute les données de couverture -->
  </configuration>
</plugin>
```

Avec `<append>true</append>`, si le fichier existe, les nouvelles données de couverture seront fusionnées dedans.

### Donc en résumé

* **Par défaut :** Chaque exécution remplace l'ancien `.exec`.
* **Avec `append=true` :** La couverture de multiples exécutions JVM (ou de multiples modules/tests) est fusionnée dans le même fichier.

---

Souhaitez-vous que j'explique également comment cela interagit avec les **builds Maven multi-modules** (où chaque module peut essayer d'écrire son propre exec JaCoCo), puisque c'est souvent la raison pour laquelle les gens rencontrent des problèmes d'écrasement vs d'ajout ?