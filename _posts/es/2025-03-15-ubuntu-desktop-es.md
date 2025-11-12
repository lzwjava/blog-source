---
audio: false
generated: true
lang: es
layout: post
title: Instalación de un Entorno de Escritorio en Ubuntu
translated: true
type: note
---

Parece que tu sistema Ubuntu podría no tener una interfaz gráfica de usuario (GUI) instalada, lo que explicaría por qué no ves un explorador de archivos (a menudo llamado gestor de archivos en Linux) o ningún tipo de "finder". Esto podría suceder si instalaste una versión servidor de Ubuntu, elegiste una instalación mínima, o si hay un problema que impide que la GUI se cargue. No te preocupes, podemos solucionarlo instalando una GUI como GNOME (el entorno de escritorio predeterminado de Ubuntu) u otra opción si lo prefieres. Aquí te explicamos cómo hacerlo paso a paso.

### Paso 1: Actualiza tu sistema
Antes de instalar nada, es una buena idea asegurarte de que tus listas de paquetes estén actualizadas y tu sistema esté completamente actualizado. Abre una terminal y ejecuta estos comandos:

```bash
sudo apt update
```
Esto actualiza la lista de paquetes disponibles.

```bash
sudo apt upgrade
```
Esto actualiza todos los paquetes instalados actualmente a sus últimas versiones. Si se te solicita, presiona `Y` para confirmar.

### Paso 2: Instala el entorno de escritorio GNOME
Ya que mencionaste que querías una GUI "como GNOME u otro", comencemos con GNOME, ya que es el predeterminado para Ubuntu Desktop e incluye un gestor de archivos llamado Nautilus. Para instalarlo, ejecuta:

```bash
sudo apt install ubuntu-desktop
```
Este comando instala el entorno de escritorio GNOME completo, junto con aplicaciones estándar como un gestor de archivos, un navegador web y más. La instalación puede tomar unos minutos, dependiendo de tu velocidad de internet y del sistema. Si te pide que elijas un gestor de pantalla (por ejemplo, GDM o LightDM), generalmente puedes mantener la opción predeterminada (GDM para GNOME) presionando Enter.

### Paso 3: Reinicia tu sistema
Después de que termine la instalación, reinicia tu sistema para iniciar la GUI:

```bash
sudo reboot
```
Una vez que tu sistema se reinicie, deberías ver una pantalla de inicio de sesión gráfica. Inicia sesión y tendrás un escritorio completamente funcional con un gestor de archivos (Nautilus) que te permitirá navegar por los archivos.

### ¿Y si no funciona?
Si aún no ves una GUI después de reiniciar, es posible que haya un problema con el gestor de pantalla o los controladores gráficos. Puedes intentar iniciar el gestor de pantalla manualmente para probar:

```bash
sudo systemctl start gdm
```
Si eso muestra una pantalla de inicio de sesión, ¡genial! Para asegurarte de que se inicie automáticamente en cada arranque, ejecuta:

```bash
sudo systemctl enable gdm
```
Si la GUI aún no aparece, verifica si hay errores revisando los registros del sistema con:

```bash
journalctl -b
```
Busca mensajes relacionados con `gdm`, `Xorg` o controladores gráficos, y no dudes en buscar más ayuda con esos detalles.

### Opciones alternativas de GUI
Si prefieres una GUI diferente en lugar de GNOME, aquí tienes algunas alternativas populares:
- **KDE Plasma** (elegante y personalizable):
  ```bash
  sudo apt install kubuntu-desktop
  ```
- **XFCE** (ligero y rápido):
  ```bash
  sudo apt install xubuntu-desktop
  ```
- **LXDE** (muy ligero, bueno para hardware antiguo):
  ```bash
  sudo apt install lubuntu-desktop
  ```
Después de instalar cualquiera de estos, reinicia con `sudo reboot` y obtendrás un entorno de escritorio con un gestor de archivos (por ejemplo, Dolphin para KDE, Thunar para XFCE).

### ¿Por qué no tenía una GUI?
Es posible que no hayas visto una GUI porque:
- Instalaste Ubuntu Server, que no incluye un escritorio por defecto.
- Elegiste una instalación mínima durante la configuración, omitiendo la GUI.
- Existe una pequeña posibilidad de que la GUI esté instalada pero no se inicie debido a un problema de configuración o de hardware.

Instalar `ubuntu-desktop` como se describió debería resolver esto si se trata de una GUI faltante. Si sospechas que hay un problema con una GUI existente, ¡avísame y podemos solucionarlo!

### Resumen
Para instalar GNOME y obtener un explorador de archivos en tu sistema Ubuntu:
1. `sudo apt update`
2. `sudo apt upgrade`
3. `sudo apt install ubuntu-desktop`
4. `sudo reboot`

Pronto tendrás una interfaz gráfica con un gestor de archivos listo para usar. ¡Disfruta de tu escritorio Ubuntu!