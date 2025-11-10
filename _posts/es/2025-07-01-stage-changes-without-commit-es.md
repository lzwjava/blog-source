---
audio: false
generated: true
lang: es
layout: post
title: Cambios de Etapa en el Gancho de Preconfirmación
translated: true
type: note
---

Para integrar los cambios del script `update_notes_link.py` en el commit actual (en lugar de crear un commit separado) durante un hook de pre-commit, necesitas modificar el hook para que prepare (stage) los archivos actualizados sin confirmarlos por separado. De esta manera, los cambios del script de Python se incluirán en el commit del usuario. A continuación, proporciono un script revisado para el hook de pre-commit que logra esto.

### Cambios Clave
- **Sin Commit Separado**: En lugar de ejecutar `git commit` en el hook, el script solo preparará los archivos actualizados (`git add`) para que se incluyan en el commit del usuario.
- **Preservar el Mensaje de Commit del Usuario**: El hook no creará un nuevo commit, asegurando que se utilice el mensaje de commit original del usuario.
- **Manejo de Errores**: Si el script de Python falla, el hook terminará con un estado distinto de cero para evitar el commit.

### Script del Hook de Pre-Commit

Aquí está el script actualizado del hook de pre-commit que prepara los cambios sin crear un commit separado:

```x-shellscript
#!/bin/bash

# Ejecutar el script update_notes_link.py y capturar su salida
OUTPUT=$(python scripts/generate/update_notes_link.py 2>&1)
EXIT_CODE=$?

# Verificar si el script de Python se ejecutó correctamente
if [ $EXIT_CODE -ne 0 ]; then
    echo "Error: update_notes_link.py falló con código de salida $EXIT_CODE"
    echo "$OUTPUT"
    exit 1
fi

# Verificar si el archivo específico fue actualizado
if echo "$OUTPUT" | grep -q "Updated original/2025-01-11-notes-en.md"; then
    echo "Enlaces de notas actualizados, preparando cambios para el commit actual."

    # Preparar los archivos relevantes
    git add original/2025-01-11-notes-en.md
    git add _posts/en/*.md

    # Verificar que los archivos fueron preparados
    if ! git diff --cached --quiet; then
        echo "Cambios preparados exitosamente."
    else
        echo "No hay cambios para preparar."
    fi
else
    echo "No hay actualizaciones para original/2025-01-11-notes-en.md, no se prepararon archivos adicionales."
fi

# Salir con éxito para permitir que el commit proceda
exit 0
```

### Explicación del Script

- **Shebang (`#!/bin/bash`)**: Asegura que el script se ejecute en un shell Bash.
- **Ejecutar Script Python**: Ejecuta `python scripts/generate/update_notes_link.py` y captura su salida y código de salida.
- **Manejo de Errores**: Verifica el código de salida (`$EXIT_CODE`) del script de Python. Si es distinto de cero, el hook falla, imprime el error y detiene el commit.
- **Verificar Salida**: Usa `grep` para verificar si la salida indica que `original/2025-01-11-notes-en.md` fue actualizado.
- **Preparar Archivos**: Ejecuta `git add` en los archivos especificados (`original/2025-01-11-notes-en.md` y `_posts/en/*.md`) para incluirlos en el commit del usuario.
- **Sin Commit**: Omite `git commit`, permitiendo que el comando `git commit` del usuario incluya los cambios preparados con su mensaje de commit original.
- **Retroalimentación**: Imprime mensajes para informar al usuario si se prepararon cambios.
- **Código de Salida**: Termina con `0` para permitir que el commit proceda, a menos que el script de Python falle.

### Configurar el Hook

1. **Crear el Hook**:
   - Coloca el script en `.git/hooks/pre-commit` en tu repositorio.

2. **Hacerlo Ejecutable**:
   ```bash
   chmod +x .git/hooks/pre-commit
   ```

3. **Probar el Hook**:
   - Modifica un archivo o asegúrate de que el script de Python actualizará `original/2025-01-11-notes-en.md`.
   - Ejecuta `git commit -m "Tu mensaje de commit"`.
   - Verifica que los archivos actualizados se incluyan en el commit revisando `git diff --cached` antes de confirmar o `git show` después de confirmar.

### Usar el Framework `pre-commit` (Opcional)

Si prefieres usar el framework `pre-commit`, puedes definir la misma lógica en un archivo `.pre-commit-config.yaml`. Este enfoque es más portable y te permite especificar qué archivos activan el hook.

1. **Instalar pre-commit**:
   ```bash
   pip install pre-commit
   ```

2. **Crear `.pre-commit-config.yaml`**:

```yaml
repos:
- repo: local
  hooks:
  - id: update-notes-links
    name: Update Notes Links
    entry: bash -c '
      OUTPUT=$(python scripts/generate/update_notes_link.py 2>&1);
      EXIT_CODE=$?;
      if [ $EXIT_CODE -ne 0 ]; then
        echo "Error: update_notes_link.py failed with exit code $EXIT_CODE";
        echo "$OUTPUT";
        exit 1;
      fi;
      if echo "$OUTPUT" | grep -q "Updated original/2025-01-11-notes-en.md"; then
        echo "Notes links updated, staging changes for the current commit.";
        git add original/2025-01-11-notes-en.md;
        git add _posts/en/*.md;
        if ! git diff --cached --quiet; then
          echo "Changes staged successfully.";
        else
          echo "No changes to stage.";
        fi;
      else
        echo "No updates to original/2025-01-11-notes-en.md, no additional files staged.";
      fi'
    language: script
    files: ^(original/2025-01-11-notes-en\.md|_posts/en/.*\.md)$
    stages: [commit]
```

3. **Instalar el Hook**:
   ```bash
   pre-commit install
   ```

4. **Probar el Hook**:
   - Confirma cambios en archivos que coincidan con la regex `files` (por ejemplo, `original/2025-01-11-notes-en.md` o `_posts/en/*.md`).
   - Verifica que el hook se ejecute, prepare los cambios si es aplicable y los incluya en tu commit.

### Diferencias Clave de las GitHub Actions Originales

- **Sin Commit Separado**: A diferencia del flujo de trabajo de GitHub Actions, que creaba un nuevo commit, este hook prepara los cambios para el commit actual del usuario.
- **Sin Push**: El hook no sube (push) los cambios, ya que los hooks de pre-commit se ejecutan localmente antes de que el commit se finalice. El usuario debe ejecutar `git push` manualmente.
- **Manejo de Errores**: El hook verifica el código de salida del script de Python para asegurarse de que no falle silenciosamente.
- **Sin Configuración de Usuario de Git**: El script omite `git config user.name` y `user.email` ya que se usará la configuración de Git del usuario para el commit.

### Notas

- **Script Python**: Asegúrate de que `scripts/generate/update_notes_link.py` exista y sea ejecutable localmente. Si depende de variables de entorno o dependencias, asegúrate de que estén disponibles.
- **Rutas de Archivos**: Verifica que las rutas `original/2025-01-11-notes-en.md` y `_posts/en/*.md` coincidan con la estructura de tu repositorio.
- **Fallo del Hook**: Si el script de Python falla, el hook evitará el commit, asegurando que no se preparen actualizaciones parciales.
- **Pruebas**: Prueba con `git commit` para confirmar que los cambios se preparan y se incluyen en el commit sin crear un commit extra. Usa `git show` para inspeccionar el contenido del commit.

### Verificación

Para verificar:
1. Modifica un archivo o asegúrate de que el script de Python actualice `original/2025-01-11-notes-en.md`.
2. Ejecuta `git commit -m "Commit de prueba"`.
3. Revisa `git show` para confirmar que los archivos actualizados se incluyan en el commit con tu mensaje original.
4. Asegúrate de que no se creen commits adicionales (por ejemplo, ningún commit `chore(notes): Update notes links`).

Si necesitas ajustes adicionales, como manejar casos de error específicos o agregar más archivos para preparar, ¡avísame!