---
audio: false
generated: true
lang: fr
layout: post
title: Localiser votre installation OpenJDK 21.0.7 sur Ubuntu 22.04
translated: true
type: note
---

La commande `java --version` que vous avez exécutée montre que vous avez OpenJDK 21.0.7 installé sur votre système, spécifiquement la version empaquetée pour Ubuntu 22.04. Ce résultat confirme que le Java Development Kit (JDK) est installé et accessible depuis votre ligne de commande.

L'emplacement de l'installation Java peut généralement être trouvé en vérifiant où se trouve le binaire `java`. Étant donné que vous êtes sur un système basé sur Ubuntu, OpenJDK est probablement installé dans un répertoire système standard, tel que `/usr/lib/jvm/`.

Pour localiser le chemin exact de l'installation Java :

1. **Trouver le chemin du binaire `java`** :
   Exécutez la commande suivante dans votre terminal :
   ```bash
   which java
   ```
   Cela produira probablement un résultat comme `/usr/bin/java`. Il s'agit d'un lien symbolique vers le véritable binaire Java.

2. **Suivre le lien symbolique vers l'emplacement réel** :
   Puisque `/usr/bin/java` est généralement un lien symbolique, vous pouvez trouver le répertoire d'installation actuel en exécutant :
   ```bash
   readlink -f $(which java)
   ```
   Cela pourrait produire un résultat comme `/usr/lib/jvm/java-21-openjdk-amd64/bin/java`, indiquant que le JDK est installé dans `/usr/lib/jvm/java-21-openjdk-amd64/`.

3. **Vérifier le répertoire d'installation** :
   Vous pouvez lister le contenu du répertoire JVM pour confirmer :
   ```bash
   ls /usr/lib/jvm/
   ```
   Vous devriez voir un répertoire comme `java-21-openjdk-amd64` ou similaire, qui contient l'installation OpenJDK.

### Résumé
Votre installation Java se trouve probablement dans `/usr/lib/jvm/java-21-openjdk-amd64/` (ou un répertoire similaire sous `/usr/lib/jvm/`). La commande `java` que vous avez exécutée est un lien symbolique pointant vers le binaire `java` dans ce répertoire. Si vous souhaitez confirmer le chemin exact, utilisez la commande `readlink -f $(which java)`.