---
audio: false
generated: true
lang: es
layout: post
title: Pasar Parámetros Personalizados de JVM en el Complemento Liberty Tools
translated: true
type: note
---

Puedes pasar parámetros personalizados de JVM—como `-Dversion=5.1`—agregándolos a tu configuración de inicio del modo de desarrollo de Liberty en VS Code. Normalmente, esto se hace editando (o creando) el archivo `.vscode/launch.json` en tu proyecto e incluyendo el parámetro bajo una propiedad como `"vmArgs"` (o `"args"` si tu configuración espera argumentos de objetivos de Maven).

Por ejemplo, si estás usando la extensión Liberty Tools con el modo de desarrollo, tu configuración podría verse así:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "type": "liberty",
      "request": "launch",
      "name": "Liberty Dev Mode",
      "goal": "dev",
      "vmArgs": "-Dversion=5.1"
    }
  ]
}
```

### Pasos:
1.  **Abre o Crea la Configuración de Inicio:**
    - En VS Code, abre tu proyecto.
    - Navega a la carpeta `.vscode` y abre (o crea) el archivo `launch.json`.

2.  **Agrega tu Configuración del Modo de Desarrollo:**
    - Agrega una entrada de configuración como se muestra arriba. La clave `"vmArgs"` te permite especificar opciones de JVM que se pasarán al servidor cuando se inicie el modo de desarrollo.

3.  **Guarda y Lanza:**
    - Guarda el archivo.
    - Usa la vista de Ejecutar y Depurar para iniciar la configuración "Liberty Dev Mode".

Si estás usando Maven directamente, también podrías iniciar el modo de desarrollo desde la línea de comandos con:

```bash
mvn liberty:dev -Dversion=5.1
```

Esto pasa la propiedad personalizada a la JVM al iniciar el servidor.

Al configurarlo de esta manera, la extensión Liberty Tools incluirá tu parámetro personalizado (`-Dversion=5.1`) cada vez que inicies el modo de desarrollo.