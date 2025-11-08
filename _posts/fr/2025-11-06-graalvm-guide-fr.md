---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Guide d'installation et d'utilisation de GraalVM
translated: true
type: note
---

## Qu'est-ce que GraalVM ?

GraalVM est un runtime open source haute performance (distribution JDK) qui prend en charge plusieurs langages de programmation comme Java, JavaScript, Python, et plus encore. Il dispose d'un compilateur JIT avancé pour une exécution plus rapide et de la capacité à compiler des applications Java en exécutables natifs via Native Image, réduisant ainsi le temps de démarrage et l'empreinte mémoire.

## Installation

1. **Télécharger GraalVM** :
   - Allez sur la page officielle de téléchargement de GraalVM.
   - Choisissez l'Édition Communautaire (gratuite) ou Oracle GraalVM (avec des fonctionnalités supplémentaires).
   - Sélectionnez la version pour votre plateforme (par exemple, Linux, macOS, Windows) et votre architecture (x64 ou ARM).
   - En 2025, la dernière version stable est GraalVM pour JDK 22 ou 23 — vérifiez le site pour la version la plus récente.

2. **Extraire et Installer** :
   - Dézippez l'archive téléchargée dans un répertoire, par exemple `/opt/graalvm` sur Linux/macOS ou `C:\Program Files\GraalVM` sur Windows.
   - Aucun programme d'installation n'est nécessaire ; c'est une distribution portable.

3. **Définir les Variables d'Environnement** :
   - Définissez `JAVA_HOME` sur le répertoire GraalVM (par exemple, `export JAVA_HOME=/opt/graalvm` sur Linux/macOS).
   - Ajoutez le répertoire `bin` à votre `PATH` (par exemple, `export PATH=$JAVA_HOME/bin:$PATH`).
   - Vérifiez avec `java -version` ; cela devrait afficher les détails de GraalVM.

4. **Installer des Composants Supplémentaires (Optionnel)** :
   - Utilisez `gu` (GraalVM Updater) pour les runtimes de langages ou Native Image : `gu install native-image` (nécessite des outils de build comme `build-essential` sur Linux).

## Construire un Programme Hello World

Nous utiliserons Java pour cet exemple, car c'est le langage principal de GraalVM. Créez une simple application "Hello World", compilez-la et exécutez-la.

### Étape 1 : Écrire le Code
Créez un fichier nommé `HelloWorld.java` :

```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World from GraalVM!");
    }
}
```

### Étape 2 : Compiler
Ouvrez un terminal dans le répertoire contenant le fichier et exécutez :
```
javac HelloWorld.java
```
Cela produit `HelloWorld.class`.

### Étape 3 : Exécuter
```
java HelloWorld
```
Sortie :
```
Hello, World from GraalVM!
```

### Avancé : Compiler en Exécutable Natif
La fonctionnalité Native Image de GraalVM vous permet de construire un binaire autonome.

1. Assurez-vous que Native Image est installé : `gu install native-image`.
2. Générez une configuration (le premier lancement peut le nécessiter) :
   ```
   native-image --no-fallback -H:+ReportExceptionStackTraces HelloWorld
   ```
   - Cela crée `HelloWorld` (ou `helloworld.exe` sur Windows), un binaire natif.
   - Lors de la première construction, il analyse l'application et peut prendre quelques minutes.

3. Exécutez le binaire natif :
   ```
   ./HelloWorld
   ```
   La sortie est la même, mais il démarre instantanément avec une faible utilisation de la mémoire.

## Conseils pour Utiliser GraalVM
- **Changer de JDK** : Utilisez SDKMAN ! (`sdk install java 22.0.2-graal`) pour une gestion facile.
- **Multi-Langage** : Exécutez du code Node.js avec `node` depuis GraalVM, ou Python avec `python`.
- **Performance** : Activez le JIT de GraalVM avec `-XX:+UnlockExperimentalVMOptions -XX:+UseJVMCICompiler`.
- **Dépannage** : Vérifiez les logs dans `~/.gu/` pour les problèmes ; assurez-vous que votre système a un compilateur C pour Native Image.

Pour plus de détails, consultez la documentation officielle.

[Téléchargements GraalVM](https://www.graalvm.org/downloads/)  
[Guide de l'Utilisateur GraalVM](https://www.graalvm.org/latest/reference-manual/)  
[Tutoriel Native Image](https://www.graalvm.org/latest/reference-manual/native-image/)