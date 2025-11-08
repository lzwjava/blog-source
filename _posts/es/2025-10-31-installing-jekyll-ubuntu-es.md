---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Instalación de Jekyll en Ubuntu
translated: true
type: note
---

### Configuración y ejecución de Jekyll en Ubuntu

Basándome en tu error ("Comando 'bundle' no encontrado") y los comandos que estás intentando ejecutar, parece que primero necesitas instalar Ruby, Bundler y Jekyll correctamente. Ubuntu no los incluye por defecto, pero es sencillo siguiendo la guía oficial de Jekyll. Te guiaré a través de la configuración completa paso a paso, y luego cómo ejecutar tus comandos específicos.

#### Paso 1: Instalar las dependencias del sistema
Abre tu terminal y ejecuta esto para instalar Ruby y las herramientas de compilación (esto incluye Ruby 3.x a través de `ruby-full`):

```bash
sudo apt update
sudo apt install ruby-full build-essential zlib1g-dev
```

- Esto configura Ruby (verifica con `ruby -v`—debería mostrar algo como 3.0+).
- Si estás en una versión reciente de Ubuntu (ej., 22.04+), esto funciona sin problemas. Evita usar Snap para Ruby si es posible, ya que puede causar problemas de ruta.

#### Paso 2: Configurar un directorio de gemas de usuario (recomendado para evitar Sudo)
Para instalar gemas sin privilegios de root (evita errores de permisos más adelante):

```bash
echo '# Install Ruby Gems to ~/gems' >> ~/.bashrc
echo 'export GEM_HOME="$HOME/gems"' >> ~/.bashrc
echo 'export PATH="$HOME/gems/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

- Verifica: Ejecuta `gem env`—debería mostrar tu `GEM_HOME` como `~/gems`.

#### Paso 3: Instalar Jekyll y Bundler
Ahora instala las herramientas:

```bash
gem install jekyll bundler
```

- Esto agrega los comandos `gem`, `jekyll` y `bundle` a tu ruta.
- Si obtienes errores de permisos, verifica el Paso 2 o usa `sudo` temporalmente (pero evítalo a largo plazo).

#### Paso 4: Crear y ejecutar tu blog
Ahora puedes ejecutar los comandos de tu fragmento. Explicaré cada uno:

1. **Crear un nuevo sitio Jekyll**:
   ```bash
   jekyll new myblog
   ```
   - Esto genera un sitio básico en una carpeta `myblog`.

2. **Entrar al directorio**:
   ```bash
   cd myblog
   ```

3. **Instalar dependencias** (aquí es donde falló tu `bundle install` original—ahora debería funcionar):
   ```bash
   bundle install
   ```
   - Obtiene gemas como los plugins de Jekyll.

4. **Servir el sitio** (inicia un servidor local en http://127.0.0.1:4000):
   ```bash
   bundle exec jekyll serve
   ```
   - Abre tu navegador en esa URL para ver tu sitio.

5. **Servir con reconstrucción incremental** (más rápido para desarrollo, solo reconstruye archivos cambiados):
   ```bash
   bundle exec jekyll serve --incremental
   ```

6. **Servir incluyendo borradores** (muestra posts no publicados):
   ```bash
   bundle exec jekyll serve --draft
   ```

7. **Si obtienes un error "webrick"** (común en Ruby 3+, ya que no está incluido por defecto):
   ```bash
   bundle add webrick
   ```
   - Luego reinicia el comando serve: `bundle exec jekyll serve`.
   - Alternativamente, agrega `gem "webrick"` a tu `Gemfile` y ejecuta `bundle install`.

8. **Servir rápidamente sin Bundler** (si omites `bundle exec`):
   ```bash
   jekyll serve
   ```
   - Pero usa `bundle exec` para consistencia en los proyectos.

#### Resolución de problemas
- **¿Sigue apareciendo "bundle not found"?** Asegúrate de que el Paso 2 haya cargado tu `~/.bashrc` correctamente (`source ~/.bashrc`), luego reinicia tu terminal o ejecuta `hash -r`. Verifica con `which bundle`.
- **¿Problemas de permisos con las gemas?** Mantén la configuración del directorio de usuario del Paso 2.
- **¿Versión de Ruby demasiado antigua?** Si `ruby -v` es <3.0, considera usar rbenv para una versión más nueva (instala via `curl -fsSL https://github.com/rbenv/rbenv-installer/raw/HEAD/bin/rbenv-installer | bash`, luego `rbenv install 3.2.0`).
- **¿El firewall bloquea el puerto 4000?** Ubuntu usualmente no lo hace, pero prueba con `curl http://127.0.0.1:4000`.
- Tu proyecto está en `~/projects/blog-source`—ejecuta estos comandos desde allí o ajusta las rutas.

Una vez servido, edita archivos en `_posts/` o `_config.yml` y guarda—Jekyll se reconstruye automáticamente. Para producción, compila con `jekyll build` y despliega en GitHub Pages o Netlify.

[Jekyll Ubuntu Installation Guide](https://jekyllrb.com/docs/installation/ubuntu/)