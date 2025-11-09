---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Frege sobre las funciones y la insaturación
translated: true
type: note
---

### ¿Qué dice el ensayo de Frege de 1904 "¿Qué es una función?"

El breve ensayo de Gottlob Frege, titulado originalmente *Was ist eine Funktion?* y publicado en un Festschrift para el físico Ludwig Boltzmann, es una aclaración concisa de la naturaleza lógica de las funciones en matemáticas. Escrito al final de la carrera de Frege (después de sus obras principales como *Grundlagen der Arithmetik* y *Grundgesetze der Arithmetik*), responde a confusiones persistentes en la práctica y pedagogía matemática, muy parecidas a los problemas que describiste con estudiantes que confunden ecuaciones gráficas (y = x² + 3x) y notación funcional (f(x) = x² + 3x). Frege no reescribe los libros de texto de matemáticas aquí, sino que disecciona por qué estas notaciones inducen a error y ofrece una base lógica precisa de lo que las funciones *realmente* son. El artículo tiene solo unas 8 páginas en alemán, y su traducción al inglés (por Peter Geach) aparece en colecciones como *Collected Papers on Mathematics, Logic, and Philosophy*.

#### Argumentos clave y estructura
Frege comienza reconociendo el éxito intuitivo de la notación funcional en matemáticas (por ejemplo, sin x, log x, o x²) pero argumenta que su uso descuidado oculta problemas lógicos más profundos. Se basa en sus ideas anteriores de "Función y concepto" (1891), donde trató por primera vez a las funciones como bloques de construcción de la lógica, no solo como herramientas aritméticas. El ensayo tiene tres hilos principales:

1.  **La naturaleza no saturada de las funciones**:
    - Frege insiste en que una función no es una "cosa" completa como un número o un objeto; es *no saturada* (o "incompleta"). Piensa en ello como un espacio en blanco que espera ser llenado: la expresión ξ² + 3ξ (usando ξ como marcador de posición) denota la función misma, pero no puede sostenerse por sí sola como una entidad significativa. Solo cuando se inserta un argumento (por ejemplo, reemplazar ξ con 2) se "satura" y produce un valor (como 2² + 3·2 = 10).
    - Esto contrasta con la enseñanza cotidiana de las matemáticas, donde y = x² + 3x se presenta como "la función" equiparada a y (un valor completo). Frege dice que esto desdibuja los límites: el lado izquierdo (y) está saturado (es un objeto), pero el lado derecho no está saturado hasta que se especifica x. La notación nos engaña para tratar la función como una fórmula estática, ignorando su papel lógico dinámico.

2.  **Crítica del uso matemático tradicional**:
    - Frege apunta al cambio histórico que mencionaste—de la notación gráfica y = f(x) a la abstracta f(x)—como síntoma de errores más profundos. Las matemáticas tempranas (por ejemplo, en la época de Euler) veían las funciones como curvas o reglas, pero para la época de Frege, la definición de Dirichlet (una función como una correspondencia arbitraria entre dominio y rango) se había impuesto. Frege está de acuerdo con la idea extensional (las funciones definidas por el comportamiento de entrada-salida) pero critica cómo se manejan mal las variables.
    - Las variables no son "cantidades variables" (un mito pedagógico común); son marcadores de posición en expresiones. Quitar una variable de 2x³ + x para "obtener la función" (como 2( )³ + ( )) falla en casos de múltiples argumentos, donde los espacios podrían necesitar el *mismo* argumento (como en x³ + x) o *diferentes* (x³ + y). Esto lleva a confusión en la vinculación de variables y en la representación de funciones complejas.
    - También asiente ala paradoja del "concepto caballo" (de su ensayo de 1892): así como no se puede formar un nombre propio como "el concepto caballo" (tratando un concepto predicativo como un objeto), no se puede nombrar directamente a las funciones como entidades completas. Intentar hacerlo colapsa la estructura lógica.

3.  **Implicaciones para la lógica y las matemáticas**:
    - Las funciones son primitivas en el logicismo de Frege (reducir las matemáticas a la lógica): son el pegamento para construir proposiciones, conceptos (funciones de primer nivel especiales que devuelven valores de verdad) e incluso números (como cursos de valores de funciones). Esto se conecta con su filosofía más amplia: las funciones permiten una inferencia precisa sin ambigüedad.
    - Frege termina con optimismo: un análisis claro de las funciones refinará las matemáticas, evitando paradojas (presagiando la carta de Russell de 1902 sobre su propia paradoja, que descarriló el *Grundgesetze* Vol. 2 por esta época).

El ensayo no es una polémica; es diagnóstico, como un filósofo-lógico depurando el lenguaje de las matemáticas. Influenció a la filosofía analítica (por ejemplo, Wittgenstein, Russell) y a la moderna teoría de tipos en lógica/computación, donde las funciones son de hecho operaciones "no saturadas".

#### ¿Qué es una función, según Frege?
En la visión de Frege, una función es **una entidad (o expresión) lógica no saturada que mapea argumentos a valores completando su estructura incompleta**. Formalmente:
- No es la ecuación (y = f(x)), la gráfica, o incluso el conjunto de salidas; esas son derivadas.
- Es el "espacio" en una expresión, como f(ξ) = ξ² + 3ξ, donde ξ señala la incompletitud.
- Propiedades: Extensional (las mismas entradas → las mismas salidas definen la identidad); jerárquica (las funciones de primer nivel toman objetos como argumentos, devuelven objetos; las de segundo nivel toman funciones); y predicativa (conceptos/relaciones como casos especiales).
- Ejemplo: Para f(x) = x² + 3x, la función es la regla/expresión con un hueco; f(2) = 10 es el valor saturado.

Esto resuelve la confusión de tus estudiantes: La "función" no es la totalidad de y = x² + 3x (que mezcla partes completas e incompletas) o solo f(x) = x² + 3x (que todavía tiene un espacio variable). Es el mecanismo de mapeo puro y no saturado subyacente. Enseñarlo de esta manera—desde la lógica, no solo desde el álgebra—evita la interferencia que notaste.

Si lo deseas, puedo sugerir formas de explicar esto en una clase para principiantes o profundizar en otros ensayos relacionados de Frege.

**Referencias**
- [Russell and Frege on the Logic of Functions (PDF summary/discussion)](https://newprairiepress.org/cgi/viewcontent.cgi?article=1023&context=biyclc)
- [The Philosophy of Gottlob Frege (excerpt on functions)](https://assets.cambridge.org/052183/6697/excerpt/0521836697_excerpt.htm)
- [Stanford Encyclopedia of Philosophy: Gottlob Frege](https://plato.stanford.edu/entries/frege/)
- [Collected Papers on Mathematics, Logic, and Philosophy (contains English translation)](https://www.oxfordbibliographies.com/display/document/obo-9780195396577/obo-9780195396577-0065.xml)