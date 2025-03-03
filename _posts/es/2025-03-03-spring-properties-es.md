---
audio: false
generated: true
lang: es
layout: post
title: Selección de Archivos de Propiedades en Spring Boot
translated: true
---

En un proyecto Spring Boot Maven, tienes dos archivos de propiedades, `appProperties.properties` y `appProperties-hk.properties`, ubicados en `src/main/resources`. Para controlar qué archivo de propiedades se usa, en particular para especificar el uso de las propiedades `-hk`, puedes aprovechar los mecanismos de configuración de Spring Boot. Aquí te explico cómo hacerlo:

### Solución

1. **Crear un archivo `application.properties`**
   - Por defecto, Spring Boot busca `application.properties` o `application.yml` en `src/main/resources` para cargar la configuración.
   - Para usar tus archivos de propiedades personalizados (`appProperties.properties` y `appProperties-hk.properties`), necesitas informar a Spring Boot que busque archivos con el nombre base `appProperties` en lugar del predeterminado `application`.
   - Agrega la siguiente línea a un nuevo archivo `application.properties` en `src/main/resources`:

     ```properties
     spring.config.name=appProperties
     ```

   - Esta configuración le indica a Spring Boot que cargue `appProperties.properties` como el archivo de configuración base, y también buscará automáticamente variantes específicas del perfil como `appProperties-{profile}.properties` cuando un perfil esté activo.

2. **Usar perfiles de Spring para especificar las propiedades `-hk`**
   - Spring Boot admite perfiles, que permiten cargar archivos de propiedades adicionales o sobrescritos según el perfil activo.
   - Dado que tu archivo se llama `appProperties-hk.properties`, sigue el patrón `appProperties-{profile}.properties`. Aquí, "hk" puede tratarse como un nombre de perfil.
   - Para usar `appProperties-hk.properties`, activa el perfil "hk" al ejecutar tu aplicación. Spring Boot cargará tanto `appProperties.properties` como `appProperties-hk.properties`, con las propiedades en `appProperties-hk.properties` sobrescribiendo cualquier propiedad coincidente en `appProperties.properties`.

3. **Cómo activar el perfil "hk"**
   - **Desde la línea de comandos**: Al ejecutar tu aplicación Spring Boot, especifica el perfil activo usando el argumento `--spring.profiles.active`. Por ejemplo:
     ```bash
     java -jar target/myapp.jar --spring.profiles.active=hk
     ```
     Reemplaza `myapp.jar` con el nombre del archivo JAR de tu aplicación generado por Maven.

   - **Desde Maven**: Si ejecutas la aplicación usando el objetivo `spring-boot:run`, configura el perfil en tu `pom.xml`:
     ```xml
     <plugin>
         <groupId>org.springframework.boot</groupId>
         <artifactId>spring-boot-maven-plugin</artifactId>
         <configuration>
             <profiles>
                 <profile>hk</profile>
             </profiles>
         </configuration>
     </plugin>
     ```
     Luego ejecuta:
     ```bash
     mvn spring-boot:run
     ```

   - **Desde una propiedad del sistema**: Establece el perfil como un argumento de la JVM:
     ```bash
     java -Dspring.profiles.active=hk -jar target/myapp.jar
     ```

   - **Desde una variable de entorno**: Exporta el perfil en tu entorno (por ejemplo, en un sistema tipo Unix):
     ```bash
     export SPRING_PROFILES_ACTIVE=hk
     java -jar target/myapp.jar
     ```

### Cómo funciona
- Con `spring.config.name=appProperties` configurado en `application.properties`, Spring Boot usa `appProperties` como el nombre base para los archivos de configuración.
- Cuando no hay ningún perfil activo, solo se carga `appProperties.properties`.
- Cuando se activa el perfil "hk" (por ejemplo, mediante `--spring.profiles.active=hk`), Spring Boot carga tanto `appProperties.properties` como `appProperties-hk.properties`. Las propiedades definidas en `appProperties-hk.properties` tienen precedencia sobre las de `appProperties.properties` si hay duplicados.

### Pasos finales
- Asegúrate de que tanto `appProperties.properties` como `appProperties-hk.properties` estén en `src/main/resources`.
- Agrega `application.properties` con `spring.config.name=appProperties` a `src/main/resources`.
- Ejecuta tu aplicación con el perfil "hk" activado para usar las propiedades `-hk`.

Este enfoque se alinea con las convenciones de Spring Boot, haciendo que sea una manera típica y sencilla de controlar qué archivo de propiedades se usa en tu proyecto. Para usar específicamente las propiedades `-hk`, simplemente activa el perfil "hk" como se describió anteriormente.