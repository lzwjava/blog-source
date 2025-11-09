---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Algoritmos criptográficos en GnuPG
translated: true
type: note
---

### Algoritmos admitidos en software criptográfico (ej., GnuPG)

Esta lista describe los algoritmos admitidos por una herramienta como GnuPG (GPG), que se utiliza comúnmente para correo seguro (PGP/MIME), cifrado de archivos y firmas digitales. Los categoriza en criptografía de clave pública (asimétrica) para intercambio de claves y firma, cifrados simétricos para el cifrado de datos masivos, funciones hash para comprobaciones de integridad y firmas, y métodos de compresión para reducir el tamaño de los datos antes del cifrado. A continuación, lo desglosaré por categoría con breves explicaciones sobre el propósito y las características clave de cada algoritmo.

#### Algoritmos de Clave Pública (Pubkey)
Estos manejan operaciones asimétricas: una clave (pública) para cifrado/verificación de firma, y otra (privada) para descifrado/firma. Se utilizan en pares de claves para comunicación segura.

- **RSA**: Rivest-Shamir-Adleman. Un algoritmo fundamental tanto para cifrado como para firmas digitales. Ampliamente utilizado debido a su seguridad con tamaños de clave grandes (ej., 2048+ bits), pero computacionalmente intensivo.
- **ELG**: ElGamal. Principalmente para cifrado (no para firmas). Basado en el problema del logaritmo discreto; eficiente para intercambio de claves pero produce textos cifrados más grandes.
- **DSA**: Algoritmo de Firma Digital. Diseñado únicamente para firmas digitales (no para cifrado). Se basa en logaritmos discretos; común en sistemas antiguos pero mayormente reemplazado por ECDSA por eficiencia.
- **ECDH**: Diffie-Hellman de Curva Elíptica. Para acuerdo/intercambio de claves utilizando curvas elípticas. Proporciona una seguridad sólida con claves más pequeñas que el DH tradicional, ideal para dispositivos móviles/restringidos.
- **ECDSA**: Algoritmo de Firma Digital de Curva Elíptica. Una variante de curva elíptica de DSA para firmas. Más rápido y seguro por bit que DSA, con uso generalizado en protocolos modernos como TLS.
- **EDDSA**: Algoritmo de Firma Digital de Curva de Edwards. Un esquema de firma de curva elíptica de alta velocidad (ej., variante Ed25519). Resistente a ataques de canal lateral; favorecido en protocolos como SSH y Signal por su simplicidad y velocidad.

#### Cifrados Simétricos
Estos cifran datos con una clave secreta compartida (más rápidos para archivos grandes). Los cifrados por bloques procesan datos en bloques de tamaño fijo, a menudo con modos como CBC para encadenamiento.

- **IDEA**: International Data Encryption Algorithm. Un cifrado por bloques de 64 bits de la década de 1990; una vez popular pero ahora considerado débil debido al tamaño de la clave y riesgos de fuerza bruta.
- **3DES**: Triple Estándar de Cifrado de Datos. Aplica DES tres veces para mayor seguridad. Algoritmo heredado; lento y vulnerable a ataques, reemplazado por AES.
- **CAST5**: CAST-128. Un cifrado por bloques de 64 bits (familia CAST). Velocidad/seguridad equilibradas para su época; todavía se usa pero eclipsado por AES.
- **BLOWFISH**: Un cifrado por bloques de 64 bits con longitudes de clave variables (hasta 448 bits). Rápido y flexible; bueno para software pero no acelerado por hardware como AES.
- **AES**: Estándar de Cifrado Avanzado (clave de 128 bits). Cifrado por bloques aprobado por NIST; el estándar de oro para el cifrado simétrico: seguro, rápido y ubicuo.
- **AES192**: AES con claves de 192 bits. Ofrece un impulso de seguridad intermedio sobre el AES estándar.
- **AES256**: AES con claves de 256 bits. Variante de mayor seguridad de AES; recomendado para datos altamente sensibles.
- **TWOFISH**: Un cifrado por bloques de 128 bits (finalista de AES). Altamente seguro con tamaños de clave flexibles; buen rendimiento en software.
- **CAMELLIA128**: Cifrado por bloques Camellia (clave de 128 bits). Estándar japonés/europeo; seguridad y velocidad similares a AES.
- **CAMELLIA192**: Camellia con claves de 192 bits. Nivel de seguridad mejorado.
- **CAMELLIA256**: Camellia con claves de 256 bits. Variante de primer nivel, comparable a AES256.

#### Algoritmos Hash
Estos crean resúmenes de tamaño fijo a partir de datos para verificar la integridad, autenticidad o su uso en firmas/contraseñas. La resistencia a colisiones es clave (aunque SHA1 ahora está comprometido).

- **SHA1**: Algoritmo de Hash Seguro 1. Produce resúmenes de 160 bits; rápido pero inseguro debido a vulnerabilidades de colisión—evitar para nuevos usos.
- **RIPEMD160**: RACE Integrity Primitives Evaluation Message Digest (160 bits). Alternativa europea a SHA1; todavía razonablemente seguro pero envejeciendo.
- **SHA256**: Familia SHA-2 (256 bits). Robusto y ampliamente utilizado; base para Bitcoin y contraseñas seguras.
- **SHA384**: SHA-2 (384 bits). Resumen más largo para mayor seguridad en aplicaciones sensibles.
- **SHA512**: SHA-2 (512 bits). Variante SHA-2 más grande; excelente para hashing de alta seguridad.
- **SHA224**: SHA-2 (224 bits). Una versión truncada de SHA-256 para compatibilidad heredada.

#### Algoritmos de Compresión
Estos reducen los datos antes del cifrado para acelerar el procesamiento y reducir el tamaño de almacenamiento/transmisión. Se aplican de forma transparente en herramientas como GPG.

- **Uncompressed**: Sin compresión—los datos se cifran tal cual. Útil para archivos ya comprimidos (ej., JPEG) para evitar sobrecarga.
- **ZIP**: Algoritmo DEFLATE (LZ77 + codificación Huffman). Común en archivos comprimidos; buen equilibrio entre velocidad y ratio.
- **ZLIB**: DEFLATE mejorado con cabeceras/sumas de comprobación. Similar a ZIP pero más flexible para flujos.
- **BZIP2**: Transformada Burrows-Wheeler + Huffman. Más lento pero logra mejores ratios de compresión que ZIP/ZLIB, especialmente para texto.

Esta configuración permite flujos de trabajo flexibles y seguros—ej., firmar con ECDSA, cifrar con AES256, aplicar hash con SHA256 y comprimir con ZLIB. Para los últimos detalles de GnuPG, consulta el [manual oficial](https://www.gnupg.org/documentation/manuals/gnupg/index.html).