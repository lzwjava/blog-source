---
audio: false
generated: true
lang: fr
layout: post
title: Saisie de la console en Java
translated: true
type: note
---

Pour utiliser le package `org.jline.reader` en Java, qui fait partie de la bibliothèque JLine pour gérer la saisie en console avec des fonctionnalités avancées comme l'édition de ligne, l'historique et la complétion, suivez ces étapes. Ce guide fournit une approche complète et pratique pour bien démarrer.

### Prérequis
Assurez-vous d'avoir ajouté la bibliothèque JLine à votre projet. Si vous utilisez Maven, incluez la dépendance suivante dans votre fichier `pom.xml` :

```xml
<dependency>
    <groupId>org.jline</groupId>
    <artifactId>jline</artifactId>
    <version>3.21.0</version> <!-- Utilisez la dernière version -->
</dependency>
```

### Étapes de base pour utiliser `org.jline.reader`

1. **Créer une instance de Terminal**
   - Utilisez la classe `TerminalBuilder` de `org.jline.terminal` pour créer un objet `Terminal`. Celui-ci représente l'environnement de console où la saisie sera lue.
   - Exemple :
     ```java
     import org.jline.terminal.Terminal;
     import org.jline.terminal.TerminalBuilder;

     Terminal terminal = TerminalBuilder.builder().build();
     ```
   - La méthode `build()` crée un terminal par défaut adapté à la plupart des environnements. Vous pouvez le personnaliser davantage (par exemple, en définissant le type de terminal), mais la valeur par défaut est souvent suffisante.

2. **Créer une instance de LineReader**
   - Utilisez la classe `LineReaderBuilder` de `org.jline.reader` pour créer un objet `LineReader`, en lui passant l'instance `Terminal`.
   - Le `LineReader` est l'interface principale pour lire la saisie utilisateur avec les fonctionnalités de JLine.
   - Exemple :
     ```java
     import org.jline.reader.LineReader;
     import org.jline.reader.LineReaderBuilder;

     LineReader reader = LineReaderBuilder.builder()
         .terminal(terminal)
         .build();
     ```

3. **Lire la saisie de l'utilisateur**
   - Utilisez la méthode `readLine()` de `LineReader` pour lire une ligne de texte saisie par l'utilisateur. Vous pouvez éventuellement spécifier un prompt à afficher.
   - Exemple :
     ```java
     String line = reader.readLine("> ");
     ```
   - Cela affiche `> ` comme prompt, attend la saisie de l'utilisateur et renvoie la chaîne saisie lorsque l'utilisateur appuie sur Entrée.

### Exemple simple
Voici un exemple complet et minimal qui lit la saisie utilisateur dans une boucle jusqu'à ce que l'utilisateur tape "exit" :

```java
import org.jline.reader.LineReader;
import org.jline.reader.LineReaderBuilder;
import org.jline.terminal.Terminal;
import org.jline.terminal.TerminalBuilder;

public class ConsoleExample {
    public static void main(String[] args) throws Exception {
        // Créer le Terminal
        Terminal terminal = TerminalBuilder.builder().build();
        
        // Créer le LineReader
        LineReader reader = LineReaderBuilder.builder()
            .terminal(terminal)
            .build();
        
        // Lire la saisie dans une boucle
        String line;
        while ((line = reader.readLine("> ")) != null) {
            System.out.println("Vous avez saisi : " + line);
            if (line.equals("exit")) {
                break;
            }
        }
    }
}
```

- **Sortie** : Lorsque vous exécutez ceci, il affiche un prompt `> `. Vous pouvez taper du texte, utiliser la touche Retour arrière ou les flèches pour l'édition (fonctionnalités non disponibles facilement avec `System.in`), et appuyer sur Entrée. Taper "exit" met fin au programme.

### Fonctionnalités optionnelles
Vous pouvez améliorer le `LineReader` avec des fonctionnalités supplémentaires :

#### 1. **Activer l'historique des commandes**
   - Ajoutez un objet `History` pour stocker et rappeler les saisies précédentes (par exemple, en utilisant les touches fléchées haut/bas).
   - Exemple :
     ```java
     import org.jline.reader.impl.history.DefaultHistory;
     import org.jline.reader.History;

     History history = new DefaultHistory();
     LineReader reader = LineReaderBuilder.builder()
         .terminal(terminal)
         .history(history)
         .build();
     ```
   - Maintenant, l'utilisateur peut naviguer dans son historique de saisie.

#### 2. **Ajouter la complétion automatique**
   - Implémentez un `Completer` pour suggérer des complétions lorsque l'utilisateur appuie sur Tab.
   - Exemple avec un compléteur de chaînes simple :
     ```java
     import org.jline.reader.Completer;
     import org.jline.reader.impl.completer.StringsCompleter;

     Completer completer = new StringsCompleter("foo", "bar", "baz");
     LineReader reader = LineReaderBuilder.builder()
         .terminal(terminal)
         .completer(completer)
         .build();
     ```
   - Taper "f" et appuyer sur Tab suggère "foo".

#### 3. **Lire les mots de passe (saisie masquée)**
   - Utilisez `readLine()` avec un caractère de masquage pour cacher la saisie (par exemple, pour les mots de passe).
   - Exemple :
     ```java
     String password = reader.readLine("Entrez le mot de passe : ", '*');
     ```
   - Affiche des astérisques (`*`) au lieu des caractères tapés.

### Gestion des ressources
Pour des applications robustes, fermez le `Terminal` une fois terminé pour libérer les ressources. Comme `Terminal` implémente `Closeable`, utilisez un bloc try-with-resources :

```java
try (Terminal terminal = TerminalBuilder.builder().build()) {
    LineReader reader = LineReaderBuilder.builder()
        .terminal(terminal)
        .build();
    String line = reader.readLine("> ");
    System.out.println("Vous avez saisi : " + line);
}
```

### Pourquoi utiliser `org.jline.reader` ?
Contrairement à la saisie basique avec `System.in` et `BufferedReader`, `org.jline.reader` fournit :
- **Édition de ligne** : Retour arrière, déplacement du curseur, etc.
- **Historique** : Rappel des saisies précédentes.
- **Complétion** : Suggestions automatiques d'options.
- **Gestion de terminal multiplateforme** : Fonctionne de manière cohérente dans différents environnements.

### Notes
- Si vous ne spécifiez pas de `Terminal` dans `LineReaderBuilder`, il en crée un par défaut en interne, donc `LineReader reader = LineReaderBuilder.builder().build();` fonctionne pour les cas simples.
- Évitez d'appeler `readLine()` depuis plusieurs threads simultanément, car `LineReader` n'est pas thread-safe pour des lectures concurrentes.
- Pour les cas d'utilisation avancés (par exemple, saisie multi-lignes, raccourcis clavier personnalisés), explorez les fonctionnalités supplémentaires de JLine comme les parsers ou les key maps.

Ceci couvre l'essentiel de l'utilisation de `org.jline.reader` pour lire efficacement la saisie en console en Java. Commencez par la configuration de base et ajoutez des fonctionnalités comme l'historique ou la complétion selon les besoins de votre application !