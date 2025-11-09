---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Ejecutables incluidos de MinGW-w64
translated: true
type: note
---

### Ejecutables incluidos en MinGW-w64

MinGW-w64 es principalmente una toolchain mínima para compilar de forma cruzada aplicaciones nativas de Windows utilizando GCC y herramientas relacionadas. Se centra en utilidades de desarrollo en lugar de un conjunto completo de comandos tipo Unix (por ejemplo, **no** incluye `gpg` o GnuPG por defecto; estos están disponibles como paquetes separados en entornos como MSYS2). El directorio `bin` de la instalación principal típicamente contiene los siguientes ejecutables (basado en una descarga independiente estándar, como las de las versiones oficiales en SourceForge). Esta lista puede variar ligeramente según la versión y la compilación, pero estos son los más comunes:

| Ejecutable | Descripción |
|------------|-------------|
| `gcc.exe` | Compilador GNU C |
| `g++.exe` | Compilador GNU C++ |
| `cpp.exe` | Preprocesador C |
| `gfortran.exe` | Compilador GNU Fortran (si está incluido en la compilación) |
| `ld.exe` | Enlazador GNU |
| `as.exe` | Ensamblador GNU |
| `ar.exe` | Archivador para crear bibliotecas |
| `ranlib.exe` | Genera índice para bibliotecas de archivo |
| `nm.exe` | Lista símbolos de archivos objeto |
| `objdump.exe` | Muestra información de archivos objeto |
| `objcopy.exe` | Copia y traduce archivos objeto |
| `strip.exe` | Elimina símbolos de ejecutables |
| `size.exe` | Lista los tamaños de sección de archivos objeto |
| `strings.exe` | Imprime cadenas imprimibles en archivos |
| `readelf.exe` | Muestra información de archivos ELF (para herramientas cruzadas) |
| `dlltool.exe` | Crea archivos de importación/exportación de DLL |
| `windres.exe` | Compila archivos de recursos de Windows |
| `gendef.exe` | Genera archivos .def a partir de DLLs |
| `genidl.exe` | Genera archivos .idl a partir de DLLs |
| `widl.exe` | Compila archivos IDL para Wine/Winelib |
| `gcc-ar.exe` | Wrapper de GCC para ar |
| `gcc-nm.exe` | Wrapper de GCC para nm |
| `gcc-ranlib.exe` | Wrapper de GCC para ranlib |

Estas son principalmente herramientas de compilación, enlace y manipulación de binarios de GCC y Binutils. Para un entorno más completo tipo Unix con herramientas como `gpg`, `make`, `bash`, etc., considere instalar MSYS2 (que incluye MinGW-w64 como un componente) y añadir paquetes via `pacman`.

[Sitio Oficial de MinGW-w64](https://www.mingw-w64.org/)  
[Paquetes de MSYS2 (para extensiones como GnuPG)](https://packages.msys2.org/package/mingw-w64-x86_64-gnupg)  
[Descargas de MinGW-w64 en SourceForge](https://sourceforge.net/projects/mingw-w64/files/)