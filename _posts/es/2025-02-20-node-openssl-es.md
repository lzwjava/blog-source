---
audio: false
generated: false
lang: es
layout: post
title: Compatibilidad de Node.js con OpenSSL
translated: true
type: note
---

Al ejecutar `ng build` con **Node.js 22.9.0** y **npm 10.8.3**, encuentras el error:

```
error 0308010C digital envelope routines::unsupported
```

Este error normalmente surge debido a un problema de compatibilidad entre versiones más recientes de Node.js (como la 22.9.0, que utiliza OpenSSL 3.0 o posterior) y ciertos algoritmos criptográficos en los que confían herramientas como Webpack, que Angular utiliza internamente. A continuación, se presenta una guía paso a paso para solucionar este problema.

---

### Solución

#### Paso 1: Habilitar el Proveedor Legacy de OpenSSL
La solución más simple e inmediata es habilitar el proveedor legacy de OpenSSL configurando la variable de entorno `NODE_OPTIONS`. Esto permite a Node.js utilizar algoritmos criptográficos más antiguos que pueden no ser compatibles por defecto en OpenSSL 3.0+.

- **Para macOS/Linux**:
  Abre tu terminal y ejecuta:
  ```bash
  export NODE_OPTIONS=--openssl-legacy-provider
  ng build
  ```

- **Para Windows (Símbolo del sistema)**:
  Abre el Símbolo del sistema y ejecuta:
  ```cmd
  set NODE_OPTIONS=--openssl-legacy-provider
  ng build
  ```

- **Para Windows (PowerShell)**:
  Abre PowerShell y ejecuta:
  ```powershell
  $env:NODE_OPTIONS="--openssl-legacy-provider"
  ng build
  ```

Después de configurar la variable de entorno, ejecuta `ng build` nuevamente. Esto debería resolver el error en la mayoría de los casos al permitir que Node.js procese las rutinas no compatibles.

---

#### Paso 2: Verificar y Actualizar Angular CLI (Si es Necesario)
Si el error persiste después del Paso 1, es posible que tu versión de Angular CLI no sea totalmente compatible con Node.js 22.9.0. Actualizarla a la última versión puede ayudar.

- Verifica tu versión actual de Angular CLI:
  ```bash
  ng --version
  ```

- Actualiza Angular CLI globalmente:
  ```bash
  npm install -g @angular/cli
  ```

- Luego, intenta ejecutar `ng build` nuevamente.

---

#### Paso 3: Verificar y Actualizar las Dependencias del Proyecto (Opcional)
Si el problema aún no se resuelve, dependencias desactualizadas en tu proyecto podrían estar causándolo. Para abordar esto:

- Abre tu archivo `package.json` y revisa las versiones de tus dependencias (por ejemplo, `@angular/core`, `@angular/cli`, etc.).
- Actualízalas cuidadosamente a sus últimas versiones compatibles:
  ```bash
  npm install
  ```
  o, si deseas actualizar todas las dependencias:
  ```bash
  npm update
  ```

- Ejecuta `ng build` nuevamente para probar.

*Nota*: Ten cuidado con las actualizaciones, ya que podrían introducir cambios importantes. Prueba tu aplicación minuciosamente después.

---

#### Paso 4: Degradar Node.js (Último Recurso)
Si ninguna de las soluciones anteriores funciona, es posible que Node.js 22.9.0 aún no sea totalmente compatible con la configuración actual de tu proyecto. Degradar a una versión de Soporte a Largo Plazo (LTS) de Node.js, como **20.x** o **18.x**, podría resolver el problema.

- Desinstala tu versión actual de Node.js.
- Descarga e instala una versión LTS desde el [sitio web oficial de Node.js](https://nodejs.org/).
- Verifica la versión instalada:
  ```bash
  node -v
  ```
- Reinstala las dependencias de tu proyecto:
  ```bash
  npm install
  ```
- Ejecuta `ng build` nuevamente.

---

### Enfoque Recomendado
Comienza con el **Paso 1** (configurar `NODE_OPTIONS`), ya que es la solución más rápida y te permite seguir usando Node.js 22.9.0. Si eso no funciona, procede con el **Paso 2** y el **Paso 3**. Utiliza el **Paso 4** solo si es necesario, ya que degradar Node.js podría limitar el acceso a funciones más recientes.

¡Esto debería resolver el error "error 0308010C digital envelope routines::unsupported" y hacer que tu comando `ng build` funcione nuevamente!