---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: Guía de Criptografía con Python
translated: true
type: note
---

### Introducción al Paquete de Criptografía

El paquete `cryptography` es una librería popular de Python que proporciona primitivas criptográficas y recetas para protocolos seguros. Se centra en la facilidad de uso y la seguridad, implementando estándares como AES, RSA y más. No está diseñado para implementar protocolos de alto nivel como SSH o TLS directamente—úsalo como un bloque de construcción. Siempre verifica que esté actualizado con los parches de seguridad.

### Instalación

Instala mediante pip:
```bash
pip install cryptography
```
Para un mejor rendimiento (especialmente para claves grandes u operaciones frecuentes), instálalo con soporte para OpenSSL:
```bash
pip install cryptography[openssl]
```
Nota: En algunos sistemas, puede que necesites instalar los headers de OpenSSL por separado (por ejemplo, `apt install libssl-dev` en Ubuntu).

### Conceptos Básicos

- **Primitivas**: Operaciones de bajo nivel como cifrado/descifrado.
- **Recetas**: Funciones de alto nivel y con opinión definida (por ejemplo, Fernet para cifrado simétrico).
- **Advertencias de Riesgo**: La librería utiliza advertencias para usos inseguros—presta atención a ellas.

Importa la librería:
```python
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import serialization, hashes, asyncioc as a
from cryptography.hazmat.primitives.asymmetric import rsa, padding
```

### Ejemplos

#### 1. Cifrado Simétrico con Fernet (El más Fácil para Principiantes)
Fernet utiliza AES-128 en modo CBC con HMAC para integridad. Es ideal para almacenar datos cifrados.

```python
from cryptography.fernet import Fernet

# Genera una clave (guárdala de forma segura, por ejemplo, en variables de entorno)
key = Fernet.generate_key()
cipher = Fernet(key)

# Cifrar
plaintext = b"Este es un mensaje secreto."
token = cipher.encrypt(plaintext)
print("Cifrado:", token)

# Descifrar
decrypted = cipher.decrypt(token)
print("Descifrado:", decrypted)
```
- **Notas**: Las claves están en base64 seguro para URLs (44 caracteres). Nunca codifiques las claves directamente en el código; rota periódicamente.

#### 2. Cifrado Asimétrico con RSA
Genera un par de claves pública/privada y cifra datos que solo el poseedor de la clave privada puede descifrar.

```python
from cryptography.hazmat.primitives.asymmetric import rsa, padding

# Generar clave privada
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

# Serializar para almacenamiento
pem_private = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()  # Usa BestAvailableEncryption() para protección con contraseña
)

# Obtener clave pública y serializar
public_key = private_key.public_key()
pem_public = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Cifrar con la clave pública
plaintext = b"Mensaje secreto"
ciphertext = public_key.encrypt(
    plaintext,
    padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
)

# Descifrar con la clave privada
decrypted = private_key.decrypt(
    ciphertext,
    padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
)
print("Descifrado:", decrypted)
```
- **Notas**: RSA es lento para datos grandes; úsalo para intercambio de claves o mensajes pequeños. El relleno OAEP previene ataques.

#### 3. Generación y Uso de Hashes
Para comprobaciones de integridad o hashing de contraseñas.

```python
from cryptography.hazmat.primitives import hashes

# Hashing de datos
digest = hashes.Hash(hashes.SHA256())
digest.update(b"Algunos datos")
hash_result = digest.finalize()
print("Hash SHA256:", hash_result.hex())
```

Para contraseñas, usa `cryptography.hazmat.primitives.kdf.pbkdf2` para la derivación de claves (por ejemplo, PBKDF2 para un hashing lento y con sal).

#### 4. Firmas Digitales con RSA
Firma datos para probar su autenticidad.

```python
# Usando las claves RSA del ejemplo anterior
message = b"Datos a firmar"
signature = private_key.sign(
    message,
    padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
    hashes.SHA256()
)

# Verificar con la clave pública
try:
    public_key.verify(
        signature,
        message,
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256()
    )
    print("Firma válida")
except Exception:
    print("Firma inválida")
```

### Mejores Prácticas

- **Gestión de Claves**: Almacena las claves de forma segura (por ejemplo, usando AWS KMS, módulos de seguridad de hardware). Nunca reutilices claves.
- **Relleno y Modos**: Siempre usa relleno seguro (por ejemplo, OAEP para RSA, GCM para AES).
- **Aleatoriedad**: Usa `os.urandom()` o el módulo `secrets` para semillas; evita `random`.
- **Actualizaciones**: La criptografía evoluciona—comprueba si hay vulnerabilidades en tu uso.
- **Evita Implementar las Tuyas Propias**: Para necesidades complejas, usa las recetas o intégrate con librerías de más alto nivel como `pyjwt` o `boto3`.
- **Pruebas**: Usa las constantes y excepciones de la librería para el manejo de errores.

### Lecturas Adicionales

- [Documentación Oficial](https://cryptography.io/en/latest/) – Referencia detallada de la API y tutoriales.
- [Página de PyPI](https://pypi.org/project/cryptography/) – Historial de versiones e integraciones.
- Para temas avanzados, explora el wiki de `cryptography` o los RFCs (por ejemplo, RFC 8017 para PKCS#1).

Si tienes un caso de uso específico (por ejemplo, cifrado de archivos o seguridad de API), proporciona más detalles para ejemplos personalizados.