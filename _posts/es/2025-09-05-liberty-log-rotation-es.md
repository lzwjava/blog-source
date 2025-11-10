---
audio: false
generated: true
image: false
lang: es
layout: post
title: Guía de Configuración de Rotación de Registros de Liberty
translated: true
type: note
---

Aquí tienes la versión corta, seguida de ejemplos que puedes pegar en `server.xml`.

### Cómo funciona la rotación de logs en Liberty

*   **Qué rota:** `messages.log` y `trace.log`.
    La rotación puede ser **basada en tamaño** y/o **basada en tiempo**. ([openliberty.io][1])
*   **Qué no rota:** `console.log` (es solo stdout/stderr). En su lugar, puedes reducirla o desactivarla. ([openliberty.io][2], [IBM][3])
*   **Dónde configurar:** el elemento `<logging …/>` en `server.xml`. (También puedes establecer los mismos valores en `bootstrap.properties`/variables de entorno si necesitas que se apliquen *antes* de que se cargue `server.xml`). ([openliberty.io][2])
*   **Logs de acceso:** el log de acceso HTTP tiene sus **propias** configuraciones de rotación basadas en tiempo bajo `httpAccessLogging` / `accessLogging`. ([openliberty.io][4])
*   **Tamaño + tiempo:** Liberty moderno admite la rotación basada en tiempo además de la opción clásica basada en tamaño, por lo que puedes usar una, otra o ambas (excepto para `console.log`). ([IBM][5])

---

### Recetas comunes para `server.xml`

#### 1) Rotación basada en tamaño (clásica)

Mantiene hasta 10 archivos, cada uno de hasta 256 MB.

```xml
<logging
  logDirectory="${server.output.dir}/logs"
  maxFileSize="256"
  maxFiles="10"/>
```

Efecto: cuando `messages.log` o `trace.log` exceda 256 MB, Liberty lo mueve a un archivo con marca de tiempo y mantiene como máximo 10 de esos archivos. (No afecta a `console.log`). ([openliberty.io][1])

#### 2) Rotación basada en tiempo (por ejemplo, diariamente a medianoche)

```xml
<logging
  rolloverStartTime="00:00"
  rolloverInterval="1d"/>
```

Efecto: `messages.log` y `trace.log` se rotan cada día a las 00:00. También puedes usar minutos (`m`) u horas (`h`), por ejemplo, `30m` o `6h`. ([openliberty.io][2])

#### 3) Combinar tamaño + tiempo (producción típica)

```xml
<logging
  logDirectory="${server.output.dir}/logs"
  maxFileSize="256"
  maxFiles="14"
  rolloverStartTime="00:00"
  rolloverInterval="1d"/>
```

Efecto: se rota **cuando ocurra primero** (por tamaño o por horario), y se mantiene un historial de 14 archivos. ([IBM][5])

#### 4) Controlar o desactivar el crecimiento de `console.log`

`console.log` no puede rotar; redúcela o desactívala y confía en `messages.log`.

```xml
<logging
  consoleLogLevel="OFF"
  copySystemStreams="false"/>
```

Notas: desactivar la consola detiene la copia propia de los logs de Liberty a `console.log`, pero la JVM aún puede escribir cosas como `-verbose:gc` en stdout/stderr. ([openliberty.io][2])

#### 5) Ajustes de nombre/formato (opcional)

```xml
<logging
  messageFileName="messages.log"
  traceFileName="trace.log"
  messageFormat="JSON"/>
```

JSON es útil para enviar los logs a un stack de logging; mantén los valores por defecto si no lo necesitas. ([openliberty.io][1])

---

### Log de acceso HTTP (independiente de lo anterior)

Habilita el logging de acceso y rótalo diariamente a medianoche:

```xml
<httpAccessLogging id="accessLogging"
  rolloverStartTime="00:00"
  rolloverInterval="1d"/>

<httpEndpoint id="defaultHttpEndpoint"
  httpPort="9080" httpsPort="9443"
  accessLoggingRef="accessLogging"/>
```

(O coloca `rolloverStartTime`/`rolloverInterval` directamente en un elemento hijo `<accessLogging …/>` de `httpEndpoint`). ([openliberty.io][4])

---

### Lista de verificación rápida

*   Usa **`maxFileSize` + `maxFiles`** para la rotación basada en tamaño. ([openliberty.io][1])
*   Usa **`rolloverStartTime` + `rolloverInterval`** para la rotación basada en tiempo. ([openliberty.io][2])
*   **No esperes que `console.log` rote**; establece `consoleLogLevel="OFF"` y `copySystemStreams="false"` si quieres evitar archivos de consola grandes. ([openliberty.io][2], [IBM][3])

Si compartes tu fragmento actual de `server.xml` o tus objetivos de retención (por ejemplo, "conservar ~7 días" o "limitar a 2 GB"), adaptaré los valores exactos.

[1]: https://openliberty.io/docs/latest/reference/config/logging.html "Logging (logging) :: Open Liberty Docs"
[2]: https://openliberty.io/docs/latest/log-trace-configuration.html "Log and trace configuration :: Open Liberty Docs"
[3]: https://www.ibm.com/support/pages/how-turn-console-logging-prevent-excess-file-growth-and-use-only-message-log-rotation-liberty-profile-or-open-liberty?utm_source=chatgpt.com "How to turn off Console logging, prevent excess file growth ..."
[4]: https://openliberty.io/docs/latest/access-logging.html "HTTP access logging :: Open Liberty Docs"
[5]: https://www.ibm.com/support/pages/how-setup-liberty-log-rollover-both-time-based-and-size-based-options-similar-traditional-websphere-0?utm_source=chatgpt.com "How to setup Liberty Log Rollover with both Time-Based ..."