---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Deshabilitar las Citas de Búsqueda Web de LibreChat
translated: true
type: note
---

## Desactivar citas en el modo de búsqueda web de LibreChat

La función de búsqueda web de LibreChat (con tecnología de proveedores como Serper.dev o SearxNG, combinados con raspadores como Firecrawl) incluye automáticamente citas en las respuestas para atribuir las fuentes y mejorar la transparencia. Según la documentación oficial y las discusiones de la comunidad, no existe un interruptor integrado específico para el usuario que desactive las citas de la búsqueda web a nivel de usuario individual. Sin embargo, puedes lograr esto o aproximarte mediante cambios de configuración, principalmente para administradores o quienes alojen la instancia ellos mismos. Aquí te explicamos cómo:

### 1. **Configuración a nivel de administrador (Enfoque recomendado)**
   Si estás ejecutando tu propia instancia de LibreChat (auto-alojada), modifica los archivos de configuración para limitar o eliminar la representación de citas. Las citas se manejan a través de la interfaz y los componentes de búsqueda.

   - **Editar `librechat.yaml` para la configuración de la interfaz**:
     LibreChat utiliza un archivo YAML para la configuración global. Busca la sección `interface`, que controla la visibilidad de las citas (inspirado en los controles de citas de archivos, que pueden extenderse a la búsqueda web).
     - Establece `fileCitations` en `false` para desactivar globalmente los permisos de citas. Aunque esto es explícitamente para búsquedas de archivos, puede influir en la representación de la interfaz de usuario de la búsqueda web en algunas configuraciones.
       ```yaml
       interface:
         fileCitations: false  # Desactiva la visualización de citas para las búsquedas en general
       ```
     - Para la búsqueda web específicamente, en la sección `webSearch`, puedes desactivar o personalizar los proveedores para evitar enlaces detallados a las fuentes:
       ```yaml
       webSearch:
         enabled: true  # Mantener activado, pero ajustar proveedores
         serper:  # O tu proveedor
           enabled: true
           # No hay un indicador directo de 'citations', pero omitir las claves API para raspadores como Firecrawl reduce los extractos/citas detallados
         firecrawl:
           enabled: false  # Desactiva el raspado de contenido, que a menudo genera citas
       ```
     - Reinicia tu instancia de LibreChat después de los cambios. Fuente para la configuración de la interfaz: [Estructura del objeto de interfaz de LibreChat](https://www.librechat.ai/docs/configuration/librechat_yaml/object_structure/interface)[1].

   - **Variables de entorno (Archivo .env)**:
     En tu archivo `.env`, desactiva los modos de depuración o registro que puedan imponer citas, o configura la búsqueda web para un proveedor mínimo.
     - Ejemplo:
       ```
       DEBUG_PLUGINS=false  # Reduce la salida detallada, incluyendo citas
       SERPER_API_KEY=tu_clave  # Usa un proveedor de búsqueda básico sin raspado para menos citas
       FIRECRAWL_API_KEY=  # Déjalo en blanco para desactivar el raspador (sin extractos/citas de página)
       ```
     - Esto cambia las respuestas a resultados de búsqueda solo de resumen sin citas en línea. Configuración completa: [Configuración .env de LibreChat](https://www.librechat.ai/docs/configuration/dotenv)[2].

   - **Personalización del proveedor de búsqueda web**:
     Cambia a un proveedor como SearxNG, que puede configurarse en el lado del servidor para omitir enlaces de origen.
     - Establece `SEARXNG_INSTANCE_URL=tu_url_searxng_minimal` en `.env`.
     - En tu instancia de SearxNG, edita su configuración para suprimir los metadatos de los resultados (por ejemplo, a través de `settings.yml` en SearxNG: deshabilita `reveal_version: false` y personaliza las plantillas para eliminar enlaces).
     - Documentación: [Configuración de Búsqueda Web](https://www.librechat.ai/docs/configuration/librechat_yaml/object_structure/web_search)[3].

### 2. **Soluciones a nivel de usuario (Sin acceso de administrador)**
   Si estás usando un LibreChat alojado (por ejemplo, una instancia pública), las opciones son limitadas ya que las citas a menudo se exigen para garantizar la precisión:
   - **Ingeniería de prompts**: Instruye explícitamente a la IA en tus mensajes, por ejemplo, "Busca en la web pero no incluyas citas o fuentes en tu respuesta." Esto funciona de manera inconsistente ya que la herramienta de búsqueda aún puede agregarlas, pero muchos modelos cumplirán parcialmente.
   - **Desactivar la búsqueda web por completo**: Si las citas son el problema principal, desactiva la búsqueda web por conversación:
     - En la interfaz de chat, evita hacer clic en el botón "Web Search".
     - Para agentes: Al crear/editar un agente, elimina la capacidad `web_search` en la configuración del agente (a través de la interfaz de usuario de Agentes). Fuente: [Documentación de Agentes](https://www.librechat.ai/docs/features/agents)[4].
     - Solicita a los administradores que agreguen un interruptor; las discusiones de la comunidad sugieren esto como una solicitud de función (por ejemplo, [Discusión en GitHub sobre el interruptor de búsqueda web](https://github.com/danny-avila/LibreChat/discussions/7738)[5]).

### 3. **Limitaciones y Notas**
   - Las citas son una parte fundamental de la búsqueda web para garantizar el uso ético de la IA y la trazabilidad, por lo que desactivarlas por completo podría requerir modificaciones de código personalizadas (por ejemplo, editar componentes del frontend como `WebSearchResults.jsx` en el repositorio de GitHub para ocultar elementos de cita).
   - No existe un indicador directo de "desactivar citas" en las versiones actuales (a partir de octubre de 2025). Consulta las actualizaciones en la [Documentación de la función de Búsqueda Web](https://www.librechat.ai/docs/features/web_search)[6], ya que las funciones evolucionan.
   - Si estás auto-alojando, prueba los cambios en un entorno de desarrollo; desactivar los raspadores podría reducir la calidad de la respuesta.
   - Los comentarios de la comunidad (por ejemplo, en Reddit) señalan errores ocasionales con las funciones de búsqueda, pero nada específico sobre las citas: [Hilo de Reddit sobre problemas de LibreChat](https://www.reddit.com/r/LocalLLaMA/comments/1k2hraj/is_it_just_me_or_is_librechat_a_complete_buggy/)[7].

Para soporte oficial, únete al Discord de LibreChat o abre un issue en GitHub con los detalles de tu configuración. Si esto no lo resuelve, ¡proporciona más contexto sobre tu versión de LibreChat o método de alojamiento!

Citas:
[1] https://www.librechat.ai/docs/configuration/librechat_yaml/object_structure/interface
[2] https://www.librechat.ai/docs/configuration/dotenv
[3] https://www.librechat.ai/docs/configuration/librechat_yaml/object_structure/web_search
[4] https://www.librechat.ai/docs/features/agents
[5] https://github.com/danny-avila/LibreChat/discussions/7738
[6] https://www.librechat.ai/docs/features/web_search
[7] https://www.reddit.com/r/LocalLLaMA/comments/1k2hraj/is_it_just_me_or_is_librechat_a_complete_buggy/