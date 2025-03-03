---
audio: false
generated: true
lang: fr
layout: post
title: Utilisation de SpringRunner dans les tests Java
translated: true
---

Pour utiliser `SpringRunner` avec le runner `@RunWith` de JUnit dans les tests Java, suivez ces étapes. Notez que je suppose que "SpringRuner" dans votre requête est une faute de frappe et que vous voulez dire `SpringRunner`. Voici un guide complet :

### Étape 1 : Ajouter la dépendance Spring Test
Pour utiliser `SpringRunner`, vous avez besoin du module Spring Test dans votre projet. Si vous utilisez Maven, ajoutez cette dépendance à votre `pom.xml` :

```xml
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-test</artifactId>
    <version>${spring.version}</version>
    <scope>test</scope>
</dependency>
```

Remplacez `${spring.version}` par la version de Spring que vous utilisez (par exemple, `5.3.22`). Si vous utilisez Gradle, ajoutez ceci à votre `build.gradle` :

```gradle
testImplementation 'org.springframework:spring-test:${springVersion}'
```

Cela garantit que `SpringRunner` et autres utilitaires de test Spring sont disponibles.

### Étape 2 : Annoter la classe de test avec `@RunWith(SpringRunner.class)`
L'annotation `@RunWith` indique à JUnit d'utiliser un runner spécifique au lieu de son runner par défaut. Pour l'intégration Spring, utilisez `SpringRunner`, qui fait partie du framework Spring TestContext. Ajoutez cette annotation à votre classe de test :

```java
import org.junit.runner.RunWith;
import org.springframework.test.context.junit4.SpringRunner;

@RunWith(SpringRunner.class)
public class MyServiceTest {
    // Code de test ici
}
```

`SpringRunner` permet d'activer des fonctionnalités Spring comme l'injection de dépendances et le chargement de contexte dans vos tests. Notez que `@RunWith` est une annotation JUnit 4, donc cette approche suppose que vous utilisez JUnit 4. Pour JUnit 5, vous utiliseriez `@ExtendWith(SpringExtension.class)` à la place, mais votre mention du "runner RunWith" suggère JUnit 4.

### Étape 3 : Configurer le contexte d'application Spring avec `@ContextConfiguration`
Pour utiliser des beans gérés par Spring dans vos tests, vous devez charger un contexte d'application Spring. L'annotation `@ContextConfiguration` spécifie comment faire cela. Par exemple, si vous avez une classe de configuration (par exemple, `AppConfig`), utilisez :

```java
import org.springframework.test.context.ContextConfiguration;

@RunWith(SpringRunner.class)
@ContextConfiguration(classes = AppConfig.class)
public class MyServiceTest {
    // Code de test ici
}
```

Si votre configuration est dans un fichier XML (par exemple, `applicationContext.xml`), utilisez :

```java
@ContextConfiguration(locations = "classpath:applicationContext.xml")
```

Cela indique à `SpringRunner` quels beans et configurations charger pour le test.

### Étape 4 : Injecter des beans Spring avec `@Autowired`
Une fois le contexte chargé, vous pouvez injecter des beans gérés par Spring dans votre classe de test en utilisant `@Autowired`. Par exemple, si vous avez un service appelé `MyService` :

```java
import org.springframework.beans.factory.annotation.Autowired;

@RunWith(SpringRunner.class)
@ContextConfiguration(classes = AppConfig.class)
public class MyServiceTest {
    @Autowired
    private MyService myService;

    // Méthodes de test ici
}
```

Cela vous permet d'utiliser le bean injecté dans vos tests.

### Étape 5 : Écrire des méthodes de test avec `@Test`
Définissez vos méthodes de test en utilisant l'annotation `@Test` de JUnit. Par exemple :

```java
import org.junit.Test;
import static org.junit.Assert.assertEquals;

@RunWith(SpringRunner.class)
@ContextConfiguration(classes = AppConfig.class)
public class MyServiceTest {
    @Autowired
    private MyService myService;

    @Test
    public void testMyServiceMethod() {
        String result = myService.doSomething();
        assertEquals("Résultat attendu", result);
    }
}
```

L'annotation `@Test` marque les méthodes que JUnit doit exécuter comme tests. Avec `SpringRunner`, ces méthodes peuvent interagir avec le contexte Spring.

### Exemple : Tout rassembler
Voici un exemple complet :

```java
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringRunner;
import static org.junit.Assert.assertEquals;

// Classe de configuration pour le test
@Configuration
class AppConfig {
    @Bean
    public MyService myService() {
        return new MyService();
    }
}

// Classe de service à tester
class MyService {
    public String doSomething() {
        return "Hello, Spring!";
    }
}

// Classe de test
@RunWith(SpringRunner.class)
@ContextConfiguration(classes = AppConfig.class)
public class MyServiceTest {
    @Autowired
    private MyService myService;

    @Test
    public void testMyServiceMethod() {
        String result = myService.doSomething();
        assertEquals("Hello, Spring!", result);
    }
}
```

### Notes supplémentaires
- **But** : `SpringRunner` est idéal pour les tests d'intégration où vous avez besoin de l'injection de dépendances ou des fonctionnalités de contexte de Spring. Pour les tests unitaires, envisagez d'utiliser Mockito ou JUnit pur.
- **Problèmes courants** : Assurez-vous que la dépendance `spring-test` est incluse, sinon vous obtiendrez des erreurs comme `ClassNotFoundException`. Vérifiez également que `@ContextConfiguration` pointe vers une configuration valide.
- **Annotations optionnelles** : Utilisez `@Transactional` pour les tests qui modifient la base de données (pour annuler les modifications) ou `@ActiveProfiles` pour spécifier un profil (par exemple, "test").

Cette configuration vous permet d'exécuter des tests JUnit avec le support de test Spring, en tirant parti des fonctionnalités comme l'injection de dépendances et la gestion de contexte.