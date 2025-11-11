---
audio: false
lang: es
layout: post
title: Inmersión en Microcomputadoras - Conversación
translated: true
type: note
---

A: Últimamente he estado revisando la arquitectura de microcomputadoras. ¿Podemos comenzar comparando las arquitecturas von Neumann y Harvard?

B: ¡Absolutamente! Von Neumann utiliza un único bus para datos e instrucciones, lo que puede causar cuellos de botella. Harvard los separa, permitiendo lecturas paralelas—común en DSPs y microcontroladores. ¿Qué caso de uso te interesa más?

A: Sistemas embebidos, en realidad. Harvard parece dominar allí. Pero ¿cómo las arquitecturas híbridas modernas como las Harvard modificadas salvan la brecha?

B: ¡Excelente pregunta! Los híbridos usan cachés separados (L1 para instrucciones/datos) pero un espacio de memoria unificado. Mira ARM Cortex-M: es similar a Harvard por velocidad pero simplifica la programación. ¿Compensaciones?

A: Compensaciones, ciertamente. La memoria unificada facilita el desarrollo pero sacrifica rendimiento. ¿Crees que la flexibilidad de RISC-V podría disruptir este espacio?

B: ¡Potencialmente! El ISA modular de RISC-V permite a los diseñadores añadir características tipo Harvard por aplicación. Para dispositivos IoT edge, eso es un cambio radical. Pero el ecosistema de ARM está consolidado. ¿Cuál es tu opinión?

A: Los ecosistemas son pegajosos, pero el modelo de código abierto de RISC-V podría acelerar optimizaciones de nicho. Cambiando de tema—¿qué tan crítica es la DMA en los microcontroladores modernos?

B: ¡Crucial! Descargar transferencias de datos (ej., ADC a memoria) ahorra ciclos de CPU. La DMA de STM32 incluso maneja transferencias periférico-a-periférico. ¿Has trabajado con buffers DMA circulares?

A: Sí, para procesamiento de audio. Pero configurar los modos de ráfaga fue complicado. ¿Cómo prioriza la DMA las solicitudes cuando múltiples periféricos compiten?

B: La prioridad típicamente es configurable por hardware. Los MCUs de NXP usan round-robin ponderado, mientras que algunas partes de TI permiten reprioritización dinámica. La latencia de interrupciones se convierte en un factor—¿alguna vez la mediste?

A: Solo empíricamente. Hablando de interrupciones, ¿cómo los RTOS como FreeRTOS manejan ISRs anidadas diferente al bare-metal?

B: Los RTOS añaden capas: guardado de contexto, invocaciones del planificador post-ISR. Las APIs 'FromISR' de FreeRTOS gestionan esto de forma segura. Pero los ISRs en bare-metal son más ligeros—compensación entre complejidad y control.

A: Tiene sentido. Para sistemas de tiempo real estricto, ¿recomendarías alguna vez un superloop sobre un RTOS?

B: ¡Solo para sistemas triviales! Los superloops luchan con tareas multi-tasa. Un RTOS adecuadamente ajustado con herencia de prioridad evita la inversión de prioridad. Las mejoras recientes de Zephyr valen la pena explorar.

A: El modelo de device tree de Zephyr es intrigante. ¿Cómo se compara con el de Linux para uso embebido?

B: El DT de Linux es pesado para microcontroladores. Kconfig + devicetree de Zephyr logra un equilibrio—la configuración estática reduce la sobrecarga en tiempo de ejecución. ¿Has portado algún driver entre ambos?

A: Todavía no, pero he visto que la API GPIO de Zephyr abstrae bien las peculiaridades del hardware. ¿Cuál es tu opinión sobre E/S mapeada en memoria vs. E/S mapeada en puertos para micros?

B: ¡La mapeada en memoria domina ahora—el direccionamiento unificado simplifica los compiladores. El E/S de puerto heredado de x86 persiste por compatibilidad hacia atrás. ¡El MMIO de ARM incluso maneja bit-banding para acceso atómico!

A: ¡El bit-banding es un salvavidas para variables compartidas! Pero ¿qué hay de las memorias RAM no volátiles emergentes como MRAM? ¿Podría disruptir la jerarquía de memoria?

B: La persistencia + velocidad de MRAM es prometedora, pero el costo/resistencia va a la zaga. Por ahora, es de nicho—piensa en registro de datos de naves espaciales. Los NVDIMMs podrían llegar a los micros más pronto. ¿Has evaluado FRAM vs. Flash?

A: Sí—la velocidad de escritura de FRAM supera por mucho a Flash, pero la densidad es un problema. Cambiando a interfaces: ¿está SPI perdiendo terreno frente a I3C en los hubs de sensores?

B: Las interrupciones multi-drop e in-band de I3C son convincentes, pero la simplicidad de SPI lo mantiene vivo. Los sensores MEMS todavía usan SPI por defecto. ¿Has probado el direccionamiento dinámico de I3C?

A: Todavía no—mi proyecto actual usa QSPI para Flash NOR externa. Hablando de almacenamiento, ¿cómo se compara eMMC con las tarjetas SD para temperaturas industriales?

B: La confiabilidad soldada de eMMC supera a los conectores de SD en entornos propensos a vibraciones. Pero SD es extraíble para actualizaciones en campo. La NAND SLC sigue siendo el rey por longevidad. ¿Alguna vez encontraste errores de wear-leveling?

A: Una vez—una mala implementación FTL bloqueó un registrador. Hablemos de seguridad: ¿cómo están manejando los micros las mitigaciones de Spectre/Meltdown?

B: TrustZone de Cortex-M33 ayuda, pero los ataques de temporización aún acechan las cachés. Los fabricantes de silicio están añadiendo barreras de ejecución especulativa. El verificador de préstamos de Rust podría prevenir algunas explotaciones—¿lo estás adoptando?

A: Experimentalmente—la curva de aprendizaje es pronunciada. Volviendo al hardware: ¿alguna opinión sobre las extensiones vectoriales de RISC-V para cargas de trabajo DSP?

B: ¡La modularidad de RVV es brillante! Es como ARM NEON pero escalable. Para tinyML, podría desplazar los núcleos DSP propietarios. ¿Has visto benchmarks vs. Cadence Tensilica?

A: Todavía no, pero estoy considerando un MCU RISC-V + RVV para control de motores. Lo que me lleva a los periféricos PWM—¿qué tan crucial es la inserción de dead-time en hardware?

B: ¡Vital para los puentes H! Los temporizadores por software no pueden igualar la precisión de nanosegundos de los bloques dedicados. Aunque el HRTIM de ST es excesivo para la mayoría. ¿Has usado alguna vez un CPLD para PWM personalizado?

A: Una vez—16 canales sincronizados para matrices de LED. Pero los MCUs modernos como el PIO del RP2040 están robando ese nicho. ¿Qué tan programable es demasiado programable?

B: ¡El PIO es un cambio radical! Pero depurar máquinas de estado se vuelve complicado. Los xCORE de XMOS aún ganan en multi-cores de tiempo real estricto. ¿Dónde trazas la línea entre MCU y FPGA?

A: Cuando las demandas de latencia requieren determinismo de sub-microsegundo, los FPGAs mandan. Pero los iCE40 de Lattice + núcleos soft RISC-V difuminan las líneas. ¿Has probado Chisel para co-diseño hardware/software?

B: El aumento de productividad con Chisel es increíble—generar Verilog desde Scala ahorra meses. Pero la cadena de herramientas aún está madurando. Hablando de tendencias, ¿cómo evolucionarán los micros basados en chiplets?

A: Los chiplets podrían permitirnos mezclar y combinar núcleos RISC-V con chiplets analógicos. Pero los costos del interposer deben bajar. El fabric 3D de TSMC es prometedor. ¿Veremos chiplets de código abierto?

B: ¡El OpenMPW de Google lo sugiere! Pero las herramientas EDA siguen siendo una barrera. Mientras tanto, lo analógico sigue siendo un arte oscuro—¿cómo maneja tu equipo la validación mixed-signal?

A: Mucha co-simulación SPICE + Python. Pero volviendo a lo digital: ¿alguna opinión sobre los micros basados en memristores para computación neuromórfica?

B: Siguen siendo rarezas de laboratorio—la variabilidad mata el rendimiento. Pero para IA en el edge, los arreglos de computación en memoria analógica (como los de Mythic) están más cerca de la producción. ¿Los has evaluado contra aceleradores de NN cuantizados?

A: Todavía no, pero soy escéptico sobre la precisión de lo analógico. Cambiando a energía: ¿qué tan bajo pueden llegar realistamente los diseños CMOS subthreshold?

B: ¡El Apollo4 de Ambiq alcanza ~6µA/MHz! Pero la fuga domina por debajo de 28nm. La recolección de energía es la siguiente frontera—¿Has usado un PMIC como el BQ25504?

A: Sí—solar + supercondensadores para una estación meteorológica. Pero los algoritmos MPPT necesitan ajuste. Pregunta final: ¿los co-procesadores cuánticos se integrarán alguna vez con los micros?

B: ¡Falta décadas para algo práctico! Pero se están investigando interfaces criogénicas CMOS. Por ahora, ¡me emocionan más los interconectores fotónicos en microservidores. Gracias por la inmersión profunda!