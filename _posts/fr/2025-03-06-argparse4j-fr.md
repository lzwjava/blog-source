---
audio: false
generated: true
lang: fr
layout: post
title: Analyse des Arguments de Ligne de Commande en Java
translated: true
---

Pour utiliser `net.sourceforge.argparse4j`, une bibliothèque Java pour analyser les arguments de ligne de commande inspirée par `argparse` de Python, suivez ces étapes :

---

### 1. **Ajouter la Dépendance**
Pour inclure `argparse4j` dans votre projet, ajoutez-le en tant que dépendance. Si vous utilisez Maven, mettez à jour votre `pom.xml` avec ce qui suit :

```xml
<dependency>
    <groupId>net.sourceforge.argparse4j</groupId>
    <artifactId>argparse4j</artifactId>
    <version>0.9.0</version>
</dependency>
```

Pour d'autres outils de construction comme Gradle, consultez le [Maven Central Repository](https://central.sonatype.com/artifact/net.sourceforge.argparse4j/argparse4j) pour la configuration équivalente.

---

### 2. **Créer un Objet `ArgumentParser`**
Commencez par créer une instance `ArgumentParser` en utilisant `ArgumentParsers.newFor("prog").build()`, où `"prog"` est le nom de votre programme. Vous pouvez également ajouter une description et activer la génération automatique de l'aide.

**Exemple :**
```java
import net.sourceforge.argparse4j.ArgumentParsers;
import net.sourceforge.argparse4j.inf.ArgumentParser;

ArgumentParser parser = ArgumentParsers.newFor("Checksum").build()
    .defaultHelp(true)  // Active l'option -h/--help
    .description("Calculer la somme de contrôle des fichiers donnés.");
```

---

### 3. **Ajouter des Arguments**
Définissez les arguments de ligne de commande que votre programme acceptera en utilisant `parser.addArgument()`. Vous pouvez spécifier :
- **Arguments optionnels** (par exemple, `-t`, `--type`) avec des indicateurs, des choix, des valeurs par défaut et du texte d'aide.
- **Arguments positionnels** (par exemple, `file`) avec un support optionnel de longueur variable en utilisant `.nargs("*")`.

**Exemple :**
```java
parser.addArgument("-t", "--type")
    .choices("SHA-256", "SHA-512", "SHA1")  // Limite à ces options
    .setDefault("SHA-256")                  // Valeur par défaut si non fournie
    .help("Spécifier la fonction de hachage à utiliser");  // Description pour le message d'aide

parser.addArgument("file")
    .nargs("*")                             // Accepte zéro ou plusieurs arguments
    .help("Fichier pour calculer la somme de contrôle");    // Description pour le message d'aide
```

---

### 4. **Analyser les Arguments de Ligne de Commande**
Analysez les arguments de ligne de commande (généralement passés en tant que `String[] args` depuis votre méthode `main`) en utilisant `parser.parseArgs()`. Enveloppez ceci dans un bloc try-catch pour gérer les erreurs d'analyse de manière élégante.

**Exemple :**
```java
import net.sourceforge.argparse4j.inf.Namespace;
import net.sourceforge.argparse4j.inf.ArgumentParserException;

public class Checksum {
    public static void main(String[] args) {
        ArgumentParser parser = ArgumentParsers.newFor("Checksum").build()
            .defaultHelp(true)
            .description("Calculer la somme de contrôle des fichiers donnés.");

        parser.addArgument("-t", "--type")
            .choices("SHA-256", "SHA-512", "SHA1").setDefault("SHA-256")
            .help("Spécifier la fonction de hachage à utiliser");
        parser.addArgument("file").nargs("*")
            .help("Fichier pour calculer la somme de contrôle");

        Namespace ns = null;
        try {
            ns = parser.parseArgs(args);  // Analyser les arguments
        } catch (ArgumentParserException e) {
            parser.handleError(e);        // Imprimer l'erreur et le message d'aide
            System.exit(1);               // Quitter en cas d'erreur
        }
    }
}
```

---

### 5. **Accéder aux Valeurs Analysées**
La méthode `parseArgs()` retourne un objet `Namespace` contenant les valeurs des arguments analysés. Utilisez des méthodes comme `getString()` ou `getList()` pour les récupérer.

**Exemple :**
```java
String hashType = ns.getString("type");  // par exemple, "SHA-256"
List<String> files = ns.getList("file"); // Liste de noms de fichiers

System.out.println("Type de hachage : " + hashType);
System.out.println("Fichiers : " + files);
```

---

### Tout Assembler
Voici un exemple complet :

```java
import net.sourceforge.argparse4j.ArgumentParsers;
import net.sourceforge.argparse4j.inf.ArgumentParser;
import net.sourceforge.argparse4j.inf.ArgumentParserException;
import net.sourceforge.argparse4j.inf.Namespace;
import java.util.List;

public class Checksum {
    public static void main(String[] args) {
        // Étape 2 : Créer le parseur
        ArgumentParser parser = ArgumentParsers.newFor("Checksum").build()
            .defaultHelp(true)
            .description("Calculer la somme de contrôle des fichiers donnés.");

        // Étape 3 : Ajouter des arguments
        parser.addArgument("-t", "--type")
            .choices("SHA-256", "SHA-512", "SHA1").setDefault("SHA-256")
            .help("Spécifier la fonction de hachage à utiliser");
        parser.addArgument("file").nargs("*")
            .help("Fichier pour calculer la somme de contrôle");

        // Étape 4 : Analyser les arguments
        Namespace ns = null;
        try {
            ns = parser.parseArgs(args);
        } catch (ArgumentParserException e) {
            parser.handleError(e);
            System.exit(1);
        }

        // Étape 5 : Accéder aux valeurs analysées
        String hashType = ns.getString("type");
        List<String> files = ns.getList("file");

        // Exemple de sortie
        System.out.println("Type de hachage : " + hashType);
        System.out.println("Fichiers : " + files);
    }
}
```

---

### Fonctionnalités Supplémentaires
- **Aide Automatique** : Exécutez votre programme avec `-h` ou `--help` pour voir un message d'aide généré.
- **Sous-commandes** : Utilisez `parser.addSubparsers()` pour des commandes complexes (par exemple, `git commit`, `git push`).
- **Annotations** : Liez les arguments aux champs de classe en utilisant des annotations (voir le manuel utilisateur pour plus de détails).

Pour une utilisation plus avancée, consultez le [Argparse4j User Manual](https://argparse4j.github.io/userguide.html).

---

Ce flux de travail vous permet de parser et de gérer facilement les arguments de ligne de commande dans votre application Java en utilisant `net.sourceforge.argparse4j`.