---
audio: false
generated: true
image: false
lang: es
layout: post
title: Soluciones para problemas del complemento Maven Tomcat
translated: true
type: note
---

Acertaste con la pista clave en tu propio log:

> `[INFO] Skipping non-war project`

Nada se inició porque **el plugin tomcat7-maven-plugin solo ejecuta aplicaciones web empaquetadas como WAR** con la estructura clásica `src/main/webapp`. Es casi seguro que tu proyecto está empaquetado como JAR en este momento, así que el plugin simplemente finaliza después de la compilación.

Hay un segundo problema: estás ejecutando **Tomcat 11** (APIs de Jakarta `jakarta.*`), pero tus dependencias son **Spring 5.2.x** (usa `javax.*`). Esa incompatibilidad significa que incluso si Tomcat se iniciara, un despliegue simple en Tomcat 11 fallaría sin una migración. Usa Tomcat 9 (javax) para Spring 5, o actualiza la aplicación a Spring 6/Jakarta para Tomcat 10/11.

Aquí tienes opciones claras que puedes elegir—elige una y funcionará:

### Opción 1 — Mantener Spring 5, ejecutar localmente con el plugin Jetty (la más rápida)

No se necesita WAR; buena para desarrollo.

1. Añade el plugin:

   ```xml
   <plugin>
     <groupId>org.eclipse.jetty</groupId>
     <artifactId>jetty-maven-plugin</artifactId>
     <version>9.4.54.v20240208</version>
   </plugin>
   ```
2. Ejecuta:

   ```bash
   mvn jetty:run -Djetty.port=8080
   ```

Esto usa `javax.*`, que coincide con Spring 5.

### Opción 2 — Mantener Spring 5, construir un WAR y usar el plugin Tomcat7

1. En `pom.xml` establece el empaquetado WAR:

   ```xml
   <packaging>war</packaging>
   ```
2. Asegúrate de que existe la estructura webapp:

   ```
   src/main/webapp/
   src/main/webapp/WEB-INF/web.xml   # opcional si tienes un inicializador de Servlet 3
   ```
3. (Opcional) Añade configuración al plugin:

   ```xml
   <plugin>
     <groupId>org.apache.tomcat.maven</groupId>
     <artifactId>tomcat7-maven-plugin</artifactId>
     <version>2.2</version>
     <configuration>
       <path>/</path>
       <port>8080</port>
     </configuration>
   </plugin>
   ```
4. Ejecuta:

   ```bash
   mvn tomcat7:run            # para webapp explotada
   # o
   mvn package && mvn tomcat7:run-war
   ```

### Opción 3 — Mantener Spring 5, desplegar en un Tomcat 9 independiente

Esto coincide con `javax.*` sin cambiar el código.

```bash
brew install tomcat@9
/opt/homebrew/opt/tomcat@9/bin/catalina start
```

Construye y coloca tu WAR en `.../tomcat@9/libexec/webapps/`.

### Opción 4 — Actualizar la aplicación a Spring 6/Jakarta, usar Tomcat 11

Si quieres un Tomcat moderno:

* Actualiza a Spring Framework 6.x / Spring Boot 3.x.
* Cambia los imports de `javax.*` a `jakarta.*`.
* Entonces Tomcat 10/11 funcionará bien.

---

#### Por qué `mvn tomcat7:run` mostró éxito pero "no pasó nada"

* Las fases de Maven se completaron exitosamente, pero el plugin detectó un **empaquetado que no es WAR**, por lo que **no inició** un Tomcat embebido. Eso es exactamente lo que significa "Skipping non-war project".

---

Si me dices qué opción prefieres, te daré el `pom.xml` exacto y los archivos mínimos para esa configuración (incluyendo un controlador pequeño y cómo acceder a él en `http://localhost:8080/hello`).