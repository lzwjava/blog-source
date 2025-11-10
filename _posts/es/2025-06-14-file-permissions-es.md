---
audio: false
generated: true
lang: es
layout: post
title: Permisos de Archivo
translated: true
type: note
---

El `crw-rw----` en la salida de `ls -alrt /dev/ttyUSB0` representa el **tipo de archivo y los permisos** para el archivo de dispositivo `/dev/ttyUSB0`. Aquí tienes un desglose:

- **c**: El primer carácter indica el tipo de archivo. `c` significa que es un **dispositivo de caracteres** (a diferencia de `b` para dispositivo de bloques, `d` para directorio o `-` para archivo regular). `/dev/ttyUSB0` es un dispositivo de puerto serial, típicamente usado para adaptadores USB-a-serial.

- **rw-rw----**: Los siguientes nueve caracteres representan los **permisos** para el archivo, divididos en tres grupos:
  - **rw-** (posiciones 2-4): Permisos para el **propietario** (root). El propietario puede **leer** (`r`) y **escribir** (`w`), pero no ejecutar (`-`).
  - **rw-** (posiciones 5-7): Permisos para el **grupo** (dialout). Los miembros del grupo `dialout` también pueden **leer** y **escribir**, pero no ejecutar.
  - **---** (posiciones 8-10): Permisos para **otros** (usuarios que no son el propietario ni del grupo). Otros no tienen **ningún permiso** (no pueden leer, escribir ni ejecutar).

### Resumen
- `/dev/ttyUSB0` es un archivo de dispositivo de caracteres.
- El propietario (`root`) y el grupo (`dialout`) pueden leer y escribir en el dispositivo.
- Otros usuarios no tienen acceso.
- Para interactuar con este dispositivo (por ejemplo, para comunicación serial), tu cuenta de usuario típicamente necesita estar en el grupo `dialout`. Puedes verificarlo con `groups` y agregarte con `sudo usermod -a -G dialout <nombre_de_usuario>` si es necesario (luego cierra la sesión y vuelve a iniciarla).