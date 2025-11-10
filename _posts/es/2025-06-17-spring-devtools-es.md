---
audio: false
generated: true
lang: es
layout: post
title: Herramientas de Desarrollo de Spring Boot para Reinicio Automático
translated: true
type: note
---

Cuando ejecutas una aplicación Spring Boot usando `mvn spring-boot:run`, los observadores de archivos y las capacidades de reinicio automático o recarga en caliente no están habilitados por defecto. Sin embargo, puedes habilitarlas añadiendo la dependencia `spring-boot-devtools` a tu proyecto. Este módulo proporciona características como reinicios automáticos y LiveReload para un desarrollo más rápido.

### Detalles
1. **Comportamiento por Defecto Sin DevTools**:
   - Ejecutar `mvn spring-boot:run` sin `spring-boot-devtools` no incluye observadores de archivos ni reinicio automático. Necesitas detener y reiniciar la aplicación manualmente para aplicar cambios en clases Java, recursos estáticos o plantillas.
   - Los recursos estáticos (por ejemplo, HTML, CSS, JS) pueden requerir una recompilación completa o un reinicio a menos que se configuren de otra manera.

2. **Con `spring-boot-devtools`**:
   - **Observadores de Archivos**: DevTools monitorea el classpath en busca de cambios en archivos Java, propiedades y ciertos recursos (por ejemplo, `/resources`, `/static`, `/templates`).
   - **Reinicio Automático**: Cuando un archivo en el classpath cambia (por ejemplo, una clase Java o un archivo de propiedades), DevTools activa un reinicio automático de la aplicación. Esto es más rápido que un inicio en frío porque usa dos cargadores de clases: uno para bibliotecas de terceros sin cambios (cargador de clases base) y otro para el código de tu aplicación (cargador de clases de reinicio).[](https://docs.spring.io/spring-boot/reference/using/devtools.html)[](https://docs.spring.io/spring-boot/docs/1.5.16.RELEASE/reference/html/using-boot-devtools.html)
   - **LiveReload**: Los cambios en recursos estáticos (por ejemplo, HTML, CSS, JS en `/static`, `/public`, o `/templates`) o plantillas (por ejemplo, Thymeleaf) activan una actualización del navegador en lugar de un reinicio completo, siempre que tengas instalada una extensión de navegador LiveReload (compatible con Chrome, Firefox, Safari).[](https://www.concretepage.com/spring-boot/spring-boot-automatic-restart-using-developer-tools-with-maven)[](https://www.codejava.net/frameworks/spring-boot/spring-boot-auto-reload-changes-using-livereload-and-devtools)
   - **Exclusiones**: Por defecto, los recursos en `/META-INF/maven`, `/META-INF/resources`, `/resources`, `/static`, `/public`, y `/templates` no activan un reinicio pero sí activan un LiveReload. Puedes personalizar esto con `spring.devtools.restart.exclude`.[](https://docs.spring.io/spring-boot/reference/using/devtools.html)

3. **Configuración para DevTools**:
   Añade la siguiente dependencia a tu `pom.xml`:
   ```xml
   <dependency>
       <groupId>org.springframework.boot</groupId>
       <artifactId>spring-boot-devtools</artifactId>
       <scope>runtime</scope>
       <optional>true</optional>
   </dependency>
   ```
   - El `<optional>true</optional>` asegura que DevTools no se incluya en las builds de producción.[](https://www.concretepage.com/spring-boot/spring-boot-automatic-restart-using-developer-tools-with-maven)
   - Ejecuta la aplicación con `mvn spring-boot:run`. DevTools habilitará automáticamente la observación de archivos y el reinicio automático.

4. **Comportamiento en IDEs**:
   - **Eclipse**: Guardar cambios (Ctrl+S) activa automáticamente una build, que DevTools detecta y reinicia la aplicación.[](https://docs.spring.io/spring-boot/docs/1.5.7.RELEASE/reference/html/howto-hotswapping.html)
   - **IntelliJ IDEA**: Necesitas activar manualmente una build (Ctrl+F9 o "Make Project") para que DevTools detecte los cambios, a menos que configures la build automática. Alternativamente, habilita "Build project automatically" en la configuración de IntelliJ para reinicios sin problemas.[](https://www.codejava.net/frameworks/spring-boot/spring-boot-auto-restart-and-live-reload-in-intellij-idea)
   - Para LiveReload, instala la extensión del navegador desde http://livereload.com/extensions/ y habilítala.[](https://www.codejava.net/frameworks/spring-boot/spring-boot-auto-reload-changes-using-livereload-and-devtools)

5. **Alternativa: Spring Loaded**:
   - En lugar de DevTools, puedes usar Spring Loaded para un intercambio en caliente más avanzado (por ejemplo, cambios en la firma de métodos). Añádelo al `spring-boot-maven-plugin`:
     ```xml
     <plugin>
         <groupId>org.springframework.boot</groupId>
         <artifactId>spring-boot-maven-plugin</artifactId>
         <dependencies>
             <dependency>
                 <groupId>org.springframework</groupId>
                 <artifactId>springloaded</artifactId>
                 <version>1.2.8.RELEASE</version>
             </dependency>
         </dependencies>
     </plugin>
     ```
   - Spring Loaded está menos recomendado que DevTools, ya que no se mantiene tan activamente y puede no ser compatible con todos los frameworks.[](https://docs.spring.io/spring-boot/docs/1.5.7.RELEASE/reference/html/howto-hotswapping.html)[](https://docs.spring.io/spring-boot/docs/1.5.16.RELEASE/reference/html/howto-hotswapping.html)

6. **Recarga en Caliente de Recursos Estáticos**:
   - Sin DevTools, puedes habilitar la recarga en caliente de recursos estáticos estableciendo la propiedad `addResources` del `spring-boot-maven-plugin`:
     ```xml
     <plugin>
         <groupId>org.springframework.boot</groupId>
         <artifactId>spring-boot-maven-plugin</artifactId>
         <configuration>
             <addResources>true</addResources>
         </configuration>
     </plugin>
     ```
   - Esto añade `src/main/resources` al classpath, permitiendo la edición in situ de archivos estáticos, pero es menos completo que DevTools.[](https://docs.spring.io/spring-boot/maven-plugin/run.html)

7. **Advertencias**:
   - DevTools puede causar problemas de carga de clases en proyectos multi-módulo. Si esto sucede, intenta deshabilitar el reinicio con `spring.devtools.restart.enabled=false` o usa JRebel para una recarga avanzada.[](https://docs.spring.io/spring-boot/reference/using/devtools.html)
   - Para archivos que no están en el classpath, usa `spring.devtools.restart.additional-paths` para monitorear directorios adicionales.[](https://docs.spring.io/spring-boot/docs/1.5.16.RELEASE/reference/html/using-boot-devtools.html)
   - LiveReload requiere una extensión del navegador y puede no funcionar para todas las configuraciones front-end (por ejemplo, React con Webpack).[](https://stackoverflow.com/questions/49888724/hot-reload-for-spring-boot-backend-frontend)
   - Si los reinicios son lentos, ajusta `spring.devtools.restart.poll-interval` y `spring.devtools.restart.quiet-period` para optimizar la observación de archivos.[](https://docs.spring.io/spring-boot/reference/using/devtools.html)

### Pasos para una Aplicación Simple
1. Crea una aplicación básica de Spring Boot (por ejemplo, usando Spring Initializr con `spring-boot-starter-web`).
2. Añade la dependencia `spring-boot-devtools` al `pom.xml`.
3. Ejecuta `mvn spring-boot:run`.
4. Modifica un archivo Java, un archivo de propiedades o un recurso estático (por ejemplo, HTML en `src/main/resources/static`).
5. Observa el reinicio automático (para Java/propiedades) o la actualización del navegador (para recursos estáticos con LiveReload habilitado).

### Ejemplo
Para una aplicación simple con un controlador REST:
```java
@RestController
public class HelloController {
    @GetMapping("/hello")
    public String hello() {
        return "Hello, World!";
    }
}
```
- Añade DevTools, ejecuta `mvn spring-boot:run`, y cambia el valor de retorno del método `hello()`. La aplicación se reiniciará automáticamente.
- Añade un `index.html` en `src/main/resources/static`, instala la extensión LiveReload, y modifica el HTML. El navegador se actualizará sin un reinicio.

### Conclusión
Para una aplicación Spring Boot simple, añadir `spring-boot-devtools` es la forma más fácil de habilitar observadores de archivos, reinicio automático y recarga en caliente. Usa `mvn spring-boot:run` con DevTools para una experiencia de desarrollo fluida. Si necesitas un intercambio en caliente más avanzado, considera Spring Loaded o JRebel, pero DevTools es suficiente para la mayoría de los casos.[](https://www.geeksforgeeks.org/hot-reload-with-spring-boot-devtools/)[](https://docs.spring.io/spring-boot/how-to/hotswapping.html)

---

A continuación se muestra un ejemplo de cómo configurar `spring-boot-devtools` para la observación de archivos, el reinicio automático y la recarga en caliente en tu aplicación Spring Boot usando un archivo `application.yml`. Esta configuración está adaptada a tu proyecto `blog-server`, basada en los registros que proporcionaste, que muestran que DevTools está activo y monitoreando `target/classes`.

### Configuración `application.yml`
```yaml
spring:
  devtools:
    restart:
      # Habilitar reinicio automático (por defecto: true)
      enabled: true
      # Directorios adicionales para monitorear en busca de reinicios (por ejemplo, carpeta de configuración personalizada)
      additional-paths:
        - /home/lzw/Projects/blog-server/config
      # Archivos/directorios a excluir para activar reinicios (se mantienen las exclusiones por defecto)
      exclude: static/**,public/**,templates/**,logs/**,generated/**
      # Intervalo de sondeo para cambios de archivos (en milisegundos, por defecto: 1000)
      poll-interval: 1000
      # Período de silencio después de cambios de archivos antes de reiniciar (en milisegundos, por defecto: 400)
      quiet-period: 400
      # Opcional: Archivo para activar reinicios manualmente
      trigger-file: .restart
    livereload:
      # Habilitar LiveReload para la actualización del navegador en cambios de recursos estáticos (por defecto: true)
      enabled: true
```

### Explicación de la Configuración
- **`spring.devtools.restart.enabled`**: Habilita el reinicio automático cuando cambian los archivos del classpath (por ejemplo, `target/classes`, como se ve en tu registro: `file:/home/lzw/Projects/blog-server/target/classes/`).
- **`spring.devtools.restart.additional-paths`**: Monitorea directorios adicionales (por ejemplo, `/home/lzw/Projects/blog-server/config`) en busca de cambios para activar reinicios.
- **`spring.devtools.restart.exclude`**: Previene reinicios por cambios en los directorios `static/`, `public/`, `templates/`, `logs/`, o `generated/`, mientras permite LiveReload para recursos estáticos (por ejemplo, HTML, CSS, JS).
- **`spring.devtools.restart.poll-interval`**: Establece la frecuencia con la que DevTools verifica los cambios de archivos (1000ms = 1 segundo).
- **`spring.devtools.restart.quiet-period`**: Espera 400ms después de detectar un cambio para asegurarse de que no hay más cambios pendientes antes de reiniciar.
- **`spring.devtools.restart.trigger-file`**: Permite reinicios manuales actualizando `.restart` (por ejemplo, `touch /home/lzw/Projects/blog-server/.restart`).
- **`spring.devtools.livereload.enabled`**: Habilita el servidor LiveReload, que activa actualizaciones del navegador para cambios en `static/` o `templates/` (requiere una extensión de navegador LiveReload).

### Pasos para Aplicar
1. Crea o actualiza `src/main/resources/application.yml` con la configuración anterior.
2. Asegúrate de que `spring-boot-devtools` esté en tu `pom.xml`:
   ```xml
   <dependency>
       <groupId>org.springframework.boot</groupId>
       <artifactId>spring-boot-devtools</artifactId>
       <scope>runtime</scope>
       <optional>true</optional>
   </dependency>
   ```
3. Ejecuta `mvn spring-boot:run`. DevTools monitoreará `target/classes` y `/home/lzw/Projects/blog-server/config` (si se añade), reiniciando la aplicación ante cambios en archivos Java o de propiedades y actualizando el navegador ante cambios en recursos estáticos.
4. Para LiveReload, instala una extensión del navegador (por ejemplo, desde http://livereload.com/extensions/) o integra un cliente LiveReload en tu front-end.

### Notas
- Tus registros muestran un inicio rápido (0.8 segundos), por lo que el `poll-interval` y `quiet-period` por defecto deberían estar bien. Ajústalos (por ejemplo, `poll-interval: 500`) si los reinicios se sienten lentos en un proyecto más grande.
- Si no necesitas LiveReload (por ejemplo, usando un servidor de desarrollo front-end separado), establece `livereload.enabled: false`.
- Para reinicios manuales, crea `.restart` en la raíz de tu proyecto y actualízalo cuando sea necesario.

Esta configuración YAML debería funcionar perfectamente con tu configuración, mejorando las características de observación de archivos y reinicio automático que ya estás viendo.