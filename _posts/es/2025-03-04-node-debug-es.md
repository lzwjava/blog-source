---
audio: false
generated: true
lang: es
layout: post
title: Depuración en Node.js con el paquete Debug
translated: true
---

### Puntos Clave
- Parece probable que "debug in npm" se refiera a usar el paquete "debug" para el registro en proyectos de Node.js gestionados por npm.
- La investigación sugiere instalar el paquete con `npm install debug`, luego usarlo en el código con un espacio de nombres como `require('debug')('myapp:component')`.
- La evidencia indica que se habilita la salida de depuración configurando la variable de entorno `DEBUG`, como `DEBUG=myapp:component npm run start`.

### Instalación y Uso del Paquete Debug
Para usar el paquete "debug" en tu proyecto de Node.js, primero instálalo usando npm:
- Ejecuta `npm install debug` en tu directorio de proyecto.

Luego, en tu código JavaScript, requiere el paquete y crea una instancia de depuración con un espacio de nombres:
- Ejemplo: `const debug = require('debug')('myapp:component'); debug('some message');`.

### Habilitando la Salida de Depuración
Para ver los mensajes de depuración, establece la variable de entorno `DEBUG` al ejecutar tu aplicación:
- Por ejemplo, ejecuta `DEBUG=myapp:component node app.js` o `DEBUG=myapp:component npm run start` si usas un script de npm.

### Controlando Espacios de Nombres
Puedes controlar qué mensajes de depuración aparecen usando comodines o exclusiones:
- Habilita múltiples espacios de nombres con `DEBUG=myapp:* node app.js`.
- Excluye espacios de nombres específicos con `DEBUG=*,-myapp:exclude node app.js`.

---

### Nota de Encuesta: Exploración Detallada del Uso de Debug en npm

Esta sección proporciona una visión general exhaustiva del uso del paquete "debug" dentro de proyectos de Node.js gestionados por npm, basada en la documentación y recursos disponibles. El enfoque está en la implementación práctica, características avanzadas y consideraciones para desarrolladores, asegurando una comprensión exhaustiva tanto para principiantes como para usuarios experimentados.

#### Introducción a Debug en el Contexto de npm
La frase "debug in npm" probablemente se refiere a utilizar el paquete "debug", una utilidad de depuración ligera para entornos de Node.js y navegadores, dentro de proyectos gestionados por npm (Node Package Manager). Dada la prominencia del paquete "debug" en los resultados de búsqueda y su relevancia para el desarrollo de Node.js, esta interpretación coincide con las necesidades comunes de los desarrolladores para el registro y la depuración en proyectos gestionados por npm. El paquete, actualmente en la versión 4.4.0 según las actualizaciones recientes, es ampliamente utilizado, con más de 55,746 otros proyectos en el registro de npm adoptándolo, lo que indica su estado estándar en el ecosistema.

#### Instalación y Uso Básico
Para comenzar, instala el paquete "debug" usando npm:
- Comando: `npm install debug`
- Esto añade el paquete a `node_modules` de tu proyecto y actualiza `package.json`.

En tu código JavaScript, requiere el paquete e inicialízalo con un espacio de nombres para categorizar los mensajes de depuración:
- Ejemplo: `const debug = require('debug')('myapp:component');`.
- Usa la instancia de depuración para registrar mensajes: `debug('some message');`.
- El espacio de nombres, como 'myapp:component', ayuda a identificar la fuente de los mensajes, haciendo que sea más fácil filtrar los registros en aplicaciones grandes.

Para ver estos mensajes de depuración, establece la variable de entorno `DEBUG` al ejecutar tu aplicación:
- Ejemplo: `DEBUG=myapp:component node app.js`.
- Si tu aplicación se inicia a través de un script de npm (por ejemplo, `npm run start`), usa: `DEBUG=myapp:component npm run start`.
- Esta variable de entorno controla qué espacios de nombres están habilitados, asegurando una depuración selectiva sin modificar el código.

#### Características Avanzadas y Configuración
El paquete "debug" ofrece varias características avanzadas para una mayor usabilidad:

##### Control de Espacios de Nombres y Comodines
- Usa comodines para habilitar múltiples espacios de nombres: `DEBUG=myapp:* node app.js` mostrará mensajes de depuración de todos los espacios de nombres que comiencen con 'myapp:'.
- Excluye espacios de nombres específicos usando un signo menos: `DEBUG=*,-myapp:exclude node app.js` habilita todos los espacios de nombres excepto aquellos que comiencen con 'myapp:exclude'.
- Esta depuración selectiva es crucial para enfocarse en partes específicas de una aplicación sin ser abrumado por los registros.

##### Codificación de Colores y Análisis Visual
- La salida de depuración incluye codificación de colores basada en los nombres de los espacios de nombres, ayudando en el análisis visual.
- Los colores están habilitados por defecto cuando stderr es un TTY (terminal) en Node.js, y pueden ser mejorados instalando el paquete `supports-color` junto con debug para una paleta de colores más amplia.
- En navegadores, los colores funcionan en inspectores basados en WebKit, Firefox (versión 31 y posteriores) y Firebug, mejorando la legibilidad en las herramientas de desarrollo.

##### Diferencia de Tiempo y Perspectivas de Rendimiento
- El paquete puede mostrar la diferencia de tiempo entre las llamadas de depuración, prefijada con "+NNNms", útil para el análisis de rendimiento.
- Esta característica está habilitada automáticamente y usa `Date#toISOString()` cuando stdout no es un TTY, asegurando la consistencia en todos los entornos.

##### Variables de Entorno y Personalización
Varias variables de entorno afinan la salida de depuración:
| Nombre             | Propósito                              |
|------------------|--------------------------------------|
| DEBUG            | Habilita/deshabilita espacios de nombres          |
| DEBUG_HIDE_DATE  | Oculta la fecha en la salida no TTY         |
| DEBUG_COLORS     | Fuerza el uso de colores en la salida         |
| DEBUG_DEPTH      | Establece la profundidad de inspección de objetos         |
| DEBUG_SHOW_HIDDEN| Muestra propiedades ocultas en objetos   |

- Por ejemplo, establecer `DEBUG_DEPTH=5` permite una inspección más profunda de objetos, útil para estructuras de datos complejas.

##### Formateadores para Salida Personalizada
Debug soporta formateadores personalizados para diferentes tipos de datos, mejorando la legibilidad de los registros:
| Formateador | Representación                      |
|-----------|-------------------------------------|
| %O        | Impresión bonita de Objeto (múltiples líneas)|
| %o        | Impresión bonita de Objeto (una línea)   |
| %s        | Cadena                              |
| %d        | Número (entero/flotante)              |
| %j        | JSON, maneja referencias circulares   |
| %%        | Signo de porcentaje único                 |

- Los formateadores personalizados pueden ser extendidos, por ejemplo, `createDebug.formatters.h = (v) => v.toString('hex')` para salida hexadecimal.

#### Integración con Scripts de npm
Para proyectos que usan scripts de npm, la integración de debug es sin problemas:
- Modifica tus scripts de `package.json` para incluir configuraciones de debug si es necesario, aunque generalmente, establecer `DEBUG` en tiempo de ejecución es suficiente.
- Ejemplo de script: `"start": "node app.js"`, ejecuta con `DEBUG=myapp:component npm run start`.
- Para usuarios de Windows, usa CMD con `set DEBUG=* & node app.js` o PowerShell con `$env:DEBUG='*';node app.js`, asegurando la compatibilidad entre plataformas.

#### Soporte para Navegadores y Casos de Borde
Aunque principalmente para Node.js, debug también soporta entornos de navegadores:
- Compila con herramientas como Browserify o usa servicios como [browserify-as-a-service](https://wzrd.in/standalone/debug@latest) para la inclusión del lado del cliente.
- Persiste el estado habilitado en navegadores usando `localStorage.debug`, por ejemplo, `localStorage.debug = 'worker:*'`.
- Nota: Los navegadores basados en Chromium (Brave, Chrome, Electron) pueden requerir habilitar el nivel de registro "Verbose" para la funcionalidad completa.

#### Mejores Prácticas y Consideraciones
- Usa espacios de nombres descriptivos, como "connect:bodyParser", para mantener la claridad en los registros.
- Añade "*" a los espacios de nombres para la depuración siempre habilitada, por ejemplo, `DEBUG=connect:*`.
- Para producción, asegúrate de que `DEBUG` no esté configurado para evitar el registro innecesario, ya que las declaraciones de depuración están en silencio sin la variable.
- Considera el rendimiento: debug es ligero, registrando solo cuando está habilitado, haciendo que sea adecuado para el desarrollo sin impactar la producción.

#### Detalle Inesperado: Depurar npm Mismo
Aunque el enfoque principal es el paquete "debug", vale la pena señalar que "debug in npm" podría ser malinterpretado como depurar la herramienta npm (por ejemplo, problemas con `npm install`). Para tales casos, usa la bandera `--verbose` de npm para obtener una salida detallada, pero esto es distinto de usar el paquete debug. Esta distinción es importante para los usuarios que exploran la depuración relacionada con npm, aunque el contexto sugiere que el paquete es más relevante.

#### Conclusión
Usar el paquete "debug" en proyectos de Node.js gestionados por npm proporciona una manera robusta y flexible de implementar la depuración selectiva. Al instalarlo mediante `npm install debug`, requerirlo con espacios de nombres y controlar la salida mediante `DEBUG`, los desarrolladores pueden gestionar eficientemente los registros, mejorar la legibilidad con colores y analizar el rendimiento. Este enfoque se alinea con las prácticas de desarrollo modernas, ofreciendo un equilibrio entre detalle y control en los flujos de trabajo de depuración.

**Citas Clave:**
- [Guía detallada de uso del paquete debug npm](https://www.npmjs.com/package/debug)