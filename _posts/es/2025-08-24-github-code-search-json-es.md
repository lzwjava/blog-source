---
audio: false
generated: true
image: false
lang: es
layout: post
title: Consejos de Búsqueda de Código de GitHub JSON
translated: true
type: note
---

Puedes escribir una consulta de búsqueda de código en GitHub de esta manera:

```
"deepseek/deepseek-chat-v3.1" language:JSON
```

### Notas:

* Las comillas aseguran que GitHub busque la cadena exacta `deepseek/deepseek-chat-v3.1`.
* `language:JSON` (o `lang:json`, ambas funcionan) restringe los resultados a archivos JSON.
* Si quieres incluir configuraciones que parecen JSON pero no están en archivos `.json` (como `.ipynb` o `.eslintrc`), puedes eliminar el filtro `lang:`.

Ejemplos:

* Buscar solo archivos JSON:

  ```
  "deepseek/deepseek-chat-v3.1" lang:json
  ```

* Buscar en todos los tipos de archivos pero seguir resaltando los resultados JSON:

  ```
  "deepseek/deepseek-chat-v3.1"
  ```

¿También quieres que te muestre cómo refinar esto aún más — por ejemplo, buscando solo dentro de repositorios, issues o código?