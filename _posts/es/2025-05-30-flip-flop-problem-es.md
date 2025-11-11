---
audio: false
generated: true
lang: es
layout: post
title: Experimento y Tabla de Estados del Biestable JK
translated: true
type: note
---

**42. Experimento con Flip-Flop JK - Reloj de Disparo por Un Pulso**
- Objetivo: Comprender el principio de funcionamiento y las características de un flip-flop JK.
- Equipo: Módulo de flip-flop JK, generador de pulsos, fuente de alimentación, cables de conexión, etc.

**Tabla 42 de Transición de Estados**

| Q₂ⁿ | Q₁ⁿ | Q₀ⁿ | Q₂ⁿ⁺¹ | Q₁ⁿ⁺¹ | Q₀ⁿ⁺¹ | Z |
|-----|-----|-----|-------|-------|-------|---|
| 0   | 0   | 0   | 0     | 0     | 1     | 0 |
| 0   | 0   | 1   | 0     | 1     | 0     | 0 |
| 0   | 1   | 0   | 0     | 1     | 1     | 0 |
| 0   | 1   | 1   | 1     | 0     | 0     | 0 |
| 1   | 0   | 0   | 0     | 0     | 0     | 1 |

### Respuesta:
La tabla representa la transición de estados de un flip-flop JK de 3 bits donde Q₂ⁿ, Q₁ⁿ y Q₀ⁿ son los estados actuales, y Q₂ⁿ⁺¹, Q₁ⁿ⁺¹ y Q₀ⁿ⁺¹ son los siguientes estados después de un pulso de reloj. La salida Z es 1 solo cuando el estado actual es 100, lo que indica una condición específica o una señal de salida. Este comportamiento es típico de un flip-flop JK, que puede mantener, establecer, reiniciar o cambiar su estado basándose en las entradas (J y K) y el pulso de reloj.

Desglosemos la tabla de transición de estados del flip-flop JK y expliquemos su comportamiento en detalle.

### Descripción General de un Flip-Flop JK
Un flip-flop JK es un tipo de circuito lógico secuencial utilizado en electrónica digital para almacenar un solo bit de datos. Tiene dos entradas, J y K, una entrada de reloj (CLK) y dos salidas, Q (el estado actual) y Q' (el complemento de Q). El flip-flop JK es una mejora sobre el flip-flop SR porque elimina el estado "inválido" (cuando ambas entradas son 1). Su comportamiento es el siguiente:

- **J = 0, K = 0**: Sin cambio (Q permanece igual).
- **J = 0, K = 1**: Reinicio (Q se convierte en 0).
- **J = 1, K = 0**: Establecer (Q se convierte en 1).
- **J = 1, K = 1**: Conmutar (Q cambia al estado opuesto).

La tabla en la imagen representa un sistema con tres flip-flops JK (Q₂, Q₁, Q₀), formando una máquina de estados de 3 bits, donde Q₂ⁿ, Q₁ⁿ y Q₀ⁿ son los estados actuales, y Q₂ⁿ⁺¹, Q₁ⁿ⁺¹ y Q₀ⁿ⁺¹ son los siguientes estados después de un pulso de reloj. Z es una señal de salida basada en el estado actual.

### Explicación de la Tabla de Transición de Estados
La tabla muestra cómo el sistema transita entre estados y cuándo se activa la salida Z. Analicemos cada fila:

| Q₂ⁿ | Q₁ⁿ | Q₀ⁿ | Q₂ⁿ⁺¹ | Q₁ⁿ⁺¹ | Q₀ⁿ⁺¹ | Z |
|-----|-----|-----|-------|-------|-------|---|
| 0   | 0   | 0   | 0     | 0     | 1     | 0 |
| 0   | 0   | 1   | 0     | 1     | 0     | 0 |
| 0   | 1   | 0   | 0     | 1     | 1     | 0 |
| 0   | 1   | 1   | 1     | 0     | 0     | 0 |
| 1   | 0   | 0   | 0     | 0     | 0     | 1 |

#### Fila 1: Estado 000 → 001, Z = 0
- **Estado Actual (Q₂ⁿ, Q₁ⁿ, Q₀ⁿ)**: 000 (decimal 0)
- **Siguiente Estado (Q₂ⁿ⁺¹, Q₁ⁿ⁺¹, Q₀ⁿ⁺¹)**: 001 (decimal 1)
- **Salida Z**: 0
- **Explicación**: El sistema comienza en el estado 000. Después de un pulso de reloj, Q₀ conmuta de 0 a 1 (probablemente porque J₀ = 1, K₀ = 1), mientras que Q₁ y Q₂ permanecen en 0 (posiblemente J₁ = 0, K₁ = 0; J₂ = 0, K₂ = 0). Z es 0, lo que indica que no se cumple la condición de salida.

#### Fila 2: Estado 001 → 010, Z = 0
- **Estado Actual**: 001 (decimal 1)
- **Siguiente Estado**: 010 (decimal 2)
- **Salida Z**: 0
- **Explicación**: Desde el estado 001, Q₀ conmuta de 1 a 0 (J₀ = 1, K₀ = 1), Q₁ conmuta de 0 a 1 (J₁ = 1, K₁ = 1) y Q₂ permanece en 0. Z permanece en 0.

#### Fila 3: Estado 010 → 011, Z = 0
- **Estado Actual**: 010 (decimal 2)
- **Siguiente Estado**: 011 (decimal 3)
- **Salida Z**: 0
- **Explicación**: Desde el estado 010, Q₀ conmuta de 0 a 1 (J₀ = 1, K₀ = 1), Q₁ permanece en 1 y Q₂ permanece en 0. Z sigue siendo 0.

#### Fila 4: Estado 011 → 100, Z = 0
- **Estado Actual**: 011 (decimal 3)
- **Siguiente Estado**: 100 (decimal 4)
- **Salida Z**: 0
- **Explicación**: Desde el estado 011, Q₀ conmuta de 1 a 0, Q₁ conmuta de 1 a 0 y Q₂ conmuta de 0 a 1 (J₂ = 1, K₂ = 1). Z permanece en 0.

#### Fila 5: Estado 100 → 000, Z = 1
- **Estado Actual**: 100 (decimal 4)
- **Siguiente Estado**: 000 (decimal 0)
- **Salida Z**: 1
- **Explicación**: Desde el estado 100, Q₂ conmuta de 1 a 0, Q₁ permanece en 0 y Q₀ permanece en 0. La salida Z es 1, lo que indica que el estado 100 activa la condición de salida (posiblemente Z = Q₂ AND NOT Q₁ AND NOT Q₀).

### Comportamiento del Sistema
- **Secuencia de Estados**: El sistema recorre los estados en este orden: 000 → 001 → 010 → 011 → 100 → 000, y se repite. Esta es una secuencia de 5 estados (de 8 estados posibles para 3 bits), lo que sugiere una configuración específica de las entradas J y K para cada flip-flop.
- **Salida Z**: Z es 1 solo cuando el estado actual es 100. Esto podría representar una condición en la que el sistema señala la finalización de un ciclo o un evento específico (por ejemplo, un contador que alcanza un valor determinado).

### Interpretación Práctica
Esta configuración de flip-flops JK parece ser un contador módulo-5 (ya que recorre 5 estados). El contador se incrementa con cada pulso de reloj, y la salida Z señala cuando se alcanza el estado 100 antes de reiniciar a 000. Tales circuitos se utilizan en sistemas digitales para contar, dividir frecuencias o generar secuencias específicas.

### Resumen
El circuito de flip-flop JK en la tabla funciona como una máquina de estados de 3 bits con un ciclo de 5 estados (000 → 001 → 010 → 011 → 100 → 000). La salida Z es 1 solo en el estado 100, lo que probablemente indica un evento específico o una condición de reinicio. Las transiciones están gobernadas por las entradas JK, que están configuradas para producir esta secuencia.