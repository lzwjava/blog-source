---
audio: false
generated: true
lang: es
layout: post
title: Complemento Copilot de Visual Studio Code
translated: true
type: note
---

No, el complemento Copilot de Visual Studio Code (VSCode) no puede utilizar una clave API personalizada, como tu clave de Gemini. GitHub Copilot, desarrollado por GitHub (propiedad de Microsoft), es una herramienta de finalización de código con tecnología de IA estrechamente integrada con la infraestructura de GitHub y sus modelos de IA específicos, originalmente basados en Codex de OpenAI. Depende de la autenticación a través de una cuenta de GitHub y una suscripción a Copilot, y no ofrece una opción incorporada para configurarlo con claves API personalizadas de otros proveedores, como Gemini de Google.

Sin embargo, dado que tienes una clave de Gemini, existen formas alternativas de aprovecharla dentro de VSCode:

- **Gemini Code Assist**: Google proporciona un asistente de codificación con tecnología de IA llamado Gemini Code Assist, que tiene una extensión oficial para VSCode. Esta extensión está diseñada para funcionar con los modelos Gemini de Google y es probable que te permita ingresar tu clave API de Gemini para la autenticación. Puedes instalar esta extensión desde el Marketplace de VSCode y configurarla con tu clave para obtener finalización de código impulsada por Gemini.

- **Complementos de Terceros**: También puede haber otras extensiones de VSCode de terceros disponibles en el Marketplace que admitan múltiples proveedores de IA y te permitan usar claves API personalizadas, incluida una para Gemini. Estos complementos te permitirían conectarte a la API de Gemini para obtener sugerencias de código, aunque podrían requerir una configuración adicional.

### Por qué Copilot no admite claves personalizadas
GitHub Copilot es una herramienta propietaria optimizada para su propio ecosistema. Si bien desarrollos recientes han llevado a GitHub a asociarse con Google para integrar modelos Gemini en Copilot, esta integración es gestionada por GitHub y no permite a los usuarios introducir directamente sus propias claves API de Gemini. En su lugar, el acceso a cualquier modelo compatible (incluido Gemini, si está disponible) se proporciona a través del servicio Copilot mismo, bajo el control de GitHub.

### Recomendación Práctica
Si tu objetivo es usar tu clave de Gemini en VSCode, instalar la **extensión Gemini Code Assist** es la opción más directa y oficialmente compatible. Así es como puedes proceder:

1. Abre VSCode.
2. Ve a la vista de Extensiones (`Ctrl+Shift+X` o `Cmd+Shift+X` en macOS).
3. Busca "Gemini Code Assist" (o consulta la documentación oficial de Google para el nombre exacto).
4. Instala la extensión y sigue sus instrucciones de configuración para ingresar tu clave API de Gemini.

Este enfoque garantiza que estás utilizando la herramienta según lo previsto, evitando posibles problemas como violar los términos de servicio o lidiar con modificaciones no compatibles de Copilot.

En resumen, aunque el complemento Copilot de VSCode en sí mismo no puede usar tu clave de Gemini, aún puedes lograr tu objetivo de usar Gemini en VSCode optando por la extensión Gemini Code Assist o un complemento de terceros compatible.