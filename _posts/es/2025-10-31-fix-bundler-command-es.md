---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Solucionar Comando Bundler No Encontrado
translated: true
type: note
---

### Comprender el Problema
Tu comando `gem install jekyll bundler` tuvo éxito (instaló 30 gems, incluyendo Bundler 2.7.2), pero el comando `bundle` no se encuentra. Este es un problema común de PATH/entorno en sistemas Ubuntu/Debian después de un `sudo gem install` a nivel del sistema. Las gems instalan binarios en `/usr/local/bin` (o similar), pero es posible que el `$PATH` de tu shell no lo incluya, o el cambio no se haya propagado (por ejemplo, necesitas recargar tu perfil).

La sugerencia del sistema de `apt install ruby-bundler` instalaría una versión más antigua (2.4.20) via apt, lo que podría generar conflicto con tu Bundler 2.7.2 instalado via gem—evita eso por ahora. Lo mismo para snap; podría aislar Ruby de una manera que rompa las rutas de las gems.

### Solución Rápida: Verificar y Usar el Bundler Instalado
1. **Verifica dónde está instalado `bundle`**:
   ```
   gem environment
   ```
   - Busca "EXECUTABLE DIRECTORY" (probablemente `/usr/local/bin`). Toma nota de esa ruta.

2. **Localiza y prueba `bundle` directamente**:
   ```
   which bundle  # Si no devuelve nada, prueba: find /usr/local -name bundle 2>/dev/null
   /usr/local/bin/bundle --version  # Debería mostrar "Bundler version 2.7.2"
   ```
   - Si funciona, ¡genial! Usa la ruta completa por ahora: `/usr/local/bin/bundle install`

3. **Ejecuta tu configuración de Jekyll con la ruta completa**:
   - En `~/projects/blog-source` (asumiendo que tiene un `Gemfile`):
     ```
     /usr/local/bin/bundle install
     /usr/local/bin/bundle exec jekyll serve
     ```
   - Esto debería instalar las dependencias de Jekyll e iniciar el servidor (usualmente en http://127.0.0.1:4000).

### Solución Permanente: Actualizar tu PATH
Si `/usr/local/bin` no está en tu `$PATH`, agrégalo:
1. Edita `~/.bashrc` (o `~/.profile` para shells de login):
   ```
   nano ~/.bashrc
   ```
   Agrega esta línea al final:
   ```
   export PATH="/usr/local/bin:$PATH"
   ```

2. Recarga tu shell:
   ```
   source ~/.bashrc
   ```

3. Verifica:
   ```
   echo $PATH  # Ahora debería incluir /usr/local/bin
   bundle --version  # Debería funcionar sin la ruta completa
   ```

Ahora vuelve a intentar:
```
bundle install
bundle exec jekyll serve
```

### Si Eso No Funciona
- **¿Problemas de permisos?** (Poco común, pero sudo puede causarlos). Reinstala sin sudo (instalación a nivel de usuario):
  ```
  gem install --user-install bundler jekyll
  ```
  Luego agrega `export PATH="$HOME/.local/share/gem/ruby/*/bin:$PATH"` a `~/.bashrc` (ajusta la ruta según la salida de `gem environment`).

- **¿Desajuste de versión de Ruby?** Verifica con `ruby --version`. Si es el Ruby del sistema (ej. 2.7.x), considera usar gestores de versiones de Ruby como `rbenv` (instala via `curl -fsSL https://github.com/rbenv/rbenv-installer/raw/HEAD/bin/rbenv-installer | bash`, luego sigue la configuración). Esto evita conflictos con el sistema a largo plazo.

- **¿Proxy aún activo?** Si tus variables de entorno (`http_proxy`, etc.) están configuradas, Bundler debería heredarlas—solo asegúrate de que estén exportadas antes de ejecutar.

Tu configuración debería ejecutarse sin problemas después del ajuste del PATH. Si encuentras errores (por ejemplo, comparte la salida de `gem environment`), ¡pégalos para obtener ayuda más específica!