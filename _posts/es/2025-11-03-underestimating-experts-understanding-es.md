---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Subestimar a los expertos y la comprensión profunda
translated: true
type: note
---

### Contexto de la Publicación
Este fragmento es de una publicación de blog (o reflexión en redes sociales) de Yin Wang, un destacado ingeniero de software, entusiasta de los lenguajes de programación y blogger conocido por sus perspicaces críticas sobre lenguajes de programación, sistemas de tipos y diseño de software. Wang ha trabajado en empresas como Google y es autor del blog Yinwang.org, donde a menudo profundiza en temas como la programación funcional, dialectos de Lisp y la filosofía detrás del diseño de lenguajes. La publicación reflexiona sobre su crecimiento personal en la comprensión de las perspectivas de los expertos, utilizando a Dan Friedman como caso de estudio. Es una humilde admisión de sesgo de confirmación: cómo nosotros (incluyendo al propio Wang) podemos juzgar erróneamente la experiencia de alguien basándonos en desacuerdos superficiales.

El tono es introspectivo y filosófico, comenzando con una observación general sobre los "patrones de pensamiento humano" (probablemente refiriéndose a cómo las personas forman prejuicios rápidamente) y vinculándolo con la propia experiencia de Wang. Utiliza esta anécdota para ilustrar que la crítica profunda a menudo surge de una comprensión profunda, no de la ignorancia.

### La Historia en la Anécdota
Yin Wang recuerda una época en la que subestimó a Dan P. Friedman, un legendario profesor de ciencias de la computación en la Universidad de Indiana y pionero en programación funcional y lógica. Friedman es mejor conocido por coescribir la icónica serie de libros *The Little Schemer* (con Matthias Felleisen), que enseña programación a través de un estilo lúdico de preguntas y respuestas utilizando Scheme, un dialecto minimalista de Lisp.

- **Juicio Erróneo Inicial de Wang**: Friedman ha sido durante mucho tiempo vocal sobre su preferencia por lenguajes dinámicos como Scheme, que no aplican tipos en tiempo de compilación (permitiendo más flexibilidad pero arriesgando errores en tiempo de ejecución). A menudo critica los sistemas de tipos estáticos en lenguajes como Haskell, argumentando que pueden ser excesivamente rígidos, verbosos o limitar la expresividad sin ofrecer beneficios proporcionales en el software del mundo real. Wang, quien respetaba el intelecto de Friedman (especialmente su dominio de conceptos avanzados como *continuations*—un mecanismo poderoso para manipular el flujo de control, similar a "capturar" el resto de la ejecución de un programa como una función), aun así lo descartó como "sesgado" porque Friedman "solo conocía lenguajes dinámicos". Wang vio esto como un punto ciego, muy similar a cómo la gente hoy podría estereotipar a los expertos basándose en sus preferencias de herramientas.

- **El Punto de Inflexión**: La perspectiva de Wang cambió cuando Friedman demostró su profundidad. En una sesión de enseñanza (probablemente en un curso o taller), Friedman utilizó *miniKanren*—un lenguaje de dominio específico embebido y liviano para programación lógica (piense en consultas relacionales, como en Prolog, pero integrado en Scheme)—para implementar el *sistema de tipos Hindley-Milner*. Este es el algoritmo de inferencia de tipos polimórficos que impulsa lenguajes como ML y Haskell, que deduce automáticamente los tipos sin anotaciones mientras garantiza seguridad. Implementarlo en un lenguaje dinámico como Scheme a través de miniKanren muestra elegantemente cómo la programación lógica puede modelar la verificación de tipos como una "búsqueda" de soluciones, tendiendo un puente entre los mundos dinámico y estático.

  Más tarde, Friedman profundizó en *tipos dependientes*—una extensión avanzada de los sistemas de tipos donde los tipos pueden depender de valores en tiempo de ejecución (por ejemplo, una función que solo acepta listas de longitud exactamente 5). Esto permite garantías aún más fuertes, como pruebas dentro del código, como en lenguajes como Idris o Agda. Friedman coescribió *The Little Typer* (2018, con David Thrall), un libro para principiantes que introduce estas ideas a través de un lenguaje simple similar a un "typer", haciendo eco del estilo de sus libros de Schemer pero para programación con tipos.

Wang se dio cuenta de que Friedman no era despectivo por ignorancia; él *entendía* los tipos estáticos (incluyendo el sofisticado sistema de Haskell, que combina Hindley-Milner con extensiones para pereza y mónadas) mejor que la mayoría de sus proponentes. Las críticas de Friedman surgen de ver sus limitaciones—por ejemplo, cómo pueden complicar programas simples o no capturar invariantes específicos del dominio sin tipos dependientes. Este "ver a través" del bombo publicitario conduce a una visión más matizada, a veces contraria.

### Por Qué Esto Importa
La publicación es un meta-comentario sobre la experiencia en lenguajes de programación: el verdadero dominio a menudo parece escepticismo, no entusiasmo ciego. Resuena con los debates en la comunidad de PL (por ejemplo, las guerras de tipado estático vs. dinámico). Wang lo usa para advertir contra juicios precipitados, trazando un paralelo con cómo ve a otros (y a sí mismo) reaccionar ante los contrarios hoy en día.

Para una lectura completa, la publicación original está en el blog de Yin Wang: [Publicación del Blog de Yin Wang sobre Dan Friedman](http://www.yinwang.org/blah?blog=2019/10/01/dan-friedman). El trabajo de Friedman es fundamental—consulte *The Little Schemer* para conceptos básicos de Scheme o *The Little Typer* para tipos dependientes.