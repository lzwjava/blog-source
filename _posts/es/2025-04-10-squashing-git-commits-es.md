---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: Comprimir confirmaciones de Git por autor
translated: true
type: note
---

### Comprender el Objetivo
Git no tiene un comando incorporado para "combinar (squash) por autor", pero puedes lograrlo usando un rebase interactivo para agrupar y combinar commits manualmente. La idea es tomar los últimos 10 commits (suponiendo que involucran 3 autores distintos) y fusionar los commits de cada autor en un solo commit por autor, resultando en 3 commits en total.

Esto asume:
- Estás en la rama con esos commits (por ejemplo, la rama main o feature).
- Los commits son lineales (sin merges).
- Conoces a los autores de antemano.

Si los commits no son lineales o son complejos, esto puede requerir un manejo cuidadoso para evitar conflictos.

### Pasos para Combinar (Squash) Commits por Autor
1. **Revisar los Últimos 10 Commits**  
   Ejecuta `git log --oneline -10` para ver los últimos 10 commits, incluyendo sus hashes, autores y mensajes. Identifica a los autores (por ejemplo, usando `git log --format="%an" -10 | sort | uniq` para listar autores únicos).

2. **Iniciar un Rebase Interactivo**  
   Identifica el commit anterior al décimo. Si tu commit más reciente está en HEAD, y hay 10 commits, la base es `HEAD~10`. Ejecuta:  
   ```
   git rebase -i HEAD~10
   ```  
   Esto abre un editor (vim por defecto) con una lista de los últimos 10 commits. Se ve así:  
   ```
   pick abc123 Primer commit por Autor A  
   pick def456 Segundo commit por Autor A  
   pick ghi789 Commit por Autor B  
   pick jkl012 Commit por Autor C  
   ... (más commits)
   ```  
   - Cada línea comienza con `pick`.

3. **Marcar Commits para Combinar (Squash) por Autor**  
   Para cada autor, cambia `pick` a `s` (squash) en todos sus commits excepto en el primero que quieras conservar para ese autor. Decide:
   - Un commit "a conservar" por autor (elige el más antiguo o el más relevante como base).
   - Cambia el resto de commits de ese autor a `s` para combinarlos en él.  
   Ejemplo (para 3 autores):  
   ```
   pick abc123 Primer commit por Autor A (conservar este)  
   s    def456 Segundo commit por Autor A (combinar en el anterior)  
   pick ghi789 Commit por Autor B (conservar este)  
   pick jkl012 Primer commit por Autor C (conservar este)  
   s    mno345 Segundo commit por Autor C (combinar en el anterior)  
   ```  
   Guarda y sale del editor. Esto inicia el rebase.

4. **Editar Mensajes de Commit Durante el Rebase**  
   Para cada operación de combinación (squash), Git se pausará y te permitirá editar el mensaje del commit (combinando los que se han fusionado). Actualízalo a algo como "Commits combinados por Autor A: descripción". Guarda y continúa.  
   Si hay más combinaciones, repite para cada autor. Ejecuta `git rebase --continue` después de cada edición.  
   Si surgen conflictos (poco común en una combinación simple), resuélvelos con `git add <archivo>` y luego `git rebase --continue`.

5. **Verificar y Hacer Push**  
   Una vez que el rebase termine, revisa el log: `git log --oneline -10`. Deberías ver 3 commits, uno por cada autor.  
   Haz un force-push si estás enviando a una rama compartida (rebase destructivo): `git push --force-with-lease origin nombre-de-la-rama`.  
   **Advertencia:** Solo haz force-push si estás seguro de que los commits antiguos no se necesitan en otro lugar, ya que esto reescribe el historial.

### Consejos y Advertencias
- Si los autores tienen muchos commits, agrupa eficientemente en la lista del rebase (todos los del Autor A juntos, etc.).
- Para automatización, herramientas como `git-interactive-rebase-tool` o scripts pueden ayudar, pero el rebase manual es directo.
- Si necesitas filtrar por autor exacto, usa `git log --author="Nombre del Autor"` de antemano para confirmar.
- Prueba primero en una rama de respaldo para evitar pérdida de datos.

Para más información sobre rebase: `git help rebase`. Si esto no coincide con tu escenario exacto, proporciona más detalles sobre la estructura de los commits.