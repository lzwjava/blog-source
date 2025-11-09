---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Instalación de Chromium en macOS
translated: true
type: note
---

Sí, macOS puede instalar Chromium sin problemas como alternativa a Google Chrome. Chromium es la base de código abierto sobre la que se construye Chrome, por lo que es muy similar en funcionalidad pero carece de algunas funciones propietarias de Google como las actualizaciones automáticas y ciertos códecs.

### Cómo instalarlo
Existen algunos métodos sencillos:

1. **A través de Homebrew (el más fácil para la mayoría de usuarios)**:
   - Instala Homebrew si aún no lo tienes: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`.
   - Luego ejecuta: `brew install --cask chromium`.
   - Esto funciona tanto en Macs con Intel como con Apple Silicon (M1/M2/M3).

2. **Descarga directa**:
   - Ve al sitio oficial de Chromium y descarga la última compilación para Mac.
   - Descomprime y arrastra la aplicación a tu carpeta de Aplicaciones.

3. **Para desarrolladores o compilaciones personalizadas**:
   - Usa herramientas como Woolyss para versiones precompiladas, o compila desde el código fuente si es necesario (requiere Xcode).

Una vez instalado, puedes configurar Chromium como tu navegador predeterminado en Configuración del Sistema > Escritorio y Dock > Navegador web predeterminado.

[Descargar Chromium](https://www.chromium.org/getting-involved/download-chromium/)  
[Fórmula de Homebrew](https://formulae.brew.sh/cask/chromium)  
[Instalación en Apple Silicon](https://dev.to/pixelrena/installing-chromium-on-mac-apple-m2-pro-tutorial-4i4i)  
[Descarga en MacUpdate](https://chromium.macupdate.com/)  
[Últimas versiones](https://chromium.woolyss.com/download/en/)