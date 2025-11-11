---
audio: false
generated: true
lang: es
layout: post
title: Cómo eliminar el cliente de Outline VPN en Ubuntu
translated: true
type: note
---

Parece que `apt` no puede encontrar un paquete llamado `outline-client`. Esto normalmente significa una de dos cosas:

1.  **No instalaste Outline usando `apt` (es decir, no se instaló como un paquete .deb).** Esta es la razón más común para este error con Outline, ya que muchos usuarios lo instalan mediante el AppImage.
2.  **El nombre del paquete es diferente, o el repositorio no está configurado.** Aunque es menos probable para Outline, es una posibilidad para otro software.

Dado tu intento anterior, es muy probable que lo hayas instalado como un **AppImage**. En este caso, tendrás que eliminarlo manualmente.

Aquí te explicamos cómo proceder:

**1. Localiza y Elimina el Archivo AppImage:**

El cliente Outline, cuando se instala como AppImage, suele ser un único archivo ejecutable. Es probable que lo descargaras en tu carpeta `Descargas`, o quizás lo movieras a una carpeta `bin` o `Aplicaciones` en tu directorio personal.

* **Ubicaciones comunes para revisar:**
    * `~/Descargas/`
    * `~/Aplicaciones/` (si la creaste)
    * `~/bin/` (si la creaste)
    * El directorio desde donde lo ejecutaste originalmente.

* **Cómo encontrarlo:** Puedes usar el comando `find` para buscarlo en tu directorio personal:
    ```bash
    find ~ -name "Outline-Client*.AppImage" 2>/dev/null
    ```
    Este comando buscará en tu directorio personal cualquier archivo que comience con "Outline-Client" y termine con ".AppImage".
    Una vez encontrado, elimínalo:
    ```bash
    rm /ruta/al/Outline-Client.AppImage
    ```
    (Reemplaza `/ruta/al/` con la ruta real encontrada por el comando `find`.)

**2. Elimina los Archivos de Configuración Residuales y de Inicio Automático:**

Incluso si eliminas el AppImage, Outline podría haber creado algunos archivos de configuración y una entrada de inicio automático.

* **Eliminar el directorio de configuración:**
    ```bash
    rm -rf ~/.config/Outline/
    ```
    Este comando elimina todo el directorio `Outline` dentro de la carpeta de configuración de tu usuario.

* **Eliminar la entrada de inicio automático (si se creó):**
    Si Outline estaba configurado para iniciarse automáticamente cuando inicias sesión, podría haber un archivo `.desktop` para él.
    ```bash
    rm -f ~/.config/autostart/Outline-Client.AppImage.desktop
    ```

* **Eliminar los iconos del escritorio (si los hay):**
    A veces los AppImages crean un icono en el escritorio en tu directorio local de iconos.
    ```bash
    find ~/.local/share/icons -name "appimagekit-outline-client*.png" -delete
    ```
    Esto eliminará cualquier icono PNG relacionado con el AppImage de Outline.

**3. Verifica y Restaura la Configuración de Red (si es necesario):**

Outline, como otras VPN, puede modificar la configuración de tu DNS. Si experimentas problemas de conectividad a Internet después de eliminar el AppImage, revisa tu archivo `/etc/resolv.conf`.

* **Inspecciona `resolv.conf`:**
    ```bash
    cat /etc/resolv.conf
    ```
    Busca líneas que parezcan haber sido añadidas por Outline (por ejemplo, direcciones IP específicas para servidores de nombres que no reconozcas como los DNS de tu router o proveedor de Internet).

* **Restaura `resolv.conf` (si es necesario):**
    Si parece que Outline lo modificó:
    * **Opción A (Recomendada para Ubuntu moderno):** Si tu sistema usa `systemd-resolved` (lo cual es común en versiones recientes de Ubuntu), normalmente puedes solucionarlo recreando el enlace simbólico:
        ```bash
        sudo rm /etc/resolv.conf
        sudo ln -s /run/systemd/resolve/stub-resolv.conf /etc/resolv.conf
        ```
    * **Opción B (Edición Manual - úsala si la Opción A no funciona o para sistemas antiguos):**
        Primero, haz una copia de seguridad:
        ```bash
        sudo cp /etc/resolv.conf /etc/resolv.conf.bak
        ```
        Luego, edita el archivo:
        ```bash
        sudo nano /etc/resolv.conf
        ```
        Comenta o elimina cualquier línea `nameserver` que haya sido añadida por Outline. Si no estás seguro de los DNS de tu ISP, puedes poner servidores DNS públicos como los de Google (`8.8.8.8` y `8.8.4.4`) o los de Cloudflare (`1.1.1.1` y `1.0.0.1`).

**4. Reinicia tu Sistema:**

Después de completar estos pasos, es muy recomendable reiniciar tu sistema Ubuntu para asegurarte de que todos los cambios surtan efecto y de que cualquier proceso en segundo plano relacionado con Outline se termine por completo.

```bash
sudo reboot
```

Siguiendo estos pasos de eliminación manual, deberías poder deshacerte por completo del cliente de VPN Outline de tu sistema Ubuntu.