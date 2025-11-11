---
audio: false
generated: true
lang: es
layout: post
title: Comandos Avanzados de Git
translated: true
type: note
---

Git es como una navaja suiza para desarrolladores: versátil, potente y ocasionalmente confuso si no sabes qué herramienta usar. Hoy vamos a profundizar en algunas de las características y flujos de trabajo más ingeniosos de Git: seleccionar cambios específicos (cherry-picking), fusionar con estilo, reorganizar (rebase) para un historial más limpio, eliminar esos archivos grandes molestos que cometiste accidentalmente y deshacer un commit cuando te das cuenta de que te has equivocado. Vamos a desglosarlo.

#### Cherry-Picking: Tomando Solo Lo Que Necesitas
Imagina que tienes una rama de funcionalidad con una docena de commits, pero hay un commit brillante allí que quieres sacar y aplicar a tu rama principal (main) sin traer el resto. Ahí es donde entra `git cherry-pick`.

Es muy sencillo: encuentra el hash del commit (puedes obtenerlo de `git log`), cambia a la rama donde lo quieres y ejecuta:
```
git cherry-pick <commit-hash>
```
Boom, ese commit ahora es parte de tu rama actual. Si hay un conflicto, Git se pausará y te permitirá resolverlo, como en una fusión. Cuando estés satisfecho, confirma (commit) los cambios y listo.

Yo uso esto constantemente cuando una corrección de un error se cuela en una rama de funcionalidad desordenada y la necesito en `main` lo antes posible. Solo ten cuidado: el cherry-picking duplica el commit, así que obtiene un nuevo hash. No esperes que funcione bien si luego fusionas la rama original sin algo de limpieza.

#### Opciones de Merge: Más Que Solo "Fusionar"
Fusionar (merge) es el pan de cada día de Git, pero ¿sabías que viene con variantes? El comando por defecto `git merge` hace un "avance rápido" (fast-forward) si es posible (enderezando el historial) o crea un commit de fusión si las ramas han divergido. Pero tienes opciones:

- **`--no-ff` (Sin Avance Rápido)**: Fuerza un commit de fusión incluso si un avance rápido es posible. Me encanta esto para mantener un registro claro de cuándo una rama de funcionalidad llegó a `main`. Ejecútalo así:
  ```
  git merge --no-ff rama-de-funcionalidad
  ```
- **`--squash`**: Extrae todos los cambios de la rama y los convierte en un solo commit en tu rama actual. Sin commit de fusión, solo un paquete limpio y ordenado. Perfecto para compactar una rama desordenada en algo presentable:
  ```
  git merge --squash rama-de-funcionalidad
  ```
  Después de esto, necesitarás hacer commit manualmente para finalizar.

Cada uno tiene su lugar. Yo me inclino por `--no-ff` para ramas de larga duración y `--squash` cuando tengo una rama llena de commits "WIP" que prefiero olvidar.

#### Rebasing: Reescribiendo la Historia Como un Profesional
Si las fusiones te parecen muy desordenadas, `git rebase` podría ser lo tuyo. Toma tus commits y los reproduce en otra rama, dándote un historial lineal que parece como si lo hubieras planeado todo perfectamente desde el principio.

Cambia a tu rama de funcionalidad y ejecuta:
```
git rebase main
```
Git levantará tus commits, actualizará la rama para que coincida con `main` y volverá a colocar tus cambios en la parte superior. Si surgen conflictos, resuélvelos, luego usa `git rebase --continue` hasta que termine.

¿La ventaja? Una línea de tiempo prístina. ¿La desventaja? Si ya has subido (push) esa rama y otros están trabajando en ella, el rebase reescribe el historial—lo que puede generar correos electrónicos enfadados de tus compañeros de equipo. Yo me limito a hacer rebase en ramas locales o proyectos en solitario. Para cosas compartidas, fusionar (merge) es más seguro.

#### Eliminar Archivos Grandes del Historial: Ups, Ese Vídeo de 2GB
Todos hemos estado ahí: cometes accidentalmente un archivo enorme, lo subes (push), y ahora tu repositorio está hinchado. Git no olvida fácilmente, pero puedes limpiar ese archivo del historial con algo de esfuerzo.

La herramienta principal aquí es `git filter-branch` o la más nueva `git filter-repo` (recomiendo esta última—es más rápida y menos propensa a errores). Digamos que cometiste `archivogrande.zip` y necesitas eliminarlo:
1. Instala `git-filter-repo` (consulta su documentación para la configuración).
2. Ejecuta:
   ```
   git filter-repo --path archivogrande.zip --invert-paths
   ```
   Esto elimina `archivogrande.zip` de cada commit en el historial.
3. Fuerza la subida (force-push) del historial reescrito:
   ```
   git push --force
   ```

Atención: esto reescribe el historial, así que coordina con tu equipo. Y si está en una pull request en algún sitio, quizás también necesites limpiar las referencias (refs). Una vez eliminado, tu repositorio se reducirá después de una recolección de basura (`git gc`).

#### Deshacer un Commit: Rebobinando el Tiempo
¿Hiciste un commit y al instante te arrepentiste? Git te cubre las espaldas. Hay un par de formas de deshacerlo, dependiendo de hasta dónde hayas llegado:

- **Si aún no has subido los cambios (push)**: Usa `git reset`. Para deshacer el último commit pero mantener los cambios en tu directorio de trabajo:
  ```
  git reset HEAD^ --soft
  ```
  ¿Quieres descartar los cambios por completo?
  ```
  git reset HEAD^ --hard
  ```
- **Si ya has subido los cambios (push)**: Necesitarás reescribir el historial. Haz reset localmente con `git reset HEAD^`, luego fuerza la subida (force-push):
  ```
  git push --force
  ```
  De nuevo, esto altera el historial compartido, así que ve con cuidado.

`git reset --soft` me ha salvado más veces de las que puedo contar—es perfecto para cuando hago commit demasiado pronto y necesito ajustar algo.

#### Conclusión

La flexibilidad de Git es lo que lo hace tan potente, pero es fácil enredarse si no conoces tus opciones. Usa cherry-pick para una precisión quirúrgica, ajusta las fusiones para que se adapten a tu flujo de trabajo, haz rebase para un historial pulido y no entres en pánico cuando necesites borrar un error—ya sea un archivo enorme o un commit apresurado. Practica estos comandos en un repositorio de prueba si estás nervioso, y pronto te parecerán algo natural.

¿Cuál es tu truco favorito de Git? ¡Házmelo saber—siempre estoy dispuesto a aprender algo nuevo