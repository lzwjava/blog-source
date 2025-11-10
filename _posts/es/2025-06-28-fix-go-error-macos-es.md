---
audio: false
generated: true
lang: es
layout: post
title: Cómo Corregir el Comando Go No Encontrado en macOS
translated: true
type: note
---

El mensaje de error `/bin/sh: go: command not found` indica que el lenguaje de programación Go no está instalado en tu sistema macOS, o no está configurado correctamente en tu PATH. El comando `make` está intentando ejecutar un proceso de compilación de Go, lo cual requiere el compilador de Go (`go`). A continuación se detallan los pasos para instalar Go en macOS y resolver este problema.

### Pasos para Instalar Go en macOS

Hay dos formas principales de instalar Go en macOS: usando el instalador oficial de Go o usando Homebrew. Cubriré ambos métodos, pero Homebrew suele ser más simple para los usuarios de macOS. Elige un método según tu preferencia.

#### Prerrequisitos
- Asegúrate de que tu versión de macOS sea 10.10 o posterior para la compatibilidad con versiones recientes de Go.
- Necesitas acceso de administrador para instalar Go y modificar archivos del sistema.
- Una aplicación de terminal (se encuentra en Aplicaciones > Utilidades > Terminal).

#### Método 1: Instalar Go Usando Homebrew (Recomendado)
Homebrew es un gestor de paquetes popular para macOS que simplifica la instalación de software.

1. **Instalar Homebrew (si aún no está instalado)**:
   - Abre Terminal y ejecuta:
     ```bash
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
     ```
   - Sigue las instrucciones en pantalla para completar la instalación.

2. **Instalar Go**:
   - Ejecuta el siguiente comando para instalar la última versión de Go:
     ```bash
     brew install go
     ```
   - Esto instala Go en `/usr/local/Cellar/go` (o una ruta similar) y añade el binario de Go a `/usr/local/bin`.

3. **Verificar la Instalación**:
   - Comprueba la versión de Go instalada ejecutando:
     ```bash
     go version
     ```
   - Deberías ver una salida como `go version go1.23.x darwin/amd64`, lo que confirma que Go está instalado.

4. **Configurar las Variables de Entorno** (si es necesario):
   - Homebrew normalmente añade Go a tu PATH automáticamente, pero si los comandos `go` no funcionan, añade la ruta del binario de Go a tu perfil de shell:
     - Abre o crea el archivo de configuración de shell apropiado (por ejemplo, `~/.zshrc` para Zsh, que es el predeterminado en macOS desde Catalina, o `~/.bash_profile` para Bash):
       ```bash
       nano ~/.zshrc
       ```
     - Añade las siguientes líneas:
       ```bash
       export PATH=$PATH:/usr/local/go/bin
       ```
     - Guarda el archivo (Ctrl+X, luego Y, luego Enter en nano) y aplica los cambios:
       ```bash
       source ~/.zshrc
       ```
     - Si quieres usar un workspace personalizado, establece `GOPATH` (opcional, ya que los módulos de Go a menudo eliminan la necesidad de esto):
       ```bash
       export GOPATH=$HOME/go
       export PATH=$PATH:$GOPATH/bin
       ```
     - Vuelve a cargar el archivo:
       ```bash
       source ~/.zshrc
       ```

5. **Probar la Instalación de Go**:
   - Ejecuta `go version` nuevamente para asegurarte de que el comando es reconocido.
   - Opcionalmente, crea un programa simple en Go para confirmar que todo funciona:
     ```bash
     mkdir -p ~/go/src/hello
     nano ~/go/src/hello/main.go
     ```
     - Añade el siguiente código:
       ```go
       package main
       import "fmt"
       func main() {
           fmt.Println("Hello, World!")
       }
       ```
     - Guarda y sal (Ctrl+X, Y, Enter), luego compila y ejecuta:
       ```bash
       cd ~/go/src/hello
       go run main.go
       ```
     - Deberías ver `Hello, World!` como salida.

#### Método 2: Instalar Go Usando el Instalador Oficial
Si prefieres no usar Homebrew, puedes instalar Go usando el paquete oficial de macOS.

1. **Descargar el Instalador de Go**:
   - Visita la página oficial de descargas de Go: https://go.dev/dl/
   - Descarga el paquete de macOS (`.pkg`) para tu arquitectura del sistema (por ejemplo, `go1.23.x.darwin-amd64.pkg` para Macs con Intel o `go1.23.x.darwin-arm64.pkg` para Apple Silicon).

2. **Ejecutar el Instalador**:
   - Haz doble clic en el archivo `.pkg` descargado en el Finder.
   - Sigue las instrucciones en pantalla para instalar Go. Se instalará en `/usr/local/go` por defecto.
   - Es posible que necesites ingresar tu contraseña de administrador.

3. **Configurar las Variables de Entorno**:
   - Abre Terminal y edita tu archivo de configuración de shell (por ejemplo, `~/.zshrc` o `~/.bash_profile`):
     ```bash
     nano ~/.zshrc
     ```
   - Añade las siguientes líneas:
     ```bash
     export GOROOT=/usr/local/go
     export GOPATH=$HOME/go
     export PATH=$GOPATH/bin:$GOROOT/bin:$PATH
     ```
   - Guarda y aplica los cambios:
     ```bash
     source ~/.zshrc
     ```
   - Nota: `GOROOT` es opcional a menos que estés desarrollando Go mismo o necesites una ruta de instalación no estándar. Las versiones modernas de Go a menudo no requieren que se establezca `GOROOT`.

4. **Verificar la Instalación**:
   - Ejecuta:
     ```bash
     go version
     ```
   - Deberías ver la versión de Go instalada (por ejemplo, `go version go1.23.x darwin/amd64`).

5. **Probar la Instalación de Go**:
   - Sigue los mismos pasos que en el Método 1, Paso 5 para crear y ejecutar un programa "Hello, World!".

#### Solución de Problemas del Error Original
Después de instalar Go, regresa a tu directorio `clash-core` y vuelve a intentar el comando `make`:
```bash
cd /path/to/clash-core
make
```

Si encuentras problemas:
- **Configuración del Proxy**: La salida de tu terminal muestra `HTTP_PROXY` y `HTTPS_PROXY` establecidos en `http://127.0.0.1:7890`. Asegúrate de que tu proxy esté activo y no interfiera con el acceso a la red de Go (por ejemplo, descargando dependencias). Puedes desactivar el proxy temporalmente para probar:
  ```bash
  unset HTTP_PROXY HTTPS_PROXY
  make
  ```
- **Permisos**: Si obtienes errores de permisos, asegúrate de tener acceso de escritura al directorio del proyecto y al workspace de Go (`$GOPATH` o `$HOME/go`).
- **Módulos de Go**: Es probable que el proyecto `clash-core` use módulos de Go. Asegúrate de estar en el directorio correcto que contiene `go.mod`, y ejecuta `go mod tidy` para obtener las dependencias antes de `make`:
  ```bash
  go mod tidy
  make
  ```
- **Incompatibilidad de Arquitectura**: El comando `make` está compilando para `linux-amd64` (`GOOS=linux GOARCH=amd64`). Si tienes la intención de ejecutar el binario en macOS, es posible que necesites modificar el Makefile o el comando de compilación para apuntar a `darwin-amd64` (para Macs con Intel) o `darwin-arm64` (para Apple Silicon). Revisa el Makefile para el target `linux-amd64 y ajústalo, o ejecuta:
  ```bash
  GOARCH=amd64 GOOS=darwin CGO_ENABLED=0 go build -trimpath -ldflags '-X "github.com/Dreamacro/clash/constant.Version=1.18" -X "github.com/Dreamacro/clash/constant.BuildTime=Sat Jun 28 12:24:27 UTC 2025" -w -s -buildid=' -o bin/clash-darwin-amd64
  ```
  Reemplaza `amd64` con `arm64` si estás en Apple Silicon.

#### Notas Adicionales
- **Desinstalar Versiones Anteriores de Go**: Si Go estaba instalado previamente, elimínalo para evitar conflictos:
  ```bash
  sudo rm -rf /usr/local/go
  sudo rm -f /etc/paths.d/go
  ```
  Luego reinstala usando uno de los métodos anteriores.
- **Workspace de Go**: Si estableciste `GOPATH`, crea el directorio:
  ```bash
  mkdir -p $HOME/go/{bin,src,pkg}
  ```
  Sin embargo, con los módulos de Go (utilizados por la mayoría de los proyectos modernos como `clash-core`), `GOPATH` es menos crítico.
- **Xcode Command Line Tools**: Algunos proyectos de Go requieren dependencias de C (por ejemplo, `CGO_ENABLED=1`). Instala Xcode Command Line Tools si es necesario:
  ```bash
  xcode-select --install
  ```
- **Múltiples Versiones de Go**: Si necesitas múltiples versiones de Go, considera usar un gestor de versiones como `gvm` (instálalo via Homebrew o script).

#### Verificación
Una vez que Go esté instalado y el comando `make` tenga éxito, el binario `clash-core` debería aparecer en el directorio `bin/` (por ejemplo, `bin/clash-linux-amd64` o `bin/clash-darwin-amd64`). Verifica que funciona ejecutando:
```bash
./bin/clash-darwin-amd64 --version
```

¡Si necesitas más ayuda o te encuentras con errores específicos, házmelo saber con el mensaje de error exacto o el contexto, y puedo proporcionar ayuda más específica!