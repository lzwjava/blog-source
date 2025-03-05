---
audio: false
generated: true
lang: fr
layout: post
title: Lecture de l'entrée console en Java
translated: true
---

Pour utiliser le package `org.jline.reader` en Java, qui fait partie de la bibliothèque JLine pour gérer les entrées de console avec des fonctionnalités avancées comme l'édition de lignes, l'historique et l'auto-complétion, suivez ces étapes. Ce guide fournit une approche complète et pratique pour vous aider à démarrer.

### Prérequis
Assurez-vous d'avoir ajouté la bibliothèque JLine à votre projet. Si vous utilisez Maven, incluez la dépendance suivante dans votre `pom.xml` :

```xml
<dependency>
    <groupId>org.jline</groupId>
    <artifactId>jline</artifactId>
    <version>3.21.0</version> <!-- Utilisez la dernière version -->
</dependency>
```

### Étapes de base pour utiliser `org.jline.reader`

1. **Créer une instance de Terminal**
   - Utilisez la classe `TerminalBuilder` de `org.jline.terminal` pour créer un objet `Terminal`. Cela représente l'environnement de console où l'entrée sera lue.
   - Exemple :
     ```java
     import org.jline.terminal.Terminal;
     import org.jline.terminal.TerminalBuilder;

     Terminal terminal = TerminalBuilder.builder().build();
     ```
   - La méthode `build()` crée un terminal par défaut adapté à la plupart des environnements. Vous pouvez le personnaliser davantage (par exemple, en définissant le type de terminal), mais le par défaut est souvent suffisant.

2. **Créer une instance de LineReader**
   - Utilisez la classe `LineReaderBuilder` de `org.jline.reader` pour créer un objet `LineReader`, en passant l'instance `Terminal` à celui-ci.
   - Le `LineReader` est l'interface principale pour lire les entrées utilisateur avec les fonctionnalités de JLine.
   - Exemple :
     ```java
     import org.jline.reader.LineReader;
     import org.jline.reader.LineReaderBuilder;

     LineReader reader = LineReaderBuilder.builder()
         .terminal(terminal)
         .build();
     ```

3. **Lire l'entrée de l'utilisateur**
   - Utilisez la méthode `readLine()` de `LineReader` pour lire une ligne de texte saisie par l'utilisateur. Vous pouvez éventuellement spécifier un invite à afficher.
   - Exemple :
     ```java
     String line = reader.readLine("> ");
     ```
   - Cela affiche `> ` comme invite, attend l'entrée de l'utilisateur et retourne la chaîne saisie lorsque l'utilisateur appuie sur Entrée.

### Exemple simple
Voici un exemple complet et minimal qui lit l'entrée de l'utilisateur dans une boucle jusqu'à ce que l'utilisateur tape "exit" :

```java
import org.jline.reader.LineReader;
import org.jline.reader.LineReaderBuilder;
import org.jline.terminal.Terminal;
import org.jline.terminal.TerminalBuilder;

public class ConsoleExample {
    public static void main(String[] args) throws Exception {
        // Créer Terminal
        Terminal terminal = TerminalBuilder.builder().build();

        // Créer LineReader
        LineReader reader = LineReaderBuilder.builder()
            .terminal(terminal)
            .build();

        // Lire l'entrée dans une boucle
        String line;
        while ((line = reader.readLine("> ")) != null) {
            System.out.println("Vous avez entré : " + line);
            if (line.equals("exit")) {
                break;
            }
        }
    }
}
```

- **Sortie** : Lorsque vous exécutez ceci, il affiche une invite `> `. Vous pouvez taper du texte, utiliser la touche de suppression ou les touches fléchées pour l'édition (fonctionnalités non facilement disponibles avec `System.in`), et appuyer sur Entrée. Taper "exit" termine le programme.

### Fonctionnalités optionnelles
Vous pouvez améliorer le `LineReader` avec des fonctionnalités supplémentaires :

#### 1. **Activer l'historique des commandes**
   - Ajoutez un objet `History` pour stocker et rappeler les entrées précédentes (par exemple, en utilisant les touches fléchées haut/bas).
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
   - Maintenant, l'utilisateur peut naviguer dans son historique d'entrées.

#### 2. **Ajouter l'auto-complétion**
   - Implémentez un `Completer` pour suggérer des complétions lorsque l'utilisateur appuie sur Tab.
   - Exemple avec un simple compléteur de chaînes :
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

#### 3. **Lire les mots de passe (entrée masquée)**
   - Utilisez `readLine()` avec un caractère de masque pour masquer l'entrée (par exemple, pour les mots de passe).
   - Exemple :
     ```java
     String password = reader.readLine("Entrez le mot de passe : ", '*');
     ```
   - Affiche des astérisques (`*`) au lieu des caractères tapés.

### Gestion des ressources
Pour des applications robustes, fermez le `Terminal` lorsque vous avez terminé pour libérer les ressources. Comme `Terminal` implémente `Closeable`, utilisez un bloc try-with-resources :

```java
try (Terminal terminal = TerminalBuilder.builder().build()) {
    LineReader reader = LineReaderBuilder.builder()
        .terminal(terminal)
        .build();
    String line = reader.readLine("> ");
    System.out.println("Vous avez entré : " + line);
}
```

### Pourquoi utiliser `org.jline.reader` ?
Contrairement à l'entrée de base avec `System.in` et `BufferedReader`, `org.jline.reader` fournit :
- **Édition de lignes** : Retour arrière, déplacement du curseur, etc.
- **Historique** : Rappel des entrées précédentes.
- **Complétion** : Suggestions automatiques.
- **Gestion des terminaux multiplateformes** : Fonctionne de manière cohérente dans différents environnements.

### Notes
- Si vous ne spécifiez pas de `Terminal` dans `LineReaderBuilder`, il en crée un par défaut en interne, donc `LineReader reader = LineReaderBuilder.builder().build();` fonctionne pour les cas simples.
- Évitez d'appeler `readLine()` à partir de plusieurs threads simultanément, car `LineReader` n'est pas thread-safe pour les lectures concurrentes.
- Pour des cas d'utilisation avancés (par exemple, entrée multi-lignes, liaisons de touches personnalisées), explorez les fonctionnalités supplémentaires de JLine comme les analyseurs ou les cartes de touches.

Cela couvre les bases de l'utilisation de `org.jline.reader` pour lire efficacement les entrées de console en Java. Commencez par la configuration de base et ajoutez des fonctionnalités comme l'historique ou la complétion selon les besoins de votre application !