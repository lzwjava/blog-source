---
audio: false
generated: true
lang: es
layout: post
title: Crear una Extensión de VSCode
translated: true
type: note
---

Crear una extensión de Visual Studio Code (VSCode) puede ser una forma gratificante de mejorar tu flujo de trabajo de desarrollo o contribuir a la comunidad. Aquí tienes una guía completa para ayudarte a comenzar a escribir un plugin de VSCode:

### 1. Prerrequisitos
- **Node.js y npm**: Asegúrate de tener Node.js y npm instalados. Puedes descargarlos desde [nodejs.org](https://nodejs.org/).
- **Yeoman y el Generador de Extensiones de VSCode**: Instala Yeoman y el Generador de Extensiones de VSCode globalmente usando npm.

```bash
npm install -g yo generator-code
```

### 2. Configurar tu Entorno de Desarrollo
- **Instalar Visual Studio Code**: Asegúrate de tener VSCode instalado. Puedes descargarlo desde [code.visualstudio.com](https://code.visualstudio.com/).

### 3. Generar una Nueva Extensión
Utiliza el generador Yeoman para crear la estructura de una nueva extensión. Abre una terminal y ejecuta:

```bash
yo code
```

Sigue las indicaciones para configurar tu extensión. Se te preguntará por:
- El tipo de extensión (por ejemplo, Nueva Extensión, Nuevo Tema de Color, etc.)
- El nombre de tu extensión
- Un identificador (por ejemplo, `mi-extension`)
- Una descripción
- Inicializar un repositorio git
- Elegir el lenguaje (TypeScript o JavaScript)
- Instalar las dependencias necesarias

### 4. Entender la Estructura del Proyecto
Tu nueva extensión tendrá la siguiente estructura:
- `.vscode/`: Contiene las configuraciones de lanzamiento para la depuración.
- `src/`: Contiene el código fuente de tu extensión.
- `package.json`: El archivo manifiesto de tu extensión.
- `tsconfig.json`: Archivo de configuración de TypeScript (si usas TypeScript).

### 5. Escribir tu Extensión
- **Activación**: Define cuándo debe activarse tu extensión en `package.json` en el campo `activationEvents`.
- **Puntos de Contribución**: Define lo que tu extensión contribuye a VSCode, como comandos, vistas o lenguajes, en la sección `contributes` de `package.json`.

### 6. Implementar Comandos
Crea comandos que los usuarios puedan invocar. Defínelos en `package.json` e impleméntalos en tu archivo de extensión principal (por ejemplo, `src/extension.ts` o `src/extension.js`).

Ejemplo de un comando en `package.json`:

```json
"contributes": {
    "commands": [
        {
            "command": "extension.sayHello",
            "title": "Say Hello"
        }
    ]
}
```

Implementa el comando en `src/extension.ts`:

```typescript
import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
    let disposable = vscode.commands.registerCommand('extension.sayHello', () => {
        vscode.window.showInformationMessage('Hello, World!');
    });

    context.subscriptions.push(disposable);
}

export function deactivate() {}
```

### 7. Depurar tu Extensión
- Presiona `F5` para abrir una nueva ventana de VSCode con tu extensión cargada.
- Establece puntos de interrupción y usa la consola de depuración para probar tu extensión.

### 8. Empaquetar y Publicar
- **Empaquetar la Extensión**: Usa la herramienta `vsce` para empaquetar tu extensión.

```bash
npm install -g vsce
vsce package
```

- **Publicar en el Marketplace**: Sigue las instrucciones en el [VSCode Marketplace](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) para publicar tu extensión.

### 9. Documentación y Mejores Prácticas
- **Documentación**: Proporciona documentación clara para tu extensión en un archivo `README.md`.
- **Pruebas**: Escribe pruebas para asegurarte de que tu extensión funciona como se espera.
- **Control de Versiones**: Sigue el versionado semántico para los lanzamientos de tu extensión.

### 10. Recursos Adicionales
- **Documentación de la API de VSCode**: [vscode-api](https://code.visualstudio.com/api)
- **Ejemplos de Extensiones**: [vscode-extension-samples](https://github.com/microsoft/vscode-extension-samples)

Siguiendo estos pasos, estarás en el camino correcto para crear una extensión de VSCode funcional y útil. ¡Feliz codificación!