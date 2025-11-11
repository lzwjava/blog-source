---
audio: false
generated: true
image: false
lang: es
layout: post
title: Tipado Predeterminado de Jackson Explicado y Deshabilitado
translated: true
type: note
---

En Jackson (la biblioteca `com.fasterxml.jackson.databind`), la **escritura predeterminada** (default typing) es una característica de `ObjectMapper` que automáticamente incluye metadatos de tipo (como `@class` o `@type`) en el JSON serializado para que los objetos puedan ser deserializados de vuelta a sus tipos polimórficos originales.

Por ejemplo, si serializas una `List<Animal>` que contiene tanto `Dog` como `Cat`, la escritura predeterminada añade campos JSON extra para que Jackson sepa qué subclase reinstanciar después.

---

### Cómo funciona la desactivación

Cuando **desactivas la escritura predeterminada**, Jackson deja de inyectar esos campos extra de metadatos de tipo. Eso significa:

* La salida JSON estará "más limpia", sin las pistas `@class`/`@type`.
* En la deserialización, Jackson solo puede reconstruir objetos usando los tipos estáticos declarados (el tipo objetivo que pasas), no los tipos originales en tiempo de ejecución.
* Cualquier caso de uso polimórfico se romperá a menos que configures explícitamente `@JsonTypeInfo`, `@JsonSubTypes` o módulos personalizados.

---

### Métodos relevantes

* **Activación** (estilo anterior a 2.10):

  ```java
  objectMapper.enableDefaultTyping();
  ```

  (obsoleto, porque era demasiado permisivo e introducía riesgos de seguridad.)

* **Desactivación**:

  ```java
  objectMapper.disableDefaultTyping();
  ```

  o en versiones más nuevas (2.10+), llamas:

  ```java
  objectMapper.activateDefaultTyping(PolymorphicTypeValidator, ObjectMapper.DefaultTyping.NON_FINAL);
  ```

  Para *desactivarlo*, simplemente **no llames** este método en absoluto (no hay escritura predeterminada a menos que la actives), o puedes llamar:

  ```java
  objectMapper.deactivateDefaultTyping();
  ```

---

### Seguridad y razonamiento

* **La escritura predeterminada está desactivada por defecto** en las versiones modernas de Jackson porque puede ser explotada (los atacantes podrían crear JSON que instancie clases peligrosas).
* Si la desactivas, Jackson se comporta en un modo "más seguro", donde la deserialización solo funciona para los tipos que enlazas explícitamente, no para tipos arbitrarios en tiempo de ejecución.
* Si necesitas soporte polimórfico, deberías anotar tus clases con `@JsonTypeInfo` en lugar de confiar en la escritura predeterminada global.

---

✅ **En resumen:**
Desactivar la escritura predeterminada le indica a Jackson **no** incluir metadatos de tipo en el JSON, lo que significa que no reconstruirá automáticamente subtipos polimórficos en la deserialización. Esto reduce la flexibilidad pero es más seguro y mantiene el JSON limpio.

¿Quieres que te muestre un **ejemplo JSON de antes/después** con la escritura predeterminada activada vs desactivada?