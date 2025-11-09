---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Cómo Corregir el Error de Instalación npm ENOTEMPTY
translated: true
type: note
---

### Comprender el Error

Tu comando `sudo npm i -g @anthropic-ai/claude-code --verbose` está fallando con un error `ENOTEMPTY` durante el proceso de instalación. Este es un problema común de npm que ocurre cuando npm intenta renombrar (o mover) un directorio existente como parte de la actualización o reinstalación de un paquete, pero el directorio no está vacío. En este caso, está fallando específicamente al renombrar `/usr/lib/node_modules/@anthropic-ai/claude-code` a una ubicación temporal de respaldo (`/usr/lib/node_modules/@anthropic-ai/.claude-code-ZjqcDZyQ`).

Esto típicamente sucede debido a:
- Una instalación previa parcial o interrumpida que dejó archivos o subdirectorios.
- Bloqueos de archivos por otro proceso (por ejemplo, si el paquete se cargó parcialmente o se está ejecutando otro comando de npm).
- Raramente, peculiaridades de permisos con instalaciones globales bajo `sudo`.

El paquete en sí (`@anthropic-ai/claude-code`) es legítimo: es la herramienta CLI oficial de Anthropic para "Claude Code", un asistente de codificación agéntico que se integra con tu terminal y base de código.

### Soluciones Rápidas

Prueba estos pasos en orden. Ejecútalos como root o con `sudo` donde se indique, ya que esta es una instalación global.

1. **Eliminar Manualmente el Directorio Existente**  
   Esto limpia la instalación parcial problemática:  
   ```
   sudo rm -rf /usr/lib/node_modules/@anthropic-ai/claude-code
   ```  
   - Si el directorio con ámbito principal (`@anthropic-ai`) ahora está vacío, también puedes eliminarlo:  
     ```
     sudo rm -rf /usr/lib/node_modules/@anthropic-ai
     ```  
   Luego reintenta tu comando original:  
   ```
   sudo npm i -g @anthropic-ai/claude-code --verbose
   ```

2. **Limpiar la Caché de npm**  
   Si lo anterior no funciona, podrían estar involucradas entradas de caché corruptas:  
   ```
   sudo npm cache clean --force
   sudo npm cache verify
   ```  
   Reintenta la instalación después de esto.

3. **Verificar Procesos en Ejecución**  
   Asegúrate de que no haya otros procesos de npm/Node usando el directorio:  
   ```
   ps aux | grep npm
   ```  
   Termina los que queden rezagados si es necesario (por ejemplo, `sudo kill <PID>`), luego reintenta.

4. **Alternativa: Usar npx para Pruebas**  
   Si solo quieres probar la herramienta sin una instalación global completa, intenta:  
   ```
   npx @anthropic-ai/claude-code --help
   ```  
   Esto lo descarga y ejecuta temporalmente sin modificar tus módulos globales.

### Consejos Adicionales
- **Mejor Práctica de Permisos**: Las instalaciones globales con `sudo` pueden llevar a problemas de propiedad más adelante. Considera usar un administrador de versiones de node como `nvm` para evitar `sudo` por completo, o establece un prefijo global personalizado:  
  ```
  mkdir ~/.npm-global
  npm config set prefix '~/.npm-global'
  export PATH=~/.npm-global/bin:$PATH
  ```  
  Luego instala sin `sudo`.
- **Verificar Después de la Instalación**: Una vez instalado, verifica con `claude-code --version` (asumiendo que ese es el nombre del binario: confirma en la documentación).
- Si los problemas persisten, comparte la salida de `npm ls -g @anthropic-ai/claude-code` para más diagnósticos.

Esto debería ponerte en marcha rápidamente. Si encuentras otro problema, ¡pega el nuevo registro!

[Claude Code en npm](https://www.npmjs.com/package/@anthropic-ai/claude-code)  
[Documentación de Anthropic: Configurar Claude Code](https://docs.claude.com/en/docs/claude-code/setup)