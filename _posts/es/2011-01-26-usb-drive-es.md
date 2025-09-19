---
audio: false
generated: false
image: false
lang: es
layout: post
title: Personaliza tu unidad USB con un fondo e icono
translated: true
---

Este post fue originalmente escrito en chino y publicado en Qzone.

---

**I. Personalizar el ícono de la unidad USB:**

1. Primero, elige un ícono que te guste. La extensión del archivo del ícono debe ser `.ico`.
2. Copia el archivo del ícono a tu unidad USB y crea un nuevo documento de texto en la unidad USB.
3. En el documento de texto, escribe lo siguiente:
   ```
   [autorun]
   ICON=\xxx.ico,0
   ```
   Donde `xxx.ico` es el nombre de tu archivo de ícono (incluyendo la extensión).
4. Guarda el archivo de texto como `autorun.inf`.
   **Nota:** Es crucial cambiar la extensión a `.inf`, no a `.txt`. Si el ícono del archivo cambia a uno con un engranaje amarillo, lo has hecho correctamente.
   Desconecta la unidad USB y vuelve a conectarla. Verás que el ícono de la unidad USB ha cambiado al que seleccionaste.
   Este método también se puede usar para discos duros externos o grabaciones de CD/DVD.

**II. Personalizar el fondo:**

1. Primero, elige una imagen de fondo que te guste y cópiala a tu unidad USB.
2. Crea un nuevo archivo de texto y copia lo siguiente en él:
   ```
   [ExtShellFolderViews]
   {BE098140-A513-11D0-A3A4-00C04FD706EC}={BE098140-A513-11D0-A3A4-00C04FD706EC}
   [{BE098140-A513-11D0-A3A4-00C04FD706EC}]
   Attributes=1
   IconArea_Image=aaa.jpg
   IconArea_Text=0x00FFFFFF
   [.ShellClassInfo]
   ConfirmFileOp=0
   ```
   Este código significa:

   Donde `aaa.jpg` es el nombre de tu archivo de imagen elegido (incluyendo la extensión).

   `IconArea_Text= 0x00FFFFFF` Esta línea cambia el color del texto en la unidad USB.

   Los códigos de color son:

   * Rojo: `0x000000FF`
   * Amarillo: `0x0000FFFF`
   * Azul: `0x00FF0000`
   * Gris: `0x00808080`
   * Verde lima: `0x006BDEC7`
   * Negro: `0x00000000`
   * Color de fondo de Excel: `0x00848284`
   * Blanco: `0x00FFFFFF`
   * Verde: `0x00008000`
   * Morado: `0x00C000C0`

   Elige un color que te guste (que combine con tu fondo) y reemplaza el código de color existente.

   Puedes cambiar el color después de `IconArea_Text=` a tu color preferido.

3. Guarda el archivo de texto como `Desktop.ini`. La modificación está completa.
   Actualiza la unidad USB y deberías ver los cambios.
   Todos los cuatro archivos mencionados anteriormente se pueden ocultar para evitar su eliminación accidental.
   Después de cambiar el ícono, necesitas desconectar y volver a conectar la unidad USB para ver el efecto.
   Después de cambiar el fondo, actualiza la unidad USB para ver los cambios.