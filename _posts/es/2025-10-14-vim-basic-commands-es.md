---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Tutorial de Comandos Básicos de Vim
translated: true
type: note
---

Vim (abreviatura de Vi IMproved) es un editor de texto modal y potente que viene por defecto en muchos sistemas Linux como Red Hat. Se maneja con teclado y es eficiente una vez que aprendes lo básico. Vim tiene tres modos principales: **Normal** (para navegación y comandos, por defecto), **Insertar** (para escribir texto) y **Visual** (para seleccionar texto). Presiona `Esc` para volver al modo Normal desde cualquier lugar.

La mejor manera de aprender de forma práctica es ejecutar `vimtutor` en tu terminal: lanza un tutorial interactivo.

## 1. Abrir y Cerrar Vim
- Abrir o crear un archivo: `vim nombre_archivo.txt` (ej., `vim notas.txt`).
- Salir sin guardar: En modo Normal, escribe `:q!` y presiona Enter.
- Salir de Vim: Consulta la sección de guardado más abajo.

## 2. Modos
- **Modo Normal**: Por defecto—úsalo para comandos. Presiona `Esc` para entrar.
- **Modo Insertar**: Presiona `i` (insertar antes del cursor) o `a` (añadir después del cursor) para entrar. Verás `-- INSERTAR --` en la parte inferior.
- **Modo Visual**: Presiona `v` para seleccionar texto.
- **Modo Línea de Comandos**: Presiona `:` para entrar (para guardar, salir, buscar).

## 3. Navegación (en Modo Normal)
Usa estos en lugar de las flechas del teclado para mayor eficiencia:
- `h`: Izquierda un carácter
- `j`: Abajo una línea
- `k`: Arriba una línea
- `l`: Derecha un carácter
- `w`: Adelante al inicio de la siguiente palabra
- `b`: Atrás al inicio de la palabra anterior
- `0`: Inicio de línea
- `$`: Fin de línea
- `gg`: Parte superior del archivo
- `G`: Parte inferior del archivo
- `:n`: Saltar a la línea n (ej., `:5`)
- Prefija con números: `5j` (bajar 5 líneas)

Activar números de línea: `:set number`

## 4. Insertar y Editar Texto
- Entrar en modo Insertar:
  - `i`: Insertar antes del cursor
  - `I`: Insertar al inicio de la línea
  - `a`: Añadir después del cursor
  - `A`: Añadir al final de la línea
  - `o`: Nueva línea debajo (entra en modo Insertar)
  - `O`: Nueva línea arriba (entra en modo Insertar)
- Salir del modo Insertar: `Esc`
- Reemplazar un solo carácter: `r` (luego escribe el nuevo carácter)
- Deshacer: `u`
- Rehacer: `Ctrl + r`
- Repetir último comando: `.`

## 5. Eliminar, Copiar y Pegar
- Eliminar carácter: `x`
- Eliminar línea: `dd`
- Eliminar rango: `:3,5d` (líneas 3 a 5)
- Copiar (yank) línea: `yy`
- Copiar texto seleccionado: En modo Visual (`v`), resalta con las flechas, luego `y`
- Pegar después del cursor: `p`
- Pegar antes del cursor: `P`
- Seleccionar texto: `v` (por caracteres), luego mueve el cursor; `Esc` para salir del modo Visual.

## 6. Guardar y Salir
- Guardar: `:w`
- Guardar y salir: `:wq` o `:x` o `ZZ` (Z mayúscula dos veces)
- Forzar guardar y salir: `:wq!`
- Salir sin guardar: `:q!` o `ZQ`

## 7. Buscar
- Buscar hacia adelante: `/patrón` (ej., `/hola`), luego Enter; `n` para el siguiente.
- Buscar hacia atrás: `?patrón`
- Reemplazar: `:%s/viejo/nuevo/g` (reemplaza todos los "viejo" por "nuevo")

## Consejos Rápidos
- Ayuda: `:help` o `:h palabra_clave`
- Dividir pantalla: `:split nombre_archivo` (horizontal) o `:vsplit nombre_archivo` (vertical); `Ctrl + w w` para cambiar.
- Practica en un archivo de prueba para evitar errores.
- Resaltado de sintaxis: `:syntax on`

Esto cubre lo esencial para que puedas editar archivos rápidamente. Para más, explora `:help` en Vim o los recursos a continuación.

[Getting started with Vim: The basics](https://opensource.com/article/19/3/getting-started-vim)  
[Basic Vim Commands](https://www.geeksforgeeks.org/linux-unix/basic-vim-commands/)  
[Vim Cheat Sheet](https://vim.rtorr.com/)