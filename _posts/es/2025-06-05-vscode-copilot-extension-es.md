---
audio: false
generated: true
lang: es
layout: post
title: Cómo Llamar a GitHub Copilot Desde una Extensión de VSCode
translated: true
type: note
---

GitHub Copilot es un asistente de codificación potente con tecnología de IA integrado en Visual Studio Code (VSCode) e IntelliJ IDEA a través de sus respectivos plugins. Si bien no existe una API REST pública para llamar a Copilot directamente, los desarrolladores pueden interactuar con sus capacidades de manera programática dentro de una extensión de VSCode utilizando la API de Chat de VSCode, la API de Modelo de Lenguaje o interacciones basadas en comandos. Esta publicación de blog explica cómo crear una extensión de VSCode que activa la funcionalidad de chat de Copilot con un prompt personalizado, simulando efectivamente una "llamada a la API" de Copilot, y explica cómo aprovechar el propio Copilot para agilizar el desarrollo.

## Comprendiendo la Integración de Copilot en VSCode

GitHub Copilot no expone una API tradicional (por ejemplo, endpoints REST) para acceso programático directo. En su lugar, su funcionalidad está disponible a través de:
- **API de Chat de VSCode**: Permite a las extensiones crear participantes de chat personalizados que interactúan con el sistema de chat de Copilot para consultas en lenguaje natural.
- **API de Modelo de Lenguaje de VSCode**: Permite a las extensiones acceder a los modelos de lenguaje grande (LLM) de Copilot para tareas como generación o análisis de código.
- **Comandos de VSCode**: Permite activar las funciones integradas de Copilot, como abrir la ventana de chat con un prompt predefinido.

Esta guía se centra en usar el comando `workbench.action.chat.open` para activar la interfaz de chat de Copilot, ya que es la forma más sencilla de integrar las capacidades de Copilot en una extensión.

## Paso a Paso: Construyendo una Extensión de VSCode para Activar el Chat de Copilot

A continuación se muestra una guía paso a paso para crear una extensión de VSCode que abre la ventana de chat de Copilot con un prompt personalizado, "llamando" efectivamente a Copilot para procesar una consulta definida por el usuario.

### 1. Configurar la Extensión de VSCode

1. **Inicializar el Proyecto**:
   - Instala el generador de extensiones de VSCode Yeoman: `npm install -g yo generator-code`.
   - Ejecuta `yo code` y selecciona "New Extension (TypeScript)" para crear una extensión basada en TypeScript.
   - Nombra la extensión, por ejemplo, `copilot-api-caller`.

2. **Configurar `package.json`**:
   - Define un comando para activar el chat de Copilot.
   - Ejemplo de `package.json`:

```json
{
  "name": "copilot-api-caller",
  "displayName": "Copilot API Caller",
  "description": "Triggers GitHub Copilot Chat with a custom prompt",
  "version": "0.0.1",
  "engines": {
    "vscode": "^1.85.0"
  },
  "categories": ["Other"],
  "activationEvents": [
    "onCommand:copilot-api-caller.triggerCopilotChat"
  ],
  "main": "./out/extension.js",
  "contributes": {
    "commands": [
      {
        "command": "copilot-api-caller.triggerCopilotChat",
        "title": "Trigger Copilot Chat"
      }
    ]
  },
  "scripts": {
    "vscode:prepublish": "npm run compile",
    "compile": "tsc -p ./",
    "watch": "tsc -watch -p ./"
  },
  "devDependencies": {
    "@types/vscode": "^1.85.0",
    "@types/node": "^20.2.5",
    "typescript": "^5.1.3"
  }
}
```

   - **Usando Copilot**: Mientras editas `package.json`, Copilot puede sugerir campos como `contributes.commands` o `activationEvents` mientras escribes. Acéptalos con `Tab` para acelerar la configuración.

### 2. Escribir el Código de la Extensión

Crea la lógica de la extensión para registrar un comando que abra el chat de Copilot con un prompt proporcionado por el usuario.

- **Archivo**: `src/extension.ts`
- **Código**:

```typescript
import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
  // Registrar el comando para activar el Chat de Copilot
  let disposable = vscode.commands.registerCommand('copilot-api-caller.triggerCopilotChat', async () => {
    // Obtener la entrada del usuario para el prompt
    const prompt = await vscode.window.showInputBox({
      prompt: 'Introduce tu consulta para GitHub Copilot',
      placeHolder: 'ej., Escribe una función JavaScript para ordenar un array'
    });

    if (prompt) {
      try {
        // Ejecutar el comando para abrir el Chat de Copilot con el prompt
        await vscode.commands.executeCommand('workbench.action.chat.open', prompt);
        vscode.window.showInformationMessage('¡Prompt enviado al Chat de Copilot!');
      } catch (error) {
        vscode.window.showErrorMessage(`Error al activar el Chat de Copilot: ${error}`);
      }
    }
  });

  context.subscriptions.push(disposable);
}

export function deactivate() {}
```

- **Cómo Funciona**:
  - Registra un comando `copilot-api-caller.triggerCopilotChat`.
  - Solicita al usuario una consulta (por ejemplo, "Escribe una función Python para invertir una cadena").
  - Usa `vscode.commands.executeCommand('workbench.action.chat.open', prompt)` para abrir la ventana de chat de Copilot con el prompt.
- **Usando Copilot**: En VSCode, escribe `import * as vscode` y Copilot sugerirá la importación completa. Añade un comentario como `// Registrar un comando para abrir el Chat de Copilot`, y Copilot puede proponer la estructura `vscode.commands.registerCommand`. Para la ejecución del comando, escribe `// Abrir el Chat de Copilot con un prompt`, y Copilot podría sugerir la llamada `executeCommand`.

### 3. Mejorar con Contexto (Opcional)

Para hacer la extensión más potente, incluye contexto del editor, como el código seleccionado, para proporcionar a Copilot información adicional.

- **Código Modificado** (`src/extension.ts`):

```typescript
import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
  let disposable = vscode.commands.registerCommand('copilot-api-caller.triggerCopilotChat', async () => {
    // Obtener el texto seleccionado del editor activo
    const editor = vscode.window.activeTextEditor;
    let context = '';
    if (editor) {
      const selection = editor.selection;
      context = editor.document.getText(selection);
    }

    // Solicitar entrada del usuario
    const prompt = await vscode.window.showInputBox({
      prompt: 'Introduce tu consulta para GitHub Copilot',
      placeHolder: 'ej., Explica este código',
      value: context ? `Respecto a este código: \n\`\`\`\n${context}\n\`\`\`\n` : ''
    });

    if (prompt) {
      try {
        await vscode.commands.executeCommand('workbench.action.chat.open', prompt);
        vscode.window.showInformationMessage('¡Prompt enviado al Chat de Copilot!');
      } catch (error) {
        vscode.window.showErrorMessage(`Error al activar el Chat de Copilot: ${error}`);
      }
    }
  });

  context.subscriptions.push(disposable);
}

export function deactivate() {}
```

- **Cómo Funciona**:
  - Recupera el texto seleccionado del editor activo y lo incluye como contexto en el prompt.
  - Prellena el cuadro de entrada con el código seleccionado, formateado como un bloque de código Markdown.
  - Envía el prompt combinado a la interfaz de chat de Copilot.
- **Usando Copilot**: Comenta `// Obtener el texto seleccionado del editor`, y Copilot puede sugerir `vscode.window.activeTextEditor`. Para el formato, escribe `// Formatear código como markdown`, y Copilot podría proponer la sintaxis de triple comilla invertida.

### 4. Probar la Extensión

1. Presiona `F5` en VSCode para iniciar el Host de Desarrollo de Extensiones.
2. Abre la Paleta de Comandos (`Ctrl+Shift+P` o `Cmd+Shift+P`) y ejecuta `Trigger Copilot Chat`.
3. Introduce un prompt (por ejemplo, "Genera un cliente REST API en TypeScript") o selecciona código y ejecuta el comando.
4. Verifica que la ventana de chat de Copilot se abre con tu prompt y proporciona una respuesta.
5. **Usando Copilot**: Si ocurren errores, añade un comentario como `// Manejar errores para la ejecución del comando`, y Copilot puede sugerir bloques try-catch o mensajes de error.

### 5. Avanzado: Usar la API de Chat de VSCode

Para más control, usa la API de Chat de VSCode para crear un participante de chat personalizado que se integre con los modelos de lenguaje de Copilot, permitiendo el procesamiento de lenguaje natural dentro de tu extensión.

- **Código de Ejemplo** (`src/extension.ts`):

```typescript
import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
  // Registrar un participante de chat
  const participant = vscode.chat.createChatParticipant('copilot-api-caller.myParticipant', async (request, context, stream, token) => {
    stream.markdown('Procesando tu consulta...\n');
    // Usar la API de Modelo de Lenguaje para generar una respuesta
    const model = await vscode.lm.selectChatModels({ family: 'gpt-4' })[0];
    if (model) {
      const response = await model.sendRequest([{ text: request.prompt }], {}, token);
      for await (const chunk of response.stream) {
        stream.markdown(chunk);
      }
    } else {
      stream.markdown('No hay un modelo adecuado disponible.');
    }
  });

  participant.iconPath = new vscode.ThemeIcon('sparkle');
  context.subscriptions.push(participant);
}

export function deactivate() {}
```

- **Cómo Funciona**:
  - Crea un participante de chat (`@copilot-api-caller.myParticipant`) invocable en la vista de Chat de Copilot.
  - Usa la API de Modelo de Lenguaje para acceder al modelo `gpt-4` de Copilot (u otro modelo disponible) para procesar el prompt.
  - Transmite (stream) la respuesta de vuelta a la vista de chat.
- **Usando Copilot**: Comenta `// Crear un participante de chat para Copilot`, y Copilot puede sugerir la estructura `vscode.chat.createChatParticipant`. Para la API de Modelo de Lenguaje, comenta `// Acceder al LLM de Copilot`, y Copilot podría proponer `vscode.lm.selectChatModels`.

### 6. Empaquetar y Desplegar

1. Instala `vsce`: `npm install -g @vscode/vsce`.
2. Ejecuta `vsce package` para crear un archivo `.vsix`.
3. Instala la extensión en VSCode a través de la vista de Extensiones o comparte el archivo `.vsix` con otros.
4. **Usando Copilot**: Añade un comentario como `// Añadir script para empaquetar la extensión` en `package.json`, y Copilot puede sugerir el script `vscode:prepublish`.

## Aprovechando Copilot Durante el Desarrollo

GitHub Copilot puede acelerar significativamente el desarrollo de extensiones:
- **Sugerencias de Código**: Mientras escribes en `src/extension.ts`, Copilot sugiere importaciones, registros de comandos y manejo de errores. Por ejemplo, escribir `vscode.commands.` provoca sugerencias como `registerCommand`.
- **Ingeniería de Prompts**: Usa comentarios claros como `// Activar el Chat de Copilot con un prompt de usuario` para guiar las sugerencias de Copilot. Refina los comentarios si las sugerencias son inexactas.
- **Depuración**: Si la extensión falla, añade comentarios como `// Registrar detalles del error`, y Copilot puede sugerir `console.log` o `vscode.window.showErrorMessage`.

## Limitaciones

- **Sin Acceso Directo a la API**: Copilot no expone una API REST pública. Las API de Chat y Modelo de Lenguaje de VSCode son las interfaces programáticas principales.
- **Autenticación**: Los usuarios deben tener una suscripción activa a Copilot (gratuita o de pago) y haber iniciado sesión en VSCode con una cuenta de GitHub.
- **Alcance de la API de Chat**: La API de Chat está limitada a la interfaz de chat; el acceso directo al motor de finalización de código de Copilot no está disponible de manera programática.
- **Entorno**: Asegúrate de que la extensión cumple con las políticas organizativas respecto a las extensiones personalizadas de VSCode.

## Conclusión

Al usar el sistema de comandos de VSCode o la API de Chat, los desarrolladores pueden "llamar" efectivamente a GitHub Copilot desde una extensión personalizada, permitiendo la interacción programática con sus capacidades de IA. El ejemplo anterior demuestra cómo activar el chat de Copilot con un prompt personalizado, mejorado con contexto del editor, y proporciona una base para integraciones más avanzadas usando la API de Modelo de Lenguaje. Con la asistencia de Copilot durante el desarrollo, crear tales extensiones se vuelve más rápido e intuitivo.

Para una mayor exploración, considera experimentar con la API de Chat para participantes personalizados o integrando contexto adicional del editor para prompts más enriquecidos. ¡Feliz codificación!