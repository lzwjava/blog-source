---
audio: false
generated: true
lang: es
layout: post
title: Instalar XeLaTeX
translated: true
type: note
---

Para instalar XeLaTeX en Ubuntu 24.04 o 22.04, sigue estos pasos:

1. **Actualizar la lista de paquetes**:
   ```bash
   sudo apt update
   ```

2. **Instalar TeX Live (que incluye XeLaTeX)**:
   - Para una instalación completa (recomendada para la mayoría de usuarios, incluye XeLaTeX y muchos paquetes):
     ```bash
     sudo apt install texlive-xetex
     ```
   - Si quieres una instalación mínima, puedes instalar `texlive`, pero `texlive-xetex` es preferible para soporte de XeLaTeX.

3. **Verificar la instalación**:
   Ejecuta el siguiente comando para comprobar si XeLaTeX está instalado:
   ```bash
   xelatex --version
   ```
   Deberías ver una salida como `XeTeX 3.14159265-2.6-0.999991` (los números de versión pueden variar).

4. **Opcional: Instalar fuentes adicionales** (si necesitas fuentes específicas para XeLaTeX):
   ```bash
   sudo apt install texlive-fonts-extra
   ```

5. **Probar XeLaTeX**:
   Crea un archivo `.tex` simple, por ejemplo, `test.tex`:
   ```latex
   \documentclass{article}
   \usepackage{fontspec}
   \setmainfont{Liberation Serif}
   \begin{document}
   ¡Hola, XeLaTeX!
   \end{document}
   ```
   Compílalo con:
   ```bash
   xelatex test.tex
   ```
   Esto debería generar un archivo `test.pdf`.

**Notas**:
- El paquete `texlive-xetex` está disponible en los repositorios de Ubuntu 22.04 y 24.04.
- Si necesitas la última versión de TeX Live, puedes instalarla manualmente desde el sitio web de TeX Live, pero el paquete de Ubuntu suele ser suficiente.
- Asegúrate de tener suficiente espacio en disco (~1-2 GB para `texlive-xetex`, más para `texlive-full`).
- Si encuentras problemas, verifica las dependencias faltantes con `sudo apt install -f`.

¡Avísame si necesitas más ayuda!