---
audio: false
generated: true
lang: es
layout: post
title: Los Modelos de Lenguaje Grande Confirman Mis Perspectivas del CFA
translated: true
type: note
---

https://weibo.com/6347862377/5183994120372979

https://substack.com/inbox/post/167355695

---

Como mencioné en mi publicación anterior de Weibo, me gusta usar LLMs para manejar cosas complejas y tediosas que no disfruto hacer o leer. Esto incluye muchos artículos académicos.

Más de una década después de crear PySonar2 (un inferenciador de tipos y analizador estático para Python) en 2009-2010, me encontré discutiendo análisis de flujo de control (CFA) con ChatGPT, lo que me trajo recuerdos de un debate que tuve con cierto "estudiante de CFA" hace diez años.

https://www.yinwang.org/blog-cn/2016/04/07/cfa

(Las capturas de pantalla que subí a un sitio web en ese entonces ya no están. Conformémonos con lo que queda.)

Es bastante interesante: cosas que vi claramente hace más de una década ahora han sido "confirmadas" por ChatGPT.

Hace quince años, cuando PySonar2 fue creado por primera vez, ya había superado toda la investigación académica sobre CFA de la época (incluyendo el último CFA2). Para un lenguaje cuasi-funcional como Python con cierres lambda, fue el primero en lograr una inferencia de tipos tan precisa. No solo era muy preciso, sino que su rendimiento también era lo suficientemente decente como para analizar todos los proyectos de Python a gran escala en GitHub.

El fundador de Sourcegraph, el mayor usuario de PySonar2, me dijo en ese entonces que el análisis de PySonar2 era sorprendentemente preciso. En ese momento, no le di mucha importancia porque mi enfoque era tan simple que asumí que cualquiera podría haberlo ideado. No fue hasta que me di cuenta de que nadie más lo había hecho antes que pensé que tal vez debería resaltar su valor.

Incluso ahora, el IDE PyCharm de JetBrains no puede lograr un análisis tan preciso o una funcionalidad de "encontrar definición". Por ejemplo, si defines una variable global inicializada a None y luego le asignas una estructura en alguna "función de inicialización", no podrás encontrar los miembros de esa estructura. No estoy diciendo que debas escribir un código tan malo, pero este es un ejemplo.

Si supieras lo que logré en la Universidad de Indiana, entenderías que PySonar2 realmente no fue gran cosa para mí: solo tomó una pequeña fracción de mi esfuerzo. En aquel entonces, no me importaba mucho el lenguaje Python. Y aquellos artículos sobre CFA eran tan oscuros que no tenía ningún interés en profundizar en ellos. Solo los hojeé y pude notar que eran en su mayoría tonterías. Así que construí PySonar2 en unos meses, dejé que otros lo usaran libremente y no me molesté en escribir un artículo. Podría explicar sus principios en solo unas pocas oraciones.

Fui demasiado modesto. Mira todos los artículos sobre CFA, k-CFA, CFA2: un montón de ellos, y aún así no podían resolver problemas del mundo real y nunca se pusieron en uso práctico. k-CFA incluso tenía un problema básico donde "las llamadas y los retornos no coincidían", algo que nunca imaginé que pudiera suceder. PySonar2 nunca tuvo este problema. ¿Cómo podría alguien hacer un diseño tan tonto, publicar un artículo sobre él y tener sucesores que continúen "mejorándolo"?

El CFA2 de Matt Might introdujo algún "autómata con pila", que era solo una forma de recuperar la pila de llamadas de función de los diseños defectuosos de trabajos anteriores. PySonar2 siempre tuvo un "autómata con pila" porque una pila surge naturalmente al interpretar las llamadas a funciones.

Matt Might tenía un blog donde explicaba orgullosamente cómo surgió la "transformación CPS automática", como si fuera el único que lo entendía. Pero sus ideas claramente evolucionaron a partir de artículos de CPS excesivamente complejos y no fueron el resultado de un pensamiento independiente, cargando con mucho lastre histórico. Su escritura a menudo suena profunda pero es difícil de seguir: ¿puedes entenderla realmente? Sus ideas no pueden compararse con mi enfoque de "40 líneas de código". Me reía cuando leía su blog, pero por cortesía y "modestia", me mantuve callado. Creo que Matt Might carece de sustancia real, y ese grupo de personas solo estaba diciendo tonterías. Esa es la verdad, que puedo revelar después de todos estos años.

¿No están estos artículos simplemente produciendo galimatías? Sí, lo sabía hace más de una década. ¿Pero quién podía entender lo que estaba pasando? Ahora puedes consultarlo con ChatGPT :)

De hecho, ChatGPT también confirmó algo más: el uso de CPS en el artículo fundamental de Olin Shivers sobre CFA fue la raíz de todos los problemas:

PySonar2 fue construido completamente de forma independiente, sin hacer referencia a ningún trabajo académico. Abordó directamente el problema de raíz sin ningún lastre académico. Ese es el valor del pensamiento simple. Esta no fue la primera vez que superé independientemente tanto a la academia como a la industria con un resultado tan contundente.

Después de que creé PySonar2, un equipo de Google pasó más de dos años tratando de construir algo mejor, pero terminaron con nada, y Google tuvo que seguir usando mi código abierto mejorado. ¿Por qué? Porque su estrategia era errónea desde el principio. Querían usar un lenguaje de programación lógica como Prolog para la inferencia de tipos de Python, y supe de inmediato que estaba condenado al fracaso. ¿Cómo lo supe? Porque ya había implementado estos métodos y entendía las limitaciones del sistema Hindley-Milner y de Prolog. ¿Cómo lo supe? Porque había implementado y mejorado lenguajes de programación lógica en IU.

Debo agradecer a ChatGPT por articular claramente los hechos que yo veía, ahorrándome la lectura de esos artículos oscuros. Estoy agradecido por su validación del valor de mis ideas. Siento que los LLMs contribuirán enormemente al progreso humano.

Ahora, comparto una conversación que tuve con ChatGPT sobre CFA, esperando que ayude a los investigadores en este campo:

https://chatgpt.com/share/6864e9a1-66c8-8002-b9f5-55e845fde7ae