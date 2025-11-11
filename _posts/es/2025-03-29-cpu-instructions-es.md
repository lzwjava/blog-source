---
audio: false
generated: true
lang: es
layout: post
title: Cómo una CPU Procesa Instrucciones
translated: true
type: note
---

Esta imagen parece ser una página de un libro de texto o apuntes de clase sobre arquitectura de computadoras, centrándose específicamente en el diseño de una CPU (Unidad Central de Procesamiento) con un enfoque en el Memory Address Register (MAR) y sus operaciones relacionadas. Aquí hay una explicación detallada del contenido:

### Descripción del Texto:
1.  **Introducción:**
    *   El texto menciona una CPU de 16 bits y discute la función del Memory Address Register (MAR) en la operación de la CPU.
    *   El MAR se describe como un registro de 16 bits utilizado para almacenar direcciones de memoria.

2.  **Operaciones que involucran al MAR:**
    *   **Instrucción 1:** El texto describe una operación donde el contenido del registro R2 se resta del contenido del registro R1, y el resultado se almacena nuevamente en R1. Adicionalmente, el contenido del MAR se mueve a R1.
    *   **Instrucción 2:** El texto menciona otra operación que involucra al MAR, pero los detalles específicos no son completamente visibles en la imagen.

### Descripción del Diagrama:
El diagrama ilustra la estructura y el flujo de datos dentro de una CPU, destacando la interacción entre varios registros y la Arithmetic Logic Unit (ALU). Estos son los componentes clave:

1.  **Registros:**
    *   **IR (Instruction Register):** Contiene la instrucción actual que se está ejecutando.
    *   **PC (Program Counter):** Lleva el registro de la dirección de la siguiente instrucción a ejecutar.
    *   **MAR (Memory Address Register):** Almacena la dirección de la ubicación de memoria a la que se está accediendo.
    *   **MDR (Memory Data Register):** Contiene los datos que se leen o escriben en la memoria.
    *   **R1 y R2:** Registros de propósito general utilizados para el almacenamiento temporal y la manipulación de datos.
    *   **Y:** Otro registro involucrado en el procesamiento de datos.

2.  **ALU (Arithmetic Logic Unit):**
    *   Realiza operaciones aritméticas y lógicas con los datos almacenados en los registros.
    *   La ALU tiene entradas A y B, y una salida Z.
    *   Las operaciones incluyen suma (ADD), resta (SUB) y operaciones bit a bit (1-Cx).

3.  **Flujo de Datos:**
    *   El diagrama muestra el flujo de datos entre los registros, la ALU y la memoria.
    *   Las flechas indican la dirección de la transferencia de datos, como desde el MAR al bus de direcciones de memoria y desde el bus de datos de memoria al MDR.

### Resumen:
La imagen proporciona una visión general de cómo una CPU procesa instrucciones, centrándose en la función del MAR en la direccionamiento de memoria y la interacción entre varios registros y la ALU. El texto y el diagrama juntos ilustran las operaciones fundamentales de una CPU, incluyendo la transferencia de datos y las operaciones aritméticas/lógicas.