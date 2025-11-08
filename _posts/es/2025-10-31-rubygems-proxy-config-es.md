---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Configuración de Proxy de RubyGems
translated: true
type: note
---

Para asegurar que `gem` (RubyGems) esté usando tu proxy (por ejemplo, en `http://127.0.0.1:7890`) durante la instalación, sigue estos pasos. Según la salida detallada que compartiste, *parece que ya está usando el proxy*—la línea "Connecting to 127.0.0.1:7890... connected" es un fuerte indicador del cliente HTTP subyacente (probablemente comportamiento de `net/http` o similar a `curl` en modo detallado).

### 1. **Configurar el Proxy (si aún no está configurado)**
   - **Opción A: Usar variables de entorno (recomendado para comandos puntuales o con sudo)**  
     Esto le indica a `gem` que enrute el tráfico a través del proxy. Ejecuta esto antes de tu instalación:
     ```
     export http_proxy=http://127.0.0.1:7890
     export https_proxy=http://127.0.0.1:7890
     sudo -E gem install jekyll bundler --verbose
     ```
     - El flag `-E` preserva tus variables de entorno al usar `sudo`.
     - Para una configuración persistente, añade las líneas `export` a tu `~/.bashrc` o `~/.profile`.

   - **Opción B: Configurar en `~/.gemrc` (a nivel de usuario, no se necesita sudo para futuras instalaciones)**  
     Crea o edita `~/.gemrc`:
     ```
     echo 'http_proxy: http://127.0.0.1:7890' >> ~/.gemrc
     echo 'https_proxy: http://127.0.0.1:7890' >> ~/.gemrc
     ```
     Luego ejecuta `gem install jekyll bundler --verbose` (sin `sudo` si es posible—`sudo` puede ignorar las configuraciones de usuario). Si usas `sudo`, quédate con la Opción A.

### 2. **Verificar que Está Usando el Proxy**
   - **Ejecutar con `--verbose` (como hiciste)**: Busca líneas como:
     - `HEAD https://index.rubygems.org/` seguido de detalles de conexión al proxy.
     - `Connecting to 127.0.0.1:7890... connected.` (esto confirma el uso del proxy).
     - Si muestra conexiones directas a `rubygems.org` (por ejemplo, direcciones IP sin mención del proxy), está omitiendo el proxy.
   
   - **Probar con un dry-run o una búsqueda de información**:
     ```
     gem fetch jekyll --verbose --platform=ruby
     ```
     O simplemente consulta el índice:
     ```
     gem search jekyll --verbose
     ```
     Revisa la salida en busca de conexiones al proxy.

   - **Comprobar las variables de entorno**:
     ```
     echo $http_proxy $https_proxy
     ```
     Si están configuradas correctamente, `gem` debería heredarlas.

   - **Depurar con `gem env`**:
     ```
     gem env
     ```
     Busca en las secciones "HTTP Proxy" o "HTTPS Proxy" la URL de tu proxy.

### Resolución de Problemas
- **Si sudo ignora el proxy**: Usa `sudo -E` o ejecuta sin `sudo` (instala en el directorio del usuario: `gem install --user-install jekyll bundler`).
- **¿No hay líneas de conexión?** Tu proxy podría no tener la verbosidad activada, o las variables de entorno no están configuradas. Prueba el proxy por separado: `curl -v https://rubygems.org/` (debería mostrar saltos por el proxy).
- **¿Proxy corporativo/estricto?** Si requiere autenticación, usa `http://usuario:contraseña@127.0.0.1:7890`.
- **¿Sigue fallando?** Desactiva el proxy temporalmente (`unset http_proxy https_proxy`) y vuelve a intentarlo—si funciona sin él, el problema es de configuración; si no, revisa tu servidor proxy (por ejemplo, los registros/logs de Clash/V2Ray).

Tu instalación tuvo éxito (respuestas 200 OK), así que probablemente esté bien—solo confirma que la próxima ejecución muestre la conexión al proxy para mayor tranquilidad. ¡Si compartes más salida, puedo ayudar a depurar más a fondo