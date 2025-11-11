---
audio: false
generated: true
lang: es
layout: post
title: Verificar Velocidad de Enlace Ethernet en Ubuntu
translated: true
type: note
---

En Ubuntu, puedes verificar la velocidad del enlace Ethernet utilizando varias herramientas de línea de comandos. Estos son los métodos más comunes:

### **1. Usando `ethtool` (Recomendado)**
`ethtool` es la forma más confiable de verificar la velocidad actual del enlace de tu interfaz Ethernet.

#### Instalar `ethtool` (si no está instalado):
```bash
sudo apt install ethtool
```

#### Verificar la velocidad del enlace:
```bash
sudo ethtool <nombre_de_la_interfaz>
```
Reemplaza `<nombre_de_la_interfaz>` con tu interfaz Ethernet (ej. `eth0`, `enp3s0`, `ens33`).

#### Ejemplo:
```bash
sudo ethtool enp3s0
```
Busca los campos `Speed` y `Duplex` en la salida:
```
Settings for enp3s0:
    Supported ports: [ TP ]
    Supported link modes:   10baseT/Half 10baseT/Full 
                            100baseT/Half 100baseT/Full 
                            1000baseT/Full 
    Supported pause frame use: No
    Supports auto-negotiation: Yes
    Supported FEC modes: Not reported
    Advertised link modes:  10baseT/Half 10baseT/Full 
                            100baseT/Half 100baseT/Full 
                            1000baseT/Full 
    Advertised pause frame use: No
    Advertised auto-negotiation: Yes
    Advertised FEC modes: Not reported
    Speed: 1000Mb/s   # <--- Esta es tu velocidad de enlace actual
    Duplex: Full      # <--- Dúplex completo o medio dúplex
    Port: Twisted Pair
    PHYAD: 1
    Transceiver: internal
    Auto-negotiation: on
    MDI-X: on (auto)
    Supports Wake-on: pumbg
    Wake-on: d
    Current message level: 0x00000007 (7)
                           drv probe link
    Link detected: yes      # <--- Indica si el cable está conectado
```

---

### **2. Usando `ip` o `ifconfig` (Información Básica)**
Estos comandos muestran si la interfaz está activa pero no muestran directamente la velocidad del enlace.

#### Usando `ip`:
```bash
ip link show <nombre_de_la_interfaz>
```
Ejemplo:
```bash
ip link show enp3s0
```
(No muestra la velocidad, solo el estado del enlace.)

#### Usando `ifconfig` (obsoleto pero aún usado):
```bash
ifconfig <nombre_de_la_interfaz>
```
Ejemplo:
```bash
ifconfig enp3s0
```
(Muestra si la interfaz está activa pero no la velocidad.)

---

### **3. Usando `dmesg` (Verificar Registros del Controlador)**
A veces, el controlador Ethernet registra la velocidad negociada durante la inicialización.
```bash
dmesg | grep <nombre_de_la_interfaz>
```
Ejemplo:
```bash
dmesg | grep enp3s0
```
Busca líneas como:
```
[    5.123456] e1000e: enp3s0 NIC Link is Up 1000 Mbps Full Duplex
```

---

### **4. Usando `mii-tool` (Sistemas Antiguos)**
Para sistemas muy antiguos, `mii-tool` podría funcionar:
```bash
sudo apt install net-tools
sudo mii-tool -v <nombre_de_la_interfaz>
```
Ejemplo:
```bash
sudo mii-tool -v eth0
```
(No recomendado para Ethernet Gigabit moderno.)

---

### **Resumen**
- **Mejor método:** `sudo ethtool <interfaz>` (muestra velocidad, dúplex, auto-negociación).
- **Alternativa:** Verificar los registros de `dmesg` si `ethtool` no está disponible.
- **Estado básico:** `ip link show` o `ifconfig` (no muestra la velocidad).

¡Avísame si necesitas más aclaraciones! 🚀