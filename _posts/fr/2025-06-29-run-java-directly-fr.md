---
audio: false
generated: true
lang: fr
layout: post
title: Exécuter Java comme des scripts Python
translated: true
type: note
---

Pour exécuter le fichier `MultiMark.java` directement, de la même manière qu'un script Python, vous avez plusieurs options. Comme vous êtes sur un système de type Unix (comme l'indique le chemin `~/projects` et la commande `ls`), je vais vous proposer des étapes pour exécuter le programme Java de manière aussi fluide que possible. Voici deux approches principales :

---

### **Option 1 : Exécuter `MultiMark.java` directement avec la commande `java` (Java 11+)**
Depuis Java 11, vous pouvez exécuter un fichier source Java unique directement sans avoir à le compiler explicitement au préalable, ce qui se rapproche de l'exécution d'un script Python.

1. **Vérifier que Java est installé**
   Vérifiez si vous avez Java 11 ou une version ultérieure installée :
   ```bash
   java --version
   ```
   Si Java n'est pas installé ou si c'est une version antérieure, installez une version compatible (par exemple, OpenJDK) :
   ```bash
   sudo apt update
   sudo apt install openjdk-17-jdk
   ```

2. **Exécuter le fichier Java directement**
   Accédez au répertoire contenant `MultiMark.java` :
   ```bash
   cd ~/projects/lzwjava.github.io/scripts/benchmark
   ```
   Exécutez le fichier Java directement en utilisant :
   ```bash
   java MultiMark.java
   ```
   Cette commande compile et exécute le fichier `MultiMark.java` en une seule étape. Le résultat (par exemple, les cœurs du CPU, le nombre de threads et les temps) s'affichera dans le terminal.

---

### **Option 2 : Créer un script shell pour plus de commodité**
Pour rendre l'exécution de `MultiMark.java` encore plus similaire à celle d'un script Python (par exemple, `./multimark`), vous pouvez créer un wrapper sous forme de script shell.

1. **Créer un script shell**
   Créez un fichier nommé `multimark` (sans extension) dans le répertoire `scripts/benchmark` :
   ```bash
   nano ~/projects/lzwjava.github.io/scripts/benchmark/multimark
   ```
   Ajoutez le contenu suivant :
   ```bash
   #!/bin/bash
   java MultiMark.java
   ```
   Enregistrez et quittez (`Ctrl+O`, `Entrée`, `Ctrl+X` dans nano).

2. **Rendre le script exécutable**
   Définissez les permissions d'exécution :
   ```bash
   chmod +x multimark
   ```

3. **Exécuter le script**
   Vous pouvez maintenant exécuter le programme comme un script Python :
   ```bash
   ./multimark
   ```
   Cela exécutera `java MultiMark.java` en arrière-plan.

---

### **Option 3 : Compiler et exécuter séparément (approche traditionnelle)**
Si vous préférez ou devez compiler le fichier Java explicitement (par exemple, pour des versions antérieures de Java ou pour vérifier les erreurs de compilation), suivez ces étapes :

1. **Compiler le fichier Java**
   Accédez au répertoire :
   ```bash
   cd ~/projects/lzwjava.github.io/scripts/benchmark
   ```
   Compilez le fichier source Java :
   ```bash
   javac MultiMark.java
   ```
   Cela génère un fichier `MultiMark.class`.

2. **Exécuter le programme compilé**
   Exécutez la classe compilée :
   ```bash
   java MultiMark
   ```
   Remarque : Utilisez `MultiMark` (sans `.java`) car vous exécutez le fichier de classe compilé.

---

### **Pour une expérience similaire à Python**
Pour que l'expérience soit aussi proche que possible de l'exécution d'un script Python, l'**Option 1** (`java MultiMark.java` direct) est la plus simple, car elle évite la compilation manuelle. L'**Option 2** (script shell) est idéale si vous voulez une commande unique comme `./multimark` qui ressemble à l'exécution de `./script.py`.

### **Notes**
- **Version de Java** : Le code utilise des bibliothèques Java standard (`java.util.*` et `System.nanoTime`), il devrait donc fonctionner avec Java 8 ou ultérieur. La fonctionnalité d'exécution directe (`java MultiMark.java`) nécessite Java 11+.
- **Performances** : Le programme `MultiMark.java` évalue les performances du tri avec plusieurs threads. L'exécuter directement ou via un script n'affectera pas ses performances, mais assurez-vous que votre système dispose de ressources suffisantes (CPU/mémoire) pour les nombres de threads testés (jusqu'à 64 threads).
- **Contexte du répertoire** : Puisque vous avez montré `ls scripts/benchmark/`, j'ai supposé que `MultiMark.java` se trouve dans ce répertoire. Ajustez les chemins si ce n'est pas le cas.
- **Gestion des erreurs** : Si vous rencontrez des erreurs (par exemple, `java: command not found`), assurez-vous que Java est installé et ajouté à votre `PATH`. Si le programme échoue (par exemple, en raison de limites de mémoire ou de threads), vérifiez la stack trace pour plus de détails.

Si vous souhaitez intégrer cela dans un workflow avec vos scripts Python (`executormark.py`, `multimark.py`, `threadmark.py`), faites-le moi savoir et je pourrai suggérer des moyens de les combiner (par exemple, appeler le programme Java depuis Python).