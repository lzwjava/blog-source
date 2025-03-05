---
audio: true
generated: true
lang: es
layout: post
title: Métricas de Aplicación en Java
translated: true
---

La biblioteca `com.yammer.metrics`, originalmente desarrollada por Yammer, ahora forma parte de la biblioteca **Dropwizard Metrics**. Proporciona una manera robusta de recopilar e informar métricas de la aplicación en Java, ayudándote a monitorear aspectos de rendimiento como el número de solicitudes, los tiempos de respuesta y más. A continuación se presenta una guía sobre cómo usarla de manera efectiva.

---

### Paso 1: Agregar la Dependencia
Dado que `com.yammer.metrics` ha evolucionado a Dropwizard Metrics, debe usar la biblioteca Dropwizard Metrics. Si está utilizando Maven, agregue la siguiente dependencia a su `pom.xml`:

```xml
<dependency>
    <groupId>io.dropwizard.metrics</groupId>
    <artifactId>metrics-core</artifactId>
    <version>4.2.0</version> <!-- Use la versión más reciente disponible -->
</dependency>
```

Dependiendo de sus necesidades, también podría querer módulos adicionales, como:
- `metrics-jvm` para métricas relacionadas con la JVM.
- `metrics-httpclient` para métricas del cliente HTTP.
- `metrics-jersey` para la integración con el marco web Jersey.

Consulte la [documentación de Dropwizard Metrics](https://metrics.dropwizard.io/) para obtener la última versión y los módulos disponibles.

---

### Paso 2: Crear un Registro de Métricas
El `MetricRegistry` es el lugar central donde se almacenan todas las métricas. Generalmente, crea una instancia para su aplicación:

```java
import com.codahale.metrics.MetricRegistry;

public class MyApplication {
    public static void main(String[] args) {
        MetricRegistry registry = new MetricRegistry();
    }
}
```

---

### Paso 3: Usar Diferentes Tipos de Métricas
Dropwizard Metrics admite varios tipos de métricas, cada una adecuada para diferentes necesidades de monitoreo:

#### **Contadores**
Los contadores se utilizan para rastrear valores que pueden aumentar o disminuir (por ejemplo, el número de solicitudes procesadas).

```java
import com.codahale.metrics.Counter;

Counter counter = registry.counter("requests.processed");
counter.inc();  // Incrementar en 1
counter.inc(5); // Incrementar en 5
counter.dec();  // Decrementar en 1
```

#### **Medidores**
Los medidores proporcionan una instantánea de un valor en un momento específico (por ejemplo, el tamaño actual de la cola). Define un medidor implementando la interfaz `Gauge`:

```java
import com.codahale.metrics.Gauge;

registry.register("queue.size", new Gauge<Integer>() {
    @Override
    public Integer getValue() {
        return someQueue.size(); // Reemplazar con su lógica
    }
});
```

#### **Histogramas**
Los histogramas rastrean la distribución estadística de los valores (por ejemplo, los tamaños de las solicitudes):

```java
import com.codahale.metrics.Histogram;

Histogram histogram = registry.histogram("request.sizes");
histogram.update(150); // Registrar un valor
```

#### **Medidores**
Los medidores miden la tasa de eventos (por ejemplo, solicitudes por segundo):

```java
import com.codahale.metrics.Meter;

Meter meter = registry.meter("requests.rate");
meter.mark(); // Registrar un evento
```

#### **Temporizadores**
Los temporizadores miden tanto la tasa como la duración de los eventos (por ejemplo, el tiempo de procesamiento de las solicitudes):

```java
import com.codahale.metrics.Timer;

Timer timer = registry.timer("request.duration");
Timer.Context context = timer.time();
try {
    // Simular algún trabajo
    Thread.sleep(100);
} finally {
    context.stop(); // Registrar la duración
}
```

---

### Paso 4: Informar Métricas
Para que las métricas sean útiles, debe informarlas en algún lugar. Dropwizard Metrics admite varios informantes, como consola, JMX o Graphite. Aquí hay un ejemplo de un informante de consola que registra métricas cada 10 segundos:

```java
import com.codahale.metrics.ConsoleReporter;
import java.util.concurrent.TimeUnit;

ConsoleReporter reporter = ConsoleReporter.forRegistry(registry)
    .convertRatesTo(TimeUnit.SECONDS)
    .convertDurationsTo(TimeUnit.MILLISECONDS)
    .build();
reporter.start(10, TimeUnit.SECONDS); // Informar cada 10 segundos
```

Para uso en producción, considere integrarse con sistemas como Graphite o exponer métricas a través de JMX.

---

### Paso 5: Integrar con Marcos (Opcional)
Si está utilizando un marco web como Jersey, puede usar el módulo `metrics-jersey` para instrumentar automáticamente sus puntos finales. Además, anotaciones como `@Timed` o `@Counted` pueden simplificar la recopilación de métricas:

```java
import com.codahale.metrics.annotation.Timed;

@Path("/example")
public class ExampleResource {
    @GET
    @Timed
    public String getExample() {
        return "¡Hola, mundo!";
    }
}
```

Agregue la dependencia `metrics-jersey` y configúrela con su aplicación Jersey para habilitar esta característica.

---

### Mejores Prácticas
- **Convenciones de Nombrado**: Use un esquema de nomenclatura jerárquica para la claridad (por ejemplo, `com.example.myapp.requests.total`).
- **Rendimiento**: Sea cauteloso con el número y la frecuencia de las métricas, ya que la recopilación excesiva puede afectar el rendimiento.
- **Documentación**: Consulte la [documentación de Dropwizard Metrics](https://metrics.dropwizard.io/) para obtener ejemplos actualizados y características avanzadas.

---

### Ejemplo: Ponerlo Todo Juntos
Aquí hay un ejemplo simple que combina varios conceptos:

```java
import com.codahale.metrics.*;
import java.util.concurrent.TimeUnit;

public class MetricsExample {
    public static void main(String[] args) throws InterruptedException {
        MetricRegistry registry = new MetricRegistry();

        // Crear un contador
        Counter counter = registry.counter("example.counter");
        counter.inc();

        // Crear un temporizador
        Timer timer = registry.timer("example.timer");
        Timer.Context context = timer.time();
        Thread.sleep(100); // Simular trabajo
        context.stop();

        // Iniciar un informante de consola
        ConsoleReporter reporter = ConsoleReporter.forRegistry(registry)
            .convertRatesTo(TimeUnit.SECONDS)
            .convertDurationsTo(TimeUnit.MILLISECONDS)
            .build();
        reporter.start(1, TimeUnit.SECONDS);

        // Mantener el programa en ejecución para ver los informes
        Thread.sleep(5000);
    }
}
```

Este código rastrea un contador y un temporizador, informando los resultados en la consola cada segundo.

---

### Notas Finales
La biblioteca `com.yammer.metrics` ha evolucionado a Dropwizard Metrics, por lo que siempre debe usar la última versión del grupo `io.dropwizard.metrics`. Si está comenzando un nuevo proyecto, también podría explorar alternativas modernas como Micrometer, pero Dropwizard Metrics sigue siendo una opción sólida para muchas aplicaciones de Java. Para más detalles, consulte la documentación oficial.