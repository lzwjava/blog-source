---
audio: false
generated: true
lang: es
layout: post
title: 'Guía de Micrómetros: Herramientas y Observabilidad'
translated: true
type: note
---

Esta guía integral cubre dos temas distintos: **Micrómetros (la herramienta de medición)** y **Micrometer (la fachada de observabilidad para aplicaciones Java, particularmente Spring Boot), centrándose en soluciones de trazado.**

Vamos a desglosarlos:

-----

## Parte 1: Guía Integral sobre Micrómetros (Herramienta de Medición)

Un micrómetro, a menudo llamado micrómetro de tornillo o pálmer, es un instrumento de medición de precisión utilizado para obtener mediciones muy precisas de pequeñas distancias, típicamente en el rango de milésimas de pulgada o centésimas de milímetro. Es ampliamente utilizado en ingeniería, mecanizado, fabricación y campos científicos donde las dimensiones precisas son críticas.

### 1. ¿Qué es un Micrómetro?

En esencia, un micrómetro utiliza un mecanismo de tornillo precisamente mecanizado para traducir el movimiento rotacional en movimiento lineal. Esto permite ajustes finos y lecturas precisas de las dimensiones de un objeto al sujetarlo entre un yunque estacionario y un husillo móvil.

### 2. Componentes Clave de un Micrómetro:

*   **Armazón (Bastidor):** El cuerpo principal en forma de C que sostiene todos los demás componentes. Proporciona estabilidad y debe manejarse con cuidado para evitar errores por expansión térmica.
*   **Yunque:** La cara de medición estacionaria contra la cual se coloca el objeto.
*   **Husillo:** La cara de medición móvil que se mueve hacia o lejos del yunque cuando se gira el tambor.
*   **Manguito (o Cuerpo):** La parte fija del micrómetro que alberga la escala lineal principal, mostrando números enteros y medias incrementos (por ejemplo, en pulgadas o milímetros).
*   **Tambor:** La parte giratoria que mueve el husillo y tiene una escala finamente graduada para lecturas más precisas.
*   **Trinquete (Tope de Seguridad):** Ubicado al final del tambor, asegura una presión de medición consistente al deslizarse cuando se aplica la fuerza correcta, evitando el apriete excesivo y la distorsión de la pieza de trabajo.
*   **Fijador (o Palanca de Bloqueo):** Se utiliza para bloquear el husillo en su lugar una vez que se ha tomado una medición, evitando movimientos accidentales y preservando la lectura.

### 3. Tipos de Micrómetros:

Los micrómetros vienen en varios tipos, cada uno diseñado para tareas de medición específicas:

*   **Micrómetro Externo:** El tipo más común, utilizado para medir dimensiones externas como el diámetro de un eje o el espesor de una placa.
*   **Micrómetro Interno:** Utilizado para medir dimensiones internas, como el diámetro de un agujero o un bore. A menudo tienen diseños diferentes, como micrómetros tubulares o de mandíbula.
*   **Micrómetro de Profundidad:** Utilizado para medir la profundidad de agujeros, ranuras o escalones.
*   **Micrómetro para Roscas:** Diseñado para medir el diámetro de paso de las roscas de tornillos.
*   **Micrómetro de Bolas:** Cuenta con yunques/husillos con forma de bola para medir el espesor de superficies curvas o características específicas como paredes de tubos.
*   **Micrómetro de Discos:** Tiene caras de medición planas y con forma de disco para medir materiales delgados, papel o dientes de engranajes.
*   **Micrómetro Digital:** Cuenta con una pantalla electrónica para lecturas digitales directas, eliminando el error de paralaje y facilitando las lecturas.
*   **Micrómetro Analógico:** Requiere la lectura manual de las escalas en el manguito y el tambor.
*   **Micrómetro con Nonio (Vernier):** Incluye una escala de nonio adicional para una precisión aún mayor, permitiendo lecturas más allá de las graduaciones principales del tambor.

### 4. Cómo Leer un Micrómetro (Ejemplo Analógico/Sistema Imperial):

Si bien las lecturas específicas varían entre el sistema imperial (pulgadas) y el métrico (milímetros) y entre analógico/digital, el principio general para los micrómetros analógicos es:

1.  **Leer la Escala del Manguito (Escala Principal):**
    *   **Pulgadas Enteras:** Anota la marca de pulgada entera más grande visible.
    *   **Décimas de Pulgada (0.100"):** Cada línea numerada en el manguito representa 0.100 pulgadas.
    *   **Veinticinco Milésimas (0.025"):** Cada línea sin numerar entre las marcas de décimas representa 0.025 pulgadas.
2.  **Leer la Escala del Tambor:**
    *   El tambor tiene 25 graduaciones, y cada marca representa 0.001 pulgadas.
    *   Lee la línea en el tambor que se alinea con la línea índice en el manguito.
3.  **Combinar las Lecturas:** Suma los valores del manguito (pulgadas enteras, décimas y veinticinco milésimas) y del tambor (milésimas) para obtener la medición final.

**Ejemplo (Sistema Imperial):**

*   Manguito:
    *   Digamos que ves "1" (para 1.000")
    *   Luego 3 líneas después del "1" (3 x 0.100" = 0.300")
    *   Y 2 líneas debajo de la línea principal (2 x 0.025" = 0.050")
    *   Total del Manguito: 1.000 + 0.300 + 0.050 = 1.350"
*   Tambor:
    *   La marca número 15 en el tambor se alinea con la línea índice (0.015")
*   **Lectura Total:** 1.350" + 0.015" = **1.365"**

### 5. Uso Adecuado y Mejores Prácticas:

*   **Limpieza:** Siempre asegúrate de que las caras de medición (yunque y husillo) estén limpias y libres de polvo, aceite o residuos.
*   **Puesta a Cero:** Antes de usar, siempre "pon a cero" el micrómetro. Cierra las caras de medición suavemente usando el trinquete hasta que se toquen. La lectura debe ser 0.000 (o el rango inicial, por ejemplo, 25-50mm). Si no es así, ajusta el micrómetro para el error de cero. Los micrómetros digitales suelen tener un botón de reset.
*   **Temperatura:** Manipula el micrómetro por su armazón aislado o usa guantes, ya que el calor corporal puede causar expansión térmica y afectar la precisión, especialmente para micrómetros más grandes. Permite que tanto la herramienta como el objeto alcancen la temperatura ambiente.
*   **Presión Constante:** Utiliza siempre el trinquete para aplicar una presión de medición constante y apropiada. Apretar en exceso puede distorsionar el objeto o el micrómetro.
*   **Posicionamiento del Objeto:** Coloca el objeto en ángulo recto entre el yunque y el husillo para evitar lecturas sesgadas.
*   **Múltiples Mediciones:** Para dimensiones críticas, realiza varias mediciones en diferentes puntos del objeto para tener en cuenta las variaciones.
*   **Almacenamiento:** Almacena los micrómetros en sus estuches protectores para evitar daños.
*   **Calibración:** Verifica y calibra regularmente los micrómetros contra patrones conocidos (por ejemplo, bloques patrón) para garantizar su precisión.

-----

## Parte 2: Micrometer como Solución de Trazado para Proyectos Spring Java

En el contexto de los proyectos Spring Java, "Micrometer" se refiere a una **fachada de observabilidad de aplicaciones** que proporciona una API neutral con respecto al proveedor para instrumentar aplicaciones basadas en JVM. Te permite recopilar y exportar varios datos de telemetría, incluyendo métricas, registro de logs y **trazado distribuido**.

Micrometer Tracing es el sucesor de Spring Cloud Sleuth y está diseñado para proporcionar información sobre sistemas distribuidos complejos mediante el seguimiento de solicitudes a través de múltiples servicios.

### 1. ¿Qué es el Trazado Distribuido?

En una arquitectura de microservicios, una sola solicitud de usuario a menudo atraviesa múltiples servicios. El trazado distribuido te permite:

*   **Rastrear el flujo:** Ver la ruta completa que toma una solicitud a través de tu sistema.
*   **Identificar cuellos de botella:** Señalar qué servicio u operación está causando latencia.
*   **Comprender las dependencias:** Visualizar las interacciones entre los diferentes servicios.
*   **Simplificar la depuración:** Correlacionar los logs con solicitudes específicas, facilitando mucho la resolución de problemas.

Un trace distribuido se compone de **spans**. Un **span** representa una única operación o unidad de trabajo dentro de un trace (por ejemplo, una solicitud HTTP a un servicio, una consulta a la base de datos, la ejecución de un método). Los spans tienen un ID único, un tiempo de inicio y finalización, y pueden incluir etiquetas (pares clave-valor) y eventos para metadatos adicionales. Los spans se organizan jerárquicamente, con relaciones padre-hijo, formando un trace.

### 2. Micrometer Tracing en Spring Boot 3.x+

Spring Boot 3.x+ se integra profundamente con la API de Observación de Micrometer y Micrometer Tracing, haciendo que sea significativamente más fácil implementar el trazado distribuido.

#### 2.1. Conceptos Básicos:

*   **API de Observación (Observation API):** La API unificada de Micrometer para instrumentar tu código, capaz de producir métricas, traces y logs desde un único punto de instrumentación.
*   **Micrometer Tracing:** Una fachada sobre bibliotecas de trazado populares como OpenTelemetry y OpenZipkin Brave. Maneja el ciclo de vida de los spans, la propagación del contexto y el reporte a los backends de trazado.
*   **Puentes de Trazado (Tracer Bridges):** Micrometer Tracing proporciona "puentes" para conectar su API a implementaciones de trazado específicas (por ejemplo, `micrometer-tracing-bridge-otel` para OpenTelemetry, `micrometer-tracing-bridge-brave` para OpenZipkin Brave).
*   **Reportadores/Exportadores:** Estos componentes envían los datos de trace recopilados a un backend de trazado (por ejemplo, Zipkin, Jaeger, Grafana Tempo).

#### 2.2. Configuración de Micrometer Tracing en un Proyecto Java Spring Boot:

Aquí tienes una guía paso a paso:

**Paso 1: Agregar Dependencias**

Necesitas `spring-boot-starter-actuator` para las características de observabilidad, un puente de Micrometer Tracing y un reportador/exportador para tu backend de trazado elegido.

**Ejemplo con OpenTelemetry y Zipkin (elección común):**

En tu `pom.xml` (Maven):

```xml
<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-actuator</artifactId>
    </dependency>

    <dependency>
        <groupId>io.micrometer</groupId>
        <artifactId>micrometer-observation</artifactId>
    </dependency>

    <dependency>
        <groupId>io.micrometer</groupId>
        <artifactId>micrometer-tracing-bridge-otel</artifactId>
    </dependency>

    <dependency>
        <groupId>io.opentelemetry</groupId>
        <artifactId>opentelemetry-exporter-zipkin</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-webflux</artifactId>
    </dependency>
</dependencies>
```

**Paso 2: Configurar las Propiedades de Trazado**

En `application.properties` o `application.yml`, puedes configurar el comportamiento del trazado.

```properties
# Habilitar el trazado (normalmente true por defecto con actuator y dependencias de tracing)
management.tracing.enabled=true

# Configurar la probabilidad de muestreo (1.0 = 100% de las solicitudes son trazadas)
# El valor por defecto suele ser 0.1 (10%), configúralo en 1.0 para desarrollo/pruebas
management.tracing.sampling.probability=1.0

# Configurar la URL base de Zipkin (si se usa Zipkin)
spring.zipkin.base-url=http://localhost:9411
```

**Paso 3: Ejecutar un Backend de Trazado (por ejemplo, Zipkin)**

Necesitas un servidor de trazado para recopilar y visualizar tus traces. Zipkin es una opción popular para el desarrollo local.

Puedes ejecutar Zipkin via Docker:

```bash
docker run -d -p 9411:9411 openzipkin/zipkin
```

Una vez en ejecución, puedes acceder a la interfaz de usuario de Zipkin en `http://localhost:9411`.

**Paso 4: Instrumentación Automática (¡La Magia de Spring Boot!)**

Para muchos componentes comunes en Spring Boot (como endpoints `RestController`, `RestTemplate`, `WebClient`, `JdbcTemplate`, productores/consumidores de Kafka, etc.), Micrometer Tracing proporciona **instrumentación automática**. Esto significa que a menudo no necesitas escribir ningún código de trazado explícito para que el trazado básico de solicitudes funcione.

Spring Boot asegura que:

*   Las solicitudes HTTP entrantes crean automáticamente un nuevo trace o continúan uno existente si hay cabeceras de trazado presentes.
*   Las solicitudes salientes realizadas con `RestTemplateBuilder`, `RestClient.Builder` o `WebClient.Builder` auto-configurados propagan el contexto de trazado a los servicios posteriores (downstream).
*   Las declaraciones de log incluyen automáticamente `traceId` y `spanId` (si configuras tu patrón de logging).

**Ejemplo de Patrón de Logging (en `application.properties`):**

```properties
logging.pattern.level=%5p [${spring.application.name:},%X{traceId:-},%X{spanId:-}] %c{1.}:%M:%L - %m%n
```

Este patrón inyectará el `traceId` y `spanId` en tus líneas de log, facilitando la correlación de logs con un trace específico.

**Paso 5: Instrumentación Manual (para lógica personalizada)**

Si bien la auto-instrumentación cubre mucho, a menudo querrás trazar lógica de negocio específica u operaciones críticas dentro de tu aplicación. Puedes hacer esto usando:

*   **Anotación `@Observed` (Recomendada para Spring Boot 3.x+):**
    Esta anotación es parte de la API de Observación de Micrometer y es la forma preferida de crear observaciones (que pueden producir tanto métricas como traces).

    ```java
    import io.micrometer.observation.annotation.Observed;
    import org.springframework.stereotype.Service;

    @Service
    public class MyService {

        @Observed(name = "myService.processData", contextualName = "processing-data")
        public String processData(String input) {
            // ... tu lógica de negocio ...
            System.out.println("Processing data: " + input);
            return "Processed: " + input;
        }
    }
    ```

    El atributo `name` define el nombre para la observación (que se convierte en el nombre de la métrica y del span de trazado). `contextualName` proporciona un nombre más legible para el span en las herramientas de trazado.

*   **API Programática (para más control):**
    Puedes usar directamente los beans `ObservationRegistry` y `Tracer` proporcionados por Spring Boot.

    ```java
    import io.micrometer.observation.Observation;
    import io.micrometer.observation.ObservationRegistry;
    import org.springframework.stereotype.Service;

    @Service
    public class AnotherService {

        private final ObservationRegistry observationRegistry;

        public AnotherService(ObservationRegistry observationRegistry) {
            this.observationRegistry = observationRegistry;
        }

        public String performComplexOperation(String id) {
            return Observation.createNotStarted("complex.operation", observationRegistry)
                    .lowCardinalityKeyValue("operation.id", id) // Agrega una etiqueta
                    .observe(() -> {
                        // ... lógica compleja aquí ...
                        try {
                            Thread.sleep(100); // Simular trabajo
                        } catch (InterruptedException e) {
                            Thread.currentThread().interrupt();
                        }
                        return "Completed complex operation for " + id;
                    });
        }
    }
    ```

    Aquí, `observe()` envuelve el bloque de código, y `lowCardinalityKeyValue` agrega una etiqueta al span.

### 3. Trazado Distribuido en Microservicios:

Cuando tienes múltiples servicios Spring Boot, Micrometer Tracing facilita la propagación del contexto automáticamente para `RestTemplate`, `WebClient` y otros clientes instrumentados. Esto significa que el `traceId` y `spanId` se pasan en las cabeceras HTTP entre servicios (por ejemplo, la cabecera `traceparent` para W3C Trace Context).

Cuando una solicitud llega a un servicio posterior (downstream), Micrometer Tracing detecta estas cabeceras y continúa el trace existente, creando nuevos spans que son hijos del span padre del servicio que llama. Esto forma el trace completo de extremo a extremo.

### 4. Visualización de Traces:

Una vez que tu aplicación está instrumentada y enviando traces a un backend como Zipkin (o Jaeger, Lightstep, etc.), puedes:

1.  **Acceder a la UI:** Ve a la interfaz de usuario web del backend de trazado (por ejemplo, `http://localhost:9411` para Zipkin).
2.  **Encontrar Traces:** Usa filtros (nombre del servicio, nombre del span, ID del trace) para encontrar traces específicos.
3.  **Analizar Detalles del Trace:** Haz clic en un trace para ver su línea de tiempo, spans individuales, sus duraciones, etiquetas y eventos.
4.  **Grafo de Dependencias:** La mayoría de los backends de trazado pueden visualizar las dependencias de servicios basándose en los traces recopilados.

### 5. Mejores Prácticas para Micrometer Tracing:

*   **Nombra tus Spans de Manera Significativa:** Usa nombres claros, concisos y de baja cardinalidad para tus spans (por ejemplo, "userService.getUser", "productService.updateStock"). Evita incluir datos altamente dinámicos en los nombres de los spans.
*   **Usa Etiquetas para los Detalles (Datos de Alta Cardinalidad):** En lugar de poner datos dinámicos en los nombres de los spans, usa etiquetas (pares clave-valor) para contexto adicional. Por ejemplo, `userId`, `orderId`, `customerType`. Ten cuidado con las etiquetas de **alta cardinalidad**, ya que pueden aumentar significativamente los costos de almacenamiento y los tiempos de consulta en tu backend de trazado. Úsalas con criterio.
*   **Mantén los Spans Granulares pero No Excesivos:** Crea spans para operaciones significativas, pero evita crear demasiados spans diminutos, ya que esto puede agregar sobrecarga. Busca un equilibrio que proporcione suficiente visibilidad sin saturar el sistema.
*   **Propaga el Contexto:** Asegúrate de que el contexto de trazado se propague correctamente a través de los límites del servicio. La auto-configuración de Spring Boot maneja esto para escenarios comunes, pero ten cuidado al usar clientes personalizados u operaciones asíncronas.
*   **Muestreo (Sampling):** Para entornos de producción de alto tráfico, considera el uso de estrategias de muestreo para reducir el volumen de datos de trazado enviados a tu backend. Spring Boot permite configurar `management.tracing.sampling.probability`.
*   **Correlaciona Logs:** Aprovecha el `traceId` y `spanId` inyectados en los logs para una depuración más fácil y la correlación del comportamiento de la aplicación con solicitudes específicas.
*   **Monitorea tu Backend de Trazado:** Asegúrate de que tu backend de trazado (por ejemplo, el servidor Zipkin) tenga recursos suficientes para manejar el volumen de traces entrantes.
*   **Integra con Otras Herramientas de Observabilidad:** El trazado es una parte de la observabilidad. Combínalo con métricas (también a través de Micrometer) y logging estructurado para obtener una visión holística de la salud y el rendimiento de tu aplicación.

Siguiendo estas pautas, puedes aprovechar eficazmente Micrometer Tracing para obtener información profunda sobre tus aplicaciones Spring Boot, especialmente en entornos distribuidos.