---
audio: false
generated: true
image: false
lang: es
layout: post
model: openai/gpt-5
title: Guía de Instalación del Navegador en Ubuntu 24.04
translated: true
type: note
---

Además de **Firefox** y **Chromium**, hay bastantes buenos navegadores que puedes instalar en **Ubuntu 24.04** — dependiendo de tus prioridades (velocidad, privacidad, compatibilidad, uso de recursos, etc.). Aquí tienes una lista categorizada con notas:

---

### 🧠 Navegadores Principales

**1. Google Chrome**

* Basado en Chromium pero incluye la sincronización de Google, códecs y funciones propietarias.
* Gran compatibilidad con aplicaciones web (como Google Docs, Meet, etc.).
* Instalar mediante `.deb` desde el sitio oficial de Google.

**2. Microsoft Edge (versión para Linux)**

* Basado en Chromium, interfaz de usuario pulida, se integra con los servicios de Microsoft.
* A menudo más rápido que Chrome en el manejo de la memoria.
* Paquete `.deb` desde el sitio de Microsoft.

---

### 🔒 Navegadores Enfocados en la Privacidad

**3. Brave**

* Construido sobre Chromium pero con bloqueador de anuncios integrado, bloqueo de rastreadores y modo ventana Tor.
* Mantiene la compatibilidad con extensiones de Chrome.
* Instalar:

  ```bash
  sudo apt install apt-transport-https curl
  sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg
  echo "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg] https://brave-browser-apt-release.s3.brave.com/ stable main" | sudo tee /etc/apt/sources.list.d/brave-browser-release.list
  sudo apt update
  sudo apt install brave-browser
  ```

**4. Vivaldi**

* También basado en Chromium, pero muy personalizable (mosaico de pestañas, atajos de teclado, herramientas de la barra lateral).
* Tiene más funciones que Chrome o Edge.
* Descargar `.deb` desde [vivaldi.com](https://vivaldi.com).

**5. Tor Browser**

* Enfocado en el anonimato y la evasión de la censura.
* Basado en Firefox ESR, dirige el tráfico a través de la red Tor.
* Instalar mediante:

  ```bash
  sudo apt install torbrowser-launcher
  ```

---

### 🪶 Navegadores Ligeros

**6. Falkon (Qt WebEngine)**

* Ligero, interfaz mínima, se integra bien con sistemas KDE/Qt.
* Instalar:

  ```bash
  sudo apt install falkon
  ```

**7. Midori**

* Proyecto antiguo revitalizado por su simplicidad y bajo uso de recursos.
* Aceptable para navegación simple, no ideal para aplicaciones web pesadas.
* Instalar:

  ```bash
  sudo apt install midori
  ```

**8. Epiphany (GNOME Web)**

* Navegador por defecto de GNOME, basado en WebKit (no Chromium).
* Simple, ligero, se adapta perfectamente al entorno GNOME.
* Instalar:

  ```bash
  sudo apt install epiphany-browser
  ```

---

### 🧪 Navegadores para Desarrolladores / de Nicho

**9. Ungoogled Chromium**

* Chromium despojado de todo rastreo de Google y dependencias de API.
* Configuración manual pero buena para una privacidad estricta.
* Suele encontrarse mediante `.deb` de la comunidad o Flatpak.

**10. Floorp**

* Un fork moderno de Firefox con privacidad y personalización mejoradas.
* Creado por desarrolladores japoneses; se está volviendo bastante popular.
* Flatpak disponible en Flathub.

---

¿Te gustaría que te recomendara una combinación (por ejemplo, *uno centrado en la privacidad, uno ligero, uno con todas las funciones*) que se adapte a tu flujo de trabajo en esta configuración de Ubuntu?