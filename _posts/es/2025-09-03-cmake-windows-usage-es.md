---
audio: false
generated: true
image: false
lang: es
layout: post
model: openai/gpt-5
title: Uso y Explicación de CMake en Windows
translated: true
type: note
---

¡Excelente pregunta! Vamos a repasar qué es **CMake**, cómo usarlo —especialmente en **Windows—** y qué significan comandos como `cmake --build`.

---

### 🔹 ¿Qué es CMake?
- **CMake** es un generador de sistemas de compilación multiplataforma.
- **No** compila los proyectos por sí mismo — crea los archivos de compilación apropiados (como soluciones de Visual Studio, Makefiles, archivos Ninja, etc.) para tu plataforma y compilador.
- Luego, usas esos archivos generados (o el propio controlador de compilación de CMake) para compilar realmente tu proyecto.

---

### 🔹 Instalar CMake en Windows
1. Descarga desde: [https://cmake.org/download/](https://cmake.org/download/)
2. Instala y asegúrate de que **"Add CMake to system PATH"** esté marcado (o agrégalo manualmente).
3. Verifica en una terminal (PowerShell o CMD):
   ```sh
   cmake --version
   ```

---

### 🔹 Flujo de trabajo típico de CMake en Windows

Supongamos que tu proyecto tiene:
```
project_root/
 ├─ CMakeLists.txt
 └─ src/
     └─ main.cpp
```

#### 1. Abre una terminal
(Puedes usar **x64 Native Tools Command Prompt for VS** si usas MSVC, o simplemente PowerShell normal si usas `MinGW`/`Ninja`.)

#### 2. Crea un directorio de compilación
Es mejor separar el código fuente y la compilación:
```sh
cd project_root
mkdir build
cd build
```

#### 3. Genera los archivos del sistema de compilación
Ejemplo con Visual Studio:
```sh
cmake .. -G "Visual Studio 17 2022" -A x64
```

Ejemplo con Ninja:
```sh
cmake .. -G Ninja
```

Este paso lee `../CMakeLists.txt` y genera las definiciones de compilación necesarias.

#### 4. Compila el proyecto
Ahora puedes usar:
```sh
cmake --build .
```

- En Windows con Visual Studio, esto realmente llama a `MSBuild` internamente.
- Con Ninja, llama a la herramienta `ninja`.

También puedes indicarle a CMake que compile en modo **Release**:
```sh
cmake --build . --config Release
```
⚠ Nota: `--config` solo se usa con generadores multi-configuración (Visual Studio, Xcode). Si usas Ninja o Makefiles, lo especificas durante la configuración:
```sh
cmake .. -DCMAKE_BUILD_TYPE=Release
```

#### 5. Ejecuta tu archivo ejecutable
Después de compilar, busca en el directorio apropiado:
- Para **Visual Studio**: `build/Debug/` o `build/Release/`
- Para **Ninja**: directamente dentro de `build/`

---

### 🔹 Hoja de referencia de comandos comunes
```sh
# Configurar proyecto (generar archivos de compilación)
cmake -S . -B build

# Configurar con tipo de compilación Release (generador de configuración única)
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release

# Compilar proyecto
cmake --build build

# Compilar con configuración específica (para Visual Studio/Xcode)
cmake --build build --config Release

# Instalar los resultados compilados (si está definido en CMakeLists)
cmake --install build
```

---

✅ **Resumen**:  
- **`cmake ..`** → Configura y genera archivos de proyecto/compilación específicos de la plataforma.  
- **`cmake --build .`** → Compila realmente usando la herramienta de compilación elegida.  
- En Windows, a menudo usarás **generadores de Visual Studio** o **Ninja** para un mejor rendimiento.  

---

¿Te gustaría que te proporcione un **ejemplo mínimo de CMakeLists.txt** y te guíe paso a paso en la compilación de un proyecto simple de C++ "Hola Mundo" en Windows?