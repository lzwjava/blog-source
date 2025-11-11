---
audio: false
generated: true
lang: es
layout: post
title: Circuitos Lógicos Secuenciales
translated: true
type: note
---

Los circuitos lógicos secuenciales son componentes fundamentales en la electrónica digital que mantienen información de estado, a diferencia de los circuitos combinacionales. Exploremos sus tipos clave y aplicaciones en detalle.

## Flip-Flops (FFs)

Los flip-flops son los elementos de memoria básicos en los sistemas digitales que almacenan un bit de información.

### Flip-Flop RS
- **Función**: El flip-flop Set-Reset es el elemento de memoria más básico
- **Entradas**: Set (S) y Reset (R)
- **Comportamiento**:
  - S=1, R=0: Salida Q=1 (estado Set)
  - S=0, R=1: Salida Q=0 (estado Reset)
  - S=0, R=0: Mantiene el estado anterior (Memoria)
  - S=1, R=1: Estado inválido/prohibido (ambas salidas pueden volverse 0 o impredecibles)
- **Aplicaciones**: Elementos de memoria simples, pero raramente utilizados en circuitos modernos debido al problema del estado inválido

### Flip-Flop D
- **Función**: Flip-flop de datos o de retardo, el más comúnmente utilizado
- **Entradas**: Datos (D) y Reloj (CLK)
- **Comportamiento**: La salida Q toma el valor de la entrada D cuando es activado por el reloj
- **Ventajas**: Elimina el problema del estado inválido del flip-flop RS
- **Aplicaciones**: Registros, almacenamiento de datos, división de frecuencia

### Flip-Flop JK
- **Función**: Más versátil que el RS, resuelve el problema del estado inválido
- **Entradas**: J (similar a Set), K (similar a Reset) y Reloj
- **Comportamiento**:
  - J=0, K=0: Sin cambio
  - J=0, K=1: Reset (Q=0)
  - J=1, K=0: Set (Q=1)
  - J=1, K=1: Toggle (Q cambia a su complemento)
- **Aplicaciones**: Contadores, registros de desplazamiento, donde la funcionalidad de toggle es útil

### Flip-Flop T
- **Función**: Flip-flop de toggle, cambia de estado con cada pulso de reloj cuando está habilitado
- **Entradas**: Toggle (T) y Reloj
- **Comportamiento**:
  - T=0: Sin cambio
  - T=1: La salida alterna con cada pulso de reloj
- **Aplicaciones**: Contadores, divisores de frecuencia (circuitos divide-por-2)

## Contadores y Registros de Desplazamiento

### Contadores
Los contadores son circuitos secuenciales que pasan por una secuencia predeterminada de estados tras la aplicación de pulsos de reloj.

#### Contadores Asíncronos (Ripple)
- **Principio de operación**: El reloj se aplica solo al primer flip-flop; los flip-flops subsiguientes son activados por la salida del FF anterior
- **Características**:
  - Diseño más simple con menos conexiones
  - Más lentos debido a los retardos de propagación que se acumulan (ripple a través del circuito)
  - Pueden tener glitches debido a tiempos de propagación desiguales
- **Ejemplo**: Contador ripple de 4 bits usando flip-flops T conectados en serie

#### Contadores Síncronos
- **Principio de operación**: El reloj se aplica a todos los flip-flops simultáneamente
- **Características**:
  - Operación más rápida ya que todos los FFs cambian de estado al mismo tiempo
  - Diseño más complejo que requiere puertas lógicas adicionales
  - Sin problemas de retardo por ripple
- **Ejemplo**: Contador binario ascendente de 4 bits con puertas AND controlando las entradas J-K

#### Tipos de Contadores
- **Contador Ascendente**: Cuenta hacia arriba (0,1,2,...,n)
- **Contador Descendente**: Cuenta hacia abajo (n,...,2,1,0)
- **Contador Ascendente/Descendente**: Puede contar en cualquier dirección basado en una señal de control
- **Contador Módulo-n**: Cuenta de 0 a n-1 y luego se reinicia (ejemplo: contador mod-10 cuenta de 0 a 9)

### Registros de Desplazamiento
Los registros de desplazamiento almacenan y desplazan datos binarios hacia la izquierda o derecha.

#### Tipos de Registros de Desplazamiento
- **SISO (Serial In, Serial Out)**: Los datos entran y salen un bit a la vez
- **SIPO (Serial In, Parallel Out)**: Los datos entran en serie pero pueden leerse en paralelo
- **PISO (Parallel In, Serial Out)**: Los datos se cargan en paralelo pero se desplazan en serie
- **PIPO (Parallel In, Parallel Out)**: Los datos entran y salen en paralelo (todos los bits a la vez)

#### Aplicaciones
- Almacenamiento de datos y transferencia entre sistemas paralelos y serie
- Retardos de tiempo
- Generadores de secuencias
- Operaciones aritméticas en computadoras

## Análisis de Circuitos Secuenciales

### Tablas y Diagramas de Estado
- **Tabla de Estado**: Una representación tabular que muestra:
  - Estado actual
  - Entradas
  - Siguiente estado
  - Salidas
- **Diagrama de Estado**: Representación gráfica con:
  - Círculos que representan estados
  - Flechas que muestran transiciones entre estados
  - Etiquetas en las flechas que indican relaciones entrada/salida

### Proceso de Análisis
1. Identificar tipos de flip-flop y sus ecuaciones características
2. Determinar variables de estado presente
3. Crear una tabla de estado que muestre transiciones basadas en las entradas
4. Desarrollar un diagrama de estado a partir de la tabla de estado
5. Analizar problemas de temporización y posibles condiciones de carrera

### Tablas de Excitación de FF
Estas tablas ayudan a determinar las entradas requeridas a los flip-flops para lograr las transiciones de estado deseadas:

- Para flip-flops D: La entrada D debe ser igual al siguiente estado deseado
- Para flip-flops JK: Usar J=Q', K=Q para establecer Q a 1, y J=0, K=1 para resetear Q a 0
- Para flip-flops T: T=1 para cambiar de estado, T=0 para mantener el estado actual

### Consideraciones de Diseño
- Los diseños síncronos son generalmente preferidos sobre los asíncronos para:
  - Temporización predecible
  - Depuración más fácil
  - Mejor inmunidad al ruido y glitches
- El skew del reloj y los tiempos de setup/hold deben considerarse para una operación confiable
- Deben incluirse provisiones de reset para la inicialización

¿Te gustaría que profundice en algún aspecto particular de los circuitos lógicos secuenciales?