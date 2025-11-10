---
audio: false
generated: true
lang: es
layout: post
title: Falta libpq-fe.h para psycopg2
translated: true
type: note
---

Al intentar instalar el paquete de Python `psycopg2`, encontraste un error que indica que la wheel no se pudo construir correctamente. La parte clave del mensaje de error es:

```
In file included from psycopg/adapter_asis.c:28:
./psycopg/psycopg.h:36:10: fatal error: libpq-fe.h: No such file or directory
   36 | #include <libpq-fe.h>
      |          ^~~~~~~~~~~~
compilation terminated.
```

Este error ocurre porque falta en tu sistema el archivo `libpq-fe.h`, un archivo de cabecera de la biblioteca cliente de PostgreSQL. El paquete `psycopg2` requiere este archivo para compilarse desde el código fuente, ya que proporciona la interfaz para conectar Python con bases de datos PostgreSQL. A continuación, explicaré por qué sucede esto y proporcionaré una solución paso a paso para solucionarlo.

---

### Por qué ocurre este error
El paquete `psycopg2` es un adaptador de PostgreSQL para Python, y cuando lo instalas usando `pip`, intenta compilar sus extensiones en C. Estas extensiones dependen de la biblioteca cliente de PostgreSQL, específicamente de los archivos de cabecera de desarrollo como `libpq-fe.h`. El mensaje de error lo confirma:

```
Parece que te falta algún requisito previo para construir el paquete desde el código fuente.
```

Tu sistema, que parece ser una distribución de Linux basada en Debian (basado en el uso de `x86_64-linux-gnu-gcc`), carece de los archivos de desarrollo de PostgreSQL necesarios. Sin estos, la compilación falla, impidiendo que se construya la wheel para `psycopg2`.

El error también sugiere dos opciones:
1. Instalar el paquete binario preconstruido `psycopg2-binary` via PyPI.
2. Instalar los requisitos previos faltantes y construir `psycopg2` desde el código fuente.

Dado que tu proyecto especifica `psycopg2` (no `psycopg2-binary`) en el archivo de requisitos, y puede ser necesario construir desde el código fuente por compatibilidad o personalización, nos centraremos en solucionar el proceso de compilación. Sin embargo, también mencionaré la opción binaria más adelante para mayor exhaustividad.

---

### Cómo solucionar el error
Para resolver esto, necesitas instalar el paquete de desarrollo del cliente PostgreSQL, que proporciona `libpq-fe.h` y otros archivos necesarios. Así es como se hace:

#### Paso 1: Identifica tu sistema
Tu salida de compilación incluye `x86_64-linux-gnu-gcc`, lo que indica que probablemente estés usando un sistema basado en Debian como Ubuntu. La solución estará adaptada a esto, pero señalaré alternativas para otras distribuciones más adelante.

#### Paso 2: Instala el paquete de desarrollo de PostgreSQL
En sistemas basados en Debian (ej. Ubuntu), el paquete `libpq-dev` contiene las cabeceras de la biblioteca cliente de PostgreSQL, incluyendo `libpq-fe.h`. Instálalo con el siguiente comando:

```bash
sudo apt-get update
sudo apt-get install libpq-dev
```

- **`sudo apt-get update`**: Asegura que tu lista de paquetes esté actualizada.
- **`sudo apt-get install libpq-dev`**: Instala los archivos de desarrollo para la biblioteca cliente de PostgreSQL.

Este paquete coloca `libpq-fe.h` en una ubicación estándar (típicamente `/usr/include/postgresql`), que el proceso de compilación busca (como se ve en tu ruta de inclusión: `-I/usr/include/postgresql`).

#### Paso 3: Reintenta la instalación
Una vez que `libpq-dev` esté instalado, reintenta instalar tus requisitos:

```bash
pip install -r scripts/requirements/requirements.local.txt
```

Esto debería tener éxito ahora, ya que el archivo faltante `libpq-fe.h` estará disponible, permitiendo que `psycopg2` construya su wheel.

---

### Verificando la solución
Si la instalación aún falla, verifica que las cabeceras de PostgreSQL estén instaladas correctamente:
- Ejecuta `pg_config --includedir` para ver dónde están ubicadas las cabeceras (ej. `/usr/include/postgresql`).
- Asegúrate de que esto coincida con la ruta de inclusión en el comando de compilación (`-I/usr/include/postgresql`).

Tu salida de compilación muestra `-DPG_VERSION_NUM=140018`, indicando que está orientado a PostgreSQL 14. El paquete `libpq-dev` es independiente de la versión y debería funcionar con las cabeceras de PostgreSQL 14.

---

### Alternativa: Usar el paquete binario
Si no necesitas construir `psycopg2` desde el código fuente (ej. para optimizaciones específicas o compatibilidad), puedes instalar el paquete preconstruido `psycopg2-binary` en su lugar:

```bash
pip install psycopg2-binary
```

Para usar esto en tu proyecto, actualiza `scripts/requirements/requirements.local.txt` para reemplazar `psycopg2` con `psycopg2-binary`. Sin embargo, ten en cuenta que `psycopg2-binary` puede tener limitaciones (ej. posibles problemas de compatibilidad con ciertas versiones de PostgreSQL), por lo que construir desde el código fuente es preferible si tu proyecto lo requiere.

---

### Para otras distribuciones
Si no estás en un sistema basado en Debian, instala el paquete equivalente:
- **Red Hat/CentOS/Fedora**: `sudo yum install postgresql-devel` o `sudo dnf install postgresql-devel`
- **Arch Linux**: `sudo pacman -S postgresql-libs`
- **macOS (con Homebrew)**: `brew install libpq`

Luego, reintenta el comando `pip install`.

---

### Resumen
El error ocurre porque falta `libpq-fe.h`, que es parte de los archivos de desarrollo del cliente PostgreSQL. Para tu sistema basado en Debian, instalar `libpq-dev` con `sudo apt-get install libpq-dev` debería resolver el problema. Después de eso, vuelve a ejecutar tu comando `pip install`, y `psycopg2` debería compilarse correctamente. Si prefieres una solución más rápida y no necesitas compilación desde el código fuente, usa `psycopg2-binary` en su lugar.