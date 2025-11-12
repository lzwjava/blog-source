---
audio: false
generated: true
lang: es
layout: post
title: WebAssembly
translated: true
type: note
---

Adentrémonos en una guía completa sobre WebAssembly (Wasm). La desglosaré en secciones digeribles: qué es, cómo funciona, por qué es importante, cómo usarlo y hacia dónde se dirige. Al final, tendrás un conocimiento sólido de WebAssembly y de cómo empezar a utilizarlo.

---

### **1. ¿Qué es WebAssembly?**
WebAssembly es un formato de instrucciones binarias diseñado como un objetivo de compilación portátil y de alto rendimiento para lenguajes de programación. Es un lenguaje de bajo nivel, similar al ensamblador, con una representación binaria compacta, pero no está destinado a ser escrito directamente por humanos; en su lugar, se genera compilando lenguajes de alto nivel como C, C++, Rust, Go o incluso Python.

- **Características Clave:**
  - **Rendimiento:** Se ejecuta a una velocidad casi nativa aprovechando las capacidades del hardware.
  - **Portabilidad:** Se ejecuta de manera consistente en todas las plataformas (navegadores, servidores, dispositivos IoT, etc.).
  - **Seguridad:** Opera en un entorno aislado (sandbox), separado del sistema anfitrión.
  - **Interoperabilidad:** Funciona junto con JavaScript, no en su contra.

- **Historia:**
  - Introducido en 2015 gracias a una colaboración entre Mozilla, Google, Microsoft y Apple.
  - Se convirtió en una recomendación del W3C en 2019, marcándolo como un estándar web oficial.

- **Casos de Uso:**
  - Videojuegos web (por ejemplo, exportaciones de Unity o Unreal Engine).
  - Aplicaciones críticas en rendimiento (por ejemplo, editores de video como Figma o herramientas similares a Photoshop).
  - Aplicaciones del lado del servidor (por ejemplo, con Node.js).
  - Ejecutar bases de código legacy en entornos modernos.

---

### **2. ¿Cómo funciona WebAssembly?**
WebAssembly cierra la brecha entre el código de alto nivel y la ejecución en máquina. Este es el proceso:

1. **Código Fuente:** Escribes código en un lenguaje como C++ o Rust.
2. **Compilación:** Un compilador (por ejemplo, Emscripten para C/C++ o `wasm-pack` para Rust) lo traduce al formato binario de WebAssembly (archivos `.wasm`).
3. **Ejecución:**
   - En los navegadores, el archivo `.wasm` se recupera (a menudo mediante JavaScript), se valida y se compila en código máquina por el runtime Wasm del navegador.
   - El runtime lo ejecuta en un sandbox, garantizando la seguridad.

- **Formato de Texto (WAT):** WebAssembly también tiene una representación de texto legible para humanos (`.wat`), útil para depurar o aprender. Por ejemplo:
  ```wat
  (module
    (func (export "add") (param i32 i32) (result i32)
      local.get 0
      local.get 1
      i32.add)
  )
  ```
  Esto define una función `add` que toma dos enteros de 32 bits y devuelve su suma.

- **Modelo de Memoria:** Wasm utiliza un modelo de memoria lineal: un array plano de bytes que el programa puede leer y escribir. Se gestiona manualmente o mediante el runtime del lenguaje fuente.

- **Interacción con JavaScript:** Cargas módulos Wasm en JavaScript usando `WebAssembly.instantiate()` o `fetch()` y llamas a funciones exportadas. Wasm también puede llamar de vuelta a JavaScript.

---

### **3. ¿Por qué usar WebAssembly?**
- **Velocidad:** Los binarios precompilados se ejecutan más rápido que JavaScript interpretado.
- **Flexibilidad de Lenguaje:** Usa C, Rust, etc., en lugar de estar limitado a JavaScript.
- **Eficiencia de Tamaño:** Los archivos `.wasm` son más pequeños que el JavaScript equivalente, reduciendo los tiempos de carga.
- **Multiplataforma:** Escribe una vez, ejecuta en cualquier lugar: navegadores, servidores o dispositivos embebidos.
- **Seguridad:** El sandboxing evita que código malicioso acceda al sistema anfitrión.

**Contrapartidas:**
- No hay acceso directo al DOM (necesitas JavaScript para eso).
- Las herramientas pueden ser complejas para principiantes.
- La depuración es más complicada que con JavaScript.

---

### **4. Cómo empezar con WebAssembly**
Recorramos un ejemplo simple: compilar una función en C a WebAssembly y ejecutarla en un navegador.

#### **Paso 1: Instalar las herramientas**
- **Emscripten:** Una cadena de herramientas para compilar C/C++ a WebAssembly.
  - Instalación: Sigue la [guía de Emscripten](https://emscripten.org/docs/getting_started/downloads.html) (requiere Python, CMake, etc.).
- **Node.js:** Opcional, para ejecutar Wasm fuera del navegador.
- **Un Servidor Web:** Los navegadores requieren que los archivos `.wasm` se sirvan a través de HTTP (por ejemplo, usa `python -m http.server`).

#### **Paso 2: Escribir el código**
Crea un archivo `add.c`:
```c
int add(int a, int b) {
    return a + b;
}
```

#### **Paso 3: Compilar a WebAssembly**
Ejecuta este comando de Emscripten:
```bash
emcc add.c -s EXPORTED_FUNCTIONS='["_add"]' -s EXPORT_ES6=1 -s MODULARIZE=1 -o add.js
```
- Genera `add.js` (un script de unión) y `add.wasm` (el binario).

#### **Paso 4: Usar en HTML**
Crea `index.html`:
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
</head>
<body>
    <script type="module">
        import init, { add } from './add.js';
        async function run() {
            await init();
            console.log(add(5, 3)); // Muestra 8
        }
        run();
    </script>
</body>
</html>
```

#### **Paso 5: Servir y probar**
- Inicia un servidor local: `python -m http.server 8080`
- Abre `http://localhost:8080` en un navegador y revisa la consola.

Para Rust, usarías `cargo` y `wasm-pack`—proceso similar, cadena de herramientas diferente.

---

### **5. Ecosistema y Herramientas**
- **Lenguajes:**
  - **C/C++:** Emscripten.
  - **Rust:** `wasm-pack`, `wasm-bindgen`.
  - **Go:** Soporte integrado para Wasm (`GOOS=js GOARCH=wasm`).
  - **AssemblyScript:** Sintaxis similar a TypeScript para Wasm.

- **Runtimes:**
  - **Navegadores:** Chrome, Firefox, Safari, Edge.
  - **Node.js:** Con `--experimental-wasm-modules`.
  - **Independientes:** Wasmtime, Wasmer, WasmEdge.

- **Bibliotecas:**
  - **WebGL:** Para gráficos (por ejemplo, juegos).
  - **WASI:** Interfaz de Sistema WebAssembly para casos de uso fuera de la web (E/S de archivos, etc.).

---

### **6. Características Avanzadas**
- **Hilos:** Compatible con SharedArrayBuffer para paralelismo.
- **SIMD:** Instrucciones vectoriales para tareas intensivas en matemáticas (por ejemplo, procesamiento de imágenes).
- **WASI:** Extiende Wasm más allá de la web, añadiendo llamadas al sistema.
- **Enlace Dinámico:** Carga múltiples módulos `.wasm` y enlázalos en tiempo de ejecución.

---

### **7. El Futuro de WebAssembly**
- **Adopción Más Amplia:** Más lenguajes y frameworks están añadiendo soporte para Wasm.
- **Computación Sin Servidor (Serverless):** La naturaleza ligera de Wasm se adapta a la computación en el edge.
- **Estandarización:** Propuestas como la recolección de basura y el manejo de excepciones están en progreso.
- **Crecimiento Fuera de la Web:** WASI y runtimes como Wasmer están llevando Wasm a IoT, aplicaciones de escritorio y más.

---

### **8. Recursos para Aprender Más**
- **Sitio Oficial:** [webassembly.org](https://webassembly.org/)
- **Documentación MDN:** [WebAssembly en MDN](https://developer.mozilla.org/en-US/docs/WebAssembly)
- **Tutoriales:** El libro "Rust and WebAssembly" (rustwasm.github.io/book) o la documentación de Emscripten.
- **Publicaciones en X:** Busca #WebAssembly en X para ver ejemplos y debates del mundo real.

---

### **Resumen Rápido**
WebAssembly es un cambio radical para el rendimiento y la portabilidad. Escribes en tu lenguaje favorito, compilas a `.wasm` y lo ejecutas en cualquier lugar, rápidamente. No es una bala de plata (JavaScript aún domina la interactividad web), pero es una herramienta poderosa en el kit del desarrollador moderno.

¿Quieres probar un ejemplo específico, explorar un caso de uso o solucionar algún problema? ¡Házmelo saber!