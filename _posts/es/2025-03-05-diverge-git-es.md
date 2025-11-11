---
audio: false
generated: true
lang: es
layout: post
title: Ramas de Git Divergentes
translated: true
type: note
---

Cuando tu rama local `main` y la rama remota `origin/main` han divergido en Git—con 74 y 70 commits diferentes respectivamente—significa que comparten un ancestro común pero desde entonces han desarrollado commits únicos. Tu objetivo es hacer que tu rama local `main` coincida con `origin/main` restableciendo tu rama local al ancestro común (el "padre de ambas") y luego usando `git pull` para incorporar los cambios remotos, descartando efectivamente tus commits locales divergentes en favor de los remotos. A continuación se detallan los pasos para lograr esto.

### Pasos para Corregir la Divergencia

1. **Obtener los Últimos Cambios Remotos**  
   Comienza asegurándote de que tu repositorio local tiene la información más reciente del remoto. Esto actualiza tu referencia a `origin/main` sin alterar tu rama local `main` todavía.

   ```bash
   git fetch origin
   ```

2. **Encontrar el Commit del Ancestro Común**  
   Usa `git merge-base` para identificar el commit del ancestro común entre tu `main` local y `origin/main`. Este es el punto donde las ramas divergieron.

   ```bash
   ancestor=$(git merge-base main origin/main)
   ```

   Este comando almacena el hash del commit del ancestro común en la variable `ancestor`.

3. **Restablecer `main` Local al Ancestro Común**  
   Restablece tu rama local `main` al commit del ancestro común. La opción `--hard` asegura que tanto el puntero de la rama como tu directorio de trabajo se actualicen, descartando todos los commits locales y los cambios realizados después de este punto.

   ```bash
   git reset --hard $ancestor
   ```

   **Precaución**: Este paso descartará todos los cambios no confirmados en tu directorio de trabajo y área de staging, así como los 74 commits únicos de tu `main` local. Si necesitas preservarlos, considera crear primero una rama de respaldo (ver "Respaldo Opcional" más abajo).

4. **Traer los Cambios Remotos**  
   Ahora, trae los cambios desde `origin/main`. Dado que tu `main` local está ahora en el ancestro común, y `origin/main` está adelantado por 70 commits, esto hará un avance rápido de tu `main` local para que coincida con `origin/main`.

   ```bash
   git pull origin main
   ```

   Después de esto, tu rama local `main` será idéntica a `origin/main`, con todos los commits locales divergentes descartados.

### Secuencia Completa de Comandos

Aquí está la secuencia completa de comandos a ejecutar:

```bash
git fetch origin
ancestor=$(git merge-base main origin/main)
git reset --hard $ancestor
git pull origin main
```

### ¿Qué Sucede?
- **Después del Paso 1**: Tu repositorio local conoce el estado más reciente de `origin/main`.
- **Después del Paso 2**: Has identificado el commit del ancestro común (por ejemplo, un hash como `abc123`).
- **Después del Paso 3**: Tu `main` local se restablece a `abc123`, perdiendo los 74 commits locales únicos.
- **Después del Paso 4**: `git pull` realiza un avance rápido de `main` a `origin/main`, incorporando los 70 commits de la rama remota.

El resultado es que tu `main` local coincide exactamente con `origin/main`, cumpliendo tu objetivo de usar la rama remota.

### Respaldo Opcional
Si no estás seguro de descartar tus commits locales y quieres preservarlos para más tarde, crea una rama de respaldo antes de restablecer:

```bash
git branch backup-main
```

Ejecuta esto antes del comando `git reset`. Tus 74 commits locales permanecerán en `backup-main`, y podrás revisarlos más tarde si es necesario.

### Notas Importantes
- **Cambios No Confirmados**: Si tienes cambios no confirmados (en tu directorio de trabajo o área de staging) que quieres conservar, guárdalos en el stash antes de restablecer:
  ```bash
  git stash
  ```
  Después de completar el proceso, puedes recuperarlos con `git stash pop`.
- **Por Qué Esto Funciona**: Restablecer al ancestro común y luego traer los cambios asegura un avance rápido limpio a `origin/main`, evitando conflictos de fusión que podrían surgir al traer cambios directamente con ramas divergidas.

Siguiendo estos pasos, restablecerás con éxito tu `main` local para que coincida con `origin/main` como deseas.