---
audio: false
generated: true
lang: es
layout: post
title: Usando Chokidar para Vigilancia de Archivos
translated: true
---

Chokidar es una biblioteca de Node.js diseñada principalmente para la vigilancia de archivos en el lado del servidor, por lo que su uso directo en el frontend (es decir, en un entorno de navegador) no es su caso de uso típico. El navegador no tiene acceso directo al sistema de archivos como Node.js, por lo que Chokidar es más adecuado para entornos de backend o de tiempo de construcción. Sin embargo, si estás trabajando en un proyecto donde usas un bundler como Webpack, Vite o Parcel en una configuración de desarrollo, o si estás construyendo una aplicación Electron (que combina Node.js con un frontend), podrías aprovechar Chokidar indirectamente. Permíteme aclarar cómo podrías abordar esto según el contexto.

### Por qué Chokidar no se ejecuta directamente en el navegador
- Chokidar depende de las APIs de Node.js como `fs` (sistema de archivos) para vigilar archivos, que no están disponibles en un entorno de navegador.
- El código frontend se ejecuta en un entorno sandbox (el navegador), donde el acceso al sistema de archivos está restringido por razones de seguridad.

### Escenarios posibles para usar Chokidar en un contexto de "frontend"
Aquí te muestro cómo podrías usar Chokidar de una manera que se relacione con el desarrollo frontend:

#### 1. **Durante el desarrollo con una herramienta de construcción**
Si estás preguntando sobre el uso de Chokidar para vigilar archivos (por ejemplo, para recarga en caliente o actualizaciones en vivo) durante el desarrollo frontend, lo integrarías en tu proceso de construcción en lugar del tiempo de ejecución del navegador.

Ejemplo con un script de Node.js personalizado:
```javascript
const chokidar = require('chokidar');

// Vigilar cambios en tus archivos de origen frontend
chokidar.watch('./src/**/*.{html,js,css}').on('all', (event, path) => {
  console.log(event, path);
  // Disparar una reconstrucción o notificar a tu servidor de desarrollo frontend aquí
});
```
- **Caso de uso**: Podrías emparejar esto con una conexión WebSocket para enviar actualizaciones al navegador durante el desarrollo.
- **Herramientas**: Combínalo con algo como `esbuild` o un servidor de desarrollo (por ejemplo, Vite ya tiene vigilancia de archivos incorporada, pero podrías personalizarla con Chokidar).

#### 2. **En una aplicación Electron**
Si tu "frontend" es parte de una aplicación Electron, puedes usar Chokidar en el proceso principal (Node.js) y comunicar los cambios al proceso de renderizado (frontend).

Ejemplo:
```javascript
// main.js (Proceso principal de Electron)
const { ipcMain } = require('electron');
const chokidar = require('chokidar');

chokidar.watch('./files').on('change', (path) => {
  ipcMain.send('file-changed', path); // Enviar evento al renderizado
});
```
```javascript
// renderer.js (Frontend)
const { ipcRenderer } = require('electron');

ipcRenderer.on('file-changed', (event, path) => {
  console.log(`Archivo cambiado: ${path}`);
  // Actualizar la interfaz de usuario en consecuencia
});
```

#### 3. **Frontend con un proxy de backend**
Si estás construyendo una aplicación web y quieres funcionalidad de vigilancia de archivos, ejecutarías Chokidar en un backend de Node.js y enviarías actualizaciones al frontend a través de WebSockets o eventos enviados por el servidor.

Ejemplo (Backend con Express y WebSocket):
```javascript
const express = require('express');
const WebSocket = require('ws');
const chokidar = require('chokidar');

const app = express();
const server = app.listen(3000);
const wss = new WebSocket.Server({ server });

chokidar.watch('./public').on('change', (path) => {
  wss.clients.forEach((client) => {
    if (client.readyState === WebSocket.OPEN) {
      client.send(`Archivo cambiado: ${path}`);
    }
  });
});
```
Frontend (Ejemplo de React):
```javascript
const socket = new WebSocket('ws://localhost:3000');
socket.onmessage = (event) => {
  console.log(event.data); // "Archivo cambiado: ..."
  // Actualizar el estado o la interfaz de usuario
};
```

### Instalación
Para usar Chokidar en cualquiera de estas configuraciones, primero lo instalarías en tu proyecto de Node.js:
```bash
npm install chokidar
```

### Métodos clave de Chokidar
- `chokidar.watch(path, [options])`: Comenzar a vigilar un archivo o directorio.
- Eventos: `.on('add', callback)`, `.on('change', callback)`, `.on('unlink', callback)`, `.on('all', (event, path) => {})`.
- Opciones: `{ ignored: /node_modules/, persistent: true }` (personaliza según sea necesario).

### Si te referías a otra cosa
Si no estás trabajando con un entorno de Node.js en absoluto y quieres un comportamiento similar a la vigilancia de archivos puramente en el navegador (por ejemplo, vigilar cambios en `<input type="file">`), házmelo saber. Eso implicaría la API `File` y oyentes de eventos, no Chokidar.

¿Cuál es tu configuración específica o objetivo? ¡Puedo adaptarlo más!