---
audio: false
generated: true
lang: fr
layout: post
title: Utiliser les matchers Hamcrest dans les tests Java
translated: true
type: note
---

Je vais vous guider dans l'utilisation des matchers Hamcrest en Java. Hamcrest est un framework qui fournit un ensemble d'objets matcher pour écrire des assertions plus lisibles dans les tests.

1. D'abord, ajoutez la dépendance Hamcrest à votre projet :

Pour Maven, ajoutez ceci dans votre pom.xml :
```xml
<dependency>
    <groupId>org.hamcrest</groupId>
    <artifactId>hamcrest</artifactId>
    <version>2.2</version>
    <scope>test</scope>
</dependency>
```

Pour Gradle, ajoutez ceci dans votre build.gradle :
```groovy
testImplementation 'org.hamcrest:hamcrest:2.2'
```

2. Voici un exemple basique d'utilisation de Hamcrest avec JUnit :

```java
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.*;  // Importer les matchers communs

import org.junit.Test;

public class ExampleTest {
    @Test
    public void testExamples() {
        // Égalité basique
        assertThat(5, is(5));
        
        // Correspondance de chaînes
        String text = "Hello World";
        assertThat(text, containsString("World"));
        assertThat(text, startsWith("Hello"));
        
        // Correspondance de collections
        List<String> items = Arrays.asList("apple", "banana", "orange");
        assertThat(items, hasItem("banana"));
        assertThat(items, hasSize(3));
        
        // Comparaisons numériques
        assertThat(10, greaterThan(5));
        assertThat(3.14, closeTo(3.0, 0.2));
    }
}
```

3. Matchers Hamcrest courants :
- `is()` : Teste l'égalité
- `equalTo()` : Teste l'égalité d'objets
- `containsString()` : Vérifie si une chaîne contient une sous-chaîne
- `startsWith()`/ `endsWith()` : Vérification du préfixe/suffixe de chaîne
- `greaterThan()`/ `lessThan()` : Comparaisons numériques
- `hasItem()` : Vérifie si une collection contient un élément
- `hasSize()` : Vérifie la taille d'une collection
- `closeTo()` : Vérifie si un nombre est dans une plage
- `not()` : Inverse n'importe quel matcher
- `allOf()` : Combine plusieurs matchers (ET)
- `anyOf()` : Combine plusieurs matchers (OU)

4. Exemple de matcher personnalisé :
```java
import org.hamcrest.BaseMatcher;
import org.hamcrest.Description;
import org.hamcrest.Matcher;

public class CustomMatchers {
    public static Matcher<String> isPalindrome() {
        return new BaseMatcher<String>() {
            @Override
            public boolean matches(Object item) {
                String str = (String) item;
                String reversed = new StringBuilder(str).reverse().toString();
                return str.equals(reversed);
            }

            @Override
            public void describeTo(Description description) {
                description.appendText("un palindrome");
            }
        };
    }
}

// Utilisation :
@Test
public void testPalindrome() {
    assertThat("racecar", isPalindrome());
}
```

5. Combinaison de matchers :
```java
@Test
public void testCombined() {
    List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);
    assertThat(numbers, allOf(
        hasSize(5),
        hasItem(greaterThan(4)),
        everyItem(lessThan(10))
    ));
}
```

Principaux avantages :
- Assertions de test plus lisibles
- Meilleurs messages d'échec
- Conditions de correspondance flexibles
- Extensible avec des matchers personnalisés

Conseils :
- Utilisez `import static` pour rendre le code plus concis
- Combinez les matchers pour des conditions complexes
- Consultez la documentation Hamcrest pour l'ensemble complet des matchers
- Hamcrest fonctionne bien avec JUnit, TestNG et d'autres frameworks de test

Souhaitez-vous que je développe un matcher spécifique ou que je montre plus d'exemples ?