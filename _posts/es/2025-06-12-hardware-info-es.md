---
audio: false
generated: true
lang: es
layout: post
title: Información de Hardware de Ubuntu Linux
translated: true
type: note
---

Para obtener información completa sobre el hardware de tu laptop (RAM, CPU, etc.) en un sistema Ubuntu Linux, puedes usar una combinación de comandos de terminal y herramientas. A continuación, se presenta una guía paso a paso para recuperar información detallada del sistema:

---

### 1. Verificar Información de la CPU
Para obtener detalles sobre tu CPU (tipo de procesador, velocidad, núcleos, etc.):
- Abre una terminal (Ctrl + Alt + T).
- Ejecuta el siguiente comando:
  ```bash
  lscpu
  ```
  - **Salida**: Muestra la arquitectura de la CPU, número de núcleos, hilos, velocidad del reloj, tamaños de caché, etc.
- Para información más detallada de la CPU, incluyendo el nombre del modelo:
  ```bash
  cat /proc/cpuinfo
  ```
  - Busca campos como `model name`, `cpu MHz` y `cpu cores`.

---

### 2. Verificar Información de la RAM (Memoria)
Para ver la RAM total y la utilizada:
- Ejecuta:
  ```bash
  free -h
  ```
  - **Salida**: Muestra la memoria total, usada y libre en un formato legible (ej., GB o MB).
- Para información detallada de la memoria (ej., tipo, velocidad y ranuras):
  ```bash
  sudo dmidecode -t memory
  ```
  - **Salida**: Proporciona detalles sobre la memoria física, como tamaño, tipo (ej., DDR4), velocidad y uso de ranuras. Requiere privilegios de root.

---

### 3. Verificar Información de Almacenamiento (HDD/SSD)
Para obtener detalles sobre tus dispositivos de almacenamiento:
- Ejecuta:
  ```bash
  lsblk
  ```
  - **Salida**: Lista todos los dispositivos de bloque (ej., SSD, HDD) con sus tamaños y puntos de montaje.
- Para información detallada sobre los discos:
  ```bash
  sudo fdisk -l
  ```
  - **Salida**: Muestra las particiones del disco y sus tamaños. Requiere privilegios de root.
- Para verificar el tipo de disco (ej., HDD o SSD) y el modelo:
  ```bash
  sudo hdparm -I /dev/sda
  ```
  - Reemplaza `/dev/sda` con tu dispositivo de disco (encuéntralo usando `lsblk`).

---

### 4. Verificar Información de la GPU (Tarjeta Gráfica)
Para encontrar detalles sobre tu tarjeta gráfica:
- Ejecuta:
  ```bash
  lspci | grep -i vga
  ```
  o
  ```bash
  lspci | grep -i nvidia
  ```
  - **Salida**: Muestra el modelo de la tarjeta gráfica (ej., Intel, NVIDIA, AMD).
- Para información más detallada de la GPU:
  ```bash
  glxinfo | grep "OpenGL renderer"
  ```
  - Requiere el paquete `mesa-utils` (`sudo apt install mesa-utils` si no está instalado).
- Para GPUs NVIDIA, usa:
  ```bash
  nvidia-smi
  ```
  - **Salida**: Muestra el uso de la GPU, versión del controlador y VRAM (si los controladores NVIDIA están instalados).

---

### 5. Verificar Resumen del Sistema
Para obtener una visión general completa de tu sistema (CPU, RAM, placa base, etc.):
- Ejecuta:
  ```bash
  sudo lshw
  ```
  - **Salida**: Lista información detallada del hardware, incluyendo CPU, RAM, almacenamiento y más. Usa `sudo lshw -short` para una versión concisa.
- Alternativamente, instala y usa `hardinfo` para una interfaz gráfica:
  ```bash
  sudo apt install hardinfo
  hardinfo
  ```
  - **Salida**: Abre una GUI que muestra información detallada del sistema (CPU, RAM, almacenamiento, sensores, etc.).

---

### 6. Verificar Información de BIOS/UEFI y Placa Base
Para obtener detalles de BIOS/UEFI y la placa base:
- Ejecuta:
  ```bash
  sudo dmidecode -t bios
  ```
  - **Salida**: Muestra la versión del BIOS, proveedor y fecha de lanzamiento.
- Para detalles de la placa base:
  ```bash
  sudo dmidecode -t baseboard
  ```
  - **Salida**: Muestra el fabricante, modelo y número de serie de la placa base.

---

### 7. Verificar Detalles del Sistema Operativo y Kernel
Para verificar tu versión de Ubuntu y el kernel:
- Ejecuta:
  ```bash
  lsb_release -a
  ```
  - **Salida**: Muestra la versión de Ubuntu y detalles de la distribución.
- Para información del kernel:
  ```bash
  uname -r
  ```
  - **Salida**: Muestra la versión del kernel de Linux.

---

### 8. Monitorear Recursos del Sistema en Tiempo Real
Para monitorear el uso de CPU, RAM y procesos en tiempo real:
- Ejecuta:
  ```bash
  top
  ```
  o
  ```bash
  htop
  ```
  - **Nota**: Instala `htop` si no está presente (`sudo apt install htop`). Proporciona una interfaz más amigable.

---

### 9. Informe Completo del Sistema con `inxi`
Para un solo comando que recopila información extensa del sistema:
- Instala `inxi`:
  ```bash
  sudo apt install inxi
  ```
- Ejecuta:
  ```bash
  inxi -Fxz
  ```
  - **Salida**: Proporciona un informe detallado incluyendo CPU, RAM, GPU, almacenamiento, red y más. El flag `-F` da un reporte completo, `-x` añade detalles extra y `-z` filtra información sensible.

---

### Ejemplo de Salida (Usando `inxi -Fxz`)
```plaintext
System:    Host: ubuntu-laptop Kernel: 5.15.0-73-generic x86_64 bits: 64 Desktop: GNOME 42.0
           Distro: Ubuntu 22.04.2 LTS (Jammy Jellyfish)
Machine:   Type: Laptop System: Dell product: Inspiron 15 v: N/A serial: <filter>
           Mobo: Dell model: 0XYZ serial: <filter> UEFI: Dell v: 1.2.3 date: 05/10/2023
CPU:       Info: 8-core model: Intel Core i7-12700H bits: 64 type: MT MCP cache: L2: 11.5 MiB
           Speed: 2500 MHz min/max: 400/4700 MHz Core speeds (MHz): 1: 2500 2: 2400 ...
Memory:    RAM: total: 15.5 GiB used: 3.2 GiB (20.6%)
           Array-1: capacity: 32 GiB slots: 2 EC: None
           Device-1: DIMM A size: 8 GiB speed: 3200 MT/s type: DDR4
           Device-2: DIMM B size: 8 GiB speed: 3200 MT/s type: DDR4
Graphics:  Device-1: Intel Alder Lake-P Integrated Graphics driver: i915 v: kernel
           Device-2: NVIDIA GA107M [GeForce RTX 3050 Mobile] driver: nvidia v: 535.54.03
           Display: x11 server: X.Org v: 1.21.1.4 driver: X: loaded: modesetting,nvidia
           OpenGL: renderer: Mesa Intel UHD Graphics (ADL-S GT2) v: 4.6 Mesa 23.0.4
Drives:    Local Storage: total: 512 GiB used: 120 GiB (23.4%)
           ID-1: /dev/nvme0n1 vendor: Samsung model: SSD 970 EVO Plus 500GB size: 512 GiB
...
```

---

### Notas
- Algunos comandos (ej., `dmidecode`, `fdisk`) requieren privilegios de root (`sudo`).
- Si un comando no está instalado (ej., `inxi`, `htop`, `mesa-utils`), instálalo usando `sudo apt install <nombre-del-paquete>`.
- Para una herramienta gráfica, `hardinfo` o `gnome-system-monitor` (preinstalado en Ubuntu) pueden proporcionar una interfaz amigable.
- Si necesitas detalles específicos (ej., información de la batería, adaptadores de red), házmelo saber y puedo proporcionar comandos adicionales.

¡Avísame si necesitas ayuda para interpretar la salida o quieres centrarte en un componente específico!