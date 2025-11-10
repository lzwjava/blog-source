---
audio: false
generated: true
lang: fr
layout: post
title: Corriger l'Erreur de Classpath Java
translated: true
type: note
---

L'erreur que vous avez rencontrée (`Could not find or load main class scripts.benchmark.MultiMark`) se produit car vous avez essayé d'exécuter le programme Java depuis le répertoire racine du projet (`~/projects/lzwjava.github.io`) en utilisant le nom qualifié complet de la classe (`scripts.benchmark.MultiMark`), mais l'environnement d'exécution Java s'attend à ce que la classe soit exécutée depuis le répertoire où la structure du package commence, ou vous devez spécifier le classpath correctement. Lorsque vous êtes passé au répertoire `scripts/benchmark` et avez exécuté `java MultiMark`, cela a fonctionné car la classe était dans le bon répertoire par rapport à la commande.

Pour exécuter `MultiMark.java` ou `MultiMark.class` depuis le répertoire racine du projet (`~/projects/lzwjava.github.io`) sans changer de répertoire, vous pouvez utiliser l'option `-cp` (classpath) avec la commande `java` pour indiquer à Java où trouver le fichier de classe compilé. Voici deux façons d'y parvenir, en restant dans le répertoire racine :

---

### **Option 1 : Exécuter la classe compilée avec le classpath**
Si `MultiMark.class` existe déjà dans `scripts/benchmark/` (comme indiqué dans votre sortie `ls`), vous pouvez l'exécuter depuis le répertoire racine en spécifiant le classpath.

1. **Restez dans le répertoire racine**
   Assurez-vous d'être dans `~/projects/lzwjava.github.io`.

2. **Exécutez le programme**
   Utilisez l'option `-cp` pour pointer vers le répertoire contenant le fichier de classe :
   ```bash
   java -cp scripts/benchmark MultiMark
   ```
   - `-cp scripts/benchmark` indique à Java de chercher les classes dans le répertoire `scripts/benchmark`.
   - `MultiMark` est le nom de la classe (sans le suffixe `.class` ou le préfixe de package, car `MultiMark.java` n'a pas d'instruction `package`).

   Cela devrait produire une sortie comme :
   ```
   CPU cores: 32
   ...
   ```

3. **Remarque** : Si `MultiMark.class` est obsolète ou manquant, compilez d'abord le fichier source depuis le répertoire racine :
   ```bash
   javac scripts/benchmark/MultiMark.java
   ```
   Puis exécutez la commande ci-dessus.

---

### **Option 2 : Exécuter directement le fichier source avec le classpath (Java 11+)**
Si vous préférez exécuter directement le fichier source (comme `python script.py`), vous pouvez utiliser la commande `java` avec le chemin du fichier source, en spécifiant le classpath.

1. **Restez dans le répertoire racine**
   Assurez-vous d'être dans `~/projects/lzwjava.github.io`.

2. **Exécutez le fichier source**
   Utilisez :
   ```bash
   java -cp scripts/benchmark scripts/benchmark/MultiMark.java
   ```
   - `-cp scripts/benchmark` définit le classpath vers le répertoire contenant la source.
   - `scripts/benchmark/MultiMark.java` spécifie le fichier source à compiler et exécuter.

   Cela compile et exécute `MultiMark.java` en une seule étape, produisant la même sortie qu'auparavant.

---

### **Option 3 : Créer un script shell dans le répertoire racine**
Pour plus de commodité (comme exécuter `./multimark` depuis le répertoire racine), vous pouvez créer un script shell dans le répertoire racine (`~/projects/lzwjava.github.io`).

1. **Créez un script shell**
   Créez un fichier nommé `multimark` dans le répertoire racine :
   ```bash
   nano multimark
   ```
   Ajoutez :
   ```bash
   #!/bin/bash
   java -cp scripts/benchmark MultiMark
   ```
   Sauvegardez et quittez.

2. **Rendez-le exécutable**
   ```bash
   chmod +x multimark
   ```

3. **Exécutez le script**
   Depuis le répertoire racine :
   ```bash
   ./multimark
   ```
   Cela exécute le programme Java sans avoir besoin de changer de répertoire.

4. **Optionnel : Compiler dans le script**
   Si vous voulez que le script gère la compilation (par exemple, si le fichier source change), modifiez le script :
   ```bash
   #!/bin/bash
   javac scripts/benchmark/MultiMark.java
   java -cp scripts/benchmark MultiMark
   ```

---

### **Points clés à noter**
- **Classpath (`-cp`)** : L'option `-cp` indique à Java où trouver les classes ou les fichiers source. Comme `MultiMark.java` n'a pas d'instruction `package`, le nom de la classe est simplement `MultiMark`, et non `scripts.benchmark.MultiMark`. S'il y avait une ligne `package scripts.benchmark;`, vous devriez utiliser `java -cp . scripts.benchmark.MultiMark` depuis la racine.
- **Version de Java** : L'exécution directe du fichier source (`java scripts/benchmark/MultiMark.java`) nécessite Java 11 ou ultérieur. Votre système semble avoir Java installé, car cela a fonctionné depuis le répertoire `scripts/benchmark`.
- **Répertoire** : Ces solutions vous permettent de rester dans le répertoire racine (`~/projects/lzwjava.github.io`), conformément à votre préférence.
- **Automatisation** : Le script shell (Option 3) se rapproche le plus d'une expérience de type Python, car vous pouvez exécuter `./multimark` comme un script Python. Vous pourriez également l'ajouter à votre `PATH` pour un accès global, mais c'est optionnel.
- **Gestion des erreurs** : Si vous obtenez des erreurs comme `NoClassDefFoundError`, assurez-vous que `MultiMark.class` existe dans `scripts/benchmark/` ou recompilez. Si Java n'est pas trouvé, vérifiez l'installation (`java --version`).

Si vous souhaitez intégrer cela à vos scripts Python ou avez besoin d'un flux de travail spécifique (par exemple, exécuter `multimark.py` et `MultiMark.java` ensemble), faites-le moi savoir !