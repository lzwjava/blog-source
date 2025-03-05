---
audio: false
generated: true
lang: es
layout: post
title: Usando ShellJS para Ejecutar Comandos de Shell
translated: true
---

ShellJS es una biblioteca de JavaScript que proporciona comandos de shell Unix (como `cp`, `mkdir`, `exec`, etc.) para su uso en proyectos de Node.js. Simplifica la escritura de scripts multiplataforma permitiéndote ejecutar comandos de shell familiares directamente en JavaScript. Sin embargo, cuando se trata del desarrollo frontend—que generalmente se refiere al código que se ejecuta en el navegador—ShellJS no es directamente aplicable porque depende de las APIs de Node.js que no están disponibles en el entorno del navegador. A continuación, explicaré por qué es así y cómo aún puedes usar ShellJS de manera efectiva en el contexto de los flujos de trabajo de desarrollo frontend.

### Por qué ShellJS no puede ejecutarse directamente en el navegador
- **Dependencia de Node.js**: ShellJS se construye sobre el entorno de ejecución de Node.js, que proporciona APIs para el acceso al sistema de archivos, la ejecución de procesos y otras operaciones a nivel del sistema. Estas APIs no están disponibles en el navegador debido a su modelo de seguridad sandbox.
- **Restricciones de seguridad del navegador**: Los navegadores impiden que JavaScript acceda al sistema de archivos local o ejecute comandos arbitrarios para proteger a los usuarios de scripts maliciosos. Dado que los comandos de ShellJS como `exec` (para ejecutar procesos externos) o `cp` (para copiar archivos) dependen de estas capacidades, no pueden funcionar en un entorno de navegador.

Como resultado, no puedes usar ShellJS directamente en JavaScript del lado del cliente que se ejecuta en el navegador. Sin embargo, ShellJS aún puede desempeñar un papel valioso en el desarrollo frontend al integrarlo en tus procesos de construcción o herramientas de desarrollo, que generalmente se ejecutan en Node.js.

### Cómo usar ShellJS en flujos de trabajo de desarrollo frontend
Aunque ShellJS no se ejecuta en el navegador, puedes aprovecharlo en scripts basados en Node.js para automatizar tareas que apoyen tu desarrollo frontend. Los proyectos frontend a menudo dependen de herramientas de construcción como Webpack, Gulp o Grunt, que se ejecutan en Node.js y pueden incorporar ShellJS para optimizar los flujos de trabajo. Aquí te muestro cómo hacerlo:

#### 1. Instalar ShellJS
Primero, asegúrate de tener Node.js instalado en tu sistema. Luego, agrega ShellJS a tu proyecto usando npm o yarn:

```bash
npm install shelljs
```

o

```bash
yarn add shelljs
```

#### 2. Crear un script de Node.js con ShellJS
Escribe un script que use ShellJS para realizar tareas relevantes para tu proyecto frontend, como copiar archivos, crear directorios o ejecutar herramientas de línea de comandos. Guarda este script como un archivo `.js` (por ejemplo, `build.js`).

Aquí tienes un ejemplo de script que prepara los activos frontend:

```javascript
const shell = require('shelljs');

// Crear un directorio de construcción si no existe
shell.mkdir('-p', 'build');

// Copiar archivos HTML al directorio de construcción
shell.cp('-R', 'src/*.html', 'build/');

// Compilar Sass a CSS
shell.exec('sass src/styles.scss build/styles.css');

// Copiar archivos JavaScript
shell.cp('-R', 'src/*.js', 'build/');
```

- **`shell.mkdir('-p', 'build')`**: Crea un directorio `build`, con `-p` asegurando que no haya error si ya existe.
- **`shell.cp('-R', 'src/*.html', 'build/')`**: Copia todos los archivos HTML de `src` a `build`, con `-R` para copiar de manera recursiva.
- **`shell.exec('sass src/styles.scss build/styles.css')`**: Ejecuta el compilador Sass para generar CSS.

#### 3. Integrar el script en tu flujo de trabajo
Puedes ejecutar este script de varias maneras:
- **Directamente a través de Node.js**:
  ```bash
  node build.js
  ```
- **Como un script de npm**: Agregarlo a tu `package.json`:
  ```json
  "scripts": {
    "build": "node build.js"
  }
  ```
  Luego ejecuta:
  ```bash
  npm run build
  ```
- **Con herramientas de construcción**: Incorpora ShellJS en herramientas como Gulp. Por ejemplo:
  ```javascript
  const gulp = require('gulp');
  const shell = require('shelljs');

  gulp.task('build', function(done) {
    shell.exec('sass src/styles.scss build/styles.css');
    shell.cp('-R', 'src/*.js', 'build/');
    done();
  });
  ```

#### 4. Casos de uso en el desarrollo frontend
ShellJS puede automatizar diversas tareas en tu flujo de trabajo frontend:
- **Gestión de activos**: Copiar imágenes, fuentes u otros archivos estáticos a un directorio de construcción.
- **Procesamiento de CSS/JavaScript**: Ejecutar herramientas como Sass, PostCSS o UglifyJS a través de `shell.exec`.
- **Pruebas y linting**: Ejecutar ejecutores de pruebas o linters (por ejemplo, `shell.exec('eslint src/*.js')`).
- **Preparación para implementación**: Agrupar archivos o limpiar directorios (por ejemplo, `shell.rm('-rf', 'build/*')`).

### Ejemplo: Automatizar un proceso de construcción frontend
Imagina que estás construyendo una simple aplicación web con HTML, Sass y JavaScript. Aquí te muestro cómo podrías usar ShellJS para automatizar la construcción:

**Estructura del directorio**:
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

// Limpiar el directorio de construcción
shell.rm('-rf', 'build/*');

// Crear el directorio de construcción
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

Ejecuta `npm run build` y ShellJS preparará tu directorio `build` con los archivos compilados y copiados, listos para la implementación.

### Puntos clave
- **No para uso en el navegador**: ShellJS no puede ejecutarse en el navegador debido a su dependencia de Node.js y operaciones a nivel del sistema.
- **Perfecto para scripts de construcción**: Úsalo en scripts basados en Node.js para automatizar tareas frontend como la manipulación de archivos y la ejecución de comandos.
- **Multiplataforma**: ShellJS asegura que tus scripts funcionen de manera consistente en Windows, Linux y macOS, lo que lo hace ideal para entornos de desarrollo diversos.

Al incorporar ShellJS en tus procesos de construcción impulsados por Node.js, puedes mejorar tu flujo de trabajo de desarrollo frontend con una potente automatización, aunque no se ejecute directamente en el navegador.