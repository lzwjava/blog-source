---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Instalación de WezTerm en Ubuntu
translated: true
type: note
---

El error "Unable to locate package wezterm" ocurre porque WezTerm no está disponible en los repositorios predeterminados de Ubuntu. Primero necesitas agregar el repositorio oficial de terceros. Aquí está la solución paso a paso usando el método nativo APT (recomendado para una integración perfecta):

1.  Agrega la clave GPG del repositorio:
    ```
    curl -fsSL https://apt.fury.io/wez/gpg.key | sudo gpg --yes --dearmor -o /usr/share/keyrings/wezterm-fury.gpg
    ```

2.  Agrega el repositorio a tus fuentes:
    ```
    echo 'deb [signed-by=/usr/share/keyrings/wezterm-fury.gpg] https://apt.fury.io/wez/ * *' | sudo tee /etc/apt/sources.list.d/wezterm.list
    ```

3.  Establece los permisos correctos en el archivo de clave:
    ```
    sudo chmod 644 /usr/share/keyrings/wezterm-fury.gpg
    ```

4.  Actualiza tu lista de paquetes:
    ```
    sudo apt update
    ```

5.  Ahora instala WezTerm:
    ```
    sudo apt install wezterm
    ```

Una vez instalado, puedes ejecutarlo con `wezterm` desde la terminal. Si prefieres la versión nightly (la más reciente) en su lugar, usa `sudo apt install wezterm-nightly` en el paso 5, pero ten en cuenta que no puede coexistir con la versión estable.

### Alternativa: Flatpak (No Se Necesita Repositorio)
Si prefieres una instalación en sandbox sin modificar las fuentes de APT:
1.  Instala Flatpak si no está presente: `sudo apt install flatpak`.
2.  Agrega Flathub: `flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo`.
3.  Instala: `flatpak install flathub org.wezfurlong.wezterm`.
4.  Ejecuta: `flatpak run org.wezfurlong.wezterm` (o agrega un alias: `alias wezterm='flatpak run org.wezfurlong.wezterm'`).

Flatpak está aislado, por lo que podría limitar algunas funciones avanzadas, pero es más simple para probar.

[Guía de Instalación de WezTerm para Linux](https://wezterm.org/install/linux.html)