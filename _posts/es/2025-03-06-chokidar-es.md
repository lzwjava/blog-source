---
audio: false
generated: true
lang: es
layout: post
title: Uso de Chokidar para la Observación de Archivos
translated: true
type: note
---

Chokidar es una librería de Node.js diseñada principalmente para la observación de archivos en el lado del servidor, por lo que usarla directamente en el frontend (es decir, en un entorno de navegador) no es su caso de uso típico. El navegador no tiene acceso directo al sistema de archivos como lo tiene Node.js, razón por la cual Chokidar es más adecuado para entornos de backend o de construcción. Sin embargo, si estás trabajando en un proyecto donde usas un bundler como Webpack, Vite o Parcel en una configuración de desarrollo, o si estás construyendo una aplicación Electron (que combina Node.js con un frontend), podrías aprovechar Chokidar indirectamente. Permíteme aclarar cómo podrías abordar esto según el contexto.

### Por qué Chokidar no se ejecuta directamente en el Navegador
- Chokidar depende de APIs de Node.js como `fs` (sistema de archivos) para observar archivos, las cuales no están disponibles en un entorno de navegador.
- El código del frontend se ejecuta en un entorno aislado (el navegador), donde el acceso al sistema de archivos está restringido por razones de seguridad.

### Escenarios Posibles para Usar Chokidar en un Contexto de "Frontend"
Aquí se explica cómo podrías usar Chokidar de una manera relacionada con el desarrollo frontend:

#### 1. **Durante el Desarrollo con una Herramienta de Construcción**
Si te refieres a usar Chokidar para observar archivos (por ejemplo, para recarga en caliente o actualizaciones en vivo) durante el desarrollo frontend, lo integrarías en tu proceso de construcción, no en el tiempo de ejecución del navegador.

Ejemplo con un script personalizado de Node.js:
```javascript
const chokidar = require('chokidar');

// Observar cambios en los archivos fuente de tu frontend
chokidar.watch('./src/**/*.{html,js,css}').on('all', (event, path) => {
  console.log(event, path);
  // Activar una reconstrucción o notificar a tu servidor de desarrollo frontend aquí
});
```
- **Caso de Uso**: Podrías combinar esto con una conexión WebSocket para enviar actualizaciones al navegador durante el desarrollo.
- **Herramientas**: Combínalo con algo como `esbuild` o un servidor de desarrollo (por ejemplo, Vite ya tiene la observación de archivos integrada, pero podrías personalizarla con Chokidar).

#### 2. **En una Aplicación Electron**
Si tu "frontend" es parte de una aplicación Electron, puedes usar Chokidar en el proceso principal (Node.js) y comunicar los cambios al proceso de renderizado (frontend).

Ejemplo:
```javascript
// main.js (Proceso principal de Electron)
const { ipcMain } = require('electron');
const chokidar = require('chokidar');

chokidar.watch('./files').on('change', (path) => {
  ipcMain.send('file-changed', path); // Enviar evento al renderizador
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

#### 3. **Frontend con un Proxy en el Backend**
Si estás construyendo una aplicación web y deseas funcionalidad de observación de archivos, ejecutarías Chokidar en un backend de Node.js y enviarías las actualizaciones al frontend mediante WebSockets o Server-Sent Events.

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
Frontend (ejemplo con React):
```javascript
const socket = new WebSocket('ws://localhost:3000');
socket.onmessage = (event) => {
  console.log(event.data); // "Archivo cambiado: ..."
  // Actualizar el estado o la interfaz de usuario
};
```

### Instalación
Para usar Chokidar en cualquiera de estas configuraciones, primero debes instalarlo en tu proyecto de Node.js:
```bash
npm install chokidar
```

### Métodos Clave de Chokidar
- `chokidar.watch(path, [options])`: Comienza a observar un archivo o directorio.
- Eventos: `.on('add', callback)`, `.on('change', callback)`, `.on('unlink', callback)`, `.on('all', (event, path) => {})`.
- Opciones: `{ ignored: /node_modules/, persistent: true }` (personalizar según sea necesario).

### Si Querías Decir Otra Cosa
Si no estás trabajando con un entorno Node.js en absoluto y deseas un comportamiento similar a la observación de archivos puramente en el navegador (por ejemplo, observar cambios en `<input type="file">), ¡avísame! Eso involucraría la API `File` y detectores de eventos, no Chokidar.

¿Cuál es tu configuración u objetivo específico? ¡Puedo adaptar esto aún más!