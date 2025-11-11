---
audio: false
generated: true
lang: es
layout: post
title: Información del Sistema Linux
translated: true
type: note
---

En Ubuntu, puedes obtener información del sistema como si es de 32 o 64 bits, la versión del sistema operativo, la cantidad de RAM y el tamaño del disco usando los siguientes comandos. A continuación se presenta una guía paso a paso:

### 1. Determinar si el Sistema es de 32 o 64 bits
- **Comando**: `uname -m`
- **Explicación**: Este comando muestra el nombre del hardware de la máquina.
  - Si la salida es `x86_64`, tu sistema es de **64 bits**.
  - Si la salida es `i686` o `i386`, tu sistema es de **32 bits**.
- **Salida de Ejemplo**:
  ```
  x86_64
  ```
  Esto indica un sistema de 64 bits.

### 2. Obtener la Versión del Sistema Operativo (SO)
- **Comando**: `lsb_release -a`
- **Explicación**: Este comando proporciona información detallada sobre la Linux Standard Base (LSB) y la distribución.
  - Busca la línea `Description` para ver la versión de Ubuntu.
- **Salida de Ejemplo**:
  ```
  No LSB modules are available.
  Distributor ID: Ubuntu
  Description:    Ubuntu 20.04.3 LTS
  Release:        20.04
  Codename:       focal
  ```
  Aquí, el SO es **Ubuntu 20.04.3 LTS**.

### 3. Obtener el Tamaño de la RAM
- **Comando**: `free -h`
- **Explicación**: Este comando muestra el uso de la memoria en un formato legible (ej. GB o MB).
  - Mira la columna `total` bajo la fila `Mem:` para encontrar la RAM total instalada.
- **Salida de Ejemplo**:
  ```
              total        used        free      shared  buff/cache   available
  Mem:          15Gi       2.3Gi       9.5Gi       300Mi       3.8Gi        12Gi
  Swap:        2.0Gi         0B       2.0Gi
  ```
  En este caso, la RAM total es de **15 GB**.

### 4. Obtener el Tamaño del Disco
- **Comando**: `lsblk -d -o NAME,SIZE`
- **Explicación**: Este comando lista todos los dispositivos de disco (excluyendo particiones) con sus tamaños.
  - El flag `-d` asegura que solo se muestren los dispositivos de disco (ej. `/dev/sda`), no sus particiones.
  - Busca el nombre del disco (ej. `sda`) y su tamaño correspondiente.
- **Salida de Ejemplo**:
  ```
  NAME   SIZE
  sda    1T
  sdb    500G
  ```
  Aquí, el sistema tiene dos discos: `/dev/sda` con un tamaño de **1 terabyte** y `/dev/sdb` con **500 gigabytes**. Si solo tienes un disco, típicamente será `sda`.

### Notas
- Estos comandos usan herramientas estándar disponibles en Ubuntu, sin requerir instalaciones adicionales.
- Para el tamaño del disco, si tu sistema tiene múltiples discos, la salida los listará todos. Típicamente, `/dev/sda` es el disco principal.
- Ejecuta estos comandos en una terminal para ver los resultados específicos de tu sistema.

¡Con estos comandos, puedes reunir rápidamente la información esencial del sistema que necesitas en tu máquina Ubuntu!