---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: Exportación Segura de Claves Secretas GPG
translated: true
type: note
---

### Exportar claves secretas con GPG en formato Armored

GPG (GNU Privacy Guard) permite exportar claves secretas (privadas) en un formato ASCII armored, lo que las guarda en un archivo legible por humanos `.asc` (no binario). Esto es útil para copias de seguridad, transferencias o importación en otra máquina.

**Advertencia importante:** Las claves secretas contienen información sensible. Expórtelas solo cuando sea necesario, cifre el archivo de salida si lo va a almacenar o transmitir, y elimine la exportación después de usarla para evitar filtraciones accidentales. Nunca comparta claves secretas públicamente.

#### Estructura básica del comando
Para exportar una clave secreta para un ID de usuario específico (correo electrónico o nombre asociado a la clave), use:

```
gpg --export-secret-keys --armor [KEY_ID] > filename.asc
```

- `KEY_ID`: La huella digital de la clave, ID corto, correo electrónico o nombre. Puede listar sus claves con `gpg --list-secret-keys`.
- `--armor`: Genera la salida en formato armored (ASCII) en lugar de binario.
- `> filename.asc`: Redirige la salida a un archivo (ej. `my_secret_key.asc`). Omita esto para imprimir en la terminal.

#### Ejemplo de uso paso a paso
1.  **Liste sus claves secretas** para encontrar el KEY_ID:
    ```
    gpg --list-secret-keys
    ```
    Salida de ejemplo:
    ```
    sec   rsa3072/ABC12345 2023-01-01 [SC] [expires: 2025-01-01]
          Key fingerprint = 1234 5678 ABCD EF01 2345 6789 ABCD EF01 2345 6789
    uid                 [ultimate] Su Nombre <su@email.com>
    ```

    Aquí, `ABC12345` es el ID de clave corto, o use la huella digital completa `ABCDEF0123456789ABCDEF0123456789` para mayor precisión.

2.  **Exporte la clave secreta**:
    ```
    gpg --export-secret-keys --armor ABC12345 > my_secret_key.asc
    ```

3.  **Verifique la exportación** (opcional):
    ```
    cat my_secret_key.asc
    ```
    El archivo debe comenzar con `-----BEGIN PGP PRIVATE KEY BLOCK-----` y terminar con `-----END PGP PRIVATE KEY BLOCK-----`.

#### Opciones adicionales
-   **Exportar todas las claves secretas**: Omita el KEY_ID para exportar todas:
    ```
    gpg --export-secret-keys --armor > all_secret_keys.asc
    ```
-   **Con protección de contraseña**: GPG le pedirá su contraseña si la clave está cifrada (valor por defecto).
-   **Si necesita claves públicas en su lugar**: Use `--export` (solo para claves públicas).

Para la documentación completa, consulte la página man de GPG: `man gpg`. Si es nuevo en GPG, genere primero una clave con `gpg --gen-key`.