---
audio: true
generated: true
lang: es
layout: post
title: Despliegue de EAR en WebSphere Liberty Profile
translated: true
---

Parece que has construido con éxito un archivo EAR (Enterprise Archive) utilizando `mvn package` con Maven, y el proceso de construcción se completó sin errores. Sin embargo, al desplegar este EAR en WebSphere Liberty Profile (WLP) e iniciar el servidor, encuentras el error "no module found." Esto es desconcertante porque una construcción fluida generalmente sugiere que todo está en orden, pero el servidor no reconoce tu aplicación como se espera. Desglosemos esto y averigüemos qué podría estar pasando, junto con los pasos para resolverlo.

### Entendiendo el Problema
Un archivo EAR es un archivo estándar de Java EE que empaqueta tu aplicación, generalmente conteniendo uno o más módulos como archivos WAR (para aplicaciones web), archivos JAR (para EJBs o bibliotecas) y un descriptor de despliegue (`application.xml`). Cuando despliegas un EAR en WLP, el servidor debería detectar estos módulos y comenzar la aplicación. El mensaje "no module found" sugiere que WLP no puede encontrar ningún módulo dentro de tu EAR o no los reconoce, impidiendo que la aplicación comience.

Dado que tu construcción de Maven fue exitosa ("todo es fluido"), el problema probablemente radica en una de las tres áreas:
1. **Contenido del archivo EAR**: El EAR podría no contener los módulos esperados, o el descriptor de despliegue podría faltar o estar incorrecto.
2. **Proceso de despliegue**: La forma en que estás desplegando el EAR en WLP podría no alinearse con cómo el servidor espera encontrarlo y procesarlo.
3. **Configuración del servidor**: WLP podría no estar configurado para reconocer los módulos en tu EAR debido a características faltantes o una configuración incorrecta.

Exploremos estas posibilidades y proporcionemos pasos prácticos para diagnosticar y solucionar el problema.

---

### Causas Posibles y Soluciones

#### 1. El Archivo EAR Podría Estar Vacío o Empaquetado Incorrectamente
Aunque la construcción fue exitosa, es posible que tu EAR no contenga ningún módulo (por ejemplo, archivos WAR o JAR) o que el archivo `application.xml`, que le dice al servidor qué módulos están incluidos, falte o esté mal configurado.

- **Por qué sucede**: En un proyecto EAR de Maven, el plugin `maven-ear-plugin` es responsable de ensamblar el EAR. Incluye módulos según la configuración de tu `pom.xml` o dependencias. Si no se especifican módulos, o si las dependencias (como un WAR) no están definidas o resueltas correctamente, el EAR podría estar vacío o carecer de un `application.xml` adecuado.
- **Cómo verificar**:
  - Abre tu archivo EAR (es un archivo ZIP) utilizando una herramienta como `unzip` o ejecuta `jar tf myApp.ear` en la terminal para listar sus contenidos.
  - Busca:
    - Archivos de módulos (por ejemplo, `my-web.war`, `my-ejb.jar`) en la raíz del EAR.
    - Un archivo `META-INF/application.xml`.
  - Dentro de `application.xml`, deberías ver entradas que definan tus módulos, como:
    ```xml
    <?xml version="1.0" encoding="UTF-8"?>
    <application>
        <module>
            <web>
                <web-uri>my-web.war</web-uri>
                <context-root>/myapp</context-root>
            </web>
        </module>
    </application>
    ```
- **Cómo solucionar**:
  - Verifica tu `pom.xml` para el módulo EAR. Asegúrate de haber especificado dependencias para los módulos que deseas incluir, por ejemplo:
    ```xml
    <dependencies>
        <dependency>
            <groupId>com.example</groupId>
            <artifactId>my-web</artifactId>
            <type>war</type>
        </dependency>
    </dependencies>
    ```
  - Configura el `maven-ear-plugin` si es necesario:
    ```xml
    <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-ear-plugin</artifactId>
        <version>3.3.0</version>
        <configuration>
            <modules>
                <webModule>
                    <groupId>com.example</groupId>
                    <artifactId>my-web</artifactId>
                    <contextRoot>/myapp</contextRoot>
                </webModule>
            </modules>
        </configuration>
    </plugin>
    ```
  - Reconstruye con `mvn clean package` y vuelve a verificar los contenidos del EAR.

Si el EAR está vacío o `application.xml` falta o está incorrecto, esto es probablemente la causa raíz. Arreglar la configuración de Maven debería resolverlo.

---

#### 2. Problema con el Método de Despliegue
La forma en que estás desplegando el EAR en WLP también podría ser el problema. WLP admite dos métodos de despliegue principales: el directorio `dropins` y la configuración explícita en `server.xml`.

- **Usando el directorio `dropins`**:
  - Si colocaste el EAR en el directorio `wlp/usr/servers/<serverName>/dropins/`, WLP debería detectarlo y desplegarlo automáticamente.
  - Sin embargo, para archivos EAR, el despliegue automático no siempre funciona como se espera, especialmente si se necesita una configuración adicional (como raíces de contexto).
- **Usando `server.xml`**:
  - Para archivos EAR, a menudo es mejor configurar la aplicación explícitamente en `wlp/usr/servers/<serverName>/server.xml`:
    ```xml
    <server>
        <featureManager>
            <feature>servlet-3.1</feature> <!-- Asegúrate de que las características requeridas estén habilitadas -->
        </featureManager>
        <application id="myApp" name="myApp" type="ear" location="${server.config.dir}/apps/myApp.ear"/>
    </server>
    ```
  - Coloca el EAR en `wlp/usr/servers/<serverName>/apps/` (o ajusta la ruta `location` en consecuencia).
- **Cómo verificar**:
  - Confirma dónde colocaste el EAR y cómo estás iniciando el servidor (por ejemplo, `./bin/server run <serverName>`).
  - Verifica los registros del servidor (por ejemplo, `wlp/usr/servers/<serverName>/logs/console.log` o `messages.log`) para mensajes de despliegue.
- **Cómo solucionar**:
  - Intenta configurar el EAR en `server.xml` como se muestra anteriormente en lugar de confiar en `dropins`.
  - Reinicia el servidor después de realizar cambios: `./bin/server stop <serverName>` seguido de `./bin/server start <serverName>`.

Si el EAR no se registró correctamente con el servidor, esto podría explicar el error.

---

#### 3. Características del Servidor Faltantes
WLP es un servidor ligero que solo carga las características que habilitas en `server.xml`. Si tu EAR contiene módulos que requieren características específicas (por ejemplo, servlets, EJBs) y esas características no están habilitadas, WLP podría no reconocer ni cargar los módulos.

- **Por qué sucede**: Por ejemplo, un archivo WAR necesita la característica `servlet-3.1` (o superior), mientras que un módulo EJB necesita `ejbLite-3.2`. Sin estas, el servidor podría fallar al procesar los módulos.
- **Cómo verificar**:
  - Mira tu `server.xml` y verifica la sección `<featureManager>`.
  - Características comunes incluyen:
    - `<feature>servlet-3.1</feature>` para módulos web.
    - `<feature>ejbLite-3.2</feature>` para módulos EJB.
  - Revisa los registros del servidor para mensajes sobre características faltantes (por ejemplo, "la característica requerida no está instalada").
- **Cómo solucionar**:
  - Agrega las características necesarias a `server.xml` según las necesidades de tu aplicación:
    ```xml
    <featureManager>
        <feature>servlet-3.1</feature>
        <!-- Agrega otras características según sea necesario -->
    </featureManager>
    ```
  - Reinicia el servidor para aplicar los cambios.

Si las características faltan, habilitarlas debería permitir que WLP reconozca los módulos.

---

### Pasos Diagnósticos
Para identificar el problema, sigue estos pasos:

1. **Inspecciona el Archivo EAR**:
   - Ejecuta `jar tf myApp.ear` o descomprímelo.
   - Asegúrate de que contenga tus módulos (por ejemplo, `my-web.war`) y un válido `META-INF/application.xml`.

2. **Verifica la Construcción de Maven**:
   - Revisa el `pom.xml` del módulo EAR para confirmar dependencias y configuración del `maven-ear-plugin`.
   - Ejecuta `mvn clean package` nuevamente y verifica la salida de la construcción para mensajes sobre la inclusión de módulos (por ejemplo, "Agregando módulo my-web.war").

3. **Verifica el Despliegue**:
   - Confirma la ubicación del EAR (por ejemplo, `dropins` o `apps`).
   - Si usas `dropins`, intenta moverlo a `apps` y agregarlo a `server.xml`.

4. **Examina los Registros del Servidor**:
   - Inicia el servidor y verifica `console.log` o `messages.log` para mensajes de error detallados más allá de "no module found."
   - Busca pistas como "la aplicación no contiene ningún módulo" o errores relacionados con características.

5. **Prueba con un EAR Simple**:
   - Crea un EAR básico con un solo archivo WAR utilizando un `pom.xml` conocido y funcionando, y despliégalo en WLP. Si funciona, el problema es específico del empaquetado de tu EAR original.

---

### Causa Más Probable
Dado que tu construcción fue fluida pero WLP informa "no module found," la causa más probable es que **el archivo EAR no contiene ningún módulo** o **el `application.xml` falta o está incorrecto**. Esto podría suceder si tu `pom.xml` no especifica correctamente los módulos para incluir, incluso aunque Maven no marcó un error. Alternativamente, si el EAR es correcto, el problema podría estar en el despliegue (por ejemplo, no configurado en `server.xml`) o en características del servidor faltantes.

### Recomendación Final
- Comienza verificando los contenidos del EAR (`jar tf myApp.ear`) y la configuración de tu `pom.xml`.
- Si el EAR está vacío o carece de `application.xml`, corrige la configuración de Maven y vuelve a construir.
- Si el EAR parece correcto, configúralo en `server.xml`, asegúrate de que las características requeridas estén habilitadas y vuelve a desplegar.
- Verifica los registros del servidor para obtener más contexto.

Siguiendo estos pasos, deberías poder identificar si el problema está en la construcción, el despliegue o la configuración del servidor y hacer que tu aplicación funcione en WLP con éxito. ¡Hazme saber si necesitas ayuda con configuraciones específicas!