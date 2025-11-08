---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Guía del Portal WiFi de Hoteles Jinjiang
translated: true
type: note
---

El portal WiFi de Jinjiang Hotels (https://portal.jinjianghotels.com.cn/) es un portal cautivo diseñado solo para acceso in situ—no es completamente rastreable públicamente fuera de la red del hotel, por lo que la navegación directa a menudo devuelve páginas vacías o de error. Según informes y guías de usuarios, aquí hay un desglose de su estructura típica de "rutas" (es decir, las principales rutas/endpoints de URL) y cómo acceder a ellas. Esto es común para Vienna Hotels (una marca de Jinjiang) y cadenas similares en China.

### Ruta Principal y Método de Acceso
- **Ruta Principal**: La ruta raíz `/` (es decir, https://portal.jinjianghotels.com.cn/ o http://portal.jinjianghotels.com.cn/).
  - Esta es la página de destino que se carga automáticamente cuando intentas acceder a cualquier sitio web no HTTPS mientras estás conectado al WiFi del hotel.
  - **Cómo Acceder**:
    1. Conecta tu dispositivo al SSID del WiFi del hotel (por ejemplo, "ViennaHotel", "Jinjiang_Free", o "Vienna_Free_WiFi"—sin contraseña inicialmente).
    2. Abre un navegador web y navega a cualquier sitio HTTP (por ejemplo, http://neverssl.com o http://172.16.16.1—la IP de la puerta de enlace local mencionada en tu primera consulta).
    3. Serás redirigido a la página raíz `/` del portal. Si no redirige automáticamente, introduce manualmente `http://172.16.16.1` o la URL del portal (usa HTTP, no HTTPS, ya que los portales cautivos a menudo bloquean o ignoran HTTPS).
  - La página está en chino pero es simple: Muestra la marca del hotel, términos de uso y botones de inicio de sesión. Usa la traducción del navegador (por ejemplo, la integrada en Chrome) para inglés.

### Subrutas/Rutas Conocidas
El portal utiliza una estructura mínima—principalmente una aplicación de una sola página con envíos de formularios en lugar de subrutas profundas. No hay documentación pública que liste todos los endpoints, pero según videos de usuarios e informes de solución de problemas, los comunes incluyen:
- **Ruta de Inicio de Sesión por SMS**: Se maneja a través de un formulario en la raíz `/` (no hay una subruta `/sms` separada; es una petición POST a un endpoint interno como `/auth/sms` o similar).
  - **Cómo Acceder/Usar**: En la página principal, haz clic en el botón de SMS (短信验证). Introduce tu número de teléfono (+86 para China, o formato internacional). Un código llega vía SMS; envíalo para autenticarte. El acceso expira después de 24 horas.
- **Rutas de Inicio de Sesión Social**: Enlaces o iframes a endpoints de terceros, por ejemplo:
  - Inicio de sesión Weibo/QQ: Redirige a `/oauth/weibo` o `/oauth/qq` (subrutas temporales para la devolución de llamada de autenticación).
  - **Cómo Acceder**: Haz clic en el botón social respectivo en la página raíz; se abre una ventana emergente o redirige brevemente.
- **Otras Subrutas Potenciales** (inferidas de sistemas similares; no confirmadas para Jinjiang):
  - `/terms` o `/agreement`: Para ver los términos completos (enlazado desde el pie de página de la página principal).
  - `/logout`: Para desconectar manualmente (rara vez usado).
  - Rutas de error como `/error` o 404 para acceso no válido.

Si estás in situ y necesitas inspeccionar las subrutas (por ejemplo, para las herramientas de desarrollo), abre la consola de desarrollo del navegador (F12) en la página del portal—puede revelar llamadas AJAX a endpoints como `/api/verify` para el envío de SMS.

### Solución de Problemas de Acceso
- **¿No hay Redirección?**: Limpia la caché del navegador, olvida/vuelve a unirte al WiFi, o activa/desactiva brevemente los datos móviles.
- **¿Teléfono Internacional?**: Funciona para la mayoría, pero los códigos pueden retrasarse—pregunta en recepción por un código compartido.
- **Nota de Seguridad**: Todo el tráfico pasa por la puerta de enlace del hotel (rango 172.16.16.x), así que usa VPN después del inicio de sesión.

Para elementos visuales, consulta los videos cortos en Douyin sobre "维也纳酒店 WiFi 登录" que muestran el flujo exacto de la página.

Referencias:  
[Reddit: Issues with WiFi in China Hotels](https://www.reddit.com/r/travelchina/comments/1kjdngn/issues_with_wifi_connection/)  
[Douyin: Vienna Hotel WiFi Steps](https://www.douyin.com/search/%E7%BB%B4%E4%B9%9F%E7%BA%B3%E9%85%92%E5%BA%97Wi-Fi%E8%BF%9E%E6%8E%A5%E6%AD%A5%E9%AA%A4)  
[Douyin: Hotel WiFi Connection Guide](https://www.douyin.com/search/%E9%85%92%E5%BA%97%E6%97%A0%E7%BA%BF%E7%BD%91%E6%80%8E%E4%B9%88%E8%BF%9E%E6%8E%A5)