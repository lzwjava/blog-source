---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Verificación de Firmas Digitales GPG
translated: true
type: note
---

### Verificación de firmas en GPG

GnuPG (GPG) te permite verificar firmas digitales para asegurar que un archivo o mensaje no ha sido alterado y proviene del remitente declarado. La verificación requiere la clave pública del firmante en tu llavero. A continuación se detallan los pasos y comandos para escenarios comunes.

#### Prerrequisitos
1.  **Instalar GPG**: Asegúrate de que GnuPG esté instalado en tu sistema (por ejemplo, mediante `apt install gnupg` en sistemas basados en Debian o `brew install gnupg` en macOS).
2.  **Importar la clave pública del firmante**: Necesitas la clave pública de la persona o entidad que firmó el archivo. Descárgala desde un servidor de claves o un archivo, luego impórtala:
    ```
    gpg --import public-key.asc
    ```
    (Reemplaza `public-key.asc` con el archivo de clave real. Si es de un servidor de claves, usa `gpg --keyserver keyserver.ubuntu.com --recv-keys KEYID` donde `KEYID` es la huella digital o el ID de la clave.)

#### Pasos para la verificación
El comando exacto depende de cómo se creó la firma (por ejemplo, inline en el archivo o separada).

1.  **Verificar una firma separada** (común para archivos como releases de software; la firma está en un archivo `.sig` separado):
    ```
    gpg --verify signature.sig original-file
    ```
    - Ejemplo de salida para una firma correcta:
      ```
      gpg: Signature made [fecha] using [tipo de clave] key ID [KEYID]
      gpg: Good signature from "[Nombre] <email@example.com>"
      ```
    - Si la clave no es de confianza, puedes ver una advertencia como "This key is not certified with a trusted signature!". Puedes ajustar los niveles de confianza con `gpg --edit-key KEYID` y luego `trust`.

2.  **Verificar un archivo con firma inline** (la firma está incrustada en el archivo, a menudo binario):
    - Para verificar solo la firma:
      ```
      gpg --verify signed-file
      ```
    - Para verificar y extraer el contenido original:
      ```
      gpg --output original-file --decrypt signed-file
      ```
      Esto solicitará una contraseña si está encriptado, pero para solo firmas, simplemente verifica.

3.  **Verificar un mensaje con firma clara** (texto legible con firma ASCII-armored, común en correos electrónicos o READMEs):
    ```
    gpg --verify clearsigned-file.txt
    ```
    La salida mostrará el estado de la firma sin alterar el archivo.

#### Resolución de problemas
-   **Error "No public key"**: Importa la clave como se mostró anteriormente.
-   **"Bad signature"**: El archivo pudo haber sido alterado— vuelve a descargarlo.
-   **Validez de la clave**: Verifica los detalles de la clave con `gpg --list-keys` o confirma que las huellas digitales coincidan con la fuente oficial.
-   Para verificación por lotes o scripting, añade `--batch --exit-on-status-write-error`.

Para más detalles sobre firma u opciones avanzadas, consulta el manual oficial.

[Making and verifying signatures - GnuPG Manual](https://www.gnupg.org/gph/en/manual/x135.html)