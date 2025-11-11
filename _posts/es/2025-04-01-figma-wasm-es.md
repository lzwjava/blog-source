---
audio: false
generated: true
lang: es
layout: post
title: Figma Aprovecha WebAssembly
translated: true
type: note
---

Figma aprovecha WebAssembly (Wasm) para potenciar su rendimiento, convirtiéndolo en un ejemplo destacado de cómo esta tecnología puede transformar las aplicaciones web. En esencia, Figma es una herramienta de diseño colaborativo que se ejecuta principalmente en el navegador, y utiliza WebAssembly para ejecutar tareas críticas e intensivas en rendimiento a velocidades casi nativas. Así es cómo funciona:

El motor de Figma está construido en C++, un lenguaje conocido por su velocidad y eficiencia pero que no es compatible de forma nativa con los navegadores. Para salvar esta brecha, Figma compila su base de código C++ en WebAssembly utilizando Emscripten, una cadena de herramientas que convierte C/C++ en binarios Wasm. Estos archivos `.wasm` se cargan luego en el navegador, donde se encargan del trabajo pesado: cosas como renderizar gráficos vectoriales complejos, gestionar documentos de diseño grandes y procesar actualizaciones en tiempo real entre múltiples usuarios.

Una gran ventaja de este enfoque es el **tiempo de carga**. Figma ha informado que cambiar a WebAssembly redujo su tiempo de carga en más de 3 veces en comparación con su uso anterior de asm.js (un subconjunto de JavaScript para ejecutar código C++). El formato binario de WebAssembly es más compacto y se analiza más rápido que JavaScript, y una vez cargado, el navegador almacena en caché el código de máquina compilado, por lo que las cargas posteriores son aún más rápidas. Esto es crucial para Figma, donde los usuarios a menudo manejan archivos masivos y esperan una respuesta instantánea.

El **motor de renderizado** es otra área clave donde WebAssembly brilla. Figma utiliza WebGL para gráficos acelerados por GPU, pero la lógica que impulsa esto—piensa en el renderizado de curvas, el enmascaramiento, los desenfoques y los modos de fusión—está gestionada por el código C++ compilado a Wasm. Esta configuración evita la canalización de renderizado HTML del navegador, dando a Figma un control afinado sobre el rendimiento y la consistencia entre plataformas. Es por eso que hacer zoom y desplazarse en Figma se siente tan fluido, incluso con miles de capas.

La **colaboración en tiempo real** también se beneficia. Las funciones multijugador de Figma dependen de Conflict-Free Replicated Data Types (CRDTs) para sincronizar cambios al instante entre usuarios. Si bien la lógica CRDT en sí misma podría no ejecutarse completamente en Wasm, el motor impulsado por C++ maneja el estado del documento y las actualizaciones de manera eficiente, asegurando que las ediciones colaborativas no ralenticen el sistema. La velocidad de WebAssembly ayuda a mantener esta fluidez, incluso con docenas de colaboradores.

Hay una arquitectura híbrida en juego aquí: el motor central (C++/Wasm) gestiona el documento y el lienzo, mientras que la UI circundante—como las barras de herramientas y los menús—está construida con JavaScript (ahora TypeScript + React). Los dos se comunican a través de un puente, con Wasm exportando funciones que JavaScript puede llamar, y viceversa. Esta división permite a Figma optimizar el rendimiento donde más importa, manteniendo la flexibilidad nativa de la web de JavaScript para tareas menos intensivas en computación.

Una salvedad: Figma no utiliza WebAssembly de manera uniforme en todos los navegadores. Históricamente, dependía más de Wasm en Firefox debido a errores tempranos de Chrome (por ejemplo, la falta de caché para el código Wasm traducido), aunque las implementaciones modernas probablemente han solucionado esto. Aun así, la canalización de C++ a Wasm sigue siendo central en su arquitectura.

En resumen, Figma utiliza WebAssembly para llevar un rendimiento de nivel de escritorio al navegador, compilando su núcleo C++ en binarios eficientes que manejan el renderizado, la gestión de documentos y la sincronización en tiempo real. Es un caso de libro de texto de cómo Wasm permite que una aplicación web supere con creces las limitaciones de rendimiento de JavaScript. ¿Quieres profundizar más en los detalles técnicos o ver cómo se compara esto con otras herramientas?