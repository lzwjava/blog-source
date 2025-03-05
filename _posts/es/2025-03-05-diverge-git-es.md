---
audio: false
generated: true
lang: es
layout: post
title: Ramas de Git Divergentes
translated: true
---

Cuando tu rama local `main` y la rama remota `origin/main` han divergido en Git—con 74 y 70 commits diferentes respectivamente—significa que comparten un ancestro común pero han desarrollado commits únicos desde entonces. Tu objetivo es hacer que tu rama local `main` coincida con `origin/main` restableciendo tu rama local al ancestro común (el "padre de ambos") y luego usando `git pull` para traer los cambios remotos, descartando efectivamente tus commits locales divergentes en favor de los remotos. A continuación se presentan los pasos para lograr esto.

### Pasos para Solucionar la Divergencia

1. **Obtener los Cambios Remotos Más Recientes**
   Comienza asegurándote de que tu repositorio local tenga la información más reciente del remoto. Esto actualiza tu referencia a `origin/main` sin alterar tu rama local `main` aún.

   ```bash
   git fetch origin
   ```

2. **Encontrar el Commit Ancestro Común**
   Usa `git merge-base` para identificar el commit ancestro común entre tu `main` local y `origin/main`. Este es el punto donde las ramas divergieron.

   ```bash
   ancestor=$(git merge-base main origin/main)
   ```

   Este comando almacena el hash del commit ancestro común en la variable `ancestor`.

3. **Restablecer `main` Local al Ancestro Común**
   Restablece tu rama local `main` al commit ancestro común. La opción `--hard` asegura que tanto el puntero de la rama como tu directorio de trabajo se actualicen, descartando todos los commits y cambios locales hechos después de este punto.

   ```bash
   git reset --hard $ancestor
   ```

   **Cuidado**: Este paso descartará todos los cambios sin confirmar en tu directorio de trabajo y área de preparación, así como los 74 commits únicos de tu `main` local. Si necesitas preservar estos, considera crear una rama de respaldo primero (ver "Respaldo Opcional" a continuación).

4. **Traer los Cambios Remotos**
   Ahora, trae los cambios de `origin/main`. Dado que tu `main` local ahora está en el ancestro común y `origin/main` está adelantado por 70 commits, esto avanzará rápidamente tu `main` local para coincidir con `origin/main`.

   ```bash
   git pull origin main
   ```

   Después de esto, tu rama local `main` será idéntica a `origin/main`, con todos los commits locales divergentes descartados.

### Secuencia Completa de Comandos

Aquí está la secuencia completa de comandos para ejecutar:

```bash
git fetch origin
ancestor=$(git merge-base main origin/main)
git reset --hard $ancestor
git pull origin main
```

### ¿Qué Sucede?
- **Después del Paso 1**: Tu repositorio local conoce el estado más reciente de `origin/main`.
- **Después del Paso 2**: Has identificado el commit ancestro común (por ejemplo, un hash como `abc123`).
- **Después del Paso 3**: Tu `main` local se restablece a `abc123`, perdiendo los 74 commits locales únicos.
- **Después del Paso 4**: `git pull` avanza rápidamente `main` a `origin/main`, trayendo los 70 commits de la rama remota.

El resultado es que tu `main` local coincide exactamente con `origin/main`, cumpliendo tu objetivo de usar la rama remota.

### Respaldo Opcional
Si no estás seguro de descartar tus commits locales y quieres preservarlos para más tarde, crea una rama de respaldo antes de restablecer:

```bash
git branch backup-main
```

Ejecuta esto antes del comando `git reset`. Tus 74 commits locales permanecerán en `backup-main`, y puedes revisitarlos más tarde si es necesario.

### Notas Importantes
- **Cambios Sin Confirmar**: Si tienes cambios sin confirmar (en tu directorio de trabajo o área de preparación) que deseas mantener, guárdalos antes de restablecer:
  ```bash
  git stash
  ```
  Después de completar el proceso, puedes recuperarlos con `git stash pop`.
- **Por Qué Funciona**: Restablecer al ancestro común y tirar asegura un avance rápido limpio a `origin/main`, evitando conflictos de fusión que podrían surgir al tirar directamente con ramas divergentes.

Siguiendo estos pasos, resetearás con éxito tu `main` local para que coincida con `origin/main` como se desea.