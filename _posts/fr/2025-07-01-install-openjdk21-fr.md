---
audio: false
generated: true
lang: fr
layout: post
title: Mise à niveau vers OpenJDK 21 sur macOS
translated: true
type: note
---

Étant donné que vous avez actuellement OpenJDK 17 installé via Homebrew sur votre système macOS, voici un guide concis pour installer OpenJDK 21, qui est la dernière version LTS (Long Term Support) à la date actuelle du 1er juillet 2025. Vous pouvez installer OpenJDK 21 aux côtés d'OpenJDK 17 et basculer entre eux selon vos besoins. La méthode la plus simple consiste à utiliser Homebrew, mais je fournirai également une option d'installation manuelle.

### Méthode 1 : Installer OpenJDK 21 en utilisant Homebrew (Recommandé)
Homebrew est déjà installé sur votre système, comme l'indique votre version actuelle de Java. C'est l'approche la plus simple et la plus facile à maintenir.

1. **Mettre à jour Homebrew** :
   Assurez-vous que Homebrew est à jour pour récupérer les derniers paquets :
   ```bash
   brew update
   ```

2. **Installer OpenJDK 21** :
   Homebrew fournit une formule spécifique pour OpenJDK 21. Exécutez la commande suivante :
   ```bash
   brew install openjdk@21
   ```
   Ceci installe OpenJDK 21 de manière "keg-only", ce qui signifie qu'il ne sera pas lié symboliquement dans `/usr/local/bin` pour éviter les conflits avec d'autres versions de Java.

3. **Ajouter OpenJDK 21 à votre PATH** :
   Pour utiliser OpenJDK 21, vous devez l'ajouter au PATH de votre système. Homebrew fournira des instructions après l'installation, mais généralement, vous pouvez le lier temporairement ou définitivement :
   - **Temporaire (pour la session en cours)** :
     ```bash
     export PATH="/opt/homebrew/opt/openjdk@21/bin:$PATH"
     ```
   - **Définitif (ajouter à la configuration du shell)** :
     Ouvrez votre fichier de configuration du shell (probablement `~/.zshrc` car macOS utilise Zsh par défaut) :
     ```bash
     nano ~/.zshrc
     ```
     Ajoutez la ligne suivante :
     ```bash
     export PATH="/opt/homebrew/opt/openjdk@21/bin:$PATH"
     ```
     Enregistrez et fermez le fichier, puis appliquez les modifications :
     ```bash
     source ~/.zshrc
     ```

4. **Définir JAVA_HOME** :
   Pour s'assurer que les applications Java peuvent localiser OpenJDK 21, définissez la variable d'environnement `JAVA_HOME` :
   ```bash
   export JAVA_HOME=$(/usr/libexec/java_home -v 21)
   ```
   Ajoutez ceci à votre `~/.zshrc` pour que ce soit définitif :
   ```bash
   echo 'export JAVA_HOME=$(/usr/libexec/java_home -v 21)' >> ~/.zshrc
   source ~/.zshrc
   ```

5. **Vérifier l'installation** :
   Vérifiez qu'OpenJDK 21 est installé et actif :
   ```bash
   java -version
   ```
   Vous devriez voir une sortie similaire à :
   ```
   openjdk 21.0.1 2023-10-17
   OpenJDK Runtime Environment (build 21.0.1+12)
   OpenJDK 64-Bit Server VM (build 21.0.1+12, mixed mode, sharing)
   ```

6. **Basculer entre les versions de Java** :
   Puisque vous avez OpenJDK 17 installé, vous pouvez basculer entre les versions en utilisant `/usr/libexec/java_home`. Par exemple :
   - Pour utiliser OpenJDK 17 :
     ```bash
     export JAVA_HOME=$(/usr/libexec/java_home -v 17)
     ```
   - Pour utiliser OpenJDK 21 :
     ```bash
     export JAVA_HOME=$(/usr/libexec/java_home -v 21)
     ```
   Alternativement, envisagez d'utiliser un gestionnaire de versions comme `jenv` (installez-le via `brew install jenv`) pour basculer plus facilement :
   ```bash
   jenv add /Library/Java/JavaVirtualMachines/openjdk-21.jdk/Contents/Home
   jenv add /Library/Java/JavaVirtualMachines/openjdk-17.jdk/Contents/Home
   jenv enable-plugin export
   jenv global 21
   ```

### Méthode 2 : Installation manuelle
Si vous préférez ne pas utiliser Homebrew, vous pouvez installer OpenJDK 21 manuellement.

1. **Télécharger OpenJDK 21** :
   - Visitez le site officiel OpenJDK (jdk.java.net/21) ou un fournisseur de confiance comme Oracle, Azul ou Adoptium.
   - Pour Apple Silicon (M1/M2), téléchargez le fichier `macOS/AArch64` tar.gz. Pour les Macs à base d'Intel, choisissez `macOS/x64`.
   - Exemple : Sur la page de téléchargement d'Oracle JDK 21, sélectionnez le fichier tar.gz ARM64 ou x64.

2. **Vérifier le téléchargement** :
   Vérifiez l'intégrité du fichier téléchargé en utilisant sa somme de contrôle SHA256 :
   ```bash
   shasum -a 256 openjdk-21.0.1_macos-aarch64_bin.tar.gz
   ```
   Comparez le résultat avec la somme de contrôle fournie sur la page de téléchargement.

3. **Extraire le fichier** :
   Extrayez le fichier tar.gz vers un répertoire de votre choix, comme votre répertoire personnel :
   ```bash
   tar -xf openjdk-21.0.1_macos-aarch64_bin.tar.gz -C ~/OpenJDK
   ```
   Le JDK sera extrait vers `~/OpenJDK/jdk-21.0.1.jdk/Contents/Home`.

4. **Déplacer vers le répertoire système** (Optionnel) :
   Pour plus de cohérence, vous pouvez déplacer le JDK vers le répertoire Java standard de macOS :
   ```bash
   sudo mv ~/OpenJDK/jdk-21.0.1.jdk /Library/Java/JavaVirtualMachines/
   ```

5. **Définir JAVA_HOME et PATH** :
   Mettez à jour votre `~/.zshrc` pour inclure :
   ```bash
   export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk-21.0.1.jdk/Contents/Home
   export PATH=$JAVA_HOME/bin:$PATH
   ```
   Appliquez les modifications :
   ```bash
   source ~/.zshrc
   ```

6. **Vérifier l'installation** :
   Confirmez l'installation :
   ```bash
   java -version
   ```
   Assurez-vous qu'il affiche OpenJDK 21.

### Notes
- **Compatibilité Apple Silicon** : Assurez-vous de télécharger la version AArch64 pour les Macs M1/M2 afin d'éviter les problèmes de performance. Homebrew sélectionne automatiquement l'architecture correcte.
- **JDK multiples** : macOS prend en charge plusieurs JDK dans `/Library/Java/JavaVirtualMachines/`. Utilisez `/usr/libexec/java_home -v <version>` pour basculer entre eux.
- **Avantage de Homebrew** : Homebrew simplifie les mises à jour (`brew upgrade openjdk@21`) et assure la compatibilité avec votre système.
- **Fournisseurs alternatifs** : Vous pouvez également utiliser les builds Azul Zulu ou Eclipse Temurin d'OpenJDK 21, disponibles sur leurs sites respectifs (par exemple, azul.com ou adoptium.net).

Si vous rencontrez des problèmes, faites-le-moi savoir et je pourrai vous aider à les résoudre![](https://www.geeksforgeeks.org/how-to-install-openjdk-in-macos/)[](https://formulae.brew.sh/formula/openjdk%4021)[](https://codetrips.com/2023/10/15/installing-java-jdk-21-macos/)