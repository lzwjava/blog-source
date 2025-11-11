---
audio: false
generated: true
lang: es
layout: post
title: Usando BrowserSync
translated: true
type: note
---

BrowserSync es una herramienta fantástica para optimizar el desarrollo front-end sincronizando acciones del navegador, recargando archivos automáticamente y proporcionando un servidor de desarrollo local. Aquí tienes una guía paso a paso sobre cómo usar BrowserSync en tu flujo de trabajo front-end:

---

### 1. **Instalar Node.js y npm**
BrowserSync es una herramienta de Node.js, por lo que necesitarás tener Node.js y npm (Node Package Manager) instalados. Si aún no los tienes:
- Descarga e instálalos desde [nodejs.org](https://nodejs.org/).
- Verifica la instalación:
  ```bash
  node -v
  npm -v
  ```

---

### 2. **Instalar BrowserSync**
Puedes instalar BrowserSync globalmente o localmente en tu proyecto.

#### Opción 1: Instalación Global
Ejecuta este comando en tu terminal para instalar BrowserSync globalmente:
```bash
npm install -g browser-sync
```
Esto te permite usar el comando `browser-sync` desde cualquier lugar.

#### Opción 2: Instalación Local (Recomendado para Proyectos)
Si prefieres mantener las dependencias vinculadas a un proyecto específico:
```bash
npm install browser-sync --save-dev
```
Esto agrega BrowserSync a `node_modules` de tu proyecto y lo lista en `package.json`.

---

### 3. **Iniciar BrowserSync**
Dependiendo de tu configuración, puedes usar BrowserSync de diferentes maneras:

#### Uso Básico (Archivos Estáticos)
Si estás trabajando con archivos HTML, CSS y JS estáticos, navega a la carpeta de tu proyecto y ejecuta:
```bash
browser-sync start --server --files "*.html, css/*.css, js/*.js"
```
- `--server`: Ejecuta un servidor local (sirve archivos desde el directorio actual).
- `--files`: Observa estos archivos para detectar cambios y recarga el navegador automáticamente.

Por ejemplo, si la estructura de tu carpeta es:
```
mi-proyecto/
├── index.html
├── css/
│   └── style.css
└── js/
    └── script.js
```
Ejecutar el comando anterior hará lo siguiente:
- Iniciar un servidor en `http://localhost:3000` (puerto predeterminado).
- Abrir tu navegador predeterminado.
- Recargar la página cada vez que `index.html`, `style.css` o `script.js` cambien.

#### Modo Proxy (Servidor Existente)
Si estás usando un servidor backend (por ejemplo, Node.js, PHP o Python), usa la opción de proxy:
```bash
browser-sync start --proxy "http://localhost:8000" --files "*.html, css/*.css, js/*.js"
```
- `--proxy`: Proxy de las solicitudes a tu servidor existente (reemplaza `http://localhost:8000` con la URL de tu servidor).
- BrowserSync superpondrá sus características (como la recarga automática) sobre él.

---

### 4. **Características Principales**
Una vez que BrowserSync esté en ejecución, obtendrás:
- **Recarga en Vivo**: Los cambios en los archivos observados activan una actualización instantánea del navegador.
- **Sincronización Multi-Dispositivo**: El desplazamiento, los clics y las entradas de formularios se sincronizan en todos los dispositivos conectados (por ejemplo, escritorio, teléfono, tableta).
- **Panel de Control UI**: Accede a un panel de control en `http://localhost:3001` (predeterminado) para ajustar configuraciones o detener el servidor.

---

### 5. **Integrar con Herramientas de Build (Opcional)**
Si usas herramientas como Gulp o Webpack, BrowserSync puede integrarse perfectamente.

#### Ejemplo con Gulp
Instala Gulp y BrowserSync:
```bash
npm install --save-dev gulp browser-sync
```
Crea un archivo `gulpfile.js`:
```javascript
const gulp = require('gulp');
const browserSync = require('browser-sync').create();

gulp.task('serve', function() {
  browserSync.init({
    server: './', // Sirve archivos desde el directorio actual
  });

  gulp.watch(['*.html', 'css/*.css', 'js/*.js']).on('change', browserSync.reload);
});

gulp.task('default', gulp.series('serve'));
```
Ejecútalo:
```bash
gulp
```

---

### 6. **Comandos y Opciones Comunes**
- Cambiar puerto: `--port 8080`
- Deshabilitar apertura automática: `--no-open`
- Observar archivos específicos: `--files "ruta/a/archivos/*"`
- Lista completa: Ejecuta `browser-sync --help`

---

### 7. **Solución de Problemas**
- **Puerto en uso**: Cambia el puerto con `--port <número>`.
- **No recarga**: Asegúrate de que las rutas de archivo en `--files` coincidan con la estructura de tu proyecto.
- **Permisos**: Si está instalado globalmente, es posible que necesites `sudo` (por ejemplo, `sudo npm install -g browser-sync` en Linux/macOS).

---

¡Eso es todo! BrowserSync ya está listo para potenciar tu desarrollo front-end. Comienza con el comando básico, ajústalo según sea necesario y disfruta de un flujo de trabajo más fluido. ¡Avísame si necesitas ayuda con una configuración específica!