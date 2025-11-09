---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Cifrado de archivos con GPG
translated: true
type: note
---

### Cifrar un archivo con tu clave GPG

Tu listado de claves GPG muestra una clave pública (pub) con la huella digital `982740390B5D33E90B6B6133892BC5A4789B71CD` asociada a tu correo electrónico `lzwjava@gmail.com`. Para cifrar un archivo usando esta clave (de modo que solo tú puedas descifrarlo con tu clave privada), sigue estos pasos en tu terminal:

1. **Navega al directorio** que contiene el archivo que quieres cifrar (por ejemplo, si tu archivo es `secret.txt`):
   ```
   cd ~/ruta/a/tu/archivo
   ```

2. **Cifra el archivo** usando la opción `--encrypt` y especifica el destinatario (tu correo o ID de clave). Esto crea un archivo cifrado `.gpg`.
   
   - Usando tu correo (más simple):
     ```
     gpg --encrypt --recipient lzwjava@gmail.com secret.txt
     ```
   
   - Usando el ID de clave (huella digital completa):
     ```
     gpg --encrypt --recipient 982740390B5D33E90B6B6133892BC5A4789B71CD secret.txt
     ```
   
   Esto genera `secret.txt.gpg`, que es la versión cifrada. El archivo original `secret.txt` permanece sin cambios.

3. **Verifica el cifrado** (opcional):
   ```
   gpg --list-packets secret.txt.gpg
   ```
   Esto muestra detalles sobre el paquete cifrado.

### Descifrar el archivo (para referencia futura)

Para descifrarlo nuevamente (solo es posible con tu clave privada y frase de contraseña):
```
gpg --decrypt secret.txt.gpg > secret.txt.decrypted
```
Ingresa tu frase de contraseña cuando se te solicite.

### Consejos
- **Cifrado simétrico** (si no necesitas una clave de destinatario, solo una frase de contraseña): Usa `gpg -c secret.txt` en su lugar.
- **Cifrar y firmar** (para probar que es de ti): Añade `--sign` al comando de cifrado, por ejemplo, `gpg --encrypt --sign --recipient lzwjava@gmail.com secret.txt`.
- Si encuentras errores (ej. clave no confiable), ejecuta `gpg --edit-key lzwjava@gmail.com` y usa `trust` para establecerla como ultimate.
- Siempre haz una copia de seguridad de tu directorio `~/.gnupg` para la seguridad de tus claves.

Para más detalles, consulta el manual de GPG: [Documentación de GPG](https://www.gnupg.org/documentation/manpage.html).