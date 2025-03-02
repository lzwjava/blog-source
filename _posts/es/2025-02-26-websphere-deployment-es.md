---
audio: true
generated: false
lang: es
layout: post
title: Solucionar problemas de implementación en WebSphere Liberty Profile
translated: true
---

Cuando intentas acceder a tu aplicación Spring Boot en `http://localhost:9080/myapp/` y encuentras un error de "context root not found" en WebSphere Liberty Profile (WLP), esto indica que WLP no ha desplegado tu aplicación bajo la raíz de contexto esperada (`/myapp`). Este problema suele surgir debido a problemas con la configuración de despliegue, la configuración del servidor o el archivo WAR en sí. A continuación se presenta una guía exhaustiva para solucionar y resolver este problema.

---

### Comprender el Problema
El error "context root not found" significa que WLP no puede encontrar una aplicación desplegada en `/myapp`. Normalmente, cuando colocas un archivo WAR llamado `myapp.war` en el directorio `dropins` de WLP, debería desplegarse automáticamente con la raíz de contexto `/myapp`, haciéndolo accesible en `http://localhost:9080/myapp/`. Dado que esto no está sucediendo, necesitamos investigar por qué falló el despliegue.

---

### Pasos de Solución de Problemas

#### 1. **Verificar los Registros del Servidor para Mensajes de Despliegue**
El primer paso es confirmar si WLP ha desplegado tu aplicación.

- **Localizar los Registros:**
  - Si tu servidor se llama `myServer`, verifica los registros en:
    ```
    /opt/ibm/wlp/usr/servers/myServer/logs/messages.log
    ```
    o
    ```
    /opt/ibm/wlp/usr/servers/myServer/logs/console.log
    ```
  - Si estás utilizando el servidor predeterminado, reemplaza `myServer` con `defaultServer`.

- **Buscar Confirmación de Despliegue:**
  - Deberías ver un mensaje como:
    ```
    [AUDIT   ] CWWKT0016I: Web application available (default_host): http://localhost:9080/myapp/
    ```
    Esto indica que la aplicación está desplegada y disponible.
  - Además, busca:
    ```
    CWWKZ0001I: Application myapp started in X.XXX seconds.
    ```
    Esto confirma que la aplicación ha iniciado correctamente.

- **Qué Hacer:**
  - Si estos mensajes están ausentes, la aplicación no se ha desplegado. Busca cualquier mensaje `ERROR` o `WARNING` en los registros que pueda indicar por qué (por ejemplo, características faltantes, permisos de archivo o fallos de inicio).
  - Si ves registros de inicio de Spring Boot (por ejemplo, el banner de Spring Boot), la aplicación se está cargando y el problema podría estar con la raíz de contexto o el mapeo de URL.

#### 2. **Verificar la Ubicación y Permisos del Archivo WAR**
Asegúrate de que el archivo WAR esté correctamente colocado en el directorio `dropins` y sea accesible para WLP.

- **Verificar la Ruta:**
  - Para un servidor llamado `myServer`, el archivo WAR debería estar en:
    ```
    /opt/ibm/wlp/usr/servers/myServer/dropins/myapp.war
    ```
  - Si usas `defaultServer`, ajusta en consecuencia:
    ```
    /opt/ibm/wlp/usr/servers/defaultServer/dropins/myapp.war
    ```

- **Verificar Permisos:**
  - Asegúrate de que el proceso WLP tenga permisos de lectura para el archivo. En un sistema Unix-like, ejecuta:
    ```bash
    ls -l /opt/ibm/wlp/usr/servers/myServer/dropins/myapp.war
    ```
    El archivo debería ser legible por el usuario que ejecuta WLP (por ejemplo, `rw-r--r--`).

- **Qué Hacer:**
  - Si el archivo está ausente o mal colocado, cópialo al directorio `dropins` correcto:
    ```bash
    cp target/myapp.war /opt/ibm/wlp/usr/servers/myServer/dropins/
    ```
  - Corrige los permisos si es necesario:
    ```bash
    chmod 644 /opt/ibm/wlp/usr/servers/myServer/dropins/myapp.war
    ```

#### 3. **Confirmar la Supervisión de `dropins` en `server.xml`**
El directorio `dropins` de WLP está habilitado por defecto, pero configuraciones personalizadas podrían deshabilitarlo.

- **Verificar `server.xml`:**
  - Abre el archivo de configuración del servidor:
    ```
    /opt/ibm/wlp/usr/servers/myServer/server.xml
    ```
  - Busca el elemento `applicationMonitor`:
    ```xml
    <applicationMonitor updateTrigger="polled" pollingRate="5s" dropins="dropins" />
    ```
    Esto confirma que WLP supervisa el directorio `dropins` cada 5 segundos en busca de nuevas aplicaciones.

- **Qué Hacer:**
  - Si está ausente, agrega la línea anterior dentro de las etiquetas `<server>` o asegúrate de que ninguna configuración de anulación deshabilite `dropins`.
  - Reinicia el servidor después de los cambios:
    ```bash
    /opt/ibm/wlp/bin/server stop myServer
    /opt/ibm/wlp/bin/server start myServer
    ```

#### 4. **Asegurarse de que las Características Requeridas Estén Habilitadas**
WLP requiere características específicas para desplegar un archivo WAR de Spring Boot, como el soporte de Servlet.

- **Verificar `server.xml`:**
  - Verifica la sección `featureManager` incluye:
    ```xml
    <featureManager>
        <feature>javaee-8.0</feature>
    </featureManager>
    ```
    La característica `javaee-8.0` incluye Servlet 4.0, que es compatible con Spring Boot. Alternativamente, al menos `servlet-4.0` debería estar presente.

- **Qué Hacer:**
  - Si está ausente, agrega la característica y reinicia el servidor.

#### 5. **Validar la Estructura del Archivo WAR**
Un archivo WAR corrupto o estructurado incorrectamente podría impedir el despliegue.

- **Inspeccionar el WAR:**
  - Descomprime el archivo WAR para verificar su contenido:
    ```bash
    unzip -l myapp.war
    ```
  - Busca:
    - `WEB-INF/classes/com/example/demo/HelloController.class` (tu clase de controlador).
    - `WEB-INF/lib/` que contiene dependencias de Spring Boot (por ejemplo, `spring-web-x.x.x.jar`).

- **Qué Hacer:**
  - Si la estructura es incorrecta, vuelve a construir el WAR:
    ```bash
    mvn clean package
    ```
    Asegúrate de que tu `pom.xml` establezca `<packaging>war</packaging>` y marque `spring-boot-starter-tomcat` como `<scope>provided</scope>`.

#### 6. **Despliegue Alternativo a través del Directorio `apps`**
Si `dropins` falla, intenta desplegar la aplicación explícitamente a través del directorio `apps`.

- **Pasos:**
  - Mueve el archivo WAR:
    ```bash
    mv /opt/ibm/wlp/usr/servers/myServer/dropins/myapp.war /opt/ibm/wlp/usr/servers/myServer/apps/
    ```
  - Edita `server.xml` para agregar:
    ```xml
    <application id="myapp" name="myapp" type="war" location="${server.config.dir}/apps/myapp.war">
        <context-root>/myapp</context-root>
    </application>
    ```
  - Reinicia el servidor:
    ```bash
    /opt/ibm/wlp/bin/server restart myServer
    ```

- **Probar de Nuevo:**
  - Accede a `http://localhost:9080/myapp/`. Si funciona, el problema estaba con `dropins`.

#### 7. **Verificar el Estado del Servidor**
Asegúrate de que el servidor esté funcionando correctamente.

- **Verificar el Estado:**
  ```bash
  /opt/ibm/wlp/bin/server status myServer
  ```
  - Si está detenido, arráncalo:
    ```bash
    /opt/ibm/wlp/bin/server start myServer
    ```

- **Probar WLP por Sí Mismo:**
  - Visita `http://localhost:9080/`. Si WLP está funcionando, verás una página de bienvenida (a menos que esté anulada). Si esto falla, hay un problema más amplio con el servidor.

---

### Resolución
Para solucionar el error "context root not found":

1. **Comienza Aquí:**
   - Verifica los registros del servidor (`messages.log` o `console.log`) para mensajes de despliegue o errores.
   - Asegúrate de que `myapp.war` esté en el directorio `dropins` con los permisos adecuados.

2. **Próximos Pasos:**
   - Verifica que `server.xml` habilite la característica `javaee-8.0` y supervise `dropins`.
   - Si no se resuelve, despliega a través del directorio `apps` con una configuración `<application>` explícita en `server.xml`.

3. **Verificación Final:**
   - Después de realizar cambios, reinicia WLP y accede a `http://localhost:9080/myapp/`. Deberías ver "Hello World!" si el despliegue tiene éxito.

Siguiendo estos pasos, identificarás si el problema radica en la configuración del servidor, la ubicación del WAR o el archivo WAR en sí, y lo resolverás en consecuencia.