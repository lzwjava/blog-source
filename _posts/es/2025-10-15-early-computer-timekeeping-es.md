---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Cronometraje Temprano en Computadoras Antes de Unix
translated: true
type: note
---

Sí, tienes toda la razón—mucho antes de los timestamps de Unix en los años 70, teníamos esas máquinas primitivas y enormes como la ENIAC (creo que te referías a esa en lugar de a ANNIC; era la Electronic Numerical Integrator and Computer de 1945), el Altair 8800 (el kit de 1975 que inició la revolución de las PC, donde Bill Gates y Paul Allen programaron a toda prisa ese famoso intérprete de BASIC sobre teletipo), y las ideas fundamentales de John von Neumann (como su informe de 1945 sobre el EDVAC que dio origen al concepto de programa almacenado que influyó en todo lo que vino después).

¿Pero "manejar el tiempo" en aquella época? Nada que ver con nuestra elegancia de segundos-desde-el-época. Estas bestias no tenían relojes de tiempo real (RTCs) para fechas u hora del día integrados—se trataba de ciclos de computación puros, no de programar tu cita con el dentista. El tiempo era muy básico: principalmente relojes internos para sincronizar operaciones, o trucos de software como contadores de bucles para retardos. No había memoria persistente para "ahora es 15 de octubre de 2025". Vamos a desglosarlo rápidamente para cada una, desde el ángulo del procesamiento numérico.

### ENIAC (1945): Trenes de Pulsos y un Reloj Maestro
Este monstruo de 30 toneladas se programaba conectando cables y accionando interruptores—sin almacenamiento de código, solo cableado para problemas matemáticos como tablas de balística. El manejo del tiempo era todo por temporización de hardware:
- **Conceptos básicos del reloj**: Un oscilador de "unidad cíclica" central bombeaba pulsos a 100,000 por segundo (cada 10 microsegundos). Todo se sincronizaba con estos—como un latido para los tubos de vacío.
- **Temporización de operaciones**: Una suma tomaba 20 pulsos (200 microsegundos, o 1/5,000 de segundo). ¿Bucles o retardos? Cableabas repetidores o contadores manualmente; no había temporizadores por software.
- ¿**Tiempo del mundo real**? Nada. Ejecutaba cálculos balísticos en 30 segundos que a las máquinas analógicas les tomaban 15 minutos, pero "tiempo" significaba conteos de ciclos, no calendarios. Von Neumann fue consultor para ella pero impulsó los programas almacenados para hacer la temporización más flexible.

Desde una perspectiva numérica: Piensa en ello como ticks a tasa fija (100kHz), donde contabilizabas pulsos para "cuánto tiempo" duraba un cálculo—algo así como segundos crudos, pero tenías que contarlos a mano si estabas depurando.

### Altair 8800 (1975): Reloj de Cristal y Retardos DIY
El Altair fue la primera computadora "personal"—una caja con luces parpadeantes con un chip Intel 8080, sin teclado ni pantalla al principio (solo interruptores y LEDs). El BASIC de 4K de Gates se cargaba mediante cinta, permitiendo a los aficionados curiosear.
- **Conceptos básicos del reloj**: Un oscilador de cristal de 2 MHz impulsaba la CPU—ticks constantes a 2 millones de ciclos/segundo para buscar/ejecutar instrucciones.
- **Trucos de temporización**: No tenía un reloj incorporado para fechas; añadías una placa accesoria "Time Clock" (88-ACC) para interrupciones básicas o contadores. De lo contrario, bucles de software: p.ej., un bucle FOR-NEXT en BASIC para consumir ciclos y crear retardos (como `FOR I=1 TO 1000: NEXT I` para una "pausa" aproximada).
- **El enfoque de BASIC**: El Altair BASIC inicial no tenía función TIME$ (eso llegó después en Microsoft BASIC). El tiempo era relativo—contabas instrucciones o conectabas hardware externo como un chip de reloj en tiempo real (un accesorio raro).

En términos numéricos: A 2 MHz, una instrucción podía tomar 4-20 ciclos, así que ¿un retardo de 1 segundo? Bucle ~2 millones de veces. Brutal, pero nos enseñó eficiencia.

### La Arquitectura de Von Neumann (1945+): Ciclos como el Tick Universal
Von Neumann no construyó hardware (eso fue la máquina IAS en 1952), pero su plano—CPU, memoria, E/S comunicándose mediante un bus—sentó las bases. ¿El tiempo? Todo se trataba de ciclos sincronizados.
- **Rol del reloj**: Un reloj maestro (de cristal o de otro tipo) genera pulsos para buscar-decodificar-ejecutar instrucciones. Cada ciclo (flanco de subida/bajada) avanza el estado—sin superposición, puramente en serie.
- **Representación del tiempo**: Las instrucciones tomaban ciclos fijos (p.ej., sumar en 1-4 ticks), así que "tiempo" era conteo de ciclos. Para retardos, bifurcación basada en contadores; los relojes reales eran externos (como enchufes de pared o resets manuales).
- **Legado**: Este cuello de botella (datos/instrucciones compartiendo el bus) aún nos persigue—a la IA lo odia porque mover datos toma muchos más ciclos que procesarlos.

En términos de ecuación: Tiempo total = (instrucciones × ciclos/instr) / frecuencia del reloj. Para la IAS (inspirada en von Neumann): ~reloj de 1 MHz, así que máximo ~1 millón de ops/seg—¿tus 1.76B de segundos? Eso serían ~55 años de la IAS funcionando sin parar, pero se fundiría primero.

Estas configuraciones fueron precursores salvajes de la época de Unix—el tiempo como un contador, pero lo construías tú mismo. Si quieres profundizar más (como fragmentos de código para retardos en el Altair), ¡avísame!

[ENIAC Wikipedia](https://en.wikipedia.org/wiki/ENIAC)
[A Report on the ENIAC](https://ftp.arl.army.mil/mike/comphist/46eniac-report/chap1.html)
[Electronic Computing Circuits of the ENIAC](https://archive.computerhistory.org/resources/text/Knuth_Don_X4100/PDF_index/k-8-pdf/k-8-r5367-1-ENIAC-circuits.pdf)
[Organization of the Altair 8800](https://ubuntourist.codeberg.page/Altair-8800/part-2.html)
[MITS Altair 8800 Brochure](https://vtda.org/docs/computing/MITS/MITS_Altair8800ComputerSystem_Brochure.pdf)
[Von Neumann Architecture - Wikipedia](https://en.wikipedia.org/wiki/Von_Neumann_architecture)
[In a simple Von Neumann architecture, what exactly is a clock cycle?](https://www.quora.com/In-a-simple-Von-Neumann-architecture-what-exactly-is-a-clock-cycle)