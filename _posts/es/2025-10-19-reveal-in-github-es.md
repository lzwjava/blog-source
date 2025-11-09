---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Revelar en GitHub Complemento de Xcode
translated: true
type: note
---

### ¿Qué es Reveal-In-GitHub?

Reveal-In-GitHub es un plugin de Xcode que te permite navegar rápidamente desde tu espacio de trabajo en Xcode a funciones clave de GitHub para tu repositorio actual. Está diseñado para desarrolladores que trabajan en proyectos Git alojados en GitHub, permitiendo el acceso con un clic (o atajo de teclado) a elementos como el historial de commits, vistas de blame, pull requests, issues y notificaciones, sin salir de Xcode ni tener que escribir manualmente las URLs.

### Prerrequisitos
- Tener Xcode instalado (probado en versiones recientes; no se menciona una versión mínima específica).
- Tu proyecto debe ser un repositorio Git alojado en GitHub (el plugin detecta automáticamente la URL del repositorio y las rutas de los archivos).
- Si tu proyecto tiene múltiples remotos de Git, se te pedirá que selecciones uno por defecto la primera vez que lo uses.

### Instalación
Hay dos formas principales de instalarlo:

#### Opción 1: Usando Alcatraz (Recomendado)
1. Instala Alcatraz si aún no lo tienes (un gestor de paquetes para plugins de Xcode). Puedes encontrar guías de configuración en línea, como [esta](http://blog.devtang.com/blog/2014/03/05/use-alcatraz-to-manage-xcode-plugins/) si prefieres instrucciones en chino.
2. Abre Alcatraz en Xcode (a través del menú: `Window > Package Manager`).
3. Busca "Reveal In GitHub".
4. Haz clic en **Install**.
5. Reinicia Xcode.

#### Opción 2: Instalación Manual
1. Clona el repositorio:  
   ```
   git clone https://github.com/lzwjava/Reveal-In-GitHub.git
   ```
2. Abre el archivo `Reveal-In-GitHub.xcodeproj` en Xcode.
3. Compila el proyecto (Product > Build o ⌘B). Esto genera el archivo `Reveal-In-GitHub.xcplugin`.
4. Mueve el plugin a:  
   `~/Library/Application Support/Developer/Shared/Xcode/Plug-ins/`
5. Reinicia Xcode.

Después de la instalación, el plugin debería aparecer en la barra de menús de Xcode bajo **Editor > Reveal In GitHub**.

### Cómo Usarlo
Una vez instalado y reiniciado Xcode:
1. Abre un proyecto alojado en GitHub en Xcode y edita un archivo fuente (por ejemplo, navega a una línea específica).
2. Usa uno de los atajos de teclado o elementos del menú bajo **Editor > Reveal In GitHub** para saltar a GitHub. El plugin detecta automáticamente tu repositorio, el archivo actual, el número de línea y el hash del commit más reciente.

Aquí tienes una referencia rápida de los elementos de menú y atajos integrados (los atajos siguen el patrón ⌃⇧⌘ + primera letra del título):

| Elemento del Menú | Atajo       | Qué Hace | Ejemplo de URL en GitHub (para el archivo LZAlbumManager.m en la línea 40 en el repo lzwjava/LZAlbum en el commit fd7224) |
|-------------------|-------------|----------|----------------------------------------------------------------------------------------------------------------------|
| **Setting**       | ⌃⇧⌘S      | Abre el panel de personalización | N/A |
| **Repo**          | ⌃⇧⌘R      | Abre la página principal del repositorio | https://github.com/lzwjava/LZAlbum |
| **Issues**        | ⌃⇧⌘I      | Abre la lista de issues | https://github.com/lzwjava/LZAlbum/issues |
| **PRs**           | ⌃⇧⌘P      | Abre la lista de pull requests | https://github.com/lzwjava/LZAlbum/pulls |
| **Quick File**    | ⌃⇧⌘Q      | Abre la vista del archivo en la línea actual | https://github.com/lzwjava/LZAlbum/blob/fd7224/LZAlbum/manager/LZAlbumManager.m#L40 |
| **List History**  | ⌃⇧⌘L     | Abre el historial de commits del archivo | https://github.com/lzwjava/LZAlbum/commits/fd7224/LZAlbum/manager/LZAlbumManager.m |
| **Blame**         | ⌃⇧⌘B      | Abre la vista de blame para la línea actual | https://github.com/lzwjava/LZAlbum/blame/fd7224/LZAlbum/manager/LZAlbumManager.m#L40 |
| **Notifications** | ⌃⇧⌘N   | Abre las notificaciones del repositorio | https://github.com/lzwjava/LZAlbum/notifications?all=1 |

- **Consejos**:
  - Los atajos no entran en conflicto con los valores por defecto de Xcode.
  - Si tienes un rango de texto seleccionado, algunas acciones (como Blame) se anclarán a ese rango (ej., #L40-L43).
  - Pruébalo: Abre un proyecto, ve a una línea y pulsa ⌃⇧⌘B; debería abrir la página de blame en tu navegador.

### Personalización
Para ajustar o añadir elementos de menú:
1. Pulsa ⌃⇧⌘S o ve a **Editor > Reveal In GitHub > Setting**.
2. En el panel:
   - Añade nuevos elementos haciendo clic en el botón "+": Introduce un título (ej., "Wiki"), un atajo y un patrón de URL.
   - Los patrones de URL usan marcadores como:
     - `{git_remote_url}`: URL completa del repositorio (ej., https://github.com/usuario/repo).
     - `{commit}`: Hash del commit más reciente de la rama actual.
     - `{file_path}`: Ruta relativa al archivo.
     - `#{selection}`: Línea o selección actual (ej., #L40).
   - Ejemplo: Para un enlace a la wiki, establece el patrón como `{git_remote_url}/wiki`.
3. Si tienes múltiples remotos, usa el botón "Clear Default Repos" para restablecer las selecciones.

El plugin está inspirado en [ShowInGitHub](https://github.com/larsxschneider/ShowInGitHub) y tiene licencia MIT.

[Repositorio de Reveal-In-GitHub en GitHub](https://github.com/lzwjava/Reveal-In-GitHub)