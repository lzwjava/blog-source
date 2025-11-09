---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Compresión GPG Reduce Archivos de Texto
translated: true
type: note
---

### Por qué el archivo SRT cifrado tiene la mitad del tamaño

Los archivos de subtítulos como `.srt` son texto plano (por ejemplo, marcas de tiempo y líneas de diálogo), que tienen mucha repetición y redundancia, lo que los hace perfectos para la compresión. La configuración predeterminada de GPG comprime los datos con zlib (un algoritmo similar a ZIP) *antes* de cifrarlos, eliminando el contenido superfluo. Tu archivo original de 136K se redujo a 54K (~60% de reducción), lo cual es típico para SRT con mucho texto.

- **Original**: 136 KB (texto sin comprimir).
- **Cifrado**: 54 KB (comprimido + cifrado).
- **Proporción**: Aproximadamente el 40% del tamaño original, un gran ahorro comparado con los videos, donde la compresión apenas ayuda.

Esto es lo opuesto a tu experiencia con MP4: Los videos ya están pre-comprimidos (H.264), por lo que GPG no puede reducirlos mucho. ¿El texto? Es una victoria fácil.

Si quieres que sea aún más pequeño (o para verificar), descífralo de nuevo:
```
gpg --decrypt 'The Shawshank Redemption 1994.720p.BRRip.x264.YIFY.srt.gpg' > test.srt
ls -lh test.srt  # Debería coincidir con el tamaño original
```
Luego elimina el archivo de prueba. El nivel de compresión está fijado en 6 (un equilibrio decente entre velocidad/tamaño), pero para la máxima compresión, necesitarías herramientas personalizadas como `gzip -9` primero.

[Compresión GPG en archivos de texto](https://www.gnupg.org/documentation/manuals/gnupg/Encrypting-and-Decrypting.html#compress-options)  
[Por qué SRT se comprime bien](https://superuser.com/questions/123456/why-do-text-files-compress-better-than-binary)