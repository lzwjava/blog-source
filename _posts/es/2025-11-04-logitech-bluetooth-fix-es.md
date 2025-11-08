---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Solución de Problemas de Emparejamiento Bluetooth de Logitech
translated: true
type: note
---

### Solución del Error AuthenticationCanceled

Este error ocurre comúnmente con teclados Bluetooth de Logitech (tu MAC `F4:73:35:78:28:4E` coincide con el prefijo OUI de Logitech) durante el emparejamiento en Ubuntu debido a tiempos de espera de autenticación, ausencia de solicitudes de PIN o manejo incorrecto del agente en BlueZ. La breve conexión/desconexión en tu registro sugiere que el teclado responde, pero el proceso excede el tiempo de espera antes de completarse. Otros dispositivos (como `54:2B:FC:F1:1C:D8`) que aparecen pueden causar interferencias—elimínalos primero.

#### Pasos Rápidos de Preparación
1.  **Elimina todos los dispositivos emparejados** para evitar conflictos:
    En `bluetoothctl`, ejecuta `devices` para listarlos, luego `remove <MAC>` para cada uno (ej., `remove 54:2B:FC:F1:1C:D8`). Sal con `exit`.

2.  **Reinicia el servicio Bluetooth**:
    ```
    sudo systemctl restart bluetooth
    sudo systemctl status bluetooth  # Verifica que esté activo
    ```

3.  **Pon el teclado en modo de emparejamiento**: Presiona y mantén presionado el botón de emparejamiento (ej., el canal Easy-Switch o el botón Bluetooth) hasta que el LED parpadee rápidamente. Haz esto de nuevo en cada intento.

#### Pasos Mejorados de Emparejamiento en bluetoothctl
Vuelve a abrir `bluetoothctl` y sigue estos pasos **exactamente**—la configuración del agente es crucial, y confiar en el dispositivo primero a menudo evita algunos tiempos de espera. Para modelos Logitech (ej., K380, K480, MX Keys), ingresa cualquier PIN **a ciegas** en el teclado físico (sin eco en pantalla) inmediatamente después del comando `pair`.

1.  **Entra en bluetoothctl**:
    ```
    bluetoothctl
    ```

2.  **Enciende y configura el agente**:
    ```
    power on
    agent on
    default-agent
    ```

3.  **Escanea y confirma el dispositivo**:
    ```
    scan on
    ```
    Espera a que aparezca `F4:73:35:78:28:4E` (actualiza con Enter si es necesario). Luego:
    ```
    scan off  # Detén el escaneo para enfocarte
    ```

4.  **Confía en el dispositivo** (ayuda con la aceptación automática en reconexiones):
    ```
    trust F4:73:35:78:28:4E
    ```

5.  **Empareja**:
    ```
    pair F4:73:35:78:28:4E
    ```
    - Si aparece un PIN/passkey (ej., `[agent] PIN code: 390412` o `[agent] Passkey: 299595`), **escríbelo inmediatamente en el teclado físico** y presiona Enter. Haz esto a ciegas—incluso si ninguna solicitud parece activa.
    - Si no aparece ningún PIN (común con algunos Logitech), intenta escribir `0000` o `1234` en el teclado y presiona Enter de todos modos.
    - Observa si aparece `[CHG] Paired: yes`. Si se conecta brevemente y luego se desconecta, vuelve a ejecutar `connect F4:73:35:78:28:4E` justo después.

6.  **Conecta y confía**:
    ```
    connect F4:73:35:78:28:4E
    trust F4:73:35:78:28:4E  # Si no se hizo antes
    ```

7.  **Sal y prueba**:
    ```
    exit
    ```
    Abre un editor de texto o terminal—escribe para verificar la entrada. Si funciona, debería reconectarse automáticamente al despertar.

#### Si aún Falla
-   **Alternativa GUI**: Usa Configuración de Ubuntu > Bluetooth (actívalo, selecciona el dispositivo). Esto a menudo muestra una solicitud de PIN visible. Si el agente de CLI falla, el pinentry de la GUI lo maneja mejor.
-   **Reintento de PIN a ciegas**: Incluso sin un código mostrado, algunos usuarios tienen éxito escribiendo `0000` + Enter justo después de `pair`—el teclado se autentica en silencio.
-   **Registros para pistas**: Ejecuta `sudo journalctl -u bluetooth -f` en otra terminal durante el emparejamiento. Busca mensajes de "PIN code" o de tiempo de espera.
-   **Actualizar BlueZ**: Asegúrate de tener la versión más reciente (Ubuntu 24.04+ tiene BlueZ 5.72+ con mejor soporte para Logitech):
    ```
    sudo apt update && sudo apt upgrade bluez
    ```
-   **Particularidad del dongle USB**: Tu emisor BT 5.3 en USB 3.0 está bien, pero prueba en un puerto USB 2.0—se han reportado raras interferencias.
-   **Específico del modelo**: Si es un K480/MX Keys, mantén presionado el botón de emparejamiento durante 5+ segundos. Para dispositivos multi-dispositivo, cambia primero a un canal no utilizado.

Esto debería resolverlo—la mayoría de los casos con Logitech se deben al paso del PIN a ciegas. Si compartes tu modelo exacto o los registros completos, puedo refinar aún más.

[Bluetooth Pairing - AuthenticationCanceled (AskUbuntu)](https://askubuntu.com/questions/1373574/bluetooth-pairing-authenticationcanceled)
[[SOLVED] Bluetooth keyboard: Unable to pair (Arch Linux Forums)](https://bbs.archlinux.org/viewtopic.php?id=174239)
[Barely able to pair Logitech K480 on bluez 5.72 (GitHub)](https://github.com/bluez/bluez/issues/654)