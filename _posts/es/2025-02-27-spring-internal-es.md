---
audio: false
generated: false
lang: es
layout: post
title: Funcionamiento Interno de Spring
translated: true
---

Vamos a profundizar en Spring y su funcionamiento interno. Spring es un robusto framework para construir aplicaciones Java, y abordaré cada parte de tu consulta paso a paso con explicaciones claras.

### ¿Cómo Funciona Spring?
Spring opera bajo el principio de **Inversión de Control (IoC)**. Esto significa que, en lugar de que tu código de aplicación controle la creación y gestión de objetos, Spring se encarga de ello. Lo hace a través de un componente llamado **contenedor IoC**. El contenedor IoC es responsable de:

- **Instanciar** objetos (llamados beans en Spring).
- **Configurarlos** según tus especificaciones.
- **Ensamblarlos** gestionando sus dependencias.

Este enfoque reduce el acoplamiento estrecho en tu código, haciéndolo más modular y fácil de mantener.

### ¿Cómo Gestiona Spring los Beans?
En Spring, **beans** son los objetos gestionados por el contenedor IoC. Aquí está cómo Spring los maneja:

1. **Definición**: Defines beans ya sea en:
   - **Archivos de configuración XML**.
   - **Configuración basada en Java** usando anotaciones como `@Bean`, `@Component`, `@Service`, etc.
2. **Creación**: Cuando la aplicación comienza, el contenedor IoC lee estas definiciones y crea los beans.
3. **Inyección de Dependencias (DI)**: Spring inyecta automáticamente dependencias (otros beans) en un bean donde sea necesario, usando:
   - **Inyección de constructor**.
   - **Inyección de setter**.
   - **Inyección de campo** (a través de `@Autowired`).

El contenedor gestiona todo el ciclo de vida de estos beans, desde la creación hasta la destrucción, y asegura que estén disponibles cuando se necesiten.

### Diferencia Entre un Servicio y un Controlador
En el contexto de **Spring MVC** (el framework web de Spring), estos dos componentes tienen propósitos distintos:

- **Controlador**:
  - Maneja **solicitudes HTTP** de los usuarios.
  - Procesa la entrada, invoca la lógica de negocio y decide qué **vista** (por ejemplo, una página web) devolver.
  - Anotado con `@Controller` o `@RestController`.
  - Vive en la **capa web**.

- **Servicio**:
  - Encapsula la **lógica de negocio** de la aplicación.
  - Realiza tareas como cálculos, procesamiento de datos o interacción con bases de datos.
  - Anotado con `@Service`.
  - Vive en la **capa de negocio**.

**Ejemplo**:
- Un controlador podría recibir una solicitud para mostrar el perfil de un usuario y llamar a un servicio para obtener los datos del usuario.
- El servicio recupera los datos de una base de datos y los devuelve al controlador, que luego los envía a la vista.

En resumen: **Los controladores gestionan las interacciones web**, mientras que **los servicios manejan la funcionalidad principal**.

### ¿Qué Proporciona Spring?
Spring es un framework integral que ofrece una amplia gama de herramientas para aplicaciones empresariales. Las características clave incluyen:

- **Inyección de Dependencias**: Simplifica la gestión de dependencias de objetos.
- **Programación Orientada a Aspectos (AOP)**: Añade preocupaciones transversales como el registro o la seguridad.
- **Gestión de Transacciones**: Asegura la consistencia de datos a través de operaciones.
- **Spring MVC**: Construye aplicaciones web robustas.
- **Spring Boot**: Simplifica la configuración con valores predeterminados preconfigurados y servidores integrados.
- **Spring Data**: Simplifica el acceso a bases de datos.
- **Seguridad**: Proporciona herramientas de autenticación y autorización.

El diseño modular de Spring te permite elegir solo las características que necesitas.

### ¿Cómo Busca Spring Objetos o Beans?
Cuando una aplicación Spring comienza:

1. El **contenedor IoC** se inicializa.
2. Escanea **definiciones de beans** en:
   - Archivos XML.
   - Clases anotadas (por ejemplo, `@Component`, `@Bean`).
3. El contenedor crea los beans y los almacena en un **mapa**, indexado por nombre o tipo.
4. Cuando se necesita un bean (por ejemplo, para inyección o recuperación directa), el contenedor lo proporciona usando:
   - **Búsqueda por nombre**.
   - **Búsqueda por tipo** (por ejemplo, a través de `@Autowired`).

Este proceso asegura que los beans estén disponibles en toda la aplicación.

### ¿Cómo Usar Tomcat o Netty como Servidor?
Spring Boot, una extensión de Spring, simplifica la configuración del servidor integrando servidores directamente en tu aplicación. Aquí está cómo funciona con **Tomcat** y **Netty**:

- **Tomcat** (Basado en Servlets):
  - Servidor predeterminado en la dependencia `spring-boot-starter-web` de Spring Boot.
  - Añade esto a tu `pom.xml`:
    ```xml
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    ```
  - Spring Boot integra Tomcat, y tu aplicación se ejecuta como un JAR ejecutable independiente.

- **Netty** (No Basado en Servlets):
  - Usado para aplicaciones web reactivas (por ejemplo, con Spring WebFlux).
  - Reemplaza Tomcat excluyéndolo y añadiendo Netty:
    ```xml
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-webflux</artifactId>
    </dependency>
    ```
  - Spring Boot integra Netty en su lugar, soportando E/S asíncronas y no bloqueantes.

Configuras el servidor a través de `application.properties` (por ejemplo, estableciendo el puerto con `server.port=8080`). No se necesita despliegue de servidor externo, Spring Boot lo maneja todo.

### Resumen
- **Núcleo de Spring**: Usa un contenedor IoC para la gestión de objetos.
- **Gestión de Beans**: Definidos mediante XML o anotaciones, con dependencias inyectadas automáticamente.
- **Servicio vs. Controlador**: Los servicios manejan la lógica de negocio; los controladores gestionan las solicitudes web.
- **Características**: Ofrece DI, AOP, soporte web y más.
- **Búsqueda de Beans**: El contenedor encuentra y proporciona beans desde las configuraciones.
- **Servidores**: Spring Boot integra Tomcat o Netty con simples cambios de dependencia.