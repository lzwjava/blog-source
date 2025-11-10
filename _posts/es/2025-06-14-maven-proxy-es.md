---
audio: false
generated: true
lang: es
layout: post
title: Configuración de Proxy de Maven
translated: true
type: note
---

Según la salida de tu comando `checkproxy`, tus proxies HTTP y HTTPS están configurados en `http://127.0.0.1:7890`. A continuación, se muestra el fragmento de configuración actualizado para el archivo `settings.xml` de Maven, para configurar Maven y que utilice estos ajustes de proxy.

### Fragmento de Configuración de Proxy Actualizado para `settings.xml`

Añade o actualiza la sección `<proxies>` en tu archivo `settings.xml` de Maven (ubicado en `~/.m2/settings.xml` o `/usr/share/maven/conf/settings.xml`) con lo siguiente:

```xml
<settings>
  <proxies>
    <proxy>
      <id>http-proxy</id>
      <active>true</active>
      <protocol>http</protocol>
      <host>127.0.0.1</host>
      <port>7890</port>
      <nonProxyHosts>localhost|127.0.0.1</nonProxyHosts>
    </proxy>
    <proxy>
      <id>https-proxy</id>
      <active>true</active>
      <protocol>https</protocol>
      <host>127.0.0.1</host>
      <port>7890</port>
      <nonProxyHosts>localhost|127.0.0.1</nonProxyHosts>
    </proxy>
  </proxies>
</settings>
```

### Explicación del Fragmento
- **`<id>`**: Identificadores únicos (`http-proxy` y `https-proxy`) para cada configuración de proxy.
- **`<active>true</active>`**: Habilita el proxy.
- **`<protocol>`**: Establecido en `http` para el proxy HTTP y `https` para el proxy HTTPS, coincidiendo con la salida de tu `checkproxy`.
- **`<host>127.0.0.1</host>`**: La dirección IP del servidor proxy, como se muestra en tus ajustes de proxy.
- **`<port>7890</port>`**: El número de puerto para ambos proxies, como se especifica.
- **`<nonProxyHosts>localhost|127.0.0.1</nonProxyHosts>`**: Excluye `localhost` y `127.0.0.1` de ser proxyados, lo cual es estándar para evitar problemas con servicios locales.
- **Sin `<username>` o `<password>`**: Dado que la salida de tu proxy no indica autenticación, estos campos se omiten. Si se requiere autenticación, añádelos con tus credenciales.

### Pasos para Aplicar
1. **Abre `settings.xml`**:
   - Si existe `~/.m2/settings.xml`, edítalo (ej. `nano ~/.m2/settings.xml`).
   - Si no existe, créalo o edita el archivo global en `/usr/share/maven/conf/settings.xml` (requiere `sudo`).

2. **Inserta o Actualiza la Sección `<proxies>`**:
   - Si `<proxies>` ya existe, reemplaza o fusiona las entradas `<proxy>` con el fragmento de arriba.
   - Si `<settings>` está vacío o es mínimo, puedes usar el fragmento completo como contenido del archivo.

3. **Guarda y Cierra** el archivo.

### Verificar la Configuración
Ejecuta un comando de Maven que requiera acceso a internet para confirmar que se está usando el proxy:
```bash
cd ~/Projects/blog-server
mvn -X clean checkstyle:check
```

En la salida de depuración (`-X`), busca líneas que indiquen que Maven está usando el proxy (ej. conexiones a `127.0.0.1:7890`). Si el comando descarga dependencias o se completa sin errores de red, el proxy está funcionando.

### Resolución de Problemas
- **El Proxy No Funciona**:
  - Asegúrate de que el servidor proxy en `127.0.0.1:7890` esté en ejecución (ej. prueba con `curl -x http://127.0.0.1:7890 https://repo.maven.apache.org`).
  - Revisa si hay errores tipográficos en el archivo `settings.xml`.
- **El Archivo de Configuración es Ignorado**:
  - Confirma que Maven está leyendo `~/.m2/settings.xml` revisando la salida de depuración para la ruta del archivo.
  - Si estás usando el archivo global, asegúrate de haber editado `/usr/share/maven/conf/settings.xml` correctamente.
- **Se Requiere Autenticación**:
  - Si tu proxy requiere un nombre de usuario y contraseña, añade:
    ```xml
    <username>yourusername</username>
    <password>yourpassword</password>
    ```
    a cada bloque `<proxy>`.

### Nota sobre el Contexto Previo
Tu problema con `checkstyle:check` en el proyecto `blog-server` (relacionado con `checks.xml` y `SuppressWithNearbyTextFilter`) debe resolverse por separado actualizando el `pom.xml` como se sugirió anteriormente (usando `maven-checkstyle-plugin:3.3.1` con Checkstyle `10.17.0` y `<configLocation>${project.basedir}/checks.xml</configLocation>`). Los ajustes de proxy anteriores asegurarán que Maven pueda descargar cualquier artefacto requerido para esa solución.

¡Avísame si encuentras problemas o necesitas ayuda con el `pom.xml` actualizado o con más depuración del proxy!