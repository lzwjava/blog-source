---
audio: false
generated: true
lang: es
layout: post
title: Uso de ShellJS para Ejecutar Comandos de Shell
translated: true
type: note
---

ShellJS es una biblioteca de JavaScript que proporciona comandos de shell de Unix (como `cp`, `mkdir`, `exec`, etc.) para usar en proyectos de Node.js. Simplifica la escritura de scripts multiplataforma al permitirte ejecutar comandos de shell familiares directamente en JavaScript. Sin embargo, cuando se trata de desarrollo frontend—normalmente referido a código que se ejecuta en el navegador—ShellJS no es aplicable directamente porque depende de las APIs de Node.js, las cuales no están disponibles en el entorno del navegador. A continuación, explicaré por qué este es el caso y cómo aún puedes usar ShellJS efectivamente en el contexto de los flujos de trabajo de desarrollo frontend.

### Por qué ShellJS no puede ejecutarse directamente en el Navegador
- **Dependencia de Node.js**: ShellJS está construido sobre el runtime de Node.js, el cual proporciona APIs para acceso al sistema de archivos, ejecución de procesos y otras operaciones a nivel de sistema. Estas APIs no están disponibles en el navegador debido a su modelo de seguridad aislado (sandboxed).
- **Restricciones de Seguridad del Navegador**: Los navegadores impiden que JavaScript acceda al sistema de archivos local o ejecute comandos arbitrarios para proteger a los usuarios de scripts maliciosos. Dado que comandos de ShellJS como `exec` (para ejecutar procesos externos) o `cp` (para copiar archivos) dependen de estas capacidades, no pueden funcionar en un entorno de navegador.

Como resultado, no puedes usar ShellJS directamente en JavaScript del lado del cliente que se ejecuta en el navegador. Sin embargo, ShellJS aún puede desempeñar un papel valioso en el desarrollo frontend integrándolo en tus procesos de compilación o herramientas de desarrollo, que normalmente se ejecutan en Node.js.

### Cómo usar ShellJS en Flujos de Trabajo de Desarrollo Frontend
Si bien ShellJS no se ejecuta en el navegador, puedes aprovecharlo en scripts basados en Node.js para automatizar tareas que apoyen tu desarrollo frontend. Los proyectos frontend a menudo dependen de herramientas de compilación como Webpack, Gulp o Grunt, que se ejecutan en Node.js y pueden incorporar ShellJS para agilizar los flujos de trabajo. He aquí cómo hacerlo:

#### 1. Instalar ShellJS
Primero, asegúrate de tener Node.js instalado en tu sistema. Luego, añade ShellJS a tu proyecto usando npm o yarn:

```bash
npm install shelljs
```

o

```bash
yarn add shelljs
```

#### 2. Crear un Script de Node.js con ShellJS
Escribe un script que use ShellJS para realizar tareas relevantes para tu proyecto frontend, como copiar archivos, crear directorios o ejecutar herramientas de línea de comandos. Guarda este script como un archivo `.js` (por ejemplo, `build.js`).

He aquí un script de ejemplo que prepara los assets frontend:

```javascript
const shell = require('shelljs');

// Crear un directorio de compilación si no existe
shell.mkdir('-p', 'build');

// Copiar archivos HTML al directorio de compilación
shell.cp('-R', 'src/*.html', 'build/');

// Compilar Sass a CSS
shell.exec('sass src/styles.scss build/styles.css');

// Copiar archivos JavaScript
shell.cp('-R', 'src/*.js', 'build/');
```

- **`shell.mkdir('-p', 'build')`**: Crea un directorio `build`, donde `-p` asegura que no habrá error si ya existe.
- **`shell.cp('-R', 'src/*.html', 'build/')`**: Copia todos los archivos HTML de `src` a `build`, con `-R` para copia recursiva.
- **`shell.exec('sass src/styles.scss build/styles.css')`**: Ejecuta el compilador de Sass para generar CSS.

#### 3. Integrar el Script en tu Flujo de Trabajo
Puedes ejecutar este script de varias maneras:
- **Directamente via Node.js**:
  ```bash
  node build.js
  ```
- **Como un Script de npm**: Añádelo a tu `package.json`:
  ```json
  "scripts": {
    "build": "node build.js"
  }
  ```
  Luego ejecuta:
  ```bash
  npm run build
  ```
- **Con Herramientas de Compilación**: Incorpora ShellJS en herramientas como Gulp. Por ejemplo:
  ```javascript
  const gulp = require('gulp');
  const shell = require('shelljs');

  gulp.task('build', function(done) {
    shell.exec('sass src/styles.scss build/styles.css');
    shell.cp('-R', 'src/*.js', 'build/');
    done();
  });
  ```

#### 4. Casos de Uso en Desarrollo Frontend
ShellJS puede automatizar varias tareas en tu flujo de trabajo frontend:
- **Gestión de Assets**: Copiar imágenes, fuentes u otros archivos estáticos a un directorio de compilación.
- **Procesamiento de CSS/JavaScript**: Ejecutar herramientas como Sass, PostCSS o UglifyJS via `shell.exec`.
- **Testing y Linting**: Ejecutar runners de pruebas o linters (por ejemplo, `shell.exec('eslint src/*.js')`).
- **Preparación para Despliegue**: Empaquetar archivos o limpiar directorios (por ejemplo, `shell.rm('-rf', 'build/*')`).

### Ejemplo: Automatizando un Proceso de Compilación Frontend
Imagina que estás construyendo una aplicación web simple con HTML, Sass y JavaScript. He aquí cómo podrías usar ShellJS para automatizar la compilación:

**Estructura de Directorios**:
```
project/
├── src/
│   ├── index.html
│   ├── styles.scss
│   └── app.js
├── build.js
└── package.json
```

**build.js**:
```javascript
const shell = require('shelljs');

// Limpiar el directorio de compilación
shell.rm('-rf', 'build/*');

// Crear el directorio de compilación
shell.mkdir('-p', 'build');

// Copiar HTML
shell.cp('src/index.html', 'build/');

// Compilar Sass
shell.exec('sass src/styles.scss build/styles.css');

// Copiar JavaScript
shell.cp('src/app.js', 'build/');
```

**package.json**:
```json
{
  "scripts": {
    "build": "node build.js"
  },
  "dependencies": {
    "shelljs": "^0.8.5"
  }
}
```

Ejecuta `npm run build`, y ShellJS preparará tu directorio `build` con los archivos compilados y copiados, listos para el despliegue.

### Puntos Clave
- **No para Uso en el Navegador**: ShellJS no puede ejecutarse en el navegador debido a su dependencia de Node.js y de operaciones a nivel de sistema.
- **Perfecto para Scripts de Compilación**: Úsalo en scripts basados en Node.js para automatizar tareas frontend como manipulación de archivos y ejecución de comandos.
- **Multiplataforma**: ShellJS asegura que tus scripts funcionen consistentemente en Windows, Linux y macOS, haciéndolo ideal para entornos de desarrollo diversos.

Al incorporar ShellJS en tus procesos de compilación impulsados por Node.js, puedes mejorar tu flujo de trabajo de desarrollo frontend con una automatización potente, a pesar de que no se ejecute directamente en el navegador.