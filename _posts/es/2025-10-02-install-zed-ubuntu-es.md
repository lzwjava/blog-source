---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: Instalar Zed en Ubuntu 24.04
translated: true
type: note
---

Para Ubuntu 24.04 LTS, el método de instalación más directo y oficial para Zed (el editor de código de alto rendimiento) es mediante el script de shell que proporcionan, que funciona de forma nativa en la mayoría de las distribuciones de Linux, incluidas las basadas en Debian como Ubuntu. Maneja las dependencias automáticamente y garantiza que obtengas la última versión estable.

### Instalación Recomendada: Script Oficial
Ejecuta esto en tu terminal:
```
curl -f https://zed.dev/install.sh | sh
```
- Esto instala Zed en `~/.local/bin/zed` (agrégalo a tu PATH si es necesario: `export PATH="$HOME/.local/bin:$PATH"` en `~/.bashrc` o similar).
- Requisitos previos: Tu sistema (glibc 2.39 en kernel 6.14) cumple con los requisitos (x86_64 glibc >= 2.31).
- Después de la instalación, inícialo con `zed` o desde el menú de aplicaciones de GNOME.
- Para el canal de vista previa (compilaciones nocturnas): `curl -f https://zed.dev/install.sh | ZED_CHANNEL=preview sh`.

Si prefieres un paquete universal y aislado (sin preocuparte por dependencias nativas), usa la opción de Flathub de tu lista (`dev.zed.Zed`) a través de Flatpak:
1. Instala Flatpak si no está presente: `sudo apt update && sudo apt install flatpak`.
2. Añade el repositorio Flathub: `flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo`.
3. Instala: `flatpak install flathub dev.zed.Zed`.
4. Ejecuta: `flatpak run dev.zed.Zed`.

El script generalmente es más rápido y está más integrado para un escritorio como GNOME, pero Flatpak es excelente si quieres aislamiento o ya lo usas para otras aplicaciones. Evita las otras opciones en tu lista, ya que son para distribuciones que no son Debian y no funcionarán directamente en Ubuntu sin configuración adicional.

### Referencias
- [Documentación de Instalación de Zed en Linux](https://zed.dev/docs/linux)
- [Anuncio de Zed en Linux](https://zed.dev/linux)
- [Paquetes de Zed en Repology](https://repology.org/project/zed-editor/versions)