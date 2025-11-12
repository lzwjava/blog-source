---
audio: false
generated: true
lang: es
layout: post
title: Acceso al contexto de aplicación de Spring
translated: true
type: note
---

Para utilizar la interfaz `ApplicationContextAware` de Spring para acceder al `ApplicationContext` en un objeto Java plano, como un consumidor de Kafka, necesitas una forma de conectar los beans gestionados por Spring con tu objeto plano. Aquí te mostramos cómo puedes hacerlo:

### Enfoque General
La interfaz `ApplicationContextAware` permite que un bean gestionado por Spring reciba el `ApplicationContext` automáticamente desde Spring. Puedes usar esto para poner el contexto a disposición de un objeto Java plano que no esté gestionado por Spring (es decir, que no sea un bean creado por el contenedor de Spring).

#### Pasos para Acceder al ApplicationContext
1. **Crear una Clase Auxiliar Gestionada por Spring**:
   Define una clase que implemente `ApplicationContextAware` y esté gestionada por Spring (por ejemplo, anotada con `@Component`). Esta clase recibirá el `ApplicationContext` cuando la aplicación Spring se inicie.

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

   - `@Component` asegura que Spring gestione este bean.
   - `setApplicationContext` es llamado por Spring para inyectar el `ApplicationContext`.
   - Una variable estática `context` y su getter permiten el acceso desde cualquier lugar.

2. **Acceder al Contexto en tu Objeto Java Plano**:
   En tu objeto Java plano (por ejemplo, un consumidor de Kafka creado manualmente), recupera el `ApplicationContext` usando la clase auxiliar y úsalo para obtener beans gestionados por Spring.

   ```java
   public class MyKafkaConsumer {
       public void processMessage() {
           ApplicationContext context = ApplicationContextProvider.getApplicationContext();
           SomeService service = context.getBean(SomeService.class);
           // Usar el servicio u otros beans según sea necesario
       }
   }
   ```

   - Esto funciona porque el `ApplicationContextProvider` es inicializado por Spring al arrancar, haciendo que el contexto esté disponible estáticamente.

3. **Alternativa: Pasar el Contexto Explícitamente**:
   Si tu objeto Java plano es creado por un bean gestionado por Spring, puedes inyectar el `ApplicationContext` en ese bean y pasarlo al objeto plano a través de un constructor o un setter.

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
           // Usar el servicio
       }
   }
   ```

   - Esto evita variables estáticas, haciendo la dependencia explícita y mejorando la capacidad de prueba.

### Solución Específica para Consumidores Kafka
Si estás trabajando con un consumidor de Kafka y usando **Spring Kafka**, el enfoque recomendado es integrar el consumidor directamente en el ecosistema Spring en lugar de tratarlo como un objeto Java plano.

#### Usando `@KafkaListener`
Define tu consumidor de Kafka como un bean gestionado por Spring con un método `@KafkaListener`. Esto te permite inyectar el `ApplicationContext` u otros beans directamente.

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
        // Usar context o someService directamente
        SomeService service = context.getBean(SomeService.class); // Si es necesario
        someService.process(message);
    }
}
```

- Spring Kafka gestiona el ciclo de vida del consumidor, incluyendo el threading y el polling.
- La inyección de dependencias elimina la necesidad de obtener el contexto manualmente en la mayoría de los casos.

#### Consumidor Kafka Manual
Si debes crear un `KafkaConsumer` manualmente (por ejemplo, usando la librería cliente de Kafka directamente), hazlo dentro de un bean gestionado por Spring y pasa el `ApplicationContext` a él, como se mostró en el enfoque de paso explícito anterior.

### Recomendaciones
- **Para Consumidores Kafka**: Usa `@KafkaListener` de Spring Kafka en un bean gestionado por Spring siempre que sea posible. Esto aprovecha la integración de Spring con Kafka y simplifica el acceso al `ApplicationContext` y a otros beans.
- **Para Objetos Java Planos en General**: Usa el enfoque estático con `ApplicationContextProvider` o pasa el `ApplicationContext` explícitamente desde un bean gestionado por Spring. Se prefiere el método de paso explícito cuando es factible, ya que evita el estado estático y mejora la capacidad de prueba.

Siguiendo estos métodos, puedes usar efectivamente `ApplicationContextAware` para poner el contexto de Spring a disposición de tu objeto Java plano, incluyendo un consumidor de Kafka, dependiendo de tu configuración específica.