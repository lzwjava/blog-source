---
audio: false
generated: true
lang: es
layout: post
title: Corregir psycopg2 instalando PostgreSQL
translated: true
type: note
---

El error que estás encontrando indica que el paquete `psycopg2` requiere el ejecutable `pg_config` de PostgreSQL para compilar desde el código fuente, pero no se encuentra en tu sistema. Esto significa que necesitas instalar PostgreSQL en tu sistema macOS para proporcionar las dependencias necesarias. A continuación se detallan los pasos para instalar PostgreSQL en macOS y resolver el problema.

### Pasos para instalar PostgreSQL en macOS

#### 1. **Instalar PostgreSQL usando Homebrew (Recomendado)**
Homebrew es la forma más fácil de instalar y gestionar PostgreSQL en macOS.

1. **Instalar Homebrew (si aún no está instalado)**:
   - Abre la Terminal y ejecuta:
     ```bash
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
     ```
   - Sigue las instrucciones en pantalla para completar la instalación de Homebrew.

2. **Instalar PostgreSQL**:
   - En la Terminal, ejecuta:
     ```bash
     brew install postgresql
     ```
   - Este comando instala PostgreSQL y sus dependencias, incluyendo el ejecutable `pg_config` necesario para `psycopg2`.

3. **Iniciar PostgreSQL**:
   - Para iniciar el servicio de PostgreSQL, ejecuta:
     ```bash
     brew services start postgresql
     ```
   - Alternativamente, para iniciarlo manualmente para una sola sesión:
     ```bash
     pg_ctl -D /opt/homebrew/var/postgres start
     ```

4. **Verificar la instalación**:
   - Comprueba si PostgreSQL está instalado y en ejecución:
     ```bash
     psql --version
     ```
   - Deberías ver la versión de PostgreSQL (ej., `psql (PostgreSQL) 17.0`).
   - También puedes iniciar sesión en el shell de PostgreSQL para confirmar:
     ```bash
     psql -U $(whoami)
     ```

#### 2. **Instalar `psycopg2` después de PostgreSQL**
Una vez instalado PostgreSQL, reintenta instalar `psycopg2`. El ejecutable `pg_config` debería estar ahora disponible en tu PATH.

1. **Instalar `psycopg2`**:
   - Ejecuta:
     ```bash
     pip install psycopg2
     ```
   - Si estás usando un archivo de requisitos, ejecuta:
     ```bash
     pip install -r scripts/requirements/requirements.local.txt
     ```

2. **Alternativa: Instalar `psycopg2-binary` (Opción más fácil)**:
   - Si quieres evitar compilar `psycopg2` desde el código fuente (lo que requiere las dependencias de PostgreSQL), puedes instalar el paquete precompilado `psycopg2-binary`:
     ```bash
     pip install psycopg2-binary
     ```
   - Nota: `psycopg2-binary` no se recomienda para entornos de producción debido a posibles problemas de compatibilidad, pero es adecuado para desarrollo o testing.

#### 3. **Opcional: Añadir `pg_config` al PATH (si es necesario)**
Si el ejecutable `pg_config` aún no se encuentra después de instalar PostgreSQL, es posible que necesites añadirlo manualmente a tu PATH.

1. Localizar `pg_config`:
   - Homebrew normalmente instala PostgreSQL en `/opt/homebrew/bin` (para Apple Silicon) o `/usr/local/bin` (para Intel Macs).
   - Verifica la ubicación:
     ```bash
     find /opt/homebrew -name pg_config
     ```
     o
     ```bash
     find /usr/local -name pg_config
     ```

2. Añadir al PATH:
   - Si `pg_config` se encuentra (ej., en `/opt/homebrew/bin`), añádelo a tu PATH editando tu archivo de configuración del shell (ej., `~/.zshrc` o `~/.bash_profile`):
     ```bash
     echo 'export PATH="/opt/homebrew/bin:$PATH"' >> ~/.zshrc
     ```
   - Aplica los cambios:
     ```bash
     source ~/.zshrc
     ```

3. Verificar `pg_config`:
   - Ejecuta:
     ```bash
     pg_config --version
     ```
   - Si devuelve una versión, el PATH está configurado correctamente.

#### 4. **Solución de problemas**
- **El error persiste**: Si `pip install psycopg2` sigue fallando, asegúrate de tener las herramientas de compilación necesarias:
  - Instala Xcode Command Line Tools:
    ```bash
    xcode-select --install
    ```
  - Instala `libpq` (la librería cliente de PostgreSQL) explícitamente si es necesario:
    ```bash
    brew install libpq
    ```

- **Compatibilidad de la versión de Python**: Asegúrate de que tu versión de Python (3.13 en tu caso) es compatible con `psycopg2`. Si los problemas persisten, considera usar un entorno virtual con una versión de Python ligeramente anterior (ej., 3.11 o 3.12):
  ```bash
  python3.11 -m venv venv
  source venv/bin/activate
  pip install psycopg2
  ```

- **Verificar Homebrew**: Asegúrate de que Homebrew esté actualizado:
  ```bash
  brew update
  brew upgrade
  ```

#### 5. **Métodos de instalación alternativos (Opcional)**
Si prefieres no usar Homebrew, puedes instalar PostgreSQL mediante:
- **Postgres.app**:
  - Descárgalo desde [postgresapp.com](https://postgresapp.com/).
  - Sigue las instrucciones de configuración para instalar e iniciar PostgreSQL.
  - Añade el directorio `bin` (ej., `/Applications/Postgres.app/Contents/Versions/latest/bin`) a tu PATH como se describió anteriormente.
- **Instalador oficial de PostgreSQL**:
  - Descarga el instalador para macOS desde [postgresql.org](https://www.postgresql.org/download/macosx/).
  - Sigue el asistente de instalación.

#### 6. **Reintenta tu proyecto**
Después de instalar PostgreSQL y `psycopg2` (o `psycopg2-binary`), reintenta ejecutar tu proyecto o reinstalar los requisitos:
```bash
pip install -r scripts/requirements/requirements.local.txt
```

### Notas adicionales
- **Por qué ocurrió el error**: El paquete `psycopg2` requiere las librerías de desarrollo de PostgreSQL (específicamente `libpq`) para compilar desde el código fuente. Instalar PostgreSQL via Homebrew proporciona estas librerías.
- **Consideraciones para producción**: Para producción, usa `psycopg2` (no `psycopg2-binary`) y asegúrate de que tu versión de PostgreSQL coincida con el entorno objetivo.
- **Documentación**: Para más detalles, consulta la guía de instalación de `psycopg2` en [psycopg.org/docs/install.html](https://www.psycopg.org/docs/install.html).

Si encuentras más problemas, ¡comparte el mensaje de error específico y puedo ayudar a solucionarlo!