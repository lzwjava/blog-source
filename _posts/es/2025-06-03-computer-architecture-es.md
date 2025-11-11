---
audio: false
generated: true
lang: es
layout: post
title: Determinar el Tipo de Arquitectura de Computadora
translated: true
type: note
---

Para determinar si tu computadora actual tiene una arquitectura x86 de 64 bits (x64) o ARM64, sigue estas instrucciones según tu sistema operativo:

**Windows:**

1.  **Presiona la tecla Windows + R** para abrir el cuadro de diálogo Ejecutar.
2.  **Escribe `msinfo32`** y presiona Enter. Esto abrirá la ventana de Información del sistema.
3.  En la ventana de Información del sistema, busca la entrada **"Tipo de sistema"**.
    * Si dice **"PC basado en x64"**, tu computadora tiene un procesador x86 de 64 bits (x64).
    * Si dice **"PC basado en ARM64"**, tu computadora tiene un procesador ARM de 64 bits (ARM64).

**macOS:**

1.  Haz clic en el **menú Apple** en la esquina superior izquierda de tu pantalla.
2.  Selecciona **"Acerca de esta Mac"**.
3.  En la pestaña "Descripción general", busca la información del **"Procesador"** o **"Chip"**:
    * Si aparece un **procesador Intel** (por ejemplo, Intel Core i7, Intel Core i9), tu Mac tiene un procesador x86 de 64 bits (x64).
    * Si aparece un **chip de silicio de Apple** (por ejemplo, Apple M1, Apple M2, Apple M3), tu Mac tiene un procesador ARM64.

**Linux:**

1.  Abre una ventana de **terminal**.
2.  Escribe el siguiente comando y presiona Enter:
    ```bash
    uname -m
    ```
3.  La salida indicará la arquitectura:
    * **`x86_64`** o **`amd64`**: Esto indica un procesador x86 de 64 bits (x64).
    * **`aarch64`** o **`arm64`**: Esto indica un procesador ARM de 64 bits (ARM64).
    * Otras salidas podrían indicar un sistema de 32 bits (aunque son menos comunes hoy en día).

Basándonos en los componentes que has listado para tu nueva construcción, el procesador **Intel Core i9-13900KF** es un procesador de arquitectura **x64 (x86 de 64 bits)**. Por lo tanto, la nueva computadora que estás construyendo será un **sistema basado en x64**.