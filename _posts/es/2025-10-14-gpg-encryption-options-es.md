---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Opciones de cifrado GPG explicadas
translated: true
type: note
---

### Explicación de las opciones de GPG

El comando `gpg` (GNU Privacy Guard) es una herramienta para cifrado, descifrado y gestión de claves. Las opciones que mencionaste se usan comúnmente juntas para cifrar archivos para un destinatario específico. Esto es lo que significa cada una:

- **`--homedir <directorio>`**: Especifica el directorio principal de GnuPG (por defecto es `~/.gnupg`). Aquí es donde GPG almacena los llaveros, archivos de configuración y otros datos. Anula la variable de entorno `GNUPGHOME` y es útil para aislar las operaciones de GPG en una ubicación personalizada (por ejemplo, para múltiples perfiles o seguridad). Debe proporcionarse en la línea de comandos.

- **`-e` (o `--encrypt`)**: Cifra los datos de entrada usando criptografía de clave pública. Este es el modo principal para el cifrado asimétrico, donde los datos se cifran con la clave pública del destinatario. Puede combinarse con otras opciones como la firma.

- **`-r <id-usuario>` (o `--recipient <id-usuario>`)**: Especifica el/los destinatario(s) para el cifrado. El `<id-usuario>` puede ser un ID de clave, un correo electrónico o un nombre asociado con la clave pública. GPG usará la clave pública correspondiente para cifrar los datos. Se pueden listar múltiples destinatarios para el cifrado grupal.

#### Ejemplo de uso
Un comando común que combina estas opciones podría verse así:
```
gpg --homedir /ruta/al/directorio/personalizado -e -r destinatario@ejemplo.com archivo_entrada.txt
```
Esto cifra `archivo_entrada.txt` para `destinatario@ejemplo.com` usando las claves de `/ruta/al/directorio/personalizado`, produciendo `archivo_entrada.txt.gpg`.

Para más detalles, ejecuta `gpg --help` o consulta la página del manual.

[ArchWiki: GnuPG](https://wiki.archlinux.org/title/GnuPG)  
[GPG Cheat Sheet](https://irtfweb.ifa.hawaii.edu/~lockhart/gpg/)  
[GPG Command in Linux](https://www.tutorialspoint.com/unix_commands/gpg.htm)