---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: Actualización del Código de Claude a la Última Versión
translated: true
type: note
---

Para actualizar Claude Code de la versión v2.0.0 a la última versión, utiliza uno de los siguientes métodos según tu tipo de instalación (todas las versiones soportan actualizaciones automáticas por defecto, que se aplican la próxima vez que inicies la herramienta; puedes desactivarlas configurando `DISABLE_AUTOUPDATER=1`):

### Mediante el Comando Integrado de Claude Code
Ejecuta el comando de actualización manual en tu terminal:
```
claude update
```
Esto aplica automáticamente la última versión. [1][2]

### Via npm (Si se Instaló Globalmente)
Si originalmente instalaste via npm, actualiza con:
```
npm update -g @anthropic-ai/claude-code
```
O fuerza la instalación de la última versión:
```
npm install -g @anthropic-ai/claude-code@latest
```
[3][4]

### Via Binario Nativo (Instalador Beta)
Para instalaciones nativas, vuelve a ejecutar el script de instalación para la última versión:
```
# macOS/Linux/WSL
curl -fsSL https://claude.ai/install.sh | bash -s latest

# Windows PowerShell
& ([scriptblock]::Create((irm https://claude.ai/install.ps1))) latest
```
[1]

**Verificación:** Después de actualizar, verifica tu versión con `claude --version` para confirmar que se ha actualizado (por ejemplo, a la versión estable actual). Si encuentras problemas, asegúrate de que npm esté actualizado (`npm install -g npm@latest`). La configuración y los ajustes se conservan entre actualizaciones. [1][3][4]

Citas:
[1] https://docs.claude.com/en/docs/claude-code/setup
[2] https://www.reddit.com/r/ClaudeAI/comments/1lvbijz/claude_code_updates_from_version_1045_to_1044/
[3] https://www.reddit.com/r/ClaudeAI/comments/1l8gbfo/dont_forget_to_update_your_claude_cli_it_makes_a/
[4] https://www.claudelog.com/faq/