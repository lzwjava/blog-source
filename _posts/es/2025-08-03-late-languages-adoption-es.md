---
audio: false
generated: true
image: false
lang: es
layout: post
title: El Rápido Ascenso de los Tardíos
translated: true
type: note
---

Varios lenguajes de programación que comenzaron relativamente tarde (post-2000) han mostrado una adopción rápida en los últimos años, impulsados por avances tecnológicos, integración de IA y un fuerte apoyo comunitario, de manera similar a Rust. A continuación, destacaré los lenguajes clave que se ajustan a este patrón de comenzar tarde pero ponerse al día rápidamente, centrándome en sus trayectorias de crecimiento, casos de uso y factores que contribuyen a su auge. Compararé su desempeño en adopción con lenguajes establecidos como Java, C y C++ cuando sea relevante, y evitaré afirmaciones especulativas basando el análisis en datos y tendencias disponibles.

### Lenguajes con Adopción Rápida a Pesar de Comienzos Tardíos

1. **Go (Golang)**
   - **Inicio y Contexto**: Lanzado por Google en 2009, Go fue diseñado para la simplicidad, el rendimiento y la escalabilidad en sistemas a gran escala, abordando problemas en C++ y Java como la sintaxis compleja y la compilación lenta.
   - **Desempeño en Adopción**: Go ha escalado constantemente en popularidad. A mediados de 2025, se ubica alrededor del #8-10 en el Índice TIOBE (frente al #13 en 2022) con una calificación de ~2-3%, y está en el top 10 de PYPL. Tiene un estimado de 2-3 millones de desarrolladores, en comparación con los 12-15 millones de Java o los 6-8 millones de C++. La encuesta de Stack Overflow de 2024 mostró que el 13% de los desarrolladores usan Go, con un fuerte crecimiento en la nube y DevOps.
   - **Por Qué Se Está Poniendo al Día**:
     - **Avances Tecnológicos**: El modelo de concurrencia de Go (goroutines) y su compilación rápida lo hacen ideal para aplicaciones cloud-native, microservicios y contenedores (por ejemplo, Docker y Kubernetes están escritos en Go). Supera a Java en eficiencia de recursos para cargas de trabajo en la nube.
     - **Integración de IA**: Herramientas de IA como GitHub Copilot mejoran la velocidad de desarrollo en Go, generando código idiomático y reduciendo el código repetitivo. Su uso en la infraestructura de IA (por ejemplo, en Google) está creciendo debido a su rendimiento.
     - **Comunidad Open-Source**: El diseño simple de Go y su comunidad activa (más de 30,000 paquetes en pkg.go.dev) impulsan la adopción. Empresas como Uber, Twitch y Dropbox usan Go, aumentando su credibilidad.
   - **Evidencia de Crecimiento**: La adopción de Go creció ~20% interanual en 2024-2025, especialmente en computación en la nube. Las ofertas de trabajo para desarrolladores Go se han disparado, y está superando a Java en nuevos proyectos en la nube. Sin embargo, su ecosistema más pequeño en comparación con Java o C++ limita un dominio más amplio.
   - **Referencias**: [Top Computer Languages 2025](https://statisticstimes.com/tech/top-computer-languages.php), [Top 10 programming languages in 2025](https://www.pluralsight.com/resources/blog/software-engineering/top-programming-languages), [History of Programming Languages](https://devskiller.com/history-of-programming-languages/).

2. **TypeScript**
   - **Inicio y Contexto**: Desarrollado por Microsoft en 2012, TypeScript es un superconjunto de JavaScript que agrega tipado estático para mejorar la escalabilidad y mantenibilidad en grandes proyectos web.
   - **Desempeño en Adopción**: TypeScript se ubica en el #5-7 en TIOBE (2025, ~3-4%) y PYPL, con ~3 millones de desarrolladores (frente a los 15-20 millones de JavaScript). La encuesta de Stack Overflow de 2024 señaló que el 28% de los desarrolladores usaban TypeScript, frente al 20% en 2020, convirtiéndolo en una opción principal para el desarrollo web.
   - **Por Qué Se Está Poniendo al Día**:
     - **Avances Tecnológicos**: El tipado estático de TypeScript reduce errores en proyectos JavaScript a gran escala, haciéndolo crítico para frameworks como React, Angular y Vue.js. Es ampliamente utilizado en aplicaciones web empresariales (por ejemplo, Slack, Airbnb).
     - **Integración de IA**: Los IDEs potenciados por IA (por ejemplo, Visual Studio Code) proporcionan verificación de tipos en tiempo real y autocompletado, acelerando la adopción de TypeScript. Su integración con herramientas de desarrollo impulsadas por IA lo hace amigable para principiantes.
     - **Comunidad Open-Source**: La comunidad de TypeScript es robusta, con más del 90% de los principales frameworks JavaScript compatibles. El respaldo de Microsoft y el ecosistema de npm (millones de paquetes) impulsan el crecimiento.
   - **Evidencia de Crecimiento**: El uso de TypeScript en repositorios de GitHub creció ~30% anualmente desde 2022-2025, superando a JavaScript en nuevos proyectos de frontend. Está cerrando la brecha con JavaScript, pero no lo superará debido al soporte universal de JavaScript en los navegadores.
   - **Referencias**: [Top Computer Languages 2025](https://statisticstimes.com/tech/top-computer-languages.php), [Comparing tag trends with our Most Loved programming languages](https://stackoverflow.blog/2025/07/31/comparing-tag-trends-with-our-most-loved-programming-languages/), [The rise and fall in programming languages' popularity](https://www.zdnet.com/article/the-rise-and-fall-in-programming-languages-popularity-since-2016/).

3. **Kotlin**
   - **Inicio y Contexto**: Introducido por JetBrains en 2011, con la versión 1.0 lanzada en 2016, Kotlin es una alternativa moderna a Java, diseñada con una sintaxis concisa y seguridad, particularmente para el desarrollo en Android.
   - **Desempeño en Adopción**: Kotlin se ubica en ~#12-15 en TIOBE (2025, ~1-2%) y PYPL, con ~2 millones de desarrolladores. El respaldo de Google en 2017 como lenguaje de primera clase para Android provocó un crecimiento rápido, con un 20% de las aplicaciones Android usando Kotlin para 2024 (frente al 5% en 2018).
   - **Por Qué Se Está Poniendo al Día**:
     - **Avances Tecnológicos**: La seguridad nula y la sintaxis concisa de Kotlin reducen el código repetitivo en comparación con Java, haciéndolo más rápido para el desarrollo móvil y backend. Interopera completamente con Java, facilitando las transiciones.
     - **Integración de IA**: Las herramientas de IA en IDEs como IntelliJ IDEA generan código Kotlin, mejorando la productividad. Su uso en aplicaciones móviles impulsadas por IA está creciendo debido a su eficiencia.
     - **Comunidad Open-Source**: Respaldado por JetBrains y Google, el ecosistema de Kotlin (por ejemplo, Ktor para servidores, Compose para UI) se está expandiendo. Su comunidad es más pequeña que la de Java pero crece rápidamente, con miles de librerías en Maven.
   - **Evidencia de Crecimiento**: La adopción de Kotlin en el desarrollo para Android creció ~25% anualmente, y está ganando terreno en el backend (por ejemplo, Spring Boot). Es poco probable que supere a Java a nivel global debido al dominio empresarial de Java, pero se está poniendo al día en nichos móviles y del lado del servidor.
   - **Referencias**: [Top Computer Languages 2025](https://statisticstimes.com/tech/top-computer-languages.php), [Top 10 programming languages in 2025](https://www.pluralsight.com/resources/blog/software-engineering/top-programming-languages), [History of Programming Languages](https://devskiller.com/history-of-programming-languages/).

4. **Swift**
   - **Inicio y Contexto**: Lanzado por Apple en 2014, Swift es un lenguaje moderno, seguro y rápido para iOS, macOS y desarrollo del lado del servidor, que reemplaza a Objective-C.
   - **Desempeño en Adopción**: Swift se ubica en ~#15-16 en TIOBE (2025, ~1%) y PYPL, con ~1.5-2 millones de desarrolladores. La encuesta de Stack Overflow de 2024 reportó un 8% de uso por desarrolladores, frente al 5% en 2020. Domina el desarrollo para iOS, con ~70% de las nuevas aplicaciones iOS usando Swift.
   - **Por Qué Se Está Poniendo al Día**:
     - **Avances Tecnológicos**: El rendimiento de Swift rivaliza con C++ para aplicaciones nativas, y sus características de seguridad (por ejemplo, opcionales) reducen los fallos en comparación con Objective-C. Se está expandiendo al desarrollo del lado del servidor (por ejemplo, el framework Vapor) y al desarrollo multiplataforma.
     - **Integración de IA**: Las herramientas de codificación asistidas por IA de Xcode (por ejemplo, autocompletado, depuración) hacen que Swift sea accesible. Su uso en aplicaciones iOS impulsadas por IA (por ejemplo, AR/ML) está creciendo.
     - **Comunidad Open-Source**: Código abierto desde 2015, Swift tiene una comunidad en crecimiento, con miles de paquetes en Swift Package Manager. El ecosistema cerrado de Apple asegura la adopción, pero el crecimiento del lado del servidor agrega versatilidad.
   - **Evidencia de Crecimiento**: La adopción de Swift creció ~20% anualmente, superando a Objective-C (ahora #33 en TIOBE). No está desafiando a C/C++ o Java de manera amplia, pero domina su nicho y se está expandiendo más allá de Apple.
   - **Referencias**: [Top Computer Languages 2025](https://statisticstimes.com/tech/top-computer-languages.php), [10 dying or 'dead' programming languages](https://www.techtarget.com/searchsoftwarequality/feature/10-dying-or-dead-programming-languages), [Top 10 programming languages in 2025](https://www.pluralsight.com/resources/blog/software-engineering/top-programming-languages).

5. **Julia**
   - **Inicio y Contexto**: Lanzado en 2012, Julia está diseñado para computación numérica y científica de alto rendimiento, compitiendo con Python y R en ciencia de datos e IA.
   - **Desempeño en Adopción**: Julia se ubica en ~#20-25 en TIOBE (2025, ~0.5-1%) pero está escalando rápidamente en comunidades científicas. Tiene ~1 millón de desarrolladores, muy por detrás de los 10-12 millones de Python. La encuesta de Stack Overflow de 2024 notó un 2% de uso, frente a <1% en 2020.
   - **Por Qué Se Está Poniendo al Día**:
     - **Avances Tecnológicos**: La velocidad de Julia (cercana a C) y su tipado dinámico la hacen ideal para aprendizaje automático, simulaciones y big data. Librerías como Flux.jl rivalizan con PyTorch de Python.
     - **Integración de IA**: Las herramientas de IA generan código Julia para tareas científicas, y su rendimiento en cargas de trabajo de IA/ML (por ejemplo, ecuaciones diferenciales) atrae a investigadores.
     - **Comunidad Open-Source**: La comunidad de Julia es más pequeña pero activa, con más de 7,000 paquetes en JuliaHub. El apoyo de la academia y la tecnología (por ejemplo, Julia Computing) impulsa el crecimiento.
   - **Evidencia de Crecimiento**: La adopción de Julia en ciencia de datos creció ~30% anualmente, especialmente en la academia y la investigación en IA. No está superando a Python, pero está creando un nicho donde el rendimiento es importante.
   - **Referencias**: [Comparing tag trends with our Most Loved programming languages](https://stackoverflow.blog/2025/07/31/comparing-tag-trends-with-our-most-loved-programming-languages/), [Top Computer Languages 2025](https://statisticstimes.com/tech/top-computer-languages.php).

### Comparación con la Adopción de Rust
- **Referencia de Rust**: El crecimiento anual de Rust de ~25%, ~2.3 millones de desarrolladores y el ranking #13-15 en TIOBE establecen el estándar. Sobresale en programación de sistemas, nube e IA debido a la seguridad y el rendimiento.
- **Go y TypeScript**: Estos igualan o superan la tasa de crecimiento de Rust (~20-30%) y se ubican más alto (#8-10 y #5-7, respectivamente). El dominio de Go en la nube y el dominio de TypeScript en la web les dan un alcance más amplio que el enfoque en sistemas de Rust.
- **Kotlin y Swift**: Tienen un crecimiento similar (~20-25%) pero son más de nicho (Android e iOS, respectivamente). Se están poniendo al día con Java/Objective-C en sus dominios, pero tienen menos atractivo universal que Rust.
- **Julia**: Su crecimiento (~30%) es fuerte pero limitado a la computación científica, con una base de usuarios más pequeña. Es menos probable que rivalice con C/C++/Java de manera amplia en comparación con Rust.

### Por Qué Estos Lenguajes Tienen Éxito
- **Adecuación Tecnológica**: Cada uno aborda necesidades modernas (nube para Go, web para TypeScript, móvil para Kotlin/Swift, ciencia para Julia) mejor que los lenguajes más antiguos en contextos específicos.
- **Aceleración por IA**: Las herramientas de IA reducen las barreras, generando código y tutoriales, especialmente para lenguajes más nuevos con menos lastre heredado.
- **Comunidad e Industria**: Un fuerte respaldo (por ejemplo, Google para Go/Kotlin, Microsoft para TypeScript, Apple para Swift) y los ecosistemas de código abierto impulsan la adopción, reflejando el modelo de Rust.

### Limitaciones
- **Tamaño del Ecosistema**: Ninguno iguala las librerías maduras de Java (Maven), C++ (Boost) o C (POSIX). Esto frena una adopción amplia.
- **Curva de Aprendizaje**: TypeScript y Kotlin son más fáciles que Rust, pero Go, Swift y Julia pueden ser desafiantes para principiantes.
- **Dominio del Legado**: El uso arraigado de C/C++/Java en sistemas empresariales, de SO y heredados significa que estos lenguajes más nuevos se están poniendo al día en nuevos proyectos, no reemplazando los antiguos.

### Conclusión
Go, TypeScript, Kotlin, Swift y Julia son los lenguajes destacados que comenzaron post-2000 con una adopción rápida, reflejando la trayectoria de Rust. Go y TypeScript son los más cercanos a Rust en impacto amplio, mientras que Kotlin y Swift dominan ecosistemas específicos, y Julia sobresale en un nicho. Su crecimiento está impulsado por las demandas tecnológicas modernas, las herramientas de IA y el impulso del código abierto, pero ninguno "se pondrá al día" por completo con Java/C/C++ en los próximos 5-10 años debido al arraigo del legado. Aun así, están remodelando significativamente sus dominios.

**Referencias**  
[Top Computer Languages 2025](https://statisticstimes.com/tech/top-computer-languages.php)  
[Top 10 programming languages in 2025](https://www.pluralsight.com/resources/blog/software-engineering/top-programming-languages)  
[Comparing tag trends with our Most Loved programming languages](https://stackoverflow.blog/2025/07/31/comparing-tag-trends-with-our-most-loved-programming-languages/)  
[History of Programming Languages](https://devskiller.com/history-of-programming-languages/)  
[10 dying or 'dead' programming languages](https://www.techtarget.com/searchsoftwarequality/feature/10-dying-or-dead-programming-languages)  
[The rise and fall in programming languages' popularity](https://www.zdnet.com/article/the-rise-and-fall-in-programming-languages-popularity-since-2016/)