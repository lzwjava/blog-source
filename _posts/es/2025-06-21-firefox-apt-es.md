---
audio: false
generated: true
lang: es
layout: post
title: Instalación de Firefox mediante APT en Ubuntu
translated: true
type: note
---

Esta guía detalla cómo instalar Firefox desde el repositorio APT de Mozilla en Ubuntu, reemplazando el paquete Snap predeterminado.

**¿Por qué usar la versión APT?**

Si bien la versión Snap es conveniente, algunos usuarios prefieren la versión APT por una mejor integración y rendimiento.

**Pasos:**

1.  **Desinstalar el Snap de Firefox:**

    ```bash
    sudo snap remove firefox
    ```

2.  **Crear un directorio keyring para APT (si no existe):**

    ```bash
    sudo install -d -m 0755 /etc/apt/keyrings
    ```

3.  **Importar la clave de firma del repositorio APT de Mozilla:**

    ```bash
    wget -q https://packages.mozilla.org/apt/repo-signing-key.gpg -O- | sudo tee /etc/apt/keyrings/packages.mozilla.org.asc > /dev/null
    ```
    *Si `wget` no está instalado, instálelo primero: `sudo apt install wget`*

4.  **Agregar el repositorio de Mozilla a la lista de fuentes:**

    ```bash
    echo "deb [signed-by=/etc/apt/keyrings/packages.mozilla.org.asc] https://packages.mozilla.org/apt mozilla main" | sudo tee -a /etc/apt/sources.list.d/mozilla.list > /dev/null
    ```

5.  **Establecer la prioridad del paquete para preferir el DEB de Mozilla:**

    Esto evita que el paquete de transición de Ubuntu reinstale el Snap.

    ```bash
    echo '
    Package: *
    Pin: origin packages.mozilla.org
    Pin-Priority: 1000

    Package: firefox*
    Pin: release o=Ubuntu
    Pin-Priority: -1' | sudo tee /etc/apt/preferences.d/mozilla
    ```

6.  **Eliminar el DEB de Firefox de Ubuntu (si está presente) e instalar la versión de Mozilla:**

    ```bash
    sudo apt update && sudo apt remove firefox
    sudo apt install firefox
    ```

¡Ahora tienes Firefox instalado desde el repositorio APT oficial de Mozilla!