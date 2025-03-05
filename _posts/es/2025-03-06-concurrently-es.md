---
audio: false
generated: true
lang: es
layout: post
title: Usando simultáneamente
translated: true
---

Parece que estás preguntando sobre el uso de "concurrently" en el contexto del desarrollo frontend. Sin embargo, "concurrently" es típicamente un paquete de Node.js utilizado para ejecutar múltiples comandos o scripts al mismo tiempo, a menudo en un contexto de flujo de trabajo de backend o desarrollo, en lugar de directamente en el código frontend. ¿Te referías a cómo usarlo en la configuración de un proyecto frontend (por ejemplo, ejecutando scripts) o a algo más como operaciones concurrentes en JavaScript frontend (por ejemplo, promesas, async/await)? Asumiré lo primero por ahora, pero ¡siéntete libre de aclarar!

### Usando `concurrently` en un Proyecto Frontend

Si estás trabajando en un proyecto frontend (por ejemplo, con React, Vue o Angular), `concurrently` se usa comúnmente en el desarrollo para ejecutar múltiples procesos simultáneamente, como iniciar un servidor de desarrollo y un observador de compilación. Aquí te muestro cómo puedes usarlo:

#### 1. Instalar `concurrently`
Primero, instálalo como una dependencia de desarrollo en tu proyecto:
```bash
npm install --save-dev concurrently
```

#### 2. Agregar Scripts a `package.json`
Define los scripts que deseas ejecutar simultáneamente en tu `package.json`. Por ejemplo, si estás ejecutando un servidor de desarrollo frontend y un preprocesador de CSS como Sass:
```json
{
  "scripts": {
    "start:frontend": "react-scripts start", // o tu comando de desarrollo frontend
    "watch:css": "sass --watch src/styles:dist/styles",
    "dev": "concurrently \"npm run start:frontend\" \"npm run watch:css\""
  }
}
```

- `start:frontend`: Ejecuta tu servidor de desarrollo frontend (por ejemplo, React, Vite, etc.).
- `watch:css`: Observa y compila tus archivos CSS.
- `dev`: Usa `concurrently` para ejecutar ambos comandos a la vez.

#### 3. Ejecutar los Scripts Concurrentes
En tu terminal, simplemente ejecuta:
```bash
npm run dev
```
Esto iniciará tanto el servidor frontend como el observador de CSS simultáneamente. Verás la salida de ambos procesos en la misma terminal y `concurrently` los mantendrá ejecutándose juntos.

#### 4. Configuración Opcional
Puedes personalizar `concurrently` con opciones como:
- `--kill-others`: Detiene todos los procesos si uno falla.
- `--names`: Etiqueta cada proceso para una salida más clara.

Ejemplo con opciones en `package.json`:
```json
"dev": "concurrently --names \"Frontend,CSS\" --kill-others \"npm run start:frontend\" \"npm run watch:css\""
```
La salida podría verse así:
```
[Frontend] Iniciando servidor frontend...
[CSS] Observando archivos CSS...
```

#### Caso de Uso en el Flujo de Trabajo Frontend
Imagina que estás construyendo una aplicación React con un servidor API separado:
- Frontend: `npm run start` (servidor de desarrollo de React en el puerto 3000).
- API: `npm run start:api` (por ejemplo, servidor Node.js en el puerto 5000).
Con `concurrently`, puedes ejecutar ambos:
```json
"dev": "concurrently \"npm run start\" \"npm run start:api\""
```

### Si Te Referías a JavaScript Concurrent en el Frontend
Si te referías a manejar operaciones concurrentes en el código frontend (por ejemplo, obtener múltiples APIs a la vez), aquí tienes un ejemplo rápido usando `Promise.all`:
```javascript
async function fetchData() {
  const [userData, postsData] = await Promise.all([
    fetch('https://api.example.com/user').then(res => res.json()),
    fetch('https://api.example.com/posts').then(res => res.json())
  ]);
  console.log(userData, postsData);
}
fetchData();
```
Esto ejecuta las llamadas a la API de manera concurrente y espera a que ambas se resuelvan.

### ¡Aclara Si Es Necesario!
Hazme saber si te referías a algo diferente por "concurrently en frontend", como una biblioteca, un framework o un caso de uso específico, y ¡adaptaré la respuesta en consecuencia!