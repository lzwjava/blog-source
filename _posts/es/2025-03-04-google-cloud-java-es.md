---
audio: false
generated: true
lang: es
layout: post
title: Cliente Java de Google Cloud
translated: true
type: note
---

### Puntos Clave
- Parece probable que para usar `com.google.cloud` en Java, necesites configurar un entorno de desarrollo Java, incluir las dependencias de las bibliotecas cliente de Google Cloud, configurar la autenticación y usar las bibliotecas para interactuar con los servicios de Google Cloud.
- La investigación sugiere que la autenticación se puede manejar automáticamente en las plataformas de Google Cloud o configurar manualmente para el desarrollo local usando credenciales de cuenta de servicio.
- La evidencia se inclina por usar Maven o Gradle para gestionar las dependencias, con ejemplos proporcionados para Cloud Storage como un caso de uso común.

### Configuración de tu Entorno de Desarrollo
Para comenzar, asegúrate de tener un Java Development Kit (JDK) versión 8 o superior instalado, junto con una herramienta de construcción como Maven o Gradle. Estas herramientas ayudan a gestionar las dependencias de tu proyecto y los procesos de construcción.

### Inclusión de Dependencias
Añade las dependencias de las bibliotecas cliente de Google Cloud a tu proyecto. Para Maven, incluye la Bill of Materials (BOM) y las bibliotecas de servicio específicas en tu archivo `pom.xml`. Por ejemplo, para usar Cloud Storage:

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>com.google.cloud</groupId>
            <artifactId>libraries-bom</artifactId>
            <version>latest_version</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
<dependencies>
    <dependency>
        <groupId>com.google.cloud</groupId>
        <artifactId>google-cloud-storage</artifactId>
    </dependency>
</dependencies>
```

Reemplaza "latest_version" con la versión actual del [repositorio GitHub de las bibliotecas cliente de Java para Google Cloud](https://github.com/googleapis/google-cloud-java).

### Configuración de la Autenticación
La autenticación a menudo se maneja automáticamente si tu aplicación se ejecuta en plataformas de Google Cloud como Compute Engine o App Engine. Para el desarrollo local, establece la variable de entorno `GOOGLE_APPLICATION_CREDENTIALS` para que apunte a un archivo de clave JSON de una cuenta de servicio, o configúralo mediante programación.

### Uso de las Bibliotecas
Una vez configurado, importa las clases necesarias, crea un objeto de servicio y realiza llamadas a la API. Por ejemplo, para listar los buckets en Cloud Storage:

```java
import com.google.cloud.storage.*;
Storage storage = StorageOptions.getDefaultInstance().getService();
Page<Bucket> buckets = storage.list();
for (Bucket bucket : buckets.iterateAll()) {
    System.out.println(bucket.getName());
}
```

Un detalle inesperado es que las bibliotecas admiten varios servicios de Google Cloud, cada uno con su propio subpaquete bajo `com.google.cloud`, como `com.google.cloud.bigquery` para BigQuery, ofreciendo una funcionalidad extensa más allá del almacenamiento.

---

### Nota de Estudio: Guía Completa sobre el Uso de `com.google.cloud` en Java

Esta nota proporciona una exploración detallada del uso de las bibliotecas cliente de Java para Google Cloud, centrándose específicamente en el paquete `com.google.cloud`, para interactuar con los servicios de Google Cloud. Amplía la respuesta directa incluyendo todos los detalles relevantes de la investigación, organizados para claridad y profundidad, adecuados para desarrolladores que buscan una comprensión exhaustiva.

#### Introducción a las Bibliotecas Cliente de Java para Google Cloud
Las bibliotecas cliente de Java para Google Cloud, accesibles bajo el paquete `com.google.cloud`, proporcionan interfaces idiomáticas e intuitivas para interactuar con servicios de Google Cloud como Cloud Storage, BigQuery y Compute Engine. Estas bibliotecas están diseñadas para reducir el código repetitivo, manejar los detalles de comunicación de bajo nivel e integrarse perfectamente con las prácticas de desarrollo Java. Son particularmente útiles para construir aplicaciones nativas de la nube, aprovechando herramientas como Spring, Maven y Kubernetes, como se destaca en la documentación oficial.

#### Configuración del Entorno de Desarrollo
Para comenzar, se requiere un Java Development Kit (JDK) versión 8 o superior, asegurando la compatibilidad con las bibliotecas. La distribución recomendada es Eclipse Temurin, una opción de código abierto certificada por Java SE TCK, como se señala en las guías de configuración. Adicionalmente, una herramienta de automatización de construcción como Maven o Gradle es esencial para gestionar las dependencias. La CLI de Google Cloud (`gcloud`) también se puede instalar para interactuar con los recursos desde la línea de comandos, facilitando las tareas de despliegue y monitoreo.

#### Gestión de Dependencias
La gestión de dependencias se simplifica usando la Bill of Materials (BOM) proporcionada por Google Cloud, que ayuda a gestionar las versiones en múltiples bibliotecas. Para Maven, añade lo siguiente a tu `pom.xml`:

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>com.google.cloud</groupId>
            <artifactId>libraries-bom</artifactId>
            <version>latest_version</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
<dependencies>
    <dependency>
        <groupId>com.google.cloud</groupId>
        <artifactId>google-cloud-storage</artifactId>
    </dependency>
</dependencies>
```

Para Gradle, se aplican configuraciones similares, asegurando la consistencia de versiones. El número de versión debe verificarse contra el [repositorio GitHub de las bibliotecas cliente de Java para Google Cloud](https://github.com/googleapis/google-cloud-java) para las actualizaciones más recientes. Este repositorio también detalla las plataformas soportadas, incluyendo x86_64, Mac OS X, Windows y Linux, pero señala limitaciones en Android y Raspberry Pi.

#### Mecanismos de Autenticación
La autenticación es un paso crítico, con opciones que varían según el entorno. En las plataformas de Google Cloud como Compute Engine, Kubernetes Engine o App Engine, las credenciales se infieren automáticamente, simplificando el proceso. Para otros entornos, como el desarrollo local, están disponibles los siguientes métodos:

- **Cuenta de Servicio (Recomendado):** Genera un archivo de clave JSON desde la Consola de Google Cloud y establece la variable de entorno `GOOGLE_APPLICATION_CREDENTIALS` en su ruta. Alternativamente, cárgalo mediante programación:
  ```java
  import com.google.auth.oauth2.GoogleCredentials;
  import com.google.cloud.storage.*;
  GoogleCredentials credentials = GoogleCredentials.fromStream(new FileInputStream("ruta/al/key.json"));
  Storage storage = StorageOptions.newBuilder().setCredentials(credentials).build().getService();
  ```
- **Desarrollo/Pruebas Local:** Usa el SDK de Google Cloud con `gcloud auth application-default login` para credenciales temporales.
- **Token OAuth2 Existente:** Usa `GoogleCredentials.create(new AccessToken(accessToken, expirationTime))` para casos de uso específicos.

El orden de precedencia para la especificación del ID del proyecto incluye las opciones de servicio, la variable de entorno `GOOGLE_CLOUD_PROJECT`, App Engine/Compute Engine, el archivo de credenciales JSON y el SDK de Google Cloud, con `ServiceOptions.getDefaultProjectId()` ayudando a inferir el ID del proyecto.

#### Uso de las Bibliotecas Cliente
Una vez que las dependencias y la autenticación están configuradas, los desarrolladores pueden usar las bibliotecas para interactuar con los servicios de Google Cloud. Cada servicio tiene su propio subpaquete bajo `com.google.cloud`, como `com.google.cloud.storage` para Cloud Storage o `com.google.cloud.bigquery` para BigQuery. Aquí hay un ejemplo detallado para Cloud Storage:

```java
import com.google.cloud.storage.*;
Storage storage = StorageOptions.getDefaultInstance().getService();
Page<Bucket> buckets = storage.list();
for (Bucket bucket : buckets.iterateAll()) {
    System.out.println(bucket.getName());
}
```

Este ejemplo lista todos los buckets, pero la biblioteca soporta operaciones como subir objetos, descargar archivos y gestionar políticas de buckets. Para otros servicios, se aplican patrones similares, con métodos detallados disponibles en los respectivos javadocs, como aquellos para BigQuery en [Google Cloud Java reference docs](https://googleapis.dev/java/google-cloud-clients/latest/).

#### Características Avanzadas y Consideraciones
Las bibliotecas soportan características avanzadas como operaciones de larga duración (LROs) usando `OperationFuture`, con tiempos de espera y políticas de reintento configurables. Por ejemplo, AI Platform (v3.24.0) incluye por defecto un retraso inicial de reintento de 5000ms, un multiplicador de 1.5, un retraso máximo de reintento de 45000ms y un tiempo de espera total de 300000ms. La configuración de proxy también es compatible, usando `https.proxyHost` y `https.proxyPort` para HTTPS/gRPC, con opciones personalizadas para gRPC vía `ProxyDetector`.

La autenticación con clave de API está disponible para algunas APIs, establecida manualmente a través de cabeceras para gRPC o REST, como se muestra en ejemplos para el servicio de Language. Las pruebas se facilitan con las herramientas proporcionadas, detalladas en el TESTING.md del repositorio, y los plugins para IDE como IntelliJ y Eclipse mejoran el desarrollo con la integración de la biblioteca.

#### Plataformas Soportadas y Limitaciones
Las bibliotecas son compatibles con varias plataformas, con clientes HTTP funcionando en todas partes y clientes gRPC soportados en x86_64, Mac OS X, Windows y Linux. Sin embargo, no son compatibles con Android, Raspberry Pi o App Engine Standard Java 7, excepto para Datastore, Storage y BigQuery. Los entornos soportados incluyen Windows x86_64, Mac OS X x86_64, Linux x86_64, GCE, GKE, GAE Std J8, GAE Flex y Alpine Linux (Java 11+).

#### Recursos y Lecturas Adicionales
Para orientación adicional, el [repositorio GitHub de las bibliotecas cliente de Java para Google Cloud](https://github.com/googleapis/google-cloud-java) ofrece ejemplos de código, guías de contribución y recursos para la resolución de problemas. Tutoriales como los de [Baeldung](https://www.baeldung.com/java-google-cloud-storage) proporcionan ejemplos prácticos, como el uso de Cloud Storage, mientras que la documentación oficial en [Google Cloud for Developers](https://developers.google.com/learn/topics/cloud-java) cubre conceptos más amplios de desarrollo de aplicaciones.

#### Tabla: Detalles Clave de Configuración

| **Aspecto**               | **Detalles**                                                                                     |
|--------------------------|-------------------------------------------------------------------------------------------------|
| Versión de Java          | Requiere Java 8 o superior.                                                                     |
| Gestión de Dependencias  | Usa BOM para consistencia de versiones, ej., Maven `libraries-bom`.                             |
| Métodos de Autenticación | Automática en GCE/GKE/GAE, manual vía `GOOGLE_APPLICATION_CREDENTIALS` o programática.          |
| Plataformas Soportadas   | Clientes HTTP en todas partes, gRPC en x86_64, Mac OS X, Windows, Linux; no en Android, Raspberry Pi.|
| Servicio de Ejemplo      | Cloud Storage: `com.google.cloud.storage`, métodos para listar buckets, gestión de objetos.     |

Esta guía completa asegura que los desarrolladores tengan toda la información necesaria para usar `com.google.cloud` en Java de manera efectiva, abordando la configuración, autenticación, uso y características avanzadas, con referencias a fuentes autorizadas para una mayor exploración.

#### Citas Clave
- [Repositorio GitHub de las bibliotecas cliente de Java para Google Cloud con código detallado y configuración](https://github.com/googleapis/google-cloud-java)
- [Documentación de Google Cloud para la visión general del desarrollo en Java](https://cloud.google.com/products/anthos)
- [Tutorial de Baeldung sobre Google Cloud Storage con Java con ejemplos prácticos](https://www.baeldung.com/java-google-cloud-storage)