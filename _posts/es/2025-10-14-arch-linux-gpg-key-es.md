---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Clave GPG de Verificación de ISO de Arch Linux
translated: true
type: note
---

Tienes esta clave GPG (la que pertenece a Pierre Schmitz, con huella digital `3E80CA1A8B89F69CBA57D98A76A5EF9054449A5C`) en tu llavero porque es la clave de firma oficial utilizada por los desarrolladores de Arch Linux para firmar criptográficamente sus imágenes ISO. Esto garantiza que la descarga sea auténtica y no haya sido manipulada.

Cuando estabas preparando una unidad USB de arranque para instalar Arch Linux en macOS (probablemente siguiendo la guía oficial del wiki de Arch), el proceso estándar implica dos pasos para la verificación:
1. Descargar la ISO y su archivo `.sig`.
2. Importar la clave GPG del desarrollador relevante (en este caso, la de Pierre Schmitz, ya que es uno de los firmantes principales de las ISOs recientes) para verificar la firma con un comando como `gpg --verify archlinux-AAAA.MM.DD-x86_64.iso.sig`.

Probablemente ejecutaste algo como `gpg --keyserver hkps://keys.openpgp.org --recv-keys 3E80CA1A8B89F69CBA57D98A76A5EF9054449A5C` para obtenerla e importarla, lo que la añadió permanentemente a tu llavero GPG local. Por eso aparece en `gpg --list-keys`.

Es inofensiva: las claves GPG son solo datos públicos para fines de verificación, y muchos usuarios de Arch terminan con algunas de estas después de verificar ISOs. Si ya no la necesitas y quieres eliminarla, ejecuta:
```
gpg --delete-key 3E80CA1A8B89F69CBA57D98A76A5EF9054449A5C
```
(Se te pedirá confirmación; solo elimina la clave pública, no las firmas que ya hayas verificado).

[Página de Descarga de ISO de Arch Linux](https://archlinux.org/download/)  
[Arch Wiki: Instalar Arch Linux en una Mac](https://wiki.archlinux.org/title/Install_Arch_Linux_on_Mac)  
[Claves GPG de Pierre Schmitz](https://pierre-schmitz.com/gpg-keys/)