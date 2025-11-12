---
audio: false
generated: true
lang: es
layout: post
title: Tutorial de Sistemas de Memoria
translated: true
type: note
---

Este tutorial cubre los conceptos clave de los sistemas de memoria, centrándose en la clasificación de la memoria, los principios de RAM/ROM y las técnicas de decodificación de direcciones. Desglosemos esto en secciones completas.

## 1. Clasificación de la Memoria

La memoria de la computadora se puede clasificar ampliamente en dos categorías principales:

### 1.1 Por Función
- **Memoria Primaria**: Accesible directamente por la CPU
  - RAM (Random Access Memory): Almacenamiento temporal
  - ROM (Read-Only Memory): Almacenamiento permanente
- **Memoria Secundaria**: Dispositivos de almacenamiento externos (discos duros, SSD, etc.)

### 1.2 Por Retención de Datos
- **Memoria Volátil**: Pierde los datos cuando se apaga la energía (la mayoría de la RAM)
- **Memoria No Volátil**: Retiene los datos sin energía (ROM, Flash)

### 1.3 Por Método de Acceso
- **Acceso Aleatorio**: Cualquier ubicación se puede acceder directamente (RAM, ROM)
- **Acceso Secuencial**: Los datos se acceden en secuencia (cintas magnéticas)

## 2. Principios de Funcionamiento de la RAM

La RAM (Random Access Memory) es la memoria de trabajo principal de la computadora.

### 2.1 DRAM (Dynamic RAM)
- Almacena cada bit en un pequeño capacitor y transistor
- Requiere refresco periódico para mantener los datos (normalmente cada pocos milisegundos)
- Mayor densidad, menor costo, más común en la memoria principal
- Ciclo de operación: row address strobe (RAS) → column address strobe (CAS) → acceso a datos

### 2.2 SRAM (Static RAM)
- Utiliza circuitos flip-flop para almacenar cada bit
- No necesita refresco, retiene los datos mientras haya energía
- Más rápida, pero más costosa y de menor densidad que la DRAM
- Se utiliza en la memoria caché

### 2.3 Organización de la RAM
- Organizada en un formato de matriz de filas y columnas
- Cada celda tiene una dirección única (fila + columna)
- Los bits de datos normalmente se organizan en longitudes de palabra (8, 16, 32, 64 bits)

## 3. Principios de Funcionamiento de la ROM

La ROM (Read-Only Memory) almacena datos permanentes o semipermanentes.

### 3.1 Tipos de ROM
- **Mask ROM**: Programada durante la fabricación, no se puede modificar
- **PROM (Programmable ROM)**: El usuario puede programarla una vez
- **EPROM (Erasable PROM)**: Se puede borrar con luz UV y reprogramar
- **EEPROM (Electrically EPROM)**: Se puede borrar y reprogramar eléctricamente
- **Flash Memory**: Forma moderna de EEPROM, permite el borrado por bloques

### 3.2 Operación de la ROM
- Contiene datos preescritos en el momento de fabricación o programación
- Lectura: Dirección → decodificador → amplificador de sensibilidad → búferes de salida
- Escritura (para tipos escribibles): Se utiliza un voltaje más alto para modificar las celdas de almacenamiento

## 4. Expansión de Memoria

A medida que los programas se vuelven más complejos, a menudo es necesaria la expansión de la memoria.

### 4.1 Expansión de Capacidad
- **Selección de Chips**: Usar múltiples chips de memoria para aumentar la memoria total
- **Expansión de Longitud de Palabra**: Combinar chips para aumentar el ancho del bus de datos
- **Expansión del Espacio de Direcciones**: Aumentar el espacio de memoria direccionable

### 4.2 Bancos de Memoria
- La memoria se organiza en bancos que se pueden acceder de forma independiente
- Permite el entrelazado, reduciendo el tiempo medio de acceso
- Facilita las operaciones paralelas en arquitecturas modernas

## 5. Técnicas de Decodificación de Direcciones

La decodificación de direcciones es crucial para acceder a la ubicación de memoria correcta.

### 5.1 Selección Lineal (Decodificación Completa)
- Cada línea de dirección se conecta directamente a una ubicación de memoria
- Simple pero ineficiente para grandes espacios de memoria
- Ejemplo: En un sistema con 16 líneas de dirección, necesitamos 2^16 (65,536) conexiones individuales

### 5.2 Selección Basada en Decodificador
- **Decodificadores de Direcciones**: Convierten la dirección binaria en señales de selección one-hot
- **Decodificador 2 a 4**: Toma 2 bits de dirección, activa una de 4 líneas de salida
- **Decodificador 3 a 8**: Toma 3 bits de dirección, activa una de 8 líneas de salida
- ICs comunes: 74LS138 (3 a 8), 74LS154 (4 a 16)

### 5.3 Decodificación Parcial
- No todos los bits de dirección se decodifican, conservando hardware
- Múltiples ubicaciones de memoria pueden mapearse a la misma ubicación física
- Crea "sombras" o "reflejos" de memoria

### 5.4 Mapeo de Memoria
- **Mapeo Contiguo**: Bloques de memoria dispuestos secuencialmente
- **Mapeo Paginado**: Memoria dividida en páginas de tamaño fijo
- **Mapeo Segmentado**: Memoria dividida en segmentos de tamaño variable

## 6. Ejemplos de Implementación

### 6.1 Ejemplo Sencillo de Expansión de RAM
Para expandir un sistema RAM de 32K × 8 a 128K × 8:
1. Usar cuatro chips RAM de 32K × 8
2. Usar 2 bits de dirección de orden superior para seleccionar entre los cuatro chips
3. Conectar las líneas de dirección restantes a todos los chips en paralelo
4. Usar un decodificador de 2 a 4 para la selección de chips

### 6.2 Circuito de Decodificación de Direcciones

Para un sistema con memoria mapeada en el rango de direcciones 0x8000-0x9FFF:
1. Las líneas de dirección A15-A13 deben ser "100" (para 0x8000-0x9FFF)
2. Usar compuertas AND para detectar este patrón
3. Habilitar el chip de memoria apropiado cuando se detecte este patrón

Esto completa nuestra visión general de los sistemas de memoria, centrándonos en la clasificación, los principios de funcionamiento y las técnicas de expansión. La comprensión de estos conceptos es fundamental para diseñar y trabajar con sistemas informáticos de manera efectiva.