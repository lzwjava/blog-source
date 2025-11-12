---
audio: false
generated: true
lang: fr
layout: post
title: Accéder au contexte d'application de Spring
translated: true
type: note
---

Pour utiliser l'interface `ApplicationContextAware` de Spring afin d'accéder au `ApplicationContext` dans un objet Java simple, tel qu'un consommateur Kafka, vous avez besoin d'un moyen de faire le lien entre les beans gérés par Spring et votre objet simple. Voici comment procéder :

### Approche générale
L'interface `ApplicationContextAware` permet à un bean géré par Spring de recevoir automatiquement le `ApplicationContext` de Spring. Vous pouvez l'utiliser pour rendre le contexte disponible à un objet Java simple qui n'est pas géré par Spring (c'est-à-dire, qui n'est pas un bean créé par le conteneur Spring).

#### Étapes pour accéder au ApplicationContext
1. **Créer une classe Helper gérée par Spring** :
   Définissez une classe qui implémente `ApplicationContextAware` et qui est gérée par Spring (par exemple, annotée avec `@Component`). Cette classe recevra le `ApplicationContext` au démarrage de l'application Spring.

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

   - `@Component` garantit que Spring gère ce bean.
   - `setApplicationContext` est appelée par Spring pour injecter le `ApplicationContext`.
   - Une variable statique `context` et un getter permettent d'y accéder de n'importe où.

2. **Accéder au contexte dans votre objet Java simple** :
   Dans votre objet Java simple (par exemple, un consommateur Kafka créé manuellement), récupérez le `ApplicationContext` en utilisant la classe helper et utilisez-le pour obtenir des beans gérés par Spring.

   ```java
   public class MyKafkaConsumer {
       public void processMessage() {
           ApplicationContext context = ApplicationContextProvider.getApplicationContext();
           SomeService service = context.getBean(SomeService.class);
           // Utiliser le service ou d'autres beans selon les besoins
       }
   }
   ```

   - Cela fonctionne car le `ApplicationContextProvider` est initialisé par Spring au démarrage, rendant le contexte disponible statiquement.

3. **Alternative : Passer le contexte explicitement** :
   Si votre objet Java simple est créé par un bean géré par Spring, vous pouvez injecter le `ApplicationContext` dans ce bean et le passer à l'objet simple via un constructeur ou un setter.

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
           // Utiliser le service
       }
   }
   ```

   - Cela évite les variables statiques, rend la dépendance explicite et améliore la testabilité.

### Solution spécifique au consommateur Kafka
Si vous travaillez avec un consommateur Kafka et utilisez **Spring Kafka**, l'approche recommandée est d'intégrer directement le consommateur dans l'écosystème Spring plutôt que de le traiter comme un objet Java simple.

#### Utilisation de `@KafkaListener`
Définissez votre consommateur Kafka comme un bean géré par Spring avec une méthode annotée `@KafkaListener`. Cela vous permet d'injecter directement le `ApplicationContext` ou d'autres beans.

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
        // Utiliser context ou someService directement
        SomeService service = context.getBean(SomeService.class); // Si nécessaire
        someService.process(message);
    }
}
```

- Spring Kafka gère le cycle de vie du consommateur, y compris le threading et le polling.
- L'injection de dépendances élimine le besoin de récupérer manuellement le contexte dans la plupart des cas.

#### Consommateur Kafka manuel
Si vous devez créer un `KafkaConsumer` manuellement (par exemple, en utilisant directement la bibliothèque cliente Kafka), faites-le au sein d'un bean géré par Spring et passez-lui le `ApplicationContext`, comme montré dans l'approche de passage explicite ci-dessus.

### Recommandations
- **Pour les consommateurs Kafka** : Utilisez `@KafkaListener` de Spring Kafka dans un bean géré par Spring autant que possible. Cela tire parti de l'intégration de Spring avec Kafka et simplifie l'accès au `ApplicationContext` et aux autres beans.
- **Pour les objets Java simples généraux** : Utilisez soit l'approche statique avec `ApplicationContextProvider`, soit passez le `ApplicationContext` explicitement depuis un bean géré par Spring. La méthode de passage explicite est préférée lorsque cela est possible, car elle évite l'état statique et améliore la testabilité.

En suivant ces méthodes, vous pouvez utiliser efficacement `ApplicationContextAware` pour rendre le contexte Spring disponible à votre objet Java simple, y compris un consommateur Kafka, en fonction de votre configuration spécifique.