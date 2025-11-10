---
audio: false
generated: true
lang: fr
layout: post
title: Générer des chaînes aléatoires avec Apache Commons Lang
translated: true
type: note
---

`RandomStringUtils` est une classe très utile de la bibliothèque Apache Commons Lang qui fournit diverses méthodes statiques pour générer des chaînes aléatoires. Cela inclut la génération de chaînes de longueurs spécifiques, contenant uniquement des lettres, uniquement des chiffres, des caractères alphanumériques, ou même à partir d'un ensemble personnalisé de caractères.

Voici comment l'utiliser et la dépendance Maven nécessaire :

## Comment utiliser `org.apache.commons.lang3.RandomStringUtils;`

Tout d'abord, vous devez importer la classe dans votre fichier Java :

```java
import org.apache.commons.lang3.RandomStringUtils;
```

Ensuite, vous pouvez utiliser ses méthodes statiques. Voici quelques exemples courants :

1.  **Générer une chaîne alphanumérique aléatoire d'une longueur spécifique :**

    ```java
    String randomAlphaNumeric = RandomStringUtils.randomAlphanumeric(10);
    System.out.println("Alphanumérique aléatoire : " + randomAlphaNumeric); // ex. : "aB5cY2x9Pq"
    ```

2.  **Générer une chaîne alphabétique aléatoire d'une longueur spécifique :**

    ```java
    String randomAlphabetic = RandomStringUtils.randomAlphabetic(8);
    System.out.println("Alphabétique aléatoire : " + randomAlphabetic); // ex. : "GhJkLmNo"
    ```

3.  **Générer une chaîne numérique aléatoire d'une longueur spécifique :**

    ```java
    String randomNumeric = RandomStringUtils.randomNumeric(6);
    System.out.println("Numérique aléatoire : " + randomNumeric); // ex. : "123456"
    ```

4.  **Générer une chaîne aléatoire avec un mélange de lettres et de chiffres, en spécifiant des drapeaux :**

    ```java
    String randomLettersAndNumbers = RandomStringUtils.random(12, true, true);
    System.out.println("Lettres et chiffres aléatoires : " + randomLettersAndNumbers); // ex. : "abC123DeF456"
    ```

5.  **Générer une chaîne aléatoire à partir d'un ensemble personnalisé de caractères :**

    ```java
    String chars = "abcdefg";
    String randomFromCustomSet = RandomStringUtils.random(5, chars);
    System.out.println("Aléatoire depuis un ensemble personnalisé : " + randomFromCustomSet); // ex. : "gcfae"
    ```

## Quelle bibliothèque utiliser dans `pom.xml`

Pour utiliser `RandomStringUtils` dans un projet Maven, vous devez ajouter la dépendance `commons-lang3` à votre fichier `pom.xml`.

Voici l'extrait de dépendance :

```xml
<dependency>
    <groupId>org.apache.commons</groupId>
    <artifactId>commons-lang3</artifactId>
    <version>3.14.0</version> </dependency>
```

**Notes importantes :**

  * **Version :** Vérifiez toujours [Maven Central](https://mvnrepository.com/artifact/org.apache.commons/commons-lang3) pour la dernière version stable de `commons-lang3`. Lors de ma dernière mise à jour, `3.14.0` ou une version supérieure est un bon choix, mais il est toujours préférable d'utiliser la dernière version stable absolument disponible.
  * **Portée :** La portée par défaut pour les dépendances est `compile`, ce qui est généralement ce que vous voulez pour les bibliothèques utilitaires comme celle-ci. Cela signifie que le JAR sera disponible pendant la compilation, les tests et l'exécution. Si vous ne l'utilisiez que pour les tests, vous pourriez utiliser `<scope>test</scope>`.
  * **Dépréciation :** Notez que certaines méthodes plus anciennes comme `RandomStringUtils.randomAlphabetic(int count)` sont dépréciées dans les nouvelles versions d'Apache Commons Lang 3. Il est plutôt recommandé d'utiliser les méthodes `secure()`, `secureStrong()` ou `insecure()`, qui offrent plus de contrôle sur la source d'aléa. Par exemple, `RandomStringUtils.secure().nextAlphanumeric(10)`. Cependant, les méthodes plus anciennes fonctionnent toujours pour de nombreux cas d'usage.