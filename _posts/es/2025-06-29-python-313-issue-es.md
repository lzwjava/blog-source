---
audio: false
generated: true
lang: es
layout: post
title: Error de CuPy con Python 3.13
translated: true
type: note
---

### Descripción del Problema

Estás encontrando un `AttributeError` al ejecutar un script de Python que importa la biblioteca CuPy para cálculos en GPU. El error ocurre durante la declaración `import cupy as cp`, impidiendo que el script se ejecute. El traceback apunta a un problema dentro del código interno de CuPy, específicamente en `cupy/cuda/device.pyx` en la línea 105, donde un decorador `memoize` intenta modificar el atributo `__name__` de una función o método incorporado. El mensaje de error es:

```
AttributeError: attribute '__name__' of 'builtin_function_or_method' objects is not writable
```

Este problema parece estar relacionado con tu uso de Python 3.13, que puede introducir problemas de compatibilidad con la versión de CuPy que tienes instalada.

### Causa del Error

El error surge porque:

- **El Decorador `memoize` de CuPy**: CuPy utiliza un decorador `memoize` para almacenar en caché los resultados de las funciones y optimizar el rendimiento. Este decorador depende de `functools.update_wrapper` de Python para copiar atributos (como `__name__`) de la función original a la función contenedora.
- **Funciones Incorporadas**: En Python, las funciones incorporadas (implementadas en C) tienen un atributo `__name__` de solo lectura. Cuando `update_wrapper` intenta establecer este atributo, falla con un `AttributeError`.
- **Compatibilidad con Python 3.13**: La función específica que se está memoizando en `device.pyx` de CuPy es probablemente una función incorporada, y Python 3.13 puede aplicar reglas más estrictas o manejar las funciones incorporadas de manera diferente a versiones anteriores, exponiendo este problema.

Dado que el error ocurre durante la importación de CuPy, es un problema sistémico vinculado a la inicialización de la biblioteca y no a la lógica de tu script.

### Solución Recomendada

La solución más simple y práctica es ejecutar tu script con una versión anterior de Python donde se sabe que CuPy es compatible, como Python 3.11 o 3.12. Esto evita el problema de compatibilidad con Python 3.13 sin requerir modificaciones en el código fuente de CuPy o soluciones alternativas complejas.

#### Por Qué Esto Funciona

- **Compatibilidad**: Las versiones de CuPy hasta las últimas release (ej., v11) están probadas y son compatibles con versiones de Python como 3.11 y 3.12, donde este error específico no ocurre.
- **Sin Cambios de Código**: Tu script, que realiza benchmarks de ordenación en GPU con CuPy, puede ejecutarse tal cual está en un entorno de Python anterior, garantizando la integridad del benchmark.
- **Facilidad de Implementación**: Cambiar de versión de Python es sencillo usando entornos virtuales o herramientas como `conda`.

### Solución Paso a Paso

Así es como puedes resolver el problema:

#### Opción 1: Usando `virtualenv`

1. **Instala Python 3.11 o 3.12**
   - Asegúrate de que Python 3.11 o 3.12 esté instalado en tu sistema (ej., a través de tu gestor de paquetes o el sitio web oficial de Python).

2. **Crea un Entorno Virtual**
   ```bash
   virtualenv -p python3.11 venv
   ```
   Esto crea un entorno virtual llamado `venv` usando Python 3.11. Reemplaza `python3.11` con `python3.12` si lo prefieres.

3. **Activa el Entorno Virtual**
   ```bash
   source venv/bin/activate
   ```

4. **Instala CuPy**
   ```bash
   pip install cupy
   ```
   Esto instala la última versión compatible de CuPy para Python 3.11.

5. **Ejecuta Tu Script**
   ```bash
   python scripts/benchmark/cudamark.py
   ```
   Tu script ahora debería ejecutarse sin el `AttributeError`.

6. **Desactiva (Cuando Termines)**
   ```bash
   deactivate
   ```

#### Opción 2: Usando `conda`

1. **Crea un Entorno Conda**
   ```bash
   conda create -n cudabench python=3.11
   ```
   Esto crea un entorno llamado `cudabench` con Python 3.11. Usa `python=3.12` si prefieres Python 3.12.

2. **Activa el Entorno**
   ```bash
   conda activate cudabench
   ```

3. **Instala CuPy**
   ```bash
   pip install cupy
   ```

4. **Ejecuta Tu Script**
   ```bash
   python scripts/benchmark/cudamark.py
   ```

5. **Desactiva (Cuando Termines)**
   ```bash
   conda deactivate
   ```

### Verificación de la Solución

Después de configurar el entorno y ejecutar el script, deberías ver una salida similar a:

```
CPU cores: <tu_número_de_núcleos>
Threads: 1, Time taken: X.XXXX seconds
Threads: 2, Time taken: X.XXXX seconds
...
ThreadCount,TimeTakenSeconds
1,X.XXXXXX
2,X.XXXXXX
...
```

Si el script se ejecuta sin el `AttributeError`, la solución ha sido exitosa.

### Notas Adicionales

- **Recuento de Hilos en Tu Script**: Tu script itera sobre recuentos de hilos (`1, 2, 4, 8, 16, 32, 64, 128`), pero la función `parallel_sort_gpu` utiliza la ordenación basada en GPU de CuPy (`cp.sort`), que no utiliza directamente hilos de la CPU. El bucle de recuento de hilos puede no afectar el rendimiento de la ordenación en GPU como se espera. Si esto es intencionado para modificaciones futuras (ej., añadir hilos de CPU), está bien; de lo contrario, podrías simplificar el benchmark para centrarte únicamente en el rendimiento de la GPU.
- **Versión de CuPy**: Si sospechas que la versión de CuPy está desactualizada, asegúrate de instalar la última ejecutando `pip install cupy --upgrade`. Sin embargo, el problema principal aquí es la compatibilidad con Python 3.13, no solo la versión de CuPy.
- **Solución a Largo Plazo**: Si debes usar Python 3.13, considera revisar el repositorio de GitHub de CuPy o su rastreador de incidencias en busca de actualizaciones que admitan Python 3.13 (a partir de junio de 2025, esto podría estar disponible). Alternativamente, podrías hacer un fork de CuPy y parchear el decorador `memoize` para manejar funciones incorporadas, pero esto es más complejo e innecesario para un benchmark.

Al usar Python 3.11 o 3.12, puedes ejecutar tu benchmark de GPU de forma fiable sin encontrar este error.