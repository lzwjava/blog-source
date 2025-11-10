---
audio: false
generated: true
image: false
lang: es
layout: post
title: Reglas de Precedencia de Propiedades de Primavera Explicadas
translated: true
type: note
---

En Spring, cuando tienes **claves de propiedad duplicadas** en tus fuentes de configuración (por ejemplo, `application.properties`, `application.yml`, variables de entorno, argumentos de la línea de comandos, etc.), **gana la última que tenga la precedencia más alta**.

Así es como funciona en detalle:

### 1. Orden de las Fuentes de Propiedades

Spring Boot aplica un **orden de fuentes de propiedades** bien definido. Por ejemplo:

* Argumentos de la línea de comandos
* `application.properties` / `application.yml` (primero los específicos del perfil, luego los predeterminados)
* Variables de entorno
* Propiedades del sistema
* Valores predeterminados en el código (`@Value("${...:default}")`)

Si la misma clave de propiedad aparece en múltiples fuentes, Spring elige la de la **fuente con mayor prioridad**.

### 2. Dentro del Mismo Archivo

Si tienes la misma clave de propiedad **repetida en un solo archivo** (como `application.properties`), Spring usa la **última ocurrencia declarada**.
Ejemplo (`application.properties`):

```properties
server.port=8080
server.port=9090
```

En este caso, `server.port=9090` toma efecto.

### 3. Entre Múltiples Archivos

Si defines la misma propiedad en `application.properties` y `application-dev.properties`, y activas el perfil `dev`, entonces el valor de `application-dev.properties` anulará el predeterminado.

### 4. Con `@PropertySource`

Si cargas múltiples archivos de propiedades mediante `@PropertySource`, el orden de declaración importa. El último puede anular los valores anteriores a menos que lo marques con `ignoreResourceNotFound` o controles explícitamente la precedencia.

---

✅ **Resumen:**

* Spring resuelve las propiedades por **precedencia de las fuentes**.
* Dentro del **mismo archivo**, gana la **última definición de la clave**.
* Entre archivos/perfiles, la **propiedad del perfil activo o del archivo cargado más tarde** anula las anteriores.

¿Quieres que también te muestre la **jerarquía exacta de precedencia de propiedades de Spring Boot (de mayor a menor)**? Eso da una imagen muy clara de dónde ocurren las anulaciones.