---
audio: false
generated: false
lang: es
layout: post
title: Fundamentos de la Electrónica
translated: true
type: note
---

### Componentes Electrónicos Básicos

1. Tipos de Resistencias: Las resistencias limitan el flujo de corriente en un circuito. Los tipos incluyen resistencias fijas, que tienen un valor de resistencia fijo, y resistencias variables como los potenciómetros, que permiten una resistencia ajustable.

2. Tipos de Condensadores: Los condensadores almacenan y liberan energía eléctrica. Los tipos incluyen condensadores cerámicos, que se utilizan comúnmente para aplicaciones de alta frecuencia, y condensadores electrolíticos, que tienen valores de capacitancia más altos pero están polarizados.

3. Inductores: Los inductores almacenan energía en un campo magnético y se oponen a los cambios en la corriente. Se utilizan en aplicaciones de filtrado y sintonización.

4. Diodos: Los diodos permiten que la corriente fluya en una sola dirección. Los diodos Zener se utilizan para la regulación de voltaje, mientras que los LED emiten luz cuando están polarizados en directa.

5. Transistores: Los transistores, como los BJT, actúan como interruptores o amplificadores electrónicos, con tipos NPN y PNP que controlan el flujo de corriente en los circuitos.

6. Transistor de Efecto de Campo (FET): Los FET controlan el flujo de corriente aplicando voltaje a la puerta, siendo los MOSFET ampliamente utilizados para conmutación y amplificación.

7. Fotodiodos: Estos diodos generan una corriente cuando se exponen a la luz, utilizados en aplicaciones ópticas como sensores de luz.

8. Optoacopladores: Se utilizan para aislar diferentes partes de un circuito, los optoacopladores transmiten señales eléctricas a través de la luz para mantener el aislamiento eléctrico.

9. Rectificadores: Los diodos se utilizan en circuitos rectificadores para convertir energía CA a CC. Los rectificadores de media onda utilizan un solo diodo, mientras que los rectificadores de onda completa utilizan dos o más diodos para convertir ambas mitades de la onda CA.

10. Termistores: Estos son resistencias sensibles a la temperatura. Los termistores de coeficiente de temperatura negativo (NTC) disminuyen la resistencia a medida que aumenta la temperatura, mientras que los termistores de coeficiente de temperatura positivo (PTC) aumentan la resistencia con temperaturas más altas.

---

### Teoría de Circuitos Electrónicos

11. Ley de Ohm: La Ley de Ohm relaciona el voltaje (V), la corriente (I) y la resistencia (R) en un circuito lineal: \\(V = I \times R\\). Forma la base para la mayoría del análisis de circuitos eléctricos.

12. Leyes de Kirchhoff: La Ley de Corrientes de Kirchhoff (LCK) establece que la suma de las corrientes que entran en un nodo es igual a la suma de las corrientes que salen, mientras que la Ley de Voltajes de Kirchhoff (LVK) establece que la suma de los voltajes en un lazo cerrado es cero.

13. Teorema de Thévenin: Este teorema simplifica una red de resistencias y fuentes en una fuente de voltaje y una resistencia equivalentes para facilitar el análisis.

14. Teorema de Norton: Similar al de Thévenin, el teorema de Norton simplifica una red en una fuente de corriente y una resistencia en paralelo para facilitar el análisis de circuitos controlados por corriente.

15. Teorema de Superposición: En circuitos con múltiples fuentes, este teorema permite analizar cada fuente de forma independiente y luego combinar los resultados.

16. Análisis de Mallas: Un método utilizado para encontrar corrientes desconocidas en un circuito utilizando corrientes de malla, a menudo aplicado en circuitos planares.

17. Método de Voltajes de Nodo: Un método utilizado para resolver circuitos asignando voltajes a los nodos (uniones) y resolviendo para las incógnitas.

18. Impedancia y Admitancia: La impedancia es la oposición total a la corriente en circuitos de CA, combinando resistencia y reactancia. La admitancia es la inversa de la impedancia, que describe la facilidad con la que la corriente fluye a través de un componente.

19. Potencia en Circuitos de CA: En circuitos de CA, la potencia se divide en potencia real (activa), potencia reactiva y potencia aparente. El factor de potencia representa la relación entre la potencia real y la potencia aparente.

20. Resonancia: La resonancia ocurre en circuitos LC cuando la reactancia inductiva y la reactancia capacitiva son iguales en magnitud pero opuestas en fase, permitiendo una transferencia máxima de energía.

---

### Circuitos con Diodos

21. Teoría Básica de Diodos: Los diodos permiten que la corriente fluya solo en condición de polarización directa (positivo al ánodo, negativo al cátodo) y bloquean la corriente en polarización inversa.

22. Circuitos Rectificadores: Los rectificadores de media onda utilizan un solo diodo, mientras que los rectificadores de onda completa utilizan dos o cuatro diodos para convertir CA a CC. Los rectificadores en puente son comunes en circuitos de fuentes de alimentación.

23. Circuitos Recortadores: Estos circuitos limitan el nivel de voltaje recortando la forma de onda en un cierto umbral. Se utilizan en conformación de ondas y protección de señales.

24. Circuitos Sujetadores: Estos circuitos desplazan el nivel de voltaje de una forma de onda, utilizados a menudo para establecer un voltaje de referencia o eliminar oscilaciones negativas en una señal.

25. Diodo Zener: Los diodos Zener están diseñados para operar en ruptura inversa, manteniendo un voltaje constante en un amplio rango de corrientes, comúnmente utilizados para regulación de voltaje.

26. LEDs: Los Diodos Emisores de Luz emiten luz cuando la corriente fluye a través de ellos. Son ampliamente utilizados en pantallas, indicadores e iluminación de fondo.

27. Aplicaciones de los Diodos: Los diodos se utilizan en detección de señales, rectificación de potencia, regulación de voltaje y en sistemas de comunicación como moduladores o demoduladores.

---

### Circuitos con Transistores

28. Características del BJT: Los BJT tienen tres regiones: emisor, base y colector. La corriente que fluye desde la base controla la corriente mayor entre el emisor y el colector.

29. Polarización de Transistores: La polarización de transistores establece un punto de operación en la región activa. Los métodos comunes incluyen polarización fija, polarización por divisor de voltaje y estabilización por emisor.

30. Amplificador Emisor Común: Esta es una de las configuraciones de amplificador con transistor más utilizadas, que proporciona una buena ganancia de voltaje pero con una inversión de fase.

31. Amplificador Colector Común: También conocido como seguidor de emisor, este circuito tiene ganancia de voltaje unitaria y alta impedancia de entrada, útil para adaptación de impedancia.

32. Amplificador Base Común: Típicamente utilizado en aplicaciones de alta frecuencia, proporciona alta ganancia de voltaje pero baja impedancia de entrada.

33. Circuitos de Conmutación: Los transistores pueden usarse como interruptores digitales, encendiendo y apagando dispositivos en circuitos lógicos y sistemas digitales.

34. Par Darlington: Una combinación de dos transistores que proporciona una alta ganancia de corriente. A menudo se utiliza cuando se necesita una alta amplificación de corriente.

35. Regiones de Saturación y Corte: Un transistor opera en saturación cuando está completamente encendido (actúa como un interruptor cerrado) y en corte cuando está completamente apagado (actúa como un interruptor abierto).

---

### Circuitos con Transistores de Efecto de Campo

36. Características del JFET: El Transistor de Efecto de Campo de Unión (JFET) se controla por el voltaje en la puerta, con corriente fluyendo entre la fuente y el drenador. La puerta está polarizada inversamente, y la corriente de drenador depende del voltaje puerta-fuente.

37. Tipos de MOSFET: Los MOSFET (Transistores de Efecto de Campo de Metal-Óxido-Semiconductor) se utilizan comúnmente para conmutación y amplificación. Vienen en dos tipos: modo de enriquecimiento (normalmente apagado) y modo de agotamiento (normalmente encendido).

38. Operación del MOSFET: El MOSFET opera creando un canal conductor entre la fuente y el drenador, controlado por el voltaje aplicado a la puerta.

39. Amplificador Fuente Común: Esta configuración se utiliza para amplificación de voltaje, ofreciendo alta ganancia e impedancia de entrada/salida moderada.

40. Amplificador Drenador Común: Conocido como seguidor de fuente, este amplificador ofrece baja impedancia de salida, lo que lo hace adecuado para adaptación de impedancia.

41. Amplificador Puerta Común: Esta configuración se utiliza en aplicaciones de alta frecuencia, proporcionando baja impedancia de entrada y alta impedancia de salida.

42. Polarización de FET: Los FET generalmente se polarizan utilizando resistencias y fuentes de voltaje para garantizar que operen en la región deseada (por ejemplo, región de estrangulamiento para MOSFETs).

43. Aplicaciones de FET: Los FET se utilizan ampliamente en amplificadores de bajo ruido, aplicaciones de RF y como resistencias controladas por voltaje en circuitos analógicos.

---

### Amplificadores

44. Tipos de Amplificadores: Los amplificadores se pueden clasificar según su operación como amplificadores de voltaje (amplifican voltaje), amplificadores de corriente (amplifican corriente) y amplificadores de potencia (amplifican ambos).

45. Amplificadores con Transistores: Las tres configuraciones principales—emisor común, colector común y base común—cada una proporciona características únicas de impedancia y ganancia.

46. Amplificadores Operacionales (Op-Amps): Los Op-Amps son amplificadores versátiles con alta ganancia. Las aplicaciones comunes incluyen amplificación diferencial, filtrado de señales y operaciones matemáticas.

47. Ganancia de los Amplificadores: La ganancia de un amplificador se refiere a cuánto se amplifica la señal de entrada. Se puede definir en términos de ganancia de voltaje, corriente o potencia, dependiendo de la aplicación.

48. Realimentación en Amplificadores: La realimentación en amplificadores puede ser negativa (reduce la ganancia y estabiliza el sistema) o positiva (aumenta la ganancia y potencialmente conduce a inestabilidad).

49. Realimentación de Voltaje y Corriente: Los amplificadores con realimentación de voltaje ajustan la salida basándose en el voltaje de entrada, mientras que los amplificadores con realimentación de corriente ajustan la salida basándose en la corriente de entrada, afectando el ancho de banda y la velocidad de respuesta.

50. Ancho de Banda de los Amplificadores: Los amplificadores típicamente muestran una compensación entre ancho de banda y ganancia. Una ganancia más alta a menudo conduce a un ancho de banda reducido y viceversa.

51. Amplificadores de Potencia: Se utilizan para amplificar señales a un nivel adecuado para impulsar altavoces, motores u otros dispositivos que consumen mucha potencia. Las clases A, B, AB y C definen diferentes características de eficiencia y linealidad.

52. Adaptación de Impedancia: Esto asegura la transferencia máxima de potencia entre componentes haciendo coincidir las impedancias de la fuente y la carga.

---

### Osciladores

53. Osciladores Sinusoidales: Estos osciladores generan formas de onda sinusoidales, comúnmente utilizadas en aplicaciones de radiofrecuencia (RF) y audio. Ejemplos incluyen los osciladores Colpitts y Hartley.

54. Osciladores de Relajación: Se utilizan para generar formas de onda no sinusoidales, típicamente ondas cuadradas o en diente de sierra, y se utilizan en aplicaciones de temporización y reloj.

55. Osciladores de Cristal: Los osciladores de cristal utilizan un cristal de cuarzo para generar una frecuencia altamente estable. Son ampliamente utilizados en relojes, radios y sistemas GPS.

56. Bucle de Enclavamiento por Fase (PLL): Un PLL se utiliza para síntesis de frecuencia y sincronización, a menudo utilizado en sistemas de comunicación para modular y demodular señales.

---

### Fuentes de Alimentación

57. Reguladores Lineales: Estos reguladores mantienen un voltaje de salida constante disipando el exceso de voltaje como calor. Son simples pero menos eficientes para aplicaciones de alta potencia.

58. Reguladores Conmutados: Los reguladores conmutados (buck, boost y buck-boost) convierten el voltaje de entrada a un voltaje de salida deseado con mayor eficiencia en comparación con los reguladores lineales.

59. Rectificadores y Filtros: Las fuentes de alimentación a menudo incluyen rectificadores para convertir CA a CC, seguidos de filtros (por ejemplo, condensadores) para suavizar la salida.

60. Técnicas de Regulación: La regulación de voltaje mantiene un voltaje de salida constante a pesar de las variaciones en la carga o el voltaje de entrada. Los reguladores lineales utilizan un transistor de paso, mientras que los reguladores conmutados utilizan componentes inductivos y capacitivos.

61. Corrección del Factor de Potencia (PFC): Esta técnica se utiliza en fuentes de alimentación para reducir la diferencia de fase entre el voltaje y la corriente, mejorando la eficiencia y reduciendo la distorsión armónica.

---

### Circuitos de Comunicación

62. Modulación de Amplitud (AM): AM es una técnica donde la amplitud de una onda portadora varía en proporción a la señal moduladora, comúnmente utilizada en radiodifusión.

63. Modulación de Frecuencia (FM): FM implica variar la frecuencia de una onda portadora de acuerdo con la señal de entrada, comúnmente utilizada para radiodifusión de mayor fidelidad.

64. Modulación de Fase (PM): En PM, la fase de la onda portadora varía en respuesta a la señal de entrada.

65. Modulación por Código de Pulsos (PCM): PCM es un método utilizado para representar digitalmente señales analógicas mediante el muestreo y la cuantificación de la señal en valores discretos.

66. Multiplexación por División de Frecuencia (FDM): FDM implica dividir el espectro de frecuencia disponible en sub-bandas más pequeñas, cada una llevando una señal diferente, ampliamente utilizada en sistemas de telecomunicaciones.

67. Multiplexación por División de Tiempo (TDM): TDM divide el tiempo en intervalos discretos y asigna cada intervalo a una señal diferente, permitiendo que múltiples señales compartan el mismo medio de transmisión.

68. Circuitos Modulador y Demodulador: Estos circuitos modulan una señal de entrada para transmisión y demodulan las señales recibidas de vuelta a su forma original.

---

### Procesamiento de Señales

69. Filtros: Los filtros se utilizan para eliminar componentes no deseados de una señal. Los tipos incluyen filtros paso bajo, paso alto, paso banda y elimina banda, cada uno diseñado para pasar ciertas frecuencias mientras atenúa otras.

70. Amplificación: La amplificación de señales aumenta la fuerza de una señal sin alterar sus componentes de frecuencia. Los amplificadores se pueden usar en varias configuraciones, como en preamplificadores, amplificadores de potencia y amplificadores diferenciales.

71. Procesamiento Digital de Señales (DSP): DSP es la manipulación de señales utilizando técnicas digitales. Implica muestreo, cuantificación y la aplicación de algoritmos como transformadas de Fourier, convolución y filtrado para procesar señales.

72. Conversión Analógica a Digital (ADC): Los ADC convierten señales analógicas continuas en datos digitales discretos. Son esenciales para interconectar sensores analógicos con sistemas digitales.

73. Conversión Digital a Analógica (DAC): Los DAC realizan la operación inversa a los ADC, convirtiendo datos digitales discretos de vuelta en señales analógicas continuas para su uso en actuadores y otros dispositivos analógicos.

74. Transformada de Fourier: La transformada de Fourier es una técnica matemática utilizada para analizar el contenido de frecuencia de una señal. Es ampliamente utilizada en procesamiento de señales, comunicaciones y sistemas de control.

75. Teorema de Muestreo: El teorema de muestreo de Nyquist-Shannon establece que para reconstruir con precisión una señal, debe muestrearse al menos al doble de la frecuencia más alta presente en la señal.

---

### Comunicación Inalámbrica

76. Técnicas de Modulación: La modulación se refiere a variar una señal portadora de acuerdo con la señal de información. Las técnicas comunes incluyen Modulación de Amplitud (AM), Modulación de Frecuencia (FM), Modulación de Fase (PM) y esquemas más avanzados como la Modulación de Amplitud en Cuadratura (QAM) utilizada en comunicaciones digitales.

77. Antenas: Las antenas se utilizan para transmitir y recibir ondas electromagnéticas. Los tipos de antenas incluyen antenas dipolo, antenas de lazo, antenas parabólicas y antenas de parche, cada una adecuada para diferentes aplicaciones en sistemas de comunicación inalámbrica.

78. Comunicación por Radiofrecuencia (RF): La comunicación RF implica transmitir datos a través de ondas de radio. Los sistemas RF se utilizan en redes celulares, Wi-Fi, Bluetooth y comunicación por satélite, con frecuencias que van desde unos pocos MHz hasta varios GHz.

79. Redes Inalámbricas: Las redes inalámbricas conectan dispositivos sin cables físicos. Las tecnologías incluyen Wi-Fi, Bluetooth, Zigbee y 5G, cada una con casos de uso específicos para comunicación de corto o largo alcance, transferencia de datos de alta velocidad y aplicaciones IoT.

80. Espectro Expandido: El espectro expandido es una técnica utilizada en comunicación inalámbrica para distribuir una señal a través de una banda de frecuencia amplia, aumentando la resistencia a las interferencias y mejorando la seguridad. Las técnicas incluyen Espectro Expandido por Secuencia Directa (DSSS) y Espectro Expandido por Salto de Frecuencia (FHSS).

81. Comunicación por Microondas: La comunicación por microondas utiliza ondas de radio de alta frecuencia (típicamente de 1 GHz a 100 GHz) para comunicación punto a punto, incluyendo enlaces satelitales, sistemas de radar y enlaces de datos de alta velocidad.

82. Protocolos Inalámbricos: Los protocolos inalámbricos definen cómo se transmiten los datos en una red inalámbrica. Ejemplos incluyen IEEE 802.11 (Wi-Fi), IEEE 802.15 (Bluetooth) y Zigbee, cada uno con diferentes características para velocidad de datos, alcance y consumo de energía.

---

### Sistemas Embebidos

83. Microcontroladores: Los microcontroladores son pequeñas computadoras integradas en un solo chip, utilizadas en sistemas embebidos para controlar dispositivos como sensores, motores y pantallas. Los microcontroladores populares incluyen Arduino, Raspberry Pi y microcontroladores PIC.

84. Sistemas Operativos de Tiempo Real (RTOS): Un RTOS es un sistema operativo diseñado para aplicaciones de tiempo real donde las tareas deben completarse dentro de restricciones de tiempo estrictas. Ejemplos incluyen FreeRTOS, RTEMS y VxWorks.

85. Programación Embebida: La programación embebida implica escribir software para microcontroladores y otros dispositivos embebidos. Requiere conocimiento de lenguajes de programación de bajo nivel como C y ensamblador, así como de interfaz de hardware y optimización.

86. Sensores y Actuadores: Los sensores son dispositivos que detectan propiedades físicas como temperatura, luz o movimiento, mientras que los actuadores se utilizan para interactuar con el mundo físico, como mover un motor o controlar una válvula. Estos son componentes esenciales en sistemas IoT y de automatización.

87. Interfaz: Los sistemas embebidos a menudo requieren interfaz con componentes externos como pantallas, sensores y módulos de comunicación. Las técnicas de interfaz incluyen I2C, SPI, UART y GPIO.

88. Gestión de Energía: La gestión de energía es crucial en sistemas embebidos para optimizar el consumo de energía, especialmente para dispositivos alimentados por batería. Las técnicas incluyen modos de ahorro de energía, reguladores de voltaje y diseño de circuitos eficientes.

---

### Electrónica de Potencia

89. Diodos de Potencia: Los diodos de potencia se utilizan para controlar el flujo de corriente en aplicaciones de alta potencia, como rectificar energía CA a CC. Están diseñados para manejar voltajes y corrientes más altos que los diodos regulares.

90. Tiristores: Un tipo de dispositivo semiconductor utilizado para conmutar y controlar grandes cantidades de potencia. Los tiristores incluyen SCR (Rectificadores Controlados de Silicio) y TRIACs, comúnmente utilizados en control de motores, iluminación y regulación de potencia.

91. MOSFETs de Potencia: Los MOSFETs de potencia se utilizan para conmutación y amplificación en circuitos de electrónica de potencia, particularmente en fuentes de alimentación, drives de motores e inversores, debido a su alta eficiencia y características de conmutación rápida.

92. IGBTs (Transistores Bipolares de Puerta Aislada): Los IGBT combinan las características de los BJT y los MOSFET y se utilizan en aplicaciones de alta potencia como inversores, drives de motores y sistemas de calentamiento por inducción.

93. Convertidores CC-CC: Los convertidores CC-CC se utilizan para convertir un nivel de voltaje CC a otro, ya sea aumentando (convertidores boost) o reduciendo (convertidores buck) el voltaje, con alta eficiencia.

94. Convertidores CA-CC: Estos convertidores, también conocidos como rectificadores, se utilizan para convertir corriente alterna (CA) a corriente continua (CC). Son ampliamente utilizados en fuentes de alimentación y en aplicaciones donde se requiere voltaje CC.

95. Inversores: Los inversores convierten CC a potencia CA y se utilizan en sistemas de energía renovable, SAI (Sistemas de Alimentación Ininterrumpida) y vehículos eléctricos.

96. Control de Potencia: El control de potencia en sistemas electrónicos implica regular los niveles de voltaje y corriente para un uso eficiente de la energía, a menudo a través de bucles de realimentación, modulación y reguladores conmutados.

---

### Sistemas de Automatización y Control

97. Controladores Lógicos Programables (PLCs): Los PLCs son computadoras digitales utilizadas para la automatización en procesos industriales, como la fabricación, el control de maquinaria y la gestión de sistemas como ascensores o semáforos.

98. Sistemas SCADA: Los sistemas SCADA (Control de Supervisión y Adquisición de Datos) se utilizan para monitorear y controlar procesos industriales, incluida la generación de energía, el tratamiento de agua y los sistemas de fabricación.

99. Sensores Industriales: Los sensores industriales se utilizan para medir parámetros físicos como temperatura, presión, flujo y nivel en aplicaciones de automatización industrial.

100. Control de Motores: Los sistemas de control de motores se utilizan para regular la velocidad, dirección y operación de motores, incluidos motores CC, motores CA y motores paso a paso. Estos sistemas son cruciales en automatización y robótica.