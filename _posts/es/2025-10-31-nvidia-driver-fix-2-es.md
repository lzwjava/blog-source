---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Solución de Conflictos en Paquetes de Controladores NVIDIA
translated: true
type: note
---

Esto parece un conflicto clásico de paquetes durante una actualización de controladores NVIDIA en Ubuntu (probablemente 22.04 según las versiones de los paquetes). El paquete `nvidia-kernel-common-535` está intentando sobrescribir un archivo de firmware (`gsp_ga10x.bin`) que ya pertenece a `nvidia-firmware-535`, haciendo que dpkg falle. Este es un problema conocido con los controladores NVIDIA de la serie 535 de los repositorios de Ubuntu.

No entres en pánico—tu sistema debería poder arrancar (aunque los gráficos podrían estar en modo de renderizado por software si el controlador está parcialmente dañado). Aquí tienes una solución paso a paso para resolverlo de forma segura. Ejecuta estos comandos en una terminal (usa TTY si la GUI es inestable: Ctrl+Alt+F3 para cambiar).

### Intento de Solución Rápida (Primero lo más Seguro)
1. Intenta reparar automáticamente los paquetes dañados:
   ```
   sudo apt --fix-broken install
   ```
   Esto a menudo resuelve problemas de dependencias/desempaquetado sin intervención manual.

2. Si eso falla (o tiene éxito parcialmente pero deja errores), limpia la instalación interrumpida:
   ```
   sudo dpkg --configure -a
   sudo apt update
   sudo apt upgrade
   ```

### Si Todavía No Funciona: Forzar la Sobrescritura del Archivo en Conflicto
El error está específicamente en el archivo deb `nvidia-kernel-common-535`. Fuerza a dpkg a sobrescribir el archivo duplicado:
```
sudo dpkg -i --force-overwrite /var/cache/apt/archives/nvidia-kernel-common-535_535.274.02-0ubuntu1_amd64.deb
```
- Esto instala solo ese paquete, ignorando el conflicto de archivos.
- Luego ejecuta:
  ```
  sudo apt --fix-broken install
  sudo apt autoremove
  sudo apt upgrade
  ```
- Reinicia después: `sudo reboot`.

### Opción Nuclear: Purgar y Reinstalar los Paquetes NVIDIA
Si lo anterior no funciona (por ejemplo, hay una incompatibilidad de versiones más profunda), elimina los componentes NVIDIA conflictivos y reinstala:
1. Purga los paquetes problemáticos (adapta las versiones si es necesario—verifica con `dpkg -l | grep nvidia`):
   ```
   sudo dpkg --force-all -P nvidia-firmware-535-535.274.02 nvidia-kernel-common-535
   ```
2. Limpia:
   ```
   sudo apt autoremove --purge
   sudo apt autoclean
   ```
3. Reinstala el controlador:
   ```
   sudo apt update
   sudo apt install nvidia-driver-535
   ```
4. Reinicia.

### Prevención/Consejos
- Añade el PPA graphics-drivers para actualizaciones NVIDIA más estables: `sudo add-apt-repository ppa:graphics-drivers/ppa && sudo apt update`.
- Si estás en un portátil, asegúrate de que Secure Boot esté desactivado en la BIOS antes de instalar controladores.
- Después del reinicio, prueba con `nvidia-smi` (debería mostrar tu GPU) o `prime-select query` (si tienes NVIDIA Optimus).
- Si esto rompe tu pantalla por completo, arranca en modo de recuperación y ejecuta las soluciones desde allí.

Si nada de esto funciona o obtienes un nuevo error, pega la salida completa aquí para más ajustes.

### Referencias
- [Unmet dependencies nvidia-dkms-535 - package conflict breaks Ubuntu 22.04 install](https://forums.developer.nvidia.com/t/unmet-dependencies-nvidia-dkms-535-package-conflict-breaks-ubuntu-22-04-install/265788)
- [Ubuntu and NVIDIA-provided packages conflict, breaking installation](https://forums.developer.nvidia.com/t/ubuntu-and-nvidia-provided-packages-conflict-breaking-installation/259150)
- [Problem with nvidia package dependencies](https://askubuntu.com/questions/1491916/problem-with-nvidia-package-dependencies)
- [nvidia-kernel-common-535 conflicts with nvidia-firmware-535](https://superuser.com/questions/1833427/nvidia-kernel-common-535-conflicts-with-nvidia-firmware-535-535-161-07-535-161-0)