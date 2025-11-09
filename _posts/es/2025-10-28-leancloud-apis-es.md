---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: APIs de LeanCloud no Llamadas Uluru
translated: true
type: note
---

No, LeanCloud no denomina su API pública como "Uluru API". Sus APIs oficiales se denominan LeanCloud REST API (para almacenamiento de datos, consultas, etc.), Cloud Engine REST API (para funciones y hooks del lado del servidor) y endpoints específicos de servicios similares, como aquellos para notificaciones push o almacenamiento de archivos. Estos están documentados extensivamente en su sitio para desarrolladores (docs.leancloud.cn) sin ninguna referencia a "Uluru".

Sin embargo, "Uluru" parece ser un nombre en clave interno o temprano asociado con el desarrollo de su producto o SDK. Esto se basa en un paquete npm archivado llamado **uluru-js-sdk** (versión 0.1.0, publicado hace ~12 años bajo la cuenta del publicador "avos"). AVOS Cloud era el nombre original de LeanCloud antes del cambio de marca, y este paquete se describe como un "JavaScript SDK para PAAS" (Plataforma como Servicio), lo que se alinea con los servicios backend de LeanCloud. Es compatible con entornos tanto de navegador como Node.js para funciones principales como operaciones de datos—coincidiendo con las ofertas iniciales de LeanCloud—pero nunca se promocionó públicamente como el SDK principal. Los SDKs actuales se comercializan como "LeanCloud SDK" (por ejemplo, para Java, Python, JavaScript, etc.) y están disponibles en GitHub bajo leancloud/.

Si esto se refiere a algo más reciente o específico (por ejemplo, una herramienta privada/interna), no está documentado públicamente. Para detalles oficiales de la API, consulta la [Documentación de LeanCloud](https://docs.leancloud.cn/en/).