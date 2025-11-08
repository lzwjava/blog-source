---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Solucionar Errores de Permiso de Bundler
translated: true
type: note
---

### Comprender el Error

Este es un problema común de permisos al usar Bundler (el gestor de dependencias de Ruby) con una instalación de Ruby del sistema (versión 3.2.0 en este caso). El error ocurre porque Bundler intenta descargar y almacenar en caché la gema `rake` (y potencialmente otras) en el directorio de gemas del sistema en `/var/lib/gems/3.2.0/cache/`, lo que requiere permisos de escritura a nivel de root. El propio Bundler está instalado localmente para el usuario (en `~/.local/share/gem/`), pero por defecto está utilizando las rutas de gemas del sistema para las instalaciones.

Esta cadena en tu `Gemfile` (Jekyll + dependencias como `minima`, `jekyll-feed`, etc.) simplemente está activando la instalación de `rake` como una dependencia profunda—no hay nada malo en tu configuración, solo son los permisos.

### Soluciones Rápidas (en orden de recomendación)

1.  **Instalar Gemas Localmente (Recomendado - No se Necesita Sudo)**
    Esto mantiene todo en tu directorio personal, evitando completamente las rutas del sistema. Ejecuta:
    ```
    bundle config set --local path 'vendor/bundle'
    bundle install
    ```
    - Esto crea una carpeta `vendor/bundle` en tu proyecto para las gemas.
    - Para ejecutar tu sitio de Jekyll más tarde, usa `bundle exec jekyll serve` (el `exec` asegura que use las gemas locales).
    - Si quieres que esto sea global para todos los proyectos: Reemplaza `--local` con `--global` y usa `~/.bundle` como la ruta.

2.  **Usar Sudo (Rápido pero No Ideal)**
    Si necesitas una instalación única y no te importan las gemas instaladas en todo el sistema:
    ```
    sudo bundle install
    ```
    - **Advertencia**: Esto instala las gemas globalmente como root, lo que puede causar problemas de propiedad más adelante (por ejemplo, necesitarías `sudo` para futuras actualizaciones). Evítalo si es posible.

3.  **Corregir Permisos del Sistema (Avanzado - Usar con Precaución)**
    Si quieres seguir usando el directorio de gemas del sistema sin sudo:
    ```
    sudo chown -R $USER:$USER /var/lib/gems/3.2.0/
    ```
    - Luego, vuelve a intentar `bundle install`.
    - **Advertencia**: Esto cambia la propiedad de las gemas del sistema, lo que podría romper paquetes gestionados por tu distribución (por ejemplo, Ubuntu). Solo haz esto si te sientes cómodo solucionando problemas.

### Recomendación a Largo Plazo
Para el desarrollo con Ruby/Jekyll, cambia a un instalador de Ruby gestionado por el usuario como [rbenv](https://github.com/rbenv/rbenv) o [RVM](https://rvm.io/). Esto evita todos los dolores de cabeza con los permisos instalando Ruby y las gemas completamente en tu directorio personal:
- Instala rbenv: Sigue la [guía oficial](https://github.com/rbenv/rbenv#installation).
- Luego: `rbenv install 3.2.0 && rbenv global 3.2.0 && gem install bundler`.
- Vuelve a intentar `bundle install`—funcionará sin problemas.

Si ninguna de estas opciones lo resuelve o encuentras otro error, ¡comparte la salida de `ruby -v`, `gem env` y tu `Gemfile.lock` (si existe) para obtener ayuda más específica