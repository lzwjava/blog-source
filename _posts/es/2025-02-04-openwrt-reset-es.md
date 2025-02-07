---
audio: true
lang: es
layout: post
title: Restablecimiento de OpenWrt
translated: true
---

## Restablecimiento a través de la Interfaz Web

Se recomienda conectar al router mediante un cable ethernet. Después de un restablecimiento, el SSID de Wi-Fi volverá a su configuración predeterminada, lo que puede no ser lo que espera.

## Restablecimiento a través de la Línea de Comandos (SSH)

Puede restablecer OpenWrt a su configuración predeterminada usando la interfaz de línea de comandos (SSH). Así es como:

1.  Conéctese a su router OpenWrt mediante SSH.
2.  Ejecute el siguiente comando:

    ```bash
    root@OpenWrt:~# firstboot
    Esto borrará todas las configuraciones y eliminará cualquier paquete instalado. ¿Está seguro? [N/y]
    y
    /dev/ubi0_1 está montado como /overlay, solo borrando archivos
    root@OpenWrt:~# reboot
    ```
3.  El router se reiniciará con la configuración predeterminada.

**Explicación de los comandos:**

*   `firstboot`: Este comando inicia el proceso de restablecimiento, borrando todas las configuraciones y paquetes instalados.
*   `reboot`: Este comando reinicia el router, aplicando el restablecimiento.
