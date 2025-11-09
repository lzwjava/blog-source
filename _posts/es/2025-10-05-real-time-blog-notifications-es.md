---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Notificaciones de Telegram para Visitas al Blog en Tiempo Real
translated: true
type: note
---

Sí, puedes configurar un sistema para analizar los registros o el tráfico de Cloudflare casi en tiempo real y enviar notificaciones de Telegram por cada visita al blog, pero no es sencillo solo con los registros de análisis estándar. Los análisis de Cloudflare son mayormente agregados (por ejemplo, resúmenes diarios/semanales), e incluso su función Logpush (que exporta registros) procesa datos por lotes cada 1-5 minutos, lo que la hace inadecuada para alertas instantáneas por visita. Instant Logs ofrece transmisión en tiempo real, pero requiere un plan Business o Enterprise y necesitaría procesamiento personalizado (por ejemplo, a través de WebSocket y un script) para activar mensajes de Telegram— eso es excesivo para la mayoría de usuarios.

El enfoque más práctico y en tiempo real es usar **Cloudflare Workers** para interceptar cada solicitud entrante a tu blog. Esto ejecuta código serverless en cada visita, permitiéndote registrar el evento y enviar inmediatamente un mensaje de Telegram a través de su API. Es gratuito para tráfico bajo (hasta 100k solicitudes/día), pero los blogs con mucho tráfico podrían alcanzar límites o generar costos—además, recibirías spam con notificaciones, así que considera filtrar (por ejemplo, solo para IPs únicas o páginas específicas).

### Pasos Rápidos de Configuración
1. **Crea un Bot de Telegram**:
   - Envía un mensaje a @BotFather en Telegram, usa `/newbot` para crear uno y anota el token del bot (ej. `123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11`).
   - Inicia un chat con tu bot, luego envía un mensaje a @userinfobot para obtener tu ID de chat (ej. `123456789`).
   - Prueba a enviar un mensaje via curl:
     ```
     curl -X POST "https://api.telegram.org/bot<TU_TOKEN_DE_BOT>/sendMessage" \
     -H "Content-Type: application/json" \
     -d '{"chat_id":"<TU_ID_DE_CHAT>","text":"¡Visita de prueba!"}'
     ```

2. **Crea un Cloudflare Worker**:
   - Inicia sesión en tu panel de Cloudflare > Workers & Pages > Create application > Create Worker.
   - Nómbralo (ej. `blog-visit-notifier`) e implementa la plantilla por defecto.

3. **Añade el Código de Notificación**:
   - Edita el código del worker para interceptar solicitudes y enviar a Telegram. Aquí un ejemplo básico (reemplaza los marcadores de posición):
     ```javascript
     export default {
       async fetch(request, env) {
         // Opcional: Registrar o filtrar la visita (ej. solo para la página principal de tu blog)
         const url = new URL(request.url);
         if (url.pathname !== '/') {  // Ajusta la ruta según sea necesario
           return fetch(request);  // Omitir páginas que no son del blog
         }

         // Enviar mensaje de Telegram (async para no bloquear)
         const message = `¡Nueva visita a ${url.origin}! IP: ${request.headers.get('cf-connecting-ip')}, Agente de Usuario: ${request.headers.get('user-agent')}`;
         await fetch(`https://api.telegram.org/bot${env.TELEGRAM_BOT_TOKEN}/sendMessage`, {
           method: 'POST',
           headers: { 'Content-Type': 'application/json' },
           body: JSON.stringify({
             chat_id: env.TELEGRAM_CHAT_ID,
             text: message,
             parse_mode: 'HTML'  // Para formateo si es necesario
           })
         }).catch(err => console.error('Error al enviar por Telegram:', err));

         // Proxy de la solicitud original a tu blog
         return fetch(request);
       }
     };
     ```
     - Esto se ejecuta en cada solicitud coincidente, registra información básica del visitante y la envía via Telegram sin retrasar la carga de la página.

4. **Configura las Variables de Entorno**:
   - En la configuración del worker > Variables > Añadir:
     - `TELEGRAM_BOT_TOKEN`: Tu token de bot.
     - `TELEGRAM_CHAT_ID`: Tu ID de chat.
   - Guarda y reimplementa.

5. **Enruta el Worker a Tu Blog**:
   - En la configuración de Workers > Triggers > Add route.
   - Configúralo para el dominio/ruta de tu blog (ej. `tublog.com/*`).
   - Esto asegura que el worker se ejecute en cada visita antes de llegar a tu servidor de origen.

6. **Prueba y Monitoriza**:
   - Visita tu blog— deberías recibir un ping de Telegram al instante.
   - Revisa los registros del worker en el panel para ver errores. Si alcanzas límites de tasa (ej. 30 msg/seg de Telegram), añade debouncing con KV storage.

### Alternativas Si Workers No Son Adecuados
- **Para Análisis de Registros por Lotes**: Usa Logpush para exportar registros de solicitudes HTTP a un servicio como AWS S3 o Google Pub/Sub, luego canalízalos a una herramienta como Zapier o n8n para alertas de Telegram (ej. resumir visitas por hora). Aunque no es en tiempo real.
- **Integraciones**: Herramientas como Albato o n8n pueden conectar webhooks de Cloudflare a Telegram para eventos más amplios, pero no por visita.
- **Limitaciones**: Los Workers gratuitos tienen 10ms de tiempo de CPU por solicitud—suficiente para esto, pero escala si es necesario. Evita en sitios de alto tráfico sin limitación.

Esta configuración convierte tu tráfico de Cloudflare en alertas instantáneas y procesables. Si necesitas ajustes de código o ayuda con errores, ¡comparte más detalles!

[Documentación de Cloudflare Workers](https://developers.cloudflare.com/workers/)  
[API de Bots de Telegram](https://core.telegram.org/bots/api)  
[Instant Logs de Cloudflare](https://developers.cloudflare.com/logs/instant-logs/)