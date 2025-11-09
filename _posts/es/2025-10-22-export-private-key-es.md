---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Exportación de una Clave Privada GPG
translated: true
type: note
---

### Exportar una clave privada GPG desde el servidor

Para exportar tu clave privada, necesitarás acceso al servidor por SSH o terminal. Las claves privadas GPG son sensibles—manéjalas de forma segura y elimina el archivo exportado después de la transferencia.

1. **Listar tus claves secretas** (para identificar la clave por correo o ID de clave):  
   ```
   gpg --list-secret-keys
   ```  
   Busca la entrada como `sec   rsa4096/ABC123DEF456 2023-01-01 [SC]`. Anota el correo o el ID de clave (ej., `user@example.com` o `ABC123DEF456`).

2. **Exportar la clave privada** (usa `--armor` para formato ASCII, más fácil de transferir):  
   ```
   gpg --export-secret-keys --armor user@example.com > private-key.asc
   ```  
   - Reemplaza `user@example.com` con tu correo real o ID de clave.  
   - Esto crea `private-key.asc` en tu directorio actual.  
   - Si tienes múltiples claves, especifica el ID de clave para mayor precisión: `gpg --export-secret-keys --armor ABC123DEF456 > private-key.asc`.  
   - **Nota de seguridad**: Esto exporta la clave *sin* su passphrase. Necesitarás ingresar la passphrase en la importación si se solicita.

3. **Transferir el archivo de forma segura** a tu laptop local:  
   - Usa `scp` (desde tu máquina local):  
     ```
     scp user@server-ip:/path/to/private-key.asc ./
     ```  
     Reemplaza `user@server-ip` con los detalles de tu servidor y `/path/to/` con la ruta real.  
   - Alternativas: `rsync` para archivos más grandes o SFTP para una opción con GUI. Evita el correo electrónico o canales no seguros.

4. **Limpiar en el servidor**:  
   ```
   rm private-key.asc
   ```  
   Verifica que se haya eliminado con `ls`.

### Importar la clave privada GPG en tu laptop local

Asumiendo que tienes GPG instalado (ej., via `apt install gnupg` en Linux, `brew install gnupg` en macOS, o Chocolatey en Windows).

1. **Importar la clave**:  
   ```
   gpg --import private-key.asc
   ```  
   - Verás una salida como "gpg: key ABC123DEF456: secret key imported".  
   - Si se solicita una passphrase durante la importación, ingresa la original.

2. **Verificar la importación**:  
   ```
   gpg --list-secret-keys
   ```  
   Tu clave debería aparecer ahora bajo "sec".

3. **Opcional: Establecer nivel de confianza** (si se usa para firmar/correo):  
   ```
   gpg --edit-key user@example.com
   ```  
   - En el prompt, escribe `trust`, selecciona "ultimate" (opción 5), luego `save` y `quit`.  
   - Esto marca la clave como totalmente confiable en tu máquina local.

### Consejos y Advertencias
- **Passphrase**: Usa siempre una passphrase fuerte. Si la olvidas, la clave se vuelve inutilizable.
- **Subclaves**: Si tu clave tiene subclaves (ej., para encriptación), expórtalas también con `--export-secret-subkeys`.
- **Backup**: Almacena las exportaciones en una bóveda segura (ej., disco encriptado).
- **Versiones**: Probado en GPG 2.x; funciona de forma similar en 1.x.
- Para más detalles, consulta la documentación oficial de GPG: [GnuPG Manual](https://www.gnupg.org/documentation/manuals/gnupg/).