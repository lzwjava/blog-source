---
audio: false
generated: true
lang: es
layout: post
title: Google Cloud Java Client
translated: true
---

### Puntos Clave
- Parece probable que para usar `com.google.cloud` en Java, necesites configurar un entorno de desarrollo de Java, incluir dependencias de la biblioteca de clientes de Google Cloud, configurar la autenticación y usar las bibliotecas para interactuar con los servicios de Google Cloud.
- La investigación sugiere que la autenticación puede manejarse automáticamente en las plataformas de Google Cloud o configurarse manualmente para el desarrollo local utilizando credenciales de cuenta de servicio.
- La evidencia indica el uso de Maven o Gradle para gestionar dependencias, con ejemplos proporcionados para el almacenamiento en la nube como un caso de uso común.

### Configuración del Entorno de Desarrollo
Para comenzar, asegúrate de tener instalado un Kit de Desarrollo de Java (JDK) versión 8 o superior, junto con una herramienta de construcción como Maven o Gradle. Estas herramientas ayudan a gestionar las dependencias de tu proyecto y los procesos de construcción.

### Inclusión de Dependencias
Añade las dependencias de la biblioteca de clientes de Google Cloud a tu proyecto. Para Maven, incluye el Bill of Materials (BOM) y las bibliotecas de servicios específicas en tu archivo `pom.xml`. Por ejemplo, para usar el almacenamiento en la nube:

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>com.google.cloud</groupId>
            <artifactId>libraries-bom</artifactId>
            <version>latest_version</version>
            <type>pom</type>
            <scope.import</scope>
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

Reemplaza "latest_version" con la versión actual del [repositorio de GitHub de las bibliotecas de clientes de Java de Google Cloud](https://github.com/googleapis/google-cloud-java).

### Configuración de Autenticación
La autenticación a menudo se maneja automáticamente si tu aplicación se ejecuta en plataformas de Google Cloud como Compute Engine o App Engine. Para el desarrollo local, establece la variable de entorno `GOOGLE_APPLICATION_CREDENTIALS` para que apunte a un archivo de clave JSON de una cuenta de servicio, o configúralo de manera programática.

### Uso de las Bibliotecas
Una vez configurado, importa las clases necesarias, crea un objeto de servicio y realiza llamadas a la API. Por ejemplo, para listar cubos en el almacenamiento en la nube:

```java
import com.google.cloud.storage.*;
Storage storage = StorageOptions.getDefaultInstance().getService();
Page<Bucket> buckets = storage.list();
for (Bucket bucket : buckets.iterateAll()) {
    System.out.println(bucket.getName());
}
```

Un detalle inesperado es que las bibliotecas soportan varios servicios de Google Cloud, cada uno con su propio subpaquete bajo `com.google.cloud`, como `com.google.cloud.bigquery` para BigQuery, ofreciendo funcionalidad más allá del almacenamiento.

---

### Nota de Encuesta: Guía Completa sobre el Uso de `com.google.cloud` en Java

Esta nota proporciona una exploración detallada del uso de las bibliotecas de clientes de Java de Google Cloud, centrándose específicamente en el paquete `com.google.cloud`, para interactuar con los servicios de Google Cloud. Amplía la respuesta directa incluyendo todos los detalles relevantes de la investigación, organizados para claridad y profundidad, adecuados para desarrolladores que buscan una comprensión exhaustiva.

#### Introducción a las Bibliotecas de Clientes de Java de Google Cloud
Las bibliotecas de clientes de Java de Google Cloud, accesibles bajo el paquete `com.google.cloud`, proporcionan interfaces idiomáticas e intuitivas para interactuar con servicios de Google Cloud como el almacenamiento en la nube, BigQuery y Compute Engine. Estas bibliotecas están diseñadas para reducir el código boilerplate, manejar detalles de comunicación de bajo nivel y integrarse sin problemas con las prácticas de desarrollo de Java. Son particularmente útiles para construir aplicaciones nativas en la nube, aprovechando herramientas como Spring, Maven y Kubernetes, como se destaca en la documentación oficial.

#### Configuración del Entorno de Desarrollo
Para comenzar, se requiere un Kit de Desarrollo de Java (JDK) versión 8 o superior, asegurando la compatibilidad con las bibliotecas. La distribución recomendada es Eclipse Temurin, una opción de código abierto, certificada por Java SE TCK, como se menciona en las guías de configuración. Además, es esencial una herramienta de automatización de construcción como Maven o Gradle para gestionar dependencias. También se puede instalar la CLI de Google Cloud (`gcloud`) para interactuar con recursos desde la línea de comandos, facilitando tareas de implementación y monitoreo.

#### Gestión de Dependencias
La gestión de dependencias se simplifica utilizando el Bill of Materials (BOM) proporcionado por Google Cloud, que ayuda a gestionar versiones en múltiples bibliotecas. Para Maven, añade lo siguiente a tu `pom.xml`:

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>com.google.cloud</groupId>
            <artifactId>libraries-bom</artifactId>
            <version>latest_version</version>
            <type>pom</type>
            <scope.import</scope>
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

Para Gradle, se aplican configuraciones similares, asegurando la consistencia de versiones. El número de versión debe verificarse contra el [repositorio de GitHub de las bibliotecas de clientes de Java de Google Cloud](https://github.com/googleapis/google-cloud-java) para las actualizaciones más recientes. Este repositorio también detalla las plataformas soportadas, incluyendo x86_64, Mac OS X, Windows y Linux, pero nota limitaciones en Android y Raspberry Pi.

#### Mecanismos de Autenticación
La autenticación es un paso crítico, con opciones que varían según el entorno. En plataformas de Google Cloud como Compute Engine, Kubernetes Engine o App Engine, las credenciales se inferen automáticamente, simplificando el proceso. Para otros entornos, como el desarrollo local, están disponibles los siguientes métodos:

- **Cuenta de Servicio (Recomendado):** Genera un archivo de clave JSON desde la consola de Google Cloud y establece la variable de entorno `GOOGLE_APPLICATION_CREDENTIALS` a su ruta. Alternativamente, cárgalo de manera programática:
  ```java
  import com.google.auth.oauth2.GoogleCredentials;
  import com.google.cloud.storage.*;
  GoogleCredentials credentials = GoogleCredentials.fromStream(new FileInputStream("path/to/key.json"));
  Storage storage = StorageOptions.newBuilder().setCredentials(credentials).build().getService();
  ```
- **Desarrollo Local/Pruebas:** Usa la SDK de Google Cloud con `gcloud auth application-default login` para credenciales temporales.
- **Token OAuth2 Existente:** Usa `GoogleCredentials.create(new AccessToken(accessToken, expirationTime))` para casos de uso específicos.

El orden de precedencia para la especificación del ID del proyecto incluye opciones de servicio, la variable de entorno `GOOGLE_CLOUD_PROJECT`, App Engine/Compute Engine, archivo de credenciales JSON y Google Cloud SDK, con `ServiceOptions.getDefaultProjectId()` ayudando a inferir el ID del proyecto.

#### Uso de las Bibliotecas de Clientes
Una vez configuradas las dependencias y la autenticación, los desarrolladores pueden usar las bibliotecas para interactuar con los servicios de Google Cloud. Cada servicio tiene su propio subpaquete bajo `com.google.cloud`, como `com.google.cloud.storage` para el almacenamiento en la nube o `com.google.cloud.bigquery` para BigQuery. Aquí tienes un ejemplo detallado para el almacenamiento en la nube:

```java
import com.google.cloud.storage.*;
Storage storage = StorageOptions.getDefaultInstance().getService();
Page<Bucket> buckets = storage.list();
for (Bucket bucket : buckets.iterateAll()) {
    System.out.println(bucket.getName());
}
```

Este ejemplo lista todos los cubos, pero la biblioteca soporta operaciones como subir objetos, descargar archivos y gestionar políticas de cubos. Para otros servicios, se aplican patrones similares, con métodos detallados disponibles en los respectivos javadocs, como los de BigQuery en [Google Cloud Java reference docs](https://googleapis.dev/java/google-cloud-clients/latest/).

#### Características Avanzadas y Consideraciones
Las bibliotecas soportan características avanzadas como operaciones de larga duración (LROs) utilizando `OperationFuture`, con políticas de tiempo de espera y reintento configurables. Por ejemplo, AI Platform (v3.24.0) incluye por defecto un retraso de reintento inicial de 5000ms, un multiplicador de 1.5, un retraso de reintento máximo de 45000ms y un tiempo de espera total de 300000ms. También se soporta la configuración de proxy, utilizando `https.proxyHost` y `https.proxyPort` para HTTPS/gRPC, con opciones personalizadas para gRPC a través de `ProxyDetector`.

La autenticación con clave API está disponible para algunas APIs, estableciéndose manualmente a través de encabezados para gRPC o REST, como se muestra en ejemplos para el servicio de Lenguaje. La prueba se facilita con herramientas proporcionadas, detalladas en el TESTING.md del repositorio, y los complementos de IDE para IntelliJ y Eclipse mejoran el desarrollo con la integración de la biblioteca.

#### Plataformas Soportadas y Limitaciones
Las bibliotecas son compatibles con diversas plataformas, con clientes HTTP funcionando en todas partes y clientes gRPC soportados en x86_64, Mac OS X, Windows y Linux. Sin embargo, no se soportan en Android, Raspberry Pi o App Engine Standard Java 7, excepto para Datastore, Storage y BigQuery. Los entornos soportados incluyen Windows x86_64, Mac OS X x86_64, Linux x86_64, GCE, GKE, GAE Std J8, GAE Flex y Alpine Linux (Java 11+).

#### Recursos y Lectura Adicional
Para orientación adicional, el [repositorio de GitHub de las bibliotecas de clientes de Java de Google Cloud](https://github.com/googleapis/google-cloud-java) ofrece ejemplos de código, directrices de contribución y recursos de solución de problemas. Tutoriales como los de [Baeldung](https://www.baeldung.com/java-google-cloud-storage) proporcionan ejemplos prácticos, como el uso del almacenamiento en la nube, mientras que la documentación oficial en [Google Cloud for Developers](https://developers.google.com/learn/topics/cloud-java) aborda conceptos más amplios de desarrollo de aplicaciones.

#### Tabla: Detalles de Configuración Clave

| **Aspecto**               | **Detalles**                                                                                     |
|--------------------------|-------------------------------------------------------------------------------------------------|
| Versión de Java           | Requiere Java 8 o superior.                                                                       |
| Gestión de Dependencias   | Usa BOM para consistencia de versiones, por ejemplo, Maven `libraries-bom`.                  |
| Métodos de Autenticación  | Automático en GCE/GKE/GAE, manual a través de `GOOGLE_APPLICATION_CREDENTIALS` o programático.  |
| Plataformas Soportadas   | Clientes HTTP en todas partes, gRPC en x86_64, Mac OS X, Windows, Linux; no en Android, Raspberry Pi.|
| Servicio de Ejemplo       | Almacenamiento en la nube: `com.google.cloud.storage`, métodos para listar cubos, gestión de objetos. |

Esta guía completa asegura que los desarrolladores tengan toda la información necesaria para usar `com.google.cloud` en Java de manera efectiva, abordando la configuración, autenticación, uso y características avanzadas, con referencias a fuentes autoritativas para una exploración más profunda.

#### Citaciones Clave
- [Repositorio de GitHub de las bibliotecas de clientes de Java de Google Cloud con código y configuración detallados](https://github.com/googleapis/google-cloud-java)
- [Documentación de Google Cloud para una visión general del desarrollo de Java](https://cloud.google.com/products/anthos)
- [Tutorial de Baeldung sobre el almacenamiento en la nube de Google con ejemplos prácticos de Java](https://www.baeldung.com/java-google-cloud-storage)