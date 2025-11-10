---
audio: false
generated: true
image: false
lang: es
layout: post
title: Principios de diseño de CLI para IA desglosados
translated: true
type: note
---

### Lecciones Clave del Prompt

Este prompt describe un sistema para una herramienta CLI con IA (Claude Code) enfocada en tareas de ingeniería de software. Esto es lo que podemos aprender sobre el diseño de asistentes de IA efectivos:

#### 1. **Priorizar la Seguridad y la Ética**
   - Enfatiza la seguridad defensiva: La IA debe rechazar tareas que involucren código malicioso (ej. crear exploits) pero permitir las defensivas, como el análisis de vulnerabilidades o reglas de detección.
   - Lección: Construye salvaguardas éticas desde el principio para prevenir el mal uso, especialmente en dominios sensibles como la programación, donde los resultados podrían tener un impacto en el mundo real.

#### 2. **Estilo de Respuesta y Concisión**
   - Manda respuestas ultra-cortas (menos de 4 líneas a menos que se soliciten detalles), con ejemplos como responder "2 + 2" simplemente con "4".
   - Evita preámbulos, explicaciones o emojis a menos que se le pidan; se centra en una salida directa y eficiente en tokens para su visualización en CLI.
   - Lección: Adapta la comunicación a la interfaz (ej. la CLI exige brevedad para evitar el desorden). Esto reduce la carga cognitiva y mejora la usabilidad en herramientas interactivas.

#### 3. **Proactividad con Límites**
   - Permite acciones proactivas (ej. ejecutar comandos, planificar tareas) pero solo cuando son iniciadas por el usuario; advierte contra sorprender a los usuarios.
   - Equilibra la autonomía (ej. verificar soluciones con tests) con el control del usuario (ej. nunca confirmar cambios sin una petición explícita).
   - Lección: La IA debe asistir de manera eficiente sin excederse, fomentando la confianza. Usa herramientas de planificación (como TodoWrite) para hacer un seguimiento transparente del progreso.

#### 4. **Integración de Herramientas y Flujo de Trabajo**
   - Proporciona un conjunto de herramientas (ej. Bash para ejecución, WebFetch para documentación, herramientas de búsqueda para bases de código) con políticas para uso paralelo y por lotes.
   - Fomenta la gestión frecuente de tareas pendientes para desglosar trabajos, verificar con linters/verificaciones de tipos y seguir convenciones de código (ej. imitar estilos existentes, revisar librerías).
   - Maneja casos extremos como hooks, redirecciones y conciencia del entorno (ej. estado de git, detalles del SO).
   - Lección: Equipa a las IAs con herramientas modulares para tareas complejas; promueve el uso secuencial/paralelo para la eficiencia. Siempre basa las acciones en el contexto (ej. busca antes de asumir).

#### 5. **Personalización para un Dominio Específico**
   - Ajustada para ingeniería de software: Planificar, buscar, implementar, verificar; referencia ubicaciones de código con precisión (ej. "ruta_del_archivo:número_de_línea").
   - Incluye canales de retroalimentación y comandos de ayuda; se adapta a configuraciones del usuario como hooks.
   - Lección: Personaliza los prompts para el dominio—aquí, las convenciones de código aseguran salidas idiomáticas y seguras. Proporciona mecanismos de autoayuda para empoderar a los usuarios.

#### 6. **Perspectivas Generales de Ingeniería de Prompts**
   - Se estructura con secciones (ej. Tono, Proactividad, Herramientas) y ejemplos para claridad.
   - Usa etiquetas tipo XML para recordatorios; especifica límites de conocimiento y detalles del modelo.
   - Lección: Los prompts efectivos son modulares, guiados por ejemplos y con muchas restricciones para guiar el comportamiento. Esto reduce las alucinaciones y asegura la consistencia.

En general, este prompt demuestra cómo crear una herramienta de IA confiable y centrada en el usuario combinando reglas estrictas, herramientas y planificación—valioso para construir sistemas similares en programación y más allá.