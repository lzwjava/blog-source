---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Corrección del Error de Configuración de libcurl
translated: true
type: note
---

Este error significa que el script `configure` está intentando encontrar **libcurl** (una librería para peticiones HTTP/HTTPS), pero no puede localizar `curl-config` — un binario auxiliar que indica dónde está instalada libcurl.

Aquí se explica cómo solucionarlo dependiendo de tu sistema:

---

### 🧩 Para Ubuntu / Debian

Ejecuta:

```bash
sudo apt update
sudo apt install libcurl4-openssl-dev
```

Luego intenta de nuevo:

```bash
./configure
```

---

### 🧩 Para Fedora / CentOS / RHEL

Ejecuta:

```bash
sudo dnf install libcurl-devel
```

---

### 🧩 Para Arch / Manjaro

Ejecuta:

```bash
sudo pacman -S curl
```

---

### 🔍 Para verificar la instalación

Después de la instalación, asegúrate de que `curl-config` esté disponible:

```bash
which curl-config
```

Si devuelve una ruta como `/usr/bin/curl-config`, estás listo.

Luego ejecuta de nuevo:

```bash
./configure
make
sudo make install
```

---

¿Te gustaría que explique qué hace realmente `curl-config` y por qué `configure` lo necesita?