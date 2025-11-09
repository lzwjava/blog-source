---
audio: false
date: 2025-09-10
generated: true
image: false
lang: es
layout: post
model: openai/gpt-5
title: Estrategia de Pruebas de API para Unicidad e Idempotencia
translated: true
type: note
---

Buena pregunta. Hagamos un zoom out y luego vayamos a lo práctico sobre la "unicidad" en las pruebas de API/integración.

# Qué es qué (repaso rápido)

* **URL (ruta + consulta)**

  * La ruta suele ser la **identidad del recurso**: `/orders/123`.
  * Los parámetros de consulta son **filtros/modificadores**: `/orders?status=PAID&page=2`.

* **Método**

  * `GET/HEAD` son seguros.
  * `PUT` es **idempotente** (misma llamada, mismo resultado).
  * `POST` **no** es idempotente a menos que añadas un esquema de **Idempotency-Key**.
  * `PATCH` no garantiza idempotencia.

* **Cabeceras**

  * `Content-Type`: cómo se codifica el **cuerpo**.

    * `application/json` → cuerpo JSON.
    * `application/x-www-form-urlencoded` → cuerpo `a=1&b=2`.
    * `multipart/form-data; boundary=----abcd` → archivos/subidas y partes mixtas.
  * `Content-Disposition` aparece **dentro de las partes multipart**, no en la petición de nivel superior. Una parte típica:

    ```
    --Boundary123
    Content-Disposition: form-data; name="file"; filename="x.png"
    Content-Type: image/png

    <binary bytes>
    --Boundary123--
    ```
  * Cabeceras personalizadas útiles:

    * **Idempotency-Key**: desduplica POSTs con efectos secundarios.
    * **X-Request-ID / Correlation-ID**: rastrea/registra una única petición a través de servicios.

* **Cuerpo**

  * JSON: un documento serializado.
  * `form-urlencoded`: pares clave-valor como una cadena de consulta pero en el cuerpo.
  * `multipart/form-data`: múltiples "partes" separadas por el delimitador `boundary` (`----WebKitFormBoundary...` es una cadena común de los navegadores).

# ¿Dónde debe residir la identidad?

* **Identidad del recurso** → en la **ruta de la URL** (`/users/{id}`), porque es estable y se puede marcar.
* **Modificadores de operación** → consulta o cabeceras.
* **Representación/estado a escribir** → cuerpo.

Intentar codificar la unicidad de la petición sólo en la URL a menudo falla para operaciones de escritura (ej., POST con JSON grande). En su lugar, piensa en **dos capas**:

1. **Identidad de la petición (huella digital)**:
   Un hash determinista de:

   * **Método** HTTP
   * **Ruta canónica** (plantilla + valores concretos)
   * **Consulta normalizada** (ordenada)
   * **Cabeceras seleccionadas** (sólo las que afectan a la semántica, ej., `Accept`, `Content-Language`, *no* `Date`)
   * **Cuerpo** (JSON normalizado o un resumen por parte para multipart)

2. **Identidad de la operación (idempotencia de negocio)**:
   Para operaciones con efectos secundarios (crear/cobrar/transferir), usa **Idempotency-Key** (un UUID por *intención de negocio*). El servidor almacena el primer resultado bajo esa clave y lo devuelve para los reintentos.

Estos resuelven problemas diferentes: las huellas digitales ayudan a tus **pruebas** y **observabilidad**; las claves de idempotencia protegen la **producción** de efectos duplicados.

# Estrategia de prueba para la "unicidad"

1. **Define una función de huella digital de petición** (lado del cliente/prueba). Lógica de ejemplo:

   * Convertir nombres de cabeceras a minúsculas; incluir sólo una lista permitida segura.
   * Ordenar parámetros de consulta; convertir cuerpo JSON a cadena estable (eliminar espacios en blanco, ordenar claves).
   * SHA-256 sobre `METHOD\nPATH\nQUERY\nHEADERS\nBODY`.

2. **Da a cada prueba un Correlation ID**

   * Genera un UUID por caso de prueba: `X-Request-ID: test-<suite>-<uuid>`.
   * Regístralo en el servidor para poder vincular los registros a una prueba.

3. **Usa Idempotency-Key donde sea necesario**

   * Para POSTs que crean recursos o cobran dinero:

     * `Idempotency-Key: <uuid>`
     * El servidor debe devolver el mismo 200/201 y cuerpo para reintentos con la misma clave dentro de una ventana de retención.

4. **Mantén los datos de prueba únicos pero mínimos**

   * Usa IDs deterministas con semilla (ej., email `user+T001@example.com`) o añade un sufijo con el UUID de la prueba.
   * Limpia, o mejor, diseña las pruebas para que sean **idempotentes** usando PUT/DELETE contra tus IDs con semilla donde sea posible.

5. **Comprueba en el nivel correcto**

   * Para operaciones **idempotentes**: comprueba **estado**, **representación** y **efectos secundarios** (ej., recuento de registros sin cambios en la repetición).
   * Para POSTs **no idempotentes** con Idempotency-Key: comprueba primera llamada 201, reintento posterior 200 con mismo cuerpo (o 201 repetido con el mismo recurso).

# Fragmentos prácticos

**Ejemplos de cURL**

* POST JSON:

  ```bash
  curl -X POST https://api.example.com/orders \
    -H 'Content-Type: application/json' \
    -H 'Idempotency-Key: 4b6f2d1a-...' \
    -H 'X-Request-ID: test-orders-create-...' \
    -d '{"customerId":"C123","items":[{"sku":"ABC","qty":1}]}'
  ```
* Subida multipart:

  ```bash
  curl -X POST https://api.example.com/uploads \
    -H 'X-Request-ID: test-upload-...' \
    -F 'file=@/path/pic.png' \
    -F 'meta={"purpose":"avatar"};type=application/json'
  ```

  (curl establece `Content-Type: multipart/form-data; boundary=----...` y cada parte tiene su propio `Content-Disposition`.)

**Huella digital de petición en Python (ilustrativo):**

```python
import hashlib, json, urllib.parse

def canonical_json(obj):
    return json.dumps(obj, separators=(',', ':'), sort_keys=True)

def normalize_query(url):
    parsed = urllib.parse.urlsplit(url)
    q = urllib.parse.parse_qsl(parsed.query, keep_blank_values=True)
    q.sort()
    return urllib.parse.urlunsplit((parsed.scheme, parsed.netloc, parsed.path, urllib.parse.urlencode(q), '')), q

def request_fingerprint(method, url, headers=None, body_bytes=b''):
    headers = headers or {}
    # lista permitida de cabeceras que afectan a la semántica
    allow = {'accept', 'content-type', 'content-language'}
    norm_headers = {k.lower(): v.strip() for k, v in headers.items() if k.lower() in allow}
    header_line = '\n'.join(f'{k}:{norm_headers[k]}' for k in sorted(norm_headers))
    url_no_query, q_pairs = normalize_query(url)
    query_line = '&'.join(f'{k}={v}' for k, v in q_pairs)
    h = hashlib.sha256()
    h.update((method.upper() + '\n').encode())
    h.update((url_no_query + '\n').encode())
    h.update((query_line + '\n').encode())
    h.update((header_line + '\n').encode())
    h.update(body_bytes or b'')
    return h.hexdigest()
```

* Para cuerpos JSON, pasa `body_bytes=canonical_json(payload).encode()`.
* Para multipart, haz un hash de cada parte y luego concaténalas para evitar ruido del boundary.

# Respondiendo a tu idea central

> "Si la URL es única entonces las peticiones son únicas; los parámetros/cuerpo aún contribuyen mucho—¿cómo pensar sobre la unicidad para las pruebas de API/integración?"

* Considera que **sólo la URL** es **insuficiente** para la unicidad en las pruebas, porque las cabeceras y el cuerpo cambian materialmente la semántica.
* Construye una **huella digital de petición** como la anterior para desduplicar/rastrear en las pruebas.
* Para la desduplicación a nivel de negocio de los **POSTs**, confía en **Idempotency-Key**, no en la URL.
* Mantén la **identidad del recurso** en la ruta para claridad y mejor determinismo en las pruebas.

# Pequeña lista de comprobación que puedes adoptar hoy

* [ ] Añade `X-Request-ID` (UUID) a cada petición de prueba.
* [ ] Añade `Idempotency-Key` a los POSTs que crean/cobran.
* [ ] Implementa un helper de prueba que calcule una huella digital de petición y la registre con cada aserción.
* [ ] Canonicaliza JSON antes del hashing; ordena parámetros de consulta; lista permitida de cabeceras semánticas.
* [ ] Prefiere PUT para upserts para hacer las pruebas idempotentes; reserva POST para creaciones reales.
* [ ] Para multipart, comprueba las **partes analizadas por el servidor** (nombres, nombres de archivo, tipos de contenido) en lugar de los bytes crudos del boundary.

Si compartes tu stack de pruebas actual (pytest/unittest + requests/httpx, o Java/Kotlin), puedo proporcionar un helper listo para usar adaptado a él.