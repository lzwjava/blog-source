---
audio: false
generated: true
lang: es
layout: post
title: Corrección de Errores de YAML y Archivos en Jekyll
translated: true
type: note
---

La salida que has proporcionado muestra dos tipos de errores:

1.  **Excepción YAML:** Esto indica un problema con el *front matter* (el bloque YAML en la parte superior) de tus archivos Markdown:

      * `/Users/lzwjava/projects/lzwjava.github.io/notes/2025-06-25-company-valuation-comparison-en.md`
      * `/Users/lzwjava/projects/lzwjava.github.io/notes/2025-06-25-top-companies-evolve-en.md`
        El error "did not find expected key while parsing a block mapping at line 2 column 1" sugiere que la sintaxis YAML en estos archivos es incorrecta, probablemente falta una clave o hay un problema de sangría en el *front matter*.

2.  **`Errno::ENOENT: No such file or directory @ rb_sysopen - /Users/lzwjava/projects/lzwjava.github.io/wandb/debug-internal.log`**: Este error indica que Jekyll está intentando acceder a un archivo o directorio que no existe, específicamente `/wandb/debug-internal.log`. Esto podría ser un archivo temporal o una dependencia de otra herramienta (como Weights & Biases - `wandb`) que Jekyll está intentando procesar.

Para responder a tu pregunta sobre cómo hacer que Jekyll ignore algunos directorios, puedes usar la opción `exclude` en tu archivo `_config.yml`.

Así es cómo hacerlo:

1.  **Abre tu archivo `_config.yml`** (ubicado en la raíz de tu proyecto Jekyll).

2.  **Añade o modifica la directiva `exclude`.** Esta directiva toma un array de rutas (archivos o directorios) que Jekyll debe ignorar durante su proceso de construcción.

    Por ejemplo, para ignorar el directorio `wandb` y cualquier otro directorio que quieras excluir, añade lo siguiente a tu `_config.yml`:

    ```yaml
    exclude:
      - wandb/
      - algun_otro_directorio/
      - otro_archivo_a_ignorar.md
    ```

    **Notas Importantes:**

      * Asegúrate de incluir la barra diagonal final (`/`) para los directorios, para garantizar que se ignore todo su contenido.
      * Las rutas son relativas a la raíz de tu proyecto Jekyll.

**Abordando tus errores específicos con `exclude`:**

  * **Para el error del directorio `wandb`:** Añadir `wandb/` a tu lista `exclude` en `_config.yml` debería evitar que Jekyll intente leer archivos dentro de él, resolviendo el error `No such file or directory` para `wandb/debug-internal.log`.

  * **Para la Excepción YAML:** La directiva `exclude` no solucionará los errores YAML en tus archivos Markdown. Necesitas **corregir manualmente el *front matter*** en `notes/2025-06-25-company-valuation-comparison-en.md` y `notes/2025-06-25-top-companies-evolve-en.md`.

    **Estructura Típica del Front Matter de Jekyll:**

    ```yaml
    ---
    layout: post
    title: "Mi Post Increíble"
    date: 2025-07-02 10:00:00 +0800
    categories: [notes, tech]
    tags: [jekyll, markdown]
    ---

    Tu contenido va aquí.
    ```

    Verifica nuevamente los archivos mencionados en la Excepción YAML para asegurarte de que siguen esta estructura, especialmente en lo que respecta a la sangría y los pares clave-valor correctos. El error "did not find expected key while parsing a block mapping at line 2 column 1" sugiere que algo está mal justo al comienzo de tu *front matter*, posiblemente una clave faltante o un espacio extra donde debería ir una clave.

Después de realizar estos cambios en tu `_config.yml` y corregir tus archivos Markdown, intenta ejecutar tu comando de construcción o servidor de Jekyll nuevamente.