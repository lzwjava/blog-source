---
audio: false
generated: true
image: false
lang: es
layout: post
title: Guía de Actualización de Node.js para Ubuntu
translated: true
type: note
---

Actualizar Node.js en Ubuntu se puede realizar de varias maneras. Los métodos más confiables y recomendados son usar **`nvm` (Node Version Manager)** o el **repositorio NodeSource**. A continuación se presentan instrucciones paso a paso para ambos métodos.

---

## **Método 1: Usar NVM (Recomendado)**
NVM te permite instalar y gestionar múltiples versiones de Node.js fácilmente.

### 1. Instalar NVM
Abre una terminal y ejecuta:
```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
```
Luego, recarga tu shell:
```bash
source ~/.bashrc
```
o
```bash
source ~/.zshrc
```
(dependiendo de tu shell)

### 2. Instalar la Última Versión de Node.js
Lista las versiones disponibles:
```bash
nvm ls-remote
```
Instala la última versión LTS (recomendada para la mayoría de usuarios):
```bash
nvm install --lts
```
O instala una versión específica (ej., 20.x):
```bash
nvm install 20
```

### 3. Establecer la Versión Predeterminada
```bash
nvm alias default 20
```

### 4. Verificar
```bash
node -v
npm -v
```

---

## **Método 2: Usar el Repositorio NodeSource**
Este método instala Node.js a nivel del sistema.

### 1. Eliminar Node.js Antiguo (si está instalado via apt)
```bash
sudo apt remove --purge nodejs npm
sudo apt autoremove
```

### 2. Agregar el Repositorio NodeSource**
Para **Node.js 20.x** (LTS a partir de Agosto 2025):
```bash
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
```
Para **Node.js 22.x** (si está disponible):
```bash
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
```

### 3. Instalar Node.js
```bash
sudo apt install -y nodejs
```

### 4. Verificar
```bash
node -v
npm -v
```

---

## **Método 3: Usar el Repositorio Predeterminado de Ubuntu (No Recomendado)**
El repositorio predeterminado de Ubuntu a menudo contiene versiones desactualizadas de Node.js. Si aún así quieres usarlo:
```bash
sudo apt update
sudo apt install nodejs npm
```
Pero esto **no es recomendado** para desarrollo, ya que la versión suele ser antigua.

---

## **¿Qué Método Deberías Usar?**
- **Usa NVM** si quieres cambiar entre versiones de Node.js fácilmente o necesitas las últimas características.
- **Usa NodeSource** si quieres una instalación estable a nivel del sistema.