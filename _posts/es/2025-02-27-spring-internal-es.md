---
audio: false
generated: true
lang: es
layout: post
title: Funcionamiento Interno de Spring
translated: true
type: note
---

Adentrémonos en Spring y su funcionamiento interno. Spring es un framework robusto para construir aplicaciones Java, y abordaré cada parte de tu consulta paso a paso con explicaciones claras.

### ¿Cómo funciona Spring?
Spring opera bajo el principio de **Inversión de Control (IoC)**. Esto significa que, en lugar de que tu código de aplicación controle la creación y gestión de objetos, Spring se hace cargo. Lo hace a través de un componente llamado **contenedor IoC**. El contenedor IoC es responsable de:

- **Instanciar** objetos (llamados beans en Spring).
- **Configurarlos** según tus especificaciones.
- **Ensamblarlos** gestionando sus dependencias.

Este enfoque reduce el acoplamiento fuerte en tu código, haciéndolo más modular y fácil de mantener.

### ¿Cómo gestiona Spring los Beans?
En Spring, los **beans** son los objetos gestionados por el contenedor IoC. Así es como Spring los maneja:

1. **Definición**: Puedes definir beans en:
   - **Archivos de configuración XML**.
   - **Configuración basada en Java** usando anotaciones como `@Bean`, `@Component`, `@Service`, etc.
2. **Creación**: Cuando la aplicación inicia, el contenedor IoC lee estas definiciones y crea los beans.
3. **Inyección de Dependencias (DI)**: Spring inyecta automáticamente las dependencias (otros beans) en un bean donde se necesite, usando:
   - **Inyección por constructor**.
   - **Inyección por setter**.
   - **Inyección de campo** (vía `@Autowired`).

El contenedor gestiona todo el ciclo de vida de estos beans—desde la creación hasta la destrucción—y se asegura de que estén disponibles cuando se requieran.

### Diferencia entre un Service y un Controller
En el contexto de **Spring MVC** (el framework web de Spring), estos dos componentes tienen propósitos distintos:

- **Controller**:
  - Maneja **solicitudes HTTP** de los usuarios.
  - Procesa la entrada, invoca la lógica de negocio y decide qué **vista** (por ejemplo, una página web) devolver.
  - Se anota con `@Controller` o `@RestController`.
  - Reside en la **capa web**.

- **Service**:
  - Encapsula la **lógica de negocio** de la aplicación.
  - Realiza tareas como cálculos, procesamiento de datos o interacción con bases de datos.
  - Se anota con `@Service`.
  - Reside en la **capa de negocio**.

**Ejemplo**:
- Un controlador podría recibir una solicitud para mostrar el perfil de un usuario y llamar a un servicio para obtener los datos del usuario.
- El servicio recupera los datos de una base de datos y se los devuelve al controlador, que luego los envía a la vista.

En resumen: **Los controladores gestionan las interacciones web**, mientras que **los servicios manejan la funcionalidad central**.

### ¿Qué proporciona Spring?
Spring es un framework integral que ofrece una amplia gama de herramientas para aplicaciones empresariales. Las características clave incluyen:

- **Inyección de Dependencias**: Simplifica la gestión de dependencias de objetos.
- **Programación Orientada a Aspectos (AOP)**: Añade preocupaciones transversales como registro de eventos o seguridad.
- **Gestión de Transacciones**: Asegura la consistencia de los datos en las operaciones.
- **Spring MVC**: Construye aplicaciones web robustas.
- **Spring Boot**: Simplifica la configuración con valores predefinidos y servidores embebidos.
- **Spring Data**: Agiliza el acceso a bases de datos.
- **Seguridad**: Proporciona herramientas de autenticación y autorización.

El diseño modular de Spring te permite elegir solo las características que necesitas.

### ¿Cómo busca Spring objetos o beans?
Cuando una aplicación Spring inicia:

1. El **contenedor IoC** se inicializa.
2. Escanea en busca de **definiciones de bean** en:
   - Archivos XML.
   - Clases anotadas (por ejemplo, `@Component`, `@Bean`).
3. El contenedor crea los beans y los almacena en un **mapa**, indexado por nombre o tipo.
4. Cuando se necesita un bean (por ejemplo, para inyección o recuperación directa), el contenedor lo proporciona usando:
   - **Búsqueda por nombre**.
   - **Búsqueda por tipo** (por ejemplo, vía `@Autowired`).

Este proceso asegura que los beans estén disponibles en toda la aplicación.

### ¿Cómo usar Tomcat o Netty como servidor?
Spring Boot, una extensión de Spring, simplifica la configuración del servidor integrando servidores directamente en tu aplicación. Así es como funciona con **Tomcat** y **Netty**:

- **Tomcat** (Basado en Servlet):
  - Servidor por defecto en la dependencia `spring-boot-starter-web` de Spring Boot.
  - Añade esto a tu `pom.xml`:
    ```xml
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    ```
  - Spring Boot integra Tomcat, y tu aplicación se ejecuta como un JAR ejecutable independiente.

- **Netty** (No Basado en Servlet):
  - Se usa para aplicaciones web reactivas (por ejemplo, con Spring WebFlux).
  - Reemplaza a Tomcat excluyéndolo y añadiendo Netty:
    ```xml
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-webflux</artifactId>
    </dependency>
    ```
  - Spring Boot integra Netty en su lugar, soportando E/S asíncrona y no bloqueante.

Puedes configurar el servidor mediante `application.properties` (por ejemplo, estableciendo el puerto con `server.port=8080`). No se necesita implementación en un servidor externo—Spring Boot lo maneja todo.

### Resumen
- **Núcleo de Spring**: Utiliza un contenedor IoC para la gestión de objetos.
- **Gestión de Beans**: Se definen vía XML o anotaciones, con dependencias inyectadas automáticamente.
- **Service vs. Controller**: Los servicios manejan la lógica de negocio; los controladores gestionan las solicitudes web.
- **Características**: Ofrece DI, AOP, soporte web y más.
- **Búsqueda de Beans**: El contenedor encuentra y proporciona beans a partir de las configuraciones.
- **Servidores**: Spring Boot integra Tomcat o Netty con simples cambios de dependencia.