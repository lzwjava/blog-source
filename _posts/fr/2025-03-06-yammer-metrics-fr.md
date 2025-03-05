---
audio: true
generated: true
lang: fr
layout: post
title: Métriques d'Application en Java
translated: true
---

La bibliothèque `com.yammer.metrics`, initialement développée par Yammer, fait désormais partie de la bibliothèque **Dropwizard Metrics**. Elle offre une méthode robuste pour collecter et signaler les métriques d'application en Java, vous aidant à surveiller des aspects de performance tels que le nombre de requêtes, les temps de réponse, et bien plus encore. Voici un guide sur la manière de l'utiliser efficacement.

---

### Étape 1 : Ajouter la Dépendance
Puisque `com.yammer.metrics` a évolué vers Dropwizard Metrics, vous devez utiliser la bibliothèque Dropwizard Metrics. Si vous utilisez Maven, ajoutez la dépendance suivante à votre `pom.xml` :

```xml
<dependency>
    <groupId>io.dropwizard.metrics</groupId>
    <artifactId>metrics-core</artifactId>
    <version>4.2.0</version> <!-- Utilisez la dernière version disponible -->
</dependency>
```

Selon vos besoins, vous pourriez également vouloir des modules supplémentaires, tels que :
- `metrics-jvm` pour les métriques liées à la JVM.
- `metrics-httpclient` pour les métriques des clients HTTP.
- `metrics-jersey` pour l'intégration avec le framework web Jersey.

Consultez la [documentation Dropwizard Metrics](https://metrics.dropwizard.io/) pour la dernière version et les modules disponibles.

---

### Étape 2 : Créer un Registre de Métriques
Le `MetricRegistry` est l'endroit central où toutes les métriques sont stockées. Vous créez généralement une instance pour votre application :

```java
import com.codahale.metrics.MetricRegistry;

public class MyApplication {
    public static void main(String[] args) {
        MetricRegistry registry = new MetricRegistry();
    }
}
```

---

### Étape 3 : Utiliser Différents Types de Métriques
Dropwizard Metrics prend en charge plusieurs types de métriques, chacun adapté à différents besoins de surveillance :

#### **Compteurs**
Les compteurs sont utilisés pour suivre des valeurs qui peuvent augmenter ou diminuer (par exemple, le nombre de requêtes traitées).

```java
import com.codahale.metrics.Counter;

Counter counter = registry.counter("requests.processed");
counter.inc();  // Incrementer de 1
counter.inc(5); // Incrementer de 5
counter.dec();  // Décrémenter de 1
```

#### **Jauges**
Les jauges fournissent un instantané d'une valeur à un moment donné (par exemple, la taille actuelle de la file d'attente). Vous définissez une jauge en mettant en œuvre l'interface `Gauge` :

```java
import com.codahale.metrics.Gauge;

registry.register("queue.size", new Gauge<Integer>() {
    @Override
    public Integer getValue() {
        return someQueue.size(); // Remplacez par votre logique
    }
});
```

#### **Histogrammes**
Les histogrammes suivent la distribution statistique des valeurs (par exemple, les tailles des requêtes) :

```java
import com.codahale.metrics.Histogram;

Histogram histogram = registry.histogram("request.sizes");
histogram.update(150); // Enregistrer une valeur
```

#### **Mètres**
Les mètres mesurent le taux d'événements (par exemple, les requêtes par seconde) :

```java
import com.codahale.metrics.Meter;

Meter meter = registry.meter("requests.rate");
meter.mark(); // Enregistrer un événement
```

#### **Minuteurs**
Les minuteurs mesurent à la fois le taux et la durée des événements (par exemple, le temps de traitement des requêtes) :

```java
import com.codahale.metrics.Timer;

Timer timer = registry.timer("request.duration");
Timer.Context context = timer.time();
try {
    // Simuler un travail
    Thread.sleep(100);
} finally {
    context.stop(); // Enregistrer la durée
}
```

---

### Étape 4 : Signaler les Métriques
Pour rendre les métriques utiles, vous devez les signaler quelque part. Dropwizard Metrics prend en charge divers rapporteurs, tels que la console, JMX ou Graphite. Voici un exemple de rapporteur de console qui enregistre les métriques toutes les 10 secondes :

```java
import com.codahale.metrics.ConsoleReporter;
import java.util.concurrent.TimeUnit;

ConsoleReporter reporter = ConsoleReporter.forRegistry(registry)
    .convertRatesTo(TimeUnit.SECONDS)
    .convertDurationsTo(TimeUnit.MILLISECONDS)
    .build();
reporter.start(10, TimeUnit.SECONDS); // Signaler toutes les 10 secondes
```

Pour une utilisation en production, envisagez d'intégrer des systèmes comme Graphite ou d'exposer les métriques via JMX.

---

### Étape 5 : Intégrer avec des Frameworks (Optionnel)
Si vous utilisez un framework web comme Jersey, vous pouvez utiliser le module `metrics-jersey` pour instrumenter automatiquement vos points de terminaison. De plus, des annotations comme `@Timed` ou `@Counted` peuvent simplifier la collecte des métriques :

```java
import com.codahale.metrics.annotation.Timed;

@Path("/example")
public class ExampleResource {
    @GET
    @Timed
    public String getExample() {
        return "Hello, world!";
    }
}
```

Ajoutez la dépendance `metrics-jersey` et configurez-la avec votre application Jersey pour activer cette fonctionnalité.

---

### Bonnes Pratiques
- **Conventions de Nommage** : Utilisez un schéma de nommage hiérarchique pour la clarté (par exemple, `com.example.myapp.requests.total`).
- **Performance** : Soyez prudent avec le nombre et la fréquence des métriques, car une collecte excessive peut affecter les performances.
- **Documentation** : Consultez la [documentation Dropwizard Metrics](https://metrics.dropwizard.io/) pour des exemples à jour et des fonctionnalités avancées.

---

### Exemple : Tout Mettre Ensemble
Voici un exemple simple combinant plusieurs concepts :

```java
import com.codahale.metrics.*;
import java.util.concurrent.TimeUnit;

public class MetricsExample {
    public static void main(String[] args) throws InterruptedException {
        MetricRegistry registry = new MetricRegistry();

        // Créer un compteur
        Counter counter = registry.counter("example.counter");
        counter.inc();

        // Créer un minuteur
        Timer timer = registry.timer("example.timer");
        Timer.Context context = timer.time();
        Thread.sleep(100); // Simuler un travail
        context.stop();

        // Démarrer un rapporteur de console
        ConsoleReporter reporter = ConsoleReporter.forRegistry(registry)
            .convertRatesTo(TimeUnit.SECONDS)
            .convertDurationsTo(TimeUnit.MILLISECONDS)
            .build();
        reporter.start(1, TimeUnit.SECONDS);

        // Garder le programme en cours d'exécution pour voir les rapports
        Thread.sleep(5000);
    }
}
```

Ce code suit un compteur et un minuteur, signalant les résultats à la console toutes les secondes.

---

### Notes Finales
La bibliothèque `com.yammer.metrics` a évolué vers Dropwizard Metrics, utilisez donc toujours la dernière version du groupe `io.dropwizard.metrics`. Si vous démarrez un nouveau projet, vous pourriez également explorer des alternatives modernes comme Micrometer, mais Dropwizard Metrics reste un choix solide pour de nombreuses applications Java. Pour plus de détails, consultez la documentation officielle !