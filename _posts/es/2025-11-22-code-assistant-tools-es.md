---
audio: false
generated: true
image: false
lang: es
layout: post
model: google/gemini-3-pro-preview
title: Categorías de Herramientas de Asistente de Código
translated: true
type: note
---

Las **llamadas a herramientas** o **acciones** típicas en un asistente de código potente como Claude Code se centran en permitirle interactuar con un entorno de codificación real y realizar las tareas que haría un desarrollador humano.

Estas llamadas a herramientas se dividen en unas pocas categorías principales:

### 1. Interacción con el Sistema de Archivos y la Base de Código

Estas son esenciales para que el asistente comprenda el proyecto, lea el código existente y realice cambios.

| Herramienta/Acción | Caso de Uso Típico |
| :--- | :--- |
| **`read_file`** (o referencia a archivo como `@nombre_de_archivo`) | Recuperar el contenido de un archivo específico para entender su lógica, dependencias o contexto. |
| **`list_directory`** | Obtener una estructura de archivos o una lista de archivos en un directorio para identificar módulos relevantes o encontrar un archivo específico. |
| **`edit_file` / `write_file`** | La acción central para implementar una solución, refactorizar, añadir una función o corregir un error en el código. |
| **`create_file`** | Escribir nuevos archivos, como un nuevo archivo de prueba, un archivo de configuración o un nuevo componente. |
| **`search_files`** | Encontrar todos los archivos en la base de código que contienen una cadena específica (por ejemplo, un nombre de función, un nombre de clase o un mensaje de error). |

### 2. Ejecución y Depuración

Para verificar su trabajo, corregir errores y obtener retroalimentación en tiempo real, el asistente necesita ejecutar comandos.

| Herramienta/Acción | Caso de Uso Típico |
| :--- | :--- |
| **`bash` / `run_command`** | Ejecutar comandos de shell como ejecutar una compilación (`npm build`), ejecutar pruebas (`pytest`, `npm test`), aplicar linter al código (`eslint`) o ejecutar un script. |
| **`code_interpreter`** | Ejecutar un pequeño fragmento de código en un entorno aislado para calcular algo rápidamente, probar una función de una librería o analizar un pequeño conjunto de datos. |

### 3. Control de Versiones (Git)

Un asistente de codificación con capacidades de agente puede gestionar el flujo de trabajo de desarrollo interactuando con Git.

| Herramienta/Acción | Caso de Uso Típico |
| :--- | :--- |
| **`git status`** | Comprobar el estado actual del directorio de trabajo. |
| **`git diff`** | Ver los cambios que se han realizado para revisar su propio trabajo. |
| **`git commit`** | Guardar los cambios en el repositorio, a menudo con un mensaje de commit generado automáticamente. |
| **`git checkout`** | Cambiar de rama o descartar cambios no confirmados. |
| **`create_pull_request`** | Automatizar el paso final de una función o corrección. |

### 4. Información Externa

Para obtener información actualizada, documentación o conectar con servicios externos, se utilizan herramientas especializadas.

| Herramienta/Acción | Caso de Uso Típico |
| :--- | :--- |
| **`web_search`** | Buscar la sintaxis más reciente, leer documentación oficial de una API o encontrar guías de solución de problemas para un error específico. |
| **APIs Personalizadas / Servidores MCP** | Conectar con servicios externos usando el Model Context Protocol (MCP), como obtener datos de Google Drive, interactuar con una base de datos (PostgreSQL) o enviar un mensaje a una herramienta de comunicación (Slack). |

En esencia, estas "llamadas a herramientas" permiten que el Modelo de Lenguaje Grande (LLM) se transforme de un generador de texto en un **agente** completo que puede observar su entorno (leer archivos, ejecutar comandos), pensar (planificar el trabajo) y actuar (editar archivos, confirmar código).

¿Te gustaría ver un ejemplo paso a paso de cómo un asistente de código podría usar estas herramientas para corregir un error simple?