---
audio: false
generated: true
lang: es
layout: post
title: Comprensión de la capa física
translated: true
type: note
---

A continuación se presenta un tutorial detallado para ayudarte a aprender el capítulo de la "Capa Física" de un curso de Tecnología de Redes de Computadoras (probablemente parte del sistema chino de Exámenes de Autoeducación para la Educación Superior). Este tutorial está estructurado para guiarte a través de los conceptos clave—medios de transmisión, técnicas de codificación de señales, conceptos básicos de transmisión de datos y componentes de hardware—proporcionando explicaciones, ejemplos y consejos de estudio. ¡Comencemos!

---

### **Tutorial: Comprendiendo la Capa Física**

La Capa Física es la base de las redes de computadoras. Se ocupa de la conexión física entre dispositivos y la transmisión de datos en bruto (bits) a través de un medio de comunicación. Este tutorial desglosará cada tema en secciones manejables, explicará conceptos técnicos en términos simples y proporcionará una ruta de aprendizaje paso a paso.

---

### **1. Medios de Transmisión**
El medio de transmisión es la ruta física que transporta las señales de datos entre dispositivos. Se divide en medios **cableados** (guiados) e **inalámbricos** (no guiados).

#### **Medios de Transmisión Cableados**
- **Par Trenzado**
  - **Descripción**: Dos cables de cobre aislados trenzados entre sí para reducir la interferencia (ruido electromagnético).
  - **Tipos**:
    - Par Trenzado No Blindado (UTP): Común en cables Ethernet (ej., Cat5e, Cat6).
    - Par Trenzado Blindado (STP): Blindaje extra para entornos ruidosos.
  - **Ventajas**: Barato, fácil de instalar.
  - **Desventajas**: Distancia limitada (100 metros para Ethernet), susceptible a interferencias.
  - **Ejemplo**: Cables de internet doméstico.

- **Cable Coaxial**
  - **Descripción**: Un conductor central rodeado por una malla blindada, utilizado para un ancho de banda mayor que el par trenzado.
  - **Tipos**: Coaxial grueso (más antiguo) y coaxial delgado.
  - **Ventajas**: Mejor resistencia a las interferencias, admite distancias más largas.
  - **Desventajas**: Más voluminoso y más caro que el par trenzado.
  - **Ejemplo**: Televisión por cable o LANs antiguas.

- **Cable de Fibra Óptica**
  - **Descripción**: Utiliza luz (señales ópticas) para transmitir datos a través de fibras delgadas de vidrio o plástico.
  - **Tipos**:
    - Monomodo: Largas distancias, una sola ruta de luz.
    - Multimodo: Distancias más cortas, múltiples rutas de luz.
  - **Ventajas**: Alto ancho de banda, largas distancias (kilómetros), inmune a interferencias electromagnéticas.
  - **Desventajas**: Caro, más difícil de instalar.
  - **Ejemplo**: Redes troncales de internet, redes de alta velocidad.

#### **Medios de Transmisión Inalámbricos**
- **Ondas de Radio**
  - **Descripción**: Ondas electromagnéticas (3 kHz a 3 GHz) que viajan por el aire.
  - **Ventajas**: Cobertura amplia, sin cables físicos.
  - **Desventajas**: Susceptible a interferencias (ej., paredes, clima).
  - **Ejemplo**: Wi-Fi, Bluetooth.

- **Microondas**
  - **Descripción**: Ondas de radio de alta frecuencia (3 GHz a 30 GHz) que requieren línea de vista entre el emisor y el receptor.
  - **Ventajas**: Alto ancho de banda, transmisión a larga distancia.
  - **Desventajas**: Necesita alineación directa, afectado por el clima.
  - **Ejemplo**: Comunicación por satélite, torres de telefonía celular.

#### **Consejos de Estudio**
- **Visualiza**: Dibuja diagramas de cables de par trenzado, coaxial y fibra óptica para ver su estructura.
- **Compara**: Haz una tabla comparando medios cableados vs. inalámbricos (costo, velocidad, distancia, interferencia).
- **Mundo Real**: Identifica ejemplos en tu hogar (ej., Wi-Fi para ondas de radio, Ethernet para par trenzado).

---

### **2. Técnicas de Codificación de Señales**
La codificación de señales convierte los datos (bits: 0s y 1s) en señales para su transmisión. Se divide en señales **analógicas** (ondas continuas) y **digitales** (niveles discretos).

#### **Señales Analógicas vs. Digitales**
- **Analógica**: Forma de onda continua (ej., ondas de sonido).
- **Digital**: Valores discretos (ej., 0V para 0, 5V para 1).
- **¿Por qué codificar?**: Para adaptarse al medio y garantizar una transferencia de datos precisa.

#### **Técnicas de Codificación Comunes**
- **Digital a Digital (ej., para medios cableados)**
  - **NRZ (Non-Return-to-Zero)**: 0 = voltaje bajo, 1 = voltaje alto. Simple pero propenso a problemas de sincronización.
  - **Manchester**: El bit se representa por una transición (ej., bajo-a-alto = 1, alto-a-bajo = 0). Utilizado en Ethernet.
  - **Ventajas/Desventajas**: Manchester evita la pérdida de sincronización pero utiliza más ancho de banda.

- **Digital a Analógico (ej., para módems)**
  - **ASK (Amplitude Shift Keying)**: Variar la amplitud, mantener la frecuencia constante.
  - **FSK (Frequency Shift Keying)**: Variar la frecuencia (ej., baja frecuencia = 0, alta frecuencia = 1).
  - **PSK (Phase Shift Keying)**: Variar la fase de la onda.
  - **Ejemplo**: Módems convirtiendo datos digitales en señales de línea telefónica.

- **Analógico a Digital (ej., para voz sobre IP)**
  - **PCM (Pulse Code Modulation)**: Muestrea la señal analógica, la cuantiza en valores digitales.
  - **Ejemplo**: Digitalización de audio para llamadas telefónicas.

#### **Consejos de Estudio**
- **Diagramas**: Dibuja formas de onda para NRZ, Manchester, ASK, FSK y PSK para ver las diferencias.
- **Practica**: Codifica una cadena binaria (ej., 1010) usando Manchester y NRZ.
- **Comprende el Propósito**: Pregunta: ¿Por qué Manchester evita problemas de sincronización? (Pista: Las transiciones proporcionan un reloj).

---

### **3. Conceptos Básicos de Transmisión de Datos**
Esta sección cubre cómo se mueven los datos de manera eficiente y confiable a través de la capa física.

#### **Conceptos Clave**
- **Ancho de Banda**
  - **Definición**: Rango de frecuencias que un medio puede transportar (medido en Hz).
  - **Impacto**: Mayor ancho de banda = más datos (bits por segundo).
  - **Ejemplo**: La fibra óptica tiene un gran ancho de banda frente al par trenzado.

- **Rendimiento (Throughput)**
  - **Definición**: Tasa de datos real alcanzada (bits por segundo, bps).
  - **Diferencia**: El ancho de banda es potencial; el rendimiento es real (afectado por ruido, errores).
  - **Ejemplo**: Ancho de banda de 100 Mbps, pero solo 80 Mbps de rendimiento debido a interferencias.

- **Ruido**
  - **Definición**: Señales no deseadas que distorsionan los datos.
  - **Tipos**:
    - Ruido térmico (movimiento aleatorio de electrones).
    - Diafonía (interferencia de cables cercanos).
    - Externo (ej., rayos).
  - **Efecto**: Causa errores de bits (ej., un 0 leído como 1).
  - **Solución**: Blindaje (STP), detección de errores (capas superiores).

#### **Consejos de Estudio**
- **Fórmulas**: Aprende la Capacidad de Shannon:
  \\( C = B \log_2(1 + S/N) \\)
  Donde \\( C \\) = capacidad (bps), \\( B \\) = ancho de banda (Hz), \\( S/N \\) = relación señal-ruido.
- **Escenario**: Si el ancho de banda = 1 MHz y S/N = 31, calcula la capacidad máxima. (Respuesta: ~5 Mbps).
- **Relaciona**: ¿Por qué el Wi-Fi se ralentiza cerca de un microondas? (Interferencia por ruido).

---

### **4. Componentes de Hardware**
Son los dispositivos físicos que soportan la transmisión de datos en la Capa Física.

#### **Dispositivos Clave**
- **Concentradores (Hubs)**
  - **Función**: Conecta múltiples dispositivos en una red, transmitiendo datos a todos los puertos.
  - **Ventajas**: Simple, barato.
  - **Desventajas**: Sin inteligencia—causa colisiones en redes congestionadas.
  - **Ejemplo**: Redes Ethernet antiguas.

- **Repetidores**
  - **Función**: Amplifica o regenera señales para extender la distancia.
  - **Ventajas**: Supera la pérdida de señal (atenuación).
  - **Desventajas**: No filtra ni gestiona el tráfico.
  - **Ejemplo**: Enlaces largos de fibra óptica.

- **Cables**
  - **Tipos**: Par trenzado (UTP/STP), coaxial, fibra óptica (cubiertos anteriormente).
  - **Función**: Medio físico para la transmisión de señales.

#### **Consejos de Estudio**
- **Compara**: Concentradores vs. repetidores (los concentradores conectan dispositivos, los repetidores extienden señales).
- **Diagrama**: Dibuja una red con un concentrador conectando PCs y un repetidor extendiendo un cable.
- **Mundo Real**: Revisa tu router—los dispositivos modernos reemplazan los concentradores con conmutadores (Capa 2).

---

### **Plan de Aprendizaje**
1. **Día 1: Medios de Transmisión**
   - Lee los apuntes, dibuja diagramas, compara cableado vs. inalámbrico.
   - Quiz: Nombra 2 ventajas y desventajas de la fibra óptica.

2. **Día 2: Codificación de Señales**
   - Estudia los tipos de codificación, dibuja formas de onda.
   - Práctica: Codifica "1100" en NRZ y Manchester.

3. **Día 3: Conceptos Básicos de Transmisión de Datos**
   - Aprende las definiciones de ancho de banda, rendimiento y ruido.
   - Resuelve: Calcula la capacidad con un ancho de banda y S/N dados.

4. **Día 4: Componentes de Hardware**
   - Comprende concentradores, repetidores, cables.
   - Dibuja: Una red con estos dispositivos.

5. **Día 5: Repaso y Examen**
   - Repasa todos los temas, revisa las áreas débiles.
   - Auto-evaluación: Explica cómo funciona el Wi-Fi en la Capa Física.

---

### **Recursos Adicionales**
- **Libros**: "Computer Networks" de Andrew Tanenbaum (explicaciones simples).
- **En línea**: Khan Academy o YouTube para tutoriales visuales sobre codificación/conceptos de señales.
- **Práctica**: Usa simuladores como Packet Tracer para ver configuraciones de la capa física.

---

Este tutorial te brinda una base sólida para el capítulo de la Capa Física. Concéntrate en comprender los conceptos (no solo memorizar) y relaciónalos con ejemplos del mundo real. ¡Buena suerte con tu examen de autoestudio! Avísame si necesitas aclaraciones sobre cualquier tema.