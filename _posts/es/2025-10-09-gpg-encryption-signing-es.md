---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Cifrado y Firma GPG Explicados
translated: true
type: note
---

### Conceptos básicos de GPG: Cifrado vs. Firma

Estás mezclando un par de conceptos aquí—GPG (GNU Privacy Guard) puede hacer **cifrado** (para proteger el contenido de archivos) y **firma** (para verificar identidad e integridad)—pero son características separadas. Lo desglosaré paso a paso, confirmaré tus puntos y aclararé dónde se superponen o difieren. Esto se basa en el uso estándar de GPG (que no ha cambiado mucho hasta 2025).

#### 1. **Generación de Claves y Tu Información (Nombre/Email)**
   - Cuando configuras GPG por primera vez, generas un **par de claves**: una clave privada (se mantiene en secreto) y una clave pública (se comparte con otros).
   - Durante la generación, proporcionas tu **nombre y email** como parte del "ID de usuario" de la clave (ej., `gpg --gen-key`). Esto vincula la clave a tu identidad.
   - También estableces una **frase de contraseña** para proteger tu clave privada. Esta frase de contraseña **no** se usa para cifrar archivos—solo sirve para desbloquear tu clave privada cuando es necesario.
   - Ejemplo de comando:
     ```
     gpg --gen-key
     ```
     Sigue las indicaciones para RSA/RSA, tamaño de clave, expiración y tu nombre/email.

#### 2. **Cifrar un Archivo**
   - **Con una contraseña (cifrado simétrico)**: Esto no involucra claves ni tu identidad—es rápido para compartir un archivo de forma segura. GPG usa la frase de contraseña para crear una única clave para el cifrado.
     - Comando: `gpg -c nombre_archivo.txt` (solicita la frase de contraseña, genera `nombre_archivo.txt.gpg`).
     - Cualquiera con la frase de contraseña puede descifrar: `gpg -d nombre_archivo.txt.gpg`.
     - Aquí no hay claves públicas/privadas; no hay verificación de identidad.
   - **Con claves públicas (cifrado asimétrico)**: Para cifrar para alguien específico, usa su clave pública. Tu nombre/email no está involucrado directamente en la salida del cifrado.
     - Comando: `gpg -e -r destinatario@ejemplo.com nombre_archivo.txt` (genera `nombre_archivo.txt.gpg`).
     - Solo la clave privada del destinatario puede descifrarlo.
   - La salida del cifrado es un archivo `.gpg`, pero **no es una firma**—son solo datos cifrados. No hay "firma GPG" solo por el cifrado.

#### 3. **Firmar un Archivo (Lo que estás describiendo)**
   - Firmar adjunta una **firma digital** a un archivo (o a su hash) para probar que vino de ti y no ha sido alterado. Aquí es donde entran tu **clave privada** e identidad.
   - **Sí, debes usar tu clave privada para generar la firma.** GPG la desbloquea con tu frase de contraseña.
     - Comando para una firma separada: `gpg --detach-sign nombre_archivo.txt` (genera `nombre_archivo.txt.sig`).
     - O en línea (firma y cifra a la vez): `gpg -s nombre_archivo.txt` (genera `nombre_archivo.txt.gpg` con la firma incrustada).
   - La firma es un "valor" criptográfico (como un hash firmado con tu clave privada) que incluye tu ID de clave y ID de usuario (nombre/email).
   - **Otros verifican con tu clave pública**: Importan tu clave pública (ej., desde un servidor de claves: `gpg --keyserver keys.openpgp.org --recv-keys TU_ID_DE_CLAVE`), luego ejecutan `gpg --verify nombre_archivo.txt.sig nombre_archivo.txt`.
     - Si coincide, dice algo como "Firma correcta de 'Tu Nombre <email>'".
   - **Sí, esto coincide con la identidad y genera confianza**:
     - La firma prueba que el archivo es del propietario de la clave (tú).
     - Si has compartido tu clave pública a través de un canal confiable (ej., tu sitio web) y la clave está firmada por otros en quienes confías, puedes "confiar" en la cadena.
     - No cifra el archivo—solo lo verifica. Combínalo con cifrado para seguridad completa (firmar y luego cifrar).

#### Diferencias Clave y Tus Preguntas

| Característica | Cifrado (Contraseña) | Cifrado (Clave Pública) | Firma |
|---------|-----------------------|--------------------------|---------|
| **¿Usa Frase de Contraseña?** | Sí, para clave simétrica | No (usa la clave pública del destinatario) | Sí, para desbloquear tu clave privada |
| **¿Involucra Tu Nombre/Email?** | No | Indirectamente (vía tu clave para respuesta de descifrado) | Sí, incrustado en la firma |
| **Salida** | Archivo `.gpg` (datos cifrados) | Archivo `.gpg` (datos cifrados) | `.sig` o incrustado en `.gpg` (valor de firma) |
| **¿Se Necesita Clave Privada?** | No | No (para cifrar a otros) | Sí, para generar |
| **Verificación** | Frase de contraseña para descifrar | Clave privada del destinatario | Cualquiera con tu clave pública |
| **Propósito** | Ocultar contenidos | Compartir de forma segura | Probar identidad/integridad |

- **Correcto sobre la clave privada**: Sí, **debes** usar tu clave privada (desbloqueada por la frase de contraseña) para firmar. ¡Nunca la compartas!
- **Correcto sobre la confianza**: Exactamente—si la firma se verifica contra tu clave pública, y confías en que esa clave pertenece al autor declarado (vía nombre/email y la web de confianza), puedes confiar en que el archivo es auténtico y no ha sido alterado. Es como un notario digital.

#### Consejos
- Siempre haz una copia de seguridad de tus claves: `gpg --export-secret-keys --armor > private.asc` (almacénala de forma segura).
- Para solo contraseñas (sin claves), herramientas como `age` u `openssl` son alternativas más simples, pero GPG es excelente para cosas vinculadas a la identidad.
- Error común: Olvidar exportar/compartir tu clave pública significa que otros no pueden verificar.

Si te referías a un comando o escenario específico (ej., cifrar *y* firmar), ¡comparte más detalles!

**Referencias**  
[Documentación de GPG: Cifrar y Firmar](https://www.gnupg.org/documentation/manuals/gnupg/)  
[Guía de Inicio Rápido de GPG](https://www.gnupg.org/documentation/manuals/gnupg/GnuPG-basics.html)