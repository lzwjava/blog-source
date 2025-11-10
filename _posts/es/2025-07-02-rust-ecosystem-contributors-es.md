---
audio: false
generated: true
lang: es
layout: post
title: Principales Colaboradores y Fundadores de Rust
translated: true
type: note
---

El ecosistema de Rust es vibrante y está en crecimiento, con muchos individuos y organizaciones contribuyendo significativamente. Aquí hay un desglose de los principales contribuyentes, programadores, proyectos influyentes y fundadores:

### Fundadores de Rust

El fundador principal del lenguaje de programación Rust es:

* **Graydon Hoare:** Comenzó Rust como un proyecto personal mientras trabajaba en Mozilla en 2006, impulsado por el deseo de un lenguaje de sistemas que abordara los problemas de seguridad de memoria prevalentes en C y C++. Él estableció los principios fundamentales del lenguaje.

Otras figuras clave que fueron fundamentales en el desarrollo temprano y la evolución de Rust en Mozilla incluyen:

* **Niko Matsakis:** Un colaborador de larga data del compilador y el diseño del lenguaje Rust, particularmente con el *borrow checker*.
* **Patrick Walton**
* **Felix Klock**
* **Manish Goregaokar**

### Principales Contribuyentes y Programadores del Ecosistema Rust (Altamente Reconocidos, Trabajo de Código Abierto)

Es un desafío proporcionar una lista definitiva de los "30 principales", ya que las contribuciones son diversas y están distribuidas entre muchos individuos y equipos. Sin embargo, aquí hay algunos programadores altamente reconocidos y contribuyentes clave conocidos por su trabajo de código abierto y su impacto en la comunidad Rust:

* **Steve Klabnik:** Un escritor prolífico, educador y miembro del equipo central. Es conocido por sus contribuciones a la documentación de Rust (por ejemplo, "The Rust Programming Language Book") y por su defensa de Rust. Ahora trabaja en Oxide Computer Company, aplicando Rust a sistemas de hardware/software.
* **Nicholas Matsakis (nikomatsakis):** Fundamental en el diseño e implementación del compilador de Rust, particularmente el *borrow checker*, que es central para las garantías de seguridad de memoria de Rust. Trabaja en Rust en AWS.
* **Mara Bos:** Un miembro prominente del Rust Libraries Team y activa en la comunidad Rust, contribuyendo a varios aspectos de la biblioteca estándar y la evolución del lenguaje. También es cofundadora de Fusion Engineering.
* **Carol Nichols:** Otra figura clave en la comunidad Rust, coautora de "The Rust Programming Language Book" y miembro de la junta de la Rust Foundation. Aboga activamente por la adopción y sostenibilidad de Rust.
* **Jon Gjengset (jonhoo):** Conocido por sus análisis profundos de los aspectos internos de Rust, especialmente la concurrencia, y por su excelente contenido educativo y transmisiones que ayudan a muchos a aprender conceptos avanzados de Rust.
* **Alex Crichton:** Un contribuyente significativo a varios proyectos de Rust, incluyendo `rust-lang/rust` y `crates.io-index`, desempeñando un papel crucial en la infraestructura del ecosistema.
* **Ralf Jung:** Conocido por su trabajo en Miri, un intérprete UBM (Undefined Behavior Machine) para Rust, que ayuda a identificar comportamiento indefinido en el código Rust.
* **Bryan Cantrill:** CTO y cofundador de Oxide Computer Company, un fuerte defensor de Rust en la programación de sistemas y la industria.
* **Josh Triplett:** Un colaborador de Rust desde hace mucho tiempo y miembro del equipo central, involucrado en muchos aspectos del desarrollo del lenguaje.
* **Armin Ronacher (mitsuhiko):** Creador del framework Python Flask, se ha convertido en una fuerza impulsora significativa para la adopción de Rust, particularmente en Sentry.
* **Andrew Gallant (BurntSushi):** Conocido por crear *crates* de Rust altamente optimizados y ampliamente utilizados como `ripgrep` (una alternativa rápida a grep) y `regex`.
* **Syrus Akbary:** Creador de Wasmer, un runtime de WebAssembly impulsado por Rust.
* **Frank McSherry:** Conocido por su trabajo en *differential dataflow* y otros proyectos que exploran la concurrencia avanzada y el procesamiento de datos en Rust.
* **Jeremy Soller:** Su trabajo en System76 y ahora en Oxide Computer Company demuestra la viabilidad de Rust hasta el nivel del sistema operativo.
* **Guillaume Gomez:** Un contribuyente prolífico al compilador de Rust y al proyecto GTK-RS (enlaces de Rust para GTK).
* **Pietro Albini:** Contribuye significativamente a la infraestructura crucial de Rust y es miembro del equipo central de Rust.
* **Dirkjan Ochtman:** Por mantener `rustls` y `quinn*, bibliotecas importantes para la comunicación segura en Rust.
* **Gary Guo:** Por mantener Rust for Linux, un esfuerzo crítico para integrar Rust en el kernel de Linux.
* **Manish Goregaokar:** Un Ingeniero de Software Senior en Google, contribuye a varios proyectos de Rust incluyendo trabajo relacionado con Unicode.

### Principales Proyectos Rust de Código Abierto (Altamente Impactantes)

Muchos proyectos de código abierto muestran las fortalezas de Rust y tienen un impacto significativo:

1.  **Rust Lang/Rust (el Compilador y la Biblioteca Estándar de Rust):** El proyecto central en sí, empoderando a todos para construir software confiable y eficiente.
2.  **Tauri Apps/Tauri:** Un framework para construir aplicaciones de escritorio y móviles más pequeñas, rápidas y seguras con un frontend web, similar a Electron pero más eficiente.
3.  **RustDesk/RustDesk:** Una aplicación de escritorio remoto de código abierto, una alternativa popular a TeamViewer.
4.  **Alacritty/Alacritty:** Un emulador de terminal multiplataforma y OpenGL conocido por su alto rendimiento.
5.  **Tokio/Tokio:** El runtime asíncrono fundamental para Rust, ampliamente utilizado para construir aplicaciones de red de alto rendimiento.
6.  **Hyper/Hyper:** Una biblioteca HTTP rápida y correcta para Rust, a menudo usada junto con Tokio.
7.  **Actix/Actix-web:** Un framework web potente, rápido y altamente concurrente para Rust.
8.  **Axum/Axum:** Un framework de aplicaciones web construido con Tokio y Hyper, que enfatiza la ergonomía y el tipado fuerte.
9.  **Ripgrep (BurntSushi/ripgrep):** Una herramienta de búsqueda orientada a líneas que busca recursivamente en directorios un patrón de regex, significativamente más rápida que `grep`.
10. **Bat (sharkdp/bat):** Un clon de `cat(1)` con alas, que ofrece resaltado de sintaxis, integración con Git y más.
11. **Fd (sharkdp/fd):** Una alternativa simple, rápida y fácil de usar a `find`.
12. **Meilisearch/Meilisearch:** Un motor de búsqueda potente, rápido y relevante.
13. **Polars/Polars:** Una biblioteca de Dataframes extremadamente rápida, a menudo vista como una alternativa en Rust a Pandas para la manipulación de datos.
14. **BevyEngine/Bevy:** Un motor de juegos impulsado por datos, sorprendentemente simple, construido en Rust.
15. **Helix Editor/Helix:** Un editor de texto modal moderno inspirado en Neovim y Kakoune, escrito en Rust.
16. **Nushell/Nushell (o Nu):** Un shell moderno que pretende llevar conceptos de lenguajes de programación a la línea de comandos.
17. **Deno/Deno:** Un runtime seguro para JavaScript y TypeScript, construido con Rust y V8.
18. **Firecracker MicroVM/Firecracker:** Desarrollado por AWS, una tecnología de virtualización ligera utilizada para la computación sin servidor (*serverless*).
19. **Crates.io:** El registro oficial de paquetes para el lenguaje de programación Rust, esencial para el ecosistema.
20. **Rustlings (rust-lang/rustlings):** Pequeños ejercicios para acostumbrar a los usuarios a leer y escribir código Rust, increíblemente valioso para principiantes.
21. **Yewstack/Yew:** Un framework moderno de Rust para construir aplicaciones web del lado del cliente usando WebAssembly.
22. **DioxusLabs/Dioxus:** Otra biblioteca de UI declarativa popular para Rust para construir aplicaciones multiplataforma.
23. **Servo/Servo:** Un motor de navegador de alto rendimiento y paralelo escrito en Rust, desarrollado por Mozilla y luego transferido a la Linux Foundation.
24. **Rocket/Rocket:** Un framework web para Rust, conocido por su seguridad de tipos y experiencia de desarrollador.
25. **Solana/Solana:** Una plataforma blockchain de alto rendimiento, con una porción significativa de sus componentes centrales escritos en Rust.
26. **Substrate/Substrate:** Un framework para construir blockchains personalizados, que también utiliza intensamente Rust.
27. **Wasmtime/Wasmtime:** Un runtime independiente estilo JIT para WebAssembly y WASI (WebAssembly System Interface).
28. **Delta (dandavison/delta):** Un paginador con resaltado de sintaxis para la salida de `diff`, `git` y `merge`.
29. **Spotify TUI (Rigellute/spotify-tui):** Una interfaz de usuario de terminal para Spotify.
30. **mdBook (rust-lang/mdBook):** Una herramienta de línea de comandos para crear libros a partir de archivos Markdown, utilizada para muchos proyectos de Rust, incluido "The Rust Programming Language Book."

Esta lista no es exhaustiva, y el ecosistema de Rust está en constante evolución con nuevos e impactantes proyectos emergiendo regularmente. La fuerza de la comunidad reside en su naturaleza colaborativa y la alta calidad de sus contribuciones de código abierto.