---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Configuration du répertoire de sortie de l'agent JaCoCo
translated: true
type: note
---

Oui — exactement 👍.

Par défaut, si vous écrivez

```bash
-javaagent:/chemin/vers/jacocoagent.jar=destfile=jacoco.exec,output=file
```

alors `jacoco.exec` est créé dans le **répertoire de travail courant** du processus JVM (souvent la racine du serveur ou l'endroit depuis lequel vous avez lancé Liberty).

Si vous souhaitez contrôler son emplacement, donnez-lui un **chemin absolu ou relatif**, par exemple :

```bash
-javaagent:/chemin/vers/jacocoagent.jar=destfile=/opt/coverage-data/jacoco.exec,output=file
```

ou

```bash
-javaagent:/chemin/vers/jacocoagent.jar=destfile=target/jacoco.exec,output=file
```

(où `target/` est relatif au répertoire de démarrage).

Donc oui, si vous voulez garantir l'emplacement du fichier `.exec`, utilisez le chemin complet.

👉 Astuce : Dans les projets Maven/Gradle, il est courant de le pointer vers `target/` (Maven) ou `build/` (Gradle), afin que les plugins de rapport puissent le récupérer automatiquement plus tard.

Souhaitez-vous que je vous montre un exemple de `jvm.options` pour Liberty avec le chemin complet configuré ?