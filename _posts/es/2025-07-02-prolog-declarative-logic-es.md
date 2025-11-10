---
audio: false
generated: true
lang: es
layout: post
title: Programación Declarativa Basada en Lógica con Prolog
translated: true
type: note
---

Prolog, abreviatura de "Programming in Logic", es un **lenguaje de programación declarativo** que contrasta marcadamente con lenguajes imperativos como Python, Java o C++. En lugar de indicarle a la computadora *cómo* resolver un problema paso a paso, describes *qué* es el problema, y Prolog utiliza su motor de inferencia integrado para encontrar soluciones.

Es especialmente adecuado para problemas que involucran **lógica, razonamiento simbólico y representación del conocimiento**, lo que lo convierte en un pilar en el campo de la Inteligencia Artificial (IA), el procesamiento del lenguaje natural y los sistemas expertos.

### Conceptos Clave de Prolog:

1.  **Hechos:**
    Los hechos son verdades fundamentales sobre el mundo que le proporcionas a Prolog. Representan afirmaciones incondicionales.

      * **Sintaxis:** `predicado(argumento1, argumento2, ...).`
      * **Ejemplos:**
          * `hombre(juan).` (Juan es un hombre)
          * `mujer(maria).` (María es una mujer)
          * `padre(juan, maria).` (Juan es padre de María)
          * `capital_de(francia, paris).` (París es la capital de Francia)

2.  **Reglas:**
    Las reglas definen relaciones entre hechos. Establecen que un cierto hecho es verdadero si uno o más otros hechos (o condiciones) son verdaderos.

      * **Sintaxis:** `cabeza :- cuerpo.` (Se lee como "la cabeza es verdadera si el cuerpo es verdadero")
          * La `cabeza` es un solo predicado.
          * El `cuerpo` es una conjunción de uno o más predicados, separados por comas (`,`), que significa "Y".
      * **Ejemplos:**
          * `feliz(X) :- le_gusta(X, pizza).` (X es feliz si a X le gusta la pizza)
          * `padre(X, Y) :- padre(X, Y), varon(X).` (X es el padre de Y si X es padre de Y Y X es varón)
          * `abuelo(G, C) :- padre(G, P), padre(P, C).` (G es abuelo de C si G es padre de P Y P es padre de C)

3.  **Consultas:**
    Una vez que has definido tus hechos y reglas (tu "base de conocimiento"), puedes hacerle preguntas a Prolog, llamadas consultas, para recuperar información o verificar relaciones.

      * **Sintaxis:** `?- consulta.`
      * Prolog intenta satisfacer la consulta encontrando variables que hagan la consulta verdadera, basándose en los hechos y reglas establecidos. Si existen múltiples soluciones, a menudo puedes solicitar a Prolog más opciones escribiendo un punto y coma (`;`).
      * **Ejemplos:**
          * `?- hombre(juan).` (¿Es Juan un hombre?)
          * `?- padre(juan, X).` (¿De quién es padre Juan? - `X` es una variable)
          * `?- abuelo(isabel, guillermo).` (¿Es Isabel abuela de Guillermo?)

4.  **Variables:**
    Las variables en Prolog se utilizan para representar valores desconocidos. Siempre comienzan con una letra mayúscula o un guión bajo (`_`). A diferencia de las variables en lenguajes imperativos, no son ubicaciones de memoria que se puedan reasignar; más bien son marcadores de posición que Prolog intenta unificar con valores para satisfacer una consulta.

5.  **Unificación:**
    Este es el mecanismo central de Prolog. La unificación es un proceso de coincidencia de patrones que intenta hacer que dos términos sean idénticos asignando valores a las variables. Si se encuentra una coincidencia, las variables se "vinculan" a esos valores. Si no es posible ninguna coincidencia, la unificación falla.

6.  **Retroceso (Backtracking):**
    Cuando Prolog intenta satisfacer una consulta, trabaja a través de los hechos y reglas de manera profunda (depth-first). Si una ruta conduce a un callejón sin salida (un objetivo no se puede satisfacer), Prolog "retrocede" a un punto de elección anterior e intenta una ruta alternativa. Esta búsqueda sistemática le permite encontrar todas las soluciones posibles a una consulta.

### Cómo Funciona Prolog (Simplificado):

1.  Cargas un programa Prolog (una colección de hechos y reglas) en el intérprete.
2.  Planteas una consulta.
3.  Prolog intenta probar la consulta comparándola con sus hechos y las cabezas de sus reglas.
4.  Si la cabeza de una regla coincide, Prolog luego intenta probar las condiciones en el cuerpo de la regla (estos se convierten en sub-objetivos).
5.  Este proceso continúa recursivamente hasta que todos los sub-objetivos son satisfechos por hechos o por reglas probadas con éxito.
6.  Si se encuentra una solución, Prolog presenta las vinculaciones de variables. Si existen múltiples soluciones, puede retroceder para encontrarlas.

### Ventajas de Prolog:

  * **Naturaleza Declarativa:** Enfócate en *qué* resolver, no en *cómo*. Esto puede conducir a un código más conciso y legible para ciertos problemas.
  * **Lógica e Inferencia Integradas:** Mecanismos potentes para el razonamiento lógico y la búsqueda.
  * **Excelente para IA Simbólica:** Ideal para sistemas expertos, procesamiento de lenguaje natural, representación del conocimiento y demostración de teoremas.
  * **Coincidencia de Patrones y Unificación:** Simplifica la manipulación compleja de datos.
  * **Retroceso:** Automatiza la búsqueda de soluciones, que tendrían que programarse manualmente en otros lenguajes.

### Desventajas de Prolog:

  * **Curva de Aprendizaje:** El paradigma declarativo puede ser un desafío para aquellos acostumbrados a la programación imperativa.
  * **Rendimiento:** Puede ser menos eficiente para cálculos numéricos o tareas intensivas de E/S en comparación con los lenguajes imperativos.
  * **E/S y Gráficos Limitados:** No está diseñado para interfaces de usuario complejas o aplicaciones gráficas.
  * **Depuración:** Rastrear el flujo de ejecución en Prolog a veces puede ser complicado debido al retroceso.

-----

### Ejemplos de Código Prolog:

Para ejecutar estos ejemplos, necesitarás un intérprete de Prolog (como SWI-Prolog, que es gratuito y ampliamente utilizado). Normalmente guardas tu código en un archivo con extensión `.pl` (por ejemplo, `familia.pl`) y luego lo cargas en el intérprete.

**Ejemplo 1: Relaciones Familiares**

Definamos algunas relaciones familiares básicas.

**`familia.pl`:**

```prolog
% Hechos: Definir relaciones básicas
varon(juan).
varon(jim).
varon(jorge).
mujer(maria).
mujer(lisa).
mujer(susan).

padre(juan, lisa).   % Juan es padre de Lisa
padre(juan, jim).    % Juan es padre de Jim
padre(maria, lisa).  % María es madre de Lisa
padre(maria, jim).   % María es madre de Jim
padre(lisa, jorge).  % Lisa es madre de Jorge
padre(jim, susan).   % Jim es padre de Susan

% Reglas: Definir relaciones derivadas
padre(X, Y) :- padre(X, Y), varon(X).          % X es el padre de Y si X es padre de Y Y X es varón.
madre(X, Y) :- padre(X, Y), mujer(X).          % X es la madre de Y si X es padre de Y Y X es mujer.
hijo(X, Y) :- padre(Y, X).                     % X es hijo de Y si Y es padre de X.
abuelo(G, C) :- padre(G, P), padre(P, C).      % G es abuelo de C si G es padre de P Y P es padre de C.
hermano(X, Y) :- padre(P, X), padre(P, Y), X \= Y. % X e Y son hermanos si comparten un padre P, y X no es el mismo que Y.
```

**Ejecutando en un Intérprete de Prolog (ej. SWI-Prolog):**

```prolog
?- consult('familia.pl').
% familia.pl compiled 0.00 sec, 7 clauses
true.

% Consultas:

?- varon(juan).
true.

?- mujer(jim).
false.

?- padre(juan, lisa).
true.

?- padre(X, jim). % ¿Quién es padre de Jim?
X = juan ;          % Escribe ';' para más soluciones
X = maria.
false.

?- padre(juan, lisa).
true.

?- madre(maria, jim).
true.

?- abuelo(juan, jorge).
true.

?- abuelo(X, susan). % ¿Quién es abuelo de Susan?
X = juan ;
X = maria.
false.

?- hermano(lisa, jim).
true.

?- hermano(lisa, jorge).
false. % Porque no comparten *todos* los padres
```

**Ejemplo 2: Base de Conocimiento Simple (Animales)**

**`animales.pl`:**

```prolog
% Hechos sobre animales y sus propiedades
animal(perro).
animal(gato).
animal(pajaro).
animal(pez).

tiene_pelo(perro).
tiene_pelo(gato).
vuela(pajaro).
nada(pez).

come(perro, huesos).
come(gato, pescado).
come(pajaro, semillas).
come(pez, plancton).

% Reglas
es_mamifero(X) :- animal(X), tiene_pelo(X). % Un mamífero es un animal que tiene pelo.
puede_volar(X) :- animal(X), vuela(X).      % Algo puede volar si es un animal y vuela.
```

**Ejecutando en un Intérprete de Prolog:**

```prolog
?- consult('animales.pl').
% animales.pl compiled 0.00 sec, 10 clauses
true.

% Consultas:

?- animal(gato).
true.

?- tiene_pelo(perro).
true.

?- come(gato, X). % ¿Qué come un gato?
X = pescado.

?- es_mamifero(perro).
true.

?- es_mamifero(pajaro).
false.

?- puede_volar(X). % ¿Qué animales pueden volar?
X = pajaro.
false.
```

Estos ejemplos ilustran la naturaleza declarativa de Prolog, donde defines las relaciones y propiedades, y el sistema infiere las respuestas a tus consultas.