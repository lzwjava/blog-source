---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: Soporte Multidirectorio de Claude Code
translated: true
type: note
---

Claude Code, el asistente de codificación impulsado por IA de Anthropic, opera principalmente dentro de su directorio de trabajo inicializado por seguridad y enfoque, pero ahora admite completamente la funcionalidad entre proyectos a través de una característica de múltiples directorios introducida en actualizaciones recientes (por ejemplo, versión 1.0.18 y posteriores). Esto permite que una sola sesión acceda y trabaje con archivos en múltiples proyectos no relacionados o directorios fuera del original, permitiendo tareas como referenciar configuraciones compartidas, integrar código frontend/backend o manejar configuraciones de monorepos sin cambiar de contexto.[1][2][3]

### Cómo Funciona la Funcionalidad entre Proyectos
- **Mecanismo Principal**: Claude Code comienza en un directorio raíz (tu proyecto "principal") pero puede expandir permisos para leer, editar y ejecutar comandos en directorios adicionales. Esto se hace mediante el flag `--add-dir` o el comando interactivo `/add-dir` durante una sesión. Los directorios agregados se tratan como extensiones del espacio de trabajo, permitiendo operaciones de archivo sin interrupciones (por ejemplo, puedes hacer lint de archivos del Proyecto A mientras editas en el Proyecto B).[3][4]
- **Alcance de la Sesión**: Cada adición de proyecto es temporal a menos que se persista mediante configuración. Los Git worktrees pueden permitir sesiones simultáneas en partes de un proyecto para una colaboración más profunda.[5][6]
- **Limitaciones**: Claude Code restringe el acceso a archivos solo a los directorios agregados; no descubrirá automáticamente rutas no relacionadas. Para configuraciones multi-proyecto persistentes (por ejemplo, monorepos), ejecuta desde un directorio principal que contenga subcarpetas.[3][7]
- **Casos de Uso**:
  - **Monorepos**: Agrega subdirectorios para divisiones frontend/backend.[3][5][7][8]
  - **Recursos Compartidos**: Referencia configuraciones o librerías desde un proyecto separado.[3][6]
  - **Colaboración entre Proyectos**: Integra código de librerías o herramientas en diferentes repositorios.[1][3]

### Cómo Instruir a Claude Code para Involucrar Otro Proyecto
Para agregar un proyecto fuera del directorio actual (por ejemplo, `${ruta_de_otro_proyecto}`):

1. **Inicia Claude Code** en tu directorio de proyecto principal (por ejemplo, `cd /ruta/al/proyecto/principal && claude`).
2. **Agrega el Directorio Adicional Interactivamente**:
   - Durante la sesión, escribe `/add-dir /ruta/completa/a/otro/proyecto` o una ruta relativa (por ejemplo, `../otro-proyecto`).
   - Claude Code confirmará el acceso—responde "yes" si se solicita.[2][3][4]
3. **Al Inicio mediante Flag CLI** (para configuración multi-directorio inmediata):
   - Ejecuta: `claude --add-dir /ruta/a/otro/proyecto` (agrega múltiples con flags repetidos).[4][5][7]
4. **Instruye a Bots/Agentes Claude**: Una vez agregado, da instrucciones en lenguaje natural como "Referencia los archivos API del directorio agregado en `/ruta/a/otro/proyecto`" o "Integra esta configuración compartida del Proyecto B." El diseño agéntico de Claude entiende estas solicitudes dentro del contexto expandido.[3][5][6]

### Mejores Prácticas y Consejos
- **Especificación de Rutas**: Usa rutas absolutas para claridad entre entornos. Evita agregar demasiados directorios para prevenir impactos en el rendimiento.[3][7]
- **Configuración del Espacio de Trabajo**: Para equipos, considera archivos de configuración para configuraciones reutilizables. Combina con herramientas como Apidog para pruebas de API entre directorios.[3][8]
- **Solución de Problemas**: Si la resolución de ruta falla, asegura permisos de escritura. Reinicia sesiones para cambios. Para problemas persistentes, revisa los logs o ejecuta desde un directorio de nivel superior.[3][7]
- **Flujos de Trabajo en Equipo**: Usa esto para microservicios o librerías compartidas; sincroniza via Git para control de versiones.[5][6][8]

Esta característica transforma los flujos de trabajo para configuraciones complejas, reduciendo la fricción en comparación con ejecutar sesiones separadas en cada directorio.[3][6] Si encuentras problemas o necesitas ejemplos para herramientas específicas, ¡proporciona más detalles!

Citas:
[1] https://www.reddit.com/r/ClaudeAI/comments/1l896ek/claude_code_v1018_we_can_now_specify_additional/
[2] https://www.threads.com/@boris_cherny/post/DMtFLWOzKAS/video-claude-code-can-now-work-across-multiple-directories-in-a-single-sessiontype-add?hl=en
[3] https://apidog.com/blog/claude-code-multi-directory-support/
[4] https://claudelog.com/faqs/--add-dir/
[5] https://www.anthropic.com/engineering/claude-code-best-practices
[6] https://www.linkedin.com/posts/valokafor_how-to-set-up-claude-code-the-right-way-for-activity-7353146981034201089-dhdX
[7] https://stackoverflow.com/questions/79763754/best-practices-for-multi-project-workspaces-in-claude-code
[8] https://www.siddharthbharath.com/claude-code-the-complete-guide/