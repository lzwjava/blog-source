---
audio: false
generated: true
image: false
lang: es
layout: post
model: anthropic/claude-sonnet-4
title: Guía para Instalar Docker en Ubuntu
translated: true
type: note
---

Según la salida de tu sistema Ubuntu, tienes varias opciones para instalar Docker. Aquí está el enfoque recomendado:

## Opción 1: Instalar Docker Engine (Recomendado)

La forma más común y recomendada es instalar Docker Engine desde el repositorio oficial de Docker:

```bash
# Actualizar el índice de paquetes
sudo apt update

# Instalar los requisitos previos
sudo apt install apt-transport-https ca-certificates curl software-properties-common

# Añadir la clave GPG oficial de Docker
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# Añadir el repositorio de Docker
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Actualizar el índice de paquetes nuevamente
sudo apt update

# Instalar Docker Engine
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

## Opción 2: Instalación Rápida via APT (Más Simple)

Desde las opciones mostradas en tu terminal, puedes usar:

```bash
sudo apt install docker.io
```

## Configuración Posterior a la Instalación

Después de la instalación, querrás:

1. **Iniciar y habilitar el servicio de Docker:**
```bash
sudo systemctl start docker
sudo systemctl enable docker
```

2. **Añadir tu usuario al grupo docker** (para ejecutar Docker sin sudo):
```bash
sudo usermod -aG docker $USER
```

Luego cierra sesión y vuelve a iniciarla, o ejecuta:
```bash
newgrp docker
```

3. **Verificar la instalación:**
```bash
docker --version
docker run hello-world
```

## ¿Qué Opción Elegir?

- **Opción 1** te da la última versión de Docker directamente de Docker Inc.
- **Opción 2** es más simple pero puede tener una versión ligeramente más antigua de los repositorios de Ubuntu

Para la mayoría de los usuarios, la Opción 2 (`sudo apt install docker.io`) es perfectamente adecuada y mucho más simple. La diferencia de versión suele ser mínima para un uso regular.

¿Te gustaría que explicara alguno de estos pasos con más detalle?