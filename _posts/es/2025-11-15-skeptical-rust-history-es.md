---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Historia Escéptica de Rust
translated: true
type: note
---

### Traducción al español y explicación de la publicación  
Título: "La historia de Rust tal como yo la he visto"

Esta es una reflexión larga, personal y bastante crítica escrita por un programador experimentado (probablemente taiwanés, publicando en chino) sobre su primer encuentro con Rust y por qué, a pesar de su popularidad actual, sigue siendo profundamente escéptico al respecto, tanto técnica como culturalmente.

#### Primer encuentro (2009, Universidad de Indiana)
- Mientras estudiaba en la Universidad de Indiana (IU), el autor tuvo dos compañeros de clase (no eran majors de pregrado en CS) que batallaron mucho en el curso avanzado de lenguajes de programación de Dan Friedman.
- Estos compañeros eran del tipo que "hablaban mucho" pero en realidad no entendían los conceptos profundos. Sin embargo, eran buenos para hacer contactos y autopromocionarse.
- En el verano de 2009, estos dos compañeros hicieron unas prácticas en Mozilla Research y trabajaron en una versión temprana del lenguaje Rust (esto habría sido el proyecto personal de Graydon Hoare que Mozilla adoptó más tarde; los compañeros probablemente fueron contribuyentes muy tempranos o becarios de verano en el proyecto).
- Al final del verano, dieron una charla universitaria presentando Rust a todos. Esta fue la primera exposición del autor al lenguaje.

#### La charla de 2009 (la primera impresión del autor)
- La charla fue puro marketing: grandes eslóganes, casi ninguna sustancia técnica.
- Mostraron una diapositiva con un triángulo con "las tres grandes características de Rust": una era "seguridad", las otras dos el autor las olvidó.
- La afirmación clave: Rust lograría una gestión de memoria completamente segura únicamente a través de análisis estático, con cero recolección de basura (sin GC en absoluto).
- El autor salió pensando: "Esto es solo publicidad de Mozilla. Nunca lanzarán un navegador con esto. Morirá como todos sus otros proyectos de investigación." (Menciona específicamente a DrServ/DrJS como otro proyecto de investigación de Mozilla que no llegó a ninguna parte).

#### Dudas sobre el diseñador y la elección del bootstrap
- El autor cuestiona la profundidad de Graydon Hoare (el creador original) en la teoría de lenguajes de programación.
- En particular, piensa que elegir OCaml como el primer lenguaje de implementación mostró falta de gusto o de comprensión profunda (una opinión controvertida pero no poco común entre algunos veteranos de PL a los que no les gustan las peculiaridades de OCaml).

#### Desarrollos posteriores
- Uno de esos compañeros luego inició un proyecto de doctorado sobre un lenguaje de GPU de "propósito general" que afirmaba que podías construir árboles, grafos, etc. en las GPU. El autor pensó que estaba condenado al fracaso porque las GPU están diseñadas para cargas de trabajo de datos paralelos, no para estructuras arbitrarias con muchos punteros. El proyecto efectivamente nunca se volvió práctico, pero el compañero aún así obtuvo un doctorado y ahora trabaja en el compilador de Rust en una gran empresa tecnológica.

#### El propio viaje del autor con la gestión de memoria
- Al autor le fascinaba personalmente la idea de una seguridad de memoria 100% estática sin GC (exactamente la propuesta original de Rust).
- Pasó mucho tiempo diseñando modelos de memoria y análisis estáticos tratando de alcanzar ese sueño.
- Un día le contó su idea a su consejero Kent Dybvig (el legendario autor de Chez Scheme). Kent respondió con calma:  
  "¿La gestión de memoria completamente estática, es siquiera posible? La gestión de memoria es inherentemente un proceso dinámico."
- Esta sola frase destrozó las ilusiones del autor. Se dio cuenta de que la recolección de basura precisa es indecidible en el caso general (relacionado con el problema de la parada).
- Cuando sugirió el conteo de referencias en su lugar, Kent señaló que el ref-counting tiene un alto overhead y a menudo funciona peor que un buen GC generacional. Las pausas de un buen GC no son un problema real si el recolector está bien diseñado (Chez Scheme lo demuestra).

#### Chez Scheme como contraejemplo
- El autor respeta profundamente a Kent Dybvig y a Chez Scheme:
  - Compilación extremadamente rápida.
  - GC altamente configurable, de baja pausa.
  - Filosofía: no perder el tiempo optimizando código estúpido; asumir que el programador es competente; elegir las abstracciones simples correctas.
- En otras palabras, sabiduría > sofisticación por la fuerza bruta.

#### Cómo resultó Rust en realidad
- El sueño original de "gestión de memoria puramente estática, sin GC nunca" está muerto.
- El Rust moderno tiene:
  - `Rc<T>` / `Arc<T>` (conteo de referencias con recolección de ciclos vía `Weak`)
  - Código `unsafe` (obligatorio para muchas bibliotecas del mundo real: pilas de red, navegadores, kernels de SO, etc.)
  - Investigación en curso tratando de hacer partes del código `unsafe` más seguras (Stacked Borrows, Tree Borrows, etc.), pero cada nuevo modelo añade restricciones de nuevo.
- Sin embargo, el marketing y la comunidad aún repiten el mantra de "fuertes garantías estáticas" y "concurrencia sin miedo".
- Cuando señalas las lagunas, la respuesta oficial se convierte en "esa es solo la filosofía de Rust" o "no entiendes el borrow checker".

#### La postura actual del autor
- Él entiende completamente los lifetimes, el borrowing, etc., e incluso ha impartido cursos avanzados de Rust donde los estudiantes implementaban intérpretes de lenguajes funcionales en Rust.
- Pero cuanto más enseña Rust, más aprecia C++:
  - Los smart pointers de C++ + RAII son más simples y más expresivos para muchas tareas.
  - Cuando realmente se necesita el máximo rendimiento, él aún elegirá C/C++ sobre Rust.
- Encuentra que los mensajes de error de Rust son notoriamente difíciles de descifrar, y la necesidad constante de luchar con el borrow checker es molesta.
- La defensa de la "filosofía" le parece una excusa religiosa para los compromisos de diseño.

#### Conclusión
El autor ve el éxito del Rust moderno en gran parte como un triunfo del marketing + el impulso del ecosistema, no como una prueba de que sus ideas centrales eran fundamentalmente más sólidas que décadas de arte previo (sistemas de regiones, Cyclone, tipos lineales, GC de alto rendimiento, etc.). Cree que las afirmaciones grandiosas originales eran ingenuas, los compromisos eran inevitables, y la comunidad ahora se esconde detrás de la "filosofía" cuando se enfrenta a las lagunas.

Es una crítica rara al estilo de un insider de alguien que:
1. vio Rust literalmente en su nacimiento,
2. estudió profundamente la seguridad de memoria por sí mismo,
3. tuvo a Kent Dybvig como mentor,
4. aún elige C/C++ en 2025 a pesar del bombo publicitario.

Ya sea que estés de acuerdo o no, es una contra-narrativa reflexiva a la historia dominante de que "Rust es el futuro que ya ha llegado".