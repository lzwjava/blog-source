---
audio: false
generated: false
image: false
lang: es
layout: post
title: Optimización de la Ingeniería de Software para la IA
translated: true
---

### Tabla de Contenidos

1. [Optimizando la Ingeniería de Software para la IA](#optimizing-software-engineering-for-ai)
    - Arquitectura Plana para el Desarrollo Centrado en IA
    - Ventajas de Python en Flujos de Trabajo Impulsados por IA
    - Ingeniería de Contexto y Optimización de Tokens
    - Estructura de Código para Asistencia de IA

2. [Prosperando como Agente Manual de IA](#thriving-as-a-manual-ai-agent)
    - Trabajando con Herramientas de IA en Entornos Empresariales
    - Selección de Herramientas y Gestión de Contexto
    - Construcción de Sistemas de Prompts Reutilizables

3. [Aprovechando Python para el Desarrollo en Java](#leveraging-python-for-java-development)
    - Scripts de Python para el Soporte de Proyectos Java
    - Estrategias de Desarrollo Multilingüe
    - Generación de Código Asistida por IA

4. [Lenguajes de Programación en la Era de la IA](#programming-languages-in-the-ai-era)
    - Futuro de Python, Rust y Java
    - Compromisos entre Rendimiento y Simplicidad
    - Evolución de Lenguajes y Integración con IA

### Optimizando la Ingeniería de Software para la IA

En este blog, utilicé cientos de scripts para ayudar con la traducción, el playground, el mantenimiento de frontmatter y los bots de Telegram. Creo que este enfoque de desarrollo podría representar el futuro de la ingeniería de software optimizada para IA.

No dependo mucho de la funcionalidad de los módulos de Python, ni quiero estructurar el código como un gran proyecto Java Spring.

He trabajado en muchos proyectos de software a lo largo de mi carrera. He observado arquitecturas bancarias impresionantes, microservicios, diseños efectivos multipaíses que minimizan la duplicación, marcos fundamentales robustos construidos sobre Spring y una fuerte gobernanza con configuración centralizada.

Aunque estas arquitecturas bancarias son impresionantes, si tuviéramos que empezar hoy, consideraría optimizar para LLMs e IA. Esto implicaría una mejor ingeniería de contexto, una mejor separación de preocupaciones y priorizar el pensamiento centrado en IA sobre el diseño centrado en humanos. Aunque Spring ofrece múltiples capas y buena abstracción, puede ser difícil para los LLMs e IA navegar.

Creo que deberíamos apuntar a estructuras más planas, similares a una organización plana. Esto significa usar solo dos niveles: el primer nivel llama al segundo nivel. En una función, es mejor llamar a otras 50 funciones directamente en lugar de tener 50 niveles o pilas anidadas. A las IA/LLMs les cuesta juzgar o inferir estructuras complejas y anidadas, pero se desempeñan bien manejando funciones más pequeñas de 100 a 200 líneas de código. Python es adecuado para llamar e importar de otros archivos.

Una razón por la que el código de Python es más fácil que el de Java es que su gestión de dependencias es simple. Solo necesitas usar `pip install` para agregar una dependencia. Con Maven, necesitas escribir la dependencia en un archivo POM XML y luego usar `mvn compile` para que Maven descargue las dependencias.

Otra razón de la simplicidad de Python es que su código se puede ejecutar directamente sin problemas.

Aunque desde Java 11, el comando `java` puede ejecutar directamente programas de código fuente de un solo archivo sin necesidad de compilarlos por separado usando `javac`. Sin embargo, a menudo, para proyectos de Java, son grandes, por lo que hay que ejecutarlos con `mvn spring-boot:run` junto con alguna configuración de propiedades.

Una tercera razón es que el diseño de módulos de Python es simple; puedes usar `from` e `import` para importar fácilmente código de otros archivos.

Actualmente, muchos chatbots de IA pueden ejecutar código de Python directamente en la ventana del chatbot, como Grok.

Al comparar 100 archivos de Java, cada uno con alrededor de 1000 líneas de código, con algunos scripts simples de Python, no es una comparación justa. Para este tipo de proyecto, preferiría tener 1000 archivos de Python, cada uno con alrededor de 100 líneas de código.

Es aceptable seleccionar líneas de código o una función para editar. Sin embargo, necesitas saber dónde seleccionar. ¿Por qué no dejar que esta tarea sea manejada por la IA para facilitar nuestras vidas? Así que solo necesitamos usar "seleccionar todo" para seleccionar todo el código y decirle a la IA/LLM cómo editar.

Para Python, es más fácil usar `if __name__ == "__main__":` para ejecutar y probar funciones en un archivo. También es más fácil para otros archivos de Python llamar a las funciones dentro de este archivo sin necesidad de ejecutar la prueba.

Esto es ingeniería de contexto optimizada para IA. ¿Podríamos abordarlo de otras maneras? La IA/LLM es autorregresiva. Sin embargo, cuando usamos Copilot o Claude Code, no sabemos cómo el Agente de Software de IA nos ayuda. Deberían pensar en ello en lugar de nosotros.

¿Podríamos, desde el lado del usuario, organizar el código específicamente para reducir el uso de tokens? Para este punto, el enfoque de tener 1000 archivos de Python con cada uno 100 líneas de código es bueno para este propósito. Porque puedes verificar funciones y archivos de código fácilmente antes de permitir que otros códigos de Python los llamen.

Pero un problema es que si quieres cambiar varios archivos de código juntos, no es fácil hacerlo. Para una forma simple, puedes copiar el código a los chatbots de IA y dejar que te digan cómo editar el código en estos archivos.

Posiblemente, no necesitemos usar el número de líneas para separar funciones o lógica. Pero deberíamos hacerlo para separar la lógica en funciones pequeñas. Podemos hacerlo separándolas naturalmente por tipo de lógica, para que parezcan más cortas.

¿Por qué queremos Ingeniería de Software Optimizada para IA? Porque la IA es poderosa, deberíamos optimizar todo para la IA y luego dejar que la IA ayude a la ingeniería de software tanto como sea posible.

Es posible no solo para el código, sino también para cualquier texto. Supongamos que somos editores muy exigentes; no queremos que la IA edite nuestros grandes textos de una vez. Queremos revisar párrafo por párrafo. Para el código, podemos tolerar errores o fallos menores. Para el texto, podemos tolerarlos porque la mayoría de los lectores no son tan exigentes.

Pero el código es diferente en el sentido de que a veces, incluso un error menor puede llevar al mal funcionamiento completo de un gran proyecto.

Para archivos XML o YAML, probablemente no necesitemos separarlos tanto porque ya están altamente estructurados.

Y para archivos HTML, deberíamos hacer alguna separación. En lugar de escribir cientos de archivos JavaScript junto con cientos de archivos HTML, haciendo que sea fácil superar las 1000 líneas de código, deberíamos usar `import` para JavaScript para gestionarlo. Para el código JavaScript, podemos usar los métodos anteriores para separarlo.

Queremos estructurar el código de manera que permita a la IA ayudarnos a agregar, editar, eliminar y ejecutar código fácilmente. Este es el comienzo. Imagina un día en el que todo el código pueda ser generado o corregido por la IA fácilmente. El mundo estará altamente digitalizado.

Imagíneme escribiendo 100 grandes proyectos de software y proporcionando APIs para conectarse con otros. Esto incluye mi agenda diaria; yo mismo soy como una empresa tecnológica con 1000 empleados en la actualidad. Están personalizados para mis necesidades, para ganar dinero o gastar dinero para mi beneficio. Esto es realmente asombroso.

### Prosperando como Agente Manual de IA

Los Agentes de IA deben ejecutarse automáticamente con código. Ahora, el título de este ensayo es "Agente Manual de IA". Podrías pensar que estoy bromeando, pero no es así.

La razón por la que digo "agente manual de IA" es que para las grandes empresas, la adopción de tecnología es lenta debido a preocupaciones de seguridad de datos y consideraciones a largo plazo.

Hay muchas nuevas tecnologías en el mercado; quién sabe cuáles durarán o cuáles desaparecerán rápidamente.

También tienen preocupaciones de seguridad de datos. Típicamente, quieren asociarse con grandes marcas cuyas políticas de datos son estrictas y monitoreadas por el público. Esto explica por qué Microsoft se ha convertido en un socio principal entre las empresas Fortune 500. Otras empresas usan sus Teams, Microsoft Office 365, Azure y Copilot.

Sin embargo, ¿qué pasa si las grandes empresas no proporcionan a sus empleados APIs de LLM para usarlas? Necesitamos pensar en cómo trabajar como agentes manuales de IA.

Eso significa que usaremos muchas herramientas para trabajar, similares al uso de herramientas o llamadas de funciones en esas APIs. Haremos nuestra propia ingeniería de prompts o ingeniería de contexto.

En lugar de usar Claude Code o Manus para realizar una tarea compleja, podemos realizar tareas nosotros mismos con un chatbot de IA sencillo.

AspectJ es bueno porque usa programación AOP para interceptar métodos. Los filtros en Spring también son buenos para capturar los registros de solicitudes HTTP. El registrador en Log4j es bueno para redirigir registros específicos a un archivo. IntelliJ IDEA es bueno porque tiene una función para exportar objetos como texto.

Los clientes SQL son buenos porque pueden exportar fácilmente archivos CSV o Excel de filas. Git diff es bueno porque puede darte texto de comparación.

Todos te ayudan a proporcionar un mejor contexto para los chatbots de IA. Y los chatbots de IA también pueden ayudar a muchos scripts de Python a realizar tareas.

Para ser un agente de IA efectivo, necesitas usar muchas herramientas efectivas para ayudarte a realizar tareas, ya sean simples o complejas.

Sin APIs para chatbots de LLM/IA, necesitas copiar el texto en los chatbots. Es un poco más tedioso que llamar directamente a la IA, pero la buena noticia es que puedes seleccionar el contexto o los prompts con más cuidado.

Por lo tanto, no necesitas preguntar a los chatbots de IA muchas veces como esos agentes de IA automáticos. Puedes seleccionar cuidadosamente las herramientas que usarás.

Por lo tanto, trabajar como un agente manual de IA tiene sus beneficios. Sin embargo, la tecnología de agentes de IA evoluciona rápidamente y muestra su potencial al mundo.

Si son muy útiles, las grandes empresas los adoptarán, al igual que los chatbots de IA. De lo contrario, no podrán competir con otras empresas que los hayan adoptado, no solo otras grandes empresas, sino también pequeñas startups. Porque la IA es tan poderosa ahora, una startup con decenas de empleados puede superar a aquellas con 1,000 empleados.

Trabajar como agentes manuales de IA a veces es inevitable. El trabajo tiene otros beneficios además de carecer de tecnología avanzada de IA. No es fácil encontrar buenos trabajos. Entonces, en este caso, nos da espacio para usar nuestra sabiduría tradicional para aprovechar al máximo los chatbots de IA.

Y significa que podemos organizar y acumular nuestros prompts para crear prompts de sistema para chatbots de IA, similares a los utilizados por Claude o Grok que han sido expuestos. De esta manera, no necesitamos escribir prompts repetidamente. Podemos usar scripts de Python para ayudarnos a escribir prompts. Podemos obtener los registros de solicitudes HTTP y escribir prompts para generar casos de prueba de API.

La magia de la programación radica en sus niveles ilimitados de abstracción. Es similar a las funciones donde puedes tener 100 niveles de llamadas de función. Por ejemplo, WeChat se construye sobre iOS, y las Mini Aplicaciones de WeChat se construyen sobre WeChat. iOS a su vez se construye sobre Objective-C o Swift, que a su vez se construyen sobre LLVM y el conjunto de instrucciones de los chips ARM de Apple.

### Aprovechando Python para el Desarrollo en Java

¿Cómo usar Python para ayudar en el desarrollo de Java en la era de la IA? Me gusta Python. He trabajado con Python más que con cualquier otro lenguaje en los últimos tres años, desde que se lanzó ChatGPT a finales de noviembre de 2022.

Una forma de ayudar es usando Python para escribir scripts de ayuda SQL, scripts de prueba y scripts de búsqueda de registros para proyectos de Java.

Usa Python para analizar archivos POM y dependencias de paquetes para Java. Usa Python para verificar la consistencia de datos en Java. Hay muchas cosas que podemos hacer en Python en lugar de Java.

Pero Java no tiene PyTorch. Python puede ayudar con cualquier cosa en 200 líneas de código que tomaría 500 líneas en Java. Pero usando herramientas de IA, no puedes obtener fácilmente tu propia versión de PyTorch. Incluso algo como TinyGrad toma tiempo en construirse.

¿Por qué escribir nuestros propios scripts primero? Una razón es que es muy personalizable. No hay software público o proyectos de código abierto que puedan ayudarnos directamente en nuestros proyectos, especialmente aquellos en grandes empresas.

Los grandes proyectos en grandes empresas se desarrollan durante una década o más. Ya tienen mucha personalización.

Por lo tanto, en el futuro, habrá muchos proyectos alrededor de los grandes proyectos en grandes empresas. Habrá más routers de código similares a Claude en herramientas de agentes de codificación internas en grandes empresas. Habrá más Postman, clientes SQL y compiladores personalizados para grandes empresas.

El código de Python también puede conectarse a agentes de Java.

Esto significa que necesito aprender Python y Java bien, para saber cómo usar uno para ayudar al otro.

Y puedo usar Python con la ayuda de la IA para crear muchas cosas para mí mismo y en proyectos corporativos también. Java no parece un obstáculo. Java, con Spring, bases de datos y Angular, Vue o React como frontend, no debería ser un obstáculo para que Python ayude mucho.

La programación es algo muy flexible. El límite es nuestra imaginación.

Así que la IA está creciendo rápidamente. Podemos medir el progreso de la IA por cuánto y cuán fácilmente podemos usar el código para lograr cosas con la ayuda de la IA en la codificación y el aprendizaje.

¿Podríamos algún día escribir algunos agentes de IA, y luego estos agentes ayudar a crear un TikTok completo, incluyendo sus muchos microservicios y grandes proyectos de iOS o Android?

Si la IA es tan poderosa, ¿qué deberíamos hacer hoy? Probablemente nada, ya que lo que hacemos hoy será fácil de implementar con la IA. En 2025, nuestro trabajo de 1 año con la ayuda de la IA probablemente se pueda hacer en 1 mes con la capacidad de la IA en 2030.

Esto plantea nuestra pregunta esencial: ¿Cuál es nuestro propósito en la vida? ¿De qué se trata todo esto? ¿Cómo vivir una buena vida?

La IA está saliendo como otras tecnologías para darnos libertad. Pero parece que todos están ocupados como máquinas en esta sociedad capitalista.

Volviendo al tema. Así que Python también puede ayudar a escribir código de Java. Puedes usar Python para obtener el contexto para escribir código y dejar que Copilot lo escriba para ti y hacerlo bien desde el primer intento.

La IA se trata de ingeniería de prompts y contexto. Los prompts y el contexto ayudan a las respuestas de los chatbots de IA.

Python puede ayudar con el contexto; Python puede ayudar a generar prompts.

Por lo tanto, esto no se trata solo de Java, sino de cualquier otro lenguaje de programación. Python puede ayudarlos profundamente. Entonces, ¿por qué seguimos necesitando usar otros lenguajes de programación?

Es el diseño intrínseco de Python lo que lo hace desempeñarse peor que otros lenguajes de programación, como C, C++ o Rust.

### Lenguajes de Programación en la Era de la IA

La IA es tan poderosa ahora que tenemos que replantearnos todo desde la perspectiva de la IA. ¿Qué lenguajes de programación serán populares en los próximos 10 años?

Python seguramente lo será. Muchos chatbots de IA usan Python para ejecutar código en el navegador, como Grok. Python es popular por su simplicidad, facilidad de aprendizaje y rendimiento decente. Es adoptado por muchos proyectos de software.

Python es más lento que C++, Java y Rust. Java tiene una gran comunidad. Rust se construye sobre C.

Me pregunto si muchos proyectos serán reescritos o reemplazados por Rust. Ser reescrito en Rust significa referirse a un proyecto antiguo y usar Rust para implementar la misma funcionalidad. Ser reemplazado significa que el software escrito en otros lenguajes ahora es reemplazado por software similar escrito en Rust.

Rust tiene una sintaxis relativamente compleja. Pero en la era de la IA, eso no es un gran problema, porque la IA ayudará a escribir el código. Para sintaxis compleja, los humanos tampoco tienen muchos problemas.

Creo que el hindi o el tamil son bastante complejos. Pero para los indios que viven en el norte, el hindi no es un problema, y para los del sur, el tamil tampoco lo es.

Pero para un ciudadano chino como yo, creo que es un gran problema aprenderlo.

A primera vista, todos los caracteres en hindi se ven similares para mí. Creo que la diferencia entre el hindi y el árabe es como la diferencia entre el chino y el japonés, o el inglés y el español.

Las diferencias entre los lenguajes de programación son menores que las entre los lenguajes naturales. Una gran razón es que los lenguajes de programación solo difieren en la apariencia de los caracteres, mientras que los lenguajes naturales también difieren en el sonido. Los lenguajes naturales difieren en dos aspectos: conjunto de caracteres y pronunciación.

Los lenguajes de programación tienen solo unos cien años de historia, pero los lenguajes naturales tienen más de cien siglos. Cuanto más tiempo pasan las personas en algo, más diferencias se desarrollan. Las personas con opiniones ligeramente diferentes crearán sus propias versiones de las cosas.

Esto explica el acento inglés. En algunos videos de TikTok, la gente dice que el peor acento inglés es el de Birmingham.

Por lo tanto, en realidad, Rust no tiene muchos problemas. Su rendimiento es bastante bueno, ya que se construye sobre C/C++.

El rendimiento es crítico para muchas aplicaciones. Hoy en día, muchas aplicaciones son utilizadas por miles de millones de personas. Para la infraestructura subyacente de computación en la nube, sus servicios son llamados muchas veces. Por lo tanto, incluso un pequeño aumento de rendimiento puede ahorrar mucho dinero.

¿Tiene Rust muchas desventajas? Una cosa de la que la gente se queja es que es difícil de aprender. La curva de aprendizaje es empinada. La IA trae buenas noticias, ya que ayuda mucho con el aprendizaje.

No necesito saber mucho sobre Rust. Como ingeniero de software con 10 años de experiencia, puedo usar la IA para ayudar a escribir muchas aplicaciones simples de Rust. Solo necesito conocer los comandos básicos de compilación de Rust como `cargo` y `cargo build`. Ni siquiera necesito saber mucho sobre la sintaxis de Rust en sí.

Para Rust, el modelo de mutabilidad o préstamo no me causa problemas. Para aplicaciones simples con menos de 200 líneas de código, puedo pedirle a la IA que corrija errores directamente proporcionando mensajes de error.

Pero ¿por qué la gente sigue usando mucho Python si Rust es tan bueno? Porque Python es bueno en otro aspecto. Es muy fácil de usar y aprender. Tiene una gran comunidad y muchas bibliotecas.

Python sigue teniendo un rendimiento lo suficientemente bueno y puede soportar productos para millones, incluso decenas de millones, de usuarios. La mayoría de los productos no tienen tantos usuarios. Si tienes tantos usuarios, puedes contratar programadores de Rust o Java para optimizar el rendimiento.

Python es bueno para muchos desarrollos: aprendizaje automático, desarrollo web, matemáticas, enseñanza y scripting. Aunque Python no es bueno para aplicaciones de escritorio, MicroPython se usa en Raspberry Pi.

¿Y Java en la era de la IA? También estará bien, ya que tiene una gran base de usuarios y comunidad. La IA ayuda mucho con eso. Es utilizado por muchas grandes empresas. Tienden a no cambiar sus lenguajes de programación principales. Para algunos de sus grandes proyectos heredados, usar un nuevo lenguaje de programación para reescribir un proyecto tomaría una década de esfuerzo. La IA ayudará con eso, pero el proceso seguirá siendo lento.

A menudo, las personas racionales en grandes empresas no considerarán cambiar su lenguaje de programación principal. Su negocio principal está en otros sectores. No les importa mucho la tecnología. Si lo hicieran, se convertirían en empresas de software o Internet y liderarían en comunidades de código abierto. Sin embargo, no muchas empresas Fortune 500 se preocupan por eso.

Habrá muchas startups debido a la IA. Las startups les gusta hacer cosas nuevas, por lo que probarán nuevos lenguajes de programación. En la era de la IA, los lenguajes de programación ágiles ganarán en pequeñas y medianas empresas.

En las competencias de algoritmos, ¿cambiará el lenguaje de programación favorito? C++ ha dominado este sector durante décadas. En las competencias de algoritmos reales, no puedes usar IA. Pero creo que en la era de la IA, menos personas participarán.

Dado que esas personas son muy buenas en programación, y hay tantas oportunidades debido a la IA, ¿por qué no más personas construirían productos reales para usuarios en lugar de practicar problemas de algoritmos? Incluso el GOAT de las competencias de algoritmos, Gennady Korotkevich, eligió unirse a Devin.

Pero las competencias de algoritmos pueden ser un pasatiempo relajante o de jubilación para programadores inteligentes. Es como el ajedrez o el baloncesto. Las personas lo hacen porque les gusta o lo necesitan, no por otras razones. Muchas personas juegan al baloncesto en sus 30 o 40 años. Probablemente lo hacen por razones de salud o para hacer la vida más divertida.

Para iOS y Android, es Java, Kotlin, Swift y Objective-C. No habrá cambios significativos debido a la IA, porque hay opciones limitadas. En el lado del usuario final, los requisitos de rendimiento no son tan altos. Google y Apple tienen un control muy alto sobre sus plataformas. Si Google y Apple no cambian, los programadores no cambiarán.

Pero para los servidores, hay muchas opciones. Los lenguajes que son más amigables con la IA ganarán.

Los lenguajes de programación procedimentales ganarán más que los lenguajes orientados a objetos. Los lenguajes procedimentales son directos y fáciles de generar por la IA, mientras que los lenguajes OOP tienen muchos niveles anidados o patrones de diseño.

¿Habrá más lenguajes de programación debido a la IA? Creo que sí. Zed y OCaml tendrán más usuarios. Los LLMs/IA son muy buenos para aprender patrones, por lo que es fácil reescribir proyectos en otros lenguajes.

Los lenguajes de programación enfrentarán más competencia en el futuro. Aquellos que sean buenos en rendimiento, sintaxis y calidad del compilador se volverán inherentemente más populares. La competencia es similar a la de los LLMs. Aquellos que son inherentemente buenos, como Claude y DeepSeek, se vuelven populares.

¿Qué pasa si la IA se vuelve tan poderosa que ya no necesitamos aprender programación? Eso aún está muy lejos. Supongamos que tenemos un proyecto muy grande con 1,000 archivos de Java. La IA probablemente necesitaría 10 años para realizar tareas en eso fácilmente.