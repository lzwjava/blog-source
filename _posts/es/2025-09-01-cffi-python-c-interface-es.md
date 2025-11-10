---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: Guía de Interfaz C de Python CFFI
translated: true
type: note
---

### ¿Qué es CFFI?
CFFI (C Foreign Function Interface) es una biblioteca de Python para llamar funciones C desde código Python. Es compatible tanto con CPython como con PyPy, proporcionando una alternativa más segura y portable a bibliotecas como ctypes. Admite dos modos principales: ABI (llamar a bibliotecas compartidas existentes) y API (compilar código C en línea).

### Instalación
Instala CFFI usando pip:
```bash
pip install cffi
```
CFFI requiere un compilador de C (por ejemplo, GCC en Linux, Visual Studio en Windows) para construir los módulos.

### Ejemplo de Uso Básico
Aquí tienes una guía paso a paso para un caso de uso simple: llamar a una función C que suma dos enteros usando el modo API (recomendado para código nuevo).

1. **Importar y Configurar FFI**:
   ```python
   from cffi import FFI
   ffibuilder = FFI()
   ```

2. **Definir Declaraciones C**:
   Especifica las firmas de las funciones C en una cadena:
   ```python
   ffibuilder.cdef("""
       int add(int a, int b);
   """)
   ```

3. **Proporcionar Código Fuente C**:
   Incluye la implementación en C:
   ```python
   ffibuilder.set_source("_example",
       """
       int add(int a, int b) {
           return a + b;
       }
       """)
   ```

4. **Compilar el Módulo**:
   Ejecuta este script una vez para construir la extensión C:
   ```python
   if __name__ == "__main__":
       ffibuilder.compile(verbose=True)
   ```
   Esto genera un módulo compilado (por ejemplo, `_example.cpython-39-x86_64-linux-gnu.so`).

5. **Usar el Módulo Compilado**:
   En tu código Python, importa y llama a la función:
   ```python
   from _example import lib
   result = lib.add(5, 3)
   print(result)  # Salida: 8
   ```

### Conceptos Clave
- **Objeto FFI**: La interfaz principal, creada con `FFI()`. Usa `cdef()` para declaraciones y `set_source()` para el código.
- **Declaraciones**: Informan a Python sobre tipos C, structs, funciones, etc. Las cadenas deben coincidir exactamente con la sintaxis de C.
- **Conversión de Tipos**: CFFI maneja tipos básicos (int, float, punteros) automáticamente. Usa arrays, structs o callbacks para mayor complejidad.
- **Manejo de Errores**: Ocurren excepciones como `CDefError` por definiciones C inválidas. Los errores en tiempo de ejecución de C (por ejemplo, vía `errno`) se pueden verificar con `ffi.errno`.
- **Gestión de Memoria**: Usa `ffi.new()` para structs/arrays de C y asegura una desasignación adecuada para evitar fugas.

### Modos: ABI vs. API
- **Modo ABI** (para bibliotecas existentes): Carga una biblioteca compartida (por ejemplo, `ffi.dlopen("mylib.so")`) y llama a las funciones directamente. Ejemplo:
  ```python
  from cffi import FFI
  ffi = FFI()
  ffi.cdef("int add(int a, int b);")
  lib = ffi.dlopen("/path/to/libmylib.so")
  result = lib.add(5, 3)
  ```
  Esto es más rápido para bibliotecas preconstruidas pero menos portable—necesitas el binario exacto.

- **Modo API** (recomendado): Compila código C en línea, como en el ejemplo anterior. Es más seguro, se optimiza mejor y funciona en múltiples plataformas.

### Características Avanzadas
- **Structs y Unions**: Define tipos complejos, por ejemplo, `cdef("struct Point { int x, y; }")`.
- **Arrays y Punteros**: Usa `ffi.new("int[10]")` para arrays o `ffi.cast("int*", ptr)` para conversiones.
- **Callbacks**: Pasa funciones Python a C usando `ffi.callback()`.
- **Integración con Paquetes**: Muchas bibliotecas (por ejemplo, cryptography, NumPy) usan CFFI para rendimiento.
- **Consejos de Rendimiento**: La compilación toma tiempo; usa compilaciones inplace o paquetes cffi para distribución. Evita transiciones pesadas Python-C en bucles.

Para la documentación completa, consulta la [documentación oficial de CFFI](https://cffi.readthedocs.io/). Esto cubre lo esencial—experimenta con los ejemplos para adaptarlos a tus necesidades. Si tienes un caso de uso específico, proporciona más detalles para un consejo personalizado.