---
audio: false
generated: true
lang: de
layout: post
title: Springs ApplicationContext zugreifen
translated: true
---

Um die `ApplicationContextAware`-Schnittstelle von Spring zu verwenden, um auf den `ApplicationContext` in einem einfachen Java-Objekt, wie z.B. einem Kafka-Consumer, zuzugreifen, benötigen Sie eine Möglichkeit, die von Spring verwalteten Beans mit Ihrem einfachen Objekt zu verbinden. Hier ist, wie Sie dies tun können:

### Allgemeiner Ansatz
Die `ApplicationContextAware`-Schnittstelle ermöglicht es einem von Spring verwalteten Bean, den `ApplicationContext` automatisch von Spring zu erhalten. Sie können dies verwenden, um den Kontext für ein einfaches Java-Objekt verfügbar zu machen, das nicht von Spring verwaltet wird (d.h. kein von dem Spring-Container erstelltes Bean).

#### Schritte zum Zugriff auf den ApplicationContext
1. **Erstellen Sie eine von Spring verwaltete Hilfsklasse**:
   Definieren Sie eine Klasse, die `ApplicationContextAware` implementiert und von Spring verwaltet wird (z.B. mit `@Component` annotiert). Diese Klasse erhält den `ApplicationContext`, wenn die Spring-Anwendung startet.

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

   - `@Component` stellt sicher, dass Spring dieses Bean verwaltet.
   - `setApplicationContext` wird von Spring aufgerufen, um den `ApplicationContext` zu injizieren.
   - Eine statische `context`-Variable und ein Getter ermöglichen den Zugriff von überall.

2. **Zugreifen auf den Kontext in Ihrem einfachen Java-Objekt**:
   In Ihrem einfachen Java-Objekt (z.B. einem manuell erstellten Kafka-Consumer) rufen Sie den `ApplicationContext` mit der Hilfsklasse ab und verwenden ihn, um Spring-verwaltete Beans zu erhalten.

   ```java
   public class MyKafkaConsumer {
       public void processMessage() {
           ApplicationContext context = ApplicationContextProvider.getApplicationContext();
           SomeService service = context.getBean(SomeService.class);
           // Verwenden Sie den Dienst oder andere Beans nach Bedarf
       }
   }
   ```

   - Dies funktioniert, weil der `ApplicationContextProvider` beim Start von Spring initialisiert wird und den Kontext statisch verfügbar macht.

3. **Alternative: Kontext explizit übergeben**:
   Wenn Ihr einfaches Java-Objekt von einem von Spring verwalteten Bean erstellt wird, können Sie den `ApplicationContext` in dieses Bean autowiren und ihn über einen Konstruktor oder Setter an das einfache Objekt übergeben.

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
           // Verwenden Sie den Dienst
       }
   }
   ```

   - Dies vermeidet statische Variablen, macht die Abhängigkeit explizit und verbessert die Testbarkeit.

### Kafka Consumer-spezifische Lösung
Wenn Sie mit einem Kafka-Consumer arbeiten und **Spring Kafka** verwenden, ist der empfohlene Ansatz, den Consumer direkt in das Spring-Ökosystem zu integrieren, anstatt ihn als einfaches Java-Objekt zu behandeln.

#### Verwendung von `@KafkaListener`
Definieren Sie Ihren Kafka-Consumer als Spring-verwaltetes Bean mit einer `@KafkaListener`-Methode. Dies ermöglicht es Ihnen, den `ApplicationContext` oder andere Beans direkt zu autowiren.

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
        // Verwenden Sie context oder someService direkt
        SomeService service = context.getBean(SomeService.class); // Wenn benötigt
        someService.process(message);
    }
}
```

- Spring Kafka verwaltet den Lebenszyklus des Consumers, einschließlich Threading und Polling.
- Autowiring eliminiert die Notwendigkeit, den Kontext manuell in den meisten Fällen abzurufen.

#### Manueller Kafka Consumer
Wenn Sie einen `KafkaConsumer` manuell erstellen müssen (z.B. unter Verwendung der Kafka-Client-Bibliothek direkt), tun Sie dies innerhalb eines von Spring verwalteten Beans und übergeben Sie den `ApplicationContext` an ihn, wie im expliziten Übergabeansatz oben gezeigt.

### Empfehlungen
- **Für Kafka-Consumer**: Verwenden Sie Spring Kafkas `@KafkaListener` in einem Spring-verwalteten Bean, wo immer möglich. Dies nutzt die Integration von Spring mit Kafka und vereinfacht den Zugriff auf den `ApplicationContext` und andere Beans.
- **Für allgemeine einfache Java-Objekte**: Verwenden Sie entweder den statischen `ApplicationContextProvider`-Ansatz oder übergeben Sie den `ApplicationContext` explizit von einem Spring-verwalteten Bean. Der explizite Übergabeansatz ist vorzuziehen, wenn dies möglich ist, da er statische Zustände vermeidet und die Testbarkeit verbessert.

Durch die Verwendung dieser Methoden können Sie `ApplicationContextAware` effektiv nutzen, um den Spring-Kontext für Ihr einfaches Java-Objekt, einschließlich eines Kafka-Consumers, verfügbar zu machen, abhängig von Ihrer spezifischen Einrichtung.