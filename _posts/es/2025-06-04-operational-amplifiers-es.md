---
audio: false
generated: true
lang: es
layout: post
title: Amplificadores Operacionales
translated: true
type: note
---

A continuación se presenta un tutorial completo sobre **Amplificadores Operacionales (Op-Amps) y Sus Aplicaciones**, que cubre los temas especificados: características y parámetros del op-amp (corto virtual, abierto virtual), circuitos típicos de op-amp (amplificadores inversores/no inversores, integradores/diferenciadores) y aplicaciones no lineales (comparadores, generadores de formas de onda). Este tutorial está diseñado para ser exhaustivo, apto para principiantes y técnicamente preciso, con ejemplos prácticos y explicaciones.

---

Los amplificadores operacionales (op-amps) son amplificadores electrónicos versátiles de alta ganancia, ampliamente utilizados en circuitos analógicos para procesamiento de señales, amplificación, filtrado y más. Este tutorial te guiará a través de sus características, circuitos clave y aplicaciones no lineales.

---

### **1. Características y Parámetros del Op-Amp**

Un amplificador operacional es un amplificador de alta ganancia, acoplado directamente, con entradas diferenciales y una salida única. Normalmente se utiliza con componentes de retroalimentación externos (resistencias, condensadores, etc.) para definir su función. A continuación se presentan las características y parámetros clave de un op-amp ideal, junto con sus implicaciones prácticas.

#### **Características del Op-Amp Ideal**
1.  **Ganancia de Lazo Abierto Infinita (A_OL)**
    - La ganancia de lazo abierto (sin retroalimentación) es teóricamente infinita, lo que significa que incluso una pequeña diferencia entre las terminales de entrada produce una salida grande. En la práctica, los op-amps reales tienen ganancias de lazo abierto de 10^5 a 10^6.
    - **Implicación**: Permite un control preciso cuando se aplica retroalimentación.

2.  **Impedancia de Entrada Infinita**
    - Las terminales de entrada no extraen corriente (la impedancia de entrada ideal es infinita). En los op-amps reales, la impedancia de entrada está típicamente en el rango de megaohmios a gigaohmios.
    - **Implicación**: El op-amp no carga la fuente de la señal de entrada, preservando la integridad de la señal.

3.  **Impedancia de Salida Cero**
    - La salida puede manejar cualquier carga sin caída de voltaje. Los op-amps reales tienen una impedancia de salida baja (por ejemplo, 10–100 ohmios).
    - **Implicación**: Garantiza una transferencia eficiente de la señal a la siguiente etapa.

4.  **Ancho de Banda Infinito**
    - Un op-amp ideal amplifica todas las frecuencias por igual. En la práctica, el producto ganancia-ancho de banda limita el rendimiento (por ejemplo, ancho de banda de ganancia unitaria de 1 MHz para un op-amp 741).
    - **Implicación**: El ancho de banda disminuye al aumentar la ganancia en configuraciones de lazo cerrado.

5.  **Voltaje de Offset Cero**
    - Sin señal de entrada, la salida es cero. Los op-amps reales tienen pequeños voltajes de offset (microvoltios a milivoltios) que pueden necesitar compensación.
    - **Implicación**: Minimiza la salida no deseada en aplicaciones de precisión.

6.  **Relación de Rechazo en Modo Común (CMRR) Infinita**
    - El op-amp rechaza las señales comunes a ambas entradas (por ejemplo, ruido). Los op-amps reales tienen un CMRR alto (80–120 dB).
    - **Implicación**: Reduce el ruido en aplicaciones de señales diferenciales.

#### **Conceptos Clave: Corto Virtual y Abierto Virtual**
-   **Corto Virtual**
    - En una configuración de retroalimentación negativa, la alta ganancia de lazo abierto fuerza a que la diferencia de voltaje entre las entradas inversora (-) y no inversora (+) sea casi cero.
    - **Explicación**: El op-amp ajusta su salida para hacer V+ ≈ V- (asumiendo retroalimentación negativa). Esto se llama "corto virtual" porque las entradas no están físicamente en cortocircuito, pero se comportan como si lo estuvieran.
    - **Ejemplo**: En un amplificador inversor, si la entrada no inversora está conectada a tierra (0 V), el op-amp ajusta la salida para mantener la entrada inversora en aproximadamente 0 V.

-   **Abierto Virtual**
    - Debido a la impedancia de entrada infinita, no fluye corriente hacia las terminales de entrada del op-amp.
    - **Explicación**: Este "abierto virtual" significa que las entradas actúan como si estuvieran desconectadas del circuito en términos de flujo de corriente, permitiendo que toda la corriente de entrada fluya a través de los componentes externos.
    - **Ejemplo**: En un seguidor de voltaje, no fluye corriente hacia las entradas del op-amp, lo que lo convierte en un buffer ideal.

#### **Parámetros Prácticos**
-   **Slew Rate**: La tasa máxima de cambio del voltaje de salida (por ejemplo, 0.5 V/µs para un op-amp 741). Limita el rendimiento a alta frecuencia.
-   **Corriente de Polarización de Entrada**: Pequeñas corrientes (nA a pA) requeridas por las entradas de los op-amps reales.
-   **Relación de Rechazo de la Fuente de Alimentación (PSRR)**: Capacidad para rechazar el ruido de la fuente de alimentación.
-   **Ruido**: El ruido interno limita el rendimiento en aplicaciones de señal baja.

---

### **2. Circuitos Típicos de Op-Amp**

Los op-amps se utilizan normalmente en configuraciones de lazo cerrado con retroalimentación negativa para crear circuitos estables y predecibles. A continuación se presentan los circuitos más comunes: amplificadores inversores y no inversores, integradores y diferenciadores.

#### **Amplificador Inversor**
-   **Función**: Amplifica la señal de entrada e invierte su fase (desplazamiento de fase de 180°).
-   **Circuito**:
    - La señal de entrada (V_in) se aplica a la entrada inversora (-) a través de la resistencia R1.
    - La entrada no inversora (+) está conectada a tierra (0 V).
    - Una resistencia de retroalimentación (R_f) conecta la salida (V_out) a la entrada inversora.
-   **Ecuaciones Clave**:
    - Ganancia de voltaje: \\( A_v = -\frac{R_f}{R_1} \\)
    - Voltaje de salida: \\( V_{out} = -\frac{R_f}{R_1} \cdot V_{in} \\)
    - Impedancia de entrada: Aproximadamente \\( R_1 \\).
-   **Corto Virtual**: La entrada inversora está a 0 V (igual que la entrada no inversora conectada a tierra).
-   **Ejemplo**: Para \\( R_1 = 10 \, \text{k}\Omega \\), \\( R_f = 20 \, \text{k}\Omega \\), y \\( V_{in} = 1 \, \text{V} \\):
    - Ganancia: \\( A_v = -\frac{20k}{10k} = -2 \\)
    - Salida: \\( V_{out} = -2 \cdot 1 = -2 \, \text{V} \\).
-   **Aplicaciones**: Amplificadores de audio, inversión de señal, amplificadores sumadores.

#### **Amplificador No Inversor**
-   **Función**: Amplifica la señal de entrada sin inversión de fase.
-   **Circuito**:
    - La señal de entrada (V_in) se aplica a la entrada no inversora (+).
    - La resistencia de retroalimentación (R_f) conecta la salida a la entrada inversora (-), con la resistencia R_1 desde la entrada inversora a tierra.
-   **Ecuaciones Clave**:
    - Ganancia de voltaje: \\( A_v = 1 + \frac{R_f}{R_1} \\)
    - Voltaje de salida: \\( V_{out} = \left(1 + \frac{R_f}{R_1}\right) \cdot V_{in} \\)
    - Impedancia de entrada: Muy alta (debido a la entrada no inversora).
-   **Corto Virtual**: El voltaje de la entrada inversora es igual a V_in (debido a la retroalimentación).
-   **Ejemplo**: Para \\( R_1 = 10 \, \text{k}\Omega \\), \\( R_f = 30 \, \text{k}\Omega \\), y \\( V_{in} = 1 \, \text{V} \\):
    - Ganancia: \\( A_v = 1 + \frac{30k}{10k} = 4 \\)
    - Salida: \\( V_{out} = 4 \cdot 1 = 4 \, \text{V} \\).
-   **Aplicaciones**: Buffer de señal, escalado de voltaje.

#### **Integrador**
-   **Función**: Integra la señal de entrada en el tiempo, produciendo una salida proporcional a la integral de la entrada.
-   **Circuito**:
    - La señal de entrada (V_in) se aplica a la entrada inversora a través de la resistencia R.
    - Un condensador (C) se coloca en la ruta de retroalimentación (desde la salida a la entrada inversora).
    - La entrada no inversora está conectada a tierra.
-   **Ecuaciones Clave**:
    - Voltaje de salida: \\( V_{out} = -\frac{1}{R \cdot C} \int V_{in}(t) \, dt \\)
    - La salida es la integral negativa de la entrada.
-   **Corto Virtual**: La entrada inversora está a 0 V.
-   **Consideraciones Prácticas**:
    - Se puede añadir una resistencia en paralelo con el condensador para limitar la ganancia de baja frecuencia y evitar la saturación.
    - Limitado por el slew rate del op-amp y la fuga del condensador.
-   **Ejemplo**: Para \\( R = 10 \, \text{k}\Omega \\), \\( C = 1 \, \mu\text{F} \\), y \\( V_{in} = 1 \, \text{V} \\) constante:
    - Salida: \\( V_{out} = -\frac{1}{10k \cdot 1\mu} \int 1 \, dt = -100 \cdot t \, \text{V/s} \\).
    - Después de 1 ms: \\( V_{out} = -0.1 \, \text{V} \\).
-   **Aplicaciones**: Computadoras analógicas, procesamiento de señales, filtros paso bajo.

#### **Diferenciador**
-   **Función**: Diferencia la señal de entrada, produciendo una salida proporcional a la tasa de cambio de la entrada.
-   **Circuito**:
    - La señal de entrada (V_in) se aplica a través de un condensador (C) a la entrada inversora.
    - Una resistencia (R) se coloca en la ruta de retroalimentación.
    - La entrada no inversora está conectada a tierra.
-   **Ecuaciones Clave**:
    - Voltaje de salida: \\( V_{out} = -R \cdot C \cdot \frac{dV_{in}}{dt} \\)
    - La salida es la derivada negativa de la entrada.
-   **Corto Virtual**: La entrada inversora está a 0 V.
-   **Consideraciones Prácticas**:
    - Susceptible a la amplificación de ruido de alta frecuencia; una pequeña resistencia en serie con el condensador de entrada puede estabilizar el circuito.
-   **Ejemplo**: Para \\( R = 10 \, \text{k}\Omega \\), \\( C = 1 \, \mu\text{F} \\), y \\( V_{in} = t \, \text{V} \\) (rampa lineal):
    - Salida: \\( V_{out} = -10k \cdot 1\mu \cdot \frac{d(t)}{dt} = -0.01 \, \text{V} \\).
-   **Aplicaciones**: Detección de flancos, filtros paso alto.

---

### **3. Aplicaciones No Lineales**

Los op-amps pueden operar en modos no lineales (sin retroalimentación negativa o con componentes específicos) para realizar tareas como comparación de señales o generación de formas de onda.

#### **Comparador**
-   **Función**: Compara dos voltajes de entrada y genera una señal alta o baja según cuál sea mayor.
-   **Circuito**:
    - Una entrada (por ejemplo, V_ref) se aplica a la entrada no inversora (+).
    - La otra entrada (V_in) se aplica a la entrada inversora (-).
    - No hay retroalimentación (configuración de lazo abierto).
-   **Operación**:
    - Si V_in > V_ref, la salida oscila al riel negativo de la fuente de alimentación (por ejemplo, -V_cc).
    - Si V_in < V_ref, la salida oscila al riel positivo de la fuente de alimentación (por ejemplo, +V_cc).
-   **Características Clave**:
    - Opera en modo de lazo abierto, utilizando la alta ganancia del op-amp para producir una salida binaria.
    - Los op-amps reales tienen slew rates finitos, lo que causa un ligero retraso en la conmutación.
-   **Ejemplo**: Para V_ref = 2 V y V_in = 3 V, con fuentes de alimentación de ±12 V:
    - Dado que V_in > V_ref, V_out ≈ -12 V.
-   **Aplicaciones**:
    - Detectores de cruce por cero, detectores de umbral, conversión analógico-digital.
-   **Consideraciones Prácticas**:
    - Añadir histéresis (retroalimentación positiva) para evitar oscilaciones cerca del umbral (configuración de disparador Schmitt).
    - A menudo se prefieren CI comparadores dedicados (por ejemplo, LM339) para una conmutación más rápida.

#### **Generadores de Formas de Onda**
-   **Función**: Generan formas de onda periódicas (por ejemplo, cuadrada, triangular o sinusoidal) utilizando op-amps con redes de retroalimentación.
-   **Tipos**:
    1.  **Generador de Onda Cuadrada (Multivibrador Astable)**:
        - **Circuito**: Utiliza un op-amp con retroalimentación positiva a través de resistencias y un condensador en la ruta de retroalimentación negativa.
        - **Operación**: El condensador se carga y descarga entre voltajes de umbral establecidos por las resistencias, haciendo que la salida conmute entre los rieles de alimentación.
        - **Frecuencia**: Determinada por la constante de tiempo RC, por ejemplo, \\( f = \frac{1}{2 \cdot R \cdot C \cdot \ln(3)} \\) (aproximado para algunas configuraciones).
        - **Ejemplo**: Para \\( R = 10 \, \text{k}\Omega \\), \\( C = 0.1 \, \mu\text{F} \\), la frecuencia es aproximadamente 1 kHz.
        - **Aplicaciones**: Señales de reloj, generación de pulsos.

    2.  **Generador de Onda Triangular**:
        - **Circuito**: Normalmente combina un generador de onda cuadrada (comparador con retroalimentación positiva) con un integrador.
        - **Operación**: La onda cuadrada impulsa al integrador, produciendo una rampa lineal (onda triangular).
        - **Ejemplo**: Una onda cuadrada de 1 kHz alimentada a un integrador con \\( R = 10 \, \text{k}\Omega \\), \\( C = 0.1 \, \mu\text{F} \\) produce una onda triangular de 1 kHz.
        - **Aplicaciones**: Señales de prueba, modulación por ancho de pulso (PWM).

    3.  **Generador de Onda Sinusoidal (Oscilador de Puente de Wien)**:
        - **Circuito**: Utiliza retroalimentación positiva a través de una red selectiva de frecuencia (resistencias y condensadores) y retroalimentación negativa para la estabilización de amplitud.
        - **Operación**: Oscila a una frecuencia donde el desplazamiento de fase es cero, por ejemplo, \\( f = \frac{1}{2 \pi R C} \\).
        - **Ejemplo**: Para \\( R = 1.59 \, \text{k}\Omega \\), \\( C = 0.01 \, \mu\text{F} \\), la frecuencia es ~10 kHz.
        - **Aplicaciones**: Generación de señal de audio, pruebas.

---

### **Consideraciones Prácticas de Diseño**
1.  **Fuente de Alimentación**: Los op-amps requieren fuentes duales (por ejemplo, ±12 V) o simples (por ejemplo, 0 a 5 V para op-amps rail-to-rail). Asegúrese de que el voltaje de alimentación admita el rango de la señal de entrada y salida.
2.  **Selección de Componentes**: Utilice resistencias y condensadores de precisión para una respuesta de ganancia y frecuencia precisa. Consulte las hojas de datos del op-amp para conocer las especificaciones de ancho de banda, slew rate y ruido.
3.  **Estabilidad**: Evite oscilaciones asegurando una retroalimentación adecuada y desacoplando las fuentes de alimentación con condensadores (por ejemplo, 0.1 µF cerca del op-amp).
4.  **Limitaciones**: Los op-amps reales se desvían del comportamiento ideal (por ejemplo, ganancia, ancho de banda y slew rate finitos). Seleccione op-amps como el LM358 (propósito general), TL081 (bajo ruido) o OPA2134 (grado audio) según las necesidades de la aplicación.

---

### **Aplicación de Ejemplo: Preamplificador de Audio**
Diseñemos un preamplificador de audio inversor simple:
-   **Requisitos**: Amplificar una señal de audio de 50 mV a 500 mV (ganancia = 10).
-   **Circuito**: Amplificador inversor con \\( R_1 = 10 \, \text{k}\Omega \\), \\( R_f = 100 \, \text{k}\Omega \\).
-   **Cálculo**: \\( A_v = -\frac{100k}{10k} = -10 \\), \\( V_{out} = -10 \cdot 0.05 = -0.5 \, \text{V} \\).
-   **Consideraciones**: Utilice un op-amp de bajo ruido (por ejemplo, OPA2134), añada un condensador de acoplamiento para bloquear la CC y asegúrese de que la fuente de alimentación admita el rango de la señal (por ejemplo, ±5 V).

---

### **Conclusión**
Los amplificadores operacionales son bloques de construcción fundamentales en la electrónica analógica, que ofrecen flexibilidad para la amplificación, el procesamiento de señales y la generación de formas de onda. Al comprender sus características (corto virtual, abierto virtual, etc.) y dominar los circuitos clave (amplificadores inversores/no inversores, integradores, diferenciadores, comparadores, generadores de formas de onda), puedes diseñar una amplia gama de circuitos. Siempre considera las limitaciones del mundo real y selecciona los componentes cuidadosamente para un rendimiento óptimo.

Para una mayor exploración, experimenta con herramientas de simulación como LTspice o prototipado en breadboard, y consulta las hojas de datos de los op-amps para aplicaciones específicas.

---

Si deseas una simulación de circuito específica, una derivación matemática o un gráfico (por ejemplo, la respuesta en frecuencia de un integrador), ¡házmelo saber y puedo proporcionar más detalles o visualizaciones!