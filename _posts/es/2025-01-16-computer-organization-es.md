---
audio: false
generated: false
lang: es
layout: post
title: Organización de Computadoras
translated: true
type: note
---

1. Definición: La Organización de Computadores se refiere a la estructura operativa e implementación de los sistemas informáticos, centrándose en cómo interactúan los componentes de hardware para ejecutar instrucciones.

2. Evolución Histórica: Rastrea el desarrollo desde las primeras computadoras mecánicas hasta los modernos procesadores multinúcleo.

3. Arquitectura Von Neumann: Un modelo fundamental donde la CPU, la memoria y las E/S están interconectadas a través de un bus.

4. Arquitectura Harvard: Separa el almacenamiento y las vías de señal para instrucciones y datos, mejorando el rendimiento.

5. Componentes de la CPU: Incluye la Unidad Aritmético-Lógica (ALU), la Unidad de Control (CU) y los Registros.

6. Funciones de la ALU: Realiza operaciones aritméticas y lógicas como suma, resta, AND, OR.

7. Rol de la Unidad de Control: Dirige la operación del procesador decodificando instrucciones y generando señales de control.

8. Registros: Pequeñas ubicaciones de almacenamiento rápido dentro de la CPU utilizadas para contener datos e instrucciones temporalmente.

9. Memoria Caché: Memoria de alta velocidad ubicada cerca de la CPU para reducir el tiempo de acceso a los datos.

10. Jerarquía de Memoria: Organiza la memoria en niveles basados en velocidad y costo, incluyendo registros, caché, RAM y almacenamiento secundario.

11. RAM (Memoria de Acceso Aleatorio): Memoria volátil utilizada para almacenar datos y código de máquina que se están utilizando actualmente.

12. ROM (Memoria de Solo Lectura): Memoria no volátil utilizada para almacenar firmware e instrucciones de arranque del sistema.

13. Estructura del Bus: Un sistema de comunicación que transfiere datos entre componentes dentro o fuera de una computadora.

14. Bus de Datos: Transporta los datos reales que se están procesando.

15. Bus de Direcciones: Transporta información sobre dónde deben enviarse o recuperarse los datos.

16. Bus de Control: Transporta señales de control desde la CPU a otros componentes.

17. Arquitectura del Conjunto de Instrucciones (ISA): Define el conjunto de instrucciones que una CPU puede ejecutar.

18. RISC (Computación de Conjunto de Instrucciones Reducido): Una filosofía de diseño ISA que utiliza un conjunto de instrucciones pequeño y altamente optimizado.

19. CISC (Computación de Conjunto de Instrucciones Complejo): Una ISA con un gran conjunto de instrucciones, algunas de las cuales pueden ejecutar tareas complejas.

20. Segmentación (Pipelining): Una técnica donde múltiples fases de instrucción se superponen para mejorar el rendimiento de la CPU.

21. Etapas de la Segmentación: Típicamente incluyen Búsqueda (Fetch), Decodificación (Decode), Ejecución (Execute), Acceso a Memoria (Memory Access) y Escritura (Write Back).

22. Riesgos en la Segmentación: Problemas como riesgos de datos, riesgos de control y riesgos estructurales que pueden interrumpir el flujo de la segmentación.

23. Predicción de Saltos (Branch Prediction): Un método para adivinar la dirección de las instrucciones de salto para mantener la segmentación llena.

24. Arquitectura Superscalar: Permite que múltiples instrucciones se procesen simultáneamente en una sola etapa de la segmentación.

25. Procesamiento Paralelo: Utilizar múltiples procesadores o núcleos para ejecutar instrucciones concurrentemente.

26. Procesadores Multinúcleo: CPUs con múltiples núcleos de procesamiento integrados en un solo chip.

27. SIMD (Instrucción Única, Múltiples Datos): Una arquitectura de procesamiento paralelo donde una sola instrucción opera sobre múltiples puntos de datos simultáneamente.

28. MIMD (Múltiples Instrucciones, Múltiples Datos): Una arquitectura paralela donde múltiples procesadores ejecutan diferentes instrucciones sobre diferentes datos.

29. Gestión de Memoria: Técnicas para gestionar y asignar memoria de manera eficiente, incluyendo paginación y segmentación.

30. Memoria Virtual: Extiende la memoria física al almacenamiento en disco, permitiendo a los sistemas manejar cargas de trabajo más grandes.

31. Paginación: Divide la memoria en páginas de tamaño fijo para simplificar la gestión de memoria y reducir la fragmentación.

32. Segmentación: Divide la memoria en segmentos de tamaño variable basados en divisiones lógicas como funciones o estructuras de datos.

33. Técnicas de Mapeo de Caché: Incluye cachés de mapeo directo, totalmente asociativo y asociativo por conjuntos.

34. Políticas de Reemplazo de Caché: Determina qué entrada de la caché reemplazar, como Menos Recientemente Usado (LRU) o Primero en Entrar, Primero en Salir (FIFO).

35. Coherencia de Caché: Garantiza la consistencia de los datos almacenados en múltiples cachés en un sistema multiprocesador.

36. Modelos de Consistencia de Memoria: Define el orden en que las operaciones parecen ejecutarse para mantener la consistencia del sistema.

37. Sistemas de Entrada/Salida (E/S): Gestiona la comunicación entre la computadora y los dispositivos externos.

38. Clasificación de Dispositivos de E/S: Incluye dispositivos de entrada, dispositivos de salida y dispositivos de almacenamiento.

39. Interfaces de E/S: Estándares como USB, SATA y PCIe que definen cómo los dispositivos se comunican con la placa base.

40. Acceso Directo a Memoria (DMA): Permite a los dispositivos transferir datos hacia/desde la memoria sin la intervención de la CPU.

41. Interrupciones: Señales que notifican a la CPU de eventos que requieren atención inmediata, permitiendo el procesamiento asíncrono.

42. Manejo de Interrupciones: El proceso mediante el cual la CPU responde a las interrupciones, incluyendo guardar el estado y ejecutar rutinas de servicio de interrupción.

43. Controladores DMA: Componentes de hardware que gestionan las operaciones DMA, liberando a la CPU de las tareas de transferencia de datos.

44. Controladores de Dispositivos (Device Drivers): Software que permite al sistema operativo comunicarse con los dispositivos de hardware.

45. Interconexión de Componentes Periféricos (PCI): Un estándar para conectar periféricos a la placa base.

46. Comunicación Serie vs. Paralela: La serie envía datos un bit a la vez, mientras que la paralela envía múltiples bits simultáneamente.

47. Puertos Serie: Interfaces como RS-232 utilizadas para comunicación serie con dispositivos.

48. Puertos Paralelos: Interfaces utilizadas para comunicación paralela, a menudo con impresoras y otros periféricos.

49. Arbitraje del Bus: El proceso de gestionar el acceso al bus entre múltiples dispositivos para prevenir conflictos.

50. Buses del Sistema vs. Buses Periféricos: Los buses del sistema conectan la CPU, la memoria y los componentes principales, mientras que los buses periféricos conectan dispositivos externos.

51. Tabla de Vectores de Interrupción: Una estructura de datos utilizada para almacenar las direcciones de las rutinas de servicio de interrupción.

52. Controladores Programables de Interrupciones: Hardware que gestiona múltiples solicitudes de interrupción y las prioriza.

53. Ancho del Bus: El número de bits que pueden transmitirse simultáneamente a través de un bus.

54. Velocidad del Reloj: La velocidad a la que una CPU ejecuta instrucciones, medida en GHz.

55. Ciclo de Reloj: La unidad de tiempo básica en la que una CPU puede realizar una operación básica.

56. Desfase del Reloj (Clock Skew): Diferencias en los tiempos de llegada de la señal de reloj a diferentes partes del circuito.

57. Distribución del Reloj: El método de entregar la señal de reloj a todos los componentes en la CPU.

58. Disipación de Calor: El proceso de eliminar el exceso de calor de la CPU para evitar el sobrecalentamiento.

59. Soluciones de Refrigeración: Incluye disipadores de calor, ventiladores y sistemas de refrigeración líquida utilizados para gestionar las temperaturas de la CPU.

60. Unidades de Fuente de Alimentación (PSUs): Proporcionan la energía necesaria a todos los componentes de la computadora.

61. Reguladores de Voltaje: Aseguran que se entreguen niveles de voltaje estables a la CPU y otros componentes.

62. Arquitectura de la Placa Base: La placa de circuito principal que aloja la CPU, la memoria y otros componentes críticos.

63. Chipsets: Grupos de circuitos integrados que gestionan el flujo de datos entre la CPU, la memoria y los periféricos.

64. Firmware: Software permanente programado en una memoria de solo lectura que controla las funciones del hardware.

65. BIOS/UEFI: Interfaces de firmware que inicializan el hardware durante el proceso de arranque y proporcionan servicios en tiempo de ejecución.

66. Proceso de Arranque: La secuencia de operaciones que inicializa el sistema cuando se enciende.

67. Etapas de la Segmentación de Instrucciones: Típicamente incluyen Búsqueda, Decodificación, Ejecución, Acceso a Memoria y Escritura.

68. Profundidad de la Segmentación: El número de etapas en una segmentación, afectando el rendimiento y la latencia de las instrucciones.

69. Equilibrado de la Segmentación: Asegurar que cada etapa tenga un tiempo de ejecución aproximadamente igual para maximizar la eficiencia.

70. Riesgos de Datos: Situaciones donde las instrucciones dependen de los resultados de instrucciones anteriores en una segmentación.

71. Riesgos de Control: Ocurren debido a instrucciones de salto que interrumpen el flujo de la segmentación.

72. Riesgos Estructurales: Suceden cuando los recursos de hardware son insuficientes para soportar todas las ejecuciones de instrucciones posibles simultáneamente.

73. Reenvío (Data Bypassing): Una técnica para reducir los riesgos de datos enrutando datos directamente entre etapas de la segmentación.

74. Parada (Burbuja en la Segmentación): Insertar ciclos de inactividad en la segmentación para resolver riesgos.

75. Ejecución Fuera de Orden: Ejecutar instrucciones a medida que los recursos están disponibles en lugar de en el orden original del programa.

76. Ejecución Especulativa: Ejecutar instrucciones antes de saber si son necesarias, para mejorar el rendimiento.

77. Algoritmos de Predicción de Saltos: Técnicas como predicción estática, predicción dinámica y predicción adaptativa de dos niveles utilizadas para adivinar direcciones de salto.

78. Paralelismo a Nivel de Instrucción (ILP): La capacidad de ejecutar múltiples instrucciones simultáneamente dentro de un solo ciclo de CPU.

79. Desenrollado de Bucles (Loop Unrolling): Una técnica de optimización que aumenta el cuerpo de los bucles para disminuir la sobrecarga del control del bucle.

80. Superpipelining: Aumentar el número de etapas de la segmentación para permitir velocidades de reloj más altas.

81. VLIW (Palabra de Instrucción Muy Larga): Una arquitectura que permite codificar múltiples operaciones en una sola palabra de instrucción.

82. EPIC (Computación de Instrucciones Explícitamente Paralelas): Una arquitectura que permite la ejecución paralela de instrucciones mediante la asistencia del compilador.

83. Renombrado de Registros: Una técnica para eliminar dependencias de datos falsas mediante la asignación dinámica de registros.

84. Hyper-Threading: Tecnología de Intel que permite que un solo núcleo de CPU ejecute múltiples hilos simultáneamente.

85. Niveles de Memoria Caché: Cachés L1 (más cercana a la CPU, más rápida), L2 y L3 con tamaño y latencia crecientes.

86. Cachés de Escritura Inmediata (Write-Through) vs. Escritura Diferida (Write-Back): La escritura inmediata actualiza tanto la caché como la memoria simultáneamente, mientras que la escritura diferida actualiza solo la caché y difiere las actualizaciones de memoria.

87. Asociatividad en Cachés: Determina cómo se mapean las líneas de caché a los conjuntos de caché, afectando las tasas de acierto y los tiempos de acceso.

88. Prebúsqueda (Prefetching): Cargar datos en la caché antes de que se soliciten realmente para reducir la latencia de acceso.

89. Patrones de Acceso a Memoria: Acceso secuencial vs. aleatorio y su impacto en el rendimiento de la caché.

90. NUMA (Acceso a Memoria No Uniforme): Un diseño de memoria donde el tiempo de acceso a la memoria varía según la ubicación de la memoria en relación con un procesador.

91. SMP (Multiprocesamiento Simétrico): Un sistema donde múltiples procesadores comparten una única memoria centralizada.

92. Sistemas de Memoria Distribuida: Sistemas donde cada procesador tiene su propia memoria privada, comunicándose a través de una red.

93. Redes de Interconexión: La topología y los protocolos utilizados para conectar múltiples procesadores y unidades de memoria.

94. Escalabilidad: La capacidad de un sistema informático para aumentar el rendimiento añadiendo más recursos.

95. Tolerancia a Fallos: La capacidad de un sistema para continuar operando correctamente en caso de fallo de algunos de sus componentes.

96. Redundancia: Incorporar componentes adicionales para aumentar la fiabilidad y disponibilidad.

97. Detección y Corrección de Errores: Técnicas como bits de paridad, sumas de comprobación (checksums) y Código Corrector de Errores (ECC) para identificar y corregir errores de datos.

98. Eficiencia Energética: Diseñar sistemas para minimizar el consumo de energía manteniendo el rendimiento.

99. Potencia de Diseño Térmico (TDP): La cantidad máxima de calor que se espera que genere una CPU o GPU bajo cargas de trabajo típicas.

100. Tendencias Futuras: Explorando avances como la computación cuántica, las arquitecturas neuromórficas y los procesadores fotónicos que están dando forma al futuro de la organización de computadores.