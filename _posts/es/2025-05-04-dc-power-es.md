---
audio: false
generated: true
lang: es
layout: post
title: Fuentes de Alimentación de CC
translated: true
type: note
---

Este tutorial proporciona una exploración detallada de las **fuentes de alimentación de CC**, centrándose en los **circuitos rectificadores y de filtro** (rectificadores de media onda y de onda completa) y las diferencias entre los **reguladores lineales y conmutados**. Incluye explicaciones teóricas, ejemplos prácticos, diseños de circuitos y aplicaciones del mundo real para garantizar una comprensión exhaustiva para principiantes y estudiantes de nivel intermedio.

---

## Tabla de Contenidos
1. **Introducción a las Fuentes de Alimentación de CC**
2. **Circuitos Rectificadores y de Filtro**
   - Rectificador de Media Onda
   - Rectificador de Onda Completa (Configuración de Puente)
   - Circuitos de Filtro
3. **Reguladores Lineales vs. Conmutados**
   - Reguladores Lineales
   - Reguladores Conmutados (Buck, Boost, Buck-Boost)
4. **Ejemplos Prácticos y Diseño de Circuitos**
5. **Aplicaciones y Consideraciones**
6. **Conclusión**

---

## 1. Introducción a las Fuentes de Alimentación de CC
Una **fuente de alimentación de CC** convierte la corriente alterna (CA) en corriente continua (CC) para alimentar dispositivos electrónicos como microcontroladores, sensores y circuitos integrados. El proceso típicamente implica:
- **Rectificación**: Convertir CA a CC pulsante.
- **Filtrado**: Suavizar la CC pulsante.
- **Regulación**: Estabilizar el voltaje o corriente de salida.

Las fuentes de alimentación de CC son críticas en electrónica, asegurando que los dispositivos reciban energía estable y con bajo ruido. Los dos componentes principales cubiertos aquí son los **circuitos rectificadores/filtros** y los **reguladores de voltaje** (lineales y conmutados).

---

## 2. Circuitos Rectificadores y de Filtro

Los circuitos rectificadores convierten CA a CC, y los filtros suavizan la salida para reducir el rizado. Analicemos esto.

### a. Rectificador de Media Onda
El **rectificador de media onda** es el circuito de rectificación más simple, que utiliza un solo diodo.

#### Cómo Funciona
- **Entrada**: Voltaje de CA (por ejemplo, de un transformador).
- **Operación**: El diodo conduce solo durante el semiciclo positivo de la forma de onda de CA, bloqueando el semiciclo negativo.
- **Salida**: CC pulsante con la misma frecuencia que la CA de entrada, que contiene solo los semiciclos positivos (o negativos, dependiendo de la orientación del diodo).

#### Diagrama del Circuito
```
Fuente CA ----> Diodo (D1) ----> Carga (R) ----> Tierra
```
- **Componentes**:
  - **Diodo**: Por ejemplo, 1N4007 (diodo rectificador de propósito general).
  - **Carga**: Una resistencia o circuito electrónico.

#### Características
- **Voltaje de Salida**: Aproximadamente \\( V_{salida} = V_{ent(pico)} - V_{diodo} \\) (donde \\( V_{diodo} \approx 0.7V \\) para diodos de silicio).
- **Eficiencia**: Baja (~40.6%), ya que solo se utiliza la mitad del ciclo de CA.
- **Rizado**: Alto, ya que la salida es intermitente.

#### Ventajas
- Simple y económico.
- Requiere componentes mínimos.

#### Desventajas
- Ineficiente (desperdicia la mitad del ciclo de CA).
- Alto rizado, requiere filtros grandes para CC suave.

---

### b. Rectificador de Onda Completa (Configuración de Puente)
El **rectificador de onda completa** utiliza tanto los semiciclos positivos como negativos de la entrada de CA, produciendo una salida de CC más consistente.

#### Cómo Funciona
- **Configuración**: Utiliza cuatro diodos en una configuración de **puente rectificador**.
- **Operación**:
  - Durante el semiciclo positivo, dos diodos conducen, dirigiendo la corriente a través de la carga.
  - Durante el semiciclo negativo, los otros dos diodos conducen, manteniendo la misma dirección de corriente a través de la carga.
- **Salida**: CC pulsante con el doble de la frecuencia de la CA de entrada.

#### Diagrama del Circuito
```
       Entrada CA
         ------
        |      |
   D1 --|-->|--|-->|-- D2
        |      |       |
        |      R       |
        |      |       |
   D3 --|<--|--|<--|-- D4
        |      |
         ------
       Tierra
```
- **Componentes**:
  - **Diodos**: Cuatro diodos (por ejemplo, 1N4007).
  - **Carga**: Resistencia o circuito.
  - **Transformador** (opcional): Reduce el voltaje de CA.

#### Características
- **Voltaje de Salida**: \\( V_{salida} = V_{ent(pico)} - 2V_{diodo} \\) (dos diodos conducen a la vez, por lo que una caída de ~1.4V para diodos de silicio).
- **Eficiencia**: Mayor (~81.2%) que la de media onda.
- **Rizado**: Menor que el de media onda, ya que los pulsos ocurren dos veces por ciclo.

#### Ventajas
- Más eficiente, utiliza el ciclo completo de CA.
- Rizado reducido, requiere filtros más pequeños.

#### Desventajas
- Más complejo (cuatro diodos).
- Caída de voltaje ligeramente mayor (debido a dos diodos).

---

### c. Circuitos de Filtro
Los rectificadores producen CC pulsante, que no es adecuada para la mayoría de la electrónica debido al **rizado** (variaciones en el voltaje). Los filtros suavizan la salida para aproximar una CC estable.

#### Filtro Común: Filtro de Condensador
Un **filtro de condensador** es el método más común, colocado en paralelo con la carga.

#### Cómo Funciona
- **Carga**: Durante el pico de la forma de onda rectificada, el condensador se carga al voltaje pico.
- **Descarga**: Cuando el voltaje rectificado cae, el condensador se descarga a través de la carga, manteniendo un voltaje más constante.
- **Resultado**: CC más suave con rizado reducido.

#### Diagrama del Circuito (Onda Completa con Filtro de Condensador)
```
       Entrada CA
         ------
        |      |
   D1 --|-->|--|-->|-- D2
        |      |       |
        |      R       C (Condensador)
        |      |       |
   D3 --|<--|--|<--|-- D4
        |      |
         ------
       Tierra
```
- **Componentes**:
  - **Condensador**: El valor depende de la corriente de carga y la tolerancia al rizado (por ejemplo, 1000µF para cargas moderadas).
  - **Carga**: Resistencia o circuito.

#### Cálculo del Rizado
El voltaje de rizado (\\( V_r \\)) se puede aproximar como:
\\[ V_r \approx \frac{I_{carga}}{f \cdot C} \\]
Donde:
- \\( I_{carga} \\): Corriente de carga (A).
- \\( f \\): Frecuencia de la salida rectificada (por ejemplo, 120Hz para onda completa a 60Hz CA).
- \\( C \\): Capacitancia (F).

#### Ejemplo
Para una corriente de carga de 100mA, un condensador de 1000µF y una frecuencia de 120Hz:
\\[ V_r \approx \frac{0.1}{120 \cdot 1000 \times 10^{-6}} \approx 0.833V \\]
Este rizado puede ser aceptable para algunas aplicaciones, pero puede reducirse con un condensador más grande o filtrado adicional (por ejemplo, filtros LC).

#### Otros Filtros
- **Filtro de Inductor**: Utiliza un inductor en serie con la carga para oponerse a los cambios rápidos de corriente.
- **Filtro LC**: Combina inductor y condensador para una mejor reducción del rizado.
- **Filtro Pi**: Configuración condensador-inductor-condensador (C-L-C) para CC muy suave.

---

## 3. Reguladores Lineales vs. Conmutados

Después de la rectificación y el filtrado, el voltaje de CC aún puede variar con cambios en la entrada o demandas de carga. Los **reguladores de voltaje** estabilizan la salida. Hay dos tipos principales: **lineales** y **conmutados**.

### a. Reguladores Lineales
Los reguladores lineales proporcionan un voltaje de salida estable disipando el exceso de potencia como calor.

#### Cómo Funciona
- Actúa como una resistencia variable, ajustando la resistencia para mantener un voltaje de salida constante.
- Requiere que el voltaje de entrada sea mayor que el voltaje de salida deseado (voltaje de desviación).

#### Ejemplo: Regulador Lineal 7805
El **7805** es un regulador lineal popular que proporciona una salida fija de 5V.

#### Diagrama del Circuito
```
Vent ----> [7805] ----> Vsal (5V)
       |         |
      C1        C2
       |         |
      Tierra   Tierra
```
- **Componentes**:
  - **CI 7805**: Sale 5V (hasta 1A con disipador de calor adecuado).
  - **Condensadores**: C1 (0.33µF) y C2 (0.1µF) para estabilidad.
  - **Vent**: Típicamente 7-12V (debe ser >5V + voltaje de desviación, ~2V).

#### Características
- **Salida**: Fija (por ejemplo, 5V para 7805) o ajustable (por ejemplo, LM317).
- **Eficiencia**: Baja, ya que el exceso de voltaje se disipa como calor (\\( Eficiencia \approx \frac{V_{sal}}{V_{ent}} \\)).
- **Ruido**: Bajo, ideal para circuitos analógicos sensibles.

#### Ventajas
- Diseño simple, fácil de implementar.
- Bajo ruido de salida, adecuado para circuitos de audio y de precisión.
- Económico.

#### Desventajas
- Ineficiente, especialmente con grandes diferencias de voltaje.
- Genera calor, requiere disipadores de calor para corrientes altas.
- Limitado a reducción (salida < entrada).

---

### b. Reguladores Conmutados
Los reguladores conmutados utilizan conmutación de alta frecuencia para controlar la transferencia de energía, logrando alta eficiencia.

#### Cómo Funciona
- Un interruptor (generalmente un MOSFET) se enciende/apaga rápidamente, controlando el flujo de energía a través de inductores y condensadores.
- La circuitería de retroalimentación ajusta el ciclo de trabajo de conmutación para mantener una salida estable.

#### Tipos de Reguladores Conmutados
1. **Buck (Reductor)**: Reduce el voltaje (por ejemplo, 12V a 5V).
2. **Boost (Elevador)**: Aumenta el voltaje (por ejemplo, 5V a 12V).
3. **Buck-Boost**: Puede aumentar o reducir (por ejemplo, 9V a 5V o 12V).

#### Diagrama del Circuito (Ejemplo Convertidor Buck)
```
Vent ----> Interruptor (MOSFET) ----> Inductor ----> Vsal
       |                      |
      Diodo                  Condensador
       |                      |
      Tierra                Tierra
```
- **Componentes**:
  - **MOSFET**: Controla la conmutación.
  - **Inductor**: Almacena energía durante el ciclo "on".
  - **Condensador**: Suaviza la salida.
  - **Diodo**: Proporciona una ruta para la corriente del inductor durante el ciclo "off".
  - **CI Controlador**: Por ejemplo, LM2596 (convertidor buck ajustable).

#### Características
- **Eficiencia**: Alta (80-95%), ya que se disipa mínima potencia como calor.
- **Ruido**: Mayor que los reguladores lineales debido a la conmutación.
- **Flexibilidad**: Puede aumentar, reducir o ambas.

#### Ventajas
- Alta eficiencia, ideal para dispositivos alimentados por batería.
- Diseños compactos con disipadores de calor más pequeños.
- Versátil (configuraciones buck, boost o buck-boost).

#### Desventajas
- Más complejo, requiere inductores y un diseño cuidadoso.
- El ruido de conmutación puede interferir con circuitos sensibles.
- Costo más alto debido a componentes adicionales.

---

## 4. Ejemplos Prácticos y Diseño de Circuitos

### Ejemplo 1: Fuente de Alimentación de 5V CC con Rectificador de Media Onda y Regulador Lineal
**Objetivo**: Diseñar una fuente de 5V CC a partir de un transformador de 9V CA.
**Pasos**:
1. **Rectificación**: Usar un diodo 1N4007 para rectificación de media onda.
2. **Filtrado**: Añadir un condensador de 1000µF para suavizar la salida.
3. **Regulación**: Usar un regulador 7805 para una salida estable de 5V.

**Circuito**:
```
9V CA ----> 1N4007 ----> 1000µF ----> 7805 ----> 5V
                     |             |        |
                    Tierra        C1       C2
                                   |        |
                                  Tierra   Tierra
```
- **C1**: 0.33µF (estabilidad de entrada).
- **C2**: 0.1µF (estabilidad de salida).

**Consideraciones**:
- El transformador debe proporcionar >7V CC después de la rectificación (9V CA es suficiente).
- Añadir un disipador de calor al 7805 si la corriente de carga excede 500mA.

---

### Ejemplo 2: Fuente de Alimentación de 5V CC con Rectificador de Onda Completa y Regulador Conmutado
**Objetivo**: Diseñar una fuente de 5V de alta eficiencia a partir de un transformador de 12V CA.
**Pasos**:
1. **Rectificación**: Usar un puente rectificador (cuatro diodos 1N4007).
2. **Filtrado**: Añadir un condensador de 2200µF.
3. **Regulación**: Usar un convertidor reductor LM2596.

**Circuito**:
```
12V CA ----> Puente Rectificador ----> 2200µF ----> LM2596 ----> 5V
                         |                       |
                        Tierra                 Tierra
```
- **LM2596**: Configurado para salida de 5V (ajustable mediante resistencias de retroalimentación).
- **Condensadores**: Seguir la hoja de datos del LM2596 para los condensadores de entrada/salida.

**Consideraciones**:
- Asegurar una selección adecuada del inductor (según la hoja de datos del LM2596).
- Añadir filtrado EMI si se usa en aplicaciones sensibles al ruido.

---

## 5. Aplicaciones y Consideraciones

### Aplicaciones
- **Rectificadores de Media Onda**: Dispositivos de bajo costo y baja potencia (por ejemplo, cargadores de batería simples).
- **Rectificadores de Onda Completa**: Fuentes de alimentación de propósito general para electrónica.
- **Reguladores Lineales**: Circuitos de audio, sensores de precisión y dispositivos de baja potencia.
- **Reguladores Conmutados**: Laptops, smartphones, drivers LED y sistemas alimentados por batería.

### Consideraciones de Diseño
- **Requisitos de Carga**: Asegurar que la fuente pueda manejar la corriente máxima.
- **Eficiencia**: Elegir reguladores conmutados para aplicaciones de alta potencia.
- **Ruido**: Usar reguladores lineales o filtrado adicional para circuitos sensibles.
- **Gestión Térmica**: Incluir disipadores de calor o un diseño de PCB adecuado para la disipación térmica.
- **Especificaciones de los Componentes**: Seleccionar diodos, condensadores y reguladores con las especificaciones de voltaje/corriente apropiadas.

---

## 6. Conclusión
Las fuentes de alimentación de CC son esenciales para alimentar dispositivos electrónicos, y entender sus componentes—rectificadores, filtros y reguladores—es clave para diseñar sistemas confiables. Los **rectificadores de media onda** son simples pero ineficientes, mientras que los **rectificadores de onda completa** ofrecen un mejor rendimiento. Los **reguladores lineales** son ideales para aplicaciones de bajo ruido pero desperdician energía, mientras que los **reguladores conmutados** proporcionan alta eficiencia para dispositivos modernos con alta demanda de energía. Al combinar estos elementos de manera reflexiva, puedes crear fuentes de alimentación robustas adaptadas a necesidades específicas.

Para un aprendizaje práctico, intenta construir los circuitos de ejemplo usando una placa de pruebas o software de simulación como LTspice. Experimenta con diferentes valores de condensadores o tipos de reguladores para observar su impacto en el rendimiento.