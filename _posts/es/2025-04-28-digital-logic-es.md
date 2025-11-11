---
audio: false
generated: true
lang: es
layout: post
title: Diseño Lógico Digital
translated: true
type: note
---

El diseño de lógica digital es la base de los sistemas informáticos modernos. Esta guía te llevará a través de conceptos esenciales, desde compuertas básicas hasta circuitos secuenciales complejos, proporcionando tanto comprensión teórica como enfoques de diseño prácticos.

## 1. Fundamentos de la Lógica Digital

### 1.1 Sistemas Numéricos y Conversiones
- **Binario (Base 2)**: Usa solo 0 y 1
- **Decimal (Base 10)**: Sistema estándar (0-9)
- **Hexadecimal (Base 16)**: Usa 0-9 y A-F
- **Octal (Base 8)**: Usa 0-7

**Técnicas de Conversión**:
- Decimal a Binario: División sucesiva por 2
- Binario a Decimal: Método de peso posicional
- Binario a Hexadecimal: Agrupar dígitos binarios en conjuntos de 4
- Binario a Octal: Agrupar dígitos binarios en conjuntos de 3

### 1.2 Aritmética Binaria
- Suma, resta, multiplicación, división
- Complemento a dos para representar números negativos
- Números con signo vs. sin signo
- Detección de desbordamiento

### 1.3 Álgebra Booleana
- **Operaciones Básicas**: AND, OR, NOT
- **Leyes Booleanas**:
  - Conmutativa: A + B = B + A; A · B = B · A
  - Asociativa: (A + B) + C = A + (B + C); (A · B) · C = A · (B · C)
  - Distributiva: A · (B + C) = A · B + A · C
  - Identidad: A + 0 = A; A · 1 = A
  - Complemento: A + A' = 1; A · A' = 0
  - DeMorgan: (A + B)' = A' · B'; (A · B)' = A' + B'

## 2. Circuitos de Lógica Combinacional

### 2.1 Proceso de Análisis y Diseño
1. Definir los requisitos del problema
2. Crear tabla de verdad
3. Derivar expresión booleana
4. Simplificar expresión
5. Implementar circuito

### 2.2 Compuertas Lógicas Básicas
- **AND**: La salida es 1 solo cuando todas las entradas son 1
- **OR**: La salida es 1 cuando cualquier entrada es 1
- **NOT**: Invierte la entrada (1→0, 0→1)
- **NAND**: Compuerta universal (AND seguida de NOT)
- **NOR**: Compuerta universal (OR seguida de NOT)
- **XOR**: La salida es 1 cuando las entradas son diferentes
- **XNOR**: La salida es 1 cuando las entradas son iguales

### 2.3 Simplificación de Expresiones
- **Método Algebraico**: Usando leyes booleanas
- **Mapa de Karnaugh (K-Map)**: Simplificación visual
  - K-Maps de 2 variables, 3 variables, 4 variables
  - Identificación de implicantes primos
  - Implicantes primos esenciales
- **Método de Quine-McCluskey**: Método tabular para expresiones más grandes

### 2.4 Módulos Combinacionales Comunes

#### 2.4.1 Codificadores
- **Función**: Convertir 2ⁿ líneas de entrada a salida de n bits
- **Tipos**:
  - Codificadores de prioridad: Manejan múltiples entradas activas
  - Codificador decimal a BCD (10 a 4)
  - Codificador octal a binario (8 a 3)
- **Aplicaciones**: Codificación de teclado, sistemas de prioridad

#### 2.4.2 Decodificadores
- **Función**: Convertir entrada de n bits a 2ⁿ líneas de salida
- **Tipos**:
  - Decodificador 3 a 8
  - Decodificador BCD a decimal
  - Decodificador BCD a 7 segmentos
- **Aplicaciones**: Decodificación de direcciones de memoria, controladores de pantalla

#### 2.4.3 Multiplexores (MUX)
- **Función**: Seleccionar una de muchas entradas basándose en líneas de selección
- **Tipos**:
  - MUX 2 a 1: 1 línea de selección, 2 entradas
  - MUX 4 a 1: 2 líneas de selección, 4 entradas
  - MUX 8 a 1: 3 líneas de selección, 8 entradas
- **Aplicaciones**: Selección de datos, conversión paralelo a serie
- **Implementaciones de Diseño**: Usando compuertas básicas, tablas de verdad

#### 2.4.4 Demultiplexores (DEMUX)
- **Función**: Enrutar una entrada a una de muchas salidas
- **Tipos**:
  - DEMUX 1 a 2
  - DEMUX 1 a 4
  - DEMUX 1 a 8
- **Aplicaciones**: Conversión serie a paralelo, distribución de datos

### 2.5 Circuitos Aritméticos
- **Semisumador**: 2 entradas, 2 salidas (suma, acarreo)
- **Sumador Completo**: 3 entradas, 2 salidas (incluye acarreo de entrada)
- **Sumador con Acarreo Rizado**: Semisumadores en cascada
- **Sumador con Acarreo Anticipado**: Suma más rápida
- **Sustractores**: Usando sumadores con entradas invertidas
- **Comparadores**: Comparar magnitud de números binarios

### 2.6 Riesgos en Circuitos Combinacionales
- **Riesgos Estáticos**:
  - Definición: Cambio momentáneo no deseado en la salida
  - Tipos: Riesgos estático-0 y estático-1
  - Detección: Usando K-Maps
  - Prevención: Añadiendo términos redundantes
- **Riesgos Dinámicos**:
  - Definición: Múltiples transiciones de salida
  - Causas: Múltiples retardos de compuerta
  - Prevención: Análisis de temporización adecuado
- **Técnicas de Eliminación de Riesgos**:
  - Reestructuración del circuito
  - Adición de elementos de retardo
  - Uso de diseño síncrono

## 3. Circuitos de Lógica Secuencial

### 3.1 Biestables
- **Biestable SR**: Latch de Set-Reset
- **Biestable D**: Latch de datos
- **Biestable JK**: SR mejorado con capacidad de alternancia
- **Biestable T**: Biestable de alternancia
- **Biestables Maestro-Esclavo**: Previene condiciones de carrera
- **Disparado por Flanco vs. Disparado por Nivel**: Características de temporización

### 3.2 Registros
- **Propósito**: Almacenar datos de múltiples bits
- **Tipos**:
  - Entrada paralela, salida paralela (PIPO)
  - Entrada serie, salida serie (SISO)
  - Entrada serie, salida paralela (SIPO)
  - Entrada paralela, salida serie (PISO)
- **Aplicaciones**: Almacenamiento de datos, operaciones de desplazamiento

### 3.3 Contadores
- **Contadores Asíncronos**:
  - Contadores de ripple
  - Contadores ascendentes/descendentes
- **Contadores Síncronos**:
  - Pulso de reloj único
  - Contador Johnson
  - Contador en anillo
- **Contadores Módulo-N**: Cuentan hasta N-1 y luego se reinician
- **Enfoques de Diseño**: Diagramas de estado, tablas de excitación

### 3.4 Máquinas de Estado
- **Máquina de Mealy**: La salida depende del estado actual y la entrada
- **Máquina de Moore**: La salida depende solo del estado actual
- **Diagrama de Estado**: Representación visual de estados y transiciones
- **Tabla de Estado**: Representación tabular de la máquina de estado
- **Asignación de Estado**: Codificación de estados con valores binarios
- **Proceso de Diseño**:
  1. Definir estados y transiciones
  2. Crear diagrama de estado
  3. Desarrollar tabla de estado
  4. Asignación de estado
  5. Derivar lógica de próximo estado y salida
  6. Implementar circuito

## 4. Memoria y Dispositivos de Lógica Programable

### 4.1 Tipos de Memoria
- **RAM (Memoria de Acceso Aleatorio)**:
  - SRAM (RAM Estática): Más rápida, más cara
  - DRAM (RAM Dinámica): Necesita refresco, mayor densidad
- **ROM (Memoria de Solo Lectura)**:
  - PROM: Programable una vez
  - EPROM: Borrable con luz UV
  - EEPROM: Borrable eléctricamente
  - Memoria Flash: Borrable en bloques
- **Diagramas de Temporización**: Ciclos de lectura/escritura

### 4.2 Dispositivos de Lógica Programable
- **PLA (Arreglo de Lógica Programable)**:
  - Planos AND y OR programables
- **PAL (Lógica de Arreglo Programable)**:
  - AND programable, OR fijo
- **CPLD (PLD Complejo)**:
  - Múltiples PLDs con interconexiones
- **FPGA (Arreglo de Compuertas Programable en Campo)**:
  - Bloques de lógica configurables
  - Tablas de búsqueda
  - Enfoques de programación

## 5. Diseño de Sistemas Digitales

### 5.1 Metodologías de Diseño
- **De arriba hacia abajo**: Comenzar con especificaciones de alto nivel
- **De abajo hacia arriba**: Comenzar con componentes básicos
- **Diseño Modular**: Dividir en bloques funcionales
- **Lenguajes de Descripción de Hardware (HDLs)**:
  - VHDL
  - Verilog
  - SystemVerilog

### 5.2 Análisis de Temporización
- **Retardo de Propagación**: Tiempo para que la señal viaje a través de una compuerta
- **Tiempos de Configuración y Mantenimiento**: Restricciones de temporización para circuitos secuenciales
- **Skew de Reloj**: Variación en los tiempos de llegada del reloj
- **Ruta Crítica**: Ruta de retardo más larga
- **Restricciones de Temporización**: Cumplir con el rendimiento requerido

### 5.3 Pruebas y Verificación
- **Modelos de Fallos**: Fallos stuck-at, fallos de puenteo
- **Generación de Patrones de Prueba**: Crear patrones de entrada para detectar fallos
- **Diseño para la Capacidad de Prueba (DFT)**:
  - Cadenas de escaneo
  - Autoprueba incorporada (BIST)
- **Métodos de Verificación**:
  - Simulación
  - Verificación formal
  - Emulación de hardware

## 6. Temas Avanzados

### 6.1 Diseño de Circuitos Asíncronos
- **Modo Fundamental**: Las entradas cambian una a la vez
- **Modo de Pulso**: Las entradas pueden cambiar simultáneamente
- **Metaestabilidad**: Comportamiento impredecible debido a violaciones de temporización
- **Protocolos de Handshaking**: Asegurar una comunicación adecuada

### 6.2 Diseño de Bajo Consumo
- **Consumo de Potencia Dinámica**: Actividad de conmutación
- **Consumo de Potencia Estática**: Corrientes de fuga
- **Técnicas de Reducción de Potencia**:
  - Clock gating
  - Power gating
  - Múltiples voltajes de alimentación
  - Escalado dinámico de voltaje

### 6.3 Diseño de Alta Velocidad
- **Segmentación**: Dividir operaciones en etapas
- **Procesamiento Paralelo**: Múltiples operaciones simultáneamente
- **Retemporización**: Optimizar la ubicación de registros
- **Segmentación de Onda**: Explotar retardos naturales

## 7. Ejemplos Prácticos de Diseño

### 7.1 Controlador de Semáforo
- Representación de diagrama de estado
- Implementación usando máquinas de estado
- Consideraciones de temporización

### 7.2 UAL (Unidad Aritmético Lógica)
- Selección de función
- Operaciones aritméticas
- Operaciones lógicas
- Estrategias de implementación

### 7.3 Controlador de Memoria
- Decodificación de direcciones
- Temporización de lectura/escritura
- Control de refresco para DRAM

## 8. Herramientas y Recursos de Diseño

### 8.1 Herramientas de Software
- **Herramientas de Simulación**: ModelSim, Icarus Verilog
- **Herramientas de Síntesis**: Quartus, Vivado, ISE
- **Herramientas de Verificación**: Verificación formal, análisis de cobertura

### 8.2 Recursos de Hardware
- **Placas de Desarrollo**: Arduino, Raspberry Pi, placas FPGA
- **Analizadores Lógicos**: Herramientas de depuración
- **Osciloscopios**: Análisis de señales

## 9. Tendencias Futuras

- **Computación Cuántica**: Qubits, compuertas cuánticas
- **Computación Neuromórfica**: Arquitecturas inspiradas en el cerebro
- **Computación Aproximada**: Intercambiar precisión por eficiencia
- **Integración 3D**: Apilamiento de lógica y memoria
- **Más allá del CMOS**: Nuevas tecnologías de dispositivos

## Referencias y Lecturas Adicionales

- Digital Design por M. Morris Mano
- Digital Logic and Computer Design por M. Morris Mano
- Fundamentals of Digital Logic with Verilog Design por Brown y Vranesic
- Contemporary Logic Design por Katz y Borriello
- FPGA Prototyping by VHDL Examples por Pong P. Chu

Esta guía integral proporciona una base sólida en los principios y prácticas del diseño de lógica digital, adecuada para estudiantes, profesionales y aficionados que buscan comprender o implementar sistemas digitales.