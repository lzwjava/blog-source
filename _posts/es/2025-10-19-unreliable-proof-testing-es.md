---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: La Prueba Poco Fiable de la Ciencia Mediante Pruebas
translated: true
type: note
---

### Por qué la gente confía ciegamente en los experimentos científicos: una analogía de programador

Mucha gente no logra captar los defectos lógicos inherentes a los experimentos científicos, lo que los lleva a aceptar la ciencia "probada" tal como se presenta. No entienden por qué una teoría que ha sido "confirmada" mediante experimentos aún puede resultar estar equivocada. Pero si comprendes los principios de las pruebas de software, verás la verdadera naturaleza de los experimentos científicos—como los problemas que discutí en mi artículo *La Lógica de las Pruebas*.

En resumen, una teoría científica es como un fragmento de código, y los experimentos científicos son como pruebas diseñadas para "verificar" que el código funciona correctamente. Imagina escribir un programa para calcular la multiplicación, pero lo implementas por error como una suma: `(x, y) => x + y`. Si lo pruebas con las entradas (2, 2) y obtienes 4, podrías pensar: "¡Genial, está multiplicando correctamente!". Pero estarías completamente equivocado. Para confirmar realmente que es una función de multiplicación, necesitarías probar *cada entrada posible* y asegurarte de que produce la salida correcta cada vez. Como no podemos probar infinitas entradas, ninguna cantidad de pruebas puede *garantizar* que el programa sea correcto. Incluso si miles pasan, aún podría fallar espectacularmente en un caso no probado.

La ciencia funciona de la misma manera. Una teoría solo está verdaderamente "probada" si se mantiene bajo *todas las condiciones concebibles*—cada "entrada" posible del universo. Una trampa común es ejecutar solo un experimento en una configuración estrecha y declarar la teoría validada. Eso es como darse palmaditas en la espalda después de la prueba (2, 2) y darlo por terminado. A veces, ejecutas miles de pruebas, y todo sale bien—hasta que llega una entrada novedosa, y bum, la teoría se desmorona.

Esta es la esencia de la "falsabilidad" de la ciencia. Algunas personas pregonan la falsabilidad como el sello distintivo de la ciencia verdadera, descartando cualquier cosa no falsable como pseudociencia. Pero usando la analogía de la programación, podemos ver que eso no es del todo correcto. La falsabilidad resalta las *limitaciones* de los experimentos—pueden refutar una teoría pero nunca probarla completamente. No debería ser la *definición* rígida de lo que cuenta como ciencia.

Cuantas más restricciones y complejidad agregues a tus pruebas (o experimentos), más difícil se vuelve afirmar con confianza que tu programa (o teoría) es correcto. En programación, las configuraciones de prueba intrincadas con montones de casos extremos hacen que la validación sea más dura y menos convincente. La ciencia no es diferente: Cuantas más condiciones controladas, equipos sofisticados y variables aisladas implique un experimento, más débil es su "persuasividad" para probar una teoría amplia. Podría funcionar en esa placa de Petri, pero ¿escalará al desordenado mundo real?

Por eso no puedo creer en la teoría de la relatividad de Einstein. Los experimentos utilizados para probarla son pocos y espaciados, confinados a condiciones ultra-especializadas sin mucha universalidad. Los experimentos clásicos de validación para la relatividad solo ocurren una vez por siglo más o menos, haciendo que la replicación independiente sea casi imposible para la mayoría de los investigadores. Hasta el día de hoy, no existe una aplicación práctica que *requiera* la relatividad— el ejemplo citado a menudo de los satélites GPS en realidad no la necesita; la física Newtoniana básica basta con pequeños ajustes. Incluso la premisa central, "la velocidad de la luz es constante independientemente del movimiento de la fuente", descansa en un único experimento en una configuración artificial con equipo hiper-complejo, elevado a verdad eterna sin un escrutinio más amplio.

Muchas teorías médicas siguen el mismo patrón: Un estudio es aclamado como el evangelio, citado sin cesar, pero rara vez se verifica de forma independiente. Las generaciones posteriores simplemente lo repiten, asumiendo que es sólido como una roca.

Esta analogía no se trata de descartar la ciencia de plano—es un llamado a mantener la humildad sobre lo que realmente significa "prueba". Los experimentos son herramientas poderosas, pero son focos, no reflectores. Iluminan parches de verdad, pero las sombras acechan en todas partes. Si tratáramos las teorías como código bajo revisión constante—abierto a pruebas y refactorización interminables—la ciencia sería aún más fuerte.