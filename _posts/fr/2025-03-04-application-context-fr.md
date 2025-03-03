---
audio: false
generated: true
lang: fr
layout: post
title: Accéder au ApplicationContext de Spring
translated: true
---

Pour utiliser l'interface `ApplicationContextAware` de Spring afin d'accéder au `ApplicationContext` dans un objet Java simple, tel qu'un consommateur Kafka, vous avez besoin d'un moyen de relier les beans gérés par Spring avec votre objet simple. Voici comment vous pouvez le faire :

### Approche Générale
L'interface `ApplicationContextAware` permet à un bean géré par Spring de recevoir automatiquement le `ApplicationContext` de Spring. Vous pouvez utiliser cela pour rendre le contexte disponible à un objet Java simple qui n'est pas géré par Spring (c'est-à-dire, pas un bean créé par le conteneur Spring).

#### Étapes pour Accéder au ApplicationContext
1. **Créer une Classe Helper Gérée par Spring** :
   Définissez une classe qui implémente `ApplicationContextAware` et est gérée par Spring (par exemple, annotée avec `@Component`). Cette classe recevra le `ApplicationContext` lorsque l'application Spring démarre.

   ```java
   import org.springframework.context.ApplicationContext;
   import org.springframework.context.ApplicationContextAware;
   import org.springframework.stereotype.Component;

   @Component
   public class ApplicationContextProvider implements ApplicationContextAware {
       private static ApplicationContext context;

       @Override
       public void setApplicationContext(ApplicationContext applicationContext) {
           context = applicationContext;
       }

       public static ApplicationContext getApplicationContext() {
           return context;
       }
   }
   ```

   - `@Component` assure que Spring gère ce bean.
   - `setApplicationContext` est appelé par Spring pour injecter le `ApplicationContext`.
   - Une variable `context` statique et un getter permettent l'accès depuis n'importe où.

2. **Accéder au Contexte dans Votre Objet Java Simple** :
   Dans votre objet Java simple (par exemple, un consommateur Kafka créé manuellement), récupérez le `ApplicationContext` en utilisant la classe helper et utilisez-le pour obtenir des beans gérés par Spring.

   ```java
   public class MyKafkaConsumer {
       public void processMessage() {
           ApplicationContext context = ApplicationContextProvider.getApplicationContext();
           SomeService service = context.getBean(SomeService.class);
           // Utilisez le service ou d'autres beans selon les besoins
       }
   }
   ```

   - Cela fonctionne parce que le `ApplicationContextProvider` est initialisé par Spring au démarrage, rendant le contexte disponible de manière statique.

3. **Alternative : Passer le Contexte Explicitement** :
   Si votre objet Java simple est créé par un bean géré par Spring, vous pouvez autowirer le `ApplicationContext` dans ce bean et le passer à l'objet simple via un constructeur ou un setter.

   ```java
   import org.springframework.beans.factory.annotation.Autowired;
   import org.springframework.context.ApplicationContext;
   import org.springframework.stereotype.Component;

   @Component
   public class KafkaConsumerCreator {
       @Autowired
       private ApplicationContext context;

       public MyKafkaConsumer createConsumer() {
           return new MyKafkaConsumer(context);
       }
   }

   public class MyKafkaConsumer {
       private final ApplicationContext context;

       public MyKafkaConsumer(ApplicationContext context) {
           this.context = context;
       }

       public void processMessage() {
           SomeService service = context.getBean(SomeService.class);
           // Utilisez le service
       }
   }
   ```

   - Cela évite les variables statiques, rendant la dépendance explicite et améliorant la testabilité.

### Solution Spécifique au Consommateur Kafka
Si vous travaillez avec un consommateur Kafka et utilisez **Spring Kafka**, l'approche recommandée consiste à intégrer le consommateur directement dans l'écosystème Spring plutôt que de le traiter comme un objet Java simple.

#### Utilisation de `@KafkaListener`
Définissez votre consommateur Kafka comme un bean géré par Spring avec une méthode `@KafkaListener`. Cela vous permet d'autowirer le `ApplicationContext` ou d'autres beans directement.

```java
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.ApplicationContext;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Component;

@Component
public class MyKafkaConsumer {
    @Autowired
    private ApplicationContext context;

    @Autowired
    private SomeService someService;

    @KafkaListener(topics = "my-topic")
    public void consume(String message) {
        // Utilisez context ou someService directement
        SomeService service = context.getBean(SomeService.class); // Si nécessaire
        someService.process(message);
    }
}
```

- Spring Kafka gère le cycle de vie du consommateur, y compris le threading et le polling.
- L'autowiring élimine le besoin de récupérer manuellement le contexte dans la plupart des cas.

#### Consommateur Kafka Manuel
Si vous devez créer un `KafkaConsumer` manuellement (par exemple, en utilisant directement la bibliothèque client Kafka), faites-le au sein d'un bean géré par Spring et passez le `ApplicationContext` à celui-ci, comme montré dans l'approche de passage explicite ci-dessus.

### Recommandations
- **Pour les Consommateurs Kafka** : Utilisez l'annotation `@KafkaListener` de Spring Kafka dans un bean géré par Spring chaque fois que cela est possible. Cela tire parti de l'intégration de Spring avec Kafka et simplifie l'accès au `ApplicationContext` et à d'autres beans.
- **Pour les Objets Java Simples Généraux** : Utilisez soit l'approche `ApplicationContextProvider` statique, soit passez le `ApplicationContext` explicitement à partir d'un bean géré par Spring. La méthode de passage explicite est préférée lorsqu'elle est faisable, car elle évite l'état statique et améliore la testabilité.

En suivant ces méthodes, vous pouvez utiliser efficacement `ApplicationContextAware` pour rendre le contexte Spring disponible à votre objet Java simple, y compris un consommateur Kafka, en fonction de votre configuration spécifique.