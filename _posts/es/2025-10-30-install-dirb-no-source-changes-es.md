---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Instalar DirB Sin Cambios en el Código Fuente
translated: true
type: note
---

### Alternativas a modificar el código fuente de DirB

Si editar el código fuente (como `variables.h`) no es una opción—quizás debido a una configuración de solo lectura, políticas o simplemente preferencia—aquí hay formas sencillas de ejecutar DirB sin necesidad de compilación. Estas aprovechan paquetes preconstruidos o reimplementaciones. Priorizaré Linux (basado en tu ruta de compilación), pero ten en cuenta ajustes específicos del SO.

#### 1. **Instalar mediante el gestor de paquetes (Más fácil para Debian/Ubuntu/Kali)**
   DirB está disponible como un paquaje precompilado en los repositorios de muchas distribuciones, por lo que no se necesitan cambios en el código fuente ni compilación.
   - **En Kali Linux** (recomendado para herramientas de pentesting como esta):
     ```
     sudo apt update
     sudo apt install dirb
     ```
     - Está oficialmente soportado y mantenido en los repositorios de Kali. [Página de Herramientas de Kali](https://www.kali.org/tools/dirb/)
   - **En Ubuntu/Debian**:
     ```
     sudo apt update
     sudo apt install dirb
     ```
     - Si no se encuentra (las versiones antiguas podrían no tenerlo), habilita el repositorio universe: `sudo add-apt-repository universe && sudo apt update`.
   - **Verificación**: Ejecuta `dirb --help` después de la instalación. Las listas de palabras están en `/usr/share/dirb/wordlists/`.
   - **Por qué funciona**: Los paquetes manejan todas las correcciones (incluyendo definiciones múltiples) upstream.

   Si estás en una distribución diferente:
   - **Fedora/RHEL**: `sudo dnf install dirb` (si está en los repositorios EPEL; añade EPEL si es necesario: `sudo dnf install epel-release`).
   - **Arch**: `sudo pacman -S dirb`.

#### 2. **Usar una reimplementación en Python (Multiplataforma, sin compilar C)**
   El DirB original está basado en C y es complicado de compilar, pero existe un port moderno en Python que es funcionalmente idéntico (o mejor) y se instala via pip—no se requieren ajustes en el código fuente.
   - **Repositorio**: [ct-Open-Source/dirb en GitHub](https://github.com/ct-Open-Source/dirb)
   - **Instalar**:
     ```
     pip install git+https://github.com/ct-Open-Source/dirb.git
     ```
     - O clonar: `git clone https://github.com/ct-Open-Source/dirb.git && cd dirb && pip install .`
   - **Uso**: Igual que el original, ej., `dirb https://example.com /usr/share/wordlists/dirb/common.txt`.
   - **Pros**: Activamente mantenido, más rápido en algunos casos, funciona en Mac/Windows/Linux. Incluye extras como escaneo recursivo.
   - **Contras**: No es el binario "oficial", pero la salida coincide estrechamente.

#### 3. **Descargar un binario preconstruido (Disponibilidad limitada)**
   - Los lanzamientos oficiales en SourceForge son principalmente tarballs de código fuente (ej., dirb222.tar.gz), que aún requieren compilación.
   - No hay binarios universales, pero si estás en Kali/Parrot OS, la ruta del paquete es la mejor.
   - Como alternativa: Si tienes Docker, puedes extraer una imagen de Kali y ejecutar DirB dentro:
     ```
     docker run -it kalilinux/kali-rolling dirb http://example.com
     ```
     - No se necesita instalación; los contenedores están preconstruidos.

#### Comparación Rápida

| Método              | Soporte de SO      | Esfuerzo | Notas |
|---------------------|---------------------|--------|-------|
| **Apt/DNF/Pacman** | Linux (Debian/Fedora/Arch) | Bajo | Precompilado; incluye listas de palabras. |
| **Python Port**    | Cualquiera (Python 3+)    | Bajo | Alternativa moderna; solo pip. |
| **Docker**         | Cualquiera (con Docker)    | Medio | Aislado; sin instalación en el host. |

Si ninguna opción se ajusta (ej., entorno restringido), considera alternativas como Gobuster (`go install github.com/OJ/gobuster/v3@latest`)—está basado en Go, se compila fácilmente sin problemas y realiza una búsqueda de directorios similar.

¿En qué sistema operativo estás? Eso ayudará a afinar la opción. Si encuentras problemas, comparte el error/salida.