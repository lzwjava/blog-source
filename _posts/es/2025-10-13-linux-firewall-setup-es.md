---
audio: false
generated: true
image: false
lang: es
layout: post
model: openai/gpt-5
title: Guía de Configuración de Firewall en Linux
translated: true
type: note
---

Buena pregunta — configurar un firewall en Linux (como **Red Hat** o **Ubuntu**) implica principalmente usar **`firewalld`** o **`ufw`**, dependiendo de tu sistema. A continuación, tienes una guía clara para ambas familias, para que puedas elegir la correcta.

---

### 🔹 En **Red Hat / CentOS / Fedora** (firewalld)

#### 1. Verifica si `firewalld` está instalado y en ejecución

```bash
sudo systemctl status firewalld
```

Si no está en ejecución:

```bash
sudo systemctl enable firewalld
sudo systemctl start firewalld
```

#### 2. Uso básico

Verifica las zonas activas (las zonas agrupan interfaces y reglas):

```bash
sudo firewall-cmd --get-active-zones
```

Lista todas las reglas para la zona actual:

```bash
sudo firewall-cmd --list-all
```

#### 3. Permitir o bloquear puertos/servicios

Permitir un puerto (ej. SSH en el puerto 22):

```bash
sudo firewall-cmd --permanent --add-port=22/tcp
```

Permitir un servicio conocido (ej. HTTP):

```bash
sudo firewall-cmd --permanent --add-service=http
```

Bloquear/eliminar uno:

```bash
sudo firewall-cmd --permanent --remove-service=http
```

Recarga para aplicar:

```bash
sudo firewall-cmd --reload
```

#### 4. Verificar reglas

```bash
sudo firewall-cmd --list-all
```

---

### 🔹 En **Ubuntu / Debian** (ufw)

Ubuntu incluye **UFW** (Uncomplicated Firewall), más simple de gestionar.

#### 1. Activar UFW

```bash
sudo ufw enable
```

#### 2. Permitir/denegar puertos o servicios

Permitir SSH:

```bash
sudo ufw allow ssh
```

Permitir HTTP (puerto 80):

```bash
sudo ufw allow 80/tcp
```

Permitir un rango de puertos específico:

```bash
sudo ufw allow 1000:2000/tcp
```

Denegar un servicio:

```bash
sudo ufw deny 23/tcp
```

#### 3. Verificar estado

```bash
sudo ufw status verbose
```

#### 4. Restablecer reglas si es necesario

```bash
sudo ufw reset
```

---

### 🔹 Para ambos sistemas

Para **bloquear todo el tráfico entrante excepto unos pocos**, puedes:

1. Denegar todo el tráfico entrante por defecto

   ```bash
   sudo ufw default deny incoming
   sudo ufw default allow outgoing
   ```

   *(para `firewalld`, usa zonas o zonas de descarte para un comportamiento similar)*

2. Luego permite puertos selectivamente (ej., 22, 80, 443).

---

### 🔹 Consejo de seguridad

Siempre **permite SSH primero** antes de activar o cambiar reglas del firewall de forma remota — de lo contrario, te quedarás fuera del sistema.

---

¿Te gustaría que muestre una **configuración mínima de firewall de ejemplo** (ej. para un servidor web típico que permita solo SSH + HTTP + HTTPS)?