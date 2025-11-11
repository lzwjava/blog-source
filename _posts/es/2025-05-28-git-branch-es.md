---
audio: false
generated: true
lang: es
layout: post
title: Herramientas de Visualización de Ramas de Git
translated: true
type: note
---

Para visualizar múltiples ramas en un repositorio Git en Windows, puedes usar TortoiseGit u otras herramientas para mostrar un gráfico de ramas seleccionadas. El Gráfico de Revisiones de TortoiseGit es potente pero puede resultar abrumador cuando muestra todas las ramas. A continuación se detallan los pasos para ver un gráfico de varias ramas específicas usando TortoiseGit, junto con herramientas alternativas para mayor flexibilidad.

### Usando TortoiseGit para Ver Múltiples Ramas
El Gráfico de Revisiones de TortoiseGit puede mostrar múltiples ramas, pero no permite seleccionar ramas específicas directamente en la interfaz. Sin embargo, puedes filtrar la vista para centrarte en las ramas relevantes.

1.  **Abrir Gráfico de Revisiones**:
    *   Navega a la carpeta de tu repositorio en el Explorador de Windows.
    *   Haz clic derecho en la carpeta, selecciona **TortoiseGit** > **Revision Graph**.
    *   Esto muestra un gráfico de todas las referencias (ramas, tags, etc.) por defecto, lo que puede ser desordenado si tienes muchas ramas.

2.  **Filtrar Ramas Específicas**:
    *   En la ventana del Gráfico de Revisiones, usa las **opciones de filtro** para reducir el desorden:
        *   Ve al menú **View** y selecciona **Show branchings and mergings** para enfatizar las relaciones entre ramas.
        *   Para centrarte en ramas específicas, haz clic derecho en un commit y selecciona **Show Log** para ver el diálogo de registro, donde puedes activar/desactivar **View > Labels > Local branches** o **Remote branches** para mostrar solo las referencias relevantes.
    *   Alternativamente, usa la opción **Walk Behavior > Compressed Graph** en el diálogo de registro para simplificar el gráfico, mostrando solo puntos de merge y commits con referencias (como las puntas de las ramas).

3.  **Navegar por el Gráfico**:
    *   Usa la **ventana de vista general** para navegar por gráficos grandes arrastrando el área resaltada.
    *   Pasa el cursor sobre un nodo de revisión para ver detalles como la fecha, el autor y los comentarios.
    *   Haz Ctrl+clic en dos revisiones para compararlas a través del menú contextual (por ejemplo, **Compare Revisions**).

4.  **Limitaciones**:
    *   El Gráfico de Revisiones de TortoiseGit muestra todas las ramas a menos que se filtren, y no hay una opción directa para seleccionar solo ramas específicas en la vista de gráfico.
    *   Para una vista más limpia, considera las herramientas alternativas que se mencionan a continuación.

### Herramientas Alternativas para Ver Múltiples Ramas
Si la interfaz de TortoiseGit es demasiado limitada para seleccionar ramas específicas, prueba estas herramientas, que ofrecen más control sobre la visualización de ramas:

#### 1. **Visual Studio Code con la Extensión Git Graph**
*   **Instalar**: Descarga Visual Studio Code e instala la extensión **Git Graph**.
*   **Uso**:
    *   Abre tu repositorio en VS Code.
    *   Accede a la vista Git Graph desde la pestaña Control de Código Fuente o la paleta de comandos (`Ctrl+Shift+P`, escribe "Git Graph").
    *   Selecciona ramas específicas para mostrar en el gráfico haciendo clic en los nombres de las ramas en la interfaz.
    *   El gráfico muestra commits, ramas y merges con líneas codificadas por colores para mayor claridad.
*   **Beneficios**: Ligero, gratuito y permite seleccionar múltiples ramas de forma interactiva. Admite la comparación de commits y operaciones básicas de Git.

#### 2. **SourceTree**
*   **Instalar**: Descarga SourceTree (gratuito) para Windows.
*   **Uso**:
    *   Abre tu repositorio en SourceTree.
    *   La vista **History** muestra una representación gráfica de las ramas y los commits.
    *   Usa la lista de ramas a la izquierda para activar/desactivar la visibilidad de ramas específicas, centrándote solo en las que quieres ver.
    *   Haz clic derecho en ramas o commits para acciones como merge o compare.
*   **Beneficios**: Visualización clara de ramas con colores consistentes y funciones interactivas como arrastrar y soltar para hacer merge.

#### 3. **GitKraken**
*   **Instalar**: Descarga GitKraken (gratuito para proyectos de código abierto, de pago para repositorios privados).
*   **Uso**:
    *   Abre tu repositorio en GitKraken.
    *   El gráfico central muestra todas las ramas, con opciones para ocultar/mostrar ramas específicas a través de la lista de ramas.
    *   Haz clic en las etiquetas de las ramas para centrarte en ramas específicas o usa la búsqueda para filtrar commits.
*   **Beneficios**: Intuitivo y visualmente atractivo, con colores consistentes para las ramas y funciones avanzadas como resolución de conflictos.

#### 4. **Línea de Comandos con `git log`**
*   Si prefieres una solución basada en terminal, usa la vista de gráfico integrada de Git:
    ```bash
    git log --graph --oneline --decorate --branches=<branch1> --branches=<branch2>
    ```
    Reemplaza `<branch1>` y `<branch2>` con los nombres de las ramas que quieres visualizar (por ejemplo, `feature1`, `feature2`). Usa `--branches=*` para todas las ramas o especifica múltiples ramas explícitamente.
*   **Alias para Conveniencia**:
    Crea un alias de Git para un acceso más fácil:
    ```bash
    git config --global alias.tree "log --graph --oneline --decorate --branches="
    ```
    Luego ejecuta `git tree feature1 feature2` para ver un gráfico de solo esas ramas.
*   **Beneficios**: No se necesita software adicional y puedes especificar ramas exactas. La salida es basada en texto pero clara para repositorios pequeños.

### Recomendaciones
*   **Para simplicidad e integración**: Usa **VS Code con Git Graph** para una solución ligera y gratuita que te permite seleccionar ramas específicas.
*   **Para visualización avanzada**: Usa **GitKraken** o **SourceTree** para una GUI más pulida con selección interactiva de ramas y colores consistentes.
*   **Para usuarios de TortoiseGit**: Quédate con el Gráfico de Revisiones y usa filtros como **Compressed Graph** o **Show branchings and mergings** para centrarte en las ramas clave, pero ten en cuenta sus limitaciones para seleccionar ramas específicas.
*   **Para usuarios de terminal**: Usa el comando `git log` con filtros de ramas específicos para una visualización rápida y precisa sin herramientas adicionales.

Si tienes un gran número de ramas, GitKraken o SourceTree son probablemente las mejores opciones para visualizar selectivamente solo las ramas que te interesan, ya que ofrecen una activación/desactivación intuitiva de ramas. ¡Avísame si necesitas ayuda para configurar alguna de estas herramientas o alguna aclaración adicional!