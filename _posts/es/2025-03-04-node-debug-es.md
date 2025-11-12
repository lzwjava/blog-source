---
audio: false
generated: true
lang: es
layout: post
title: Depuración en Node.js con el Paquete Debug
translated: true
type: note
---

### Puntos Clave
- Es probable que "debug in npm" se refiera al uso del paquete "debug" para logging en proyectos Node.js gestionados por npm.
- La investigación sugiere instalar el paquete con `npm install debug`, y luego usarlo en el código con un namespace como `require('debug')('myapp:component')`.
- La evidencia apunta a habilitar la salida de debug estableciendo la variable de entorno `DEBUG`, por ejemplo `DEBUG=myapp:component npm run start`.

### Instalación y Uso del Paquete Debug
Para usar el paquete "debug" en tu proyecto Node.js, primero instálalo usando npm:
- Ejecuta `npm install debug` en el directorio de tu proyecto.

Luego, en tu código JavaScript, requiere el paquete y crea una instancia de debug con un namespace:
- Ejemplo: `const debug = require('debug')('myapp:component'); debug('algún mensaje');`.

### Habilitar la Salida de Debug
Para ver los mensajes de debug, establece la variable de entorno `DEBUG` al ejecutar tu aplicación:
- Por ejemplo, ejecuta `DEBUG=myapp:component node app.js` o `DEBUG=myapp:component npm run start` si usas un script de npm.

### Controlar los Namespaces
Puedes controlar qué mensajes de debug aparecen usando comodines o exclusiones:
- Habilita múltiples namespaces con `DEBUG=myapp:* node app.js`.
- Excluye namespaces específicos con `DEBUG=*,-myapp:exclude node app.js`.

---

### Nota de Estudio: Exploración Detallada del Uso de Debug en npm

Esta sección proporciona una visión general completa del uso del paquete "debug" dentro de proyectos Node.js gestionados por npm, basada en la documentación y recursos disponibles. El enfoque está en la implementación práctica, características avanzadas y consideraciones para desarrolladores, asegurando una comprensión exhaustiva tanto para principiantes como para usuarios experimentados.

#### Introducción a Debug en el Contexto de npm
La frase "debug in npm" muy probablemente se refiere a utilizar el paquete "debug", una utilidad de depuración ligera para entornos Node.js y navegadores, dentro de proyectos gestionados por npm (Node Package Manager). Dada la prominencia del paquete "debug" en los resultados de búsqueda y su relevancia para el desarrollo en Node.js, esta interpretación se alinea con las necesidades comunes de los desarrolladores para el logging y la depuración en proyectos gestionados por npm. El paquete, actualmente en la versión 4.4.0 según actualizaciones recientes, es ampliamente utilizado, con más de 55,746 otros proyectos en el registro de npm adoptándolo, lo que indica su estatus estándar en el ecosistema.

#### Instalación y Uso Básico
Para comenzar, instala el paquete "debug" usando npm:
- Comando: `npm install debug`
- Esto agrega el paquete a los `node_modules` de tu proyecto y actualiza el `package.json`.

En tu código JavaScript, requiere el paquete e inicialízalo con un namespace para categorizar los mensajes de debug:
- Ejemplo: `const debug = require('debug')('myapp:component');`.
- Usa la instancia de debug para registrar mensajes: `debug('algún mensaje');`.
- El namespace, como 'myapp:component', ayuda a identificar la fuente de los mensajes, facilitando el filtrado de logs en aplicaciones grandes.

Para ver estos mensajes de debug, establece la variable de entorno `DEBUG` al ejecutar tu aplicación:
- Ejemplo: `DEBUG=myapp:component node app.js`.
- Si tu aplicación se inicia mediante un script de npm (ej., `npm run start`), usa: `DEBUG=myapp:component npm run start`.
- Esta variable de entorno controla qué namespaces están habilitados, asegurando una depuración selectiva sin modificar el código.

#### Características Avanzadas y Configuración
El paquete "debug" ofrece varias características avanzadas para una mayor usabilidad:

##### Control de Namespaces y Comodines
- Usa comodines para habilitar múltiples namespaces: `DEBUG=myapp:* node app.js` mostrará mensajes de debug de todos los namespaces que comiencen con 'myapp:'.
- Excluye namespaces específicos usando un signo menos: `DEBUG=*,-myapp:exclude node app.js` habilita todos los namespaces excepto aquellos que comiencen con 'myapp:exclude'.
- Esta depuración selectiva es crucial para enfocarse en partes específicas de una aplicación sin sentirse abrumado por los logs.

##### Codificación de Colores y Análisis Visual
- La salida de debug incluye codificación de colores basada en los nombres de los namespaces, ayudando al análisis visual.
- Los colores están habilitados por defecto cuando stderr es un TTY (terminal) en Node.js, y pueden mejorarse instalando el paquete `supports-color` junto con debug para una paleta de colores más amplia.
- En navegadores, los colores funcionan en inspectores basados en WebKit, Firefox (versión 31 y posteriores) y Firebug, mejorando la legibilidad en las herramientas de desarrollo.

##### Diferencia de Tiempo e Información de Rendimiento
- El paquete puede mostrar la diferencia de tiempo entre las llamadas de debug, prefijada con "+NNNms", útil para el análisis de rendimiento.
- Esta característica se habilita automáticamente y usa `Date#toISOString()` cuando stdout no es un TTY, asegurando consistencia entre entornos.

##### Variables de Entorno y Personalización
Varias variables de entorno ajustan la salida de debug:
| Nombre             | Propósito                              |
|------------------|--------------------------------------|
| DEBUG            | Habilita/deshabilita namespaces          |
| DEBUG_HIDE_DATE  | Oculta la fecha en salida no TTY         |
| DEBUG_COLORS     | Fuerza el uso de color en la salida         |
| DEBUG_DEPTH      | Establece la profundidad de inspección de objetos         |
| DEBUG_SHOW_HIDDEN| Muestra propiedades ocultas en objetos   |

- Por ejemplo, establecer `DEBUG_DEPTH=5` permite una inspección más profunda de objetos, útil para estructuras de datos complejas.

##### Formateadores para Salida Personalizada
Debug admite formateadores personalizados para diferentes tipos de datos, mejorando la legibilidad de los logs:
| Formateador | Representación                      |
|-----------|-------------------------------------|
| %O        | Objeto impreso de forma legible (múltiples líneas)|
| %o        | Objeto impreso de forma legible (una sola línea)   |
| %s        | String                              |
| %d        | Número (entero/flotante)              |
| %j        | JSON, maneja referencias circulares   |
| %%        | Signo de porcentaje simple                 |

- Los formateadores personalizados se pueden extender, ej., `createDebug.formatters.h = (v) => v.toString('hex')` para salida hexadecimal.

#### Integración con Scripts de npm
Para proyectos que usan scripts de npm, integrar debug es sencillo:
- Modifica los scripts en tu `package.json` para incluir configuraciones de debug si es necesario, aunque típicamente, establecer `DEBUG` en tiempo de ejecución es suficiente.
- Ejemplo de script: `"start": "node app.js"`, ejecutado con `DEBUG=myapp:component npm run start`.
- Para usuarios de Windows, usa CMD con `set DEBUG=* & node app.js` o PowerShell con `$env:DEBUG='*';node app.js`, asegurando compatibilidad multiplataforma.

#### Soporte para Navegadores y Casos Especiales
Aunque principalmente para Node.js, debug también admite entornos de navegador:
- Compila con herramientas como Browserify o usa servicios como [browserify-as-a-service](https://wzrd.in/standalone/debug@latest) para inclusión en el lado del cliente.
- Persiste el estado habilitado en navegadores usando `localStorage.debug`, ej., `localStorage.debug = 'worker:*'`.
- Nota: Los navegadores basados en Chromium (Brave, Chrome, Electron) pueden requerir habilitar el nivel de log "Verbose" para toda la funcionalidad.

#### Mejores Prácticas y Consideraciones
- Usa namespaces descriptivos, como "connect:bodyParser", para mantener la claridad en los logs.
- Añade "*" a los namespaces para una depuración siempre habilitada, ej., `DEBUG=connect:*`.
- Para producción, asegúrate de que `DEBUG` no esté establecida para evitar logging innecesario, ya que las declaraciones de debug son silenciosas sin la variable.
- Considera el rendimiento: debug es ligero, registrando solo cuando está habilitado, haciéndolo adecuado para desarrollo sin impactar la producción.

#### Detalle Inesperado: Depurar npm en Sí Mismo
Aunque el enfoque principal es el paquete "debug", vale la pena señalar que "debug in npm" podría malinterpretarse como depurar la herramienta npm (ej., problemas con `npm install`). Para tales casos, usa el flag `--verbose` de npm para una salida detallada, pero esto es distinto a usar el paquete debug. Esta distinción es importante para usuarios que exploran la depuración relacionada con npm, aunque el contexto sugiere que el paquete es más relevante.

#### Conclusión
Usar el paquete "debug" en proyectos Node.js gestionados por npm proporciona una forma robusta y flexible de implementar una depuración selectiva. Al instalar mediante `npm install debug`, requerirlo con namespaces y controlar la salida mediante `DEBUG`, los desarrolladores pueden gestionar los logs de manera eficiente, mejorar la legibilidad con colores y analizar el rendimiento. Este enfoque se alinea con las prácticas de desarrollo modernas, ofreciendo un equilibrio entre detalle y control en los flujos de trabajo de depuración.

**Citas Clave:**
- [debug npm package detailed usage guide](https://www.npmjs.com/package/debug)