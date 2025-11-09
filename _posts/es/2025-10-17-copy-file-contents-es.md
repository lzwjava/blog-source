---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Copiar Contenido de Archivo en Vi
translated: true
type: note
---

## Copiar (o Mover) Todo el Contenido de un Archivo a un Nuevo Archivo en Vi

Basándome en tu uso de vi, asumiré que quieres seleccionar y copiar/eliminar todo el contenido de un archivo, y luego pegarlo en un archivo nuevo. Vi no tiene una opción directa de "seleccionar todo" como los editores gráficos, pero puedes lograrlo eficientemente en **modo comando** (presiona `Esc` para asegurarte de estar allí). Cubriré tanto **copiar** (dejando el original intacto) como **cortar/eliminar** (mover el contenido).

### Paso a Paso: Copiar Todo el Contenido a un Nuevo Archivo
1. Abre tu archivo fuente:  
   ```
   vi archivoviejo.txt
   ```

2. Yank (copiar) todo el archivo:  
   - Escribe `gg` (ir al inicio del archivo).  
   - Luego escribe `yG` (yank desde la posición actual hasta el final del archivo).  
   *Alternativa (específico de Vim, funciona en vim de Red Hat):* Escribe `:1,$y` y presiona `Enter` (copia las líneas 1 hasta el final).

3. Abre el nuevo archivo:  
   - Escribe `:e archivo_nuevo.txt` y presiona `Enter` (crea/abre el nuevo archivo).

4. Pega el contenido:  
   - Escribe `p` (pega después del cursor; como está vacío, pega al inicio).  
   *Alternativa:* Escribe `P` para pegar antes del cursor.

5. Guarda y cierra el nuevo archivo:  
   - Escribe `:wq` y presiona `Enter`.

El archivo original permanece sin cambios.

### Paso a Paso: Eliminar Todo el Contenido y Pegarlo en un Nuevo Archivo (Mover)
Esto elimina el contenido original después de copiarlo.

1. Abre tu archivo fuente:  
   ```
   vi archivo_viejo.txt
   ```

2. Yank (copiar) todo el archivo primero:  
   - `gg` luego `yG` (o `:1,$y`).

3. Elimina todo el contenido:  
   - Escribe `gg` (al inicio).  
   - Luego `dG` (elimina desde la posición actual hasta el final).  
   *Alternativa:* Escribe `:%d` y presiona `Enter` (elimina todas las líneas).  
   Guarda si es necesario: `:w` (sobrescribe el archivo ahora vacío).

4. Abre el nuevo archivo:  
   - Escribe `:e archivo_nuevo.txt` y presiona `Enter`.

5. Pega:  
   - Escribe `p`.

6. Guarda y cierra:  
   - `:wq`.

### Consejos Rápidos
- Si eliminas accidentalmente sin copiar primero, usa `u` para deshacer.
- Para hacer esto entre archivos sin abrir uno nuevo cada vez: Copia en el primer archivo, luego usa `vi archivo_nuevo.txt`, pega y guarda.
- Para archivos grandes, estos comandos son rápidos ya que vi maneja los buffers eficientemente.

¡Practica en archivos de prueba para familiarizarte!

[How to Copy Text to Another File in Vim](https://stackoverflow.com/questions/1239801/how-to-copy-to-the-end-of-the-line-in-vim)  
[Vim: Yank (copy) entire file](https://vim.fandom.com/wiki/Yank_%28copy%29_the_entire_file)