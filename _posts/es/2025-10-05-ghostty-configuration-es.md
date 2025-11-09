---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Comprensión del Archivo de Configuración de Ghostty
translated: true
type: note
---

### Cómo funciona el archivo de configuración de Ghostty

El archivo de configuración de Ghostty utiliza un formato de texto simple con pares clave-valor al estilo de `clave = valor`. Está diseñado para ser sencillo, permitiéndote anular solo los valores predeterminados que te interesen—Ghostty incluye valores predeterminados sensatos para todo lo demás, por lo que un archivo de configuración mínimo o incluso vacío funciona correctamente.

#### Desglose rápido de la sintaxis
- **Claves y valores**: Las claves siempre están en minúsculas y distinguen entre mayúsculas y minúsculas (ej., `font-family = JetBrains Mono`). Los valores pueden ir sin comillas a menos que contengan espacios o caracteres especiales (ej., `font-family = "JetBrains Mono Nerd Font"`). Los espacios alrededor del `=` no importan.
- **Comentarios**: Inicia una línea con `#` para notas (ej., `# Mi tema personalizado`). No hay comentarios en línea después de los valores, o se interpretarán como parte del valor.
- **Restablecer al valor predeterminado**: Usa un valor vacío como `clave =` para revertir una configuración al valor predeterminado integrado de Ghostty.
- **Valores especiales**: Algunas opciones tienen formatos únicos, como las duraciones (ej., `resize-overlay-duration = 4s 200ms`)—consulta la documentación para los detalles específicos.
- **Carga del archivo**: Ghostty busca la configuración en `~/.config/ghostty/config` (Linux/Windows) o `~/Library/Application Support/com.mitchellh.ghostty/config` (macOS). Puedes incluir otros archivos con `config-file = ruta/a/otro.conf` para configuraciones modulares.
- **Anulaciones por CLI**: Cualquier configuración también se puede establecer mediante banderas de línea de comandos (ej., `ghostty --font-family="Fira Code"`), las cuales tienen prioridad sobre el archivo.

Los cambios surten efecto inmediatamente si recargas con la combinación de teclas predeterminada (Cmd+Shift+, en macOS o Ctrl+Shift+, en Linux/Windows) o ejecutando `ghostty +reload-config`.

Para ver todas las opciones y valores predeterminados, ejecuta `ghostty +show-config --default --docs` en tu terminal.

### ¿Qué es una configuración normal?
Una configuración "normal" suele ser mínima—solo ajusta algunas cosas como la fuente, los colores o el relleno para mayor comodidad. Los valores predeterminados de Ghostty incluyen JetBrains Mono como familia de fuentes (con soporte integrado para Nerd Font), un esquema limpio de fondo/primer plano y sin relleno adicional.

Aquí tienes un ejemplo simple y típico para una configuración con tema oscuro, una fuente popular, algo de relleno y enlaces de teclado básicos. Guarda esto como tu archivo `config`:

```
# Tema oscuro básico con relleno y fuente personalizada
background = 1e1e1e
foreground = f8f8f2
font-family = "JetBrains Mono Nerd Font"
font-size = 14

# Añade un poco de espacio alrededor del texto
window-padding-x = 8
window-padding-y = 8

# Enlaces de teclado personalizados (anula los predeterminados si es necesario)
keybind = cmd+t=new_tab
keybind = cmd+w=close_tab
keybind = cmd+d=new_split:right
```

Esto mantiene las cosas ligeras mientras personaliza lo esencial. Puedes expandirlo con más colores (ej., entradas de la paleta como `color0 = 282a36`) o temas de la documentación.

[Documentación de Configuración de Ghostty](https://ghostty.org/docs/config)