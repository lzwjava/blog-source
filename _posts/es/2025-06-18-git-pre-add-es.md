---
audio: false
generated: true
lang: es
layout: post
title: Alternativas a los Hooks Pre-add de Git
translated: true
type: note
---

Git no tiene un hook `pre-add` incorporado, pero existen varias formas de lograr una funcionalidad similar. Aquí hay algunos enfoques:

### 1. **Alias de Git (Enfoque Recomendado)**
Puedes crear un alias de Git que ejecute tus verificaciones antes de llamar a `git add`:

```bash
git config --global alias.safe-add '!your-pre-add-script.sh && git add'
```

Luego usa `git safe-add` en lugar de `git add`.

### 2. **Script Contenedor**
Crea un script llamado `git-pre-add` en tu PATH que:
1. Ejecute tus verificaciones pre-add
2. Llame a `git add` si las verificaciones son exitosas

```bash
#!/bin/bash
# Tu lógica de validación pre-add aquí
if [ alguna_condicion ]; then
  git add "$@"
else
  echo "Las verificaciones pre-add fallaron"
  exit 1
fi
```

### 3. **Usando Hooks Existentes**
Podrías aprovechar los hooks existentes de forma creativa:
- **pre-commit**: Aunque se ejecuta después de add pero antes del commit, podrías verificar los archivos preparados aquí
- **prepare-commit-msg**: Similar a pre-commit pero más temprano en el proceso

### 4. **Monitoreo del Sistema de Archivos**
Para necesidades más avanzadas, podrías usar:
- **inotifywait** (Linux) para observar tu directorio de trabajo
- **fswatch** (Mac) para una funcionalidad similar

### Ejemplo de Script de Verificación Pre-Add
Aquí hay un ejemplo simple que evita agregar archivos con espacios en blanco al final:

```bash
#!/bin/bash
# .git/hooks/pre-commit (pero funciona en archivos preparados)

# Verificar errores de espacios en blanco
if git diff --cached --check; then
  exit 0
else
  echo "Se encontraron errores de espacios en blanco en los archivos preparados"
  exit 1
fi
```

Recuerda hacer que cualquier script de hook sea ejecutable (`chmod +x script.sh`).

¿Te gustaría que profundice en algún enfoque en particular para tu caso de uso?