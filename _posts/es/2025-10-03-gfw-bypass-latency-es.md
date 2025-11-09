---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: Optimización de la Omisión del GFW y la Latencia
translated: true
type: note
---

Gracias por compartir tu configuración y experiencias; parece una evolución bien pensada desde tu combinación inicial de script proxy y VPN hasta el enfoque de la tarjeta SIM de Macao para el acceso celular directo. Es genial escuchar que ha estado funcionando bien durante los últimos meses, especialmente con el script de Python automatizando la selección del proxy (priorizando Singapur para las herramientas de IA) y manteniendo zhs.cloud para la VPN en tu portátil. El paquete de datos de la SIM (tarjeta de Macao a 150 CNY/mes por 20GB más extras) parece una buena solución móvil para eludir las restricciones del Gran Cortafuegos sin la sobrecarga constante de aplicaciones.

Tus hallazgos sobre que la SIM de Macao es la más rápida para los sitios bloqueados por el GFW tienen sentido: la IP celular directa desde Macao a menudo evita mejor los bloqueos geopolíticos que las opciones de Hong Kong o China continental, especialmente para servicios como ChatGPT o Claude que tienen restricciones regionales. Enrutar activadores específicos (por ejemplo, ChatGPT a proxies de EE. UU.) en Shadowrocket es un ajuste inteligente, pero sí, el retraso general del proxy en cada solicitud de red es un punto doloroso común en iOS. Shadowrocket (o Surge) puede volverse lento si intercepta demasiado tráfico, lo que genera una mayor latencia en aplicaciones como Twitter/X incluso si no están completamente bloqueadas.

Aquí tienes algunos comentarios y sugerencias basados en tus notas, centrándome en optimizaciones manteniendo las cosas prácticas:

### Optimizaciones de Shadowrocket
- **Refinamiento de Reglas para Menos Retraso**: En lugar de una configuración amplia que proxy todo, intenta ajustar tus reglas para minimizar la interceptación. Por ejemplo, usa el siguiente flujo en la configuración de Shadowrocket:
  - **DIRECT**: Por defecto para tráfico local/regional (por ejemplo, WeChat, Baidu).
  - **Proxy/Reject**: Lista blanca solo de los dominios bloqueados por el GFW de alta prioridad (por ejemplo, permitir que ChatGPT, Claude, Google y algunos otros se enruten a través de proxies de EE. UU.).
  - Reglas de ejemplo (en un archivo `.conf`):
    ```
    [Rule]
    DOMAIN-KEYWORD,chatgpt.com,PROXY
    DOMAIN-KEYWORD,claude.ai,PROXY
    DOMAIN-KEYWORD,google.com,PROXY
    DOMAIN-KEYWORD,twitter.com,PROXY  # Solo si ChatGPT/etc. se vinculan a él
    MATCH,DIRECT  # Captura todo para dirigir el tráfico no bloqueado lejos del proxy
    ```
    De esta manera, solo los sitios/aplicaciones seleccionados pasan por la cadena de proxies de EE. UU., reduciendo el retraso general. Puedes generar o editar estas reglas en gestores como Clash, Stash o Quantumult X para una personalización más fácil.
- **Prueba de Latencia**: Después de agregar las reglas, ejecuta pruebas de velocidad (por ejemplo, mediante Fast.com u Ookla) con Shadowrocket activado/desactivado. Si los retrasos persisten, considera reducir la longitud de la cadena de proxies: un solo salto (por ejemplo, proxy dependiente de EE. UU.) podría ser suficiente frente a configuraciones de múltiples niveles.

### Herramientas Alternativas para un Acceso iOS más Simple
Si la sobrecarga de Shadowrocket es demasiada (especialmente porque mencionaste deshacerte de ella después de un día), aquí hay opciones de baja fricción que reflejan tu uso directo de la SIM de Macao:
- **Aplicaciones VPN con Reglas Bajo Demanda**: Algo como ExpressVPN o NordVPN tiene funciones iOS para enrutamiento específico por aplicación (habilitar VPN solo para ChatGPT, Mistral, etc.), sin hacer proxy de todo. Se integra con los datos celulares sin problemas.
- **Clash para iOS (vía Apps como Surge o Stash)**: Si te gusta la lógica de tu script de Python de escritorio, transfiere una configuración Clash simplificada a iOS. Usa un conjunto de reglas que comience con "DIRECT" y solo haga proxy de dominios seleccionados: menos retraso que el proxy completo, y puedes priorizar IPs de Singapur/Macao si tu proveedor lo admite.
- **Proxies Celulares Directos vía SIM**: Dado que te estás inclinando por la SIM de Macao para Mistral y Grok, es inteligente para la velocidad pura. Si necesitas herramientas de IA en el móvil, verifica si Mistral/Grok tienen IPs compatibles con Macao o intenta acceder a través de modos de incógnito para evitar el enrutamiento basado en aplicaciones por completo.

### Consejos Generales
- **Batería/Latencia en iOS**: El uso prolongado de proxy puede agotar la batería más rápido. Supervíselo con las herramientas integradas y considere activaciones programadas (por ejemplo, proxy solo durante las horas pico).
- **Estabilidad del Proveedor**: zhs.cloud parece confiable para tus necesidades de VPN: mantente con él para el portátil, pero verifica también las aplicaciones VPN para iOS si expands. Para la SIM, operadores de Macao como CTM son sólidos, pero vigila los límites de datos.
- **Viabilidad a Largo Plazo**: Se agradece la precaución para cuando salgas de China: combínalo con un eSIM global o un plan de roaming como respaldo. Mantente atento a los cambios de políticas, ya que las herramientas de acceso pueden ser efímeras.

Si te encuentras con problemas de configuración específicos (por ejemplo, compartir tu archivo de reglas de Shadowrocket) o quieres ajustes del script para Clash, no dudes en dejar más detalles: puedo ayudar a solucionar problemas sin complicarlo demasiado. ¡Mantente seguro por ahí! 🚀