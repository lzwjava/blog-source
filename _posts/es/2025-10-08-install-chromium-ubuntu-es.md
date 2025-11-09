---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Instalación de Chromium en Ubuntu 24.04
translated: true
type: note
---

Para instalar **Chromium** en **Ubuntu 24.04**, tienes algunas buenas opciones, dependiendo de si quieres la **versión oficial Snap**, la versión **APT (paquete Debian)** o una **descarga manual**. Aquí tienes una guía clara para cada una:

---

### 🧩 Opción 1: Instalar via Snap (Método Oficial de Ubuntu)

Este es el método **predeterminado** y más estable.

```bash
sudo snap install chromium
```

Luego, ejecútalo con:

```bash
chromium
```

✅ *Ventajas:*

* Mantenido oficialmente por Canonical.
* Se actualiza automáticamente.

⚠️ *Desventajas:*

* El inicio puede ser más lento.
* La sandboxing de Snap puede causar problemas con proxies del sistema o acceso a archivos.

---

### ⚙️ Opción 2: Instalar via APT (Paquete Debian, Sin Snap)

Si **no te gusta Snap**, puedes instalar Chromium desde un **repositorio de terceros**, como la compilación oficial de Debian proporcionada por **ungoogled-chromium** u **OBS**.

1.  Añade el repositorio OBS:

    ```bash
    sudo apt install wget gnupg
    wget -qO - https://download.opensuse.org/repositories/home:/ungoogled_chromium/Ubuntu_24.04/Release.key | sudo gpg --dearmor -o /usr/share/keyrings/ungoogled-chromium.gpg
    ```

2.  Añade el repositorio:

    ```bash
    echo "deb [signed-by=/usr/share/keyrings/ungoogled-chromium.gpg] https://download.opensuse.org/repositories/home:/ungoogled_chromium/Ubuntu_24.04/ /" | sudo tee /etc/apt/sources.list.d/ungoogled-chromium.list
    ```

3.  Instala Chromium:

    ```bash
    sudo apt update
    sudo apt install ungoogled-chromium
    ```

Luego, ejecútalo con:

```bash
ungoogled-chromium
```

✅ *Ventajas:*

* Sin dependencia de Snap.
* Versión disponible reforzada para la privacidad.

⚠️ *Desventajas:*

* Las actualizaciones son más lentas que con Snap.
* Algunas funciones (como Google Sync) deshabilitadas.

---

### 🧰 Opción 3: Instalar desde la Compilación Oficial de Chromium (Manual)

Si quieres la **última versión de desarrollo**:

```bash
sudo apt install chromium-browser
```

Si se redirige a Snap y quieres evitarlo:

```bash
sudo apt purge chromium-browser
sudo apt install chromium
```

O, descarga un archivo `.deb` manualmente:

```bash
wget https://commondatastorage.googleapis.com/chromium-browser-snapshots/Linux_x64/LAST_CHANGE -O /tmp/LAST_CHANGE
LATEST=$(cat /tmp/LAST_CHANGE)
wget "https://commondatastorage.googleapis.com/chromium-browser-snapshots/Linux_x64/${LATEST}/chrome-linux.zip"
unzip chrome-linux.zip
./chrome-linux/chrome
```

---

### 🌍 Nota sobre la Configuración del Proxy

Dado que tu sistema usa:

```
HTTP_PROXY=http://127.0.0.1:7890
HTTPS_PROXY=http://127.0.0.1:7890
```

asegúrate de que Snap y APT respeten tu proxy exportando estas variables en `/etc/environment` o en tu perfil de shell:

```bash
export http_proxy=http://127.0.0.1:7890
export https_proxy=http://127.0.0.1:7890
```

---

¿Te gustaría que te muestre cómo hacer que Chromium use automáticamente ese proxy (para que siempre se conecte a través de él)?