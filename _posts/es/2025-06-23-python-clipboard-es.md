---
audio: false
generated: true
lang: es
layout: post
title: Acceso al Portapapeles de Python en Ubuntu
translated: true
type: note
---

Para leer desde el portapapeles en Ubuntu usando Python, puedes utilizar bibliotecas como `pyperclip` o interactuar con utilidades del sistema como `xclip` o `xsel`. A continuación se presentan dos enfoques comunes:

### Enfoque 1: Usar `pyperclip`
`pyperclip` es una biblioteca multiplataforma de Python para acceder al portapapeles.

1. **Instalar pyperclip**:
   ```bash
   pip install pyperclip
   ```

2. **Código Python para leer del portapapeles**:
   ```python
   import pyperclip

   # Leer el contenido del portapapeles
   contenido_portapapeles = pyperclip.paste()
   print(contenido_portapapeles)
   ```

3. **Notas**:
   - Asegúrate de que `xclip` o `xsel` estén instalados en Ubuntu, ya que `pyperclip` depende de ellos:
     ```bash
     sudo apt update
     sudo apt install xclip xsel
     ```
   - Este método es simple y funciona en múltiples plataformas.

### Enfoque 2: Usar `xclip` Directamente
Si prefieres interactuar directamente con el portapapeles del sistema, puedes usar `xclip`.

1. **Instalar xclip**:
   ```bash
   sudo apt update
   sudo apt install xclip
   ```

2. **Código Python para leer del portapapeles usando `xclip`**:
   ```python
   import subprocess

   # Leer el contenido del portapapeles
   process = subprocess.run(['xclip', '-selection', 'clipboard', '-o'], capture_output=True, text=True)
   contenido_portapapeles = process.stdout
   print(contenido_portapapeles)
   ```

3. **Notas**:
   - Este enfoque llama directamente a la herramienta de línea de comandos `xclip`.
   - Usa `-selection clipboard` para el portapapeles moderno (Ctrl+C/Ctrl+V) o `-selection primary` para el portapapeles de selección del ratón.
   - Asegúrate de que `xclip` esté instalado.

### Recomendaciones
- **Usa `pyperclip`** por su simplicidad y portabilidad, a menos que tengas razones específicas para usar `xclip` o `xsel`.
- Ambos métodos requieren que `xclip` o `xsel` estén instalados para acceder al portapapeles en Ubuntu.
- Si el contenido del portapapeles no es texto (por ejemplo, una imagen), estos métodos pueden no funcionar como se espera, y necesitarías una biblioteca como `pyclip` o manejo adicional para datos que no son texto.

Probado en Ubuntu 22.04 con Python 3.10. Si encuentras problemas, asegúrate de que las herramientas requeridas (`xclip` o `xsel`) estén instaladas y de que el portapapeles contenga datos de texto.