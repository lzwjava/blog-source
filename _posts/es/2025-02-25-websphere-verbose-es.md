---
audio: true
lang: es
layout: post
title: Registro detallado en WebSphere Liberty Server
translated: true
---

Para abordar su consulta sobre la opción de registro detallado para el comando del servidor en WebSphere Liberty Profile (WLP), aclaremos qué hace el comando `server` y cómo se puede controlar la verbosidad.

El comando `server` en WLP se utiliza para gestionar instancias del servidor, con acciones como `start`, `stop`, `run` o `status`. Por ejemplo:

- `server start <serverName>` inicia el servidor en segundo plano, con la salida redirigida a archivos de registro (por ejemplo, `logs/console.log`).
- `server run <serverName>` inicia el servidor en primer plano, mostrando la salida directamente en la terminal.

Su pregunta se refiere a una "opción de registro detallado" para el comando `server`, lo que podría implicar una salida más detallada del propio comando o un registro más detallado del servidor que gestiona. Después de explorar las opciones, está claro que el comando `server` no tiene una bandera directa como `--verbose` o `-v` para aumentar su propia verbosidad de salida. En su lugar, la verbosidad se refiere al comportamiento de registro del servidor, que se puede influir al invocar el comando.

### Habilitar Registro Detallado
En WLP, la verbosidad de los registros se controla a través de la configuración de registro del servidor, no directamente mediante una bandera del comando `server`. Aquí está cómo puede habilitar el registro detallado:

#### 1. **Configurar el Registro en `server.xml`**
La forma principal de habilitar el registro detallado es ajustando el elemento `<logging>` en el archivo `server.xml` del servidor, que generalmente se encuentra en `<WLP_HOME>/usr/servers/<serverName>/`. Puede establecer una especificación de rastreo detallada para aumentar la verbosidad de los registros. Por ejemplo:

```xml
<logging traceSpecification="*=all" />
```

- `*=all` habilita todos los puntos de rastreo, haciendo que los registros sean extremadamente detallados (útil para la depuración).
- Para una verbosidad más dirigida, puede especificar componentes, por ejemplo, `*=info:com.example.*=debug`, estableciendo el nivel predeterminado en `info` pero `debug` para el paquete `com.example`.

Otros atributos útiles incluyen:
- `logLevel`: Establece el nivel general de registro (por ejemplo, `INFO`, `DEBUG`, `TRACE`).
- `consoleLogLevel`: Controla el nivel de mensajes escritos en `console.log` o la terminal (por ejemplo, `DEBUG` o `TRACE`).

Ejemplo con un nivel de consola más fino:
```xml
<logging consoleLogLevel="DEBUG" traceSpecification="*=audit" />
```

Cuando ejecuta `server start`, los registros (incluida la salida detallada) van a `logs/console.log`. Con `server run`, esta salida detallada aparece directamente en su terminal.

#### 2. **Usar Variables de Entorno**
También puede controlar la verbosidad del registro mediante variables de entorno, que anulan o complementan las configuraciones de `server.xml`. Por ejemplo, establezca la variable `WLP_LOGGING_CONSOLE_LOGLEVEL` antes de ejecutar el comando `server`:

```bash
export WLP_LOGGING_CONSOLE_LOGLEVEL=DEBUG
server start <serverName>
```

- Esto establece el nivel de registro de la consola en `DEBUG`, asegurando una salida más detallada.
- Los niveles válidos incluyen `INFO`, `DEBUG`, `FINE`, `FINER`, `FINEST`, etc.

Para `server run`, esto hará que la salida de la terminal sea más detallada; para `server start`, afecta `console.log`.

#### 3. **Opciones Detalladas Específicas de JVM**
Si está interesado en salidas detalladas específicas como los registros de recolección de basura, puede agregar opciones de JVM (aunque esto está relacionado con el tiempo de ejecución del servidor, no con el propio comando `server`). Agregue `-verbose:gc` al archivo `jvm.options` en `<WLP_HOME>/usr/servers/<serverName>/`, o inclúyalo a través de `server.xml`:

```xml
<jvmEntries verbose="gc" />
```

Esto genera registros relacionados con la recolección de basura, generalmente en `console.log` o en la terminal con `server run`.

### Cómo Esto Se Relaciona con el Comando `server`
- **No Hay Opción Directa `--verbose`**: El comando `server` (por ejemplo, `server start`) no tiene una opción `--verbose` o similar para detallar sus pasos de ejecución más allá de los mensajes de estado básicos (por ejemplo, "Servidor iniciado").
- **El Registro del Servidor Controla la Verbosidad**: La verbosidad que ve depende de la configuración de registro del servidor. Use `server run` para observar los registros en vivo en la terminal, o verifique los archivos de registro después de `server start`.

Por ejemplo:
- Con `<logging traceSpecification="*=all"/>` en `server.xml`, ejecutar `server run <serverName>` inunda la terminal con registros detallados.
- Con `server start <serverName>`, la misma verbosidad aparece en `logs/console.log`.

### Recomendación
Para lograr un registro detallado al usar el comando `server`:
1. Edite `server.xml` para incluir una especificación de rastreo detallada (por ejemplo, `*=all` para máxima verbosidad o un nivel específico como `*=debug`).
2. Alternativamente, establezca `WLP_LOGGING_CONSOLE_LOGLEVEL=DEBUG` en su entorno.
3. Use `server run` para ver la salida detallada directamente, o `server start` y verifique `logs/console.log`.

Este enfoque asegura que obtenga los registros detallados que necesita, adaptados a sus requisitos de depuración o monitoreo.

Si se refería a algo más específico (por ejemplo, verbosidad de ejecución del comando en lugar de registros del servidor), ¡siéntase libre de aclarar! De lo contrario, configurar el registro del servidor como se describió es la forma estándar de habilitar el registro detallado con el comando `server` en WLP.