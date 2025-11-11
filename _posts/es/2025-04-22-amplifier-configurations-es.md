---
audio: false
generated: true
lang: es
layout: post
title: Configuraciones de Amplificador
translated: true
type: note
---

Aquí tienes una explicación completa de las **tres configuraciones básicas de amplificadores**—**Emisor Común (CE)**, **Colector Común (CC)** (también conocido como **Seguidor de Emisor**), y **Base Común (CB)**—centrándose en su estructura, características de señal, ventajas, desventajas y aplicaciones típicas.

---

## 🔷 1. Amplificador de Emisor Común (CE)

### 🔧 Configuración
- **Entrada**: Aplicada entre la base y el emisor.
- **Salida**: Tomada del colector y el emisor.
- **Terminal común**: El emisor es común tanto para la entrada como para la salida.

### 🔍 Características Clave

| Propiedad                | Descripción                       |
|-------------------------|------------------------------------|
| **Ganancia de Voltaje** | Alta                               |
| **Ganancia de Corriente** | Moderada a alta                   |
| **Ganancia de Potencia** | Alta                               |
| **Desplazamiento de Fase** | 180° (salida invertida)             |
| **Impedancia de Entrada** | Moderada                           |
| **Impedancia de Salida** | Moderada                           |

### ✅ Ventajas
- Bueno para amplificación de voltaje y potencia.
- Configuración más ampliamente utilizada.

### ❌ Desventajas
- Invierte la señal (desplazamiento de fase de 180°).
- Menos adecuado para adaptación de impedancia.

### 🧰 Aplicaciones
- Amplificación de señal de propósito general.
- Amplificadores de audio.
- Etapas intermedias en amplificadores.

---

## 🔷 2. Amplificador de Colector Común (CC) — *Seguidor de Emisor*

### 🔧 Configuración
- **Entrada**: Aplicada entre la base y el colector.
- **Salida**: Tomada del emisor y el colector.
- **Terminal común**: El colector es común.

### 🔍 Características Clave

| Propiedad                | Descripción                           |
|-------------------------|----------------------------------------|
| **Ganancia de Voltaje** | Aproximadamente 1 (ganancia unidad)    |
| **Ganancia de Corriente** | Alta                                   |
| **Ganancia de Potencia** | Moderada                               |
| **Desplazamiento de Fase** | 0° (sin inversión)                      |
| **Impedancia de Entrada** | Alta                                   |
| **Impedancia de Salida** | Baja                                    |

### ✅ Ventajas
- Excelente etapa buffer.
- Buena para adaptación de impedancia (alta impedancia de entrada, baja impedancia de salida).
- Sin inversión de señal.

### ❌ Desventajas
- Sin ganancia de voltaje.
- No es adecuado como amplificador independiente donde se necesita amplificación de voltaje.

### 🧰 Aplicaciones
- Buffer entre etapas.
- Manejo de cargas de baja impedancia.
- Seguidores de voltaje.

---

## 🔷 3. Amplificador de Base Común (CB)

### 🔧 Configuración
- **Entrada**: Aplicada entre el emisor y la base.
- **Salida**: Tomada del colector y la base.
- **Terminal común**: La base es común.

### 🔍 Características Clave

| Propiedad                | Descripción                             |
|-------------------------|------------------------------------------|
| **Ganancia de Voltaje** | Alta                                     |
| **Ganancia de Corriente** | Menor que 1                              |
| **Ganancia de Potencia** | Moderada                                 |
| **Desplazamiento de Fase** | 0° (sin inversión)                        |
| **Impedancia de Entrada** | Muy baja                                 |
| **Impedancia de Salida** | Alta                                     |
| **Respuesta en Frecuencia** | Muy amplia (buena para uso en alta frecuencia) |

### ✅ Ventajas
- Excelente respuesta en alta frecuencia.
- Operación estable.

### ❌ Desventajas
- Baja impedancia de entrada—requiere un diseño cuidadoso de la etapa de excitación.
- Ganancia de corriente limitada.

### 🧰 Aplicaciones
- Amplificadores de RF (radiofrecuencia).
- Amplificación de señales de alta frecuencia.
- Adaptación de impedancia (para fuentes de baja impedancia a cargas de alta impedancia).

---

## 🧠 Tabla Resumen

| Configuración   | Ganancia de Voltaje | Ganancia de Corriente | Desplazamiento de Fase | Impedancia Entrada | Impedancia Salida | Aplicación                    |
|-----------------|--------------|--------------|-------------|---------|----------|-------------------------------|
| **Emisor Común (CE)**   | Alta         | Alta         | 180°       | Media  | Media   | Amplificación general         |
| **Colector Común (CC)** | ≈1 (unidad)   | Alta         | 0°         | Alta    | Baja      | Buffering, adaptación de impedancia |
| **Base Común (CB)**       | Alta         | <1           | 0°         | Baja     | Alta     | Uso en alta frecuencia            |

---

¿Te gustarían diagramas visuales de estas configuraciones o un análisis de circuito de ejemplo para alguna de ellas?