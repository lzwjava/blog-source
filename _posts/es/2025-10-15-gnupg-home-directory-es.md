---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Contenido del Directorio Home de GnuPG Explicado
translated: true
type: note
---

Estos archivos y directorios forman parte de tu directorio personal de GnuPG (GPG) (`~/.gnupg/`), que almacena claves criptográficas y datos relacionados para cifrado, firma y autenticación. GPG es una herramienta para la comunicación segura y la protección de datos. Aquí tienes un desglose de cada uno basado en el comportamiento estándar de GnuPG 2.1+:

- **openpgp-revocs.d**: Un directorio que contiene certificados de revocación (archivos `.rev`) generados cuando creas pares de claves. Se utilizan para revocar (invalidar) tus claves si se ven comprometidas o ya no son necesarias, impidiendo su uso futuro.

- **private-keys-v1.d**: Un directorio que almacena tus claves privadas (secretas) en el formato moderno de claves introducido en GnuPG 2.1. Cada clave está en su propio archivo para una mejor seguridad y gestión. Mantén esto altamente protegido: es como tu caja fuerte digital.

- **pubring.kbx**: El archivo del llavero de claves públicas en el nuevo formato "keybox" (`.kbx`). Contiene las claves públicas importadas de otros, que usas para cifrar mensajes para ellos o verificar sus firmas.

- **pubring.kbx~**: Una copia de seguridad de `pubring.kbx`, creada automáticamente por GPG durante ediciones o actualizaciones. El sufijo tilde (`~`) es una convención común en Linux para las copias de seguridad.

- **trustdb.gpg**: El archivo de la base de datos de confianza, que rastrea los niveles de confianza que has asignado a las claves públicas (por ejemplo, "ultimate" para tus propias claves, o niveles para otros basados en firmas). Ayuda a GPG a decidir si una clave es confiable para su validación.

Si has generado o importado claves recientemente, esta configuración es normal. Siempre haz una copia de seguridad de todo tu directorio `~/.gnupg/` de forma segura y nunca compartas las claves privadas. Para más detalles, consulta la documentación oficial de GnuPG.

[Using the GNU Privacy Guard](https://www.gnupg.org/documentation/manuals/gnupg.pdf)  
[GnuPG Part 2 - Create and Manage Keys](https://www.hacksanity.com/kb/gnupg-create-manage-keys/)  
[How to Back Up and Restore Your GPG Keys on Linux](https://www.howtogeek.com/816878/how-to-back-up-and-restore-gpg-keys-on-linux/)  
[GPG(1) Manual](https://www.gnupg.org/(en)/documentation/manuals/gnupg24/gpg.1.html)