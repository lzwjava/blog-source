---
audio: false
generated: true
lang: es
layout: post
title: La Relación de Rust con C
translated: true
type: note
---

No, Rust no está "construido sobre C" en el sentido de que compile a C o requiera C como una capa fundamental para sus propias operaciones. Rust es un lenguaje de programación de sistemas moderno y separado.

Aquí hay un desglose de la relación entre Rust y C, y cómo Rust interactúa con las bibliotecas C:

**¿Está Rust construido sobre C?**

* **Compilador:** El compilador de Rust (`rustc`) está escrito principalmente en Rust mismo. Las primeras versiones del compilador se arrancaron usando OCaml, pero ahora es auto-alojado.
* **Interacción de bajo nivel:** Rust es un lenguaje de bajo nivel que puede interactuar directamente con el sistema operativo y el hardware, de manera similar a C o C++. No depende de C como intermediario para estas operaciones fundamentales.
* **LLVM:** El compilador de Rust utiliza LLVM (Low Level Virtual Machine) como su backend para la generación y optimización de código. LLVM mismo está escrito en gran parte en C++. Esto significa que el código de Rust eventualmente se traduce a la Representación Intermedia (IR) de LLVM, que luego se optimiza y compila a código máquina. Así que, en ese sentido, hay una dependencia de una cadena de herramientas basada en C++ (LLVM), pero Rust en sí mismo no está "construido sobre C".

**¿Puede Rust usar todas las bibliotecas C?**

Sí, Rust tiene una excelente interoperabilidad con las bibliotecas C a través de su **Interfaz de Función Externa (FFI)**. Esto significa que puedes llamar funciones y usar estructuras de datos de bibliotecas C existentes directamente dentro de tu código Rust.

Así es como funciona generalmente:

1.  **Bloques `extern "C"`:** Defines un bloque `extern "C"` en tu código Rust para declarar las firmas de las funciones C que deseas llamar. Esto le indica al compilador de Rust que estas funciones se adhieren a la Interfaz Binaria de Aplicaciones (ABI) de C, que dicta cómo se llaman las funciones y cómo se disponen los datos en la memoria.
2.  **Atributo `#[link]`:** Usas el atributo `#[link(name = "foo")]` para indicarle al enlazador de Rust que se enlace con la biblioteca C especificada (por ejemplo, `libfoo.so` o `foo.lib`).
3.  **Bloques `unsafe`:** Las llamadas a funciones C típicamente se envuelven en bloques `unsafe` en Rust. Esto se debe a que las fuertes garantías de seguridad de memoria de Rust no se pueden hacer cumplir al interactuar con código "externo" que no sigue las reglas de Rust. Tú, como programador, eres responsable de garantizar la seguridad de estas llamadas.
4.  **`bindgen`:** Para bibliotecas C más grandes, escribir manualmente todas las declaraciones `extern "C"` puede ser tedioso. Herramientas como `bindgen` pueden generar automáticamente los enlaces FFI de Rust a partir de archivos de cabecera C, simplificando enormemente el proceso.
5.  **Crate `cty`:** El crate `cty` proporciona tipos primitivos compatibles con C (como `c_int`, `c_char`, etc.) para garantizar un mapeo correcto de tipos de datos entre Rust y C.

**¿Por qué usar bibliotecas C en Rust?**

* **Aprovechar código existente:** Existe un vasto ecosistema de bibliotecas C bien probadas y altamente optimizadas para diversas tareas (por ejemplo, llamadas al sistema, criptografía, computación numérica, gráficos). Rust te permite aprovechar este recurso existente sin tener que reescribir todo desde cero.
* **Interfaces del sistema operativo:** Los sistemas operativos exponen muchas de sus funcionalidades a través de interfaces compatibles con C. Rust necesita poder llamar a estas funciones para interactuar con el SO.
* **Secciones críticas de rendimiento:** Si bien Rust es generalmente muy rápido, es posible que ya exista algún código altamente especializado y crítico para el rendimiento en C y pueda integrarse directamente.

En resumen, Rust no está "construido sobre C", pero proporciona mecanismos robustos (FFI) para una interoperabilidad perfecta con las bibliotecas C, permitiendo a los desarrolladores de Rust aprovechar el extenso ecosistema de C.