---
audio: false
lang: es
layout: post
title: Versión de Servlet en WebSphere Liberty Profile
translated: true
---

### Entendiendo el Error

El mensaje de error de `console.log` indica una `DDParser ParseException` relacionada con el archivo `web-fragment.xml` en el `spring-web-6.2.3.jar`. Específicamente, indica que el descriptor de implementación especifica la versión "50" (que corresponde a Servlet 5.0), pero el servidor WebSphere Liberty Profile (WLP) está actualmente provisionado con la versión "40" (Servlet 4.0). Esta discrepancia ocurre porque:

- **Servlet 5.0** es parte de Jakarta EE 9 y es requerido por versiones más nuevas de Spring Boot (por ejemplo, Spring Boot 3.x, que incluye `spring-web-6.2.3.jar`).
- **Servlet 4.0** es parte de Java EE 8, y WLP probablemente está configurado con la característica `javaee-8.0`, que no soporta Servlet 5.0.

Para solucionar esto, necesitas alinear la versión de Servlet soportada por WLP con la versión requerida por tu aplicación. La solución recomendada es actualizar WLP para soportar Servlet 5.0 habilitando la característica `jakartaee-9.1`.

---

### Solución: Actualizar WLP para Soporte de Servlet 5.0

Aquí está cómo solucionar el problema actualizando WLP para usar la característica `jakartaee-9.1`, que incluye soporte para Servlet 5.0:

#### 1. **Localizar el Archivo `server.xml`**
- El archivo de configuración `server.xml` define las características habilitadas en WLP.
- Generalmente se encuentra en el directorio del servidor, como `/opt/ibm/wlp/usr/servers/myServer/server.xml`, donde `myServer` es el nombre de tu servidor.

#### 2. **Editar el Archivo `server.xml`**
- Abre el archivo `server.xml` en un editor de texto.
- Localiza la sección `<featureManager>`, que enumera las características habilitadas para el servidor. Puede verse algo así:
  ```xml
  <featureManager>
      <feature>javaee-8.0</feature>
  </featureManager>
  ```
- Reemplaza la característica `javaee-8.0` con `jakartaee-9.1` para habilitar el soporte de Servlet 5.0:
  ```xml
  <featureManager>
      <feature>jakartaee-9.1</feature>
  </featureManager>
  ```
- Guarda el archivo.

#### 3. **Aplicar Cambios en Modo de Desarrollo de WLP (Si Aplica)**
- Si estás ejecutando WLP en **modo de desarrollo** (por ejemplo, usando el comando `wlp/bin/server run` o una integración de IDE), puedes aplicar los cambios de la siguiente manera:
  - **Reinicio Manual:**
    - Detén el servidor:
      ```bash
      /opt/ibm/wlp/bin/server stop myServer
      ```
    - Inicia el servidor nuevamente:
      ```bash
      /opt/ibm/wlp/bin/server start myServer
      ```
  - **Recarga en Caliente del Modo de Desarrollo:**
    - Si WLP está ejecutándose en modo de desarrollo (por ejemplo, a través de `server run` o un IDE), puede detectar automáticamente los cambios en `server.xml`. Sin embargo, para asegurarte de que la nueva característica se cargue, se recomienda un reinicio.

#### 4. **Verificar la Solución**
- Después de reiniciar el servidor, vuelve a desplegar tu aplicación (por ejemplo, copiando el archivo WAR al directorio `dropins` o usando tu método de despliegue).
- Verifica los registros del servidor para confirmar el despliegue exitoso. Busca mensajes como:
  ```
  [AUDIT   ] CWWKT0016I: Aplicación web disponible (default_host): http://localhost:9080/myapp/
  ```
  ```
  CWWKZ0001I: Aplicación myapp iniciada en X.XXX segundos.
  ```
- Accede a tu aplicación (por ejemplo, `http://localhost:9080/myapp/`) para confirmar que se está ejecutando sin errores.

---

### Solución Alternativa: Degradar Spring Boot

Si actualizar WLP a `jakartaee-9.1` no es una opción (por ejemplo, debido a restricciones de compatibilidad con otras aplicaciones), puedes degradar tu aplicación Spring Boot a una versión compatible con Servlet 4.0:

#### 1. **Cambiar a Spring Boot 2.7.x**
- Spring Boot 2.7.x soporta Servlet 4.0 (y versiones anteriores como Servlet 3.1).
- Actualiza tu `pom.xml` para usar Spring Boot 2.7.x:
  ```xml
  <parent>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-parent</artifactId>
      <version>2.7.18</version> <!-- Usa la última versión 2.7.x -->
      <relativePath/>
  </parent>
  ```

#### 2. **Reconstruir y Redeploy**
- Reconstruye tu aplicación:
  ```bash
  mvn clean package
  ```
- Vuelve a desplegar el archivo WAR generado en WLP y verifica que se inicie sin errores.

---

### Resumen
- **Causa del Error:** Tu aplicación (`spring-web-6.2.3.jar`) requiere Servlet 5.0, pero WLP está configurado para Servlet 4.0.
- **Solución Preferida:** Actualizar WLP para usar la característica `jakartaee-9.1` modificando `server.xml` y reiniciando el servidor.
- **Solución Alternativa:** Degradar a Spring Boot 2.7.x para coincidir con el soporte de Servlet 4.0 de WLP.

La solución preferida (actualizar WLP) asegura que tu aplicación pueda usar las últimas características de Spring Boot 3.x y Jakarta EE 9. Sigue los pasos anteriores para resolver el problema y desplegar tu aplicación exitosamente.