---
audio: false
generated: true
lang: es
layout: post
title: Uso de Git Pull y Push con Clonados Superficiales
translated: true
type: note
---

Sí, aún puedes usar `git pull` o `git push` después de clonar un repositorio con un historial limitado usando `--depth=20`. Sin embargo, hay algunas consideraciones importantes a tener en cuenta:

### 1. **Qué hace `--depth=20`**
   - La opción `--depth=20` crea un *clon superficial*, obteniendo solo los 20 commits más recientes (o el número especificado) desde la rama predeterminada (o la rama especificada si usas `--branch`).
   - Esto reduce la cantidad de historial descargado, haciendo que el clon sea más rápido y de menor tamaño, pero el repositorio no contendrá el historial completo de commits.

### 2. **Usar `git pull` con un Clon Superficial**
   - **Sí, puedes usar `git pull`** en un clon superficial para obtener y fusionar nuevos commits desde el repositorio remoto.
   - Por defecto, `git pull` obtendrá nuevos commits y actualizará el historial superficial, manteniéndolo consistente con la rama remota.
   - Si se agregan nuevos commits a la rama remota, `git pull` los obtendrá y extenderá el historial en tu repositorio local, aún respetando la naturaleza superficial del clon.

   **Nota**: Si el historial de la rama cambia de una manera que afecte a commits más antiguos que tu historial superficial (por ejemplo, un `force push` o un `rebase` en el remoto), puedes encontrar problemas. En tales casos, podrías necesitar profundizar el historial (usando `git fetch --deepen=<n>` o `git fetch --unshallow` para obtener el historial completo) para resolver conflictos o continuar trabajando.

### 3. **Usar `git push` con un Clon Superficial**
   - **Sí, puedes usar `git push`** para enviar tus commits locales al repositorio remoto.
   - Un clon superficial no restringe tu capacidad para crear nuevos commits y enviarlos al repositorio remoto, siempre que el remoto acepte tus cambios.
   - Sin embargo, si el repositorio remoto requiere operaciones que dependen del historial completo (por ejemplo, una fusión o un `rebase` que involucre commits más antiguos), es posible que necesites obtener más historial para completar el `push` exitosamente.

### 4. **Limitaciones de los Clones Superficiales**
   - **Historial Limitado**: Algunas operaciones de Git, como `git log`, `git blame` o `git rebase`, pueden estar limitadas porque los commits más antiguos no están disponibles localmente.
   - **Fusiones y Rebases**: Si necesitas fusionar o hacer `rebase` con commits fuera de tu historial superficial, es posible que necesites obtener más historial usando `git fetch --deepen=<n>` o `git fetch --unshallow`.
   - **Force Pushes**: Si la rama remota se reescribe (por ejemplo, con `git push --force`), tu clon superficial podría no tener suficiente contexto para manejar los cambios, requiriendo que profundices el historial o hagas un nuevo clon.

### 5. **Cómo Profundizar un Clon Superficial (Si es Necesario)**
   Si encuentras problemas con `git pull` o `git push` debido al historial limitado, puedes obtener historial adicional:
   - **Profundizar por un número específico de commits**:
     ```bash
     git fetch --deepen=20
     ```
     Esto obtiene 20 commits más de historial.
   - **Obtener el historial completo**:
     ```bash
     git fetch --unshallow
     ```
     Esto convierte tu clon superficial en un clon completo con todo el historial.

### 6. **Consejo Práctico**
   - Un clon superficial con `--depth=20` usualmente es suficiente para la mayoría de los flujos de trabajo, especialmente si solo estás trabajando en cambios recientes o contribuyendo con actualizaciones pequeñas.
   - Si anticipas que necesitarás el historial completo (por ejemplo, para fusiones complejas, `rebases` o depuración), considera clonar el repositorio completo sin la opción `--depth` o profundizar el historial más tarde según sea necesario.
   - Siempre asegúrate de tener acceso de escritura al repositorio remoto (por ejemplo, `git@github.com:cisco/ChezScheme.git`) antes de intentar hacer `push`.

### Ejemplo de Flujo de Trabajo
```bash
# Clonar con historial limitado
git clone git@github.com:cisco/ChezScheme.git --depth=20
cd ChezScheme

# Hacer cambios y commit
git commit -m "Mis cambios"

# Pull de los últimos cambios
git pull origin main

# Push de tus cambios
git push origin main
```

Si encuentras problemas debido al clon superficial, profundiza el historial como se describió anteriormente.

### Resumen
Sí, puedes usar `git pull` y `git push` con un clon superficial creado usando `--depth=20`. Sin embargo, es posible que necesites obtener historial adicional para ciertas operaciones si el historial superficial es insuficiente. Usa `git fetch --deepen` o `git fetch --unshallow` para abordar cualquier limitación.