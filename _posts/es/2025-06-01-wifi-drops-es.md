---
audio: false
generated: true
lang: es
layout: post
title: Cómo solucionar las caídas de Wi-Fi en Ubuntu
translated: true
type: note
---

Las desconexiones de Wi-Fi en Ubuntu mientras las conexiones por cable permanecen estables pueden deberse a varios factores. Aquí tienes una guía paso a paso para diagnosticar y solucionar el problema:

---

### **1. Verificar problemas de controladores**
Es probable que tu placa base MSI B760M Mortar WiFi utilice una tarjeta **Intel Wi-Fi 6E AX211/AX210**. Aunque los controladores Intel generalmente tienen buen soporte en Linux, aún pueden surgir problemas.

#### **Pasos:**
- **Identificar el chipset de Wi-Fi:**  
  Ejecuta en la terminal:  
  ```bash
  lspci -knn | grep -iA3 net
  ```
  Busca el adaptador Wi-Fi (probablemente `Intel Corporation Device [8086:...]`).

- **Verificar si el controlador correcto está cargado:**  
  ```bash
  lsmod | grep iwlwifi
  ```
  Si no aparece nada, el controlador no está cargado.

- **Instalar/Actualizar controladores:**  
  Los controladores Intel Wi-Fi (`iwlwifi`) están incluidos en el kernel de Linux, pero puedes necesitar actualizaciones de firmware:
  ```bash
  sudo apt update && sudo apt install --reinstall linux-firmware
  ```

---

### **2. Desactivar el ahorro de energía para Wi-Fi**
A veces Linux apaga agresivamente la tarjeta Wi-Fi para ahorrar energía, lo que causa caídas.

#### **Pasos:**
- Desactivar temporalmente el ahorro de energía:  
  ```bash
  sudo sed -i 's/wifi.powersave = 3/wifi.powersave = 2/' /etc/NetworkManager/conf.d/default-wifi-powersave-on.conf
  ```
  O verificar manualmente con:
  ```bash
  iw dev wlan0 get power_save
  ```
  (Reemplaza `wlan0` con el nombre de tu interfaz de `ip a`).

- **Aplicar los cambios:**  
  ```bash
  sudo systemctl restart NetworkManager
  ```

---

### **3. Verificar interferencias o problemas del router**
- **Probar con otro dispositivo** (teléfono/portátil) para ver si el problema persiste.
- **Cambiar el canal de Wi-Fi** (usa `iwlist` para escanear canales congestionados):
  ```bash
  sudo iwlist wlan0 scan | grep Frequency
  ```
- Probar la **banda de 5GHz** (si está disponible) para menos interferencias.

---

### **4. Desactivar IPv6**
Algunos routers/ISPs tienen problemas de compatibilidad con IPv6.

#### **Pasos:**
- Edita `/etc/sysctl.conf` y añade:
  ```plaintext
  net.ipv6.conf.all.disable_ipv6=1
  net.ipv6.conf.default.disable_ipv6=1
  ```
- Aplicar:
  ```bash
  sudo sysctl -p
  ```

---

### **5. Actualizar Kernel y NetworkManager**
Los kernels más nuevos suelen corregir problemas de Wi-Fi.
```bash
sudo apt update && sudo apt upgrade
```
Si es necesario, instala un **kernel mainline** (ej. 6.5+):
```bash
sudo apt install linux-image-generic-hwe-22.04
```

---

### **6. Desactivar el cifrado por hardware (si aplica)**
Algunas tarjetas Intel Wi-Fi tienen problemas con el cifrado por hardware.  
Edita `/etc/modprobe.d/iwlwifi.conf` (crea el archivo si no existe):
```plaintext
options iwlwifi 11n_disable=1
```
Luego:
```bash
sudo modprobe -r iwlwifi && sudo modprobe iwlwifi
```

---

### **7. Verificar RFKill o Wi-Fi bloqueado**
```bash
rfkill list
```
Si el Wi-Fi está bloqueado (ej. `soft blocked: yes`), desbloquéalo:
```bash
sudo rfkill unblock wifi
```

---

### **8. Probar con un adaptador USB Wi-Fi**
Si el problema persiste, prueba con un **adaptador USB Wi-Fi compatible con Linux** (ej. TP-Link Archer T4U) para aislar si el problema es de la tarjeta Intel.

---

### **9. Revisar los registros en busca de errores**
```bash
journalctl -u NetworkManager --no-pager -n 50
```
Busca errores de `iwlwifi` o eventos de desconexión.

---

### **Notas finales**
- Si nada de lo anterior funciona, considera **hacer un dual-boot con Windows** para verificar si el problema es de hardware.
- Alternativamente, usa un **adaptador USB-a-Ethernet** si el Wi-Fi sigue siendo inestable.

¡Avísame si necesitas más ayuda para depurar!