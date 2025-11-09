---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Desactivar la ventana emergente de confirmación de edición de código de Claude
translated: true
type: note
---

Para desactivar la ventana emergente de confirmación de edición en Claude Code (para que aplique los cambios directamente a archivos como `sync_githook.py` sin preguntar), necesitas configurar los permisos en tu archivo `settings.json`. Este es el "Claude Code JSON" al que te refieres—es el archivo de configuración principal de Claude Code para configuraciones a nivel de usuario.

### Pasos para Configurarlo

1. **Ubicar o Crear el Archivo**:
   - El archivo está en `~/.claude/settings.json` (en macOS/Linux) o `%USERPROFILE%\.claude\settings.json` (en Windows). La carpeta `.claude` está oculta, así que usa tu terminal o explorador de archivos para navegar allí.
   - Si el archivo o la carpeta no existen, créalos. Puedes hacer esto ejecutando el comando `/config` de Claude Code en su REPL interactivo (te guiará para abrir la interfaz de configuración).

2. **Editar el JSON**:
   - Abre `settings.json` en cualquier editor de texto (por ejemplo, VS Code).
   - Agrega o actualiza la sección `permissions` para aprobar automáticamente las ediciones. Aquí tienes una configuración simple para desactivar los mensajes para todas las acciones de edición:

     ```json:disable-run
     {
       "permissions": {
         "defaultMode": "acceptEdits",
         "allow": [
           "Edit(*)",
           "Write(*)",
           "MultiEdit(*)"
         ],
         "ask": []
       }
     }
     ```

     - **Qué hace esto**:
       - `"defaultMode": "acceptEdits"`: Establece el valor predeterminado global para aceptar ediciones sin solicitar confirmación.
       - `"allow"`: Aprueba previamente herramientas específicas como `Edit` (para ediciones de un solo archivo), `Write` (para escribir contenido) y `MultiEdit` (para cambios por lotes) para cualquier archivo (comodín `*`).
       - `"ask": []`: Garantiza que ninguna acción active un mensaje a menos que sea explícitamente denegada en otro lugar.
     - Guarda el archivo. Los cambios se aplican inmediatamente en tu próxima sesión de Claude Code.

3. **Probarlo**:
   - Reinicia Claude Code o recarga la sesión.
   - Pídele que edite un archivo (por ejemplo, "Edita sync_githook.py para agregar un comentario"). Debería aplicar el cambio sin la ventana emergente.
   - Si deseas configuraciones específicas del proyecto (por ejemplo, solo para este repositorio), crea `.claude/settings.json` en la carpeta raíz de tu proyecto en su lugar.

4. **Ajustes Opcionales**:
   - Para un control más granular (por ejemplo, permitir ediciones solo en ciertos directorios): Cambia `"Edit(*)"` por `"Edit(./src/**)"`.
   - Si los mensajes persisten, ejecuta `/allowed-tools` en el REPL para verificar las reglas actuales, o usa `/config` para ajustar a través de la interfaz de usuario.
   - Por seguridad, evita reglas `allow` demasiado amplias—comienza de manera simple y expande.

Esto debería hacer que tu flujo de trabajo sea más rápido sin interrupciones. Si estás en un entorno empresarial, consulta con tu administrador, ya que las políticas gestionadas podrían anular la configuración del usuario.

[Documentación de Configuración de Claude Code](https://docs.claude.com/en/docs/claude-code/settings)  
[Guía para Desactivar Mensajes de Permiso de Claude Code](https://www.arsturn.com/blog/how-to-disable-claude-code-permission-prompts)