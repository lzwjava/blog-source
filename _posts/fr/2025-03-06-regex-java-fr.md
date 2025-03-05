---
audio: false
generated: true
lang: fr
layout: post
title: Expressions Régulières en Java
translated: true
---

# Comment utiliser `java.util.regex` en Java

Le package `java.util.regex` en Java fournit des outils pour travailler avec les expressions régulières (regex), qui sont des motifs utilisés pour correspondre et manipuler du texte. Ce guide vous guidera à travers les bases de l'utilisation de ce package, en se concentrant sur les deux classes principales : `Pattern` et `Matcher`. Je couvrirai également des cas d'utilisation courants avec des exemples pour vous aider à démarrer.

## Vue d'ensemble de `java.util.regex`

Le package `java.util.regex` comprend :

- **`Pattern`** : Représente une expression régulière compilée. Vous la créez à partir d'une chaîne de caractères regex.
- **`Matcher`** : Applique le motif à une chaîne d'entrée spécifique et effectue des opérations de correspondance.

De plus, la classe `String` de Java offre des méthodes basées sur regex pour des tâches plus simples.

## Étapes de base pour utiliser `java.util.regex`

Pour utiliser les expressions régulières en Java, suivez ces étapes :

1. **Compiler un motif** : Convertissez votre chaîne de caractères regex en un objet `Pattern`.
2. **Créer un Matcher** : Utilisez le motif pour créer un `Matcher` pour votre texte d'entrée.
3. **Effectuer des opérations** : Utilisez le matcher pour vérifier les correspondances, trouver des motifs ou manipuler le texte.

Voici comment cela fonctionne en pratique.

## Exemple 1 : Validation d'une adresse e-mail

Créons un validateur d'e-mail simple en utilisant un motif regex de base : `".+@.+\\..+"`. Ce motif correspond aux chaînes avec au moins un caractère avant et après un symbole `@`, suivi d'un point et de plus de caractères (par exemple, `example@test.com`).

```java
import java.util.regex.*;

public class EmailValidator {
    public static boolean isValidEmail(String email) {
        // Définir le motif regex
        String regex = ".+@.+\\..+";
        // Compiler le motif
        Pattern pattern = Pattern.compile(regex);
        // Créer un matcher pour la chaîne d'entrée
        Matcher matcher = pattern.matcher(email);
        // Vérifier si la chaîne entière correspond au motif
        return matcher.matches();
    }

    public static void main(String[] args) {
        String email = "example@test.com";
        if (isValidEmail(email)) {
            System.out.println("Email valide");
        } else {
            System.out.println("Email invalide");
        }
    }
}
```

### Explication
- **`Pattern.compile(regex)`** : Compile la chaîne regex en un objet `Pattern`.
- **`pattern.matcher(email)`** : Crée un `Matcher` pour la chaîne d'entrée `email`.
- **`matcher.matches()`** : Retourne `true` si la chaîne entière correspond au motif, `false` sinon.

**Sortie** : `Email valide`

Note : Il s'agit d'un motif d'e-mail simplifié. La validation d'e-mail réelle nécessite un regex plus complexe (par exemple, selon RFC 5322), mais cela sert de point de départ.

## Exemple 2 : Trouver tous les hashtags dans une chaîne

Supposons que vous souhaitiez extraire tous les hashtags (par exemple, `#java`) d'un tweet. Utilisez le regex `"#\\w+"`, où `#` correspond au symbole hashtag littéral et `\\w+` correspond à un ou plusieurs caractères de mot (lettres, chiffres ou underscores).

```java
import java.util.regex.*;

public class HashtagExtractor {
    public static void main(String[] args) {
        String tweet = "Ceci est un #échantillon tweet avec #multiples hashtags comme #java";
        String regex = "#\\w+";
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(tweet);

        // Trouver toutes les correspondances
        while (matcher.find()) {
            System.out.println(matcher.group());
        }
    }
}
```

### Explication
- **`matcher.find()`** : Déplace vers la correspondance suivante dans la chaîne d'entrée et retourne `true` si une correspondance est trouvée.
- **`matcher.group()`** : Retourne le texte correspondant pour la correspondance actuelle.

**Sortie** :
```
#échantillon
#multiples
#java
```

## Exemple 3 : Remplacer du texte avec regex

Pour remplacer toutes les occurrences d'un mot (par exemple, censurer "badword" avec des astérisques), vous pouvez utiliser la méthode `String.replaceAll()`, qui utilise regex en interne.

```java
public class TextCensor {
    public static void main(String[] args) {
        String text = "Ceci est un exemple badword avec badword répété.";
        String censored = text.replaceAll("badword", "*******");
        System.out.println(censored);
    }
}
```

**Sortie** : `Ceci est un ******* exemple avec ******* répété.`

Pour des remplacements plus complexes, utilisez `Matcher` :

```java
import java.util.regex.*;

public class ComplexReplacement {
    public static void main(String[] args) {
        String text = "Contact : 123-456-7890";
        String regex = "\\d{3}-\\d{3}-\\d{4}"; // Correspond aux numéros de téléphone
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(text);
        String result = matcher.replaceAll("XXX-XXX-XXXX");
        System.out.println(result);
    }
}
```

**Sortie** : `Contact : XXX-XXX-XXXX`

## Exemple 4 : Utiliser des groupes pour analyser des données structurées

Les groupes regex, définis avec des parenthèses `()`, vous permettent de capturer des parties d'une correspondance. Par exemple, pour analyser un numéro de sécurité sociale (SSN) comme `123-45-6789` :

```java
import java.util.regex.*;

public class SSNParser {
    public static void main(String[] args) {
        String ssn = "123-45-6789";
        String regex = "(\\d{3})-(\\d{2})-(\\d{4})"; // Groupes pour zone, groupe, série
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(ssn);

        if (matcher.matches()) {
            System.out.println("Numéro de zone : " + matcher.group(1));
            System.out.println("Numéro de groupe : " + matcher.group(2));
            System.out.println("Numéro de série : " + matcher.group(3));
        }
    }
}
```

### Explication
- **`"(\\d{3})-(\\d{2})-(\\d{4})"`** : Définit trois groupes :
  - Groupe 1 : `\\d{3}` (trois chiffres)
  - Groupe 2 : `\\d{2}` (deux chiffres)
  - Groupe 3 : `\\d{4}` (quatre chiffres)
- **`matcher.group(n)`** : Récupère le texte correspondant au groupe `n` (indice basé sur 1).

**Sortie** :
```
Numéro de zone : 123
Numéro de groupe : 45
Numéro de série : 6789
```

Vous pouvez également utiliser des **groupes nommés** pour plus de clarté :

```java
String regex = "(?<zone>\\d{3})-(?<groupe>\\d{2})-(?<série>\\d{4})";
Pattern pattern = Pattern.compile(regex);
Matcher matcher = pattern.matcher("123-45-6789");
if (matcher.matches()) {
    System.out.println("Zone : " + matcher.group("zone"));
    System.out.println("Groupe : " + matcher.group("groupe"));
    System.out.println("Série : " + matcher.group("série"));
}
```

## Fonctionnalités supplémentaires et conseils

### Drapeaux

Modifiez le comportement du motif avec des drapeaux dans `Pattern.compile()` :
- **`Pattern.CASE_INSENSITIVE`** : Ignore la casse lors de la correspondance.
  ```java
  Pattern pattern = Pattern.compile("hello", Pattern.CASE_INSENSITIVE);
  Matcher matcher = pattern.matcher("HELLO");
  System.out.println(matcher.matches()); // true
  ```

### Méthodes de chaîne

Pour des tâches simples, utilisez les méthodes `String` :
- **`matches()`** : Vérifie si la chaîne entière correspond à un regex.
  ```java
  String text = "chat";
  System.out.println(text.matches("\\w{3}")); // true
  ```
- **`split()`** : Divise une chaîne par un motif regex.
  ```java
  String data = "pomme, banane, cerise";
  String[] fruits = data.split("\\s*,\\s*");
  // Sortie : pomme, banane, cerise
  ```

### Échappement des caractères spéciaux

Regex utilise des caractères spéciaux comme `.`, `*`, et `?`. Pour les correspondre littéralement, échappez-les avec `\\` :
- Correspondre à une période : `"\\."`
- Dans les chaînes Java, échappez les barres obliques inverses : `"\\d"` pour les chiffres, `"\\\\"` pour une barre oblique inverse littérale.

### Performance

La compilation d'un motif est coûteuse. Réutilisez les objets `Pattern` lorsque cela est possible :
```java
Pattern pattern = Pattern.compile("\\d+"); // Compiler une fois
for (String input : new String[]{"123", "456"}) {
    Matcher matcher = pattern.matcher(input);
    if (matcher.matches()) {
        System.out.println("Nombre : " + input);
    }
}
```

### Gestion des erreurs

Les motifs regex invalides lancent une `PatternSyntaxException`. Gérez-la dans le code de production :
```java
try {
    Pattern pattern = Pattern.compile("["); // Motif regex invalide
} catch (PatternSyntaxException e) {
    System.err.println("Motif regex invalide : " + e.getMessage());
}
```

## Résumé

- **Compiler un motif** : `Pattern.compile(regex)`
- **Créer un Matcher** : `pattern.matcher(input)`
- **Opérations clés** :
  - `matches()` : Correspondance de la chaîne complète
  - `find()` : Trouver la correspondance suivante
  - `group()` : Extraire le texte correspondant
  - `replaceAll()` : Remplacer les correspondances
- **Pratique** : Utilisez les méthodes `String` pour des tâches simples.
- **Bonnes pratiques** : Échappez les caractères spéciaux, réutilisez les motifs et gérez les exceptions.

Cela couvre les bases de `java.util.regex`. Pour des sujets avancés comme les anticipations ou les classes de caractères, consultez la [documentation Java](https://docs.oracle.com/en/java/javase/17/docs/api/java.util.regex/package-summary.html) ou expérimentez avec des cas d'utilisation spécifiques !