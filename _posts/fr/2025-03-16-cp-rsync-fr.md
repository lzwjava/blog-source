---
audio: false
generated: true
lang: fr
layout: post
title: Copie de fichiers avec structure de répertoire
translated: true
type: note
---

Compte tenu de la sortie de votre commande `find`, vous souhaitez copier tous les fichiers `.log` vers `/Users/lzwjava/projects/logs` tout en préservant leur structure de répertoire. Par exemple, un fichier comme `./CoreSimulator/FC275C39-59CC-4483-A64E-5D459D7A1D57/system.log` devrait se retrouver sous `/Users/lzwjava/projects/logs/CoreSimulator/FC275C39-59CC-4483-A64E-5D459D7A1D57/system.log`. Je vais vous montrer comment y parvenir en utilisant `find` combiné avec `cp` ou `rsync`, en veillant à ce que la hiérarchie des répertoires soit conservée.

---

### **Solution 1 : Utilisation de `find` avec `cp`**
Vous pouvez utiliser `find` pour localiser les fichiers `.log` et `cp` avec l'option `--parents` pour les copier tout en préservant leur structure de répertoire.

#### **Commande**
```bash
find . -name "*.log" -exec cp --parents {} /Users/lzwjava/projects/logs \;
```

#### **Explication**
- **`find . -name "*.log"`** : Localise tous les fichiers `.log` dans le répertoire courant et les sous-répertoires (comme dans votre exemple).
- **`-exec cp --parents {} /Users/lzwjava/projects/logs \;`** :
  - `cp --parents` : Copie le fichier et recrée son chemin de répertoire relatif à la source (`.`).
  - `{}` : Espace réservé pour chaque fichier trouvé par `find`.
  - `/Users/lzwjava/projects/logs` : Répertoire de destination.
  - `\;` : Termine la commande `-exec`.

#### **Résultat**
- `./CoreSimulator/FC275C39-59CC-4483-A64E-5D459D7A1D57/system.log` → `/Users/lzwjava/projects/logs/CoreSimulator/FC275C39-59CC-4483-A64E-5D459D7A1D57/system.log`
- La structure de répertoire sous `CoreSimulator` est préservée.

#### **Avant d'exécuter**
- Assurez-vous que `/Users/lzwjava/projects/logs` existe :
  ```bash
  mkdir -p /Users/lzwjava/projects/logs
  ```

---

### **Solution 2 : Utilisation de `rsync`**
`rsync` est un autre outil puissant qui peut copier des fichiers tout en préservant la structure des répertoires, et il est souvent plus efficace pour les opérations en masse.

#### **Commande**
```bash
find . -name "*.log" -exec rsync -R -a {} /Users/lzwjava/projects/logs \;
```

#### **Explication**
- **`-R`** : Utilise les chemins relatifs, préservant la structure de répertoire depuis la source (`.`).
- **`-a`** : Mode archive (préserve les horodatages, les permissions, etc.).
- `{}` : Chaque fichier `.log` trouvé.
- `/Users/lzwjava/projects/logs` : Répertoire cible.

#### **Résultat**
Identique au précédent — les fichiers sont copiés avec leurs chemins relatifs complets intacts.

#### **Avant d'exécuter**
- Créez le répertoire de destination s'il n'existe pas :
  ```bash
  mkdir -p /Users/lzwjava/projects/logs
  ```

---

### **Vérification de la copie**
Après avoir exécuté l'une ou l'autre commande, vérifiez la destination :
```bash
ls -R /Users/lzwjava/projects/logs
```
Vous devriez voir :
```
/Users/lzwjava/projects/logs:
CoreSimulator

/Users/lzwjava/projects/logs/CoreSimulator:
CoreSimulator.log  FC275C39-59CC-4483-A64E-5D459D7A1D57  Simulator.log

/Users/lzwjava/projects/logs/CoreSimulator/FC275C39-59CC-4483-A64E-5D459D7A1D57:
com.apple.itunesstored  system.log

/Users/lzwjava/projects/logs/CoreSimulator/FC275C39-59CC-4483-A64E-5D459D7A1D57/com.apple.itunesstored:
itunesstored.log
```

---

### **Points clés à noter**
- **Permissions :** Assurez-vous d'avoir un accès en écriture à `/Users/lzwjava/projects/logs`. Sinon, utilisez `sudo` (par exemple, `sudo cp ...`) ou ajustez les permissions :
  ```bash
  chmod -R u+w /Users/lzwjava/projects/logs
  ```
- **Écrasement :** Si des fichiers existent déjà à la destination :
  - `cp` écrasera sans avertissement.
  - `rsync -a` écrasera également, mais vous pouvez ajouter `--ignore-existing` pour ignorer les fichiers existants :
    ```bash
    find . -name "*.log" -exec rsync -R -a --ignore-existing {} /Users/lzwjava/projects/logs \;
    ```
- **Test à blanc (Vérification préalable) :**
  - Pour `cp`, ajoutez `echo` pour prévisualiser :
    ```bash
    find . -name "*.log" -exec echo cp --parents {} /Users/lzwjava/projects/logs \;
    ```
  - Pour `rsync`, utilisez `--dry-run` :
    ```bash
    find . -name "*.log" -exec rsync -R -a --dry-run {} /Users/lzwjava/projects/logs \;
    ```

---

### **Que choisir ?**
- **`cp`** : Plus simple, aucun outil supplémentaire nécessaire (disponible sur tous les systèmes de type Unix).
- **`rsync`** : Plus flexible (par exemple, pour la synchronisation, ignorer les doublons), mais nécessite que `rsync` soit installé (standard sur la plupart des systèmes).

Les deux fonctionneront dans votre cas. Je recommande de commencer par `cp --parents` pour sa simplicité.

---

### **Commande finale (recommandée)**
```bash
mkdir -p /Users/lzwjava/projects/logs
find . -name "*.log" -exec cp --parents {} /Users/lzwjava/projects/logs \;
```

Exécutez cette commande depuis votre répertoire `Logs` (`lzwjava@anonymous Logs %`), et c'est fait ! Faites-moi savoir si vous rencontrez des problèmes ou si vous souhaitez ajuster le comportement (par exemple, aplatir la structure).