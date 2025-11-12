---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: Guía de Ganchos de Git Precommit Prepush
translated: true
type: note
---

### Resumen de Git Hooks

Los Git hooks son scripts personalizables que automatizan tareas en puntos específicos del flujo de trabajo de Git. Pueden ser del lado del cliente (se ejecutan en tu máquina local) o del lado del servidor (se ejecutan en el repositorio remoto). Los hooks se almacenan en el directorio `.git/hooks/` de un repositorio. A continuación, desglosaré los hooks pre-commit, pre-push y los del lado del servidor relacionados con el push, explicando cómo se ejecutan.

### Hooks del Lado del Cliente: Pre-Commit y Pre-Push

Estos hooks se ejecutan localmente en tu máquina antes de que las acciones se finalicen, permitiéndote aplicar reglas o ejecutar verificaciones.

- **Hook Pre-Commit**:
  - **Cuándo se ejecuta**: Se activa automáticamente justo antes de que confirmes los cambios (por ejemplo, mediante `git commit`).
  - **Propósito**: Útil para verificaciones de calidad del código, como ejecutar linters, tests o herramientas de formateo. Si el hook falla (termina con un estado distinto de cero), la confirmación se aborta.
  - **Ejemplo**: Un hook pre-commit de ejemplo podría ejecutar `eslint` en archivos JavaScript. Si hay errores, la confirmación se detiene.
  - **Cómo funciona**: El script está en `.git/hooks/pre-commit`. Hazlo ejecutable con `chmod +x .git/hooks/pre-commit`. Si usas herramientas como Husky (una librería popular para gestionar Git hooks), simplifica la configuración.

- **Hook Pre-Push**:
  - **Cuándo se ejecuta**: Se activa automáticamente justo antes de que hagas push a un remoto (por ejemplo, mediante `git push`).
  - **Propósito**: Verifica cosas como ejecutar tests, verificar la cobertura del código o asegurar la compatibilidad antes de enviar los cambios al remoto. Si falla, el push se bloquea.
  - **Nota sobre "some prepush"**: No existe un hook estándar "prepush" en Git—asumo que te refieres al hook "pre-push" (con un guion). Puedes crear scripts pre-push personalizados, a menudo mediante herramientas como Husky, para aplicar reglas como "solo hacer push si pasan todos los tests".
  - **Ejemplo**: Un hook pre-push podría ejecutar `npm test` y abortar el push si los tests fallan. Si se omite (por ejemplo, con `git push --no-verify`), el hook no se ejecutará.
  - **Cómo funciona**: Se encuentra en `.git/hooks/pre-push`. Se necesitan permisos de ejecución. Recibe argumentos como el nombre del remoto y la referencia (ref) que se está enviando.

Los hooks del lado del cliente aseguran que los problemas se detecten temprano, evitando que confirmaciones o pushes incorrectos salgan de tu máquina.

### Hooks del Lado del Servidor Durante el Push

Cuando ejecutas `git push`, el push se envía al repositorio remoto (por ejemplo, GitHub, GitLab o un servidor personalizado). El remoto puede tener sus propios hooks que se ejecutan durante o después del proceso de push. Estos se almacenan en el directorio `.git/hooks/` del repositorio Git remoto y son gestionados por el administrador del servidor.

- **Proceso Durante el Push**:
  1. **Verificaciones locales**: El hook pre-push se ejecuta primero (si está presente).
  2. **Transferencia de datos**: Los cambios se envían al remoto.
  3. **Ejecución remota**: Los hooks del lado del servidor se ejecutan en el servidor remoto, no en tu máquina.

- **Hook Pre-Receive**:
  - **Cuándo se ejecuta**: En el servidor remoto, inmediatamente después de recibir el push pero antes de actualizar cualquier referencia (ramas o etiquetas).
  - **Propósito**: Valida los cambios entrantes. Puede rechazar el push completo si las verificaciones fallan, como forzar mensajes de commit, revisiones de código o escaneos de seguridad.
  - **Cómo funciona**: Si el hook termina con un estado distinto de cero, el push es denegado y verás un mensaje de error. Ejemplo: Rechazar pushes que introduzcan archivos de un tamaño superior a un límite.

- **Hook Update** (Similar a Pre-Receive pero por referencia):
  - **Cuándo se ejecuta**: Para cada rama/etiqueta que se está actualizando, después de pre-receive.
  - **Propósito**: Permite un control más granular, como verificar si el push es de un usuario autorizado o si la rama sigue las convenciones de nomenclatura.
  - **Cómo funciona**: Recibe detalles sobre la referencia que se está actualizando.

- **Hook Post-Receive**:
  - **Cuándo se ejecuta**: En el servidor remoto, después de que el push es completamente aceptado y las referencias se han actualizado.
  - **Propósito**: Activa acciones posteriores, como desplegar código, enviar notificaciones (por ejemplo, alertas de Slack) o ejecutar scripts posteriores al despliegue como "reconstruir la aplicación".
  - **Cómo funciona**: Se ejecuta de forma confiable después de un push exitoso. Ejemplo: Activar automáticamente un pipeline de CI/CD o actualizar un servidor web.

Los hooks del lado del servidor proporcionan una aplicación centralizada de reglas, por lo que incluso si se omiten tus hooks locales, el remoto aún puede validar o reaccionar al push. Plataformas como GitHub usan webhooks (equivalentes basados en API) para propósitos similares, pero para servidores Git bare o repositorios auto-alojados, los hooks mencionados son clave.

### Diferencias Clave y Mejores Prácticas

- **Cliente vs. Servidor**: Los hooks del cliente (como pre-commit/pre-push) te dan retroalimentación rápida localmente. Los hooks del servidor aplican reglas para todo el repositorio.
- **Personalización**: Los hooks son scripts de shell (por ejemplo, Bash) pero pueden invocar Python, Node.js, etc. Usa herramientas como pre-commit (un framework) para gestionarlos.
- **Omitir**: Se puede confirmar con `--no-verify`, hacer push con `--no-verify`, pero los hooks del servidor no se pueden omitir a menos que tengas acceso de administrador.
- **Consejos de Configuración**: Los hooks no se copian entre repositorios, así que añádelos a una plantilla de repositorio o usa una herramienta para instalarlos.

Si estás configurando esto, consulta la documentación de Git o herramientas como Husky para proyectos de node. ¡Si tienes un escenario específico (por ejemplo, un ejemplo de código), proporciona más detalles para un consejo más personalizado