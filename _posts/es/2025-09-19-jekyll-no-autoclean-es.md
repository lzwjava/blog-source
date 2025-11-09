---
audio: false
generated: true
image: false
lang: es
layout: post
model: openai/gpt-5
title: Jekyll Build Carece de Función de Auto-Limpieza
translated: true
type: note
---

Jekyll en sí no tiene una bandera `--replace` o `--refresh`. Cada ejecución de `jekyll build` escribirá (o sobrescribirá) los archivos generados en la carpeta `--destination` que especifiques, pero **no elimina automáticamente los archivos antiguos** que ya no existen en tu fuente. Eso significa que pueden quedar archivos obsoletos.

Si deseas una salida de compilación limpia, necesitas limpiar el directorio de destino tú mismo antes de ejecutar `jekyll build`. Dos enfoques comunes:

**1. Limpieza manual en tu script**
Antes de llamar a `jekyll build`, limpia el directorio de destino:

```python
import shutil

def run_jekyll(destination: str, extra_args: list[str]) -> int:
    # Remove old files
    dest_path = Path(destination)
    if dest_path.exists():
        shutil.rmtree(dest_path)

    command = [
        "jekyll",
        "build",
        "--destination",
        destination,
        *extra_args,
    ]
    completed = subprocess.run(command, check=False)
    return completed.returncode
```

**2. Usar el `_site` propio de Jekyll**
Si dejas que Jekyll use el `_site` predeterminado bajo la raíz de tu proyecto (en lugar de un `--destination` personalizado), `jekyll clean` está disponible para purgar la salida antes de recompilar:

```bash
jekyll clean && jekyll build
```

Pero `jekyll clean` solo conoce `_site`, no una carpeta personalizada.

---

Entonces:

* No hay un `--replace` incorporado.
* Si estás usando un destino personalizado (como en tu script), debes eliminarlo explícitamente antes de compilar si deseas una salida nueva.

¿Te gustaría que ajuste tu script para que tenga una opción `--clean` (como `jekyll clean`) que limpie automáticamente el destino antes de compilar?