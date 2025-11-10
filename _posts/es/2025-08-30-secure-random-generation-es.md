---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: Generación Segura de Números Aleatorios con Python Secrets
translated: true
type: note
---

### Introducción al módulo `secrets`
El módulo `secrets` (introducido en Python 3.6) es parte de la biblioteca estándar y proporciona acceso a la generación de números aleatorios criptográficamente seguros. A diferencia del módulo `random`, que es adecuado para simulaciones o juegos, `secrets` está diseñado para tareas relacionadas con la seguridad, como generar contraseñas, tokens o secretos, ya que utiliza el generador de números aleatorios seguro criptográficamente del sistema operativo (por ejemplo, `/dev/urandom` en sistemas tipo Unix).

Para usarlo, simplemente impórtalo:
```python
import secrets
```

### Funciones clave y uso
Aquí están las principales funciones en `secrets`, con breves explicaciones y ejemplos. Estas generan valores aleatorios que son difíciles de predecir.

| Función | Propósito | Ejemplo de uso |
|----------|---------|---------------|
| `secrets.token_bytes(n)` | Genera `n` bytes aleatorios. Útil para crear claves binarias. | `key = secrets.token_bytes(16)`  # 16 bytes aleatorios |
| `secrets.token_hex(n)` | Genera `n` bytes aleatorios y los devuelve como una cadena hexadecimal (el doble de larga que `n` debido a la codificación hexadecimal). Ideal para tokens hexadecimales. | `hex_key = secrets.token_hex(16)`  # Cadena hexadecimal de 32 caracteres |
| `secrets.token_urlsafe(n)` | Genera `n` bytes aleatorios, codificados en base64 para uso seguro en URLs (por ejemplo, en tokens web). | `url_token = secrets.token_urlsafe(32)`  # Cadena de ~43 caracteres |
| `secrets.randbelow(n)` | Devuelve un entero aleatorio entre 0 y `n-1` (inclusive). Alternativa segura a `random.randint`. | `num = secrets.randbelow(100)`  # Entero aleatorio de 0 a 99 |
| `secrets.choice(seq)` | Devuelve un elemento aleatorio de una secuencia no vacía `seq`. Alternativa segura a `random.choice`. | `item = secrets.choice(['a', 'b', 'c'])`  # Aleatorio de la lista |

### Ejemplos prácticos
1. **Generar una contraseña segura**:
   Combina `secrets.choice` con constantes de cadena para una contraseña aleatoria.
   ```python
   import string
   import secrets

   alphabet = string.ascii_letters + string.digits + string.punctuation
   password = ''.join(secrets.choice(alphabet) for _ in range(12))
   print(password)  # ej., "X8f#9L&pW2c%"
   ```

2. **Crear tokens para API**:
   Usa `token_urlsafe` para cadenas aleatorias seguras para la web.
   ```python
   token = secrets.token_urlsafe(32)
   print(token)  # ej., "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
   ```

3. **Elecciones aleatorias para juegos o simulaciones (con seguridad)**:
   ```python
   winners = secrets.choice(['Alice', 'Bob', 'Charlie'])
   print(f"Ganador: {winners}")
   ```

### Mejores prácticas y notas
- **Fundamento de seguridad**: `secrets` evita la predictibilidad, haciéndolo resistente a ataques. Nunca uses `random` para contraseñas o tokens, ya que puede tener una semilla y ser predecible.
- **Rendimiento**: Las llamadas pueden ser más lentas que `random`, pero eso está bien para código crítico para la seguridad—no lo uses en exceso en bucles para tareas no críticas.
- **Casos límite**: `secrets.choice` lanza un `ValueError` para secuencias vacías; `randbelow(0)` lanza un `ValueError`.
- **Dependencias**: No se necesitan bibliotecas externas; está integrado.
- Para más detalles, consulta la [documentación oficial de Python](https://docs.python.org/3/library/secrets.html). ¡Si tienes un caso de uso específico, proporciona más contexto para un consejo personalizado!