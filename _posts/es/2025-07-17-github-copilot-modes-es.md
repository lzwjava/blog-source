---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast:free
title: Modos de GitHub Copilot Comparados
translated: true
type: note
---

### Resumen

GitHub Copilot ofrece varios modos de asistencia de código en IDEs como VS Code y Visual Studio, incluyendo el Modo Edición (que se alinea con tu descripción de "modo corrección" para seleccionar y reparar líneas o funciones específicas) y el Modo Agente (que maneja ediciones más amplias y autónomas en archivos o proyectos completos). El Modo Edición es preciso y controlado por el usuario, ideal para correcciones específicas, mientras que el Modo Agente actúa como un programador en pareja con IA, razonando a través de tareas complejas y realizando cambios en múltiples archivos sin necesidad de entrada constante.[1][1] Ambos modos mejoran la productividad pero difieren en alcance, autonomía y flujo de trabajo.

### Diferencias Clave

El Modo Edición se centra en fragmentos de código seleccionados por el usuario, proporcionando sugerencias para revisar y aprobar antes de aplicar los cambios. En contraste, el Modo Agente opera a un nivel superior, analizando el contexto completo de la base de código para planificar, ejecutar e iterar en las ediciones de forma autónoma, modificando a menudo archivos completos o componentes relacionados para mantener la coherencia.[2][1] Aquí tienes una comparación lado a lado:

| Característica           | Modo Edición (Modo Corrección)                                                                 | Modo Agente                                                                 |
|--------------------------|--------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| **Alcance**              | Limitado a líneas, funciones seleccionadas o un único archivo. Resaltas código para corregir errores, refactorizar o mejorar partes específicas.[1] | Espacio de trabajo o proyecto completo. Identifica y edita archivos relacionados automáticamente, más allá de lo que seleccionas.[2][3] |
| **Control del Usuario**  | Alto: Sugiere cambios para tu revisión y aprobación explícita. Tú defines exactamente qué editar.[4] | Medio: Aplica ediciones automáticamente pero marca comandos riesgosos (ej., ejecuciones de terminal) para revisión. Tú estableces el objetivo mediante prompts en lenguaje natural.[1][1] |
| **Autonomía**            | Baja: Proporciona sugerencias específicas; no razona entre archivos ni ejecuta acciones independientes.[1] | Alta: Razona paso a paso, ejecuta tests/comandos, detecta errores y se autocorrige. Mantiene el contexto entre sesiones.[2][3] |
| **Tiempo de Respuesta**  | Rápido: Análisis rápido solo de la selección.[2] | Más lento: Analiza el contexto completo del proyecto, lo que puede tomar más tiempo para bases de código grandes.[2] |
| **Ideal Para**           | Correcciones rápidas como depurar una función, optimizar un bucle o reescribir un método sin impacto más amplio.[1] | Tareas complejas como refactorizar entre archivos, generar tests para un módulo, migrar código o construir características desde cero.[3][5] |
| **Ejemplos**             | - Seleccionar una función con errores: "Arregla esta comprobación de nulos."<br>- Resaltar líneas: "Haz esto asíncrono." [2] | - Prompt: "Refactoriza toda la capa de servicio para usar async/await y actualiza todas las dependencias."<br>- O: "Moderniza este proyecto Java a JDK 21 en todos los archivos." [5][6] |
| **Riesgos/Limitaciones** | Riesgo mínimo, ya que los cambios están aislados; pero requiere selección manual para cada corrección.[1] | La mayor autonomía puede llevar a cambios no deseados; revisa siempre los diffs. No es ideal para entornos altamente controlados.[7][4] |

### Casos de Uso y Flujos de Trabajo

- **Modo Edición para Correcciones Específicas**: Úsalo cuando sabes exactamente qué está mal, por ejemplo, seleccionando código propenso a errores en una función para resolver un bug o mejorar el rendimiento. Es como una herramienta de "edición puntual": selecciona el código en tu IDE, solicita a Copilot mediante el chat (ej., "@workspace /fix") y aplica la vista previa del diff. Este modo brilla en el desarrollo iterativo donde quieres mantener el control total y evitar modificar áreas no afectadas. Por ejemplo, en un proyecto .NET, podrías seleccionar un método y pedir "Identifica excepciones de referencia nula y sugiere correcciones" solo para ese fragmento.[2][8] Está disponible en VS Code y Visual Studio con las extensiones de GitHub Copilot.

- **Modo Agente para Ediciones de Proyecto Completo**: Actívalo para cambios holísticos, como cuando necesitas editar archivos completos o coordinar actualizaciones en una base de código. Inicia una sesión en Copilot Chat (ej., "#agentmode" o mediante el menú desplegable), da un prompt de alto nivel como "Encuentra todos los usos de la API obsoleta y migra a la nueva en este proyecto", y observa cómo planifica los pasos: analizando archivos, proponiendo ediciones, ejecutando tests e iterando. Puede crear nuevos archivos, actualizar namespaces o incluso generar secciones de una aplicación. En la modernización de Java, por ejemplo, escanea un proyecto legacy, actualiza las dependencias de Gradle y valida los cambios en múltiples archivos.[5][3] Este modo es particularmente potente para refactorización, búsqueda de errores a escala o automatización de tareas repetitivas como agregar documentación o tests.[6][9]

El Modo Agente se basa en los fundamentos del Modo Edición pero los expande—piensa en Edición como un bisturí para cortes precisos, y en Agente como un cirujano manejando la operación completa.[1] Las instrucciones personalizadas (ej., mediante la configuración de VS Code) pueden guiar al Modo Agente para mantener la coherencia, como hacer cumplir convenciones de nomenclatura en las ediciones.[1]

### Cuándo Elegir Cada Uno

- Opta por el **Modo Edición/Corrección** si tu tarea es localizada (ej., arreglar una única función) para mantener las cosas simples y rápidas.
- Cambia al **Modo Agente** para eficiencia en alcances más grandes, como ediciones de archivos completos o refactorizaciones de múltiples pasos, pero comienza con tareas pequeñas para generar confianza en sus resultados.[2][1] Ambos requieren una suscripción a GitHub Copilot (Pro o superior) y están integrados en VS Code/Visual Studio. Para mejores resultados, combínalos: Usa Edición para correcciones iniciales, luego Agente para propagar los cambios a todo el proyecto.[8] Si estás trabajando con código sensible, revisa cuidadosamente todas las propuestas del Agente para evitar sorpresas.[7]

Citas:
[1] https://github.blog/ai-and-ml/github-copilot/copilot-ask-edit-and-agent-modes-what-they-do-and-when-to-use-they/
[2] https://devblogs.microsoft.com/dotnet/ask-mode-vs-agent-mode/
[3] https://github.blog/ai-and-ml/github-copilot/agent-mode-101-all-about-github-copilots-powerful-mode/
[4] https://github.blog/developer-skills/github/less-todo-more-done-the-difference-between-coding-agent-and-agent-mode-in-github-copilot/
[5] https://github.blog/ai-and-ml/github-copilot/a-step-by-step-guide-to-modernizing-java-projects-with-github-copilot-agent-mode/
[6] https://code.visualstudio.com/docs/copilot/chat/chat-agent-mode
[7] https://www.reddit.com/r/GithubCopilot/comments/1je448f/after_playing_with_agent_mode_i_think_my_favorite/
[8] https://visualstudiomagazine.com/articles/2025/06/18/copilot-compared-advanced-ai-features-in-visual-studio-2022-vs-vs-code.aspx
[9] https://github.blog/ai-and-ml/github-copilot/github-copilot-coding-agent-101-getting-started-with-agentic-workflows-on-github/