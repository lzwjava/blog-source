---
audio: false
generated: true
lang: es
layout: post
title: Métricas de Aplicación en Java
translated: true
type: note
---

La biblioteca `com.yammer.metrics`, desarrollada originalmente por Yammer, ahora forma parte de la biblioteca **Dropwizard Metrics**. Proporciona una forma robusta de recopilar y reportar métricas de aplicaciones en Java, ayudándote a monitorear aspectos del rendimiento como conteos de solicitudes, tiempos de respuesta y más. A continuación se presenta una guía sobre cómo usarla efectivamente.

---

### Paso 1: Agregar la Dependencia
Dado que `com.yammer.metrics` ha evolucionado a Dropwizard Metrics, deberías usar la biblioteca Dropwizard Metrics. Si estás usando Maven, agrega la siguiente dependencia a tu `pom.xml`:

```xml
<dependency>
    <groupId>io.dropwizard.metrics</groupId>
    <artifactId>metrics-core</artifactId>
    <version>4.2.0</version> <!-- Usa la última versión disponible -->
</dependency>
```

Dependiendo de tus necesidades, también podrías querer módulos adicionales, tales como:
- `metrics-jvm` para métricas relacionadas con la JVM.
- `metrics-httpclient` para métricas de cliente HTTP.
- `metrics-jersey` para integración con el framework web Jersey.

Consulta la [documentación de Dropwizard Metrics](https://metrics.dropwizard.io/) para obtener la última versión y los módulos disponibles.

---

### Paso 2: Crear un Registro de Métricas
El `MetricRegistry` es el lugar central donde se almacenan todas las métricas. Normalmente creas una instancia para tu aplicación:

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
Dropwizard Metrics soporta varios tipos de métricas, cada una adecuada para diferentes necesidades de monitoreo:

#### **Contadores**
Los contadores se utilizan para rastrear valores que pueden aumentar o disminuir (por ejemplo, el número de solicitudes procesadas).

```java
import com.codahale.metrics.Counter;

Counter counter = registry.counter("requests.processed");
counter.inc();  // Incrementar en 1
counter.inc(5); // Incrementar en 5
counter.dec();  // Decrementar en 1
```

#### **Gauges**
Los gauges proporcionan una instantánea de un valor en un momento específico (por ejemplo, el tamaño actual de una cola). Defines un gauge implementando la interfaz `Gauge`:

```java
import com.codahale.metrics.Gauge;

registry.register("queue.size", new Gauge<Integer>() {
    @Override
    public Integer getValue() {
        return someQueue.size(); // Reemplaza con tu lógica
    }
});
```

#### **Histogramas**
Los histogramas rastrean la distribución estadística de valores (por ejemplo, tamaños de solicitud):

```java
import com.codahale.metrics.Histogram;

Histogram histogram = registry.histogram("request.sizes");
histogram.update(150); // Registrar un valor
```

#### **Meters**
Los meters miden la tasa de eventos (por ejemplo, solicitudes por segundo):

```java
import com.codahale.metrics.Meter;

Meter meter = registry.meter("requests.rate");
meter.mark(); // Registrar un evento
```

#### **Timers**
Los timers miden tanto la tasa como la duración de los eventos (por ejemplo, el tiempo de procesamiento de una solicitud):

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

### Paso 4: Reportar Métricas
Para que las métricas sean útiles, necesitas reportarlas en algún lugar. Dropwizard Metrics soporta varios reportadores, como consola, JMX o Graphite. Aquí hay un ejemplo de un reportador de consola que registra métricas cada 10 segundos:

```java
import com.codahale.metrics.ConsoleReporter;
import java.util.concurrent.TimeUnit;

ConsoleReporter reporter = ConsoleReporter.forRegistry(registry)
    .convertRatesTo(TimeUnit.SECONDS)
    .convertDurationsTo(TimeUnit.MILLISECONDS)
    .build();
reporter.start(10, TimeUnit.SECONDS); // Reportar cada 10 segundos
```

Para uso en producción, considera integrar con sistemas como Graphite o exponer métricas vía JMX.

---

### Paso 5: Integrar con Frameworks (Opcional)
Si estás usando un framework web como Jersey, puedes usar el módulo `metrics-jersey` para instrumentar automáticamente tus endpoints. Adicionalmente, anotaciones como `@Timed` o `@Counted` pueden simplificar la recolección de métricas:

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

Agrega la dependencia `metrics-jersey` y configúrala con tu aplicación Jersey para habilitar esta característica.

---

### Mejores Prácticas
- **Convenciones de Nombrado**: Usa un esquema de nombres jerárquico para mayor claridad (por ejemplo, `com.example.myapp.requests.total`).
- **Rendimiento**: Ten cuidado con el número y la frecuencia de las métricas, ya que una recolección excesiva puede impactar el rendimiento.
- **Documentación**: Consulta la [documentación de Dropwizard Metrics](https://metrics.dropwizard.io/) para obtener ejemplos actualizados y características avanzadas.

---

### Ejemplo: Integrando Todo
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

        // Crear un timer
        Timer timer = registry.timer("example.timer");
        Timer.Context context = timer.time();
        Thread.sleep(100); // Simular trabajo
        context.stop();

        // Iniciar un reportador de consola
        ConsoleReporter reporter = ConsoleReporter.forRegistry(registry)
            .convertRatesTo(TimeUnit.SECONDS)
            .convertDurationsTo(TimeUnit.MILLISECONDS)
            .build();
        reporter.start(1, TimeUnit.SECONDS);

        // Mantener el programa ejecutándose para ver los reportes
        Thread.sleep(5000);
    }
}
```

Este código rastrea un contador y un timer, reportando los resultados a la consola cada segundo.

---

### Notas Finales
La biblioteca `com.yammer.metrics` ha evolucionado a Dropwizard Metrics, así que siempre usa la última versión del grupo `io.dropwizard.metrics`. Si estás comenzando un nuevo proyecto, también podrías explorar alternativas modernas como Micrometer, pero Dropwizard Metrics sigue siendo una opción sólida para muchas aplicaciones Java. Para más detalles, ¡consulta la documentación oficial!