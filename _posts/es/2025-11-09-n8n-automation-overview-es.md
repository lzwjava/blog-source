---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Descripción General de la Plataforma de Automatización de Flujos de Trabajo
  n8n
translated: true
type: note
---

n8n (se pronuncia "n-eight-n") es una plataforma de automatización de flujos de trabajo de código abierto diseñada para equipos técnicos y desarrolladores. Te permite conectar diferentes aplicaciones, servicios y APIs para automatizar tareas repetitivas, flujos de datos y procesos complejos sin depender en gran medida de código personalizado, aunque admite código cuando es necesario. Piensa en ella como una alternativa auto-alojada a herramientas como Zapier o Make, pero con más flexibilidad, incluyendo la capacidad de construir agentes de IA de múltiples pasos, integrar cualquier modelo de lenguaje grande (LLM) y ejecutar todo en tu propia infraestructura para una mejor privacidad y control de los datos.

En esencia, n8n utiliza una interfaz visual basada en nodos donde los flujos de trabajo se construyen arrastrando y conectando "nodos" (bloques de construcción que representan desencadenantes, acciones o transformaciones). Tiene licencia fair-code (el código fuente está disponible en GitHub), admite más de 400 integraciones preconstruidas (por ejemplo, Google Sheets, Slack, OpenAI, GitHub) y puede manejar todo, desde notificaciones simples hasta automatizaciones avanzadas impulsadas por IA, como resumir tickets o generar contenido.

### Características Clave
- **Constructor Visual de Flujos de Trabajo**: Arrastra y suelta nodos para configuraciones sin código, con opciones para incrustar JavaScript, Python o incluso bibliotecas npm/Python para lógica personalizada.
- **Integración de IA**: Construye agentes de múltiples pasos con herramientas como LangChain, conéctate a cualquier LLM (local o basado en la nube) y crea interfaces de chat para consultar datos o ejecutar tareas a través de Slack, SMS o voz.
- **Auto-Alojamiento y Seguridad**: Implementación completa on-premise mediante Docker o npm; admite SSO, secretos cifrados, RBAC y registros de auditoría. Sin vendor lock-in—aloja también tus propios modelos de IA.
- **Desarrollo Híbrido**: Combina la interfaz de usuario con código; reproduce datos para pruebas, registros en línea para depuración y más de 1.700 plantillas para inicios rápidos.
- **Escalabilidad**: Funciones empresariales como historial de flujos de trabajo, control de versiones con Git, entornos aislados e incrustación para automatizaciones orientadas al cliente.
- **Ejemplos de Rendimiento**: Empresas como Delivery Hero ahorran más de 200 horas mensuales; StepStone condensa semanas de trabajo en horas.

En comparación con Zapier, n8n es más amigable para los desarrolladores (acceso al código, auto-alojamiento), rentable (núcleo gratuito, sin tarifas por tarea) y centrado en la privacidad (los datos no se enrutan a través de terceros). Es ideal para equipos que manejan datos sensibles en finanzas, salud u operaciones internas.

# Cómo Usar n8n: Guía Completa

Esta guía te lleva a través de todo, desde la configuración hasta el uso avanzado. Usaremos un ejemplo práctico: un monitor de fuentes RSS que envía por correo electrónico nuevos artículos diariamente (ampliable a resúmenes de IA). Se asume un conocimiento técnico básico; n8n se ejecuta en Node.js.

## 1. Instalación y Configuración

n8n es ligero y rápido de iniciar. Prerrequisitos: Node.js (versión 18+ recomendada) para instalaciones locales; Docker para contenedores. Para producción, usa un VPS como DigitalOcean o AWS.

### Inicio Rápido Local (Desarrollo/Pruebas)
1. Abre tu terminal.
2. Ejecuta: `npx n8n`
   - Esto descarga y lanza n8n temporalmente.
3. Accede al editor en `http://localhost:5678` en tu navegador.
   - Inicio de sesión predeterminado: No se necesitan credenciales inicialmente (configúralas más tarde para mayor seguridad).

### Instalación Local Persistente (npm)
1. Instala globalmente: `npm install n8n -g`
2. Inicia: `n8n start`
3. Accede en `http://localhost:5678`.

### Docker (Recomendado para Producción)
1. Extrae la imagen: `docker run -it --rm --name n8n -p 5678:5678 -v ~/.n8n:/home/node/.n8n n8nio/n8n`
   - Esto asigna un volumen para la persistencia de datos.
2. Para configuraciones avanzadas (por ejemplo, base de datos PostgreSQL): Usa `docker-compose.yml` de la documentación.
3. Accede en `http://localhost:5678`.

### Opciones en la Nube
- **n8n Cloud**: Alojamiento gestionado en n8n.io—regístrate, despliega en minutos, comienza gratis con límites.
- **PaaS de Terceros**: Usa Render, Railway o Sevalla (plantillas de un clic). Ejemplo en Sevalla:
  1. Regístrate en sevalla.com.
  2. Selecciona la plantilla "n8n", despliega recursos (por ejemplo, 1 CPU, 1GB RAM).
  3. Obtén una URL como `https://your-n8n.sevalla.app`.

**Consejos**: Para el auto-alojamiento, asegúralo con HTTPS (a través de un proxy inverso como Nginx), establece variables de entorno (por ejemplo, `N8N_BASIC_AUTH_ACTIVE=true`) y haz una copia de seguridad de la carpeta `~/.n8n`. Escala con el modo cola para flujos de trabajo de alto volumen.

## 2. Descripción General de la Interfaz de Usuario

Una vez abierto:
- **Lienzo**: Espacio de trabajo en blanco para flujos de trabajo. Haz clic en "+" para añadir nodos.
- **Panel de Nodos**: Biblioteca buscable de más de 400 nodos (por ejemplo, "Schedule Trigger").
- **Panel de Ejecución**: Muestra el flujo de datos en tiempo real durante las pruebas.
- **Barra Lateral**: Configuración de flujos de trabajo, historial de ejecuciones, plantillas.
- **Barra Superior**: Guardar, activar/desactivar toggle, opciones de compartir/exportar.

Los flujos de trabajo se guardan automáticamente; usa Git para el control de versiones en equipos.

## 3. Conceptos Básicos

- **Flujo de Trabajo**: Una secuencia de nodos conectados que define la lógica de automatización. Los flujos de trabajo activos se ejecutan con desencadenantes; los inactivos son para pruebas.
- **Nodos**: Bloques modulares:
  - **Desencadenantes**: Inician flujos de trabajo (por ejemplo, Schedule para trabajos cron, Webhook para eventos HTTP, RSS Read para fuentes).
  - **Acciones**: Realizan trabajo (por ejemplo, Send Email, HTTP Request para APIs, Function para código personalizado).
  - **Nodos Principales**: IF (condicionales), Merge (combinar datos), Set (manipular variables).
- **Conexiones**: Las flechas entre nodos muestran el flujo de datos (formato JSON). Los datos de un nodo alimentan al siguiente.
- **Expresiones**: Marcadores de posición dinámicos como `{{ $json.title }}` para extraer datos (por ejemplo, el título de un artículo) en los campos. Usa `$now` para marcas de tiempo o `$input.all()` para lotes.
- **Credenciales**: Almacenamiento seguro para claves API/OAuth. Establécelas una vez por servicio (por ejemplo, OAuth de Gmail) y reutilízalas en todos los nodos.
- **Ejecuciones**: Ejecuciones de un flujo de trabajo; visualiza registros, reproduce datos o depura errores.

## 4. Creando Tu Primer Flujo de Trabajo: Paso a Paso

Construyamos "Correo Electrónico de Resumen RSS Diario".

1. **Crear Nuevo Flujo de Trabajo**:
   - Haz clic en "New" > Nómbralo "Resumen RSS".
   - Se abre el lienzo.

2. **Añadir Nodo Desencadenante**:
   - Haz clic en "+" > Busca "Schedule Trigger".
   - Configura: Se activa "Cada Día" a las 9:00 AM (cron: `0 9 * * *`).
   - Prueba: Haz clic en "Execute Node" (se ejecuta una vez ahora).

3. **Añadir Nodo de Obtención de Datos**:
   - Haz clic en "+" después del desencadenante > "RSS Read".
   - URL: `https://blog.cloudflare.com/rss/`.
   - Ejecutar: Obtiene elementos (por ejemplo, JSON con título, enlace, fecha de publicación).

4. **Transformar Datos (Nodo Function Opcional)**:
   - "+" > "Function".
   - Código:
     ```
     // Limitar a los 3 primeros elementos
     return items.slice(0, 3);
     ```
   - Esto ejecuta JS en los datos entrantes.

5. **Añadir Nodo de Acción**:
   - "+" > "Gmail" (o "Email Send" para SMTP).
   - Credenciales: Haz clic en "Create New" > OAuth para Gmail (sigue el flujo de autenticación de Google).
   - Para: Tu correo electrónico.
   - Asunto: `Resumen Diario: {{ $input.first().json.title }}`
   - Mensaje: Bucle sobre los elementos con la expresión:
     ```
     {{#each $input.all()}}
     - {{ $json.title }}: {{ $json.link }} ({{ $json.pubDate }})
     {{/each}}
     ```
   - (Usa una sintaxis similar a Handlebars para los bucles).

6. **Conectar y Probar**:
   - Arrastra flechas: Desencadenante → RSS → Function → Email.
   - "Execute Workflow": Observa el flujo de datos; revisa la bandeja de entrada.
   - Corrige errores: Los nodos rojos resaltan problemas (por ejemplo, credenciales no válidas).

7. **Activar**:
   - Activa el toggle "Active". Ahora se ejecuta diariamente.

Guarda y exporta como JSON para compartir.

## 5. Construyendo Flujos de Trabajo Más Complejos

- **Condicionales**: Añade un nodo "IF" después de RSS: `{{ $json.pubDate }} > {{ $now.minus({days:1}) }}` para filtrar elementos nuevos.
- **Bucles y Lotes**: Usa "Split In Batches" para procesar grandes conjuntos de datos.
- **Manejo de Errores**: Añade un flujo de trabajo "Error Trigger" o "IF" para reintentos. Usa "Set" para registrar errores.
- **Integraciones de API**: Nodo "HTTP Request" para endpoints personalizados (por ejemplo, POST a un webhook de Slack).
- **Manipulación de Datos**: Nodos "Edit Fields" o Function para ajustes de JSON.
- **Pruebas**: Reproduce ejecuciones específicas; simula datos en los nodos.

Ejemplo: Monitor de Twitter
1. Desencadenante: "Twitter Trigger" en menciones.
2. Nodo de IA: "OpenAI" para clasificar el sentimiento.
3. IF: Positivo → Añadir a CRM; Negativo → Alerta en Slack.

## 6. Uso Avanzado y Mejores Prácticas

- **Flujos de Trabajo de IA**: Añade un nodo "AI Agent" > Encadénalo con herramientas (por ejemplo, buscar, resumir). Integra LLMs locales a través del nodo "Ollama".
- **Nodos Personalizados**: Construye mediante JS (tutorial en la documentación); publica en la comunidad.
- **Escalado**: Usa el modo cola (`N8N_WORKER=1`), base de datos externa (PostgreSQL) y webhooks para tiempo real.
- **Seguridad**: Cifra secretos, usa RBAC para equipos, registros de auditoría.
- **Depuración**: Registros en línea en Functions (`console.log(items)`); control de versiones con Git.
- **Trampas Comunes**: Vigila los tipos de datos (todo JSON); maneja los límites de tasa en los nodos; comienza de forma simple antes de usar IA.
- **Extensiones**: Incrusta en aplicaciones, usa plantillas (más de 1700 disponibles) o npm para extras.

Para producción, monitoriza mediante herramientas externas; el auto-alojamiento ahorra costos (frente a los $20+/mes de Zapier).

## Referencias
- [Sitio Oficial de n8n](https://n8n.io/)
- [Documentación de n8n - Instalación](https://docs.n8n.io/hosting/installation/)
- [Guía para Principiantes de freeCodeCamp](https://www.freecodecamp.org/news/a-beginners-guide-to-automation-with-n8n/)
- [Documentación de Flujos de Trabajo de n8n](https://docs.n8n.io/workflows/)
- [Medium: Guía para Dominar n8n](https://medium.com/data-science-collective/mastering-n8n-from-scratch-a-step-by-step-guide-for-beginners-its-easier-than-you-think-2d7ca5d47277)
- [Wikipedia: n8n](https://en.wikipedia.org/wiki/N8n)