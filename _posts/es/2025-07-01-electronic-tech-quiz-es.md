---
audio: false
generated: true
lang: es
layout: post
title: Cuestionario de Autoevaluación de Tecnología Electrónica
translated: true
type: note
---

A continuación se presenta un cuestionario de ejemplo diseñado para un examen de autoestudio basado en el esquema proporcionado para *Fundamentals of Electronic Technology (III)*, editado por Wen Xidong y publicado por Economic Science Press. El cuestionario cubre conceptos clave de electrónica analógica, electrónica digital y aplicaciones prácticas, adaptado para evaluar la comprensión fundamental adecuada para un examen de autoestudio en China. Las preguntas son una mezcla de opción múltiple, respuesta corta y resolución de problemas para reflejar los estilos de examen típicos.

---

### Cuestionario de Ejemplo: Fundamentos de Tecnología Electrónica (III)
**Examen de Autoestudio**
**Instrucciones**: Conteste todas las preguntas. Muestre su trabajo para las preguntas de resolución de problemas. Cada pregunta vale los puntos indicados. Total: 100 puntos.

---

#### Parte I: Electrónica Analógica (40 puntos)

1. **Opción Múltiple: Análisis de Circuitos (5 puntos)**
   ¿Cuál de las siguientes opciones describe correctamente la Ley de Voltaje de Kirchhoff (LVK)?
   a) La suma de las corrientes que entran a un nodo es igual a la suma de las corrientes que salen de él.
   b) La suma de las caídas de voltaje alrededor de un lazo cerrado es igual a cero.
   c) La resistencia total en un circuito en serie es la suma de las resistencias individuales.
   d) El voltaje a través de ramas en paralelo es diferente.
   **Respuesta**: b) La suma de las caídas de voltaje alrededor de un lazo cerrado es igual a cero.

2. **Respuesta Corta: Configuraciones de Amplificadores (10 puntos)**
   Explique brevemente la diferencia entre las configuraciones Emisor Común (CE) y Colector Común (CC) de un amplificador BJT en términos de sus características de entrada/salida y aplicaciones típicas.
   **Respuesta de Ejemplo**:
   - **Configuración CE**: Alta ganancia de voltaje, impedancia de entrada moderada y salida invertida. Se utiliza en aplicaciones que requieren amplificación, como amplificadores de audio.
   - **Configuración CC**: Ganancia de voltaje unitaria, alta impedancia de entrada, baja impedancia de salida, salida no invertida. A menudo se utiliza como un buffer o etapa de adaptación de impedancia.

3. **Resolución de Problemas: Amplificadores Operacionales (15 puntos)**
   Un circuito amplificador operacional inversor tiene una resistencia de realimentación \\( R_f = 10 \, \text{k}\Omega \\) y una resistencia de entrada \\( R_{\text{in}} = 2 \, \text{k}\Omega \\). El voltaje de entrada es \\( V_{\text{in}} = 1 \, \text{V} \\).
   a) Calcule el voltaje de salida \\( V_{\text{out}} \\).
   b) ¿Cuál es la ganancia del circuito?
   **Solución**:
   a) Para un amplificador operacional inversor, \\( V_{\text{out}} = -\left(\frac{R_f}{R_{\text{in}}}\right) V_{\text{in}} = -\left(\frac{10 \, \text{k}\Omega}{2 \, \text{k}\Omega}\right) \cdot 1 \, \text{V} = -5 \, \text{V} \\).
   b) Ganancia \\( A = -\frac{R_f}{R_{\text{in}}} = -\frac{10}{2} = -5 \\).

4. **Opción Múltiple: Fuentes de Alimentación DC (10 puntos)**
   ¿Cuál es una ventaja clave de un regulador de conmutación sobre un regulador lineal?
   a) Menor costo
   b) Mayor eficiencia
   c) Diseño más simple
   d) Mejor regulación de voltaje
   **Respuesta**: b) Mayor eficiencia

---

#### Parte II: Electrónica Digital (40 puntos)

5. **Opción Múltiple: Compuertas Lógicas (5 puntos)**
   ¿Qué compuerta lógica produce una salida de 1 solo cuando todas sus entradas son 0?
   a) AND
   b) OR
   c) NOR
   d) XOR
   **Respuesta**: c) NOR

6. **Respuesta Corta: Lógica Combinacional (10 puntos)**
   Describa la función de un multiplexor y proporcione una aplicación práctica.
   **Respuesta de Ejemplo**: Un multiplexor selecciona una de varias señales de entrada y la dirige a una única salida basándose en líneas de selección. Actúa como un selector de datos. **Aplicación**: Se utiliza en sistemas de comunicación para encauzar múltiples flujos de datos en un único canal.

7. **Resolución de Problemas: Lógica Secuencial (15 puntos)**
   Diseñe un contador binario ascendente de 3 bits utilizando flip-flops JK. Proporcione la tabla de estados y describa la operación para un ciclo de reloj comenzando desde el estado 010 (binario 2).
   **Solución**:
   - **Tabla de Estados**:
     | Estado Presente (Q2 Q1 Q0) | Estado Siguiente (Q2 Q1 Q0) | Entradas JK (J2 K2 | J1 K1 | J0 K0) |
     |-------------------------|-----------------------|-----------------------|
     | 010                     | 011                   | 0 0 | 0 0 | 1 1 |
   - **Operación**: Desde el estado 010, en el siguiente ciclo de reloj, Q0 conmuta (0 → 1), Q1 y Q2 permanecen sin cambios, resultando en 011 (binario 3). J0 = K0 = 1 para conmutar Q0; los otros son no importa o 0.

8. **Opción Múltiple: Dispositivos Lógicos Programables (10 puntos)**
   ¿Cuál de las siguientes es una característica de un FPGA?
   a) Estructura lógica fija
   b) Bloques lógicos e interconexiones reprogramables
   c) Solo soporta circuitos analógicos
   d) No se puede programar usando HDL
   **Respuesta**: b) Bloques lógicos e interconexiones reprogramables

---

#### Parte III: Aplicaciones Prácticas (20 puntos)

9. **Respuesta Corta: Herramientas de Simulación (10 puntos)**
   Explique el papel de las herramientas de simulación como Multisim en el diseño de circuitos electrónicos. ¿Por qué son útiles para los estudiantes que aprenden *Fundamentos de Tecnología Electrónica*?
   **Respuesta de Ejemplo**: Multisim permite a los estudiantes diseñar, simular y probar circuitos virtualmente antes de construirlos, reduciendo errores y costos. Ayuda a visualizar el comportamiento del circuito (ej. voltaje, corriente) y a experimentar con parámetros, mejorando la comprensión de conceptos como amplificadores y circuitos lógicos.

10. **Resolución de Problemas: Sistemas de Señal Mixta (10 puntos)**
    Un sistema de monitoreo de temperatura utiliza un sensor analógico que entrega 0–5 V y una pantalla digital a través de un ADC de 3 bits. Si el voltaje de referencia del ADC es 5 V, calcule el tamaño del paso de voltaje y la salida digital para una lectura del sensor de 3.75 V.
    **Solución**:
    - Tamaño del paso = \\( \frac{V_{\text{ref}}}{2^n} = \frac{5 \, \text{V}}{2^3} = 0.625 \, \text{V} \\).
    - Salida digital = \\( \text{floor}\left(\frac{3.75}{0.625}\right) = \text{floor}(6) = 110 \\) (binario).

---

### Notas para la Preparación del Examen de Autoestudio en China
- **Estructura**: El cuestionario está diseñado para alinearse con el formato de examen de autoestudio en China, que a menudo enfatiza la comprensión teórica, la resolución de problemas y las aplicaciones prácticas. Las preguntas están equilibradas para evaluar la memoria, el análisis y las habilidades de diseño.
- **Consejos de Estudio**:
  - Enfóquese en dominar las leyes fundamentales (ej. Ohm, Kirchhoff) y sus aplicaciones.
  - Practique el diseño de circuitos básicos (ej. amplificadores, contadores) utilizando componentes estándar.
  - Utilice herramientas de simulación como Multisim o Proteus para verificar diseños.
  - Revise a fondo las características de los semiconductores y las operaciones de las compuertas lógicas.
- **Recursos**: El libro de texto *Fundamentals of Electronic Technology (III)* por Wen Xidong (Economic Science Press) es el recurso principal. Complemente con tutoriales en línea o plataformas como Coursera para simulaciones de circuitos y conceptos básicos de HDL.
- **Contexto del Examen**: Los exámenes de autoestudio en China, como los administrados por la National Education Examinations Authority (NEEA), requieren una preparación disciplinada. Los exámenes anteriores (si están disponibles) y los ejercicios de capítulos del libro de texto son críticos para el éxito.

Si desea preguntas adicionales, temas específicos enfatizados o un enfoque en preguntas relacionadas con laboratorio, ¡hágamelo saber! También puedo proporcionar una clave de respuestas más detallada o adaptar el cuestionario para un formato de examen específico.