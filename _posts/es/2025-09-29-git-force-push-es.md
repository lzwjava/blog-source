---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: Forzar Push mediante Eliminación de Rama
translated: true
type: note
---

```python
#!/usr/bin/env python3
"""
git_force_push.py

Este script realiza un "force push" eliminando primero la rama remota,
y luego subiendo la rama local. Esto funciona si el repositorio permite
eliminaciones de ramas pero no force pushes.

Uso: python git_force_push.py <remote> <branch>
Ejemplo: python git_force_push.py origin main

Nota: Esto asume que tienes permisos suficientes y que la eliminación está permitida.
Ten cuidado, ya que eliminar una rama puede perder commits.
"""

import subprocess
import sys

def run_command(command):
    """Ejecuta un comando de shell y devuelve su salida."""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error ejecutando comando '{command}': {e}")
        print(f"Stderr: {e.stderr}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python git_force_push.py <remote> <branch>")
        sys.exit(1)

    remote = sys.argv[1]
    branch = sys.argv[2]

    # Eliminar la rama remota
    delete_cmd = f"git push {remote} :{branch}"
    print(f"Eliminando rama remota: {delete_cmd}")
    run_command(delete_cmd)

    # Subir la rama local
    push_cmd = f"git push {remote} {branch}"
    print(f"Subiendo rama local: {push_cmd}")
    run_command(push_cmd)

    print("Force push completado exitosamente.")
```

### Cómo Funciona
- **Paso de Eliminación**: Ejecuta `git push origin :main` para eliminar la rama remota (como está permitido en tu repositorio).
- **Paso de Subida**: Ejecuta `git push origin main` para subir la rama local, creándola de nuevo en el repositorio remoto.
- Esto efectivamente logra un force push descartando el historial remoto y reemplazándolo con el historial local.
- **Notas de Seguridad/Uso**: Prueba primero en un repositorio no crítico. Esto requiere la configuración y permisos adecuados de Git. Si el repositorio tiene protecciones adicionales (por ejemplo, mediante hooks), podría fallar. Sin garantías; las operaciones de Git pueden ser destructivas.