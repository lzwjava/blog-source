---
audio: false
generated: true
image: false
lang: es
layout: post
model: openai/gpt-5
title: Conceptos Básicos de Gestión de Claves GPG
translated: true
type: note
---

## Introducción a la Gestión de Claves GPG

GPG (GNU Privacy Guard) es una implementación gratuita del estándar OpenPGP para comunicación segura, utilizada para cifrar, firmar y verificar datos. En su núcleo está la **criptografía de clave pública**, donde cada usuario tiene una **clave pública** (compartida abiertamente para cifrado y verificación) y una **clave privada** (guardada en secreto para descifrado y firma). La gestión de claves implica crear, distribuir, mantener y proteger estas claves para evitar manipulaciones, compromisos o mal uso. Una gestión deficiente puede llevar a ataques como la sustitución de claves, donde un atacante reemplaza tu clave con la suya para interceptar comunicaciones.

El modelo de "red de confianza" en GPG permite a los usuarios certificar las claves de los demás, construyendo una red de identidades verificadas. Las claves se almacenan en **keyrings** (archivos públicos y privados, por ejemplo, `pubring.kbx` y `secring.gpg` en versiones antiguas, o unificados en las más recientes). Siempre haz una copia de seguridad de tus claves privadas y utiliza frases de contraseña seguras.

## Estructura de una Clave

Un par de claves GPG no es solo una clave, es un conjunto:
- **Clave primaria**: Una clave maestra de firma (por ejemplo, RSA o DSA) utilizada para certificar (firmar) otras claves y autofirmar los componentes de tu clave.
- **Subclaves**: Claves subordinadas opcionales para tareas específicas:
  - Subclave de firma: Para firmar mensajes.
  - Subclave de cifrado: Para cifrar datos (a menudo se rota periódicamente).
  - Subclave de autenticación: Para SSH o similar.
- **Identificadores de Usuario (UIDs)**: Cadenas como "Alice (Comentario) <alice@example.com>" que vinculan la clave a una identidad real. Pueden existir múltiples UIDs para diferentes roles.
- **Autofirmas**: La clave primaria firma sus propios componentes para evitar manipulaciones.

Visualiza la estructura de una clave de forma interactiva:
```
gpg --edit-key <id-de-clave-o-email>
```
Dentro del menú, usa `check` para verificar las autofirmas o `toggle` para ver las partes privadas (si están disponibles).

## Generación de Claves

Comienza con un par de claves primarias. Utiliza el método interactivo para principiantes:

1. Ejecuta `gpg --full-gen-key` (o `--gen-key` para valores predeterminados).
2. Elige el tipo de clave (predeterminado: RSA para firma y cifrado).
3. Selecciona el tamaño de la clave (por ejemplo, 4096 bits para mayor seguridad; se recomienda un mínimo de 2048).
4. Establece la fecha de expiración (por ejemplo, 1y para un año; "0" para nunca; evita la expiración indefinida si es posible).
5. Ingresa el identificador de usuario (nombre, email).
6. Establece una frase de contraseña segura (20+ caracteres, mayúsculas/minúsculas/símbolos).

Para una generación rápida (no interactiva):
```
gpg --quick-generate-key "Alice <alice@example.com>" rsa default 1y
```

Después de la generación, crea un **certificado de revocación** (un archivo para invalidar tu clave si es comprometida):
```
gpg --output revoke.asc --gen-revoke <tu-id-de-clave>
```
Almacena esto de forma segura (por ejemplo, impreso en una caja fuerte); no lo compartas hasta que sea necesario.

Para agregar subclaves o UIDs más tarde:
- Ingresa `gpg --edit-key <id-de-clave>`, luego `addkey` (para subclave) o `adduid` (para UID). Estos se autofirman automáticamente.

## Listado y Visualización de Claves

- Listar claves públicas: `gpg --list-keys` (o `--list-public-keys`).
- Listar claves privadas: `gpg --list-secret-keys`.
- Vista detallada: `gpg --list-keys --with-subkey-fingerprint <id-de-clave>` (muestra las huellas digitales de las subclaves).

La salida muestra el ID de la clave (corto/largo), fechas de creación/expiración, capacidades (por ejemplo, `[SC]` para firmar/certificar) y UIDs.

## Exportación e Importación de Claves

**Exportar** comparte tu clave pública o hace copias de seguridad de las privadas:
- Clave pública: `gpg --armor --export <id-de-clave> > mykey.asc` (en formato ASCII-armored para email).
- Clave privada (solo copia de seguridad): `gpg --armor --export-secret-keys <id-de-clave> > private.asc`.
- A un servidor de claves: `gpg --keyserver hkps://keys.openpgp.org --send-keys <id-de-clave>`.

**Importar** agrega las claves de otros a tu keyring público:
- `gpg --import <archivo.asc>` (fusiona con las existentes; agrega nuevas firmas/subclaves).
- Desde un servidor de claves: `gpg --keyserver hkps://keys.openpgp.org --recv-keys <id-de-clave>`.

Después de importar, verifica con `gpg --edit-key <id-de-clave>` y `check` para ver las autofirmas.

## Firma y Certificación de Claves

Para construir confianza:
- Firmar una clave (certificar que es válida): `gpg --sign-key <otro-id-de-clave>` (o `lsign-key` solo para uso local).
- Firma rápida: `gpg --quick-sign-key <huella-digital> "User ID"`.
- Establecer nivel de confianza: En `--edit-key`, usa `trust` (por ejemplo, "5" para confianza absoluta).

Esto crea firmas en la clave, visibles en los listados. La red de confianza calcula la validez basándose en tu confianza en los firmantes.

## Revocación de Claves

La revocación invalida una clave o componente sin eliminarlo, asegurando que otros vean que ya no es válida:
- Clave completa: Importa tu certificado de revocación: `gpg --import revoke.asc`, luego exporta/envía la clave actualizada.
- Subclave/UID: En `--edit-key`, selecciona con `key 1` o `uid 1`, luego `revkey` o `revuid`.
- Revocar UID rápidamente: `gpg --quick-revoke-uid <id-de-clave> <uid-a-revocar>`.

Razones para la revocación: comprometida, ya no se usa, reemplazada. Siempre publica las claves revocadas.

## Mejores Prácticas

- **Seguridad**: Utiliza tokens de hardware (por ejemplo, YubiKey) para las claves privadas. Rota las subclaves de cifrado anualmente (`gpg --quick-add-key <huella-digital> rsa encr 1y`). Cambia las frases de contraseña regularmente (`gpg --change-passphrase <id-de-clave>`).
- **Expiración**: Establece fechas de expiración razonables (1-2 años) para forzar actualizaciones y detectar compromisos.
- **Distribución**: Comparte claves públicas a través de servidores de claves o directamente; verifica las huellas digitales en persona o a través de canales confiables para evitar ataques de intermediario.
- **Copia de seguridad**: Exporta las claves privadas a un almacenamiento cifrado. Genera certificados de revocación inmediatamente.
- **Limpieza**: Usa `gpg --edit-key` con `clean` para eliminar firmas inválidas.
- **Actualizaciones**: A partir de 2025, GnuPG 2.5+ admite algoritmos resistentes a la computación cuántica (por ejemplo, `--quick-generate-key ... pqc`); considera migrar para garantizar la seguridad futura.
- **Errores Comunes**: Nunca compartas claves privadas. Evita las expiraciones indefinidas. Prueba las revocaciones en un entorno de pruebas.

Para practicar, experimenta en un directorio de prueba con `gpg --homedir ./test-gpg`.

[Manual de GnuPG: Gestión de Claves](https://www.gnupg.org/gph/en/manual/c235.html)  
[Manual de GNU Privacy Guard: Gestión de Claves OpenPGP](https://www.gnupg.org/documentation/manuals/gnupg/OpenPGP-Key-Management.html)  
[GnuPG: Primeros Pasos](https://www.gnupg.org/gph/en/manual/c14.html)