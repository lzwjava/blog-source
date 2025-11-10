---
audio: false
generated: true
image: false
lang: es
layout: post
title: Guía de Configuración Local de TypeScript
translated: true
type: note
---

Para ejecutar TypeScript localmente, normalmente usarás **npm** y el compilador de TypeScript (`tsc`). Aquí tienes una guía paso a paso:

---

### 1. Inicializa tu proyecto

Si aún no tienes un `package.json`:

```bash
npm init -y
```

Esto crea un `package.json` para que puedas gestionar las dependencias.

---

### 2. Instala TypeScript

Instálalo como una dependencia de desarrollo:

```bash
npm install typescript --save-dev
```

Si también quieres tener el compilador de TypeScript (`tsc`) disponible globalmente:

```bash
npm install -g typescript
```

---

### 3. Crea un tsconfig.json

Genera un archivo de configuración por defecto:

```bash
npx tsc --init
```

Esto crea `tsconfig.json`, que controla cómo TypeScript compila tus archivos (target, sistema de módulos, modo estricto, etc.).

---

### 4. Escribe un archivo TypeScript

Ejemplo `index.ts`:

```ts
function greet(name: string): string {
  return `Hello, ${name}!`;
}

console.log(greet("World"));
```

---

### 5. Compila TypeScript

Ejecuta:

```bash
npx tsc
```

Esto compila todos los archivos `.ts` de acuerdo con `tsconfig.json`.

O, para compilar solo un archivo:

```bash
npx tsc index.ts
```

Esto genera un archivo `.js` (por ejemplo, `index.js`).

---

### 6. Ejecuta el JavaScript compilado

Usa Node.js:

```bash
node index.js
```

---

### 7. Opcional: Compilación automática al guardar

Ejecuta con `--watch` para que se recompile cada vez que edites:

```bash
npx tsc --watch
```

---

👉 Ese es el flujo de trabajo estándar:
`npm install` → `tsc` (compilar) → `node` (ejecutar el código compilado).

---

¿Quieres que también te muestre cómo **omitir la compilación manual** ejecutando TypeScript directamente con `ts-node`?