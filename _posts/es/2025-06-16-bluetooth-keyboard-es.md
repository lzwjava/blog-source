---
audio: false
generated: true
lang: es
layout: post
title: Solucionar Problemas de Conexión del Teclado Bluetooth
translated: true
type: note
---

Basado en la salida de `bluetoothctl` que muestra `[DEL] Device` al intentar conectar, aquí tienes una solución precisa:

### Solución Inmediata para el Problema de Eliminación de Conexión
1. **Eliminar los registros existentes del dispositivo** (crítico para configuraciones obsoletas):
   ```bash
   bluetoothctl
   remove F4:73:35:78:28:4E  # Eliminar teclado
   remove 24:27:30:24:C8:31   # Eliminar dispositivo potencialmente interferente
   exit
   ```

2. **Reiniciar la pila de Bluetooth**:
   ```bash
   sudo systemctl stop bluetooth
   sudo rm -rf /var/lib/bluetooth/*
   sudo systemctl start bluetooth
   ```

3. **Reparar usando la secuencia correcta**:
   ```bash
   bluetoothctl
   power on
   discoverable on
   pairable on
   agent on  # Habilitar el agente de contraseña
   scan on
   ```
   - **Poner el K380 en modo de emparejamiento** (LED parpadeando rápidamente)
   - Cuando el teclado aparezca:
     ```bash
     pair F4:73:35:78:28:4E
     ```
   - **Inmediatamente escribe el código de acceso de 6 dígitos** que se muestra en pantalla (ej., `123456`) **en el teclado** y presiona Enter

4. **Conectar solo después de un emparejamiento exitoso**:
   ```bash
   connect F4:73:35:78:28:4E
   trust F4:73:35:78:28:4E
   scan off
   quit
   ```

### Por Qué Ocurre Esto
- El `[DEL] Device` ocurre porque:
  - La pila de Bluetooth detecta un fallo de conexión y purga el registro del dispositivo
  - **Falta el paso de emparejamiento** antes del intento de conexión
  - Posible interferencia de RF de otros dispositivos (como el dispositivo `midea`)

### Comprobaciones Adicionales Críticas
1. **Verificar la conexión de la antena**:
   - Asegúrate de que las antenas Bluetooth estén enroscadas en el panel trasero de E/S de tu placa base MSI

2. **Comprobar controladores del kernel**:
   ```bash
   dmesg | grep -i bluetooth
   ```
   Busca errores como `hci0: command timeout` o `Firmware failed to start`

3. **Actualizar firmware** (si aparecen errores de timeout):
   ```bash
   sudo apt install linux-firmware
   ```

4. **Probar con un entorno mínimo**:
   ```bash
   sudo rfkill unblock all
   sudo systemctl stop NetworkManager  # Detención temporal
   sudo systemctl restart bluetooth
   ```

### Si Sigue Fallando
1. **Método de emparejamiento alternativo** (evitar el agente):
   ```bash
   echo -e 'remove F4:73:35:78:28:4E\npair F4:73:35:78:28:4E\nconnect F4:73:35:78:28:4E\ntrust F4:73:35:78:28:4E' | bluetoothctl
   ```

2. **Comprobar la batería del teclado** (crítico para Bluetooth):
   - Reemplaza la batería si el voltaje es bajo (el K380 usa CR2032 x 2)

3. **Prueba con adaptador Bluetooth USB**:
   - Si el Bluetooth interno es problemático, prueba con un adaptador USB CSR4.0 de $10

**Indicadores de éxito esperados**:
- Mensaje de `Pairing successful`
- `Connection successful` en bluetoothctl
- `dmesg` mostrando `HIDP: Bluetooth HID device driver`

Después del emparejamiento, tu K380 debería sobrevivir a los reinicios. Si las desconexiones se repiten, revisa `journalctl -u bluetooth -f` para ver errores en tiempo real.