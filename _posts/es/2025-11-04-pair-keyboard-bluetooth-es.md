---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Emparejar Teclado Logitech por Bluetooth CLI
translated: true
type: note
---

### Requisitos Previos
- Asegúrate de que tu emisor Bluetooth 5.3 (dongle) esté conectado al puerto USB 3.0 y que Ubuntu lo reconozca. Ejecuta `lsusb` en la terminal para verificar si aparece (busca algo como "Bluetooth" o el ID del fabricante). Si no, prueba un puerto USB diferente o reinicia.
- Instala las herramientas de Bluetooth si no están presentes:  
  ```
  sudo apt update
  sudo apt install bluez bluetooth bluez-tools
  ```
- Desbloquea Bluetooth si es necesario:  
  ```
  rfkill unblock bluetooth
  ```
- Reinicia el servicio de Bluetooth:  
  ```
  sudo systemctl restart bluetooth
  ```

### Pasos para Emparejar Usando bluetoothctl (Recomendado para CLI)
La herramienta `bluetoothctl` es la forma estándar de gestionar Bluetooth en Linux/Ubuntu. Los teclados Logitech (como MX Keys, K380 o similares) a menudo requieren ingresar un PIN de emparejamiento en el teclado físico.

1. **Abre la consola de Bluetooth**:  
   ```
   bluetoothctl
   ```
   Esto entra en un shell interactivo (el prompt cambia a `[bluetooth]#`).

2. **Habilita el adaptador**:  
   ```
   power on
   ```
   (Si dice "No default controller available", ejecuta `list` para ver tu adaptador y `select <MAC_del_adaptador>` si hay múltiples).

3. **Configura el agente de emparejamiento**:  
   ```
   agent on
   default-agent
   ```
   Esto habilita el manejo de PIN y hace que tu sesión sea la predeterminada para el emparejamiento.

4. **Inicia el escaneo de dispositivos**:  
   ```
   scan on
   ```
   Mantén esto ejecutándose. Tu teclado Logitech debería aparecer después de ~10-20 segundos (ej., como "Logitech K380" o similar, con una dirección MAC como `XX:XX:XX:XX:XX:XX`).

5. **Pon tu teclado Logitech en modo de emparejamiento**:  
   - Enciéndelo (si tiene un interruptor de encendido).  
   - Presiona y mantén presionado el botón de emparejamiento Bluetooth (generalmente en el lateral o la parte superior—consulta tu modelo; para modelos multi-dispositivo como MX Keys, mantén presionado el botón del canal 1/2/3 durante 3-5 segundos hasta que el LED parpadee rápidamente).  
   - Si es un modelo de un solo dispositivo, mantén presionado el botón de emparejamiento principal.

6. **Empareja el dispositivo**:  
   Una vez que aparezca en el escaneo (presiona Enter para actualizar), ejecuta:  
   ```
   pair <DIRECCIÓN_MAC>
   ```
   - Ejemplo: `pair 12:34:56:78:9A:BC`  
   - Ubuntu solicitará un PIN (a menudo 0000 o 1234 para Logitech—prueba los valores predeterminados primero).  
   - **Paso clave para Logitech**: Escribe el PIN directamente en el *teclado físico* y presiona Enter. (Si no aparecen notificaciones gráficas, esto es crucial—algunos usuarios reportan que necesitan habilitar las notificaciones del sistema mediante `gnome-control-center` > Notificaciones, pero la CLI a menudo evita esto).

7. **Confía y conecta**:  
   ```
   trust <DIRECCIÓN_MAC>
   connect <DIRECCIÓN_MAC>
   ```
   - Esto se conecta automáticamente en usos futuros.

8. **Sale de la consola**:  
   ```
   exit
   ```

### Solución de Problemas
- **El dispositivo no se detecta al escanear**: Asegúrate de que el teclado esté en modo de emparejamiento (LED parpadeando). Ejecuta `scan off` y luego `scan on` nuevamente. Espera hasta 30 segundos.
- **El emparejamiento falla (ej., "AuthenticationCanceled")**: Elimina el dispositivo primero (`remove <MAC>`), luego vuelve a intentar. Para modelos Logitech problemáticos, intenta mantener presionado el botón de emparejamiento por más tiempo o alterna entre canales.
- **No aparece la solicitud de PIN**: Algunos teclados se emparejan sin uno—procede a conectar. Si se queda atascado, revisa los registros: `sudo journalctl -u bluetooth -f` durante el emparejamiento.
- **Problemas con el adaptador**: Si usas un dongle USB Bluetooth 5.3, confirma la compatibilidad del kernel (Ubuntu 22.04+ maneja bien BT 5.3). Actualiza el kernel si usas una versión anterior de Ubuntu: `sudo apt install linux-generic-hwe-22.04`.
- **Alternativa gráfica**: Abre Configuración > Bluetooth, actívalo y empareja desde allí—pero la CLI es más confiable para las peculiaridades de Logitech.
- Prueba: Después del emparejamiento, escribe en una terminal. Si funciona, añádelo para que se conecte automáticamente al inicio mediante `bluetoothctl` o crontab.

Si tu modelo específico de Logitech (ej., MX Keys Mini) tiene problemas únicos, proporciona el modelo exacto para pasos personalizados.

### Referencias
- [Pairing LOGITECH K380 in Ubuntu 20.04](https://unix.stackexchange.com/questions/590221/pairing-logitech-k380-in-ubuntu-20-04)  
- [Logitech MX Keys won't pair with Bluetooth](https://askubuntu.com/questions/1270419/20-04-logitech-mx-keys-wont-pair-with-bluetooth)  
- [Pair Logitech MX Keys with Xubuntu via Bluetooth](https://zroupas.github.io/linux/2021/08/25/pair_mxkeys_xubuntu_bt.html)  
- [Ubuntu 20.04 cannot pair Bluetooth Keyboard](https://askubuntu.com/questions/1398096/ubuntu-20-04-cannot-pair-bluetooth-keyboard)